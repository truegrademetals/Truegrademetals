#!/usr/bin/env python3
"""Recursive mirror of www.aeether.com for the STEELCHINA project.

Starts from the homepage and sitemap, follows every internal link to discover
all HTML pages, downloads all referenced assets, and rewrites links so the
site works offline.
"""
import os
import re
import sys
import time
import logging
import argparse
from pathlib import Path
from queue import Queue
from urllib.parse import urljoin, urlparse, urlunparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

from curl_cffi import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("recursive_mirror.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)

BASE_URL = "https://www.aeether.com"
OUTPUT_DIR = Path("www")

ASSET_EXTENSIONS = {
    ".css", ".js", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".ttf", ".otf", ".woff", ".woff2", ".eot",
    ".mp4", ".webm", ".mp3", ".ogg",
}

SKIP_PREFIXES = (
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

stats_lock = Lock()
downloaded_pages = 0
downloaded_assets = 0
failed_pages = []
failed_assets = []


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    path = unquote(parsed.path)
    return urlunparse((parsed.scheme, parsed.netloc, path, parsed.params, parsed.query, ""))


def is_internal(url: str) -> bool:
    parsed = urlparse(url)
    if not parsed.netloc:
        return True
    return parsed.netloc.lower() == urlparse(BASE_URL).netloc.lower()


def is_html_url(url: str) -> bool:
    parsed = urlparse(url)
    path = unquote(parsed.path)
    ext = Path(path).suffix.lower()
    return ext in ("", ".html", ".htm", ".php", ".asp", ".aspx")


def url_to_local_path(url: str) -> Path:
    parsed = urlparse(url)
    path = unquote(parsed.path)
    if path.startswith("/"):
        path = path[1:]
    if not path:
        path = "index.html"
    local = OUTPUT_DIR / path.replace("/", os.sep)
    if local.suffix == "":
        local = local / "index.html"
    return local


def local_path_to_url(local_path: Path) -> str:
    rel = local_path.relative_to(OUTPUT_DIR).as_posix()
    if rel.endswith("/index.html"):
        rel = rel[:-11]
    if not rel or rel == "index.html":
        return BASE_URL + "/"
    return f"{BASE_URL}/{rel}"


def download(url: str, local_path: Path, retries: int = 3, timeout: int = 60) -> bool:
    local_path.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=timeout, stream=True)
            resp.raise_for_status()
            content_type = resp.headers.get("Content-Type", "").lower()
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
            time.sleep(2 * (attempt + 1))
    logger.error("Giving up on %s", url)
    return False


def extract_urls(html: str, page_url: str) -> set:
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

    for tag in soup.find_all("a", href=True):
        add(tag["href"])
    for tag in soup.find_all("img"):
        for attr in ("src", "data-src", "data-original"):
            add(tag.get(attr, ""))
        srcset = tag.get("srcset") or tag.get("data-srcset")
        if srcset:
            for part in srcset.split(","):
                candidate = part.strip().split(" ")[0]
                add(candidate)
    for tag in soup.find_all("source", srcset=True):
        for part in tag["srcset"].split(","):
            candidate = part.strip().split(" ")[0]
            add(candidate)
    for tag in soup.find_all("link", href=True):
        add(tag["href"])
    for tag in soup.find_all("script", src=True):
        add(tag["src"])
    for tag in soup.find_all(["video", "audio"]):
        add(tag.get("src", ""))
        add(tag.get("poster", ""))
    for style_tag in soup.find_all("style"):
        for match in re.finditer(r'url\s*\(\s*["\']?([^"\')\s]+)', style_tag.get_text()):
            add(match.group(1))
    for tag in soup.find_all(style=True):
        for match in re.finditer(r'url\s*\(\s*["\']?([^"\')\s]+)', tag["style"]):
            add(match.group(1))

    return found


def rewrite_html(html: str, page_url: str) -> str:
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
            return os.path.relpath(target_local, page_dir).replace(os.sep, "/")
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
    sitemap_url = f"{BASE_URL}/sitemap.xml"
    logger.info("Fetching sitemap: %s", sitemap_url)
    urls = set()
    try:
        resp = session.get(sitemap_url, timeout=60)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "xml")
        for loc in soup.find_all("loc"):
            url = loc.get_text(strip=True)
            if is_internal(url):
                urls.add(normalize_url(url))
    except Exception as e:
        logger.error("Cannot fetch sitemap: %s", e)
    logger.info("Sitemap contains %s internal URLs", len(urls))
    return urls


