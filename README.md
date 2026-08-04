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
    scrape-gcd-docs.py                  # Documentation scraper (Playwright)
  docs-raw/                             # Scraped Berlin (GCD) docs
    _manifest.json                      # Page inventory with metadata
    _last_updated.json                  # Per-page last-updated dates
  docs-raw-s3ns/                        # Scraped S3NS (Cloud de Confiance) docs
    _manifest.json
    _last_updated.json
  LICENSE                               # Apache-2.0
```

## Documentation coverage

The skill's reference files are synthesized from scraped pages covering both sovereign cloud documentation sites.

### Berlin (GCD) - scraped from berlin.devsitetest.how

| Reference file | Pages covered | Content |
|---|---|---|
| `product-differences.md` | 122 | Per-product GCD vs GCP differences, plus GCD-specific product sub-pages (Compute, BigQuery, Storage, IAM, GKE, DNS, KMS, Logging, Monitoring, Pub/Sub, etc.) |
| `terraform.md` | 32 | Provider config, state storage, resources, best practices |
| `services.md` | 29 | Product landing pages and Technology Area categories |
| `quotas.md` | 28 | Quota management, monitoring, gcloud CLI examples |
| `authentication.md` | 21 | Workforce Identity Federation, ADC, tokens, client libraries |
| `developer-guide.md` | 20 | gcloud CLI setup, client libraries, API endpoints, Discovery API |
| `overview.md` | 6 | Architecture, universes, regions, zones, billing, support |
| `organization-setup.md` | 5 | Org setup paths (minimal/basic/enterprise), IdP, Fabric FAST |
| `key-differences.md` | 1 | Comprehensive top-level GCD vs GCP differences |
| `gotchas.md` | -- | Synthesized from all sources |

### S3NS (Cloud de Confiance) - scraped from documentation.s3ns.fr

The S3NS region has a broader product catalog including additional networking products (VPC, Cloud NAT, Cloud VPN, Cloud Interconnect, Cloud Router, Cloud Load Balancing, Cloud NGFW, VPC Service Controls, Cloud Armor, Network Service Tiers) and tools (Cloud Code, Lakehouse, Cloud Billing, API Registry, Cloud Marketplace, Organization Policy, Service Directory). The scraped docs are in `docs-raw-s3ns/`.

### Technology Areas covered

Every item in the sovereign cloud docs "Technology Areas" menu is covered:

- Access and resource management
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

Each available service has its `tpc-differences` page plus region-specific sub-pages scraped and synthesized into `references/product-differences.md`:

| Product | Pages | Includes |
|---|---|---|
| Access Context Manager | 8 | Landing, differences, access levels, policies |
| API Keys | 5 | Landing, differences, quotas, REST reference |
| Artifact Registry | 6 | Landing, differences, access control, quickstarts |
| BigQuery | 15 | Landing, differences, bq CLI, quotas, quickstarts, data loading |
| Compute Engine | 6 | Landing, differences, create VM, SSH, REST reference |
| Cloud DNS | 8 | Landing, differences, zones, records, policies |
| Cloud KMS | 8 | Landing, differences, key creation, import, retrieval |
| Cloud Logging | 10 | Landing, differences, audit, buckets, queries, log writing |
| Cloud Monitoring | 4 | Landing, differences, client libraries |
| Cloud SQL | 3 | Landing, differences, release notes |
| Google Kubernetes Engine | 9 | Landing, differences, cluster creation, workload identity |
| IAM | 15 | Landing, differences, roles, service accounts, custom roles |
| Pub/Sub | 11 | Landing, differences, topics, publishing, access control |
| Resource Manager | 11 | Landing, differences, projects, folders, tags |
| Service Usage | 9 | Landing, differences, enable/disable, setup |
| Cloud Storage | 10 | Landing, differences, bucket creation, uploads, APIs |

## Updating the docs

The scraper uses Playwright to render JS-heavy DevSite pages and tracks last-updated dates for each page. It supports scraping both regions independently.

### Prerequisites

```bash
uv venv && source .venv/bin/activate
uv pip install playwright
playwright install chromium
```

### Run the scraper

```bash
# Scrape Berlin only (default)
python3 scripts/scrape-gcd-docs.py --region berlin

# Scrape S3NS only
python3 scripts/scrape-gcd-docs.py --region s3ns

# Scrape both regions
python3 scripts/scrape-gcd-docs.py --region all
```

Each region's docs are scraped into their respective output directory (`docs-raw/` for Berlin, `docs-raw-s3ns/` for S3NS). Compare `_last_updated.json` against a previous run to identify which pages changed.

After scraping, the reference files in `references/` should be regenerated to incorporate any documentation updates.

## License

Apache-2.0
