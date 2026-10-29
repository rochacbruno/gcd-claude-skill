#!/usr/bin/env python3
"""Scrape sovereign cloud documentation.

Supports multiple regions:
  - berlin: Google Cloud Dedicated in Germany (berlin.devsitetest.how)
  - s3ns:   Cloud de Confiance by S3NS in France (documentation.s3ns.fr)

Uses fast parallel SSR HTTP fetching by default (standard library urllib +
ThreadPoolExecutor), with optional Playwright headless browser rendering
(--use-playwright) as a fallback.

Crawls and dynamically discovers:
  1. Product catalog (/products), release notes (/release-notes), and all
     cross-cutting pages under /docs/*
  2. All available products dynamically discovered from /products,
     /release-notes, and /docs/* category pages (in addition to known seeds)
  3. Per-product landing pages (/<product>/docs or /<product>/overview)
  4. Per-product tpc-differences pages (/<product>/docs/tpc-differences or
     /<product>/tpc-differences)
  5. Explicit product sub-pages known to contain sovereign-cloud-specific
     content, plus 1st-level <article> links for newly discovered products

Detects and skips fallback redirects to /docs/tpc-differences (or
/docs/overview/tpc-key-differences) when a product or tpc-differences page
does not exist, and cleans up stale files not present in the new manifest.

Tracks last-updated dates and full page manifests for incremental updates
and automated skill synchronization (via scripts/sync-skill.py).

Usage:
    python3 scripts/scrape-gcd-docs.py [--region berlin|s3ns|all] [--output-dir DIR] [--use-playwright]
"""

import argparse
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
import html
import json
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# -- Region configurations ----------------------------------------------------

REGIONS = {
    "berlin": {
        "name": "Google Cloud Dedicated in Germany",
        "base_url": "https://berlin.devsitetest.how",
        "extra_headers": {"X-DevSite-Proxy": "gcd"},
        "default_output_dir": "docs-raw",
    },
    "s3ns": {
        "name": "Cloud de Confiance by S3NS",
        "base_url": "https://documentation.s3ns.fr",
        "extra_headers": {},
        "default_output_dir": "docs-raw-s3ns",
    },
}

MAX_RETRIES = 3
PAGE_TIMEOUT = 30_000
NETWORK_IDLE_TIMEOUT = 10_000
HTTP_TIMEOUT_SECONDS = 20
DEFAULT_WORKERS = 10

# -- Product lists -------------------------------------------------------------

# Core products available in both regions (baseline seeds; new products are
# also discovered dynamically from /products, /release-notes, and /docs/*).
CORE_PRODUCTS = [
    "access-context-manager",
    "api-keys",
    "artifact-registry",
    "assured-workloads/access-transparency",
    "bigquery",
    "bigtable",
    "billing",
    "composer",
    "compute",
    "dns",
    "filestore",
    "iam",
    "kms",
    "kubernetes-engine",
    "logging",
    "managed-spark",
    "monitoring",
    "pubsub",
    "resource-manager",
    "run",
    "secret-manager",
    "service-usage",
    "sql",
    "storage",
    "storage-transfer",
]

# Networking products available in both regions (referenced in both regions'
# key-differences documentation and /products catalog)
NETWORKING_PRODUCTS = [
    "armor",
    "firewall",
    "load-balancing",
    "nat",
    "network-connectivity",
    "network-tiers",
    "vpc",
    "vpc-service-controls",
]

# Products documented without a /docs segment in their URL path
NON_DOCS_PRODUCTS = [
    "gemini-enterprise-agent-platform",
    "organization-policy",
]

# Additional products documented in the S3NS region (or cross-referenced)
S3NS_EXTRA_PRODUCTS = [
    "api-registry",
    "code",
    "container-optimized-os",
    "lakehouse",
    "marketplace",
    "sdk",
    "service-directory",
]


def get_products(region: str) -> list[str]:
    """Return the initial seed product list for a given region."""
    products = CORE_PRODUCTS + NETWORKING_PRODUCTS + NON_DOCS_PRODUCTS
    if region == "s3ns":
        products = products + S3NS_EXTRA_PRODUCTS
    return sorted(set(products))


# Paths that are deep GCP docs trees we should NOT recurse into blindly.
DEEP_CRAWL_BLOCKLIST = {
    "ai-introduction", "samples", "pricing", "quotas-limits", "resources", "api",
}

