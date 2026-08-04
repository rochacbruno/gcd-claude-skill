---
name: gcd
description: >
  Google Cloud Dedicated (GCD) and Cloud de Confiance (S3NS) sovereign cloud
  expert. Use when working with sovereign Google Cloud regions, or when the user
  mentions GCD, Google Cloud Dedicated, Cloud de Confiance, S3NS, sovereign
  cloud, universe domain, apis-berlin-build0.goog, s3nsapis.fr,
  u-germany-northeast1, u-france-east1, Trusted Partner Cloud, TPC, or data
  sovereignty requirements for Google Cloud workloads. Provides guidance on
  region-specific services, authentication, Terraform, networking, and key
  differences from public Google Cloud. Also use when asked to review a PR,
  code review, or diff targeting these sovereign clouds.
license: Apache-2.0
metadata:
  author: rochacbruno
  version: "2.0.0"
---

# Google Cloud Dedicated (GCD) / Cloud de Confiance (S3NS)

Google Cloud sovereign cloud platforms provide Google Cloud technology and
services with strict data and operational sovereignty guarantees. They are
**separate products from Google Cloud** with their own isolated infrastructure,
networking, and management.

Two regions are currently documented:

| | Berlin (GCD) | France (S3NS) |
|---|---|---|
| Full name | Google Cloud Dedicated in Germany | Cloud de Confiance by S3NS |
| Region | `u-germany-northeast1` | `u-france-east1` |
| Zones | `u-germany-northeast1-a/b/c` | `u-france-east1-a/b/c` |
| API endpoint domain | `apis-berlin-build0.goog` | `s3nsapis.fr` |
| Console URL | `console.cloud.berlin-build0.goog` | `console.cloud.s3nscloud.fr` |
| Project ID prefix | `eu0:` | `s3ns:` |
| Image project prefix | `eu0-system:` | `s3ns-system:` |
| SA domain (user) | `eu0.iam.gserviceaccount.com` | `s3ns.iam.gserviceaccount.com` |
| SA domain (default compute) | `developer.eu0-system.iam.gserviceaccount.com` | `developer.s3ns-system.iam.gserviceaccount.com` |
| SA domain (agents) | `eu0-system.system.gserviceaccount.com` | `s3ns-system.system.gserviceaccount.com` |
| Docs URL | `berlin.devsitetest.how` | `documentation.s3ns.fr` |
| Docs access | Requires `X-DevSite-Proxy: gcd` header | Direct (no header) |
| Support | GCD support portal | `support.s3ns.fr` |
| Compliance target | German/EU sovereignty | French SecNumCloud (ANSSI) |

When helping users, ask which region they are targeting if not specified.
The architecture, constraints, and guidance apply equally to both regions -
only the identifiers differ.

## Critical facts

- Each sovereign cloud is a fully isolated universe with **no network path to public GCP**
- Single region per universe with three zones
- "Global" resources exist for API compatibility but are scoped to the single region
- Only a **subset of GCP services** is available
- API endpoints use region-specific domains instead of `googleapis.com`
  - Berlin: `<service>.apis-berlin-build0.goog`
  - S3NS: `<service>.s3nsapis.fr`
