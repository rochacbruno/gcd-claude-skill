# Google Cloud Dedicated (GCD) & Cloud de Confiance (S3NS) Developer Guide

This reference covers the essential setup and development patterns for working
with Google Cloud sovereign cloud platforms:
- **Berlin (Germany — Google Cloud Dedicated / GCD):** universe domain `apis-berlin-build0.goog`, region `u-germany-northeast1` (`a`, `b`, `c`), project prefix `eu0:`
- **France (Cloud de Confiance by S3NS):** universe domain `s3nsapis.fr`, region `u-france-east1` (`a`, `b`, `c`), project prefix `s3ns:`

Each sovereign cloud operates as a local, isolated cloud based on Google Cloud running in a single region with three zones.

## Key Differences from Google Cloud

- **Cloud Shell, Cloud Workstations, and Cloud Code are not available.** Install all tools locally or on a sovereign cloud VM.
- **`gcloud init` is not available.** Use the multi-step setup described below.
- **Default VPC networks are not created automatically** in new projects.
- **Project IDs carry a universe prefix:** `eu0:example-project` (Berlin) or `s3ns:example-project` (France S3NS).
- **Only a single region is available per universe:** `u-germany-northeast1` (Berlin) or `u-france-east1` (S3NS), each with three zones (`a`, `b`, `c`).
- **Cloud Identity is not available.** Use Workforce Identity Federation or service accounts.
- **Not all Google Cloud products are available.** Check [services.md](services.md) and [product-differences.md](product-differences.md) (and on S3NS, verify the ANSSI **SecNumCloud 3.2** qualification status).

## Setting Up the gcloud CLI

### Prerequisites

- A workload/workforce identity pool name (from your organization administrator).
- An identity provider (IdP) configured for your organization.
- Python 3.10 to 3.14.

### Installation

Download and install the gcloud CLI from the universe-specific storage endpoint:

**Berlin (GCD):**

```bash
# Download (Linux x86_64)
curl -O https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-linux-x86_64.tar.gz

# Extract and install
tar -xf google-cloud-cli-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh
```

**France (S3NS):**

```bash
# Download (Linux x86_64)
curl -O https://storage.s3nsapis.fr/cloud-sdk-release/google-cloud-cli-linux-x86_64.tar.gz

# Extract and install
tar -xf google-cloud-cli-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh
```

Available packages:
- Linux 64-bit (x86_64): `google-cloud-cli-linux-x86_64.tar.gz`
- Linux 64-bit (Arm): `google-cloud-cli-linux-arm.tar.gz`
- Linux 32-bit (x86): `google-cloud-cli-linux-x86.tar.gz`

After installation, open a new terminal so PATH changes take effect.

### Universe Domain Configuration

The gcloud CLI must be configured to target the sovereign cloud universe (`apis-berlin-build0.goog` for Berlin GCD or `s3nsapis.fr` for France S3NS), replacing the default `googleapis.com` used in public Google Cloud:

```bash
# Berlin (GCD)
gcloud config set api_endpoint_overrides/all https://apis-berlin-build0.goog/
gcloud config set universe_domain apis-berlin-build0.goog

# France (S3NS)
gcloud config set api_endpoint_overrides/all https://s3nsapis.fr/
gcloud config set universe_domain s3nsapis.fr
```

## Client Library Setup

### Environment Variable

Set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable before using any client libraries or running code samples:

```bash
# Berlin (GCD)
export GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog

# France (S3NS)
export GOOGLE_CLOUD_UNIVERSE_DOMAIN=s3nsapis.fr
```

You can also specify the target universe programmatically in your client options.

### Available Languages

Cloud Client Libraries are available for: Go, Java, Node.js, Python, Ruby, PHP, C#, C++, and Rust.

### Authentication

Use Application Default Credentials (ADC) for authentication. Cloud Identity is not available in GCD or S3NS — use Workforce Identity Federation (including Google Workspace, Microsoft Entra ID, AD FS, or Okta identity providers) or service accounts.

## API Access Patterns

### Service Endpoint FQDN Format

Service names remain the same as in Google Cloud (e.g., `bigquery.googleapis.com`), but service endpoint FQDNs use the universe domain:

