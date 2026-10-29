# Google Cloud Dedicated (GCD) & Cloud de Confiance (S3NS) - Overview Reference

## What are Google Cloud Dedicated and Cloud de Confiance?

**Google Cloud Dedicated (GCD)** in Germany and **Cloud de Confiance by S3NS** (PREMI3NS) in France are sovereign cloud platforms built on the same technology as Google Cloud, but operating as fully independent, self-contained universes. They provide Google Cloud services with strict data and operational sovereignty guarantees — no data leaves the local jurisdiction, and the platform is operated by a dedicated local entity (such as S3NS in France under ANSSI **SecNumCloud 3.2** qualification).

Each sovereign cloud is a **separate product** from public Google Cloud. It runs as an isolated cloud with its own networking, completely disconnected from Google Cloud's network.

Key characteristics:

- Built on the same technology as Google Cloud, with a curated set of sovereign cloud products and features
- Completely standalone — no connection to public Google Cloud's network
- Strong data and operational sovereignty — all customer data and metadata stay within the local jurisdiction
- Designed for workloads with enhanced regulatory and compliance requirements (including ANSSI **SecNumCloud 3.2**, HDS, and ISO 27001 on S3NS)
- Only external identity providers are supported for human users (via Workforce Identity Federation)
- Domain names, API endpoints, project ID prefixes, and tooling differ from public Google Cloud

## Architecture: Universes, Regions, and Zones

### Universes

A **universe** is a fully self-contained cloud with its own networking, separate from all other universes. Public Google Cloud is one universe (global, multi-region). Each sovereign cloud deployment is a separate universe scoped to a single jurisdiction.

### Regions and Zones

Each sovereign cloud universe operates as a **single region** divided into **three zones** (independent failure domains with high-bandwidth, low-latency interconnections). Multi-region features (cross-region load balancing, multi-region storage) are not available — deploy across multiple zones within the region for high availability.

| Attribute | Berlin (GCD — Germany) | France (S3NS — Cloud de Confiance) |
|---|---|---|
| **Region** | `u-germany-northeast1` | `u-france-east1` |
| **Zones** | `u-germany-northeast1-a`, `-b`, `-c` | `u-france-east1-a`, `-b`, `-c` |
| **Universe domain** | `apis-berlin-build0.goog` | `s3nsapis.fr` |
| **Project ID prefix** | `eu0:` | `s3ns:` |
| **Console URL** | `https://console.cloud.berlin-build0.goog` | `https://console.cloud.s3nscloud.fr` |
| **Documentation site** | `https://berlin.devsitetest.how` | `https://documentation.s3ns.fr` |
| **Support portal** | Dedicated EU support project in GCP console | `https://support.s3ns.fr` |

### Resource Scoping

- **Zonal resources** (e.g., VMs, zonal disks, Bigtable clusters) — must be in the same zone to interact directly (e.g., attaching a zonal disk to a VM)
- **Regional resources** (e.g., regional external/internal load balancers, Filestore Regional instances, Cloud Run services) — usable across zones within the region
- **Global resources** — exist conceptually for API compatibility with Google Cloud code, but are physically scoped to the single sovereign region (`u-germany-northeast1` or `u-france-east1`)

## Domain Names and Endpoints

Each sovereign cloud universe uses its own domain names:

- **Berlin (GCD):** API endpoints use `*.apis-berlin-build0.goog` (e.g., `compute.apis-berlin-build0.goog`), Cloud Run URLs use `*.run-berlin-build0.goog`
- **France (S3NS):** API endpoints use `*.s3nsapis.fr` (e.g., `compute.s3nsapis.fr`), Cloud Run URLs use `*.s3nsrun.fr`

## Projects

Every resource must belong to a project. Projects work similarly to Google Cloud projects with one key difference:

- All project IDs are automatically prefixed with the universe prefix:
  - **Berlin (GCD):** `eu0:` (e.g., `eu0:my-project`)
  - **France (S3NS):** `s3ns:` (e.g., `s3ns:my-project`)
- Setting a default project: `gcloud config set project s3ns:my-project` (or `eu0:my-project`)
- Each project is associated with one billing account
- A project serves as a namespace — resource names must be unique within a project

## Key Differences from Google Cloud

- **Identity:** Only external identity providers via Workforce Identity Federation (no Google-managed identities)
- **Multi-region:** No cross-region features (no multi-region storage, no cross-region load balancing)
- **API endpoints:** Universe-specific domain names for all service endpoints
- **Machine types:** Modern Compute Engine machine families (`C3`, `M3`, `A3`) and Hyperdisk (`hyperdisk-balanced`); older machine families (`E2`, `N1`, `N2`, `T2D`) are unavailable
- **Tools:** Cloud Shell, Cloud Workstations, and Cloud Code are not available
- **SecNumCloud 3.2 (S3NS):** On S3NS PREMI3NS, 29 services are **Qualifié SecNumCloud 3.2** and 10 recently released services are in **Qualification en cours** (available today, ANSSI qualification in progress) — see [services.md](services.md)

