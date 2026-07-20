#!/usr/bin/env python3
"""Mirror www.aeether.com into a local STEELCHINA project."""

import os
import re
import sys
import time
import hashlib
import logging
import argparse
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed

from curl_cffi import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("mirror.log", encoding="utf-8"), logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

BASE_URL = "https://www.aeether.com"
OUTPUT_DIR = Path("www")
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)

# Assets we want to download in addition to HTML pages.
ASSET_EXTENSIONS = {
    ".css", ".js", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".ttf", ".otf", ".woff", ".woff2", ".eot",
    ".mp4", ".webm", ".mp3", ".ogg",
}

# Skip these external / CDN paths entirely.
SKIP_PREFIXES = (
    "http://", "https://",
    "//",
    "mailto:", "tel:", "javascript:", "data:",
    "/cdn-cgi/",
)

session = requests.Session(impersonate="chrome131")
session.headers.update({
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
})


def normalize_url(url: str) -> str:
    """Return a canonical URL string for deduplication."""
    parsed = urlparse(url)
    # Drop fragment, keep query.
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, ""))


def is_html_url(url: str) -> bool:
    """Return True if URL looks like an HTML page (no file extension or .html/.htm)."""
    parsed = urlparse(url)
    path = unquote(parsed.path)
    ext = Path(path).suffix.lower()
    return ext in ("", ".html", ".htm", ".php", ".asp", ".aspx")


def is_internal(url: str) -> bool:
    """Return True if URL belongs to the target domain."""
    parsed = urlparse(url)
    if not parsed.netloc:
        return True
    return parsed.netloc.lower() == urlparse(BASE_URL).netloc.lower()


def url_to_local_path(url: str) -> Path:
    """Map an absolute internal URL to a local filesystem path under OUTPUT_DIR."""
    parsed = urlparse(url)
    path = unquote(parsed.path)
    if path.startswith("/"):
        path = path[1:]
    if not path:
        path = "index.html"
    # If path ends with /, treat as index.html inside that directory.
    local = OUTPUT_DIR / path.replace("/", os.sep)
    if local.suffix == "":
        local = local / "index.html"
    return local


