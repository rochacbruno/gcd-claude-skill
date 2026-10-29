# Google Cloud Dedicated (GCD) & Cloud de Confiance (S3NS) - Critical Gotchas

Common mistakes and non-obvious facts that trip up developers moving from
public GCP to Google Cloud Dedicated (Berlin) or Cloud de Confiance by S3NS (France).

## Identity and Authentication

- **No Cloud Identity.** Regular Google Accounts cannot be used. Only external
  identities via Workforce Identity Federation (including Google Workspace, Entra ID,
  Okta, or AD FS as an IdP) or service accounts are supported.
- **No Cloud Shell, Cloud Workstations, or Cloud Code.** You must install the
  `gcloud` CLI and other tools locally or on a VM running inside the sovereign cloud.
- **Set `GOOGLE_CLOUD_UNIVERSE_DOMAIN`.** Before running any code that uses
  Google Cloud client libraries, you must export:
  - Berlin (GCD): `GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog`
  - France (S3NS): `GOOGLE_CLOUD_UNIVERSE_DOMAIN=s3nsapis.fr`
  Without this, client libraries will try to reach public GCP endpoints (`googleapis.com`) and fail.

## Project IDs and Service Account Emails

- **Project IDs require the universe prefix (`eu0:` or `s3ns:`).** Every project
  created in sovereign cloud gets a prefix (`eu0:example-project` on Berlin,
  `s3ns:example-project` on S3NS). You must include this prefix in `gcloud` commands,
  Terraform configs, API calls, and console references.
- **Service account emails do NOT include the project prefix.** A user-managed
  service account in project `s3ns:my-project` has the email
  `my-sa@my-project.s3ns.iam.gserviceaccount.com` (or `my-sa@my-project.eu0.iam.gserviceaccount.com`
  in Berlin) — never put `s3ns:` or `eu0:` after the `@`.

## Service Endpoints

- **API endpoints use a universe-specific FQDN:**
  - Public GCP: `<service>.googleapis.com`
  - Berlin (GCD): `<service>.apis-berlin-build0.goog`
  - France (S3NS): `<service>.s3nsapis.fr`
- **OAuth scope names are the same.** If a scope includes `googleapis` in
  public GCP, it also uses `googleapis` in GCD and S3NS. Do not change scope URLs.
- **Default API service names are the same** (e.g., `bigquery.googleapis.com`
  for enabling/disabling APIs), even though the service endpoint FQDN differs.

## S3NS SecNumCloud 3.2 Qualification Status

- **Not every service available on S3NS is already ANSSI SecNumCloud 3.2 qualified.**
  On S3NS PREMI3NS (`u-france-east1`), **29 services** are **`Qualifié SecNumCloud 3.2`**,
  while **10 recently released services** (`Access Transparency`, `Bigtable`, `Cloud Quotas`,
  `Cloud Run`, `Filestore`, `Gemini platform / Agent Platform`, `Managed Airflow / Composer 3`,
  `Managed Spark / Dataproc`, `Secret Manager`, `Storage Transfer Service`) are in
  **`Qualification en cours`** (available and documented today, ANSSI qualification in progress).
  4 roadmap services (`Cloud Asset Inventory`, `Cloud Build`, `Cloud Spanner`,
  `Network Connectivity Center`) are **`À venir`**. Always check [services.md](services.md)
  when designing workloads subject to strict SecNumCloud 3.2 compliance mandates.

## Architecture Constraints

- **Single region only.** Each sovereign cloud universe has one region with three zones:
  - Berlin (GCD): `u-germany-northeast1` (`-a`, `-b`, `-c`)
  - France (S3NS): `u-france-east1` (`-a`, `-b`, `-c`)
  Features that rely on multiple regions (cross-region load balancing, multi-region storage) are not supported.
- **"Global" resources are regional.** Global resources exist for API compatibility
  but are physically scoped to `u-germany-northeast1` or `u-france-east1` only.
- **No default VPC network.** New projects do not have a `default` VPC network.
  You must explicitly create a VPC and subnet before launching VMs, GKE clusters, or databases.

## Service-Specific Gotchas

- **Compute Engine:** Only `C3`, `M3`, and `A3` (H100 GPU) VM families and `hyperdisk-balanced`
  disks are supported. Legacy machine types (`e2-*`, `n1-*`, `n2-*`) and Persistent Disks (`pd-*`)
  will fail. Public OS images must include the sovereign image project prefix
  (`s3ns-system:debian-cloud/debian-12` or `eu0-system:debian-cloud/debian-12`).
