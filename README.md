# Google Cloud Dedicated (GCD) Agent Skill

An [Agent Skill](https://agentskills.io) that gives AI coding agents expertise in Google Cloud Dedicated - Google's sovereign cloud platform. Works with Claude Code, Cursor, Gemini CLI, VS Code Copilot, and any other agent that supports the agentskills standard.

GCD is a separate product from public Google Cloud, running in isolated sovereign regions with strict data residency guarantees. Developers moving from GCP to GCD regularly hit differences in service availability, API endpoints, authentication, and tooling. This skill catches those issues before they become wasted hours.

## What it does

When activated, the skill provides:

- GCD-specific guidance for architecture, authentication, Terraform, and developer tooling
- Automatic detection of public GCP patterns that won't work in GCD (wrong endpoints, unavailable services, missing universe domain config)
- Per-product difference details for all 16 available GCD services
- Region-agnostic advice - Berlin (`u-germany-northeast1`) is the reference region, but the skill adapts to any GCD region

## Installation

### Claude Code - as a skill

Copy or symlink into your personal skills directory:

```bash
# Personal skill (available in all projects)
cp -r /path/to/gcd-claude-skill ~/.claude/skills/gcd

# Or project skill (available in one project)
cp -r /path/to/gcd-claude-skill .claude/skills/gcd
```

### Claude Code - as a plugin

The repo includes a `.claude-plugin/plugin.json` manifest, so it can be loaded as a plugin:

```bash
# Load via additional directory
claude --add-dir /path/to/gcd-claude-skill

# Or place in skills dir and it auto-loads as a skills-directory plugin
```

### Other agents (Cursor, Gemini CLI, VS Code Copilot, etc.)

Place the `SKILL.md` and `references/` directory where your agent discovers skills. The skill follows the open [agentskills.io](https://agentskills.io) standard and requires no agent-specific configuration.

## Structure

```
gcd-claude-skill/
  SKILL.md                              # Main skill (agentskills standard)
  .claude-plugin/
    plugin.json                         # Claude Code plugin manifest
  references/
    overview.md                         # Architecture, regions, zones, sovereignty model
    key-differences.md                  # Top-level GCD vs public GCP differences
    services.md                         # Available services and limitations
    product-differences.md              # Per-product GCD vs GCP differences
    authentication.md                   # Identity, credentials, ADC, tokens
    developer-guide.md                  # gcloud CLI, client libraries, API endpoints
    terraform.md                        # Terraform/IaC configuration for GCD
    organization-setup.md               # Org setup, IdP, Fabric FAST toolkit
    quotas.md                           # Quota management, monitoring, CLI
    gotchas.md                          # Critical pitfalls and common mistakes
  scripts/
    scrape-gcd-docs.py                  # Documentation scraper (Playwright)
  docs-raw/                             # Scraped raw docs (264 pages)
    _manifest.json                      # Page inventory with metadata
    _last_updated.json                  # Per-page last-updated dates
  LICENSE                               # Apache-2.0
```

## Documentation coverage

The skill's reference files are synthesized from 264 scraped pages covering the full GCD documentation site: 126 cross-cutting GCD docs, 16 product landing pages, 16 per-product tpc-differences pages, and 106 product sub-pages with GCD-specific content.

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

### Technology Areas covered

Every item in the GCD docs "Technology Areas" menu is covered:

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

Each available GCD service has its `tpc-differences` page plus GCD-specific sub-pages scraped and synthesized into `references/product-differences.md`:

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

The scraper uses Playwright to render JS-heavy DevSite pages and tracks last-updated dates for each page.

### Prerequisites

```bash
uv venv && source .venv/bin/activate
uv pip install playwright
playwright install chromium
```

### Run the scraper

```bash
python3 scripts/scrape-gcd-docs.py
```

This re-scrapes all 264 pages into `docs-raw/`, updating `_manifest.json` and `_last_updated.json`. Compare `_last_updated.json` against a previous run to identify which pages changed.

After scraping, the reference files in `references/` should be regenerated to incorporate any documentation updates.

## License

Apache-2.0
