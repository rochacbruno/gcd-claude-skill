# Key Differences Between Google Cloud Dedicated (GCD) and Google Cloud (GCP)

Google Cloud Dedicated (GCD) is a local, isolated cloud environment based on Google Cloud, running in Germany. It uses the same Google-developed code and infrastructure but operates as a separate "universe" with its own subset of products, features, and workflows.

---

## Architecture: Single-Region Constraint

- GCD runs in **one region only**: `u-germany-northeast1`, which contains **three zones**.
- There is no multi-region redundancy. All multi-region GCP features are unavailable.
- Use multiple zones (not regions) for redundancy and high availability.
- `global` resources (e.g., Cloud KMS `global` location, Secret Manager global secrets) are still available but effectively resolve to the single region `u-germany-northeast1`.
- Any existing multi-region architectures or load-balancing designs must be reworked for single-region operation.

---

## Domain Names and API Endpoints

### Universe Domain

The GCD universe domain is `apis-berlin-build0.goog` (instead of `googleapis.com`).

### Service Names vs. Service Endpoints

| Aspect | GCP | GCD |
|---|---|---|
| Service names (for enabling/disabling APIs) | `bigquery.googleapis.com` | `bigquery.googleapis.com` (same) |
| Service endpoints (for API requests) | `bigquery.googleapis.com` | `bigquery.apis-berlin-build0.goog` |
| Console URL | `console.cloud.google.com` | `console.cloud.berlin-build0.goog` |

- **Service names** are identical between GCP and GCD.
- **Service endpoints** (the actual FQDNs for API calls) use the GCD-specific domain.
- **Endpoint pattern:** `<service>.apis-berlin-build0.goog`
- OAuth scope names remain consistent. If a scope uses `googleapis` in GCP, it also uses `googleapis` in GCD.

### Resource Names and URLs

- **Full resource names (FRNs)** are the same as GCP, including the `googleapis` domain. Example: `//bigquery.googleapis.com/projects/my-project/datasets/my-dataset`
- **Relative resource names** (without parent API) are also the same. Example: `projects/my-project/datasets/my-dataset`
- **Resource URLs** use the GCD endpoint domain and are therefore different. Example: `https://bigquery.apis-berlin-build0.goog/bigquery/v2/projects/my-project/datasets/my-dataset`

---

## Project ID Prefix

- All GCD project IDs carry a mandatory universe-specific prefix: **`eu0:`**
- This prefix is automatically prepended when creating projects.
- The prefix must be included in all commands, API calls, and console references.
- Example: a project named `my-app` has the project ID `eu0:my-app`.
- Exception: the `eu0:` prefix is NOT used in user-created service account names (the project part of the service account email omits the prefix).

| Field | Example |
|---|---|
| Project name | `MyProject` |
| Project ID | `eu0:myproject` |
| Project number | `123456789012` |

---

## Identity and Authentication

- **Cloud Identity is not available** in GCD.
- **Regular Google Accounts and Google Groups are not supported** for IAM.
- Authentication must use one of:
  - **Workforce Identity Federation** (supports Google Workspace, Microsoft/Azure AD, Okta, and other external IdPs)
  - **Service accounts**
- IAM roles and permissions are consistent between GCP and GCD.

---

## Service Accounts

Service account email addresses use GCD-specific domains:

| GCP Domain | GCD Domain | Usage |
|---|---|---|
| `developer.gserviceaccount.com` | `developer.eu0-system.iam.gserviceaccount.com` | Compute Engine default service account |
| `iam.gserviceaccount.com` | `eu0.iam.gserviceaccount.com` | Most user-managed service accounts |
| (various) | `eu0-system.iam.gserviceaccount.com` | Some service agents |
| `system.gserviceaccount.com` | `eu0-system.system.gserviceaccount.com` | Some service agents |

Examples:
- Default Compute Engine SA: `1234567-compute@developer.eu0-system.iam.gserviceaccount.com`
- User-created SA: `my-sa@my-project.eu0.iam.gserviceaccount.com`

Note: user-created service account names do NOT include the `eu0:` project ID prefix.

---

## Service Availability and Feature Limitations

- Not all GCP products are available in GCD. Check the GCD product list for current availability.
- Available products use the same names and same underlying code as GCP, but may have reduced capabilities.
- Key limitations:
  - **GKE**: Only Autopilot mode is available (no Standard mode).
  - **Compute Engine**: Limited VM types; older VM families unavailable; no ARM-based images; no TPUs.
  - **IAM**: Certain IAM policies are not supported.
  - **Cloud Shell**: Not available at all.
