import os
import re
from pathlib import Path

ROOT = Path('docs/tgm')
PATTERN = re.compile(r'(?<=["\'(])\/Steel-China\/?')

def homepage_prefix(path):
    rel = os.path.relpath(ROOT, path.parent).replace('\\', '/')
    if rel == '.':
        return '../index.html'
    else:
        return rel + '/../index.html'

for path in ROOT.rglob('*'):
    if not path.is_file():
        continue
    if path.suffix.lower() not in ('.html', '.css', '.js'):
        continue
    try:
        text = path.read_text(encoding='utf-8', errors='surrogateescape')
    except Exception as e:
        print(f'Skip read {path}: {e}')
        continue
    original = text
    prefix = homepage_prefix(path)
    text = PATTERN.sub(prefix, text)
    if text != original:
        try:
            path.write_text(text, encoding='utf-8', errors='surrogateescape')
            print(f'Fixed {path}')
        except Exception as e:
            print(f'Failed write {path}: {e}')
