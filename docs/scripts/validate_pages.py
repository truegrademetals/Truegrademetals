#!/usr/bin/env python3
"""
validate_pages.py
Structural validation for the unified TrueGrade Metals website.

Checks every HTML page under tgm/ (and root index.html) for:
  - Exactly one <html> and one <body>
  - Global nav / footer placeholders present
  - No legacy footer markers (e.g. id/class containing old brand patterns)
  - No Aeether brand references
  - Exactly one <h1>
  - Canonical link present
  - <title> present
"""
import re
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent.parent
TGM = ROOT / "tgm"

SKIP_DIRS = {"components"}
SKIP_PATTERNS = [
    re.compile(r"template\.html$", re.I),
    re.compile(r"-template\.html$", re.I),
]

LEGACY_MARKERS = [
    re.compile(r"Aeether", re.I),
    re.compile(r"aeether", re.I),
]


def should_check(p: Path) -> bool:
    rel = p.relative_to(TGM)
    if any(part in SKIP_DIRS for part in rel.parts):
        return False
    if any(pat.search(p.name) for pat in SKIP_PATTERNS):
        return False
    return True


def check_page(p: Path) -> list:
    errors = []
    raw = p.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(raw, "html.parser")

    if len(soup.find_all("html")) != 1:
        errors.append("html count != 1")
    if len(soup.find_all("body")) != 1:
        errors.append("body count != 1")
    if not soup.find("div", id="global-nav"):
        errors.append("missing #global-nav")
    if not soup.find("div", id="global-footer"):
        errors.append("missing #global-footer")
    if not soup.title or not soup.title.string.strip():
        errors.append("missing title")
    if len(soup.find_all("h1")) != 1:
        errors.append(f"h1 count = {len(soup.find_all('h1'))}")
    if not soup.find("link", attrs={"rel": "canonical"}):
        errors.append("missing canonical")

    lower = raw.lower()
    for marker in LEGACY_MARKERS:
        if marker.search(raw):
            errors.append(f"legacy marker: {marker.pattern}")
            break
    return errors


def main():
    pages = [ROOT / "index.html"]
    pages += [p for p in TGM.rglob("*.html") if should_check(p)]

    bad = []
    for p in pages:
        try:
            errs = check_page(p)
            if errs:
                bad.append((p.relative_to(ROOT).as_posix(), errs))
        except Exception as e:
            bad.append((p.relative_to(ROOT).as_posix(), [str(e)]))

    print(f"Checked {len(pages)} pages. {len(bad)} pages have issues.")
    for path, errs in bad[:30]:
        print(f"  {path}: {errs}")
    if len(bad) > 30:
        print(f"  ... and {len(bad)-30} more")


if __name__ == "__main__":
    main()
