#!/usr/bin/env python3
"""Fast broken-link audit for the local mirror (regex-only)."""
from pathlib import Path
from urllib.parse import unquote
from collections import defaultdict
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

WWW = Path('www').resolve()

# Pre-compile regex
link_re = re.compile(r'(?:href|src|data-src|poster|data-url|srcset)=["\']([^"\']+)["\']', re.IGNORECASE)
url_re = re.compile(r'url\(["\']?([^\)"\']+)["\']?\)', re.IGNORECASE)

broken = defaultdict(list)
missing_targets = defaultdict(list)
checked = 0
html_files = list(WWW.rglob('*.html'))
logging.info(f'Scanning {len(html_files)} HTML files...')

for idx, html_file in enumerate(html_files, 1):
    rel = html_file.relative_to(WWW)
    try:
        text = html_file.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue

    # Ignore URLs inside HTML comments (many templates comment out menu items)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    urls = set(link_re.findall(text)) | set(url_re.findall(text))

    for raw in urls:
        # srcset may contain multiple URLs with descriptors
        for part in raw.split(','):
            url = part.strip().split()[0] if part.strip() else ''
            if not url:
                continue
            if url[0] == '#' or url.startswith('data:') or \
               url.startswith('javascript:') or url.startswith('mailto:') or \
               url.startswith('tel:') or url.startswith('cdn-cgi/'):
                continue
            if url.startswith('http') and 'www.aeether.com' not in url:
                continue  # external

            checked += 1
            url = url.split('#')[0].split('?')[0]
            url = unquote(url).strip('/')
            url = url.replace('https://www.aeether.com/', '').replace('http://www.aeether.com/', '')

            if url.startswith('/'):
                target = WWW / url.lstrip('/')
            else:
                target = (html_file.parent / url).resolve()
                if not str(target).startswith(str(WWW)):
                    continue

            if not target.exists():
                broken[str(rel)].append(url)
                missing_targets[url].append(str(rel))

    if idx % 200 == 0:
        logging.info(f'  {idx}/{len(html_files)} files scanned...')

print(f'\nTotal local links checked: {checked}')
print(f'Broken links found: {sum(len(v) for v in broken.values())}')
print(f'Pages with broken links: {len(broken)}')
print(f'Unique missing targets: {len(missing_targets)}')

print('\n=== Top missing targets ===')
for target, pages in sorted(missing_targets.items(), key=lambda x: -len(x[1]))[:50]:
    print(f'{target} (referenced from {len(pages)} pages)')

print('\n=== Sample pages with broken links ===')
for page, links in list(broken.items())[:20]:
    print(f'{page}: {links[:5]}')