```text
# Berlin (GCD)
<service>.googleapis.com  -->  <service>.apis-berlin-build0.goog

# France (S3NS)
<service>.googleapis.com  -->  <service>.s3nsapis.fr
```

Examples:
- `bigquery.googleapis.com` becomes `bigquery.apis-berlin-build0.goog` (Berlin) or `bigquery.s3nsapis.fr` (S3NS)
- `storage.googleapis.com` becomes `storage.apis-berlin-build0.goog` (Berlin) or `storage.s3nsapis.fr` (S3NS)
- `compute.googleapis.com` becomes `compute.apis-berlin-build0.goog` (Berlin) or `compute.s3nsapis.fr` (S3NS)

### Resource Naming

Full resource names (FRNs) remain the same as in Google Cloud, including `googleapis` in the domain portion:

```text
//bigquery.googleapis.com/projects/my-project/datasets/my-dataset
```

Resource names without their parent API are also unchanged:

```text
projects/my-project/datasets/my-dataset
```

URLs, however, use the universe-specific service endpoint:

```text
# Berlin (GCD)
https://bigquery.apis-berlin-build0.goog/bigquery/v2/projects/my-project/datasets/my-dataset

# France (S3NS)
https://bigquery.s3nsapis.fr/bigquery/v2/projects/my-project/datasets/my-dataset
```

### Project ID Format

All sovereign cloud project IDs carry a mandatory universe prefix (`eu0:` in Berlin, `s3ns:` in S3NS). This prefix is automatically added when you create a project. Always include it when referencing projects in commands and API calls:

```bash
# Berlin (GCD)
gcloud config set project eu0:my-project

# France (S3NS)
gcloud config set project s3ns:my-project
```

### Service Account Domains

Service account email addresses use universe-specific domains:

| Type | Google Cloud | Berlin (GCD) | France (S3NS) |
|------|-------------|--------------|---------------|
| Compute Engine default | `developer.gserviceaccount.com` | `developer.eu0-system.iam.gserviceaccount.com` | `developer.s3ns-system.iam.gserviceaccount.com` |
| User-managed | `iam.gserviceaccount.com` | `eu0.iam.gserviceaccount.com` | `s3ns.iam.gserviceaccount.com` |
| Service agents | `system.gserviceaccount.com` | `eu0-system.system.gserviceaccount.com` | `s3ns-system.system.gserviceaccount.com` |

Example user-created service accounts:
- Berlin: `my-sa@my-project.eu0.iam.gserviceaccount.com`
- S3NS: `my-sa@my-project.s3ns.iam.gserviceaccount.com`

Note: the project's `eu0:` or `s3ns:` prefix is **not** used in service account email addresses.

### OAuth Scopes

OAuth scope names are consistent between Google Cloud, GCD, and S3NS. If a scope includes `googleapis` in Google Cloud, it also does so in GCD and S3NS.

## Discovery API

The Discovery API provides machine-readable metadata about available APIs in each sovereign cloud universe.

### Listing All Available APIs

```text
# Berlin (GCD)
GET https://discovery.apis-berlin-build0.goog/discovery/v1/apis

# France (S3NS)
GET https://discovery.s3nsapis.fr/discovery/v1/apis
```

### Getting a Discovery Document for a Specific API

The URI format is:

```text
# Berlin (GCD)
https://<API>.apis-berlin-build0.goog/$discovery/rest?version=<VERSION>

# France (S3NS)
https://<API>.s3nsapis.fr/$discovery/rest?version=<VERSION>
```

Example — get the Discovery document for the Service Usage API v1:

```text
GET https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1
GET https://serviceusage.s3nsapis.fr/$discovery/rest?version=v1
```

### Discovery Document Contents

Each Discovery document includes:
- Identification: name, version, title, description
- Schemas: API resource schemas based on JSON Schema
- Methods: available API methods and their parameters
- OAuth scopes: list of OAuth scopes for the API
- Inline documentation: descriptions of schemas, methods, and parameters

## Required Domains

The following domains must be accessible for the sovereign cloud console and tools to function. Ensure your firewall or proxy allows traffic to these.

### Console Functionality (Required)

