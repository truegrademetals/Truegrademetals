#!/usr/bin/env python3
"""Repair empty files in the mirror by re-fetching from origin."""
import os
import sys
import logging
import time
from pathlib import Path
from urllib.parse import urljoin, quote
from curl_cffi import requests
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

BASE_DIR = Path('www')
BASE_URL = 'https://www.aeether.com/'


def url_from_path(rel_path: Path) -> str:
    # Convert Windows backslashes to forward slashes
    rel_str = rel_path.as_posix()
    # URL-encode individual path segments to handle spaces etc.
    parts = rel_str.split('/')
    encoded = '/'.join(quote(part, safe='') for part in parts)
    return urljoin(BASE_URL, encoded)


def repair_empty(max_retries: int = 2):
    empty_files = [p for p in BASE_DIR.rglob('*') if p.is_file() and p.stat().st_size == 0]
    logging.info(f'Found {len(empty_files)} empty files')

    fixed = 0
    still_empty = 0
    failed = []

    for empty_file in tqdm(empty_files, desc='Repairing empty files'):
        rel = empty_file.relative_to(BASE_DIR)
        url = url_from_path(rel)

        for attempt in range(max_retries + 1):
            try:
                resp = requests.get(url, impersonate='chrome', timeout=60)
                if resp.status_code == 200 and len(resp.content) > 0:
                    empty_file.write_bytes(resp.content)
                    fixed += 1
                    break
                else:
                    if attempt == max_retries:
                        failed.append((str(rel), resp.status_code, len(resp.content)))
                        still_empty += 1
            except Exception as e:
                if attempt == max_retries:
                    failed.append((str(rel), f'ERR:{type(e).__name__}', str(e)))
                    still_empty += 1
            time.sleep(0.05)

    logging.info(f'Fixed: {fixed}, Still empty/failed: {still_empty}')
    if failed:
        logging.warning('Failed URLs (first 30):')
        for item in failed[:30]:
            logging.warning(f'  {item}')


if __name__ == '__main__':
    repair_empty()