# Product sub-pages known to contain sovereign-cloud-specific content
# (rewritten with region endpoints, project prefixes, etc.).
COMMON_PRODUCT_PAGES = [
    "/access-context-manager/docs/create-access-level",
    "/access-context-manager/docs/create-access-policy",
    "/access-context-manager/docs/create-basic-access-level",
    "/access-context-manager/docs/manage-access-levels",
    "/access-context-manager/docs/reference/rest",
    "/access-context-manager/docs/release-notes",
    "/api-keys/docs/quotas",
    "/api-keys/docs/reference/rest",
    "/api-keys/docs/release-notes",
    "/artifact-registry/docs/access-control",
    "/artifact-registry/docs/quickstarts",
    "/artifact-registry/docs/reference/rest",
    "/artifact-registry/docs/release-notes",
    "/bigquery/docs/bq-command-line-tool",
    "/bigquery/docs/controlling-costs",
    "/bigquery/docs/create-machine-learning-model",
    "/bigquery/docs/custom-quotas",
    "/bigquery/docs/dataframes-quickstart",
    "/bigquery/docs/exporting-data",
    "/bigquery/docs/loading-data-cloud-storage-csv",
    "/bigquery/docs/quickstarts/load-data-bq",
    "/bigquery/docs/quickstarts/query-public-dataset-console",
    "/bigquery/docs/quickstarts/quickstart-client-libraries",
    "/bigquery/docs/release-notes",
    "/bigquery/docs/reservations-intro",
    "/bigquery/docs/tables",
    "/bigquery/docs/troubleshoot-quotas",
    "/compute/docs/disks/hyperdisks",
    "/compute/docs/gpus",
    "/compute/docs/instances/create-start-instance",
    "/compute/docs/instances/ssh",
    "/compute/docs/reference/rest/v1",
    "/compute/docs/release-notes",
    "/compute/shielded-vm/docs",
    "/dns/docs/overview",
    "/dns/docs/policies",
    "/dns/docs/records",
    "/dns/docs/release-notes",
    "/dns/docs/set-up-dns-records-domain-name",
    "/dns/docs/zones",
    "/iam/docs/attach-service-accounts",
    "/iam/docs/configuring-temporary-access",
    "/iam/docs/creating-custom-roles",
    "/iam/docs/grant-role-console",
    "/iam/docs/granting-changing-revoking-access",
    "/iam/docs/manage-access-other-resources",
    "/iam/docs/permissions-change-log",
    "/iam/docs/reference/rest",
    "/iam/docs/release-notes",
    "/iam/docs/roles-overview",
    "/iam/docs/service-account-creds",
    "/iam/docs/service-accounts-create",
    "/iam/docs/service-agents",
    "/iam/docs/workforce-identity-federation",
    "/iam/docs/workload-identity-federation",
    "/iam/docs/write-policy-client-libraries",
    "/kms/docs/creating-keys",
    "/kms/docs/destroy-restore",
    "/kms/docs/importing-a-key",
    "/kms/docs/reference/rest",
    "/kms/docs/release-notes",
    "/kms/docs/retrieve-public-key",
    "/kubernetes-engine/docs/concepts/kubernetes-engine-overview",
    "/kubernetes-engine/docs/concepts/machine-learning",
    "/kubernetes-engine/docs/how-to/cluster-access-for-kubectl",
    "/kubernetes-engine/docs/how-to/workload-identity",
    "/kubernetes-engine/docs/quickstarts/create-cluster",
    "/kubernetes-engine/docs/reference/rest",
    "/kubernetes-engine/docs/release-notes",
    "/logging/docs/audit",
    "/logging/docs/buckets",
    "/logging/docs/reference/libraries",
    "/logging/docs/reference/v2/rest",
    "/logging/docs/release-notes",
    "/logging/docs/view/building-queries",
    "/logging/docs/view/logs-viewer-interface",
    "/logging/docs/write-query-log-entries-gcloud",
    "/monitoring/docs/reference/libraries",
    "/monitoring/docs/release-notes",
    "/pubsub/docs/access-control",
    "/pubsub/docs/create-topic",
    "/pubsub/docs/monitoring",
    "/pubsub/docs/publish-receive-messages-console",
    "/pubsub/docs/publish-receive-messages-gcloud",
    "/pubsub/docs/publisher",
    "/pubsub/docs/release-notes",
    "/pubsub/docs/resource-location-restriction",
    "/pubsub/docs/troubleshooting",
    "/resource-manager/docs/authorizing",
    "/resource-manager/docs/creating-managing-folders",
    "/resource-manager/docs/creating-managing-projects",
    "/resource-manager/docs/limits",
    "/resource-manager/docs/listing-all-resources",
    "/resource-manager/docs/manage-google-cloud-resources",
    "/resource-manager/docs/reference/essentialcontacts/rest",
    "/resource-manager/docs/release-notes",
    "/resource-manager/docs/tags/tags-creating-and-managing",
    "/service-usage/docs/enable-disable",
    "/service-usage/docs/list-services",
    "/service-usage/docs/overview",
    "/service-usage/docs/quotas",
    "/service-usage/docs/reference/rest",
    "/service-usage/docs/release-notes",
    "/service-usage/docs/set-up-development-environment",
    "/sql/docs/release-notes",
    "/storage/docs/creating-buckets",
    "/storage/docs/discover-object-storage-console",
    "/storage/docs/json_api",
    "/storage/docs/reference/libraries",
    "/storage/docs/release-notes",
    "/storage/docs/troubleshooting",
    "/storage/docs/uploading-objects",
    "/storage/docs/xml-api/overview",
]

