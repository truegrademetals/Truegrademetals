#!/usr/bin/env python3
"""
fix_images.py
Add loading="lazy" and intrinsic width/height attributes to reduce CLS.
Skips the first image on each page (assumed above-the-fold / LCP candidate).
"""
import re
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image as PilImage

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


def resolve_image_src(page: Path, src: str) -> Path | None:
    if not src or src.startswith(("http://", "https://", "data:", "#")):
        return None
    if src.lower().endswith(".svg"):
        return None
    # Resolve relative to the page directory
    if src.startswith("/"):
        return ROOT / src.lstrip("/")
    return page.parent / src


def get_image_dimensions(p: Path) -> tuple[int, int] | None:
    try:
        with PilImage.open(p) as im:
            return im.width, im.height
    except Exception:
        return None


def process_page(p: Path) -> dict:
    raw = p.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(raw, "html.parser")
    imgs = soup.find_all("img")
    lazy_added = 0
    dims_added = 0

    for idx, img in enumerate(imgs):
        src = img.get("src", "")

        # Loading strategy: first image eager (default), rest lazy
        if not img.get("loading"):
            if idx == 0:
                img["loading"] = "eager"
            else:
                img["loading"] = "lazy"
                lazy_added += 1

        # Skip dimension injection for SVGs and images that already have both
        if img.get("width") and img.get("height"):
            continue
        if src.lower().endswith(".svg"):
            continue

        img_path = resolve_image_src(p, src)
        if img_path and img_path.exists():
            dims = get_image_dimensions(img_path)
            if dims:
                img["width"] = str(dims[0])
                img["height"] = str(dims[1])
                dims_added += 1

    p.write_text(str(soup), encoding="utf-8")
    return {"path": p.relative_to(ROOT).as_posix(), "lazy_added": lazy_added, "dims_added": dims_added}


def main():
    pages = [ROOT / "index.html"]
    pages += [p for p in TGM.rglob("*.html") if should_check(p)]

    total_lazy = 0
    total_dims = 0
    for p in pages:
        try:
            r = process_page(p)
            total_lazy += r["lazy_added"]
            total_dims += r["dims_added"]
        except Exception as e:
            print(f"ERROR {p}: {e}")

    print(f"Processed {len(pages)} pages.")
    print(f"Added loading=lazy to {total_lazy} images.")
    print(f"Added width/height to {total_dims} images.")


if __name__ == "__main__":
    main()
