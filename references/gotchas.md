# Google Cloud Dedicated - Critical Gotchas

Common mistakes and non-obvious facts that trip up developers moving from
public GCP to Google Cloud Dedicated.

## Identity and Authentication

- **No Cloud Identity.** Regular Google Accounts cannot be used. Only external
  identities via Workforce Identity Federation (including Google Workspace as
  an IdP) or service accounts are supported.
- **No Cloud Shell.** You must install the gcloud CLI and other tools locally
  or on a VM running inside GCD. Any workflow that depends on Cloud Shell must
  be updated.
- **Set GOOGLE_CLOUD_UNIVERSE_DOMAIN.** Before running any code that uses
  Google Cloud client libraries, you must export
  `GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog` (or the domain for
  your specific GCD region). Without this, client libraries will try to reach
  public GCP endpoints and fail.

## Project IDs

- **Project IDs require the `eu0:` prefix.** Every project created in GCD gets
  a prefix like `eu0:`. You must reference projects as `eu0:example-project`,
  not just `example-project`. This affects gcloud commands, Terraform configs,
  API calls, and anywhere a project ID is used.

## Service Endpoints

- **API endpoints use a different FQDN.** For example:
  - Public GCP: `compute.googleapis.com`
  - GCD Berlin: `compute.apis-berlin-build0.goog`
  - The pattern is `SERVICE.apis-REGION.goog`
- **OAuth scope names are the same.** If a scope includes `googleapis` in
  public GCP, it also uses `googleapis` in GCD. Do not change scope URLs.
- **Default API service names are the same** (e.g., `bigquery.googleapis.com`
  for enabling/disabling APIs), but the service endpoint FQDN differs.

## Architecture Constraints

- **Single region only.** GCD has no multi-region redundancy. The Berlin
  region has one region (`u-germany-northeast1`) with three zones (`a`, `b`,
  `c`). Features that rely on multiple regions (cross-region load balancing,
  multi-region storage) are not supported.
- **"Global" resources are regional.** Global resources exist for API
  compatibility but are scoped to `u-germany-northeast1` only.
- **No inter-region redundancy.** Design for single-region high availability
  using multiple zones within the region.

## Service Availability

- **Only a subset of GCP services is available.** Check the product list
  before designing. Major available services: Compute Engine, GKE (Autopilot
  only), Cloud Storage, BigQuery, Cloud SQL, Pub/Sub, Cloud DNS, Cloud KMS,
  IAM, Artifact Registry, Cloud Logging, Cloud Monitoring.
- **GKE is Autopilot only.** Standard mode is not available.
- **Older Compute Engine machine types are unavailable.** Verify your desired
  VM types exist before writing Terraform or deployment configs.
- **Preview features are generally unavailable.** Do not rely on features
  marked as Preview in public GCP documentation.
- **New GCP features may not launch simultaneously in GCD.** Subscribe to GCD
  release notes for updates.

## SSH Access

- **OS Login is unavailable.** You cannot use `gcloud compute os-login` or
  rely on OS Login for SSH key and user management. Manage SSH keys and
  user accounts manually or via instance metadata.
- **Use `gcloud compute ssh` when possible.** It handles key generation,
  metadata-based key distribution, and firewall rule setup automatically.
  This works for normal interactive access and automation/CI where gcloud
  is installed.
- **For environments without gcloud**, use plain SSH with pre-configured
  keys and users (set via instance metadata or baked into the image).
- **IAP TCP forwarding is unavailable.** You cannot tunnel SSH through
  Identity-Aware Proxy. If VMs lack public IPs, use a bastion host with
  plain SSH for the second hop.
- **Interactive serial console access is unavailable.** If a VM is
  unreachable via SSH, you cannot fall back to the serial console.

## Naming and Branding

- **"Google-managed" does not mean Google manages your data.** In GCD, the
  operator manages everything. "Google-managed encryption keys" in GCD are
  actually "Google Cloud-powered encryption keys / Managed in Google Cloud
  Dedicated". The technology is the same, but the operator manages it.

## Billing and SLAs

- **Billing is handled by your GCD operator, not Google.** Google Cloud
  billing documentation does not apply.
- **SLAs are with your operator, not Google.** Google Cloud SLAs do not apply
  to GCD.

## Terraform and IaC

- **The Google Cloud provider for Terraform requires universe_domain
  configuration.** You must set `universe_domain` in the provider block and
  use GCD-specific settings.
- **Not all Terraform resources are available.** Only resources corresponding
  to available GCD services work. Terraform plans that reference unavailable
  resources will fail.
- **State storage must be within GCD.** If using a GCS backend for Terraform
  state, the bucket must be in GCD.

## Networking

- **GCD has its own network, separate from the public internet and other
  universes.** There is no network path between GCD and public GCP.
- **Domain names differ.** Console, API, and service domains all use
  GCD-specific hostnames.

## Documentation

- **GCD docs may redirect to the differences page** when you follow a link to
  a product or feature that is unavailable. If you land on the "Key
  differences" page unexpectedly, the feature you were looking for is probably
  not available in GCD.