# Networking sub-pages that require explicit seeding because the auto-seed
# (/<product>/docs and /<product>/docs/tpc-differences) does not cover
# sub-products under network-connectivity or important VPC sub-pages.
NETWORKING_PRODUCT_PAGES = [
    "/network-connectivity/docs/interconnect",
    "/network-connectivity/docs/interconnect/tpc-differences",
    "/network-connectivity/docs/router",
    "/network-connectivity/docs/router/tpc-differences",
    "/network-connectivity/docs/vpn",
    "/network-connectivity/docs/vpn/concepts/tpc-differences",
    "/vpc/docs/create-modify-vpc-networks",
    "/vpc/docs/flow-logs",
    "/vpc/docs/shared-vpc",
    "/vpc/docs/vpc-peering",
]

# Sub-pages for products only in the S3NS region
S3NS_EXTRA_PRODUCT_PAGES = [
    "/code/docs/intellij",
    "/code/docs/vscode",
    "/organization-policy/overview",
    "/organization-policy/tpc-differences",
]


def get_product_pages(region: str) -> list[str]:
    """Return the product sub-pages list for a given region."""
    pages = COMMON_PRODUCT_PAGES + NETWORKING_PRODUCT_PAGES
    if region == "s3ns":
        pages = pages + S3NS_EXTRA_PRODUCT_PAGES
    return sorted(set(pages))


def get_explicitly_seeded_products() -> set[str]:
    """Return products that already have curated sub-page rules (core + networking + S3NS extra)."""
    seeded: set[str] = set(NETWORKING_PRODUCTS + S3NS_EXTRA_PRODUCTS + ["organization-policy"])
    for page in COMMON_PRODUCT_PAGES:
        parts = page.lstrip("/").split("/")
        if len(parts) >= 3 and parts[1] == "docs":
            seeded.add(parts[0])
    return seeded


# -- Link & product discovery helpers ------------------------------------------

# Matches internal documentation hrefs inside <article> or page HTML
INTERNAL_HREF_RE = re.compile(r'href="(/[a-z0-9][a-z0-9/_-]*)"')

# Hub pages from which we do NOT auto-discover new products:
# - /docs/product-list contains ~140 links to public GCP products that 404
# - /docs/sdk-languages-frameworks-tools links to language portals (/python/docs, /go/docs, etc.)
PRODUCT_DISCOVERY_EXCLUDED_HUBS = {
    "/docs",
    "/release-notes",
    "/docs/product-list",
    "/docs/sdk-languages-frameworks-tools",
}

# Non-service DevSite portals that should never be treated as sovereign cloud products
IGNORED_PRODUCT_SLUGS = {
    "apis", "appengine", "cpp", "dotnet", "go", "java",
    "nodejs", "php", "python", "ruby", "support", "gemini/enterprise",
}

# Known generic fallback redirect destinations when a product or tpc-differences
# page does not exist in the sovereign cloud documentation.
FALLBACK_REDIRECT_PATHS = {
    "/docs/tpc-differences",
    "/docs/overview/tpc-key-differences",
}


def extract_links(html_fragment: str) -> list[str]:
    """Extract all internal documentation links from an HTML fragment."""
    links: set[str] = set()
    for m in INTERNAL_HREF_RE.finditer(html_fragment):
        path = m.group(1).rstrip("/")
        if not path or path == "/docs":
            continue
        # Skip static assets or non-doc paths
        if any(path.endswith(ext) for ext in (".png", ".svg", ".jpg", ".css", ".js", ".json", ".xml")):
            continue
        links.add(path)
    return sorted(links)


def infer_product_from_link(link: str) -> str | None:
    """Infer a product identifier from a documentation link, if applicable.

    Examples:
      /bigtable/docs -> "bigtable"
      /bigtable/docs/tpc-differences -> "bigtable"
      /assured-workloads/access-transparency/docs -> "assured-workloads/access-transparency"
      /gemini-enterprise-agent-platform -> "gemini-enterprise-agent-platform"
      /organization-policy/overview -> "organization-policy"
    """
    if link.startswith("/docs/") or link in ("/docs", "/products", "/release-notes"):
        return None

    parts = link.lstrip("/").split("/")
    prod = None
    if len(parts) >= 2 and parts[1] == "docs":
        prod = parts[0]
    elif len(parts) >= 3 and parts[2] == "docs":
        prod = f"{parts[0]}/{parts[1]}"
    elif parts[0] in NON_DOCS_PRODUCTS:
        prod = parts[0]

    if prod and prod in IGNORED_PRODUCT_SLUGS:
        return None
    return prod


