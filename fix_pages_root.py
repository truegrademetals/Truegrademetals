#!/usr/bin/env python3
"""Point home links to the GitHub Pages repo subpath."""
from pathlib import Path

WWW = Path('www').resolve()
changed = 0
for html_file in WWW.rglob('*.html'):
    text = html_file.read_text(encoding='utf-8', errors='ignore')
    new_text = text.replace('href="/"', 'href="/Steel-China/"')
    if new_text != text:
        html_file.write_text(new_text, encoding='utf-8')
        changed += 1
print(f'Updated home links in {changed} files.')
