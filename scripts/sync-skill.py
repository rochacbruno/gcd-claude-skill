#!/usr/bin/env python3
"""
Synchronize gcd-claude-skill capability files from scraped documentation.

Runs automatically in CI after `scripts/scrape-gcd-docs.py --region all`.
Reads `docs-raw/_manifest.json`, `docs-raw-s3ns/_manifest.json`,
`docs-raw-s3ns/_secnumcloud_status.json`, and all `*_tpc-differences.md` files
across both regions to:
1. Update the auto-synced product differences index in `references/product-differences.md`
   and automatically generate + insert a full `## <Product Name>` section for any
   newly discovered service with a `*_tpc-differences.md` page (or re-render any
   previously auto-generated section when its upstream `*_tpc-differences.md` changes).
2. Update the auto-synced available API services list, S3NS SecNumCloud 3.2 qualification
   breakdown, and discovered documentation inventory table in `references/services.md`.
3. Update the auto-synced available services and S3NS SecNumCloud 3.2 status summary in `SKILL.md`.
4. Update the auto-synced per-product coverage table and page statistics in `README.md`.
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parent.parent
BERLIN_DIR = BASE_DIR / "docs-raw"
S3NS_DIR = BASE_DIR / "docs-raw-s3ns"

PRODUCT_DIFFS_FILE = BASE_DIR / "references" / "product-differences.md"
SERVICES_FILE = BASE_DIR / "references" / "services.md"
SKILL_FILE = BASE_DIR / "SKILL.md"
README_FILE = BASE_DIR / "README.md"

# Cross-cutting tpc-differences files that are not per-product
PLATFORM_WIDE_TPC_FILES = {
    "tpc-differences.md",
    "overview_tpc-key-differences.md",
}

# Mapping from product slug (derived from filename prefix before _tpc-differences.md
# or manifest path) to canonical display name and section heading in product-differences.md
KNOWN_PRODUCT_META = {
    "access-context-manager": {
        "display": "Access Context Manager",
        "section": "Access Context Manager",
        "category": "general",
        "includes": "Landing, differences, access levels, policies",
    },
    "assured-workloads_access-transparency": {
        "display": "Access Transparency",
        "section": "Access Transparency",
        "category": "general",
        "includes": "Landing, overview, logs, access approvals",
    },
    "gemini-enterprise-agent-platform": {
        "display": "Agent Platform (Gemini Enterprise Agent Platform)",
        "section": "Agent Platform (Gemini Enterprise Agent Platform)",
        "category": "general",
        "includes": "Landing, differences, Model Garden, online inference, open-weight models",
    },
    "api-keys": {
        "display": "API Keys",
        "section": None,
        "category": "general",
        "includes": "Landing, API key restrictions, quotas, REST reference",
    },
    "artifact-registry": {
        "display": "Artifact Registry",
        "section": "Artifact Registry",
        "category": "general",
        "includes": "Landing, differences, Docker/Apt/Yum, access control, quickstarts",
    },
    "bigquery": {
        "display": "BigQuery",
        "section": "BigQuery",
        "category": "general",
        "includes": "Landing, differences, bq CLI, quotas, quickstarts, data loading, reservations",
    },
    "bigtable": {
        "display": "Bigtable",
        "section": "Bigtable",
        "category": "general",
        "includes": "Landing, differences, instances, replication, backups, CMEK, change streams",
    },
    "armor": {
        "display": "Cloud Armor",
        "section": "Cloud Armor",
        "category": "networking",
        "includes": "Landing, differences, security policies, WAF rules, rate limiting",
    },
    "billing": {
        "display": "Cloud Billing",
        "section": "Cloud Billing",
        "category": "general",
        "includes": "Landing, differences, BigQuery billing export, access control",
    },
    "dns": {
        "display": "Cloud DNS",
        "section": "Cloud DNS",
        "category": "networking",
        "includes": "Landing, differences, private zones, records, forwarding, peering",
    },
    "network-connectivity_interconnect": {
        "display": "Cloud Interconnect",
        "section": "Cloud Interconnect",
        "category": "networking",
        "includes": "Landing, differences, Dedicated & Partner Interconnect, MACsec",
    },
    "kms": {
        "display": "Cloud KMS",
        "section": "Cloud KMS",
        "category": "general",
        "includes": "Landing, differences, software keys, EKM, CMEK, key import",
    },
    "load-balancing": {
        "display": "Cloud Load Balancing",
        "section": "Cloud Load Balancing",
        "category": "networking",
        "includes": "Landing, differences, regional Application & Network Load Balancers",
    },
    "logging": {
        "display": "Cloud Logging",
        "section": "Logging",
        "category": "general",
        "includes": "Landing, differences, audit logs, log buckets, sinks, queries",
    },
    "monitoring": {
        "display": "Cloud Monitoring",
        "section": "Monitoring",
        "category": "general",
        "includes": "Landing, differences, PromQL, Prometheus export, client libraries",
    },
    "nat": {
        "display": "Cloud NAT",
        "section": "Cloud NAT",
        "category": "networking",
        "includes": "Landing, differences, Public NAT, GCE/GKE configuration",
    },
    "firewall": {
        "display": "Cloud NGFW",
        "section": "Cloud NGFW (Next Generation Firewall)",
        "category": "networking",
        "includes": "Landing, differences, firewall rules, hierarchical & network policies",
    },
    "quotas": {
        "display": "Cloud Quotas",
        "section": "Cloud Quotas",
        "category": "general",
        "includes": "Landing, differences, quota viewing, adjustment requests, REST API",
    },
    "network-connectivity_router": {
        "display": "Cloud Router",
        "section": "Cloud Router",
        "category": "networking",
        "includes": "Landing, differences, regional dynamic BGP routing",
    },
    "run": {
        "display": "Cloud Run",
        "section": "Cloud Run",
        "category": "general",
        "includes": "Landing, differences, container services & jobs, Direct VPC egress",
    },
    "sql": {
        "display": "Cloud SQL",
        "section": "Cloud SQL",
        "category": "general",
        "includes": "Landing, differences, MySQL & PostgreSQL Enterprise Plus, C3 series",
    },
    "storage": {
        "display": "Cloud Storage",
        "section": "Cloud Storage",
        "category": "general",
        "includes": "Landing, differences, single-region buckets, uploads, FUSE, HMAC",
    },
    "network-connectivity_vpn": {
        "display": "Cloud VPN",
        "section": "Cloud VPN",
        "category": "networking",
        "includes": "Landing, differences, HA VPN topologies and tunnels",
    },
    "compute": {
        "display": "Compute Engine",
        "section": "Compute Engine",
        "category": "general",
        "includes": "Landing, differences, C3/M3/A3 VMs, Hyperdisk, Shielded VM, OS images",
    },
    "container-optimized-os": {
        "display": "Container-Optimized OS",
        "section": "Container-Optimized OS",
        "category": "general",
        "includes": "Landing, differences, H100 GPU drivers, release notes",
    },
    "filestore": {
        "display": "Filestore",
        "section": "Filestore",
        "category": "general",
        "includes": "Landing, differences, Regional tier NFS, Direct Peering, GKE CSI",
    },
    "sdk": {
        "display": "Google Cloud CLI (gcloud SDK)",
        "section": None,
        "category": "general",
        "includes": "Installation, universe domain configuration, release notes",
    },
    "iam": {
        "display": "IAM",
        "section": "IAM",
        "category": "general",
        "includes": "Landing, differences, Workforce/Workload Identity, service accounts, custom roles",
    },
    "kubernetes-engine": {
        "display": "Google Kubernetes Engine (GKE)",
        "section": "Kubernetes Engine (GKE)",
        "category": "general",
        "includes": "Landing, differences, Autopilot clusters, Workload Identity, Storage FUSE",
    },
    "composer": {
        "display": "Managed Airflow (Cloud Composer 3)",
        "section": "Managed Airflow (Cloud Composer)",
        "category": "general",
        "includes": "Landing, differences, Composer 3 HA environments, DAGs, plugins",
    },
    "managed-spark": {
        "display": "Managed Service for Apache Spark (Dataproc)",
        "section": "Managed Service for Apache Spark (Dataproc)",
        "category": "general",
        "includes": "Landing, differences, GCE Spark clusters (image 2.3+), jobs, CMEK",
    },
    "network-tiers": {
        "display": "Network Service Tiers",
        "section": "Network Service Tiers",
        "category": "networking",
        "includes": "Landing, differences, Premium Tier overview",
    },
    "organization-policy": {
        "display": "Organization Policy",
        "section": "Organization Policy",
        "category": "general",
        "includes": "Landing, differences, managed & custom constraints",
    },
    "pubsub": {
        "display": "Pub/Sub",
        "section": "Pub/Sub",
        "category": "general",
        "includes": "Landing, differences, topics, push/pull subscriptions, IAM",
    },
    "resource-manager": {
        "display": "Resource Manager",
        "section": "Resource Manager",
        "category": "general",
        "includes": "Landing, differences, organizations, folders, projects, tags",
    },
    "secret-manager": {
        "display": "Secret Manager",
        "section": "Secret Manager",
        "category": "general",
        "includes": "Landing, differences, global & regional secrets, v1 API, CMEK",
    },
    "service-directory": {
        "display": "Service Directory",
        "section": None,
        "category": "general",
        "includes": "Landing, private DNS zones, release notes",
    },
    "service-usage": {
        "display": "Service Usage",
        "section": "Service Usage",
        "category": "general",
        "includes": "Landing, differences, enabling/disabling services, REST reference",
    },
    "storage-transfer": {
        "display": "Storage Transfer Service",
        "section": "Storage Transfer Service",
        "category": "general",
        "includes": "Landing, differences, GCS transfers, agent-based S3 transfers",
    },
    "terraform": {
        "display": "Terraform",
        "section": "Terraform",
        "category": "general",
        "includes": "Landing, differences, provider universe_domain, GCS state backend",
    },
    "vpc": {
        "display": "VPC",
        "section": "VPC (Virtual Private Cloud)",
        "category": "networking",
        "includes": "Landing, differences, subnets, Private Google Access, Private Service Connect",
    },
    "vpc-service-controls": {
        "display": "VPC Service Controls",
        "section": "VPC Service Controls",
        "category": "networking",
        "includes": "Landing, differences, service perimeters, ingress/egress rules",
    },
}

# Explicit fallback mapping from PREMI3NS service names (when URL points to cloud.google.com)
SECNUMCLOUD_NAME_TO_SLUG = {
    "gemini platform": "gemini-enterprise-agent-platform",
    "managed service for apache airflow": "composer",
    "managed service for apache spark": "managed-spark",
    "cloud quota": "quotas",
    "storage transfer service": "storage-transfer",
    "cloud key management service": "kms",
    "google kubernetes engine autopilot": "kubernetes-engine",
    "virtual private cloud": "vpc",
    "identity and access management": "iam",
}

# Additional baseline API services that are part of core cross-cutting docs
BASELINE_CORE_SERVICES = [
    "API Discovery Service",
    "BigLake",
    "BigQuery Data Policy",
    "BigQuery ML",
    "BigQuery Reservation",
    "BigQuery Storage",
    "Cloud Audit Logs",
    "Cloud External Key Manager (EKM)",
    "Cloud GPUs",
    "Hyperdisk",
    "Private Service Connect",
    "Service Account Credentials",
    "Shielded VM",
    "Workforce Identity Federation",
    "Workload Identity Federation",
]


def load_manifest(region_dir: Path) -> dict:
    manifest_path = region_dir / "_manifest.json"
    if not manifest_path.exists():
        return {}
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def load_secnumcloud_status() -> dict:
    status_path = S3NS_DIR / "_secnumcloud_status.json"
    if not status_path.exists():
        return {"source_url": "https://www.s3ns.io/offres/premi3ns-cloud-de-confiance", "summary": {}, "services": []}
    return json.loads(status_path.read_text(encoding="utf-8"))


def slug_from_secnumcloud_item(item: dict) -> str | None:
    name_lower = item.get("name", "").strip().lower()
    # Sub-features of BigQuery or IAM that have their own cards on PREMI3NS
    # should not overwrite the parent product slug if they match a sub-page URL
    if name_lower in (
        "bigquery reservation",
        "service account credentials",
        "workforce identity federation",
        "workload identity federation using the security token service api",
        "networking",
    ):
        return None
    if name_lower in SECNUMCLOUD_NAME_TO_SLUG:
        return SECNUMCLOUD_NAME_TO_SLUG[name_lower]

    url = item.get("url", "")
    if url:
        parsed = urlparse(url)
        slug = slug_from_manifest_entry(parsed.path, "")
        if slug:
            return slug
    return None


def slug_from_tpc_filename(filename: str) -> str:
    slug = filename.removesuffix("_tpc-differences.md")
    if slug == "network-connectivity_vpn_concepts":
        return "network-connectivity_vpn"
    return slug


def slug_from_manifest_entry(path: str, filename: str) -> str | None:
    if filename in ("products.md", "release-notes.md", "index.md", "docs.md"):
        return None
    if path.startswith("/assured-workloads/access-transparency"):
        return "assured-workloads_access-transparency"
    if path.startswith("/network-connectivity/docs/interconnect"):
        return "network-connectivity_interconnect"
    if path.startswith("/network-connectivity/docs/router"):
        return "network-connectivity_router"
    if path.startswith("/network-connectivity/docs/vpn"):
        return "network-connectivity_vpn"
    if path.startswith("/network-connectivity/docs"):
        return None
    if path.startswith("/docs/terraform"):
        return "terraform"
    if path.startswith("/docs/quotas"):
        return "quotas"
    if path.startswith("/docs/"):
        return None
    parts = path.strip("/").split("/")
    if parts and parts[0]:
        return parts[0]
    return None


def parse_tpc_markdown(md_path: Path) -> dict:
    """Deterministically parse a `*_tpc-differences.md` file."""
    text = md_path.read_text(encoding="utf-8")
    title_m = re.search(
        r"^#\s+(.+?)\s+in\s+(?:Cloud de Confiance|Google Cloud(?: Dedicated)?)\s+versus\s+Google Cloud",
        text,
        re.M,
    )
    raw_title = title_m.group(1).strip() if title_m else md_path.stem.replace("_tpc-differences", "")

    # Extract Key differences bullets
    kd_m = re.search(r"## Key differences\s+(.*?)(?=\n### |\n## |\Z)", text, re.S)
    bullets = []
    if kd_m:
        kd_body = kd_m.group(1)
        for part in re.split(r"\n-\s+", kd_body):
            part = part.strip()
            if not part or part.startswith("There are some differences"):
                continue
            part = re.split(
                r"\n\nA more detailed list|\n\nIf you are already familiar|\n\nIf you would like",
                part,
            )[0].strip()
            part = re.sub(r"\s+", " ", part)
            if part:
                bullets.append(part)

    # Extract ### sections and their | **Feature** | Description | table rows without catastrophic regex
    sections = []
    for sec_m in re.finditer(r"###\s+([^\n]+)\n(.*?)(?=\n### |\n## |\Z)", text, re.S):
        sec_name = sec_m.group(1).strip()
        sec_body = sec_m.group(2)
        parts = re.split(r"\|\s*\*\*([^*|\n]+)\*\*\s*\|", sec_body)
        rows = []
        for idx in range(1, len(parts) - 1, 2):
            feat = re.sub(r"\s+", " ", parts[idx]).strip()
            desc_raw = parts[idx + 1]
            desc_raw = re.split(r"\|\s*\|", desc_raw)[0]
            desc = re.sub(r"\s+", " ", desc_raw).strip().rstrip("|").strip()
            if feat and desc:
                rows.append((feat, desc))
        if rows:
            sections.append((sec_name, rows))

    digest_payload = json.dumps(
        {"bullets": bullets, "sections": sections},
        ensure_ascii=False,
        sort_keys=True,
    )
    digest = hashlib.sha256(digest_payload.encode("utf-8")).hexdigest()[:10]

    return {
        "title": raw_title,
        "bullets": bullets,
        "sections": sections,
        "digest": digest,
    }


def render_auto_product_section(slug: str, display_name: str, parsed: dict) -> str:
    """Render a clean markdown section for a newly discovered product with `tpc-differences`."""
    lines = [
        f"## {display_name}",
        f"<!-- AUTO-GENERATED-PRODUCT:{slug}:START -->",
        "",
    ]
    if parsed["bullets"]:
        lines.append("**Key differences:**")
        for b in parsed["bullets"]:
            lines.append(f"- {b}")
        lines.append("")

    for sec_name, rows in parsed["sections"]:
        lines.append(f"**{sec_name}:**")
        for feat, desc in rows:
            lines.append(f"- **{feat}:** {desc}")
        lines.append("")

    if not parsed["bullets"] and not parsed["sections"]:
        lines.append("- Refer to the sovereign cloud documentation for product-specific constraints.")
        lines.append("")

    lines.append(f"<!-- AUTO-GENERATED-PRODUCT:{slug}:END -->")
    return "\n".join(lines)


def replace_marker_block(text: str, marker_name: str, new_body: str) -> str:
    start_tag = f"<!-- AUTO-SYNC:{marker_name}:START -->"
    end_tag = f"<!-- AUTO-SYNC:{marker_name}:END -->"
    pattern = re.compile(re.escape(start_tag) + r".*?" + re.escape(end_tag), re.S)
    replacement = f"{start_tag}\n{new_body.rstrip()}\n{end_tag}"
    if pattern.search(text):
        return pattern.sub(lambda _: replacement, text, count=1)
    return text


def collect_inventory():
    berlin_manifest = load_manifest(BERLIN_DIR)
    s3ns_manifest = load_manifest(S3NS_DIR)
    secnumcloud_data = load_secnumcloud_status()

    # Map slug -> SecNumCloud status label
    slug_to_secnum = {}
    for item in secnumcloud_data.get("services", []):
        if item.get("status") in ("qualified", "in_progress"):
            slug = slug_from_secnumcloud_item(item)
            if slug:
                slug_to_secnum[slug] = item.get("status_label", "—")

    # Collect per-slug page counts and tpc-differences info
    products = {}

    def ensure_slug(slug: str):
        if slug not in products:
            meta = KNOWN_PRODUCT_META.get(slug, {})
            default_display = slug.replace("_", " / ").replace("-", " ").title()
            products[slug] = {
                "slug": slug,
                "display": meta.get("display", default_display),
                "section": meta.get("section", default_display),
                "category": meta.get("category", "general"),
                "includes": meta.get("includes", "Landing, differences, guides, release notes"),
                "secnumcloud": slug_to_secnum.get(slug, "—"),
                "berlin_pages": 0,
                "s3ns_pages": 0,
                "tpc_filename": None,
                "berlin_tpc_updated": None,
                "s3ns_tpc_updated": None,
                "latest_updated": None,
                "parsed_tpc": None,
            }
        return products[slug]

    for region_name, manifest, region_dir in [
        ("berlin", berlin_manifest, BERLIN_DIR),
        ("s3ns", s3ns_manifest, S3NS_DIR),
    ]:
        for path, info in manifest.items():
            fn = info["filename"]
            lu = info.get("last_updated")
            is_tpc = (
                fn.endswith("_tpc-differences.md")
                and fn not in PLATFORM_WIDE_TPC_FILES
            )
            slug = (
                slug_from_tpc_filename(fn)
                if is_tpc
                else slug_from_manifest_entry(path, fn)
            )
            if not slug:
                continue
            entry = ensure_slug(slug)
            if region_name == "berlin":
                entry["berlin_pages"] += 1
            else:
                entry["s3ns_pages"] += 1
            if lu and (not entry["latest_updated"] or lu > entry["latest_updated"]):
                entry["latest_updated"] = lu
            if is_tpc:
                entry["tpc_filename"] = fn
                if region_name == "berlin":
                    entry["berlin_tpc_updated"] = lu
                else:
                    entry["s3ns_tpc_updated"] = lu
                md_path = region_dir / fn
                if md_path.exists() and (entry["parsed_tpc"] is None or region_name == "s3ns"):
                    parsed = parse_tpc_markdown(md_path)
                    entry["parsed_tpc"] = parsed
                    if slug not in KNOWN_PRODUCT_META and parsed["title"]:
                        entry["display"] = parsed["title"]
                        entry["section"] = parsed["title"]

    return berlin_manifest, s3ns_manifest, secnumcloud_data, products


def parse_recent_release_notes(max_entries: int = 12) -> list[dict]:
    """Parse the most recent sovereign cloud release notes from release-notes.md."""
    rn_path = S3NS_DIR / "release-notes.md"
    if not rn_path.exists():
        rn_path = BERLIN_DIR / "release-notes.md"
    if not rn_path.exists():
        return []

    lines = rn_path.read_text(encoding="utf-8").splitlines()
    entries = []
    seen_keys = set()
    current_date = None
    current_product = None
    note_types = {"Feature", "Change", "Security", "Announcement", "Fixed", "Deprecated", "Issue", "Breaking"}

    i = 0
    n = len(lines)
    while i < n and len(entries) < max_entries:
        line = lines[i].strip()
        date_m = re.match(r"^##\s+([A-Z][a-z]+\s+\d{1,2},\s+\d{4})\s*$", line)
        if date_m:
            current_date = date_m.group(1)
            current_product = None
            i += 1
            continue

        prod_m = re.match(r"^\*\*([^*]+?)\*\*\s*$", line)
        if prod_m and not prod_m.group(1).strip().endswith("."):
            current_product = prod_m.group(1).strip()
            i += 1
            continue

        if current_date and current_product and line in note_types:
            note_type = line
            i += 1
            while i < n and not lines[i].strip():
                i += 1
            subheading = None
            if i < n and lines[i].strip().startswith("#### "):
                subheading = lines[i].strip()[5:].strip()
                i += 1
                while i < n and not lines[i].strip():
                    i += 1

            para_lines = []
            while i < n:
                pline = lines[i].strip()
                if not pline:
                    if para_lines:
                        break
                    i += 1
                    continue
                if (
                    pline.startswith("#")
                    or pline in note_types
                    or (re.match(r"^\*\*([^*]+?)\*\*\s*$", pline) and not pline.endswith(".**"))
                ):
                    break
                para_lines.append(pline)
                i += 1

            summary_text = re.sub(r"\s+", " ", " ".join(para_lines)).strip()
            # Convert relative doc links to clean text or keep markdown links readable
            summary_text = re.sub(r"\[([^\]]+)\]\((/[^)]+)\)", r"\1 (`\2`)", summary_text)
            if subheading:
                full_summary = f"**{subheading}:** {summary_text}" if summary_text else f"**{subheading}**"
                dedup_key = (current_date, current_product, subheading)
            else:
                full_summary = summary_text
                dedup_key = (current_date, current_product, full_summary[:80])

            if full_summary and dedup_key not in seen_keys:
                seen_keys.add(dedup_key)
                entries.append(
                    {
                        "date": current_date,
                        "product": current_product,
                        "type": note_type,
                        "summary": full_summary.replace("|", "\\|"),
                    }
                )
            continue

        i += 1

    return entries


def sync_product_differences(products: dict, check_only: bool = False) -> bool:
    content = PRODUCT_DIFFS_FILE.read_text(encoding="utf-8")
    original = content

    tpc_products = sorted(
        [p for p in products.values() if p["tpc_filename"]],
        key=lambda x: x["display"].lower(),
    )

    # Read previously recorded digests from the TPC-DIFFERENCES-INDEX table (if present)
    previous_digests = {}
    for row_m in re.finditer(
        r"\|\s*`([^`]+_tpc-differences\.md)`\s*\|\s*[^|]+?\s*\|\s*`([0-9a-f]{10})`\s*\|",
        content,
    ):
        fn = row_m.group(1).strip()
        old_digest = row_m.group(2).strip()
        previous_digests[fn] = old_digest

    # 1. Build index summary + collapsible tracked inventory table with digests
    latest_date = max(
        (p["s3ns_tpc_updated"] or p["berlin_tpc_updated"] or "" for p in tpc_products),
        default="unknown",
    )
    index_lines = [
        f"> **Auto-synced coverage:** {len(tpc_products)} product-specific `tpc-differences` guides tracked across Berlin (`docs-raw/`) and S3NS (`docs-raw-s3ns/`), latest upstream update `{latest_date}`.",
        "",
        "<details>",
        f"<summary>Tracked <code>tpc-differences</code> inventory ({len(tpc_products)} guides)</summary>",
        "",
        "| Product | S3NS SecNumCloud 3.2 | Differences File | Last Updated | Digest |",
        "|---|---|---|---|---|",
    ]
    for p in tpc_products:
        lu = p["s3ns_tpc_updated"] or p["berlin_tpc_updated"] or "—"
        digest = p["parsed_tpc"]["digest"] if p["parsed_tpc"] else "0000000000"
        index_lines.append(
            f"| {p['display']} | {p['secnumcloud']} | `{p['tpc_filename']}` | {lu} | `{digest}` |"
        )
    index_lines.append("")
    index_lines.append("</details>")

    content = replace_marker_block(
        content, "TPC-DIFFERENCES-INDEX", "\n".join(index_lines)
    )

    # 2. Check for any product with a tpc-differences page that:
    #    (a) is not yet in product-differences.md -> auto-generate full `## <Product>` section
    #    (b) has an AUTO-GENERATED-PRODUCT block -> refresh it
    #    (c) is an existing curated section whose upstream digest changed -> inject/update
    #        an AUTO-SYNC:UPSTREAM-DIFFS:<slug> block inside that section.
    existing_headings = {
        m.group(1).strip().lower()
        for m in re.finditer(r"^##\s+([^\n]+)", content, re.M)
    }

    for p in tpc_products:
        slug = p["slug"]
        sec_title = p["section"] or p["display"]
        parsed = p["parsed_tpc"]
        if not parsed:
            continue

        auto_pattern = re.compile(
            rf"##\s+{re.escape(sec_title)}\n<!-- AUTO-GENERATED-PRODUCT:{re.escape(slug)}:START -->.*?<!-- AUTO-GENERATED-PRODUCT:{re.escape(slug)}:END -->",
            re.S,
        )
        if auto_pattern.search(content):
            rendered = render_auto_product_section(slug, sec_title, parsed)
            content = auto_pattern.sub(lambda _: rendered, content, count=1)
        elif sec_title.lower() not in existing_headings and p["display"].lower() not in existing_headings:
            rendered = render_auto_product_section(slug, sec_title, parsed)
            inserted = False
            for m in re.finditer(r"\n---\n\n##\s+([^\n]+)", content):
                heading = m.group(1).strip()
                if heading.lower() > sec_title.lower():
                    pos = m.start()
                    content = content[:pos] + f"\n---\n\n{rendered}" + content[pos:]
                    inserted = True
                    break
            if not inserted:
                content = content.rstrip() + f"\n\n---\n\n{rendered}\n"
            existing_headings.add(sec_title.lower())
            print(f"  [sync-skill] Injected new product section in product-differences.md: ## {sec_title}")
        else:
            old_digest = previous_digests.get(p["tpc_filename"])
            if old_digest and old_digest != parsed["digest"]:
                update_lines = [
                    f"<!-- AUTO-SYNC:UPSTREAM-DIFFS:{slug}:START -->",
                    f"**Latest upstream documentation updates (`{p['s3ns_tpc_updated'] or p['berlin_tpc_updated']}`):**",
                ]
                for b in parsed["bullets"]:
                    update_lines.append(f"- {b}")
                for s_name, rows in parsed["sections"]:
                    for feat, desc in rows:
                        update_lines.append(f"- **{s_name} — {feat}:** {desc}")
                update_lines.append(f"<!-- AUTO-SYNC:UPSTREAM-DIFFS:{slug}:END -->")
                update_block = "\n".join(update_lines)

                existing_update_pat = re.compile(
                    rf"<!-- AUTO-SYNC:UPSTREAM-DIFFS:{re.escape(slug)}:START -->.*?<!-- AUTO-SYNC:UPSTREAM-DIFFS:{re.escape(slug)}:END -->",
                    re.S,
                )
                if existing_update_pat.search(content):
                    content = existing_update_pat.sub(lambda _: update_block, content, count=1)
                else:
                    sec_pat = re.compile(
                        rf"(^##\s+{re.escape(sec_title)}\n.*?)(?=\n---\n|\Z)",
                        re.M | re.S,
                    )
                    content = sec_pat.sub(
                        lambda m: m.group(1).rstrip() + "\n\n" + update_block + "\n",
                        content,
                        count=1,
                    )
                print(f"  [sync-skill] Updated existing section with upstream changes: ## {sec_title}")

    if content != original:
        if not check_only:
            PRODUCT_DIFFS_FILE.write_text(content, encoding="utf-8")
        return True
    return False


def sync_services_md(
    berlin_manifest: dict,
    s3ns_manifest: dict,
    secnumcloud_data: dict,
    products: dict,
    check_only: bool = False,
) -> bool:
    content = SERVICES_FILE.read_text(encoding="utf-8")
    original = content

    # 1. Build full alphabetical list of available API services
    service_names = set(BASELINE_CORE_SERVICES)
    for p in products.values():
        if p["berlin_pages"] > 0 or p["s3ns_pages"] > 0:
            service_names.add(p["display"])

    sorted_services = sorted(service_names, key=lambda s: s.lower())
    api_list_md = "\n".join(f"- {name}" for name in sorted_services)
    content = replace_marker_block(content, "AVAILABLE-API-SERVICES", api_list_md)

    # 2. Build S3NS SecNumCloud 3.2 status block
    services_list = secnumcloud_data.get("services", [])
    qualified = sorted(
        [s for s in services_list if s.get("status") == "qualified"],
        key=lambda x: x["name"].lower(),
    )
    in_progress = sorted(
        [s for s in services_list if s.get("status") == "in_progress"],
        key=lambda x: x["name"].lower(),
    )
    upcoming = sorted(
        [s for s in services_list if s.get("status") == "upcoming"],
        key=lambda x: x["name"].lower(),
    )

    secnum_lines = [
        f"**Summary (PREMI3NS catalog):** **{len(qualified)}** `Qualifié SecNumCloud 3.2` | **{len(in_progress)}** `Qualification en cours` | **{len(upcoming)}** `À venir`",
        "",
        f"### Qualifié SecNumCloud 3.2 ({len(qualified)} services)",
        "",
        ", ".join(f"**{s['name']}**" for s in qualified) + ".",
        "",
        f"### Qualification en cours ({len(in_progress)} services — available on S3NS, ANSSI qualification in progress)",
        "",
        "| Service (PREMI3NS) | Status | Documentation Hub |",
        "|---|---|---|",
    ]
    for s in in_progress:
        slug = slug_from_secnumcloud_item(s)
        hub_name = products[slug]["display"] if slug and slug in products else s["name"]
        secnum_lines.append(f"| {s['name']} | `{s['status_label']}` | {hub_name} |")

    secnum_lines.extend(
        [
            "",
            f"### À venir ({len(upcoming)} services — S3NS roadmap, not yet available)",
            "",
            ", ".join(f"**{s['name']}**" for s in upcoming) + ".",
        ]
    )
    content = replace_marker_block(content, "SECNUMCLOUD-STATUS", "\n".join(secnum_lines))

    # 3. Build Discovered Documentation Inventory table
    table_lines = [
        f"Total scraped pages: **{len(berlin_manifest)}** (Berlin GCD) / **{len(s3ns_manifest)}** (France S3NS).",
        "",
        "| Service / Documentation Hub | Berlin Pages | S3NS Pages | S3NS SecNumCloud 3.2 | Differences Guide | Last Updated |",
        "|---|---:|---:|---|---|---|",
    ]
    for p in sorted(products.values(), key=lambda x: x["display"].lower()):
        if p["berlin_pages"] == 0 and p["s3ns_pages"] == 0:
            continue
        tpc_cell = f"`{p['tpc_filename']}`" if p["tpc_filename"] else "—"
        lu = p["latest_updated"] or "—"
        table_lines.append(
            f"| {p['display']} | {p['berlin_pages']} | {p['s3ns_pages']} | {p['secnumcloud']} | {tpc_cell} | {lu} |"
        )

    content = replace_marker_block(
        content, "DISCOVERED-PRODUCTS-TABLE", "\n".join(table_lines)
    )

    # 4. Build Recent Sovereign Cloud Release Notes table
    release_notes = parse_recent_release_notes(max_entries=12)
    if release_notes:
        rn_lines = [
            "| Date | Product | Type | Summary |",
            "|---|---|---|---|",
        ]
        for rn in release_notes:
            rn_lines.append(
                f"| {rn['date']} | **{rn['product']}** | `{rn['type']}` | {rn['summary']} |"
            )
        content = replace_marker_block(
            content, "RECENT-RELEASE-NOTES", "\n".join(rn_lines)
        )

    if content != original:
        if not check_only:
            SERVICES_FILE.write_text(content, encoding="utf-8")
        return True
    return False


def sync_skill_md(secnumcloud_data: dict, products: dict, check_only: bool = False) -> bool:
    content = SKILL_FILE.read_text(encoding="utf-8")
    original = content

    general_services = {
        "API Discovery Service",
        "BigQuery Reservation",
        "Service Account Credentials",
        "Shielded VM",
        "Workforce/Workload Identity Federation",
    }
    networking_services = set()

    for p in products.values():
        if p["berlin_pages"] == 0 and p["s3ns_pages"] == 0:
            continue
        if p["category"] == "networking":
            networking_services.add(p["display"])
            if p["slug"] == "dns":
                general_services.add(p["display"])
        else:
            name = p["display"]
            if name == "Google Kubernetes Engine (GKE)":
                name = "Google Kubernetes Engine (Autopilot only)"
            general_services.add(name)

    gen_str = ", ".join(sorted(general_services, key=lambda s: s.lower()))
    net_str = ", ".join(sorted(networking_services, key=lambda s: s.lower()))

    services_list = secnumcloud_data.get("services", [])
    qualified = sorted(
        [s["name"] for s in services_list if s.get("status") == "qualified"],
        key=lambda s: s.lower(),
    )
    in_progress = sorted(
        [s["name"] for s in services_list if s.get("status") == "in_progress"],
        key=lambda s: s.lower(),
    )
    upcoming = sorted(
        [s["name"] for s in services_list if s.get("status") == "upcoming"],
        key=lambda s: s.lower(),
    )

    block_lines = [
        f"**Both regions (Compute, Data, Storage, Security & Ops):** {gen_str}.",
        "",
        f"**Both regions (Networking):** {net_str}.",
    ]
    if qualified or in_progress or upcoming:
        block_lines.extend(
            [
                "",
                "**S3NS (`u-france-east1`) SecNumCloud 3.2 qualification status ([PREMI3NS](https://www.s3ns.io/offres/premi3ns-cloud-de-confiance)):**",
                f"- **Qualifié SecNumCloud 3.2 ({len(qualified)}):** {', '.join(qualified)}.",
                f"- **Qualification en cours ({len(in_progress)} — available on S3NS today, ANSSI qualification in progress):** {', '.join(in_progress)}.",
                f"- **À venir ({len(upcoming)} — S3NS roadmap, not yet available):** {', '.join(upcoming)}.",
            ]
        )

    content = replace_marker_block(content, "AVAILABLE-SERVICES", "\n".join(block_lines))

    if content != original:
        if not check_only:
            SKILL_FILE.write_text(content, encoding="utf-8")
        return True
    return False


def sync_readme_md(berlin_manifest: dict, s3ns_manifest: dict, products: dict, check_only: bool = False) -> bool:
    content = README_FILE.read_text(encoding="utf-8")
    original = content

    tpc_products = sorted(
        [p for p in products.values() if p["tpc_filename"] or p["slug"] in ("api-keys", "assured-workloads_access-transparency")],
        key=lambda x: x["display"].lower(),
    )

    lines = [
        f"Total scraped pages: **{len(berlin_manifest)}** in `docs-raw/` (Berlin GCD) and **{len(s3ns_manifest)}** in `docs-raw-s3ns/` (S3NS Cloud de Confiance).",
        "",
        "| Product | Berlin Pages | S3NS Pages | S3NS SecNumCloud 3.2 | Includes |",
        "|---|---:|---:|---|---|",
    ]
    for p in tpc_products:
        lines.append(
            f"| {p['display']} | {p['berlin_pages']} | {p['s3ns_pages']} | {p['secnumcloud']} | {p['includes']} |"
        )

    content = replace_marker_block(content, "COVERAGE-TABLE", "\n".join(lines))

    if content != original:
        if not check_only:
            README_FILE.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Synchronize gcd-claude-skill capability files from scraped documentation."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify that all skill files are in sync without modifying them (exits 1 if out of sync).",
    )
    args = parser.parse_args()

    mode_label = "Checking" if args.check else "Synchronizing"
    print(f"{mode_label} skill files from scraped documentation manifests...")
    berlin_manifest, s3ns_manifest, secnumcloud_data, products = collect_inventory()
    tpc_count = sum(1 for p in products.values() if p["tpc_filename"])
    secnum_summary = secnumcloud_data.get("summary", {})
    print(
        f"  Loaded manifests: Berlin={len(berlin_manifest)} pages, "
        f"S3NS={len(s3ns_manifest)} pages, "
        f"Products={len(products)} ({tpc_count} with tpc-differences), "
        f"SecNumCloud={secnum_summary}"
    )

    changed = []
    if sync_product_differences(products, check_only=args.check):
        changed.append("references/product-differences.md")
    if sync_services_md(berlin_manifest, s3ns_manifest, secnumcloud_data, products, check_only=args.check):
        changed.append("references/services.md")
    if sync_skill_md(secnumcloud_data, products, check_only=args.check):
        changed.append("SKILL.md")
    if sync_readme_md(berlin_manifest, s3ns_manifest, products, check_only=args.check):
        changed.append("README.md")

    if changed:
        if args.check:
            print(f"  Out-of-sync files detected: {', '.join(changed)}", file=sys.stderr)
            sys.exit(1)
        print(f"  Updated files: {', '.join(changed)}")
    else:
        print("  All skill files are already up to date.")


if __name__ == "__main__":
    main()