def product_seed_paths(product: str) -> list[str]:
    """Return the standard landing and tpc-differences seed paths for a product."""
    if product in NON_DOCS_PRODUCTS:
        paths = [
            f"/{product}",
            f"/{product}/overview",
            f"/{product}/tpc-differences",
        ]
        return paths
    return [
        f"/{product}/docs",
        f"/{product}/docs/tpc-differences",
        f"/{product}/docs/release-notes",
    ]


def is_product_landing_or_diff(path: str, products: set[str]) -> str | None:
    """If path is a product landing or tpc-differences page, return its product name."""
    for prod in products:
        if prod in NON_DOCS_PRODUCTS:
            if path in (f"/{prod}", f"/{prod}/overview", f"/{prod}/tpc-differences"):
                return prod
        else:
            if path in (f"/{prod}/docs", f"/{prod}/docs/tpc-differences"):
                return prod
    return None


def is_allowed_product_subpage(link: str, product: str) -> bool:
    """Check whether a 1st-level link inside a product's landing <article> should be crawled."""
    if product in NON_DOCS_PRODUCTS:
        prefix = f"/{product}/"
    else:
        prefix = f"/{product}/docs/"

    if not link.startswith(prefix):
        return False

    subpath = link[len(prefix):]
    if not subpath:
        return False

    segments = subpath.split("/")
    # Avoid recursing into blocked deep trees (except reference/rest, reference/libraries, etc.)
    if segments[0] in DEEP_CRAWL_BLOCKLIST:
        return False
    # Limit depth of auto-discovered sub-pages to keep crawl focused and fast
    if len(segments) > 4:
        return False
    return True


# -- Content extraction --------------------------------------------------------

def extract_last_updated(page_html: str) -> str:
    """Extract the 'last updated' date from DevSite pages."""
    for pattern in [
        r'Updated\s+([\d]{4}-[\d]{2}-[\d]{2})',
        r'Last updated\s+([\d]{4}-[\d]{2}-[\d]{2})',
        r'Updated\s+(\w+ \d{1,2},\s*\d{4})',
        r'Last updated\s+(\w+ \d{1,2},\s*\d{4})',
        r'date"[^>]*>\s*([\d]{4}-[\d]{2}-[\d]{2})',
        r'date"[^>]*>\s*(\w+ \d{1,2},\s*\d{4})',
        r'UTC\.\s*([\d]{4}-[\d]{2}-[\d]{2})',
    ]:
        m = re.search(pattern, page_html, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return ""


def extract_title(page_html: str) -> str:
    """Extract the page title."""
    m = re.search(r"<title>([^<]+)</title>", page_html)
    if m:
        title = html.unescape(m.group(1))
        title = title.split("|")[0].strip()
        title = title.replace("&nbsp;", " ").replace("\xa0", " ").strip()
        return title
    return ""


def extract_article_content(page_html: str) -> str:
    """Extract the main article content from the rendered page."""
    for pattern in [
        r'<article[^>]*class="[^"]*devsite-article[^"]*"[^>]*>(.*?)</article>',
        r"<article[^>]*>(.*?)</article>",
        r'<div[^>]*class="[^"]*devsite-article-body[^"]*"[^>]*>(.*?)</div>\s*(?:</div>)',
    ]:
        m = re.search(pattern, page_html, re.DOTALL)
        if m:
            return m.group(1)
    body = re.search(r"<body[^>]*>(.*?)</body>", page_html, re.DOTALL)
    return body.group(1) if body else page_html


def is_fallback_redirect(requested_path: str, final_url: str, page_html: str) -> tuple[bool, str]:
    """Detect whether a fetched page redirected to the generic fallback differences page.

    Returns (is_fallback_redirect, final_path).
    Note: Legitimate content redirects (e.g. /kms/docs/creating-keys -> /kms/docs/create-key
    or /docs/tpc-differences -> /docs/overview/tpc-key-differences) are NOT treated as
    bogus fallback redirects.
    """
    req_norm = requested_path.rstrip("/") or "/"
    parsed = urllib.parse.urlparse(final_url)
    final_path = parsed.path.rstrip("/") or "/"

    if req_norm not in FALLBACK_REDIRECT_PATHS:
        if final_path in FALLBACK_REDIRECT_PATHS:
            return True, final_path
        title = extract_title(page_html)
        if title.startswith("Key differences between "):
            return True, "/docs/tpc-differences"

    return False, final_path


def html_to_markdown(content: str) -> str:
    """Convert HTML content to clean markdown."""
    text = content

    text = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.DOTALL)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    for tag in ["nav", "header", "footer", "aside"]:
        text = re.sub(rf"<{tag}[^>]*>.*?</{tag}>", "", text,
                       flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(
        r'<div[^>]*class="[^"]*devsite-(?:nav|breadcrumb|toc)[^"]*"[^>]*>.*?</div>',
        "", text, flags=re.DOTALL)

    for i in range(6, 0, -1):
        text = re.sub(
            rf"<h{i}[^>]*>(.*?)</h{i}>",
            lambda m, lv=i: "\n" + "#" * lv + " " + m.group(1).strip() + "\n",
            text, flags=re.DOTALL)

    text = re.sub(
        r"<pre[^>]*><code[^>]*>(.*?)</code></pre>",
        lambda m: "\n```\n" + html.unescape(m.group(1)).strip() + "\n```\n",
        text, flags=re.DOTALL)
    text = re.sub(
        r"<pre[^>]*>(.*?)</pre>",
        lambda m: "\n```\n" + html.unescape(m.group(1)).strip() + "\n```\n",
        text, flags=re.DOTALL)

    text = re.sub(
        r"<code[^>]*>(.*?)</code>",
        lambda m: "`" + html.unescape(m.group(1)).strip() + "`",
        text, flags=re.DOTALL)

    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
                  r"[\2](\1)", text, flags=re.DOTALL)

    text = re.sub(r"<li[^>]*>", "\n- ", text, flags=re.DOTALL)
    text = re.sub(r"</li>", "", text)
    text = re.sub(r"<[uo]l[^>]*>", "\n", text, flags=re.DOTALL)
    text = re.sub(r"</[uo]l>", "\n", text)

    text = re.sub(r"<tr[^>]*>", "\n| ", text, flags=re.DOTALL)
    text = re.sub(r"</tr>", " |", text)
    text = re.sub(r"<t[hd][^>]*>", "", text, flags=re.DOTALL)
    text = re.sub(r"</t[hd]>", " | ", text)

    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<p[^>]*>", "\n\n", text, flags=re.DOTALL)
    text = re.sub(r"</p>", "\n", text)

    text = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", text, flags=re.DOTALL)
    text = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", text, flags=re.DOTALL)
    text = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", text, flags=re.DOTALL)
    text = re.sub(r"<i[^>]*>(.*?)</i>", r"*\1*", text, flags=re.DOTALL)

    text = re.sub(
        r"<blockquote[^>]*>(.*?)</blockquote>",
        lambda m: "\n> " + m.group(1).strip() + "\n",
        text, flags=re.DOTALL)

    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"^ +", "", text, flags=re.MULTILINE)
    return text.strip()


