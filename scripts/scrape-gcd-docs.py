#!/usr/bin/env python3
"""Scrape Google Cloud Dedicated documentation from berlin.devsitetest.how.

Uses Playwright for headless browser rendering (JS-rendered content).
Crawls:
  1. All pages under /docs/* (the cross-cutting GCD docs)
  2. Per-product landing pages (/<product>/docs)
  3. Per-product tpc-differences pages (/<product>/docs/tpc-differences)
  4. First-level sub-pages linked from each product landing page

Tracks last-updated dates for incremental re-scrapes.

Requirements:
    pip install playwright
    playwright install chromium

Usage:
    python3 scripts/scrape-gcd-docs.py [--output-dir docs-raw]
"""

import argparse
import html
import json
import re
import sys
import time
from collections import deque
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

BASE_URL = "https://berlin.devsitetest.how"
EXTRA_HEADERS = {"X-DevSite-Proxy": "gcd"}
MAX_RETRIES = 3
PAGE_TIMEOUT = 30_000
NETWORK_IDLE_TIMEOUT = 10_000

# Products available in GCD
GCD_PRODUCTS = [
    "access-context-manager",
    "api-keys",
    "artifact-registry",
    "bigquery",
    "compute",
    "dns",
    "iam",
    "kms",
    "kubernetes-engine",
    "logging",
    "monitoring",
    "pubsub",
    "resource-manager",
    "service-usage",
    "sql",
    "storage",
]

# Paths that are deep GCP docs trees we should NOT recurse into.
# We only want the landing page and tpc-differences from these.
DEEP_CRAWL_BLOCKLIST = {
    "ai-introduction", "reference", "samples", "release-notes",
    "pricing", "quotas-limits", "resources", "api",
}