- New GCP features may not launch simultaneously in GCD.
- Preview/pre-GA features are generally not available in GCD.
- Some products may be unavailable if they depend on other products that are not in GCD.

---

## Billing and Cost Management

- Billing is handled by your **GCD operator**, not by Google directly.
- Pricing may differ from public GCP pricing.
- **No free trial tier** is available.
- **Committed use discounts (CUDs)** are not available.
- Quotas may differ from GCP defaults. Quota increase requests must go through GCD support.

---

## SLAs

- Google Cloud SLAs do **not** apply to GCD.
- All SLAs are between you and your GCD universe operator.
- Contact your operator for SLA details.

---

## Tooling Differences

### gcloud CLI

- The gcloud CLI requires additional setup to target GCD instead of public GCP.
- Must configure the CLI to use the GCD universe domain and external identity (not Google Accounts).
- gcloud commands for unavailable products/features are also unavailable.

### Client Libraries

- You must set the environment variable `GOOGLE_CLOUD_UNIVERSE_DOMAIN` before using client libraries.
- This tells libraries to target GCD endpoints instead of public GCP endpoints.

### Cloud Shell

- **Cloud Shell is not available** in GCD.
- Install CLI tools locally or on a VM running in GCD.
- Any workflows, scripts, or documentation that rely on Cloud Shell must be adapted for local tooling.

### Console

- The GCD console is at `console.cloud.berlin-build0.goog`.
- Language selection is made at sign-on and cannot be changed within the console.
- The guided organization setup flow is not available in the GCD console.

---

## Networking

- GCD runs a **completely separate, isolated network** from GCP.
  - Separate data center infrastructure.
  - Separate WAN for inter-data center traffic.
  - Separate internet connectivity via peering or transit.
- **No default VPC** is created automatically for new projects (unlike GCP). You must create or assign a VPC explicitly.
- Available networking products include: VPC, Cloud NAT, Cloud VPN, Cloud Interconnect, Cloud Router, Cloud DNS, Cloud Load Balancing, Cloud NGFW, VPC Service Controls, Google Cloud Armor - but each may have its own GCD-specific limitations.

---

## Organization Setup

- You cannot create a new organization yourself. Your GCD operator creates and provides an empty organization.
- The guided organization setup wizard available in the GCP console is not available in GCD.

---

## Platform Management

- Products labeled "Google-managed" in GCD are actually managed by your GCD operator, not by Google. The correct mental model is "Google-powered".
- Example: "Google-managed encryption keys" are renamed to "Google Cloud-powered encryption keys / Managed in Google Cloud Dedicated in Germany" to reflect that the operator manages them.
- GCD has its own dedicated SRE team with independent monitoring and alerting stacks, separate from GCP's.

---

## Hardware and OS

- GCD does not provide the same hardware and OS support as GCP.
- No ARM-based Compute Engine images.
- No TPUs.
- Limited machine type families and sizes.
- New machine types or OS releases in GCP do not imply future availability in GCD.

---

## Quick Reference: What Stays the Same vs. What Changes

| Aspect | Same as GCP? | GCD Value |
|---|---|---|
| Service names (API names) | Yes | `compute.googleapis.com` |
| Service endpoints | **No** | `compute.apis-berlin-build0.goog` |
| Full resource names (FRNs) | Yes | `//compute.googleapis.com/...` |
| Resource URLs | **No** | `https://compute.apis-berlin-build0.goog/...` |
| OAuth scopes | Yes | Same scope strings |
| IAM roles/permissions | Yes | Same role names |
| Project IDs | **No** | Prefixed with `eu0:` |
| Service account domains | **No** | `eu0.iam.gserviceaccount.com` etc. |
| Region | **No** | `u-germany-northeast1` (single region) |
| Console domain | **No** | `console.cloud.berlin-build0.goog` |
| Universe domain env var | N/A | `GOOGLE_CLOUD_UNIVERSE_DOMAIN` must be set |
| Billing | **No** | Through GCD operator |
| SLAs | **No** | With GCD operator |
| Cloud Identity | **No** | Not available; use Workforce Identity Federation |
| Cloud Shell | **No** | Not available |