def path_to_filename(path: str) -> str:
    """Convert a URL path to a safe filename."""
    if path.startswith("/docs"):
        name = path.replace("/docs/", "").replace("/docs", "index")
    else:
        name = path.lstrip("/").replace("/docs/", "_").replace("/docs", "")
    if not name:
        name = "index"
    name = name.replace("/", "_")
    return name + ".md"


# -- Fetchers (HTTP SSR + Optional Playwright) ---------------------------------

def fetch_http(base_url: str, path: str, extra_headers: dict[str, str]) -> dict | None:
    """Fetch a DevSite page via standard HTTP (SSR)."""
    url = base_url + path
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; GCD-Docs-Scraper/3.0)",
        "Accept": "text/html,application/xhtml+xml",
        **extra_headers,
    }
    for attempt in range(MAX_RETRIES):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SECONDS) as resp:
                if resp.status == 404:
                    return None
                final_url = resp.geturl()
                raw_bytes = resp.read()
                page_html = raw_bytes.decode("utf-8", errors="replace")
                redirected, final_path = is_fallback_redirect(path, final_url, page_html)
                if redirected:
                    return {"redirect_to": final_path}
                return {"html": page_html, "final_url": final_url}
        except urllib.error.HTTPError as e:
            if e.code in (400, 403, 404, 410):
                return None
            wait = 2 ** (attempt + 1)
            print(f"  [HTTP {e.code}] {path} - retry {attempt + 1}", file=sys.stderr)
            time.sleep(wait)
        except Exception as e:
            wait = 2 ** (attempt + 1)
            print(f"  [Error] {path}: {e} - retry {attempt + 1}", file=sys.stderr)
            time.sleep(wait)

    print(f"  [FAILED] {path}", file=sys.stderr)
    return None


