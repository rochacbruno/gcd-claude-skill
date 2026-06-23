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

## How to help

When a user asks about Google Cloud and appears to be working in a GCD context:

1. Identify whether they are targeting GCD or public GCP
2. If GCD, load the relevant reference files above
3. Apply the gotchas -- especially universe domain, project prefix, and endpoint differences
4. If they paste code or config from public GCP docs, adapt it for GCD
5. If they reference an unavailable service, explain it is not in GCD and suggest alternatives
6. When uncertain about any detail, query the GCD docs directly (see above) before searching the web
