#!/usr/bin/env python3
"""Find and download any missing assets from the aeether.com mirror."""

import os
import re
import sys
import logging
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed

from curl_cffi import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

BASE_URL = "https://www.aeether.com"
OUTPUT_DIR = Path("www")
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)

session = requests.Session(impersonate="chrome131")
session.headers.update({
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
})


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, ""))


def is_internal(url: str) -> bool:
    parsed = urlparse(url)
    if not parsed.netloc:
        return True
    return parsed.netloc.lower() == urlparse(BASE_URL).netloc.lower()


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


def extract_urls_from_html(html: str, page_url: str) -> set:
    soup = BeautifulSoup(html, "lxml")
    found = set()
    skip_prefixes = (
        "http://", "https://", "//", "mailto:", "tel:", "javascript:", "data:", "/cdn-cgi/",
    )

    def add(raw_url: str):
        if not raw_url:
            return
        raw_url = raw_url.strip()
        if raw_url.startswith(skip_prefixes):
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
                add(part.strip().split(" ")[0])
    for tag in soup.find_all("source", srcset=True):
        for part in tag["srcset"].split(","):
            add(part.strip().split(" ")[0])
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


def download(url: str, local_path: Path, timeout: int = 45) -> bool:
    local_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        resp = session.get(url, timeout=timeout, stream=True)
        resp.raise_for_status()
        content_type = resp.headers.get("Content-Type", "").lower()
        if "text" in content_type or "json" in content_type or "xml" in content_type:
            local_path.write_text(resp.text, encoding="utf-8", errors="replace")
        else:
            with open(local_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        return True
    except Exception as e:
        logger.warning("Failed: %s -> %s", url, e)
        if local_path.exists():
            try:
                local_path.unlink()
            except Exception:
                pass
        return False


def main():
    logger.info("Scanning downloaded HTML files for missing assets...")
    html_files = list(OUTPUT_DIR.rglob("*.html"))
    all_asset_urls = set()
    for html_file in tqdm(html_files, desc="Scanning HTML"):
        try:
            html = html_file.read_text(encoding="utf-8", errors="ignore")
            # Reconstruct the original URL from local path.
            rel = html_file.relative_to(OUTPUT_DIR)
            url_path = "/" + "/".join(rel.parts)
            if url_path.endswith("/index.html"):
                url_path = url_path[:-10]
            page_url = BASE_URL + url_path
            urls = extract_urls_from_html(html, page_url)
            for u in urls:
                local = url_to_local_path(u)
                if local.suffix.lower() not in ("", ".html", ".htm", ".php", ".asp", ".aspx"):
                    all_asset_urls.add(u)
        except Exception as e:
            logger.warning("Error scanning %s: %s", html_file, e)

    missing = [u for u in all_asset_urls if not url_to_local_path(u).exists()]
    logger.info("Total assets referenced: %s", len(all_asset_urls))
    logger.info("Missing assets: %s", len(missing))

    if not missing:
        logger.info("Mirror is complete. No missing assets.")
        return

    success = 0
    failed = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_url = {executor.submit(download, url, url_to_local_path(url)): url for url in missing}
        for future in tqdm(as_completed(future_to_url), total=len(missing), desc="Downloading missing"):
            url = future_to_url[future]
            try:
                if future.result():
                    success += 1
                else:
                    failed.append(url)
            except Exception as e:
                logger.error("Exception for %s: %s", url, e)
                failed.append(url)

    logger.info("=" * 60)
    logger.info("Completion summary: %s downloaded, %s failed", success, len(failed))
    if failed:
        logger.info("Failed URLs: %s", failed)


if __name__ == "__main__":
    main()
