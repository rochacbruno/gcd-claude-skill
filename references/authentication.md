# Authentication for Google Cloud Dedicated (GCD)

## Critical Difference: No Cloud Identity

GCD does **not** use Google Cloud Identity for user management. Instead, all human user
authentication is handled through **Workforce Identity Federation**, which lets you bring
your own external identity provider (IdP). Supported IdPs include any provider that
implements OpenID Connect (OIDC) or SAML 2.0 - for example, Google Workspace, Microsoft
Entra ID, Active Directory Federation Services (AD FS), and Okta.

For programmatic (non-human) access, GCD uses **service accounts** managed by IAM, just
like standard Google Cloud. For workloads running outside GCD, **Workload Identity
Federation** enables authentication without service account keys.

### Principal types summary

| Principal type | Use case |
|---|---|
| Workforce Identity Federation user | Human users signing in via an external IdP |
| Service account | Programmatic/workload access within GCD |
| Workload Identity Federation principal | Workloads running outside GCD (other clouds, on-prem) |

## Universe Domain Requirement

GCD operates in its own universe domain. You **must** set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN`
environment variable before using client libraries or tools:

```bash
export GOOGLE_CLOUD_UNIVERSE_DOMAIN="apis-berlin-build0.goog"
```

This tells client libraries and the gcloud CLI to route requests to the GCD-specific
API endpoints instead of the public Google Cloud endpoints. Without this variable, API
calls will fail or be routed incorrectly.

The GCD console URL is `https://console.cloud.berlin-build0.goog/`.

### Key GCD-specific endpoints

| Service | Endpoint |
|---|---|
| IAM Credentials | `https://iamcredentials.apis-berlin-build0.goog` |
| Security Token Service (STS) | `https://sts.apis-berlin-build0.goog` |
| Resource Manager | `https://cloudresourcemanager.apis-berlin-build0.goog` |
| Service account email format | `NAME@PROJECT.eu0.iam.gserviceaccount.com` |

## Identity Provider Setup

Before any user can authenticate, an organization administrator must configure the IdP.

### Bootstrap process

1. You receive a **bootstrap ID** from Google - a temporary identity from a special
   GCD IdP that grants initial access.
2. Sign in to the GCD console at `https://console.cloud.berlin-build0.goog/` with the
   bootstrap ID.
3. Grant the bootstrap ID the **IAM Workforce Pool Admin** role (it already has
   Organization Administrator).
4. Create a **workforce identity pool** under IAM > Workforce Identity Federation.
5. Configure your IdP provider within the pool (OIDC or SAML 2.0). You **must** set the
   `google.posix_username` attribute mapping (required for SSH):

```
google.subject = assertion.subject
google.posix_username = assertion.attributes['username']
google.groups = assertion.attributes['groups']
```

6. Grant a user or group from your IdP the **Organization Administrator** and **IAM
   Workforce Pool Admin** roles, using the principal format:

```
principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/USERNAME
```

Or for a group:

```
principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/group/GROUP_EMAIL
```

7. Sign out and sign back in with the new administrator identity. The bootstrap ID is
   no longer needed.

## Authentication Methods

### 1. gcloud CLI authentication

Install the gcloud CLI, then sign in with your federated identity:

```bash
# Sign in with Workforce Identity Federation credentials
# Follow the provider-specific instructions for your IdP
gcloud auth login

# Initialize the CLI
gcloud init
```

After sign-in, all gcloud commands use the authenticated principal. You can generate
access tokens for REST calls:

```bash
# Print an access token for use in REST requests
gcloud auth print-access-token
```

For service account impersonation via gcloud:

```bash
# One-off command with impersonation
gcloud storage buckets list --impersonate-service-account=SA_EMAIL

# Set impersonation as default for all commands
gcloud config set auth/impersonate_service_account SA_EMAIL

# Print an access token for an impersonated service account
gcloud auth print-access-token --impersonate-service-account=SA_EMAIL
```

### 2. Application Default Credentials (ADC)

ADC is the recommended strategy for authenticating client libraries automatically. ADC
searches for credentials in this order:

1. **`GOOGLE_APPLICATION_CREDENTIALS` environment variable** - points to a credential
   JSON file (Workforce Identity Federation config, Workload Identity Federation config,
   or service account key).
2. **Local ADC file** - created by `gcloud auth application-default login`, stored at:
   - Linux/macOS: `$HOME/.config/gcloud/application_default_credentials.json`
   - Windows: `%APPDATA%\gcloud\application_default_credentials.json`
3. **Attached service account** - retrieved from the metadata server when running on
   GCD compute resources.

Important: gcloud credentials and ADC credentials are **separate**. Logging into gcloud
does not automatically configure ADC.

#### Set up ADC for local development

**Option A: User credentials (Workforce Identity Federation)**

```bash
# First, sign in to gcloud with your federated identity
gcloud auth login

# Then create ADC credentials
gcloud auth application-default login
```

**Option B: Service account impersonation (recommended for consistent environments)**

Requires the `roles/iam.serviceAccountTokenCreator` role on the target service account.

```bash
gcloud auth application-default login --impersonate-service-account SERVICE_ACCT_EMAIL
```

Supported languages for impersonation-based ADC: C#, C++, Go, Java, Node.js, PHP,
Python, Ruby, Rust.