def discover_links_from_page(
    path: str,
    page_html: str,
    products: set[str],
    explicitly_seeded_products: set[str],
) -> tuple[list[str], list[str]]:
    """Return (new_paths_to_visit, newly_discovered_products) from a fetched page."""
    new_paths: list[str] = []
    new_products: list[str] = []

    article_html = extract_article_content(page_html)

    # 1. Cross-cutting /docs/* pages: scan full page HTML for /docs/... links
    # so sidebar navigation (<devsite-book-nav>) under /docs/terraform,
    # /docs/quotas, /docs/discovery, /docs/overview, etc. is fully discovered.
    if path == "/docs" or path.startswith("/docs/"):
        for link in extract_links(page_html):
            if link.startswith("/docs/"):
                new_paths.append(link)
            elif "tpc-differences" in link:
                new_paths.append(link)

    # 2. Product discovery hubs (/products and /docs/* category pages):
    # scan <article> for product links and tpc-differences links.
    is_product_hub = (
        path == "/products"
        or (path.startswith("/docs/") and path not in PRODUCT_DISCOVERY_EXCLUDED_HUBS)
    )
    if is_product_hub:
        for link in extract_links(article_html):
            if "tpc-differences" in link:
                new_paths.append(link)

            prod = infer_product_from_link(link)
            if prod:
                if prod not in products:
                    products.add(prod)
                    new_products.append(prod)
                for seed in product_seed_paths(prod):
                    new_paths.append(seed)
                if path == "/products" or link.endswith("/docs") or "tpc-differences" in link:
                    new_paths.append(link)
        return new_paths, new_products

    # 3. Product landing page or tpc-differences page
    matched_prod = is_product_landing_or_diff(path, products)
    if matched_prod:
        for link in extract_links(article_html):
            if "tpc-differences" in link:
                new_paths.append(link)
            elif link.startswith("/docs/"):
                new_paths.append(link)
            elif matched_prod not in explicitly_seeded_products:
                # Automatically crawl 1st-level <article> guides for any product
                # that does not have a static list in COMMON_PRODUCT_PAGES
                if is_allowed_product_subpage(link, matched_prod):
                    new_paths.append(link)

    return new_paths, new_products


# -- Main crawl ----------------------------------------------------------------