def download(url: str, local_path: Path, retries: int = 3, timeout: int = 60) -> bool:
    """Download a single URL to a local file. Returns True on success."""
    local_path.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=timeout, stream=True)
            resp.raise_for_status()
            content_type = resp.headers.get("Content-Type", "").lower()
            # Decide text vs binary mode.
            if "text" in content_type or "json" in content_type or "xml" in content_type:
                text = resp.text
                local_path.write_text(text, encoding="utf-8", errors="replace")
            else:
                with open(local_path, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            return True
        except Exception as e:
            logger.warning("Download failed (%s/%s): %s -> %s", attempt + 1, retries, url, e)
            if local_path.exists():
                try:
                    local_path.unlink()
                except Exception:
                    pass
            time.sleep(2 * (attempt + 1))
    logger.error("Giving up on %s", url)
    return False


def extract_urls_from_html(html: str, page_url: str) -> set:
    """Extract all internal URLs (pages + assets) referenced from an HTML page."""
    soup = BeautifulSoup(html, "lxml")
    found = set()

    def add(raw_url: str):
        if not raw_url:
            return
        raw_url = raw_url.strip()
        if raw_url.startswith(SKIP_PREFIXES):
            return
        absolute = urljoin(page_url, raw_url)
        if not is_internal(absolute):
            return
        found.add(normalize_url(absolute))

    # <a href>
    for tag in soup.find_all("a", href=True):
        add(tag["href"])

    # <img src / data-src / srcset>
    for tag in soup.find_all("img"):
        for attr in ("src", "data-src", "data-original"):
            add(tag.get(attr, ""))
        srcset = tag.get("srcset") or tag.get("data-srcset")
        if srcset:
            for part in srcset.split(","):
                candidate = part.strip().split(" ")[0]
                add(candidate)

    # <source srcset>
    for tag in soup.find_all("source", srcset=True):
        for part in tag["srcset"].split(","):
            candidate = part.strip().split(" ")[0]
            add(candidate)

    # <link href>
    for tag in soup.find_all("link", href=True):
        add(tag["href"])

    # <script src>
    for tag in soup.find_all("script", src=True):
        add(tag["src"])

    # <video>/<audio> src, poster
    for tag in soup.find_all(["video", "audio"]):
        add(tag.get("src", ""))
        add(tag.get("poster", ""))

    # Inline CSS url(...)
    for style_tag in soup.find_all("style"):
        for match in re.finditer(r'url\s*\(\s*["\']?([^"\')\s]+)', style_tag.get_text()):
            add(match.group(1))

    # Inline style attributes url(...)
    for tag in soup.find_all(style=True):
        for match in re.finditer(r'url\s*\(\s*["\']?([^"\')\s]+)', tag["style"]):
            add(match.group(1))

    return found


def rewrite_html(html: str, page_url: str) -> str:
    """Rewrite internal URLs in HTML to local relative paths."""
    soup = BeautifulSoup(html, "lxml")
    page_dir = Path(url_to_local_path(page_url)).parent

    def rel(raw_url: str) -> str:
        if not raw_url:
            return raw_url
        stripped = raw_url.strip()
        if stripped.startswith(SKIP_PREFIXES):
            return raw_url
        absolute = urljoin(page_url, stripped)
        if not is_internal(absolute):
            return raw_url
        target_local = url_to_local_path(absolute)
        try:
            rel_path = os.path.relpath(target_local, page_dir)
            # Normalize to forward slashes for HTML.
            return rel_path.replace(os.sep, "/")
        except ValueError:
            return raw_url

    def rewrite_srcset(value: str) -> str:
        parts = []
        for part in value.split(","):
            bits = part.strip().split(" ", 1)
            if bits:
                bits[0] = rel(bits[0])
                parts.append(" ".join(bits))
        return ", ".join(parts)

    for tag in soup.find_all("a", href=True):
        tag["href"] = rel(tag["href"])

    for tag in soup.find_all("img"):
        for attr in ("src", "data-src", "data-original"):
            if tag.get(attr):
                tag[attr] = rel(tag[attr])
        for attr in ("srcset", "data-srcset"):
            if tag.get(attr):
                tag[attr] = rewrite_srcset(tag[attr])

    for tag in soup.find_all("source", srcset=True):
        tag["srcset"] = rewrite_srcset(tag["srcset"])

    for tag in soup.find_all("link", href=True):
        tag["href"] = rel(tag["href"])

    for tag in soup.find_all("script", src=True):
        tag["src"] = rel(tag["src"])

    for tag in soup.find_all(["video", "audio"]):
        if tag.get("src"):
            tag["src"] = rel(tag["src"])
        if tag.get("poster"):
            tag["poster"] = rel(tag["poster"])

    def rewrite_css_urls(css_text: str) -> str:
        return re.sub(
            r'url\s*\(\s*(["\']?)([^"\')\s]+)\1\s*\)',
            lambda m: f'url({m.group(1)}{rel(m.group(2))}{m.group(1)})',
            css_text,
        )

    for tag in soup.find_all("style"):
        tag.string = rewrite_css_urls(tag.get_text())

    for tag in soup.find_all(style=True):
        tag["style"] = rewrite_css_urls(tag["style"])

    return str(soup)


def rewrite_css_file(local_path: Path, base_page_url: str) -> None:
    """Rewrite url(...) references inside a downloaded CSS file."""
    try:
        text = local_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return

    css_dir = local_path.parent

    def rel(raw_url: str) -> str:
        stripped = raw_url.strip().strip('"').strip("'")
        if stripped.startswith(SKIP_PREFIXES):
            return raw_url
        absolute = urljoin(base_page_url, stripped)
        if not is_internal(absolute):
            return raw_url
        target_local = url_to_local_path(absolute)
        try:
            return os.path.relpath(target_local, css_dir).replace(os.sep, "/")
        except ValueError:
            return raw_url

    rewritten = re.sub(
        r'url\s*\(\s*(["\']?)([^"\')\s]+)\1\s*\)',
        lambda m: f'url({m.group(1)}{rel(m.group(2))}{m.group(1)})',
        text,
    )
    local_path.write_text(rewritten, encoding="utf-8")


def fetch_sitemap() -> set:
    """Fetch and parse sitemap.xml for the initial list of pages."""
    sitemap_url = f"{BASE_URL}/sitemap.xml"
    logger.info("Fetching sitemap: %s", sitemap_url)
    try:
        resp = session.get(sitemap_url, timeout=60)
        resp.raise_for_status()
    except Exception as e:
        logger.error("Cannot fetch sitemap: %s", e)
        return set()

    soup = BeautifulSoup(resp.text, "xml")
    urls = set()
    for loc in soup.find_all("loc"):
        url = loc.get_text(strip=True)
        if is_internal(url):
            urls.add(normalize_url(url))
    logger.info("Sitemap contains %s internal URLs", len(urls))
    return urls


def collect_pages():
    """Return (pages, file_assets) from the sitemap."""
    sitemap_urls = fetch_sitemap()
    home = normalize_url(BASE_URL + "/")
    if home in sitemap_urls:
        sitemap_urls.remove(home)

    pages = [home]
    file_assets = set()
    for url in sitemap_urls:
        if is_html_url(url):
            pages.append(url)
        else:
            file_assets.add(url)
    return pages, file_assets


def main(max_workers: int = 8):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pages, file_assets = collect_pages()
    if not pages:
        logger.error("No pages found; aborting.")
        return

    logger.info("Starting mirror of %s pages + %s sitemap file assets into %s",
                len(pages), len(file_assets), OUTPUT_DIR.resolve())

    # Track discovered asset URLs that are not HTML pages.
    asset_urls = set(file_assets)
    page_urls_set = set(pages)
    failed_pages = []

    # Phase 1: download HTML pages, rewrite them, and collect asset references.
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(download_and_rewrite_page, url): url for url in pages}
        for future in tqdm(as_completed(future_to_url), total=len(pages), desc="HTML pages"):
            url = future_to_url[future]
            try:
                discovered = future.result()
                for d in discovered:
                    if d not in page_urls_set:
                        asset_urls.add(d)
            except Exception as e:
                logger.error("Page processing failed: %s -> %s", url, e)
                failed_pages.append(url)

    logger.info("Discovered %s asset URLs", len(asset_urls))

    # Phase 2: download assets.
    failed_assets = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_asset = {executor.submit(download_asset, url): url for url in sorted(asset_urls)}
        for future in tqdm(as_completed(future_to_asset), total=len(asset_urls), desc="Assets"):
            url = future_to_asset[future]
            try:
                if not future.result():
                    failed_assets.append(url)
            except Exception as e:
                logger.error("Asset download failed: %s -> %s", url, e)
                failed_assets.append(url)

    # Summary.
    logger.info("=" * 60)
    logger.info("Mirror complete")
    logger.info("Pages: %s downloaded, %s failed", len(pages) - len(failed_pages), len(failed_pages))
    logger.info("Assets: %s discovered, %s failed", len(asset_urls), len(failed_assets))
    if failed_pages:
        logger.info("Failed pages: %s", failed_pages[:10])
    if failed_assets:
        logger.info("Failed assets: %s", failed_assets[:10])