**Option C: Service account key (least recommended)**

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
```

Service account keys are persistent credentials and present a security risk if
compromised. Prefer impersonation or attached service accounts instead.

#### Set up ADC for production (on GCD compute resources)

Attach a user-managed service account to the resource (Compute Engine VM, GKE pod, etc.).
ADC automatically discovers credentials via the metadata server. Steps:

1. Create a user-managed service account.
2. Grant it the minimum necessary IAM roles (principle of least privilege).
3. Attach the service account to the compute resource.

### 3. Client library authentication

Client libraries automatically use ADC. Set up ADC for your environment, set
`GOOGLE_CLOUD_UNIVERSE_DOMAIN`, install the relevant client library, then create a
client with no explicit credentials:

**Python example:**

```python
from google.cloud import storage

storage_client = storage.Client(project="your-project-id")
buckets = storage_client.list_buckets()
for bucket in buckets:
    print(bucket.name)
```

**Go example:**

```go
client, err := storage.NewClient(ctx)
if err != nil {
    return fmt.Errorf("NewClient: %w", err)
}
defer client.Close()
```

**Node.js example:**

```javascript
const {Storage} = require('@google-cloud/storage');
const storage = new Storage({projectId});
const [buckets] = await storage.getBuckets();
```

The client library handles token acquisition and refresh automatically.

### 4. REST API authentication

**Using gcloud credentials:**

```bash
curl -X GET \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  "https://cloudresourcemanager.apis-berlin-build0.goog/v3/projects/PROJECT_ID"
```

**Using ADC credentials:**

```bash
curl -X GET \
  -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  "https://cloudresourcemanager.apis-berlin-build0.goog/v3/projects/PROJECT_ID"
```

**Using the metadata server (from GCD compute resources):**

```bash
# Get token from metadata server
curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" \
  -H "Metadata-Flavor: Google"

# Use token in request
curl -X GET \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  "https://cloudresourcemanager.apis-berlin-build0.goog/v3/projects/PROJECT_ID"
```

If an API requires a quota project, include the `x-goog-user-project` header:

```bash
-H "x-goog-user-project: PROJECT_ID"
```

## Service Account Impersonation

Service account impersonation lets an authenticated principal (user or another service
account) request short-lived credentials for a target service account. This is more secure
than service account keys because credentials are temporary and require prior
authentication.

### Prerequisites

- Enable the **Service Account Credentials API** (`iamcredentials.googleapis.com`).
- The calling principal needs the **Service Account Token Creator** role
  (`roles/iam.serviceAccountTokenCreator`) on the target service account. This is
  required even if the caller has the Owner role.

### Methods

- **gcloud flag**: `--impersonate-service-account=SA_EMAIL` on any gcloud command.
- **gcloud default config**: `gcloud config set auth/impersonate_service_account SA_EMAIL`.
- **ADC with impersonation**: `gcloud auth application-default login --impersonate-service-account SA_EMAIL`.
- **Programmatic**: Use the IAM Credentials API to generate short-lived tokens directly.

## Token Types

GCD uses several token types:

| Token | Lifetime | Use |
|---|---|---|
| Service account access token | 5 min - 12 hours (default 1 hour) | Authenticate API calls with a service account |
| Service account JWT | Up to 1 hour | Self-signed token, no authorization server needed |
| Federated access token | Up to 1 hour (workforce) or matches external token (workload) | Authenticate workforce/workload identity pool principals |
| ID token | 1 hour | Identify users, service-to-service auth |

All access tokens are short-lived bearer tokens. They cannot be revoked and remain valid
until expiry.

## Security Considerations

### Multi-factor authentication (MFA / 2SV)

GCD requires 2-step verification (2SV) for console access. If your organization uses a
third-party IdP, you can use the 2SV mechanism provided by that IdP. 2SV enforcement
does not directly affect service accounts, but affects users impersonating service
accounts.

### Reauthentication

- Google Workspace session length can be configured by administrators. When sessions
  expire, ADC credentials also expire and must be refreshed with
  `gcloud auth application-default login`.
- Sensitive actions (billing changes, IAM policy changes at org/folder/project level)
  require reauthentication if more than 15 minutes have elapsed. This applies only to
  Google-managed accounts - users federated via Workforce Identity Federation are exempt.

### Credential validation for external sources

When accepting credential configurations from external sources, validate these fields:

| Field | Expected value |
|---|---|
| `service_account_impersonation_url` | `https://iamcredentials.apis-berlin-build0.goog/v1/projects/-/serviceAccounts/SA_EMAIL:generateAccessToken` |
| `token_url` | `https://sts.apis-berlin-build0.goog/v1/token` |

For service account keys from external sources, use type-specific credential loaders
(e.g., `ServiceAccountCredentials.fromStream()` in Java) rather than generic loaders, and
verify the `type` field equals `service_account`.

## Quick Reference: Environment Variables

| Variable | Purpose |
|---|---|
| `GOOGLE_CLOUD_UNIVERSE_DOMAIN` | **Required.** Set to `apis-berlin-build0.goog` |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to a credential JSON file for ADC |
| `GOOGLE_EXTERNAL_ACCOUNT_ALLOW_EXECUTABLES` | Set to `1` to allow executable-based credential sources |

## Decision Tree: Choosing an Authentication Method

1. **Running on a GCD compute resource?**
   - On GKE: Use Workload Identity Federation for GKE.
   - On other GCD resources (Compute Engine, etc.): Attach a service account.
2. **Local development, no service account needed?**
   - Use `gcloud auth application-default login` with your Workforce Identity Federation
     credentials.
3. **Local development, service account needed for consistency?**
   - Use `gcloud auth application-default login --impersonate-service-account SA_EMAIL`.
4. **Workload running outside GCD (other cloud, on-prem)?**
   - Supports workload identity federation? Configure Workload Identity Federation.
   - Does not support federation? Create a service account key (last resort).
