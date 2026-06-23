# GCD Organization Setup

## Operator-Provisioned Organization Model

In Google Cloud Dedicated (GCD), you cannot self-create organizations. When you onboard, the operator provisions a new empty organization for you. You receive a **bootstrap ID** from a special GCD identity provider, along with sign-in instructions. This bootstrap ID grants initial administrator access so you can complete the setup steps described below.

Your organization must then be configured with projects, networks, and other resources before it can be used.

## Step 1 - Set Up an Identity Provider

GCD uses **Workforce Identity Federation** (WIF) for identity management. You bring your own identity provider (IdP) rather than using Google-managed identities. WIF supports any IdP that implements OpenID Connect (OIDC) or SAML 2.0, including:

- Google Workspace
- Microsoft Entra ID
- Active Directory Federation Services (AD FS)
- Okta

### Identity Provider Setup Procedure

1. **Sign in with your bootstrap ID** to access the GCD console.

2. **Grant your bootstrap ID the IAM Workforce Pool Admin role:**
   - Navigate to IAM & Admin in the GCD console.
   - Edit your bootstrap principal and add the "IAM Workforce Pool Admin" role.

3. **Configure Workforce Identity Federation:**
   - Navigate to IAM > Workforce Identity Federation.
   - Create a new workforce identity pool.
   - Add your IdP to the pool (follow provider-specific guides for Entra ID, Okta, etc.).
   - You **must** set the `google.posix_username` attribute mapping (required for SSH):

   ```
   google.subject = assertion.subject
   google.posix_username = assertion.attributes['username']
   google.groups = assertion.attributes['groups']
   ```

4. **Create a new Organization Administrator** using an identity from your IdP. Grant this identity both the "Organization Administrator" and "IAM Workforce Pool Admin" roles. Use the following principal format:

   ```
   principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/USERNAME
   ```

   Or for a group (recommended):

   ```
   principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/group/GROUP_EMAIL
   ```

5. **Sign out and sign back in** with the newly configured administrator ID. The bootstrap ID is no longer needed.

## Step 2 - Configure the Organization

There are three main configuration paths depending on your needs.

### Path A - Minimal Setup (Exploration Only)

For trying out GCD features before a full setup. Creates a single project and VPC network - not for production use.

**Prerequisites:** IdP configured, Google Cloud CLI set up.

**Steps:**

1. Create a project in your organization.
2. Create and configure a VPC network:

```bash
gcloud compute networks create default
gcloud compute firewall-rules create default-allow-internal \
  --allow=tcp:1-65535,udp:1-65535,icmp --source-ranges 10.128.0.0/9
gcloud compute firewall-rules create default-allow-ssh --allow=tcp:22
gcloud compute firewall-rules create default-allow-rdp --allow=tcp:3389
gcloud compute firewall-rules create default-allow-icmp --allow=icmp
```

Note: Unlike standard Google Cloud, GCD projects do **not** have a default VPC network. You must create one manually.

### Path B - Basic Setup with Fabric FAST ("Starter")

For smaller organizations, startups, or proof-of-concepts. Uses the Fabric FAST "starter" configuration to create a usable organization in a single step. A single team or engineer manages the entire stack.

**What you get:**

- Two environment folders (dev and prod), tagged for cost tracking and policies
- Two projects per folder: a network project and an application project
- One VPC network per folder with a subnet and basic firewall rules (including IAP login)
- One top-level management project (`prod-iac-core-0`) for Terraform state, service accounts, and audit logs

**Dataset:** `starter-gcd`

### Path C - Enterprise Setup with Fabric FAST ("Classic")

Recommended for most enterprise users. Uses staged Terraform deployment with the "classic" configuration, providing a deep, enterprise-grade folder hierarchy with separation of duties between teams.

**Fabric FAST stages:**

| Stage | Purpose |
|---|---|
| Organization setup | Bootstrap, resource hierarchy, IAM, org policies |
| VPC-SC | VPC Service Controls configuration |
| Networking | Centralized network resources (hub-and-spoke, VPN, NVA, NCC options) |
| Project factory | YAML-based folder and project management |
| Security | Centralized security (Cloud KMS and related resources) |

Only the Organization setup stage is required - all others are optional.

**Dataset:** `classic-gcd`

### Comparing Starter vs Classic

| Aspect | Classic | Starter |
|---|---|---|
| Execution | Sequential stages (0 through 3) | Everything in a single Stage 0 |
| Folder structure | Deep, enterprise-grade tree (Common, Networking, Security, Tenants) | Flat structure (Dev, Prod) |
| Separation of duties | Different teams for networking, security, workloads | Single team manages everything |
| Networking | Hub-and-spoke, cross-region routing, VPC-SC | Simple isolated Shared VPCs per environment |