# Product sub-pages known to contain GCD-specific content (rewritten with
# GCD endpoints, project prefixes, etc.). Discovered by scanning all product
# sub-pages for GCD markers (apis-berlin, eu0:, universe_domain, etc.).
# These are added as explicit seeds rather than discovered via crawl,
# because crawling product sub-pages expands into thousands of standard
# GCP docs pages.
GCD_PRODUCT_PAGES = [
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
    "/bigquery/docs/tables",
    "/bigquery/docs/troubleshoot-quotas",
    "/compute/docs/instances/create-start-instance",
    "/compute/docs/instances/ssh",
    "/compute/docs/reference/rest/v1",
    "/compute/docs/release-notes",
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
    "/iam/docs/service-accounts-create",
    "/iam/docs/service-agents",
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


def is_crawlable_link(link: str, source_path: str = "") -> bool:
    """Decide whether to follow a link during crawl.

    Rules:
    - /docs/* paths: always follow (GCD-specific cross-cutting docs)
    - /<product>/docs: follow if it's a known GCD product (landing page)
    - /<product>/docs/tpc-differences: always follow (GCD-specific diffs)
    - Other /<product>/docs/* sub-pages: do NOT follow (standard GCP docs)

    The per-product sub-pages under /<product>/docs/ are standard GCP
    documentation served through the GCD proxy. They are not GCD-specific.
    Only the tpc-differences pages contain GCD-specific content.
    """
    if link.startswith("/docs"):
        return True

    parts = link.lstrip("/").split("/")
    if len(parts) < 2 or parts[1] != "docs":
        return False

    product = parts[0]
    if product not in GCD_PRODUCTS:
        return False

    # Product landing: /<product>/docs
    if len(parts) == 2:
        return True

    # Only follow tpc-differences sub-pages during crawl.
    # Other GCD-specific product sub-pages are added as explicit seeds
    # via GCD_PRODUCT_PAGES (discovered by scanning for GCD markers).
    sub_page = parts[2] if len(parts) > 2 else ""
    return sub_page == "tpc-differences"


# -- Link extraction -----------------------------------------------------------

DOC_LINK_RE = re.compile(
    r'href="('
    r'/docs(?:/[^"?#]*)?'
    r'|'
    r'/[a-z][a-z0-9-]*/docs(?:/[^"?#]*)?'
    r')"'
)


def extract_links(page_html: str) -> list[str]:
    """Extract all documentation links from rendered HTML."""
    links: set[str] = set()
    for m in DOC_LINK_RE.finditer(page_html):
        path = m.group(1).rstrip("/")
        if path and path != "/docs":
            links.add(path)
    return sorted(links)


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


# -- Main crawl ----------------------------------------------------------------

def crawl_and_scrape(output_dir: Path) -> dict:
    """Crawl and scrape all GCD documentation pages using Playwright."""
    output_dir.mkdir(parents=True, exist_ok=True)

    discovered: set[str] = set()
    to_visit: deque[str] = deque()
    visited: set[str] = set()
    results: dict[str, dict] = {}

    # Seed paths
    seeds = ["/docs"]
    for product in GCD_PRODUCTS:
        seeds.append(f"/{product}/docs")
        seeds.append(f"/{product}/docs/tpc-differences")
    seeds.extend(GCD_PRODUCT_PAGES)

    for p in seeds:
        discovered.add(p)
        to_visit.append(p)

    print(f"Starting crawl from {BASE_URL}")
    print(f"Seed pages: {len(seeds)}")
    print(f"Output directory: {output_dir}")
    print()

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(
            extra_http_headers=EXTRA_HEADERS,
            user_agent="GCD-Docs-Scraper/2.0 (Playwright)",
        )

        def fetch(path: str) -> dict | None:
            url = BASE_URL + path
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

                    page.wait_for_timeout(800)
                    rendered = page.content()
                    page.close()
                    return {"html": rendered}

                except PwTimeout:
                    page.close()
                    wait = 2 ** (attempt + 1)
                    print(f"  [Timeout] {path} - retry {attempt+1}",
                          file=sys.stderr)
                    time.sleep(wait)
                except Exception as e:
                    page.close()
                    wait = 2 ** (attempt + 1)
                    print(f"  [Error] {path}: {e}", file=sys.stderr)
                    time.sleep(wait)

            print(f"  [FAILED] {path}", file=sys.stderr)
            return None

        # BFS crawl
        print("Phase 1: Discovering and fetching pages...")
        page_count = 0
        while to_visit:
            path = to_visit.popleft()
            if path in visited:
                continue
            visited.add(path)

            result = fetch(path)
            if result is None:
                print(f"  SKIP {path}")
                continue

            page_html = result["html"]
            # Only discover new links from /docs/* pages and product landing/tpc-differences pages.
            # Product sub-pages link deep into GCP docs; don't follow those.
            should_discover = (
                path.startswith("/docs")
                or path.endswith("/docs")
                or "tpc-differences" in path
            )
            new_count = 0
            if should_discover:
                new_links = extract_links(page_html)
                for link in new_links:
                    if link not in discovered and is_crawlable_link(link, path):
                        discovered.add(link)
                        to_visit.append(link)
                        new_count += 1

            results[path] = result
            page_count += 1
            print(f"  [{page_count}] FOUND {path} (+{new_count} new)")

            time.sleep(0.3)

        browser.close()

    print(f"\nFetched {len(results)} pages total")

    # Phase 2: Process and save
    print("\nPhase 2: Processing and saving pages...")
    manifest = {}

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

        header = f"# {title}\n\n" if title else ""
        header += f"Source: {BASE_URL}{path}\n"
        if last_updated:
            header += f"Last updated: {last_updated}\n"
        header += "\n"

        full_content = header + markdown
        filepath.write_text(full_content, encoding="utf-8")

        manifest[path] = {
            "title": title,
            "filename": filename,
            "size": len(full_content),
            "url": f"{BASE_URL}{path}",
            "last_updated": last_updated,
        }
        date_tag = f" [{last_updated}]" if last_updated else ""
        print(f"  SAVED {filename} ({len(full_content)} chars){date_tag}")

    # Save manifest
    manifest_path = output_dir / "_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    # Save update tracker
    tracker_path = output_dir / "_last_updated.json"
    tracker = {
        path: info["last_updated"]
        for path, info in manifest.items()
        if info.get("last_updated")
    }
    tracker_path.write_text(
        json.dumps(tracker, indent=2, ensure_ascii=False), encoding="utf-8")

    pages_with_dates = sum(1 for v in manifest.values() if v.get("last_updated"))
    print(f"\nManifest: {manifest_path}")
    print(f"Tracker: {tracker_path}")
    print(f"Total: {len(manifest)} pages ({pages_with_dates} with dates)")

    return manifest


def main():
    parser = argparse.ArgumentParser(description="Scrape GCD documentation")
    parser.add_argument("--output-dir", default="docs-raw",
                        help="Output directory (default: docs-raw)")
    args = parser.parse_args()

    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / args.output_dir

    manifest = crawl_and_scrape(output_dir)

    if not manifest:
        print("\nERROR: No pages were scraped!", file=sys.stderr)
        sys.exit(1)

    print(f"\nDone! Scraped {len(manifest)} pages to {output_dir}")


if __name__ == "__main__":
    main()
