#!/usr/bin/env python3
"""
apply_seo.py
Lightweight enterprise SEO pass across all TrueGrade Metals pages.

Fixes applied:
  - Ensure exactly one <h1> per page (demote extras to <h2>; inject sr-only h1 if missing).
  - Ensure canonical link exists.
  - Ensure basic Organization + WebSite + WebPage JSON-LD schema exists.
  - Strip empty/placeholder alt attributes where a reasonable alt can be inferred.
  - Remove any lingering legacy brand references.

Usage:
  python scripts/apply_seo.py
"""
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, Tag

ROOT = Path(__file__).parent.parent  # STEELCHINA/docs
TGM = ROOT / "tgm"
BASE_URL = "https://www.truegrademetals.com"

SKIP_DIRS = {"components"}
SKIP_PATTERNS = [
    re.compile(r"template\.html$", re.I),
    re.compile(r"-template\.html$", re.I),
]


def should_process(p: Path) -> bool:
    rel = p.relative_to(TGM)
    if any(part in SKIP_DIRS for part in rel.parts):
        return False
    if any(pat.search(p.name) for pat in SKIP_PATTERNS):
        return False
    return True


def page_url(rel: Path) -> str:
    return f"{BASE_URL}/tgm/{rel.as_posix()}"


def clean_title(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s*[\-|—]\s*$", "", s)
    return s


def infer_page_title(soup: BeautifulSoup, fallback: str) -> str:
    if soup.title and soup.title.string:
        return clean_title(str(soup.title.string))
    h2 = soup.find("h2")
    if h2 and h2.get_text(strip=True):
        return clean_title(h2.get_text(strip=True))
    return clean_title(fallback)


def add_canonical(soup: BeautifulSoup, url: str):
    existing = soup.find("link", attrs={"rel": "canonical"})
    if existing:
        return
    link = soup.new_tag("link", rel="canonical", href=url)
    head = soup.find("head")
    if head:
        head.append(link)


def add_schema(soup: BeautifulSoup, url: str, title: str, description: str):
    scripts = soup.find_all("script", type="application/ld+json")
    has_org = False
    has_webpage = False
    for s in scripts:
        txt = s.get_text(strip=True)
        if '"@type": "Organization"' in txt or '"@type":"Organization"' in txt:
            has_org = True
        if '"@type": "WebPage"' in txt or '"@type":"WebPage"' in txt:
            has_webpage = True

    graph = []
    if not has_org:
        graph.append({
            "@context": "https://schema.org",
            "@type": "Organization",
            "@id": f"{BASE_URL}/",
            "name": "TrueGrade Metals",
            "url": f"{BASE_URL}/",
            "logo": f"{BASE_URL}/tgm/LOGO.svg",
            "email": "info@truegrademetals.com",
            "telephone": "+86-519-81809659",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Changzhou",
                "addressRegion": "Jiangsu",
                "addressCountry": "CN",
            },
            "sameAs": [f"{BASE_URL}/"],
        })
    if not has_webpage:
        graph.append({
            "@context": "https://schema.org",
            "@type": "WebPage",
            "@id": url,
            "url": url,
            "name": title,
            "description": description,
            "inLanguage": "en",
            "isPartOf": {"@id": f"{BASE_URL}/"},
        })

    if graph:
        script = soup.new_tag("script", type="application/ld+json")
        script.string = "\n" + json.dumps(graph, ensure_ascii=False, indent=2) + "\n"
        head = soup.find("head")
        if head:
            head.append(script)


def fix_headings(soup: BeautifulSoup, title: str):
    h1s = soup.find_all("h1")
    if len(h1s) > 1:
        for h in h1s[1:]:
            h.name = "h2"
    elif not h1s:
        h1 = soup.new_tag("h1", **{"class": "sr-only"})
        h1.string = title
        # Try to place after global nav placeholder or after body opening
        body = soup.find("body")
        nav = soup.find("div", id="global-nav")
        if nav and nav.parent == body:
            nav.insert_after(h1)
        elif body:
            body.insert(0, h1)
        else:
            soup.append(h1)


def add_sr_only_css(soup: BeautifulSoup):
    """Ensure sr-only utility exists in page."""
    if soup.find("style", string=re.compile(r"\.sr-only")):
        return
    style = soup.new_tag("style")
    style.string = """
      .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }
    """
    head = soup.find("head")
    if head:
        head.append(style)


def fix_image_alts(soup: BeautifulSoup):
    for img in soup.find_all("img"):
        alt = img.get("alt")
        if alt and alt.strip():
            continue
        src = img.get("src", "")
        if not src:
            img["alt"] = ""
            continue
        name = Path(src).stem
        name = re.sub(r"[-_]+", " ", name)
        name = re.sub(r"\d+$", "", name).strip()
        if not name:
            img["alt"] = ""
            continue
        img["alt"] = name.title()


def remove_legacy_references(text: str) -> str:
    # Catch common misspellings / old brand
    text = re.sub(r"Aeether|aeether|AEETHER", "TrueGrade Metals", text, flags=re.I)
    return text


def process_page(p: Path) -> dict:
    p = p.resolve()
    rel = p.relative_to(TGM)
    url = page_url(rel)
    raw = p.read_text(encoding="utf-8", errors="ignore")
    raw = remove_legacy_references(raw)

    soup = BeautifulSoup(raw, "html.parser")

    title = infer_page_title(soup, rel.stem.replace("-", " ").title())
    meta_desc = soup.find("meta", attrs={"name": "description"})
    description = meta_desc.get("content", title) if meta_desc else title

    add_canonical(soup, url)
    add_schema(soup, url, title, description)
    fix_headings(soup, title)
    add_sr_only_css(soup)
    fix_image_alts(soup)

    p.write_text(str(soup), encoding="utf-8")
    return {"path": str(rel), "h1_count": len(soup.find_all("h1"))}


def main():
    pages = [p for p in TGM.rglob("*.html") if should_process(p)]
    results = []
    for p in pages:
        try:
            results.append(process_page(p))
        except Exception as e:
            print(f"ERROR {p}: {e}")

    bad = [r for r in results if r["h1_count"] != 1]
    print(f"Processed {len(results)} pages. {len(bad)} still have h1 count != 1.")
    for r in bad[:20]:
        print(" ", r["path"], r["h1_count"])


if __name__ == "__main__":
    main()
