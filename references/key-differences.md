# Key Differences Between Sovereign Cloud (GCD / S3NS) and Public Google Cloud (GCP)

Google Cloud Dedicated (GCD in Germany) and Cloud de Confiance by S3NS (PREMI3NS in France) are local, isolated cloud environments based on Google Cloud. They use the same Google-developed code and infrastructure but operate as separate "universes" with their own subset of products, features, and workflows.

---

## Architecture: Single-Region Constraint

- Each sovereign cloud universe runs in **one region only**, containing **three zones**:
  - **Berlin (GCD — Germany):** `u-germany-northeast1` (`u-germany-northeast1-a`, `-b`, `-c`)
  - **France (S3NS — Cloud de Confiance):** `u-france-east1` (`u-france-east1-a`, `-b`, `-c`)
- There is no multi-region redundancy. All multi-region GCP features are unavailable.
- Use multiple zones (not regions) for redundancy and high availability.
- `global` resources (e.g., Cloud KMS `global` location, Secret Manager global secrets) are available for API compatibility but physically resolve to the single region (`u-germany-northeast1` or `u-france-east1`).
- Any existing multi-region architectures or cross-region load-balancing designs must be reworked for single-region, multi-zone operation.

---

## Domain Names and API Endpoints

### Universe Domain

- **Berlin (GCD):** `apis-berlin-build0.goog`
- **France (S3NS):** `s3nsapis.fr`

### Service Names vs. Service Endpoints

| Aspect | Public GCP | Berlin (GCD) | France (S3NS) |
|---|---|---|---|
| Service names (for enabling/disabling APIs) | `bigquery.googleapis.com` | `bigquery.googleapis.com` (same) | `bigquery.googleapis.com` (same) |
| Service endpoints (for API requests) | `bigquery.googleapis.com` | `bigquery.apis-berlin-build0.goog` | `bigquery.s3nsapis.fr` |
| Cloud Run service URLs | `*.run.app` | `*.run-berlin-build0.goog` | `*.s3nsrun.fr` |
| Console URL | `console.cloud.google.com` | `console.cloud.berlin-build0.goog` | `console.cloud.s3nscloud.fr` |

- **Service names** are identical between GCP, GCD, and S3NS.
- **Service endpoints** (the actual FQDNs for API calls) use the universe-specific domain (`<service>.apis-berlin-build0.goog` or `<service>.s3nsapis.fr`).
- **OAuth scope names** remain consistent. If a scope uses `googleapis` in GCP, it also uses `googleapis` in GCD and S3NS.

### Resource Names and URLs

- **Full resource names (FRNs)** are the same as GCP, including the `googleapis` domain. Example: `//bigquery.googleapis.com/projects/my-project/datasets/my-dataset`
- **Relative resource names** (without parent API) are also the same. Example: `projects/my-project/datasets/my-dataset`
- **Resource URLs** use the sovereign cloud endpoint domain and are therefore different:
  - Berlin: `https://bigquery.apis-berlin-build0.goog/bigquery/v2/projects/my-project/datasets/my-dataset`
  - S3NS: `https://bigquery.s3nsapis.fr/bigquery/v2/projects/my-project/datasets/my-dataset`

---

## Project ID Prefix

- All sovereign cloud project IDs carry a mandatory universe-specific prefix:
  - **Berlin (GCD):** **`eu0:`** (e.g., `eu0:my-app`)
  - **France (S3NS):** **`s3ns:`** (e.g., `s3ns:my-app`)
- This prefix is automatically prepended when creating projects.
- The prefix must be included in all commands, API calls, Terraform configs, and console references.
- **Exception:** The `eu0:` or `s3ns:` prefix is **NOT** used in user-created service account email addresses (the project part of the service account email omits the prefix).

| Field | Berlin (GCD) Example | France (S3NS) Example |
|---|---|---|
| Project name | `MyProject` | `MyProject` |
| Project ID | `eu0:myproject` | `s3ns:myproject` |
| Project number | `123456789012` | `123456789012` |

---

## Identity and Authentication

- **Cloud Identity is not available** in GCD or S3NS.
- **Regular Google Accounts and Google Groups are not supported** for IAM.
- Authentication must use one of:
  - **Workforce Identity Federation** (supports Google Workspace, Microsoft Entra ID, AD FS, Okta, and other OIDC/SAML 2.0 IdPs)
  - **Service accounts**
  - **Workload Identity Federation** (for external workloads)