| Domain | Purpose |
|--------|---------|
| `console.cloud.berlin-build0.goog` / `console.cloud.s3nscloud.fr` | Sovereign cloud console (Berlin / S3NS) |
| `*.apis-berlin-build0.goog` / `*.s3nsapis.fr` | Sovereign cloud APIs (Berlin / S3NS) |
| `www.gstatic.com` | Static content (scripts, stylesheets, images) |
| `ssl.gstatic.com` | Images |
| `fonts.gstatic.com` | Fonts |
| `*.clients6.google.com` | Google APIs |
| `*.googleapis.com` | Google APIs |
| `apis.google.com` | Google API Client Libraries |
| `reauth.cloud.google.com` | Multi-factor authentication |
| `csp.withgoogle.com` | Content Security Policy reporting |

### Monitoring (Recommended)

| Domain or URL | Purpose |
|---------------|---------|
| `cloud.google.com/log` | Error logging |
| `www.google-analytics.com` | Analytics |
| `www.googletagmanager.com` | Tag management |

If monitoring domains are blocked, the console may still work, but the operator will not receive client-side console error reports.

## Common Setup Tasks

### Initial Network Setup

Default networks are not automatically created. Set up a network manually before deploying workloads:

```bash
gcloud compute networks create default
gcloud compute firewall-rules create default-allow-internal \
  --allow=tcp:1-65535,udp:1-65535,icmp \
  --source-ranges=10.128.0.0/9
gcloud compute firewall-rules create default-allow-ssh \
  --allow=tcp:22
gcloud compute firewall-rules create default-allow-rdp \
  --allow=tcp:3389
gcloud compute firewall-rules create default-allow-icmp \
  --allow=icmp
```

### Local Development Environment

Since Cloud Shell, Cloud Workstations, and Cloud Code are not available, set up your local environment (or a sovereign cloud Compute Engine VM) with:

1. Install the `gcloud` CLI from the sovereign cloud storage release bucket (see installation section above).
2. Install language runtimes as needed (Go, Python, Node.js, Java, etc.) and Terraform (`>= 1.12`).
3. Install Docker if working with containers (and configure `gcloud auth configure-docker <region>-docker.pkg.dev` targeting Artifact Registry).
4. Set the universe domain environment variable:

```bash
# Berlin (GCD)
export GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog

# France (S3NS)
export GOOGLE_CLOUD_UNIVERSE_DOMAIN=s3nsapis.fr
```

### IAM and Access Control

Access is managed through IAM. Roles bundle permissions and are granted by administrators to principals (authenticated identities).

Roles can be granted at multiple levels:
- **Organization, folder, project**: Permissions apply to all contained resources.
- **Service-specific resources**: Granular access to individual resources (instances, disks, buckets, secrets, etc.).

Advanced options include deny policies and conditional attribute-based access controls. Additional access control is available through Access Context Manager, VPC Service Controls, and Organization Policy Service.

## Quick Reference

| Item | Berlin (GCD — Germany) | France (S3NS — Cloud de Confiance) |
|------|------------------------|------------------------------------|
| Universe domain | `apis-berlin-build0.goog` | `s3nsapis.fr` |
| Environment variable | `GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog` | `GOOGLE_CLOUD_UNIVERSE_DOMAIN=s3nsapis.fr` |
| Region | `u-germany-northeast1` (3 zones: `a`, `b`, `c`) | `u-france-east1` (3 zones: `a`, `b`, `c`) |
| Project ID prefix | `eu0:` | `s3ns:` |
| Service endpoint pattern | `<service>.apis-berlin-build0.goog` | `<service>.s3nsapis.fr` |
| Console URL | `https://console.cloud.berlin-build0.goog/` | `https://console.cloud.s3nscloud.fr/` |
| Documentation URL | `https://berlin.devsitetest.how/` | `https://documentation.s3ns.fr/` |
| Discovery API endpoint | `https://discovery.apis-berlin-build0.goog/discovery/v1/apis` | `https://discovery.s3nsapis.fr/discovery/v1/apis` |
| User SA domain | `<project>.eu0.iam.gserviceaccount.com` | `<project>.s3ns.iam.gserviceaccount.com` |
| CLI download endpoint | `https://storage.apis-berlin-build0.goog/cloud-sdk-release/` | `https://storage.s3nsapis.fr/cloud-sdk-release/` |
