#!/usr/bin/env python3
"""
validate_conversion.py
Validation checks for category and product template rollout.
"""
import subprocess
import re
from pathlib import Path

BASE = Path("C:/Users/WIN10/STEELCHINA/docs/tgm")
PRODUCTS_DIR = BASE / "products"
HOST = "http://localhost:8080"

CATEGORY_SAMPLES = [
    "nickel-alloy.html",
    "nickel-alloy-pipes.html",
    "nickel-alloy-fittings.html",
    "nickel-alloy-bars.html",
    "nickel-alloy-sheets.html",
    "nickel-alloy-wires.html",
]

PRODUCT_SAMPLES = [
    "nickel-alloy-seamless-pipe-tube.html",
    "nickel-alloy-elbow.html",
    "nickel-alloy-round-bar-rod.html",
    "nickel-alloy-sheet.html",
    "nickel-alloy-wire.html",
    "nickel-alloy-plate.html",
    "nickel-alloy-coil.html",
    "monel-400-nickel-alloy-seamless-pipe-tube.html",
    "inconel-625-nickel-alloy-plate.html",
    "hastelloy-C-276-nickel-alloy-wire.html",
    "incoloy-825-nickel-alloy-reducer.html",
    "nickel-alloy-capillary-tube.html",
    "nickel-alloy-coil-tube.html",
    "nickel-alloy-welded-pipe-tube.html",
    "nickel-alloy-thick-walled-pipe.html",
    "nickel-alloy-hexagon-bar.html",
    "nickel-alloy-flat-bar.html",
    "hastelloy-B-2-nickel-alloy-bars.html",
    "monel-K-500-nickel-alloy-round-bar-rod.html",
    "inconel-718-nickel-alloy-strip.html",
]


def curl_head(url):
    try:
        result = subprocess.run(
            ["curl", "-I", "-s", "--max-time", "10", url],
            capture_output=True, text=True, check=False
        )
        return result.stdout + result.stderr
    except Exception as e:
        return f"ERROR: {e}"


def _attr_refs(text):
    """Yield path-like values from href/src attributes."""
    for m in re.finditer(r'(?:href|src)=["\']([^"\']+)["\']', text, re.IGNORECASE):
        yield m.group(1)


def _basename(ref):
    # Strip query/fragment, normalize separators, return filename
    return ref.split("?")[0].split("#")[0].replace("\\", "/").split("/")[-1]


def check_file(path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    issues = []

    # Duplicate opening tags (rough check)
    if len(re.findall(r"<html(?=[\s>])", text, re.IGNORECASE)) > 1:
        issues.append("duplicate <html>")
    if len(re.findall(r"<body(?=[\s>])", text, re.IGNORECASE)) > 1:
        issues.append("duplicate <body>")

    # Legacy CSS/JS — match whole file references only
    legacy_files = [
        "nav.css", "products.css", "products-all.css", "products-all.js",
        "category-all.css", "category-all.js", "footer.js",
    ]
    refs = list(_attr_refs(text))
    for bad in legacy_files:
        if any(_basename(r) == bad for r in refs):
            issues.append(f"legacy ref: {bad}")

    # Required enterprise CSS/JS
    is_product = path.parent.name == "products"
    if is_product:
        if "/tgm/product-enterprise.css" not in text:
            issues.append("missing product-enterprise.css")
        if "/tgm/product-enterprise.js" not in text:
            issues.append("missing product-enterprise.js")
    else:
        if "category-enterprise.css" not in text:
            issues.append("missing category-enterprise.css")
        if "category-enterprise.js" not in text:
            issues.append("missing category-enterprise.js")

    if "/tgm/tgm-core.js" not in text:
        issues.append("missing tgm-core.js")
    if "/tgm/components/global-footer.js" not in text:
        issues.append("missing global-footer.js")
    if '<div id="global-footer"></div>' not in text:
        issues.append("missing #global-footer div")

    # Images and tables presence
    has_img = "<img" in text
    has_table = "<table" in text

    return issues, has_img, has_table


def main():
    all_samples = [(BASE / p, f"/tgm/{p}") for p in CATEGORY_SAMPLES] + \
                  [(PRODUCTS_DIR / p, f"/tgm/products/{p}") for p in PRODUCT_SAMPLES]

    print(f"Validating {len(all_samples)} sample pages via {HOST}\n")
    print("=" * 80)

    curl_ok = 0
    curl_fail = []
    for path, rel in all_samples:
        url = f"{HOST}{rel}"
        out = curl_head(url)
        if "HTTP/1.0 200 OK" in out or "HTTP/1.1 200 OK" in out:
            curl_ok += 1
            print(f"[OK] {rel}")
        else:
            curl_fail.append(rel)
            print(f"[FAIL] {rel}\n{out[:200]}")

    print("\n" + "=" * 80)
    print(f"HTTP 200: {curl_ok}/{len(all_samples)}")
    if curl_fail:
        print("Failed:", curl_fail)

    print("\n" + "=" * 80)
    print("File-level validation:")
    file_ok = 0
    file_issues = []
    total_tables = 0
    total_imgs = 0
    for path, rel in all_samples:
        if not path.exists():
            file_issues.append((rel, ["file not found"]))
            continue
        issues, has_img, has_table = check_file(path)
        total_imgs += int(has_img)
        total_tables += int(has_table)
        if issues:
            file_issues.append((rel, issues))
            print(f"[ISSUE] {rel}: {', '.join(issues)}")
        else:
            file_ok += 1
            print(f"[OK] {rel} (img={has_img}, table={has_table})")

    print("\n" + "=" * 80)
    print(f"File checks passed: {file_ok}/{len(all_samples)}")
    print(f"Samples with images: {total_imgs}/{len(all_samples)}")
    print(f"Samples with tables: {total_tables}/{len(all_samples)}")
    if file_issues:
        print("\nIssues summary:")
        for rel, issues in file_issues:
            print(f"  {rel}: {issues}")


if __name__ == "__main__":
    main()