def download_and_rewrite_page(url: str) -> set:
    """Download an HTML page, rewrite its links, and return discovered URLs.

    If the page already exists locally, skip the download and parse the local copy.
    """
    local_path = url_to_local_path(url)
    local_path.parent.mkdir(parents=True, exist_ok=True)

    if local_path.exists() and local_path.stat().st_size > 0:
        try:
            html = local_path.read_text(encoding="utf-8", errors="ignore")
            return extract_urls_from_html(html, url)
        except Exception:
            pass

    try:
        resp = session.get(url, timeout=60)
        resp.raise_for_status()
    except Exception as e:
        logger.warning("Page download failed: %s -> %s", url, e)
        raise

    html = resp.text
    discovered = extract_urls_from_html(html, url)
    rewritten = rewrite_html(html, url)
    local_path.write_text(rewritten, encoding="utf-8", errors="replace")
    return discovered


def download_asset(url: str) -> bool:
    """Download a non-HTML asset. Also rewrite CSS url() references."""
    local_path = url_to_local_path(url)
    if local_path.exists():
        return True

    # Large files (PDFs, videos, archives) need more time.
    ext = local_path.suffix.lower()
    timeout = 300 if ext in (".pdf", ".mp4", ".webm", ".zip", ".rar", ".7z") else 45

    ok = download(url, local_path, timeout=timeout)
    if ok and ext == ".css":
        rewrite_css_file(local_path, url)
    return ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mirror aeether.com for STEELCHINA project")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent download workers")
    args = parser.parse_args()
    main(max_workers=args.workers)