def crawl_and_scrape(
    output_dir: Path,
    region: str,
    use_playwright: bool = False,
    workers: int = DEFAULT_WORKERS,
) -> dict:
    """Crawl and scrape all documentation pages for a region."""
    region_config = REGIONS[region]
    base_url = region_config["base_url"]
    extra_headers = region_config["extra_headers"]
    products: set[str] = set(get_products(region))
    explicitly_seeded_products = get_explicitly_seeded_products()
    product_pages = get_product_pages(region)

    output_dir.mkdir(parents=True, exist_ok=True)

    discovered: set[str] = set()
    to_visit: deque[str] = deque()
    visited: set[str] = set()
    results: dict[str, dict] = {}

    # Seed paths: top-level hubs + product seeds + curated sub-pages
    seeds = ["/docs", "/products", "/release-notes"]
    for product in sorted(products):
        seeds.extend(product_seed_paths(product))
    seeds.extend(product_pages)

    for p in seeds:
        p_norm = p.rstrip("/")
        if p_norm and p_norm not in discovered:
            discovered.add(p_norm)
            to_visit.append(p_norm)

    mode_label = "Playwright" if use_playwright else f"HTTP SSR ({workers} workers)"
    print(f"Starting crawl: {region_config['name']} [{mode_label}]")
    print(f"Base URL: {base_url}")
    print(f"Initial products: {len(products)}")
    print(f"Initial seed pages: {len(discovered)}")
    print(f"Output directory: {output_dir}")
    print()

    print("Phase 1: Discovering and fetching pages...")
    page_count = 0

    if use_playwright:
        from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(
                extra_http_headers=extra_headers,
                user_agent="GCD-Docs-Scraper/3.0 (Playwright)",
            )

            def fetch_pw(path: str) -> dict | None:
                url = base_url + path
                for attempt in range(MAX_RETRIES):
                    page = context.new_page()
                    try:
                        resp = page.goto(url, timeout=PAGE_TIMEOUT,
                                         wait_until="domcontentloaded")
                        if resp and resp.status == 404:
                            page.close()
                            return None
                        try:
                            page.wait_for_selector(
                                "article, .devsite-article-body",
                                timeout=NETWORK_IDLE_TIMEOUT)
                        except PwTimeout:
                            pass
                        page.wait_for_timeout(500)
                        final_url = page.url
                        rendered = page.content()
                        page.close()
                        redirected, final_path = is_fallback_redirect(path, final_url, rendered)
                        if redirected:
                            return {"redirect_to": final_path}
                        return {"html": rendered, "final_url": final_url}
                    except Exception as e:
                        page.close()
                        wait = 2 ** (attempt + 1)
                        print(f"  [Error] {path}: {e}", file=sys.stderr)
                        time.sleep(wait)
                return None

            while to_visit:
                path = to_visit.popleft()
                if path in visited:
                    continue
                visited.add(path)
                result = fetch_pw(path)
                if result is None:
                    print(f"  SKIP (404) {path}")
                    continue
                if "redirect_to" in result:
                    target = result["redirect_to"]
                    print(f"  SKIP (redirect -> {target}) {path}")
                    continue

                page_html = result["html"]
                new_links, new_prods = discover_links_from_page(
                    path, page_html, products, explicitly_seeded_products
                )
                for prod in new_prods:
                    print(f"  [NEW PRODUCT DISCOVERED] {prod}")
                added = 0
                for link in new_links:
                    if link not in discovered:
                        discovered.add(link)
                        to_visit.append(link)
                        added += 1

                results[path] = result
                page_count += 1
                print(f"  [{page_count}] FOUND {path} (+{added} new)")
                time.sleep(0.2)

            browser.close()
    else:
        # Fast parallel BFS using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=workers) as executor:
            while to_visit:
                batch: list[str] = []
                while to_visit and len(batch) < workers * 2:
                    path = to_visit.popleft()
                    if path not in visited:
                        visited.add(path)
                        batch.append(path)

                if not batch:
                    break

                future_to_path = {
                    executor.submit(fetch_http, base_url, path, extra_headers): path
                    for path in batch
                }
                for future in as_completed(future_to_path):
                    path = future_to_path[future]
                    result = future.result()
                    if result is None:
                        print(f"  SKIP (404) {path}")
                        continue
                    if "redirect_to" in result:
                        target = result["redirect_to"]
                        print(f"  SKIP (redirect -> {target}) {path}")
                        continue

                    page_html = result["html"]
                    new_links, new_prods = discover_links_from_page(
                        path, page_html, products, explicitly_seeded_products
                    )
                    for prod in new_prods:
                        print(f"  [NEW PRODUCT DISCOVERED] {prod}")
                    added = 0
                    for link in new_links:
                        if link not in discovered:
                            discovered.add(link)
                            to_visit.append(link)
                            added += 1

                    results[path] = result
                    page_count += 1
                    print(f"  [{page_count}] FOUND {path} (+{added} new)")

    print(f"\nFetched {len(results)} valid pages total (across {len(products)} products)")

    # Phase 2: Process and save
    print("\nPhase 2: Processing and saving pages...")
    manifest = {}
    valid_filenames: set[str] = set()

    for path, data in sorted(results.items()):
        page_html = data["html"]
        title = extract_title(page_html)
        last_updated = extract_last_updated(page_html)
        article_html = extract_article_content(page_html)
        markdown = html_to_markdown(article_html)

        if not markdown or len(markdown) < 50:
            print(f"  SKIP (too short) {path}")
            continue

        filename = path_to_filename(path)
        filepath = output_dir / filename
        valid_filenames.add(filename)

        header = f"# {title}\n\n" if title else ""
        header += f"Source: {base_url}{path}\n"
        if last_updated:
            header += f"Last updated: {last_updated}\n"
        header += "\n"

        full_content = header + markdown
        filepath.write_text(full_content, encoding="utf-8")

        manifest[path] = {
            "title": title,
            "filename": filename,
            "size": len(full_content),
            "url": f"{base_url}{path}",
            "last_updated": last_updated,
        }
        date_tag = f" [{last_updated}]" if last_updated else ""
        print(f"  SAVED {filename} ({len(full_content)} chars){date_tag}")

    # Clean up stale/redirect-duplicate .md files no longer in manifest
    removed_files = 0
    for existing_md in sorted(output_dir.glob("*.md")):
        if existing_md.name not in valid_filenames:
            existing_md.unlink()
            removed_files += 1
            print(f"  REMOVED stale file {existing_md.name}")

    # Save manifest
    manifest_path = output_dir / "_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Save update tracker
    tracker_path = output_dir / "_last_updated.json"
    tracker = {
        path: info["last_updated"]
        for path, info in manifest.items()
        if info.get("last_updated")
    }
    tracker_path.write_text(
        json.dumps(tracker, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if region == "s3ns":
        scrape_s3ns_secnumcloud_status(output_dir)

    pages_with_dates = sum(1 for v in manifest.values() if v.get("last_updated"))
    print(f"\nManifest: {manifest_path}")
    print(f"Tracker: {tracker_path}")
    print(f"Total: {len(manifest)} pages ({pages_with_dates} with dates, {removed_files} stale files removed)")

    return manifest


S3NS_PREMI3NS_URL = "https://www.s3ns.io/offres/premi3ns-cloud-de-confiance"


def scrape_s3ns_secnumcloud_status(output_dir: Path) -> dict | None:
    """Fetch S3NS PREMI3NS product page and extract SecNumCloud 3.2 qualification status per service."""
    output_dir.mkdir(parents=True, exist_ok=True)
    status_path = output_dir / "_secnumcloud_status.json"
    print(f"\nFetching S3NS SecNumCloud qualification status from {S3NS_PREMI3NS_URL}...")
    req = urllib.request.Request(
        S3NS_PREMI3NS_URL,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            raw_html = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [Warning] Could not fetch {S3NS_PREMI3NS_URL}: {e}", file=sys.stderr)
        if status_path.exists():
            return json.loads(status_path.read_text(encoding="utf-8"))
        return None

    idx = raw_html.find("Liste des services")
    snippet = raw_html[idx:] if idx != -1 else raw_html
    parts = snippet.split('<div class="relative flex flex-col items-center rounded-[10px]')

    seen_names: set[str] = set()
    services: list[dict] = []

    for part in parts[1:]:
        card = part.split("</a></div>")[0]
        h3_m = re.search(r"<h3[^>]*>([^<]+)</h3>", card)
        if not h3_m:
            continue
        name = html.unescape(h3_m.group(1)).strip()
        if not name or name in seen_names:
            continue
        seen_names.add(name)

        badge_m = re.search(r'<div class="absolute right-3 z-10 top-3">(.*?)</div>', card, re.S)
        badge_raw = (
            re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", badge_m.group(1)))).strip()
            if badge_m
            else ""
        )
        badge_lower = badge_raw.lower()
        if "en cours" in badge_lower or "qualification" in badge_lower:
            status = "in_progress"
            status_label = "Qualification en cours"
        elif "venir" in badge_lower:
            status = "upcoming"
            status_label = "À venir"
        elif not badge_raw:
            status = "qualified"
            status_label = "Qualifié SecNumCloud 3.2"
        else:
            status = "other"
            status_label = badge_raw

        p_m = re.search(r"<p[^>]*>([^<]+)</p>", card)
        desc = html.unescape(p_m.group(1)).strip() if p_m else ""
        href_m = re.search(r'<a[^>]+href="([^"]+)"', card)
        href = html.unescape(href_m.group(1)).strip() if href_m else ""

        services.append(
            {
                "name": name,
                "status": status,
                "status_label": status_label,
                "description": desc,
                "url": href,
            }
        )

    if not services:
        print("  [Warning] No service cards parsed from PREMI3NS page", file=sys.stderr)
        return None

    counts = {
        "qualified": sum(1 for s in services if s["status"] == "qualified"),
        "in_progress": sum(1 for s in services if s["status"] == "in_progress"),
        "upcoming": sum(1 for s in services if s["status"] == "upcoming"),
    }
    payload = {
        "source_url": S3NS_PREMI3NS_URL,
        "summary": counts,
        "services": services,
    }
    status_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"  SAVED {status_path.name} ({len(services)} services: "
        f"{counts['qualified']} qualified SecNumCloud 3.2, "
        f"{counts['in_progress']} qualification in progress, "
        f"{counts['upcoming']} upcoming)"
    )
    return payload


def main():
    parser = argparse.ArgumentParser(description="Scrape sovereign cloud docs")
    parser.add_argument("--region", default="berlin",
                        choices=["berlin", "s3ns", "all"],
                        help="Region to scrape (default: berlin)")
    parser.add_argument("--output-dir", default=None,
                        help="Output directory (default: per-region)")
    parser.add_argument("--use-playwright", action="store_true",
                        help="Use Playwright headless browser instead of fast HTTP SSR fetcher")
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS,
                        help=f"Number of parallel HTTP workers (default: {DEFAULT_WORKERS})")
    parser.add_argument("--secnumcloud-only", action="store_true",
                        help="Only fetch and update S3NS SecNumCloud qualification status")
    args = parser.parse_args()

    script_dir = Path(__file__).parent.parent

    if args.secnumcloud_only:
        output_dir = script_dir / (args.output_dir or REGIONS["s3ns"]["default_output_dir"])
        scrape_s3ns_secnumcloud_status(output_dir)
        return

    regions_to_scrape = list(REGIONS.keys()) if args.region == "all" else [args.region]

    for region in regions_to_scrape:
        if args.output_dir and len(regions_to_scrape) == 1:
            output_dir = script_dir / args.output_dir
        else:
            output_dir = script_dir / REGIONS[region]["default_output_dir"]

        manifest = crawl_and_scrape(
            output_dir,
            region,
            use_playwright=args.use_playwright,
            workers=args.workers,
        )

        if not manifest:
            print(f"\nERROR: No pages were scraped for {region}!",
                  file=sys.stderr)
            sys.exit(1)

        print(f"\nDone! Scraped {len(manifest)} pages for {region} to {output_dir}")
        print()


if __name__ == "__main__":
    main()