## Available Services

Both sovereign cloud regions support a comprehensive set of Google Cloud services across Compute, Containers, AI/ML, Storage, Databases, Analytics, Networking, Security, and Observability:

- **Compute & Containers:** Compute Engine (`C3`, `M3`, `A3`, Hyperdisk, Shielded VM), GKE (Autopilot only), Cloud Run (services & jobs), Container-Optimized OS, Artifact Registry
- **AI & Machine Learning:** Agent Platform / Gemini Enterprise Agent Platform (Model Garden & online inference for open-weight models like Gemma and Mistral), BigQuery ML (internal models)
- **Storage & Transfer:** Cloud Storage (single-region), Filestore (Regional tier NFS), Storage Transfer Service (GCS & agent-based S3)
- **Databases:** Cloud SQL (MySQL & PostgreSQL Enterprise Plus on C3), Bigtable (single-region, multi-zone replication)
- **Data Analytics & Orchestration:** BigQuery (with Storage, Data Policy, Reservation, BigLake), Managed Service for Apache Spark / Dataproc (GCE clusters on image 2.3+), Managed Airflow / Cloud Composer 3 (Highly Resilient Large/Custom), Pub/Sub
- **Networking:** VPC, Cloud DNS, Cloud Load Balancing (regional), Cloud NAT, Cloud VPN (HA VPN), Cloud Interconnect, Cloud Router, Cloud Armor (Standard), Cloud NGFW (Essentials & Standard), Network Service Tiers (Premium), Private Service Connect, Service Directory, VPC Service Controls
- **Security & Governance:** IAM, Secret Manager, Cloud KMS & EKM, Access Context Manager, Access Transparency, Organization Policy, API Keys, Workforce/Workload Identity Federation
- **Observability & Management:** Cloud Logging, Cloud Monitoring (PromQL/Grafana), Cloud Billing, Cloud Quotas, Resource Manager, Service Usage, Terraform

Each service has a dedicated differences section in [product-differences.md](product-differences.md) documenting what varies from public Google Cloud (`/[service]/docs/tpc-differences`).

## Interacting with GCD and S3NS

Four primary methods:

1. **Console** — Web UI at `console.cloud.berlin-build0.goog` (Berlin) or `console.cloud.s3nscloud.fr` (S3NS)
2. **gcloud CLI** — Configured to target the sovereign cloud universe (`apis-berlin-build0.goog` or `s3nsapis.fr`) and Workforce Identity Federation
3. **Client libraries** — Available for Python, Java, Go, JavaScript/Node.js, C#/.NET, PHP, C++, Ruby, Rust; requires `GOOGLE_CLOUD_UNIVERSE_DOMAIN`
4. **Terraform** — Infrastructure as code via the Google Cloud Terraform provider with `universe_domain` set (see [terraform.md](terraform.md))

## Getting Started Workflow

### For platform admins (one-time setup):
1. Set up an identity provider (Workforce Identity Federation)
2. Configure the organization (projects, network, resources via Fabric FAST — see [organization-setup.md](organization-setup.md))

### For developers:
1. Set up API access
2. Configure the `gcloud` CLI for the target universe + IdP configuration
3. Configure client libraries with `GOOGLE_CLOUD_UNIVERSE_DOMAIN`

## Billing

- Billing is handled by your sovereign cloud operator (Google Cloud Dedicated operator in Germany; S3NS in France)
- A valid Cloud Billing account is required and must be linked to projects
- Detailed usage and cost data can be exported to BigQuery (see [product-differences.md](product-differences.md))

## Support

- **France (S3NS — Cloud de Confiance):** Support cases are filed directly via the S3NS customer support portal at [https://support.s3ns.fr](https://support.s3ns.fr).
- **Berlin (GCD — Germany):** Support requires a dedicated empty Google Cloud project inside an Assured Workloads folder configured with the "EU Data Boundary and Support" control package; cases are filed in the Google Cloud console against that project and routed to the EU support team.

## Documentation Structure

Sovereign cloud documentation lives at `https://berlin.devsitetest.how` (Berlin) and `https://documentation.s3ns.fr` (S3NS).

Key documentation sections:
- Overview and key differences: `/docs/overview/tpc-overview`, `/docs/overview/tpc-key-differences`
- Getting started: `/docs/get-started-tpc`
- Regions and zones: `/docs/get-started-tpc/regions-and-zones`
- Per-service differences: `/[service]/docs/tpc-differences`
- Products list: `/products`
- Release notes: `/release-notes`
