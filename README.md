# Google Cloud Dedicated (GCD) Agent Skill

An [Agent Skill](https://agentskills.io) that gives AI coding agents expertise in Google Cloud's sovereign cloud platforms - Google Cloud Dedicated (Berlin) and Cloud de Confiance by S3NS (France). Works with Claude Code, Cursor, Gemini CLI, VS Code Copilot, and any other agent that supports the agentskills standard.

These sovereign clouds are separate products from public Google Cloud, running in isolated regions with strict data residency guarantees. Developers moving from GCP regularly hit differences in service availability, API endpoints, authentication, and tooling. This skill catches those issues before they become wasted hours.

## Supported regions

| Region | Product name | Identifier | Docs |
|---|---|---|---|
| Berlin, Germany | Google Cloud Dedicated in Germany | `u-germany-northeast1` | `berlin.devsitetest.how` |
| France | Cloud de Confiance by S3NS | `u-france-east1` | `documentation.s3ns.fr` |

## What it does

When activated, the skill provides:

- Sovereign-cloud-specific guidance for architecture, authentication, Terraform, and developer tooling
- Automatic detection of public GCP patterns that won't work in sovereign clouds (wrong endpoints, unavailable services, missing universe domain config)
- Per-product difference details for available services in each region
- Multi-region awareness with region-specific identifiers (endpoints, project prefixes, SA domains, image projects)

## Installation

### Claude Code - as a project skill (recommended)

Clone the repo and symlink it into your project's `.claude/skills/` directory:

```bash
# Clone the skill repo
git clone https://github.com/rochacbruno/gcd-claude-skill.git

# From your project root, create the skills directory and symlink
mkdir -p .claude/skills
ln -s /path/to/gcd-claude-skill .claude/skills/gcd
```

The skill activates automatically when Claude detects sovereign-cloud-related work in that project. You can also invoke it directly with `/gcd`.

To share with your team, commit the symlink:

```bash
git add .claude/skills/gcd
git commit -m "Add GCD skill"
```

### Claude Code - as a personal skill

Symlink into your personal skills directory so the skill is available across all projects:

```bash
git clone https://github.com/rochacbruno/gcd-claude-skill.git
mkdir -p ~/.claude/skills
ln -s /path/to/gcd-claude-skill ~/.claude/skills/gcd
```

### Claude Code - as a plugin

The repo includes a `.claude-plugin/plugin.json` manifest, so it can be loaded as a plugin:

```bash
# Load via additional directory
claude --add-dir /path/to/gcd-claude-skill

# Or place in skills dir and it auto-loads as a skills-directory plugin
mkdir -p ~/.claude/skills
ln -s /path/to/gcd-claude-skill ~/.claude/skills/gcd
```

### Other agents (Cursor, Gemini CLI, VS Code Copilot, etc.)

Clone the repo and place (or symlink) the `SKILL.md` and `references/` directory where your agent discovers skills. The skill follows the open [agentskills.io](https://agentskills.io) standard and requires no agent-specific configuration.

## Structure

```
gcd-claude-skill/
  SKILL.md                              # Main skill (agentskills standard)
  .claude-plugin/
    plugin.json                         # Claude Code plugin manifest
  references/
    overview.md                         # Architecture, regions, zones, sovereignty model
    key-differences.md                  # Top-level sovereign cloud vs public GCP differences
    services.md                         # Available services and limitations
    product-differences.md              # Per-product sovereign cloud vs GCP differences
    authentication.md                   # Identity, credentials, ADC, tokens
    developer-guide.md                  # gcloud CLI, client libraries, API endpoints
    terraform.md                        # Terraform/IaC configuration
    organization-setup.md               # Org setup, IdP, Fabric FAST toolkit
    quotas.md                           # Quota management, monitoring, CLI
    gotchas.md                          # Critical pitfalls and common mistakes
  scripts/
    scrape-gcd-docs.py                  # Documentation scraper (HTTP SSR + optional Playwright)
    sync-skill.py                       # Synchronizes SKILL.md, references/, and README.md from scraped docs
  docs-raw/                             # Scraped Berlin (GCD) docs
    _manifest.json                      # Page inventory with metadata
    _last_updated.json                  # Per-page last-updated dates
  docs-raw-s3ns/                        # Scraped S3NS (Cloud de Confiance) docs
    _manifest.json
    _last_updated.json
  LICENSE                               # Apache-2.0
```

## Documentation coverage

The skill's reference files are synthesized and automatically synchronized from scraped pages covering both sovereign cloud documentation sites (`/products`, `/release-notes`, `/docs/*`, and all product documentation hubs).

### Reference files

| Reference file | Content |
|---|---|
| `product-differences.md` | Per-product sovereign cloud vs GCP differences across all 38 product `tpc-differences` pages (Compute, BigQuery, Bigtable, Cloud Run, GKE, IAM, Secret Manager, Composer, Managed Spark, Filestore, Storage Transfer, Networking, etc.) |
| `services.md` | Complete catalog of available and unavailable services by Technology Area, plus auto-synced documentation inventory |
| `terraform.md` | Provider config, state storage, resources, best practices |
| `quotas.md` | Quota management, monitoring, gcloud CLI examples |
| `authentication.md` | Workforce Identity Federation, ADC, tokens, client libraries |
| `developer-guide.md` | gcloud CLI setup, client libraries, API endpoints, Discovery API |
| `overview.md` | Architecture, universes, regions, zones, billing, support |
| `organization-setup.md` | Org setup paths (minimal/basic/enterprise), IdP, Fabric FAST |
| `key-differences.md` | Comprehensive top-level sovereign cloud vs GCP differences |
| `gotchas.md` | Synthesized from all sources |

### Technology Areas covered

Every item in the sovereign cloud docs "Technology Areas" menu is covered:

- Access and resource management
- AI and ML (Agent Platform / BigQuery ML)
- Application development
- Application hosting
- Compute
- Data analytics
- Databases
- Networking technologies
- Observability and monitoring
- Security
- Storage
- Infrastructure as code
- SDK, languages, frameworks, and tools

### Per-product differences covered

Each available service has its `tpc-differences` page plus region-specific sub-pages scraped and synchronized into `references/product-differences.md`:

<!-- AUTO-SYNC:COVERAGE-TABLE:START -->
Total scraped pages: **434** in `docs-raw/` (Berlin GCD) and **433** in `docs-raw-s3ns/` (S3NS Cloud de Confiance).

| Product | Berlin Pages | S3NS Pages | S3NS SecNumCloud 3.2 | Includes |
|---|---:|---:|---|---|
| Access Context Manager | 8 | 8 | Qualifié SecNumCloud 3.2 | Landing, differences, access levels, policies |
| Access Transparency | 7 | 7 | Qualification en cours | Landing, overview, logs, access approvals |
| Agent Platform (Gemini Enterprise Agent Platform) | 7 | 7 | Qualification en cours | Landing, differences, Model Garden, online inference, open-weight models |
| API Keys | 4 | 4 | — | Landing, API key restrictions, quotas, REST reference |
| Artifact Registry | 6 | 6 | Qualifié SecNumCloud 3.2 | Landing, differences, Docker/Apt/Yum, access control, quickstarts |
| BigQuery | 16 | 16 | Qualifié SecNumCloud 3.2 | Landing, differences, bq CLI, quotas, quickstarts, data loading, reservations |
| Bigtable | 14 | 14 | Qualification en cours | Landing, differences, instances, replication, backups, CMEK, change streams |
| Cloud Armor | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, security policies, WAF rules, rate limiting |
| Cloud Billing | 8 | 8 | — | Landing, differences, BigQuery billing export, access control |
| Cloud DNS | 8 | 8 | Qualifié SecNumCloud 3.2 | Landing, differences, private zones, records, forwarding, peering |
| Cloud Interconnect | 2 | 2 | Qualifié SecNumCloud 3.2 | Landing, differences, Dedicated & Partner Interconnect, MACsec |
| Cloud KMS | 8 | 8 | Qualifié SecNumCloud 3.2 | Landing, differences, software keys, EKM, CMEK, key import |
| Cloud Load Balancing | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, regional Application & Network Load Balancers |
| Cloud Logging | 10 | 10 | Qualifié SecNumCloud 3.2 | Landing, differences, audit logs, log buckets, sinks, queries |
| Cloud Monitoring | 4 | 4 | Qualifié SecNumCloud 3.2 | Landing, differences, PromQL, Prometheus export, client libraries |
| Cloud NAT | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, Public NAT, GCE/GKE configuration |
| Cloud NGFW | 3 | 3 | — | Landing, differences, firewall rules, hierarchical & network policies |
| Cloud Quotas | 29 | 29 | Qualification en cours | Landing, differences, quota viewing, adjustment requests, REST API |
| Cloud Router | 2 | 2 | Qualifié SecNumCloud 3.2 | Landing, differences, regional dynamic BGP routing |
| Cloud Run | 14 | 14 | Qualification en cours | Landing, differences, container services & jobs, Direct VPC egress |
| Cloud SQL | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, MySQL & PostgreSQL Enterprise Plus, C3 series |
| Cloud Storage | 10 | 10 | Qualifié SecNumCloud 3.2 | Landing, differences, single-region buckets, uploads, FUSE, HMAC |
| Cloud VPN | 2 | 2 | Qualifié SecNumCloud 3.2 | Landing, differences, HA VPN topologies and tunnels |
| Compute Engine | 9 | 9 | Qualifié SecNumCloud 3.2 | Landing, differences, C3/M3/A3 VMs, Hyperdisk, Shielded VM, OS images |
| Container-Optimized OS | 3 | 3 | — | Landing, differences, H100 GPU drivers, release notes |
| Filestore | 16 | 16 | Qualification en cours | Landing, differences, Regional tier NFS, Direct Peering, GKE CSI |
| Google Kubernetes Engine (GKE) | 9 | 9 | Qualifié SecNumCloud 3.2 | Landing, differences, Autopilot clusters, Workload Identity, Storage FUSE |
| IAM | 18 | 18 | Qualifié SecNumCloud 3.2 | Landing, differences, Workforce/Workload Identity, service accounts, custom roles |
| Managed Airflow (Cloud Composer 3) | 18 | 18 | Qualification en cours | Landing, differences, Composer 3 HA environments, DAGs, plugins |
| Managed Service for Apache Spark (Dataproc) | 10 | 10 | Qualification en cours | Landing, differences, GCE Spark clusters (image 2.3+), jobs, CMEK |
| Network Service Tiers | 3 | 3 | — | Landing, differences, Premium Tier overview |
| Organization Policy | 3 | 3 | Qualifié SecNumCloud 3.2 | Landing, differences, managed & custom constraints |
| Pub/Sub | 11 | 11 | Qualifié SecNumCloud 3.2 | Landing, differences, topics, push/pull subscriptions, IAM |
| Resource Manager | 11 | 11 | Qualifié SecNumCloud 3.2 | Landing, differences, organizations, folders, projects, tags |
| Secret Manager | 10 | 10 | Qualification en cours | Landing, differences, global & regional secrets, v1 API, CMEK |
| Service Usage | 9 | 9 | Qualifié SecNumCloud 3.2 | Landing, differences, enabling/disabling services, REST reference |
| Storage Transfer Service | 7 | 7 | Qualification en cours | Landing, differences, GCS transfers, agent-based S3 transfers |
| Terraform | 32 | 32 | — | Landing, differences, provider universe_domain, GCS state backend |
| VPC | 7 | 7 | Qualifié SecNumCloud 3.2 | Landing, differences, subnets, Private Google Access, Private Service Connect |
| VPC Service Controls | 3 | 3 | — | Landing, differences, service perimeters, ingress/egress rules |
<!-- AUTO-SYNC:COVERAGE-TABLE:END -->

## Updating the docs

The scraper uses parallel HTTP SSR requests (with automatic product discovery from `/products`, `/release-notes`, and `/docs/*` Technology Area hubs) and tracks last-updated dates for each page. An optional `--use-playwright` flag is available if headless browser rendering is needed.

### Run the scraper and synchronize the skill

```bash
# Scrape Berlin only (default)
python3 scripts/scrape-gcd-docs.py --region berlin

# Scrape S3NS only
python3 scripts/scrape-gcd-docs.py --region s3ns

# Scrape both regions
python3 scripts/scrape-gcd-docs.py --region all

# Synchronize SKILL.md, references/services.md, references/product-differences.md, and README.md
python3 scripts/sync-skill.py
```

Each region's docs are scraped into their respective output directory (`docs-raw/` for Berlin, `docs-raw-s3ns/` for S3NS). Running `python3 scripts/sync-skill.py` parses both regions' manifests and `*_tpc-differences.md` pages, automatically updating product inventories, coverage tables, and injecting new product difference sections whenever new services are added to the documentation.

## License

Apache-2.0
