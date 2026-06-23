# Google Cloud Dedicated (GCD) - Overview Reference

## What is Google Cloud Dedicated?

Google Cloud Dedicated (GCD) is a sovereign cloud platform built on the same technology as Google Cloud, but operating as a fully independent, self-contained universe. It provides Google's cloud services with strict data and operational sovereignty guarantees - no data leaves the local jurisdiction.

GCD is a **separate product** from Google Cloud. It runs as an isolated cloud with its own networking, completely disconnected from Google Cloud's network and the public internet.

Key characteristics:

- Built on the same technology as Google Cloud, but only a subset of products and features are available
- Completely standalone - no connection to Google Cloud's network
- Strong data sovereignty - all data stays within the local jurisdiction
- Designed for workloads with enhanced regulatory requirements
- Only external identity providers are supported (via Workforce Identity Federation)
- Domain names, API endpoints, and tooling differ from Google Cloud

## Architecture: Universes, Regions, and Zones

### Universes

A **universe** is a fully self-contained cloud with its own networking, separate from the public internet and all other universes. Google Cloud is one universe (global, multi-region). Each GCD deployment is another, smaller universe scoped to a single jurisdiction.

### Regions

Each GCD universe currently operates as a **single region**. Multi-region features (cross-region load balancing, multi-region storage) are not available.

**Berlin region (Germany):** `u-germany-northeast1`

Berlin is one GCD region - the architecture and concepts described here apply to any current or future sovereign GCD region.

### Zones

Regions are divided into **zones** - independent failure domains with high-bandwidth, low-latency interconnections. Deploy across multiple zones for fault tolerance.

**Berlin zones:**
- `u-germany-northeast1-a`
- `u-germany-northeast1-b`
- `u-germany-northeast1-c`

### Resource Scoping

- **Zonal resources** (e.g., VMs, zonal disks) - must be in the same zone to interact (e.g., attaching a disk to a VM)
- **Regional resources** (e.g., static external IPs) - usable by any resource in the region regardless of zone
- **Global resources** - exist conceptually for API compatibility with Google Cloud code, but are equivalent to resources scoped to the single region (e.g., `u-germany-northeast1`)

## Domain Names and Endpoints

GCD uses different domain names from Google Cloud. These are specific to each GCD universe.

**Berlin universe examples:**
- Documentation site: `berlin.devsitetest.how`
- Console: `console.cloud.berlin-build0.goog`
- API endpoints: `*.apis-berlin-build0.goog` (e.g., `compute.apis-berlin-build0.goog` instead of `compute.googleapis.com`)

## Projects

Every GCD resource must belong to a project. Projects work similarly to Google Cloud projects with one key difference:

- All GCD project IDs are automatically prefixed with `eu0:` (e.g., `eu0:my-project`)
- Setting a default project: `gcloud config set project eu0:my-project`
- Each project is associated with one billing account
- A project serves as a namespace - resource names must be unique within a project

## Key Differences from Google Cloud

- **Identity:** Only external identity providers via Workforce Identity Federation (no Google-managed identities)
- **Multi-region:** No cross-region features (no multi-region storage, no cross-region load balancing)
- **API endpoints:** Different domain names for all service endpoints
- **Machine types:** Older Compute Engine machine types are unavailable
- **Tools:** Some Google Cloud tools are unavailable or work differently (e.g., Cloud Shell is not available)
- **Documentation:** GCD docs are derived from Google Cloud docs but exclude unavailable features; broken links may occasionally appear

## Available Services

GCD supports a subset of Google Cloud services. Key categories include:

- **Compute:** Compute Engine, GKE (Google Kubernetes Engine)
- **Storage:** Cloud Storage
- **Databases:** Cloud SQL, BigQuery
- **Networking:** VPC, Cloud DNS, Cloud Load Balancing, Cloud NAT, Cloud VPN, Cloud Interconnect, Cloud Router, Cloud Armor, Cloud Next Generation Firewall
- **Security:** IAM, Cloud KMS, Access Context Manager, VPC Service Controls
- **Observability:** Cloud Logging, Cloud Monitoring
- **Messaging:** Pub/Sub
- **Management:** Resource Manager, Service Usage
- **Containers:** Artifact Registry

Each service has a dedicated "differences page" documenting what varies from the Google Cloud version. These are located at paths like `/[service]/docs/tpc-differences` (e.g., `/compute/docs/tpc-differences`).

## Interacting with GCD

Four primary methods:

1. **Console** - Web UI at `console.cloud.berlin-build0.goog`
2. **gcloud CLI** - Requires one-time configuration to target the GCD universe and identity provider
3. **Client libraries** - Available for Python, Java, Go, JavaScript/Node.js, C#/.NET, PHP, C++, Ruby, Rust; must specify target universe
4. **Terraform** - Infrastructure as code via the Google Cloud Terraform provider

## Getting Started Workflow

### For platform admins (one-time setup):
1. Set up an identity provider (Workforce Identity Federation)
2. Configure the organization (projects, network, resources)

### For developers:
1. Set up API access
2. Configure the gcloud CLI for GCD (universe targeting + IdP configuration)
3. Configure client libraries with the target universe

## Billing

- GCD uses Cloud Billing, but not all Google Cloud billing features are available
- A valid Cloud Billing account is required and must be linked to GCD projects
- Multiple projects can bill to the same account
- Detailed pricing information is provided separately per deployment

## Support

Support during preview is provided by Google. The process requires:

1. A dedicated Google Cloud project (not a GCD project) specifically for support cases
2. A Google Cloud organization with an Assured Workloads folder configured for EU Data Boundary and Support
3. Support cases are filed through the Google Cloud console (not the GCD console) against this dedicated project
4. Cases are routed to the GCD support team in the EU

Key detail: the support project must be an empty Google Cloud project inside an Assured Workloads folder with the "EU Data Boundary and Support" control package selected.

## Documentation Structure

GCD documentation lives at the documentation site for each universe (e.g., `berlin.devsitetest.how/docs` for Berlin). It mirrors Google Cloud documentation but excludes pages for unavailable services.

Key documentation sections:
- Overview and key differences: `/docs/overview/tpc-overview`, `/docs/overview/tpc-key-differences`
- Getting started: `/docs/get-started-tpc`
- Regions and zones: `/docs/get-started-tpc/regions-and-zones`
- Per-service differences: `/[service]/docs/tpc-differences`
- Products list: `/products`
- Billing: `/docs/overview/tpc-billing`, `/billing/docs/concepts`

A banner on documentation pages indicates when content might not yet be relevant to the GCD universe.
