#!/usr/bin/env python3
"""Fast broken-link audit for the local mirror."""
from pathlib import Path
from urllib.parse import unquote
from collections import defaultdict
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

WWW = Path('www').resolve()

broken = defaultdict(list)
missing_targets = defaultdict(list)
checked = 0

for html_file in WWW.rglob('*.html'):
    rel = html_file.relative_to(WWW)
    try:
        text = html_file.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue

    soup = BeautifulSoup(text, 'lxml')
    attrs = [('a', 'href'), ('link', 'href'), ('script', 'src'),
             ('img', 'src'), ('source', 'srcset'), ('video', 'poster'),
             ('audio', 'src'), ('embed', 'src'), ('object', 'data')]

    for tag, attr in attrs:
        for el in soup.find_all(tag):
            raw = el.get(attr)
            if not raw:
                continue
            # srcset can have multiple URLs
            for part in raw.split(','):
                url = part.strip().split()[0] if part.strip() else ''
                if not url or url.startswith('#') or url.startswith('data:') or \
                   url.startswith('javascript:') or url.startswith('mailto:') or \
                   url.startswith('tel:'):
                    continue
                if url.startswith('http') and not url.startswith('https://www.aeether.com') and not url.startswith('http://www.aeether.com'):
                    continue  # external

                checked += 1
                # Strip query/fragment
                url = url.split('#')[0].split('?')[0]
                url = unquote(url).strip('/')

                if url.startswith('https://www.aeether.com/') or url.startswith('http://www.aeether.com/'):
                    url = url.replace('https://www.aeether.com/', '').replace('http://www.aeether.com/', '')

                if url.startswith('/'):
                    target = WWW / url.lstrip('/')
                else:
                    target = (html_file.parent / url).resolve()
                    # Ensure still inside www
                    if not str(target).startswith(str(WWW)):
                        continue

                if not target.exists():
                    broken[str(rel)].append(url)
                    missing_targets[url].append(str(rel))

print(f'Total local links checked: {checked}')
print(f'Broken links found: {sum(len(v) for v in broken.values())}')
print(f'Pages with broken links: {len(broken)}')
print(f'Unique missing targets: {len(missing_targets)}')

print('\n=== Top missing targets ===')
for target, pages in sorted(missing_targets.items(), key=lambda x: -len(x[1]))[:50]:
    print(f'{target} (referenced from {len(pages)} pages)')

print('\n=== Sample pages with broken links ===')
for page, links in list(broken.items())[:20]:
    print(f'{page}: {links[:5]}')