- Project IDs require a region-specific prefix (`eu0:` for Berlin, `s3ns:` for S3NS)
- No Cloud Identity, no Cloud Shell, no regular Google Accounts
- Authentication uses Workforce Identity Federation or service accounts
- Billing and SLAs are with the sovereign cloud operator, not Google
- Client libraries require `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable

## Gotchas

Before writing any code, Terraform, or gcloud commands for a sovereign cloud
region, check these:

1. **Set the universe domain.** Export `GOOGLE_CLOUD_UNIVERSE_DOMAIN` with the
   correct domain for the target region (`apis-berlin-build0.goog` for Berlin,
   `s3nsapis.fr` for S3NS) before using client libraries.

2. **Use the full project ID.** Always include the region prefix:
   `eu0:example-project` (Berlin) or `s3ns:example-project` (S3NS).

3. **Use sovereign cloud service endpoints.** Replace `googleapis.com` with the
   region's endpoint domain in any REST calls or configurations. OAuth scope
   URLs stay the same.

4. **Check service availability.** Not all GCP services exist in sovereign
   cloud. GKE is Autopilot only. Older VM types are unavailable. Preview
   features are generally unavailable. S3NS has a broader product catalog
   (more networking products) than Berlin.

5. **Design for single-region.** No multi-region storage, no cross-region
   load balancing. Use multiple zones within the single region for HA.

6. **No Cloud Shell.** Install gcloud CLI and tools locally or on a sovereign
   cloud VM.

7. **Terraform needs universe_domain.** Set `universe_domain` in the provider
   block and use region-specific backend endpoints for state storage.

8. **"Google-managed" means operator-managed.** The sovereign cloud operator
   manages all services and data, not Google.

9. **Image projects use region prefixes.** Use `eu0-system:debian-cloud`
   (Berlin) or `s3ns-system:debian-cloud` (S3NS), not `debian-cloud`.

10. **Service account domains differ.** User-created SAs use
    `PROJECT.eu0.iam.gserviceaccount.com` (Berlin) or
    `PROJECT.s3ns.iam.gserviceaccount.com` (S3NS).

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

**Both regions:** Access Context Manager, API Discovery Service, API Keys,
Artifact Registry, BigQuery, BigQuery Reservation, Cloud DNS, Cloud KMS,
Cloud Logging, Cloud Monitoring, Cloud SQL, Cloud Storage, Compute Engine,
Google Kubernetes Engine (Autopilot only), IAM, Pub/Sub, Resource Manager,
Service Account Credentials, Service Usage, Workforce/Workload Identity
Federation.

**Both regions (networking):** Cloud Armor, Cloud DNS, Cloud Interconnect,
Cloud Load Balancing, Cloud NAT, Cloud NGFW, Cloud Router, Cloud VPN,
Network Service Tiers, VPC, VPC Service Controls.

**S3NS additional:** API Registry, Cloud Billing, Cloud Code, Cloud Marketplace,
Container-Optimized OS, Lakehouse, Organization Policy, SDK docs,
Service Directory.

## Resolving ambiguity

When facing ambiguity or uncertainty about sovereign cloud behavior, features,
or configuration, always search the sovereign cloud documentation **before**
searching the public web. Public GCP docs and web results frequently describe
features or configurations that do not exist in sovereign cloud.

### Berlin (GCD) docs

Requires the `X-DevSite-Proxy: gcd` header:

```bash
# Cross-cutting docs
curl -s -H "X-DevSite-Proxy:gcd" "https://berlin.devsitetest.how/docs/<path>"

# Per-product docs
curl -s -H "X-DevSite-Proxy:gcd" "https://berlin.devsitetest.how/<product>/docs/<path>"

# Example: Compute Engine differences
curl -s -H "X-DevSite-Proxy:gcd" "https://berlin.devsitetest.how/compute/docs/tpc-differences"
```

### S3NS (Cloud de Confiance) docs

Directly accessible (no header needed):

```bash
# Cross-cutting docs
curl -s "https://documentation.s3ns.fr/docs/<path>"

# Per-product docs
curl -s "https://documentation.s3ns.fr/<product>/docs/<path>"

