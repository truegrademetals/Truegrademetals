#!/usr/bin/env python3
"""
Generate /sitemap.xml for the TrueGrade Metals website.

Usage:
  python scripts/generate_sitemap.py

Rules:
  - Includes all .html pages under the project root.
  - Excludes component/template files, redirects and utility pages.
  - Uses file mtime for <lastmod>.
  - Assigns priority by page type.
"""
from pathlib import Path
from datetime import datetime, timezone
import re

ROOT = Path(__file__).parent.parent  # STEELCHINA/docs
BASE_URL = "https://www.truegrademetals.com"

EXCLUDE_PATHS = {
    "tgm/index.html",            # redirect only
    "tgm/components",
    "tgm/why-trust-truegrade-metals.html",  # optional: keep if public
}

EXCLUDE_PATTERNS = [
    r"^tgm/components/",
]


def priority_for(rel: str) -> str:
    if rel == "index.html":
        return "1.0"
    if re.search(r"tgm/nickel-alloy[^/]*\.html$", rel):
        return "0.9"
    if "/products/" in rel:
        return "0.8"
    if "/grades/" in rel:
        return "0.8"
    if "/solutions/" in rel:
        return "0.8"
    if "/guides/" in rel:
        return "0.8"
    if "/media/" in rel:
        return "0.7"
    if "/tools/" in rel:
        return "0.7"
    if rel.startswith("tgm/blog"):
        return "0.7"
    if rel in {"tgm/about-us.html", "tgm/contact-us.html", "tgm/gallery.html", "tgm/media.html", "tgm/grades.html", "tgm/solutions.html", "tgm/tools.html"}:
        return "0.8"
    return "0.5"


def should_include(rel: str) -> bool:
    for pat in EXCLUDE_PATTERNS:
        if re.search(pat, rel):
            return False
    if rel in EXCLUDE_PATHS:
        return False
    if rel.endswith("template.html") or rel.endswith("-template.html"):
        return False
    return True


def url_for(rel: str) -> str:
    if rel == "index.html":
        return BASE_URL + "/"
    return BASE_URL + "/" + rel.replace("\\", "/")


def main():
    pages = []
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT).as_posix()
        if not should_include(rel):
            continue
        mtime = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc)
        pages.append({
            "loc": url_for(rel),
            "lastmod": mtime.strftime("%Y-%m-%d"),
            "priority": priority_for(rel),
        })

    pages.sort(key=lambda x: x["loc"])

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for page in pages:
        lines.extend([
            "  <url>",
            f"    <loc>{page['loc']}</loc>",
            f"    <lastmod>{page['lastmod']}</lastmod>",
            f"    <priority>{page['priority']}</priority>",
            "  </url>",
        ])
    lines.append("</urlset>")

    sitemap = ROOT / "sitemap.xml"
    sitemap.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {sitemap} with {len(pages)} URLs.")


if __name__ == "__main__":
    main()