- IAM roles and permissions are consistent between GCP, GCD, and S3NS.

---

## Service Accounts

Service account email addresses use universe-specific domains:

| GCP Domain | Berlin (GCD) Domain | France (S3NS) Domain | Usage |
|---|---|---|---|
| `developer.gserviceaccount.com` | `developer.eu0-system.iam.gserviceaccount.com` | `developer.s3ns-system.iam.gserviceaccount.com` | Compute Engine default service account |
| `iam.gserviceaccount.com` | `eu0.iam.gserviceaccount.com` | `s3ns.iam.gserviceaccount.com` | User-managed service accounts |
| (various) | `eu0-system.iam.gserviceaccount.com` | `s3ns-system.iam.gserviceaccount.com` | Some service agents |
| `system.gserviceaccount.com` | `eu0-system.system.gserviceaccount.com` | `s3ns-system.system.gserviceaccount.com` | Some service agents |

Examples:
- Default Compute Engine SA: `1234567-compute@developer.eu0-system.iam.gserviceaccount.com` (Berlin) / `1234567-compute@developer.s3ns-system.iam.gserviceaccount.com` (S3NS)
- User-created SA: `my-sa@my-project.eu0.iam.gserviceaccount.com` (Berlin) / `my-sa@my-project.s3ns.iam.gserviceaccount.com` (S3NS)

Note: user-created service account emails do **NOT** include the `eu0:` or `s3ns:` project ID prefix.

---

## Service Availability, SecNumCloud 3.2, and Feature Limitations

- Not all GCP products are available in GCD or S3NS. Check [services.md](services.md) for current availability.
- **S3NS SecNumCloud 3.2 status:** On S3NS (`u-france-east1`, PREMI3NS), 29 services are **Qualifié SecNumCloud 3.2** and 10 recently released services (`Access Transparency`, `Bigtable`, `Cloud Quotas`, `Cloud Run`, `Filestore`, `Gemini platform / Agent Platform`, `Managed Service for Apache Airflow / Composer 3`, `Managed Service for Apache Spark / Dataproc`, `Secret Manager`, `Storage Transfer Service`) are in **Qualification en cours** (available today, ANSSI qualification in progress). Always verify whether the customer requires strictly SecNumCloud-qualified services.
- Key architectural limitations across available products (see [product-differences.md](product-differences.md) for full details):
  - **GKE:** Only Autopilot mode is available (no Standard mode).
  - **Compute Engine:** Only `C3`, `M3`, and `A3` (H100 GPU) VM families; only Hyperdisk (`hyperdisk-balanced`); no ARM images; no TPUs; no OS Login.
  - **Cloud Run:** Deploy from Artifact Registry only (`*.s3nsrun.fr` / `*.run-berlin-build0.goog`); Direct VPC egress only (no Serverless VPC Access connectors); no Cloud Run functions.
  - **Cloud SQL:** MySQL and PostgreSQL only (no SQL Server), Enterprise Plus edition on `C3` (`db-perf-optimized-N-*`) only.
  - **Bigtable:** Single-region multi-zone replication only; no Terraform support; no GoogleSQL for Bigtable; no Data Boost.
  - **Agent Platform (Gemini Enterprise Agent Platform):** Open-weight models (Gemma, Mistral) via Model Garden & synchronous online inference (`Predict`/`RawPredict`) only; no proprietary Gemini models, no Vertex AI / Gen AI SDKs.
  - **Managed Spark (Dataproc):** Compute Engine clusters on image `2.3+` only; no Serverless Spark or Spark on GKE.
  - **Managed Airflow (Cloud Composer):** Composer 3 Highly Resilient in Large/Custom sizes only; no Composer 1 or 2.
  - **Filestore:** Regional tier (`1 TiB`–`9.75 TiB`) with Direct Peering only; no Basic/Zonal/Enterprise tiers, no Private Services Access.
  - **Secret Manager:** Global endpoint (`secretmanager.s3nsapis.fr` / `secretmanager.apis-berlin-build0.goog`) required even for regional secrets; `v1` API only.
  - **Cloud Shell, Cloud Workstations, Cloud Code:** Not available at all.

