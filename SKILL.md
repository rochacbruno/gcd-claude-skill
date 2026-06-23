---
name: gcd
description: >
  Google Cloud Dedicated (GCD) sovereign cloud expert. Use when working with
  Google Cloud Dedicated, sovereign cloud, GCD regions, or when the user
  mentions GCD, Google Cloud Dedicated, sovereign cloud, universe domain,
  apis-berlin-build0.goog, u-germany-northeast1, Trusted Partner Cloud,
  TPC, or data sovereignty requirements for Google Cloud workloads.
  Provides guidance on GCD-specific services, authentication, Terraform,
  networking, and key differences from public Google Cloud.
  Also use when asked to review a PR, code review, or diff targeting GCD.
license: Apache-2.0
metadata:
  author: rochacbruno
  version: "1.0.0"
---

# Google Cloud Dedicated (GCD)

Google Cloud Dedicated is a sovereign cloud platform that provides Google
Cloud technology and services with strict data and operational sovereignty
guarantees. It is a **separate product from Google Cloud** with its own
isolated infrastructure, networking, and management.

GCD runs in sovereign regions. Berlin (Germany) is the reference region used
throughout this skill, but the architecture and guidance apply to any GCD
region. When helping users, ask which GCD region they are targeting if not
specified.

## Critical facts

- GCD is a fully isolated universe with **no network path to public GCP**
- Single region per universe (e.g., `u-germany-northeast1` with zones `a`, `b`, `c`)
- "Global" resources exist for API compatibility but are scoped to the single region
- Only a **subset of GCP services** is available
- API endpoints use `<service>.apis-<region-host>.goog` instead of `<service>.googleapis.com`
  - Berlin example: `compute.apis-berlin-build0.goog`
- Project IDs require a prefix (e.g., `eu0:my-project`)
- No Cloud Identity, no Cloud Shell, no regular Google Accounts
- Authentication uses Workforce Identity Federation or service accounts
- Billing and SLAs are with the GCD operator, not Google
- Client libraries require `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable

## Gotchas

Before writing any code, Terraform, or gcloud commands for GCD, check these:

1. **Set the universe domain.** Export `GOOGLE_CLOUD_UNIVERSE_DOMAIN=apis-berlin-build0.goog`
   (or the appropriate domain for the target region) before using client libraries.

2. **Use the full project ID.** Always include the prefix: `eu0:example-project`,
   not just `example-project`.

3. **Use GCD service endpoints.** Replace `googleapis.com` with the GCD endpoint
   in any REST calls or configurations. OAuth scope URLs stay the same.

4. **Check service availability.** Not all GCP services exist in GCD.
   GKE is Autopilot only. Older VM types are unavailable. Preview features
   are generally unavailable.

5. **Design for single-region.** No multi-region storage, no cross-region
   load balancing. Use multiple zones within the single region for HA.

6. **No Cloud Shell.** Install gcloud CLI and tools locally or on a GCD VM.

7. **Terraform needs universe_domain.** Set `universe_domain` in the provider
   block and use GCD-specific backend endpoints for state storage.

8. **"Google-managed" means operator-managed.** The GCD operator manages all
   services and data, not Google.

## When to load reference files

Load these files based on what the user needs help with:

- **Architecture, regions, or getting started** -
  Read [references/overview.md](references/overview.md)

- **What is different from public GCP** -
  Read [references/key-differences.md](references/key-differences.md)

- **Which services are available** -
  Read [references/services.md](references/services.md)

- **Per-product differences from public GCP** (Compute, BigQuery, GKE, IAM, etc.) -
  Read [references/product-differences.md](references/product-differences.md)

- **Authentication, identity providers, or credentials** -
  Read [references/authentication.md](references/authentication.md)

- **gcloud CLI, client libraries, API endpoints, or developer setup** -
  Read [references/developer-guide.md](references/developer-guide.md)

- **Terraform, IaC, or infrastructure provisioning** -
  Read [references/terraform.md](references/terraform.md)

- **Organization setup, identity providers, or Fabric FAST** -
  Read [references/organization-setup.md](references/organization-setup.md)

- **Quotas, quota management, or quota increases** -
  Read [references/quotas.md](references/quotas.md)

- **Common mistakes or troubleshooting** -
  Read [references/gotchas.md](references/gotchas.md)

## Available services (quick list)

Access Context Manager, API Discovery Service, API Keys, Artifact Registry,
BigQuery, BigQuery Data Policy, BigQuery Reservation, Cloud DNS, Cloud KMS,
Cloud Logging, Cloud Monitoring, Cloud SQL Admin, Cloud Storage,
Compute Engine, Google Kubernetes Engine (Autopilot only), IAM, Networking,
Organization Policy, Pub/Sub, Resource Manager, Service Account Credentials,
Service Directory, Service Usage, Workforce Identity Federation,
Workload Identity Federation.

## Region-agnostic guidance

The Berlin region (`u-germany-northeast1`, endpoint host `berlin-build0`)
is the reference throughout this skill's documentation. When the user works
with a different GCD region:

- Replace `apis-berlin-build0.goog` with the region's endpoint host
- Replace `u-germany-northeast1` with the region's identifier
- Replace zone names (`u-germany-northeast1-a/b/c`) accordingly
- The project ID prefix may differ (Berlin uses `eu0:`)
- All architectural constraints (single-region, service subset) apply equally

## Resolving ambiguity

When facing ambiguity or uncertainty about GCD behavior, features, or
configuration, always search the GCD documentation **before** searching
the public web. Public GCP docs and web results frequently describe
features or configurations that do not exist in GCD.

To search the GCD docs, use curl with the required proxy header:

```bash
curl -s -H "X-DevSite-Proxy:gcd" "https://berlin.devsitetest.how/docs/<path>"
```

For per-product documentation:

```bash
curl -s -H "X-DevSite-Proxy:gcd" "https://berlin.devsitetest.how/<product>/docs/<path>"
```

Examples:

```bash
# Search for Compute Engine differences
curl -s -H "X-DevSite-Proxy:gcd" "https://berlin.devsitetest.how/compute/docs/tpc-differences"