def discover_and_mirror(max_workers: int = 6):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Start set of pages to crawl.
    seed_urls = fetch_sitemap()
    seed_urls.add(normalize_url(BASE_URL + "/"))

    # Track known/queued URLs to avoid duplicates.
    known_pages = set()
    known_assets = set()
    page_queue = Queue()

    for url in seed_urls:
        if is_html_url(url):
            known_pages.add(url)
            page_queue.put(url)
        else:
            known_assets.add(url)

    logger.info("Initial queue: %s pages", page_queue.qsize())

    # --- Phase 1: recursively discover and download HTML pages ---
    def process_page(url: str) -> set:
        global downloaded_pages
        local_path = url_to_local_path(url)
        needs_download = True

        if local_path.exists() and local_path.stat().st_size > 0:
            # Re-parse existing local copy to discover links (it may already be rewritten).
            try:
                html = local_path.read_text(encoding="utf-8", errors="ignore")
                discovered = extract_urls(html, url)
                # If it's already rewritten, many links are relative; extract_urls handles them via urljoin.
                needs_download = False
            except Exception:
                discovered = set()
        else:
            discovered = set()

        if needs_download:
            try:
                resp = session.get(url, timeout=60)
                resp.raise_for_status()
            except Exception as e:
                logger.warning("Page download failed: %s -> %s", url, e)
                with stats_lock:
                    failed_pages.append(url)
                return set()

            html = resp.text
            discovered = extract_urls(html, url)
            rewritten = rewrite_html(html, url)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_text(rewritten, encoding="utf-8", errors="replace")
            with stats_lock:
                downloaded_pages += 1

        return discovered

    pbar = tqdm(total=page_queue.qsize(), desc="Pages discovered")
    active = True

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        # Seed initial batch
        while not page_queue.empty() and len(futures) < max_workers * 2:
            url = page_queue.get()
            futures[executor.submit(process_page, url)] = url

        while futures:
            for future in as_completed(list(futures.keys())):
                url = futures.pop(future)
                try:
                    discovered = future.result()
                except Exception as e:
                    logger.error("Page processing failed: %s -> %s", url, e)
                    with stats_lock:
                        failed_pages.append(url)
                    discovered = set()

                new_pages = 0
                new_assets = 0
                for d in discovered:
                    if is_html_url(d):
                        if d not in known_pages:
                            known_pages.add(d)
                            page_queue.put(d)
                            new_pages += 1
                    else:
                        if d not in known_assets:
                            known_assets.add(d)
                            new_assets += 1

                if new_pages:
                    pbar.total += new_pages
                pbar.update(1)

                # Submit more work if available
                while not page_queue.empty() and len(futures) < max_workers * 2:
                    next_url = page_queue.get()
                    futures[executor.submit(process_page, next_url)] = next_url

                if not futures and page_queue.empty():
                    break

        pbar.close()

    logger.info("Phase 1 complete: %s pages known, %s assets discovered", len(known_pages), len(known_assets))
    logger.info("Downloaded/re-parsed pages: %s, failed: %s", downloaded_pages, len(failed_pages))

    # --- Phase 2: download all discovered assets ---
    def process_asset(url: str) -> bool:
        global downloaded_assets
        local_path = url_to_local_path(url)
        if local_path.exists() and local_path.stat().st_size > 0:
            if local_path.suffix.lower() == ".css":
                rewrite_css_file(local_path, url)
            return True

        ext = local_path.suffix.lower()
        timeout = 300 if ext in (".pdf", ".mp4", ".webm", ".zip", ".rar", ".7z") else 45

        ok = download(url, local_path, timeout=timeout)
        if ok:
            with stats_lock:
                downloaded_assets += 1
            if ext == ".css":
                rewrite_css_file(local_path, url)
        else:
            with stats_lock:
                failed_assets.append(url)
        return ok

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_asset, url): url for url in sorted(known_assets)}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Assets"):
            url = futures[future]
            try:
                future.result()
            except Exception as e:
                logger.error("Asset processing failed: %s -> %s", url, e)
                with stats_lock:
                    failed_assets.append(url)

    logger.info("=" * 60)
    logger.info("Recursive mirror complete")
    logger.info("Pages: %s known, %s newly downloaded, %s failed", len(known_pages), downloaded_pages, len(failed_pages))
    logger.info("Assets: %s discovered, %s newly downloaded, %s failed", len(known_assets), downloaded_assets, len(failed_assets))
    if failed_pages:
        logger.info("Failed pages (first 20): %s", failed_pages[:20])
    if failed_assets:
        logger.info("Failed assets (first 20): %s", failed_assets[:20])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursive mirror of aeether.com for STEELCHINA")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent workers")
    args = parser.parse_args()
    discover_and_mirror(max_workers=args.workers)