---

## Billing and Cost Management

- Billing is handled by your **sovereign cloud operator** (e.g., S3NS in France), not by public Google Cloud directly.
- Pricing differs from public GCP pricing.
- **No free trial tier** is available.
- **Committed use discounts (CUDs)** are not available.
- Quotas may differ from GCP defaults. Quota increase requests must go through sovereign cloud support (`support.s3ns.fr` for S3NS).

---

## SLAs

- Public Google Cloud SLAs do **not** apply to GCD or S3NS.
- All SLAs are between you and your sovereign cloud operator.

---

## Tooling Differences

### gcloud CLI

- Download from the sovereign cloud storage release bucket (`storage.apis-berlin-build0.goog/cloud-sdk-release/` or `storage.s3nsapis.fr/cloud-sdk-release/`).
- Must configure the CLI to use the sovereign cloud universe domain (`apis-berlin-build0.goog` or `s3nsapis.fr`) and Workforce Identity Federation.

### Client Libraries

- You must set the environment variable `GOOGLE_CLOUD_UNIVERSE_DOMAIN` (`apis-berlin-build0.goog` or `s3nsapis.fr`) before using client libraries.

### Cloud Shell

- **Cloud Shell is not available** in GCD or S3NS.
- Install CLI tools locally or on a VM running in the sovereign cloud.

### Console

- **Berlin (GCD):** `console.cloud.berlin-build0.goog`
- **France (S3NS):** `console.cloud.s3nscloud.fr`
- Language selection is made at sign-on and cannot be changed within the console.
- The guided organization setup wizard is not available in the console (use Fabric FAST — see [organization-setup.md](organization-setup.md)).

---

## Networking

- Each sovereign cloud runs a **completely separate, isolated network** from public GCP.
- **No default VPC** is created automatically for new projects. You must create or assign a VPC explicitly.
- Available networking products include: VPC, Cloud NAT, Cloud VPN (HA VPN), Cloud Interconnect, Cloud Router, Cloud DNS, Cloud Load Balancing (regional), Cloud NGFW, VPC Service Controls, Google Cloud Armor, Service Directory, and Private Service Connect.

---

## Platform Management

- Products labeled "Google-managed" in public GCP are managed by your **sovereign cloud operator** in GCD and S3NS. The correct mental model is "Google-powered, operator-managed".
- Example: "Google-managed encryption keys" are "Google Cloud-powered encryption keys / Managed in Cloud de Confiance by S3NS" (or "Managed in Google Cloud Dedicated in Germany").
- Each sovereign cloud has its own dedicated local operations and SRE team with independent monitoring and alerting stacks.

---

## Quick Reference: What Stays the Same vs. What Changes

| Aspect | Same as GCP? | Berlin (GCD) Value | France (S3NS) Value |
|---|---|---|---|
| Service names (API names) | Yes | `compute.googleapis.com` | `compute.googleapis.com` |
| Service endpoints | **No** | `compute.apis-berlin-build0.goog` | `compute.s3nsapis.fr` |
| Full resource names (FRNs) | Yes | `//compute.googleapis.com/...` | `//compute.googleapis.com/...` |
| Resource URLs | **No** | `https://compute.apis-berlin-build0.goog/...` | `https://compute.s3nsapis.fr/...` |
| OAuth scopes | Yes | Same scope strings | Same scope strings |
| IAM roles/permissions | Yes | Same role names | Same role names |
| Project IDs | **No** | Prefixed with `eu0:` | Prefixed with `s3ns:` |
| Service account domains | **No** | `eu0.iam.gserviceaccount.com` | `s3ns.iam.gserviceaccount.com` |
| Region | **No** | `u-germany-northeast1` | `u-france-east1` |
| Console domain | **No** | `console.cloud.berlin-build0.goog` | `console.cloud.s3nscloud.fr` |
| Universe domain env var | N/A | `GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog` | `GOOGLE_CLOUD_UNIVERSE_DOMAIN=s3nsapis.fr` |
| Billing & SLAs | **No** | Through GCD operator | Through S3NS |
| Cloud Identity | **No** | Not available; use Workforce Identity Federation | Not available; use Workforce Identity Federation |
| Cloud Shell | **No** | Not available | Not available |