# Check GKE documentation
curl -s -H "X-DevSite-Proxy:gcd" "https://berlin.devsitetest.how/kubernetes-engine/docs"

# Check authentication setup
curl -s -H "X-DevSite-Proxy:gcd" "https://berlin.devsitetest.how/docs/authentication"
```

The response is HTML. Extract the article content and strip tags to read it.
Without the `X-DevSite-Proxy:gcd` header the request will 404.

Only fall back to public web search if the GCD docs do not cover the topic.

## Code review for GCD

When reviewing a PR or diff that targets GCD, check against this checklist.
Load [references/product-differences.md](references/product-differences.md) and
[references/gotchas.md](references/gotchas.md) for full details on any item.
When uncertain whether a feature is available, query the GCD docs directly
(see "Resolving ambiguity" above) before approving.

### Endpoints and domains

- [ ] No hardcoded `googleapis.com` in API calls, configs, or client setup.
      Must use `apis-<region>.goog` (e.g., `compute.apis-berlin-build0.goog`).
- [ ] `GOOGLE_CLOUD_UNIVERSE_DOMAIN` is set before using client libraries.
- [ ] OAuth scope URLs are left as `googleapis.com` (they stay the same).

### Project IDs

- [ ] Project IDs include the `eu0:` prefix everywhere: Terraform, gcloud
      commands, API calls, IAM bindings, service account references.

### Service availability

- [ ] No references to unavailable services: Cloud Functions, App Engine,
      Dataflow, Cloud Run (check current availability), Spanner, Firestore,
      Memorystore, Cloud Tasks, Cloud Scheduler, Secret Manager, Vertex AI.
- [ ] No use of unavailable features within available services:
  - GKE Standard mode (Autopilot only)
  - Persistent Disk or Local SSD (Hyperdisk Balanced only)
  - N2, E2, T2A, or other unavailable VM series (C3, M3, A3 Edge only)
  - BigQuery scheduled queries, data masking, column-level access control
  - Pub/Sub dead-letter queues, exactly-once delivery, ordering keys, schemas
  - Cloud SQL Server engine (MySQL and PostgreSQL only)
  - Cloud Storage Transfer Service, Storage Insights
- [ ] No reliance on Preview features (generally unavailable in GCD).

### Architecture

- [ ] No multi-region assumptions: dual-region buckets, cross-region load
      balancing, multi-region storage classes, global endpoint routing.
- [ ] "Global" resources are understood to be scoped to the single region.
- [ ] HA designs use multiple zones within `u-germany-northeast1`, not regions.

### Authentication and identity

- [ ] No Cloud Identity, Google Accounts, or Google Groups as principals.
- [ ] Uses Workforce Identity Federation or service accounts only.
- [ ] No Cloud Shell references in scripts, CI, or documentation.
- [ ] Service account emails use GCD domains:
      `PROJECT_ID.eu0.iam.gserviceaccount.com` (not `.iam.gserviceaccount.com`).

### Terraform and IaC

- [ ] Provider block includes `universe_domain = "apis-berlin-build0.goog"`.
- [ ] GCS backend for state uses `storage_custom_endpoint` for GCD.
- [ ] No Terraform resources for unavailable services.
- [ ] Machine types are C3, M3, or A3 Edge only.
- [ ] Disk types are `hyperdisk-balanced` only.
- [ ] Image projects use `eu0-system:` prefix (e.g., `eu0-system:debian-cloud`).

### Networking

- [ ] Does not assume a default VPC exists (GCD does not auto-create one).
- [ ] Uses zonal DNS names only (no global DNS).
- [ ] DNS zones are private only (public DNS zones unavailable).

### GKE specifics

- [ ] Cluster mode is Autopilot (not Standard).
- [ ] VPC-native clusters only (no route-based).
- [ ] Max 32 Pods per node.
- [ ] Workload identity uses `eu0.svc.id.goog` domain.
- [ ] No Binary Authorization, Config Sync, or fleet management.
- [ ] Cloud Storage FUSE CSI requires `custom-endpoint` mount option.

### Cloud Storage

- [ ] Bucket location is single-region only (no dual-region or multi-region).
- [ ] Location is explicitly set (no default location in GCD).
- [ ] No domain-named buckets or custom domain content serving.
- [ ] HMAC keys use service accounts (not user accounts).

### IAM

- [ ] Principals are service accounts or Workforce/Workload Identity only.
- [ ] No Google Accounts or Google Groups in IAM bindings.
- [ ] No use of PAM, PAB, or Policy Intelligence tools.
- [ ] Service agent domains use `eu0-system` (not standard GCP domains).

### Naming and documentation

- [ ] Does not describe operator-managed resources as "Google-managed".

## How to help

When a user asks about Google Cloud and appears to be working in a GCD context:

1. Identify whether they are targeting GCD or public GCP
2. If GCD, load the relevant reference files above
3. Apply the gotchas -- especially universe domain, project prefix, and endpoint differences
4. If they paste code or config from public GCP docs, adapt it for GCD
5. If they reference an unavailable service, explain it is not in GCD and suggest alternatives
6. When uncertain about any detail, query the GCD docs directly (see above) before searching the web
