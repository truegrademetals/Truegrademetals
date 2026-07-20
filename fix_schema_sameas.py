import re
from pathlib import Path

ROOT = Path('docs/tgm')
PATTERN = re.compile(
    r'"sameAs":\s*\[[^\]]*?"https://www\.truegrademetals\.com Metals-Co-Limited-102908481648226"[^\]]*?\]',
    re.DOTALL
)
REPLACEMENT = '"sameAs": [\n                "https://www.truegrademetals.com"\n              ]'

for path in ROOT.rglob('*.html'):
    try:
        text = path.read_text(encoding='utf-8', errors='surrogateescape')
    except Exception as e:
        print(f'Skip read {path}: {e}')
        continue
    original = text
    text = PATTERN.sub(REPLACEMENT, text)
    if text != original:
        try:
            path.write_text(text, encoding='utf-8', errors='surrogateescape')
            print(f'Fixed {path}')
        except Exception as e:
            print(f'Failed write {path}: {e}')
