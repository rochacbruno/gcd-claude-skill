# Google Cloud Dedicated (GCD) Developer Guide

This reference covers the essential setup and development patterns for working
with Google Cloud Dedicated (GCD), focusing on the universe domain
`apis-berlin-build0.goog`. GCD is a local, isolated cloud based on Google Cloud
running in a single region (`u-germany-northeast1`) with three zones.

## Key Differences from Google Cloud

- Cloud Shell is not available. Install all tools locally or on a GCD VM.
- `gcloud init` is not available. Use the multi-step setup described below.
- Default VPC networks are not created automatically in new projects.
- Project IDs carry a universe prefix: `eu0:example-project`.
- Only a single region is available (`u-germany-northeast1` with three zones).
- Cloud Identity is not available. Use Workforce Identity Federation or service accounts.
- Not all Google Cloud products are available. Check the GCD product list.

## Setting Up the gcloud CLI

### Prerequisites

- A workload identity pool name (from your organization administrator).
- An identity provider (IdP) configured for your organization.
- Python 3.10 to 3.14.

### Installation

Download and install the gcloud CLI from the GCD-specific storage endpoint:

```bash
# Download (Linux x86_64)
curl -O https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-linux-x86_64.tar.gz

# Extract
tar -xf google-cloud-cli-linux-x86_64.tar.gz

# Install
./google-cloud-sdk/install.sh
```

Available packages:
- Linux 64-bit (x86_64): `google-cloud-cli-linux-x86_64.tar.gz`
- Linux 64-bit (Arm): `google-cloud-cli-linux-arm.tar.gz`
- Linux 32-bit (x86): `google-cloud-cli-linux-x86.tar.gz`

After installation, open a new terminal so PATH changes take effect.

### Universe Domain Configuration

The gcloud CLI must be configured to target the GCD universe. The universe
domain for GCD is `apis-berlin-build0.goog`. This replaces the default
`googleapis.com` used in standard Google Cloud.

## Client Library Setup

### Environment Variable

Set the universe domain environment variable before using any client libraries
or running code samples:

```bash
export GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog
```

You can also specify the target universe programmatically in your code. The
syntax varies by language.

### Available Languages

Cloud Client Libraries are available for: Go, Java, Node.js, Python, Ruby, PHP,
C#, and C++. Each has a GitHub repository with installation instructions and
samples.

### Authentication

Use Application Default Credentials (ADC) for authentication. Cloud Identity is
not available in GCD - use Workforce Identity Federation (including Google
Workspace, Microsoft, or Okta identity providers) or service accounts.

## API Access Patterns

### Service Endpoint FQDN Format

Service names remain the same as in Google Cloud (e.g.,
`bigquery.googleapis.com`), but service endpoint FQDNs use the GCD universe
domain:

```
<service>.googleapis.com  -->  <service>.apis-berlin-build0.goog
```

Examples:
- `bigquery.googleapis.com` becomes `bigquery.apis-berlin-build0.goog`
- `storage.googleapis.com` becomes `storage.apis-berlin-build0.goog`
- `compute.googleapis.com` becomes `compute.apis-berlin-build0.goog`

### Resource Naming

Full resource names (FRNs) remain the same as in Google Cloud, including
`googleapis` in the domain portion:

```
//bigquery.googleapis.com/projects/my-project/datasets/my-dataset
```

Resource names without their parent API are also unchanged:

```
projects/my-project/datasets/my-dataset
```

URLs, however, use the universe-specific service endpoint:

```
https://bigquery.apis-berlin-build0.goog/bigquery/v2/projects/my-project/datasets/my-dataset
```

### Project ID Format

All GCD project IDs carry the universe prefix `eu0:`. This prefix is
automatically added when you create a project. Always include it when
referencing projects in commands and API calls:

```bash
# Correct
gcloud config set project eu0:my-project

# The project ID "my-project" is always referenced as "eu0:my-project"
```

### Service Account Domains

Service account email addresses use GCD-specific domains:

| Type | Google Cloud | GCD |
|------|-------------|-----|
| Compute Engine default | `developer.gserviceaccount.com` | `developer.eu0-system.iam.gserviceaccount.com` |
| User-managed | `iam.gserviceaccount.com` | `eu0.iam.gserviceaccount.com` |
| Service agents | `system.gserviceaccount.com` | `eu0-system.system.gserviceaccount.com` |

Example: a user-created service account might be
`my-sa@my-project.eu0.iam.gserviceaccount.com`.

Note: the project's `eu0:` prefix is not used in service account names.

### OAuth Scopes

OAuth scope names are consistent between Google Cloud and GCD. If a scope
includes `googleapis` in Google Cloud, it also does so in GCD.

## Discovery API

The Discovery API provides machine-readable metadata about available GCD APIs.

### Listing All Available APIs

```
GET https://discovery.apis-berlin-build0.goog/discovery/v1/apis
```

### Getting a Discovery Document for a Specific API

The URI format is:

```
https://<API>.apis-berlin-build0.goog/$discovery/rest?version=<VERSION>
```

Example - get the Discovery document for the Service Usage API v1:

```
GET https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1
```

### Discovery Document Contents

Each Discovery document includes:
- Identification: name, version, title, description
- Schemas: API resource schemas based on JSON Schema
- Methods: available API methods and their parameters
- OAuth scopes: list of OAuth scopes for the API
- Inline documentation: descriptions of schemas, methods, and parameters

## Required Domains

The following domains must be accessible for the GCD console and tools to
function. Ensure your firewall or proxy allows traffic to these.

### Console Functionality (Required)

| Domain | Purpose |
|--------|---------|
| `console.cloud.google.com` | GCD console |
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

If monitoring domains are blocked, the console may still work but Google will
not be aware of errors or issues you encounter.

## Common Setup Tasks

### Initial Network Setup

Default networks are not automatically created. Set up a default network
manually before following tutorials:

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

Since Cloud Shell is not available, set up your local environment with:

1. Install the gcloud CLI (see installation section above).
2. Install language runtimes as needed (Go, Python, Node.js, etc.).
3. Install Docker if working with containers.
4. Set the universe domain environment variable:

```bash
export GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog
```

### Developer Tools

- **Cloud Workstations**: Standardized browser-accessible development environments with preconfigured settings.
- **gcloud CLI**: Command-line management, scripting, and automation.
- **Cloud Code**: VS Code and JetBrains IDE extensions for GCD API integration, debugging, and documentation access.

### IAM and Access Control

Access is managed through IAM. Roles bundle permissions and are granted by
administrators to principals (authenticated identities).

Roles can be granted at multiple levels:
- **Organization, folder, project**: Permissions apply to all contained resources.
- **Service-specific resources**: Granular access to individual resources (instances, disks, buckets, etc.).

Advanced options include deny policies and conditional attribute-based access
controls. Additional access control is available through Access Context Manager
and Organization Policy Service.

## Quick Reference

| Item | Value |
|------|-------|
| Universe domain | `apis-berlin-build0.goog` |
| Environment variable | `GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog` |
| Region | `u-germany-northeast1` (3 zones) |
| Project ID prefix | `eu0:` |
| Service endpoint pattern | `<service>.apis-berlin-build0.goog` |
| Console URL | `https://console.cloud.berlin-build0.goog/` |
| Discovery API endpoint | `https://discovery.apis-berlin-build0.goog/discovery/v1/apis` |
| User SA domain | `<project>.eu0.iam.gserviceaccount.com` |
| Download endpoint | `https://storage.apis-berlin-build0.goog/cloud-sdk-release/` |