- **GKE is Autopilot only.** Standard mode is not available.
- **Cloud Run:** Deploys containers from Artifact Registry only; service URLs use
  `*.s3nsrun.fr` (S3NS) or `*.run-berlin-build0.goog` (Berlin). Uses Direct VPC egress only
  (Serverless VPC Access connectors are not supported). Cloud Run functions are not available.
- **Bigtable:** Does **not** support Terraform (`google_bigtable_*` resources fail). Provision
  Bigtable instances, clusters, and tables via `gcloud`, `cbt`, client libraries, or the console.
  GoogleSQL for Bigtable and Data Boost are unavailable.
- **Secret Manager:** Even when creating or accessing **regional secrets** (`u-france-east1` or
  `u-germany-northeast1`), you must use the **global endpoint** (`secretmanager.s3nsapis.fr` or
  `secretmanager.apis-berlin-build0.goog`), not a regional `secretmanager.<region>.rep.*` endpoint.
  Only the `v1` API is supported (`v1beta1`/`v1beta2` are unavailable).
- **Agent Platform (Gemini Enterprise Agent Platform):** Supports open-weight models (`Gemma`, `Mistral`)
  from Model Garden deployed to dedicated GPU endpoints (`Predict`/`RawPredict` only). Proprietary
  Gemini models, Vertex AI SDK, and Google Gen AI SDK are **not** supported.
- **Managed Service for Apache Spark (Dataproc):** Supports Compute Engine Spark clusters on image `2.3+`
  only (`C3`, `M3`, `A3` VMs). Serverless Spark and Spark on GKE are unavailable.
- **Managed Airflow (Cloud Composer):** Only **Composer 3** Highly Resilient environments in
  **Large** or **Custom** sizes are supported (Small and Medium sizes are unavailable).
- **Filestore:** Only the **Regional** tier (`1 TiB`–`9.75 TiB`) using **Direct Peering** is supported
  (Basic, Zonal, Enterprise tiers and Private Services Access are unavailable).
- **Cloud Monitoring:** Native custom dashboards and alerting UI are unavailable in the console.
  Query metrics via **PromQL** or export them via the Prometheus API to self-hosted Grafana.

## SSH Access

- **OS Login is unavailable.** You cannot use `gcloud compute os-login` or
  rely on OS Login for SSH key and user management. Manage SSH keys and
  user accounts manually or via instance metadata.
- **Mandatory WIF attribute for SSH:** When setting up Workforce Identity Federation,
  you **must** map `google.posix_username` so `gcloud compute ssh` can provision POSIX accounts.
- **Use `gcloud compute ssh` when possible.** It handles key generation,
  metadata-based key distribution, and firewall rule setup automatically.
- **IAP TCP forwarding is unavailable.** You cannot tunnel SSH through
  Identity-Aware Proxy. If VMs lack public IPs, use a bastion host with
  plain SSH for the second hop.
- **Interactive serial console access is unavailable.** If a VM is
  unreachable via SSH, you cannot fall back to the interactive serial console.

## Naming and Branding

- **"Google-managed" does not mean Google manages your data.** In GCD and S3NS, the
  local sovereign operator manages the platform. "Google-managed encryption keys" are
  "Google Cloud-powered encryption keys / Managed in Cloud de Confiance by S3NS" (or
  "Managed in Google Cloud Dedicated").

## Billing, Support, and SLAs

- **Billing and SLAs are with your sovereign cloud operator (e.g., S3NS), not Google.**
  Public Google Cloud billing docs, free tier, CUDs, and SLAs do not apply.
- **Support channels differ:** S3NS customers use [https://support.s3ns.fr](https://support.s3ns.fr);
  Berlin GCD customers use a dedicated EU Data Boundary support project.

## Terraform and IaC

- **Set `universe_domain` in the Google Terraform provider** (`s3nsapis.fr` or `apis-berlin-build0.goog`).
- **Set `storage_custom_endpoint` in the `gcs` backend** (`https://storage.s3nsapis.fr/storage/v1/` or `https://storage.apis-berlin-build0.goog/storage/v1/`).
- **Not all Terraform resources are available.** Only resources corresponding to available services work (and Bigtable does not support Terraform in sovereign cloud).

## Documentation

- **Sovereign cloud docs may redirect to `/docs/tpc-differences`** when you follow a link to
  a product or feature that is unavailable. If you land on the "Differences from Google Cloud"
  page unexpectedly, the feature you were looking for is not available in GCD or S3NS.
