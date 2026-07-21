#!/usr/bin/env python3
"""
audit_performance.py
Lightweight performance / accessibility pre-audit.
Reports common issues without running Lighthouse.
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


def should_check(p: Path) -> bool:
    rel = p.relative_to(TGM)
    if any(part in SKIP_DIRS for part in rel.parts):
        return False
    if any(pat.search(p.name) for pat in SKIP_PATTERNS):
        return False
    return True


def main():
    pages = [ROOT / "index.html"]
    pages += [p for p in TGM.rglob("*.html") if should_check(p)]

    missing_alt = []
    missing_lazy = []
    missing_dimensions = []
    render_blocking = []

    for p in pages:
        raw = p.read_text(encoding="utf-8", errors="ignore")
        soup = BeautifulSoup(raw, "html.parser")

        for img in soup.find_all("img"):
            # Only below-fold images need lazy; skip tiny icons/logos
            src = img.get("src", "")
            if not src or "LOGO" in src or "logo" in src.lower() or src.endswith(".svg"):
                continue
            alt = img.get("alt", "")
            if not alt or alt.strip() in {"", "image", "img"}:
                missing_alt.append((p.name, src[:60]))
            if img.get("loading", "").lower() != "lazy":
                missing_lazy.append((p.name, src[:60]))
            if not img.get("width") or not img.get("height"):
                missing_dimensions.append((p.name, src[:60]))

        # Look for render-blocking CSS not preconnected or inlined
        for link in soup.find_all("link", rel="stylesheet"):
            href = link.get("href", "")
            if href.startswith("http") and "fonts.googleapis.com" not in href:
                render_blocking.append((p.name, href[:60]))

    print(f"Audited {len(pages)} pages.")
    print(f"Images missing useful alt: {len(missing_alt)}")
    print(f"Images missing loading=lazy: {len(missing_lazy)}")
    print(f"Images missing explicit width/height: {len(missing_dimensions)}")
    print(f"External render-blocking stylesheets: {len(render_blocking)}")

    print("\nSample missing alt (first 10):")
    for name, src in missing_alt[:10]:
        print(f"  {name}: {src}")

    print("\nSample missing dimensions (first 10):")
    for name, src in missing_dimensions[:10]:
        print(f"  {name}: {src}")


if __name__ == "__main__":
    main()