# Example: Compute Engine differences
curl -s "https://documentation.s3ns.fr/compute/docs/tpc-differences"
```

The response is HTML. Extract the article content and strip tags to read it.
Only fall back to public web search if the sovereign cloud docs do not cover
the topic.

## Code review for sovereign cloud

When reviewing a PR or diff that targets a sovereign cloud region, check
against this checklist. Load
[references/product-differences.md](references/product-differences.md) and
[references/gotchas.md](references/gotchas.md) for full details on any item.
When uncertain whether a feature is available, query the docs directly
(see "Resolving ambiguity" above) before approving.

### Endpoints and domains

- [ ] No hardcoded `googleapis.com` in API calls, configs, or client setup.
      Must use the region's endpoint domain (e.g., `compute.apis-berlin-build0.goog`
      or `compute.s3nsapis.fr`).
- [ ] `GOOGLE_CLOUD_UNIVERSE_DOMAIN` is set before using client libraries.
- [ ] OAuth scope URLs are left as `googleapis.com` (they stay the same).

### Project IDs

- [ ] Project IDs include the region prefix everywhere: Terraform, gcloud
      commands, API calls, IAM bindings, service account references.
      Berlin uses `eu0:`, S3NS uses `s3ns:`.

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
- [ ] No reliance on Preview features (generally unavailable).

### Architecture

- [ ] No multi-region assumptions: dual-region buckets, cross-region load
      balancing, multi-region storage classes, global endpoint routing.
- [ ] "Global" resources are understood to be scoped to the single region.
- [ ] HA designs use multiple zones within the region, not multiple regions.

### Authentication and identity

- [ ] No Cloud Identity, Google Accounts, or Google Groups as principals.
- [ ] Uses Workforce Identity Federation or service accounts only.
- [ ] No Cloud Shell references in scripts, CI, or documentation.
- [ ] Service account emails use the region's SA domain (not `.iam.gserviceaccount.com`).

### Terraform and IaC

- [ ] Provider block includes `universe_domain` with the correct region domain.
- [ ] GCS backend for state uses `storage_custom_endpoint` for the region.
- [ ] No Terraform resources for unavailable services.
- [ ] Machine types are C3, M3, or A3 Edge only.
- [ ] Disk types are `hyperdisk-balanced` only.
- [ ] Image projects use the region prefix (e.g., `eu0-system:debian-cloud`
      or `s3ns-system:debian-cloud`).

### Networking

- [ ] Does not assume a default VPC exists (sovereign cloud does not auto-create one).
- [ ] Uses zonal DNS names only (no global DNS).
- [ ] DNS zones are private only (public DNS zones unavailable).
- [ ] Private Google Access uses region-specific VIPs and domains.

### GKE specifics

- [ ] Cluster mode is Autopilot (not Standard).
- [ ] VPC-native clusters only (no route-based).
- [ ] Max 32 Pods per node.
- [ ] Workload identity uses the region's domain (`eu0.svc.id.goog` for Berlin).
- [ ] No Binary Authorization, Config Sync, or fleet management.
- [ ] Cloud Storage FUSE CSI requires `custom-endpoint` mount option.

### Cloud Storage

- [ ] Bucket location is single-region only (no dual-region or multi-region).
- [ ] Location is explicitly set (no default location).
- [ ] No domain-named buckets or custom domain content serving.
- [ ] HMAC keys use service accounts (not user accounts).

### IAM

- [ ] Principals are service accounts or Workforce/Workload Identity only.
- [ ] No Google Accounts or Google Groups in IAM bindings.
- [ ] No use of PAM, PAB, or Policy Intelligence tools.
- [ ] Service agent domains use the region prefix
      (`eu0-system` for Berlin, `s3ns-system` for S3NS).

### Naming and documentation

- [ ] Does not describe operator-managed resources as "Google-managed".

## How to help

When a user asks about Google Cloud and appears to be working in a sovereign
cloud context:

1. Identify whether they are targeting Berlin, S3NS, or public GCP
2. If sovereign cloud, load the relevant reference files above
3. Apply the gotchas - especially universe domain, project prefix, and endpoint differences
4. If they paste code or config from public GCP docs, adapt it for the correct region
5. If they reference an unavailable service, explain it is not available and suggest alternatives
6. When uncertain about any detail, query the region's docs directly (see above) before searching the web
