#!/usr/bin/env python3
"""Point every logo/home anchor to the site root (/)."""
from pathlib import Path
from bs4 import BeautifulSoup
import re

WWW = Path('www').resolve()
HOME_PAT = re.compile(r'^(?:\.\./)*index\.html$|^(?:\.\./)*AEETHER/index\.html$')

def is_home_anchor(tag):
    href = tag.get('href', '')
    # Recognise root-level index redirect or relative ../index.html variants
    if HOME_PAT.match(href):
        return True
    if href in ('AEETHER/index.html', '/AEETHER/index.html', '/index.html'):
        return True
    return False

def looks_like_home_link(tag):
    if not is_home_anchor(tag):
        return False
    # Logo image anywhere inside the anchor
    for img in tag.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt', '')
        if 'LOGO.svg' in src or 'logo' in alt.lower() or 'AEETHER' in alt:
            return True
    # Plain "AEETHER" text breadcrumb / footer title
    text = tag.get_text(strip=True)
    if text == 'AEETHER':
        return True
    return False

html_files = list(WWW.rglob('*.html'))
changed = 0
for idx, html_file in enumerate(html_files, 1):
    text = html_file.read_text(encoding='utf-8', errors='ignore')
    soup = BeautifulSoup(text, 'lxml')
    modified = False
    for a in soup.find_all('a'):
        if looks_like_home_link(a):
            a['href'] = '/'
            modified = True
    if modified:
        html_file.write_text(str(soup), encoding='utf-8')
        changed += 1
    if idx % 200 == 0:
        print(f'  {idx}/{len(html_files)} files checked...')

print(f'Fixed home links in {changed}/{len(html_files)} files.')