## Fabric FAST Setup Procedure (Paths B and C)

The setup steps below apply to both the basic and enterprise paths. The key difference is the dataset you select.

### Prerequisites

- IdP configured and signed in with administrator ID
- Google Cloud CLI configured for GCD
- Git and Terraform (minimum version 1.12) installed
- Organization ID (find it with `gcloud organizations list`)
- Administrator principal identifier
- Essential contact email address

### 1. Grant Required IAM Permissions

```bash
export FAST_PRINCIPAL="PRINCIPAL_ID"
export FAST_ORG_ID="ORG_ID"

export FAST_ROLES="\
roles/billing.admin \
roles/logging.admin \
roles/iam.organizationRoleAdmin \
roles/orgpolicy.policyAdmin \
roles/resourcemanager.folderAdmin \
roles/resourcemanager.organizationAdmin \
roles/resourcemanager.projectCreator \
roles/resourcemanager.tagAdmin \
roles/owner"

for role in $FAST_ROLES; do
  gcloud organizations add-iam-policy-binding $FAST_ORG_ID \
    --member $FAST_PRINCIPAL --role $role --condition None
done
```

### 2. Create a Temporary Project

Fabric FAST requires at least one existing project because org policy services are not available at the organization root during initial setup.

```bash
# After creating a project in the console or CLI:
gcloud config set project PROJECT_ID

gcloud services enable \
  bigquery.googleapis.com \
  cloudbilling.googleapis.com \
  cloudresourcemanager.googleapis.com \
  essentialcontacts.googleapis.com \
  iam.googleapis.com \
  logging.googleapis.com \
  orgpolicy.googleapis.com \
  serviceusage.googleapis.com
```

This project can be deleted after setup is complete.

### 3. Clone and Navigate to Fabric FAST

```bash
git clone https://github.com/GoogleCloudPlatform/cloud-foundation-fabric.git
cd cloud-foundation-fabric/fast/stages/0-org-setup
```

### 4. Create the Providers File

Create `providers.tf` in the `0-org-setup` directory to target GCD API endpoints:

```hcl
provider "google" {
  universe_domain = "apis-berlin-build0.goog"
}

provider "google-beta" {
  universe_domain = "apis-berlin-build0.goog"
}
```

### 5. Configure the Dataset

**For basic (starter) setup** - create `terraform.tfvars`:

```hcl
factories_config = {
  dataset = "datasets/starter-gcd"
}
```

Then edit `datasets/starter-gcd/defaults.yaml` with your values:

```yaml
projects:
  defaults:
    prefix: PREFIX
    locations:
      logging: global
      storage: u-germany-northeast1
    overrides:
      universe:
        domain: apis-berlin-build0.goog
        prefix: eu0
        forced_jit_service_identities:
          - compute.googleapis.com
        unavailable_service_identities:
          - dns.googleapis.com
          - monitoring.googleapis.com
          - networksecurity.googleapis.com
context:
  email_addresses:
    gcp-organization-admins: CONTACT_EMAIL
  iam_principals:
    gcp-organization-admins: ADMIN_ID
  locations:
    primary: u-germany-northeast1
```

**For enterprise (classic) setup** - follow the instructions in the [README-GCD](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/blob/master/fast/stages/0-org-setup/README-GCD.md) to switch to `classic-gcd` and configure.

### 6. Apply Terraform

```bash
terraform init
terraform apply
```

For enterprise setup, continue applying additional stages (networking, security, project factory) as needed. Additional stages do not require GCD-specific customization.

## Key Configuration Values for GCD

| Value | Description |
|---|---|
| Universe domain | `apis-berlin-build0.goog` |
| Universe prefix | `eu0` |
| Primary region | `u-germany-northeast1` |
| Console URL | `console.cloud.berlin-build0.goog` |
| Starter dataset | `datasets/starter-gcd` |
| Classic dataset | `classic-gcd` |
| Terraform minimum version | 1.12 |

## Important Notes

- Fabric FAST is the only supported landing zone Terraform for GCD. You can adapt your own Terraform, but review the key differences between GCD and standard Google Cloud carefully.
- GCD projects do not have default VPC networks - you must create them.
- The `google.posix_username` WIF attribute mapping is mandatory for SSH access.
- A "hardened" Fabric FAST organization option exists with additional security controls but has not yet been customized for GCD. You can use it as a source for specific controls.
- Project IDs in GCD receive an automatic universe-specific prefix in addition to any prefix you configure.
