#!/usr/bin/env python3
"""
convert_products.py
Apply the enterprise product template to all legacy product pages in tgm/products/.
Reference implementation: tgm/products/nickel-alloy-seamless-pipe-tube.html
"""
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, Tag

BASE = Path("C:/Users/WIN10/STEELCHINA/docs/tgm")
PRODUCTS_DIR = BASE / "products"
SCRIPT_DIR = Path(__file__).parent
LOG_PATH = SCRIPT_DIR / "convert_products.log"

SVG_CERT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>'
SVG_TRACE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
SVG_WORLD = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'
SVG_SUPPORT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'


def clean_text(t):
    if not t:
        return ""
    return " ".join(t.split())


def extract_meta(soup, name=None, prop=None):
    if name:
        tag = soup.find("meta", attrs={"name": name})
        if tag:
            return tag.get("content", "")
    if prop:
        tag = soup.find("meta", attrs={"property": prop})
        if tag:
            return tag.get("content", "")
    return ""


def extract_title(soup):
    return clean_text(soup.title.string) if soup.title else ""


def section_html(soup, section_id):
    sec = soup.find("section", id=section_id)
    if not sec:
        return ""
    return "".join(str(c) for c in sec.contents)


def first_tag_text(parent, tag_name):
    if not parent:
        return ""
    t = parent.find(tag_name)
    return clean_text(t.get_text()) if t else ""


def first_paragraph_text(parent):
    if not parent:
        return ""
    p = parent.find("p")
    if p:
        return clean_text(p.get_text())
    return clean_text(parent.get_text())[:250]


def build_head(soup, slug, canonical):
    title = extract_title(soup) or f"Nickel Alloy Product -- TrueGrade Metals"
    keywords = extract_meta(soup, "keywords") or "Nickel Alloy"
    description = extract_meta(soup, "description") or ""
    og_title = extract_meta(soup, prop="og:title") or title
    og_desc = extract_meta(soup, prop="og:description") or description
    og_image = extract_meta(soup, prop="og:image") or "https://www.truegrademetals.com/tgm/image/products/seamless-pipe-tube/main-photo-1.jpg"
    og_url = extract_meta(soup, prop="og:url") or canonical

    # Preserve all JSON-LD exactly as in legacy
    scripts = soup.find_all("script", type="application/ld+json")
    schema_blocks = []
    for s in scripts:
        txt = s.get_text(strip=True)
        if txt:
            schema_blocks.append(txt)

    schemas = "\n".join(f'<script type="application/ld+json">\n{b}\n</script>' for b in schema_blocks)

    return f"""<!DOCTYPE HTML>
<html lang="en">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start': new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-M2WGSR9');</script>
<!-- End Google Tag Manager -->
<meta charset="utf-8"/>
<title>{title}</title>
<meta content="{keywords}" name="keywords"/>
<meta content="TrueGrade Metals" name="author"/>
<meta content="{description}" name="description"/>
<meta content="width=device-width, initial-scale=1, maximum-scale=3, minimum-scale=1, user-scalable=no" name="viewport"/>
<meta content="telephone=no" name="format-detection"/>
<meta content="{og_title}" property="og:title"/>
<meta content="Products" property="og:type"/>
<meta content="{og_url}" property="og:url"/>
<meta content="{og_image}" property="og:image"/>
<meta content="truegrademetals.com" property="og:site_name"/>
<meta content="{og_desc}" property="og:description"/>
<link href="../favicon.ico" rel="shortcut icon"/>
<link href="../favicon.ico" rel="Bookmark"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&amp;family=Inter:wght@300;400;500;600;700&amp;family=Space+Grotesk:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="/tgm/components/tgm-tokens.css" rel="stylesheet"/>
<link href="/tgm/product-enterprise.css" rel="stylesheet"/>
<link href="/tgm/components/tgm-tables-graphs.css" rel="stylesheet"/>
<link href="/tgm/chemical-all.css" rel="stylesheet"/>
{schemas}
</head>"""


def build_hero(soup):
    sec = soup.find("section", id="main-page")
    if not sec:
        return "", "Nickel Alloy Product", "", ""

    # Product name from h1
    h1 = sec.find("h1")
    product_name = ""
    eyebrow = "Nickel Alloy from China"
    if h1:
        spans = h1.find_all("span")
        if spans:
            eyebrow = clean_text(spans[0].get_text())
            product_name = clean_text(h1.get_text().replace(spans[0].get_text(), ""))
        else:
            product_name = clean_text(h1.get_text())
    product_name = product_name or "Nickel Alloy Product"

    # Breadcrumb
    bread = sec.find("ol", id="breadol")
    breadcrumb_html = str(bread) if bread else f"""<ol id="breadol"><li><a href="/"><b>TrueGrade Metals</b></a></li><li><a href="/tgm/nickel-alloy.html"><b>Products</b></a></li><li>{product_name}</li></ol>"""

    # Grade chips
    grade_point = sec.find("div", class_="grade-point")
    if grade_point:
        grade_chips = "".join(str(c) for c in grade_point.contents)
    else:
        grade_chips = """<a class="monel-point" href="../grades/monel.html">MONEL</a><a class="inconel-point" href="../grades/inconel.html">INCONEL</a><a class="incoloy-point" href="../grades/incoloy.html">INCOLOY</a><a class="hastelloy-point" href="../grades/hastelloy.html">HASTELLOY</a>"""

    # Value proposition: prefer detail-description paragraph; otherwise generic
    dd = sec.find("div", id="detail-description")
    if dd:
        value_prop = first_paragraph_text(dd)
    else:
        value_prop = f"Precision {product_name.lower()} manufactured in China with full traceability and certified quality."

    # Main images for gallery later
    main_photo = sec.find("div", id="main-photo")
    thumb_photo = sec.find("div", id="main-photo-2")

    hero = f"""<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-M2WGSR9" style="display:none;visibility:hidden" width="0"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<!-- Global Navigation -->
<div id="global-nav" style="min-height:122px"></div>
<script src="/tgm/components/global-nav.js"></script>

<main id="main-content">

<!-- 1. Hero -->
<section id="main-page">
  {breadcrumb_html}
  <div id="title-bread">
    <h1><span>{eyebrow}</span>{product_name}</h1>
  </div>
  <div id="detail-description">
    <p>{value_prop}</p>
  </div>
  <div class="grade-point">
    {grade_chips}
  </div>
  <div class="cat-hero-trust" aria-label="Sourcing confidence">
    <span class="cat-hero-trust-item">{SVG_CERT} MTC included</span>
    <span class="cat-hero-trust-item">{SVG_TRACE} Full traceability</span>
    <span class="cat-hero-trust-item">{SVG_WORLD} Global shipping</span>
    <span class="cat-hero-trust-item">{SVG_SUPPORT} Engineering support</span>
  </div>
  <div class="cat-hero-cta">
    <button class="click-event" id="contactbutton" type="button">
      <img alt="Get a quote" src="../image/emaillogo.svg"/>
      <p>Get a Free Quote NOW</p>
    </button>
    <a class="cat-hero-secondary" href="/tgm/contact-us.html">Speak to an engineer</a>
  </div>
</section>"""

    return hero, product_name, str(main_photo) if main_photo else "", str(thumb_photo) if thumb_photo else ""


def build_quick_spec(soup):
    sec = soup.find("section", id="specifications-features-1")
    if not sec:
        return ""
    specs_div = sec.find("div", id="specifications")
    if not specs_div:
        return ""
    ul = specs_div.find("ul")
    cards = []
    if ul:
        for li in ul.find_all("li", recursive=False):
            txt = clean_text(li.get_text())
            txt = re.sub(r"^[•\s]+", "", txt)
            if ":" in txt:
                k, v = txt.split(":", 1)
                cards.append(f'<div class="prod-spec-card"><dt>{k.strip()}</dt><dd>{v.strip()}</dd></div>')
            elif txt:
                cards.append(f'<div class="prod-spec-card"><dt>Specification</dt><dd>{txt}</dd></div>')
    if not cards:
        return ""
    return f"""<!-- 2. Quick Specification Summary -->
<section id="prod-quick-spec" aria-labelledby="prod-spec-heading">
  <div class="cat-section-head">
    <h2 id="prod-spec-heading"><span>Specifications</span>Quick specification summary</h2>
  </div>
  <div class="prod-spec-grid">
    {''.join(cards[:8])}
  </div>
</section>"""


def build_gallery(main_photo_html, thumb_photo_html, product_name):
    if not main_photo_html:
        return ""
    # Convert legacy main-photo images to prod-gallery-slide
    soup_main = BeautifulSoup(main_photo_html, "lxml")
    imgs = []
    for idx, img in enumerate(soup_main.find_all("img"), start=1):
        cls = "prod-gallery-slide active" if idx == 1 else "prod-gallery-slide"
        alt = img.get("alt", f"{product_name} photo {idx}")
        src = img.get("src", "")
        lazy_attr = 'loading="lazy"' if idx > 1 else ""
        imgs.append(f'<img alt="{alt}" id="mainphoto{idx}" src="{src}" class="{cls}" {lazy_attr}/>')
    main_imgs = "\n".join(imgs)

    thumbs = []
    if thumb_photo_html:
        soup_thumb = BeautifulSoup(thumb_photo_html, "lxml")
        for idx, img in enumerate(soup_thumb.find_all("img"), start=1):
            alt = img.get("alt", f"{product_name} thumbnail {idx}")
            src = img.get("src", "")
            thumbs.append(f'<button type="button" data-index="{idx}" aria-label="View image {idx}"><img src="{src}" alt="{alt}" loading="lazy"/></button>')
    thumbs_html = "\n".join(thumbs)

    return f"""<!-- 3. Product Gallery -->
<section id="prod-gallery" aria-labelledby="prod-gallery-heading">
  <div class="cat-section-head">
    <h2 id="prod-gallery-heading"><span>Gallery</span>Product photos</h2>
  </div>
  <div class="prod-gallery-grid">
    <div class="prod-gallery-main">
      {main_imgs}
    </div>
    <div class="prod-gallery-thumbs">
      {thumbs_html}
    </div>
  </div>
</section>"""


def build_overview(soup):
    sec = soup.find("section", id="description-catalogue-1")
    if not sec:
        return ""
    desc = sec.find("div", id="description-catalogue-2")
    if not desc:
        return ""
    # Remove the H2 Overview heading to avoid duplicate
    for h in desc.find_all("h2"):
        h.decompose()
    content = "".join(str(c) for c in desc.contents)
    return f"""<!-- 4. Product Overview -->
<section id="prod-overview" aria-labelledby="prod-overview-heading">
  <div class="cat-section-head">
    <h2 id="prod-overview-heading"><span>Overview</span>Product overview</h2>
  </div>
  <div class="prod-overview-inner">
    {content}
  </div>
</section>"""


def build_benefits(soup):
    sec = soup.find("section", id="main-page")
    if not sec:
        return ""
    adv = sec.find("div", id="main-advantage")
    if not adv:
        return ""
    cards = []
    for div in adv.find_all("div", recursive=False):
        img = div.find("img")
        p = div.find("p")
        if img and p:
            alt = img.get("alt", "")
            src = img.get("src", "")
            # Preserve existing <br/> tags; just clean whitespace in text nodes
            text_html = "".join(str(c) for c in p.contents)
            text_html = re.sub(r"\s+", " ", text_html).strip()
            cards.append(f'<article class="prod-benefit-card"><img alt="{alt}" class="main-advantage-logo" src="{src}"/><p>{text_html}</p></article>')
    if not cards:
        return ""
    return f"""<!-- 5. Engineering Benefits -->
<section id="prod-benefits" aria-labelledby="prod-benefits-heading">
  <div class="cat-section-head">
    <h2 id="prod-benefits-heading"><span>Engineering</span>Engineering benefits</h2>
  </div>
  <div class="prod-benefits-grid">
    {''.join(cards)}
  </div>
</section>"""


def build_applications(soup):
    sec = soup.find("section", id="specifications-features-1")
    if not sec:
        return ""
    app_div = sec.find("div", id="applications")
    if not app_div:
        return ""
    # Convert ul li to app cards
    cards = []
    ul = app_div.find("ul")
    if ul:
        for li in ul.find_all("li", recursive=False):
            txt = clean_text(li.get_text())
            txt = re.sub(r"^\d+\.\s*", "", txt)
            if txt:
                cards.append(f'<article class="prod-app-card">{txt}</article>')
    if not cards:
        return ""
    return f"""<!-- 6. Applications -->
<section id="prod-applications" aria-labelledby="prod-app-heading">
  <div class="cat-section-head">
    <h2 id="prod-app-heading"><span>Applications</span>Where it is used</h2>
  </div>
  <div class="prod-app-grid">
    {''.join(cards)}
  </div>
</section>"""


def build_grades_section(soup):
    content = section_html(soup, "grades-page")
    if not content:
        return ""
    return f"""<!-- 7. Chemical Composition / Grades -->
<section id="grades-page">
  {content}
</section>"""


def build_technical_sheet(soup):
    content = section_html(soup, "technical-sheet-1")
    mp = section_html(soup, "mechanical-properties-1")
    eg = section_html(soup, "equivalent-grades-1")
    if not any([content, mp, eg]):
        return ""
    return f"""<!-- 8. Mechanical Properties & Technical Data -->
<section class="fold1" id="technical-sheet-1">
  {content}
  {mp}
  {eg}
</section>"""


def build_process(soup):
    content = section_html(soup, "process-formula-1")
    if not content:
        return ""
    return f"""<!-- 9. Technical Graphs / Manufacturing Process -->
<section id="process-formula-1">
  {content}
</section>"""


def build_standards(soup):
    sec = soup.find("section", id="specifications-features-1")
    standards = []
    if sec:
        std_div = sec.find("div", id="standards")
        if std_div:
            ul = std_div.find("ul")
            if ul:
                for li in ul.find_all("li", recursive=False):
                    txt = clean_text(li.get_text())
                    if txt:
                        standards.append(f"<li>{txt}</li>")
    if not standards:
        standards = ["<li>ASTM / ASME standards available on request</li>"]
    return f"""<!-- 10. Standards & Equivalent Grades -->
<section id="prod-standards" aria-labelledby="prod-standards-heading">
  <div class="cat-section-head">
    <h2 id="prod-standards-heading"><span>Standards</span>Standards &amp; equivalent grades</h2>
    <p>Products are produced and tested to ASTM / ASME specifications with DIN / EN equivalents available on request.</p>
  </div>
  <div class="prod-standards-grid">
    <div class="prod-standards-card">
      <h3>ASTM / ASME Standards</h3>
      <ul>
        {''.join(standards)}
      </ul>
    </div>
    <div class="prod-standards-card">
      <h3>Equivalent Grades</h3>
      <ul>
        <li>DIN / EN equivalents</li>
        <li>JIS equivalents</li>
        <li>GB standards on request</li>
        <li>Cross-reference sheets available</li>
      </ul>
    </div>
  </div>
</section>"""


def build_quality(soup):
    sec = soup.find("section", id="quality-inspection-1")
    if not sec:
        return """<!-- 11. Quality Assurance -->
<section id="prod-quality" aria-labelledby="prod-quality-heading">
  <div class="cat-section-head">
    <h2 id="prod-quality-heading"><span>Quality</span>Quality assurance</h2>
  </div>
  <div class="prod-quality-grid">
    <article class="prod-quality-card"><h3>Mill Test Certificates</h3><p>Every lot ships with original MTC per EN 10204/3.1, covering chemical composition and mechanical properties.</p></article>
    <article class="prod-quality-card"><h3>Full Traceability</h3><p>Batch tracking from melt through production to final delivery, with heat number and certificate references.</p></article>
    <article class="prod-quality-card"><h3>Inspection &amp; Testing</h3><p>Dimensional checks, surface inspection and non-destructive testing available on request.</p></article>
    <article class="prod-quality-card"><h3>Third-Party Verification</h3><p>Independent inspection by SGS, TÜV or your nominated body can be arranged before shipment.</p></article>
  </div>
</section>"""
    return f"""<!-- 11. Quality Assurance -->
<section id="prod-quality" aria-labelledby="prod-quality-heading">
  <div class="cat-section-head">
    <h2 id="prod-quality-heading"><span>Quality</span>Quality assurance</h2>
  </div>
  {str(sec)}
</section>"""


def build_downloads(soup):
    sec = soup.find("section", id="description-catalogue-1")
    if not sec:
        return ""
    cat = sec.find("div", id="description-catalogue-3")
    if not cat:
        return ""
    return f"""<!-- 12. Downloads -->
<section id="prod-downloads" aria-labelledby="prod-download-heading">
  <div class="prod-download-card">
    <h3 id="prod-download-heading">Download catalogue</h3>
    {str(cat)}
  </div>
</section>"""


def build_package_logistics(soup):
    sec = soup.find("section", id="package-logistics-1")
    if not sec:
        return ""
    # Split into package and logistics if possible
    pkg = sec.find("div", id="package") or sec.find("div", class_="package")
    log = sec.find("div", id="logistics") or sec.find("div", class_="logistics")
    pkg_html = ""
    log_html = ""
    if pkg:
        pkg_html = f"""<!-- 13. Package -->
<section id="prod-package" aria-labelledby="prod-package-heading">
  <div class="cat-section-head">
    <h2 id="prod-package-heading"><span>Shipping</span>Package</h2>
  </div>
  <div class="prod-container">
    <div class="prod-package-grid">
      {str(pkg)}
    </div>
  </div>
</section>"""
    if log:
        log_html = f"""<!-- 14. Logistics -->
<section id="prod-logistics" aria-labelledby="prod-logistics-heading">
  <div class="cat-section-head">
    <h2 id="prod-logistics-heading"><span>Shipping</span>Logistics</h2>
  </div>
  <div class="prod-container">
    <div class="prod-logistics-grid">
      {str(log)}
    </div>
  </div>
</section>"""
    if not pkg and not log:
        # Keep whole section as package
        pkg_html = f"""<!-- 13. Package -->
<section id="prod-package" aria-labelledby="prod-package-heading">
  <div class="cat-section-head">
    <h2 id="prod-package-heading"><span>Shipping</span>Package &amp; Logistics</h2>
  </div>
  <div class="prod-container">
    <div class="prod-package-grid">
      {str(sec)}
    </div>
  </div>
</section>"""
    return pkg_html + "\n" + log_html


def build_faq(soup):
    # Try to find FAQ section by id or class
    faq_sec = soup.find("section", id="faq") or soup.find("div", id="faq")
    if not faq_sec:
        # search for div containing Q/A
        for sec in soup.find_all("section"):
            if sec.find("div", class_="Q") or sec.find(class_="FAQ-fold-1"):
                faq_sec = sec
                break
    if not faq_sec:
        return ""
    return f"""<!-- 15. FAQs -->
<section id="prod-faq" aria-labelledby="prod-faq-heading">
  <div class="cat-section-head">
    <h2 id="prod-faq-heading"><span>FAQ</span>Frequently asked questions</h2>
  </div>
  <div class="prod-faq-list">
    {str(faq_sec)}
  </div>
</section>"""


def build_related_products(soup):
    # Prefer popular-products section
    for sid in ["popular-products", "related-products-1", "related-products"]:
        sec = soup.find("section", id=sid)
        if sec:
            return f"""<!-- 16. Related Products -->
<section id="popular-products">
  {str(sec)}
</section>"""
    return ""


def build_resources():
    return """<!-- 17. Related Resources -->
<section id="prod-resources" aria-labelledby="prod-resources-heading">
  <div class="cat-section-head">
    <h2 id="prod-resources-heading"><span>Resources</span>Related resources</h2>
  </div>
  <div class="prod-resources-grid">
    <a class="prod-resource-card" href="/tgm/tools/nickel-alloy-weight-calculator.html"><h3>Weight Calculator</h3><p>Quickly estimate the weight of nickel alloy pipe, bar, sheet and wire.</p><span class="cat-info-link">Calculate →</span></a>
    <a class="prod-resource-card" href="/tgm/tools/pipe-schedule-calculator.html"><h3>Pipe Schedule Calculator</h3><p>Find wall thickness and OD combinations for common schedules.</p><span class="cat-info-link">Calculate →</span></a>
    <a class="prod-resource-card" href="/tgm/tools/nickel-alloy-grades-comparison.html"><h3>Grade Comparison</h3><p>Cross-reference ASTM, DIN and EN grade equivalents.</p><span class="cat-info-link">Compare →</span></a>
    <a class="prod-resource-card" href="/tgm/media/alloy-knowledge/index.html"><h3>Alloy Knowledge</h3><p>Technical guides on Monel, Inconel, Incoloy and Hastelloy.</p><span class="cat-info-link">Read →</span></a>
    <a class="prod-resource-card" href="/tgm/nickel-alloy.html"><h3>Nickel Alloy Products</h3><p>Browse the full range of nickel alloy product forms.</p><span class="cat-info-link">View category →</span></a>
  </div>
</section>"""


def build_rfq(product_name):
    return f"""<!-- 18. RFQ Section -->
<section id="prod-rfq" aria-labelledby="prod-rfq-heading">
  <div class="prod-rfq-card">
    <h2 id="prod-rfq-heading">Request a competitive quotation</h2>
    <p>Tell us your grade, size, quantity and delivery destination. Our materials team will review your specification and return a professional quotation within 24 hours.</p>
    <div class="prod-rfq-actions">
      <a class="cat-btn" href="/tgm/contact-us.html">Get a Free Quote</a>
      <a class="cat-btn-ghost" href="mailto:info@truegrademetals.com">Email us directly</a>
    </div>
  </div>
</section>"""


def build_final_cta(product_name):
    return f"""<!-- 19. Final Trust CTA -->
<section id="prod-final-cta" aria-label="Final call to action">
  <div class="prod-final-cta-inner">
    <div>
      <h2>Ready to source {product_name.lower()}?</h2>
      <p>Engineering support, certified materials and global delivery — one message away.</p>
    </div>
    <a class="cat-btn" href="/tgm/contact-us.html">Request a Technical Quotation</a>
  </div>
</section>"""


def build_footer():
    return """</main>

<aside id="float-form" itemscope="" itemtype="https://schema.org/WPSideBar">
  <div class="click-event" id="floatbutton">
    <img alt="press and contact us" id="floatlogo" src="../image/emaillogo.svg" loading="lazy"/>
  </div>
  <div class="floatcontact1" id="floatcontact">
    <div id="floatcross"></div>
    <form action="mailto:info@truegrademetals.com" id="floatform" method="GET" enctype="text/plain" name="sendmail">
      <div class="short-input">
        <label class="label" for="aside-email">Your E-mail:</label>
        <input class="form1" id="aside-email" name="email" placeholder="Please input your E-mail" type="text"/>
      </div>
      <div class="short-input">
        <label class="label" for="aside-subject">Subject:</label>
        <input class="form1" id="aside-subject" name="subject" placeholder="Please input the project name" type="text"/>
      </div>
      <div class="long-input">
        <label class="label" for="aside-content">Your Request:</label>
        <textarea class="form2" id="aside-content" name="body" placeholder="Please tell us the following information: 
Grade (such as Monel 400, Inconel 600, Incoloy 800, Hastelloy C-276, etc.); 
Product form (Pipe, Bar, Sheet, Plate, Wire or Others); 
Size &amp; Quantity."></textarea>
      </div>
      <div id="aside-submit">
        <input id="submit2" name="submit" type="submit" value="Submit"/>
        <p id="errorMessage2"> </p>
      </div>
    </form>
    <ul id="floatinformation">
      <li id="email"><img alt="email TrueGrade Metals" class="contactslogo" itemprop="image" src="../image/emaillogo-2.svg" loading="lazy"/><div class="contact-div">E-mail: <a href="mailto:info@truegrademetals.com">info@truegrademetals.com</a></div><div class="copy-button"></div><div class="copy-text">✔ E-mail has been Copied</div></li>
      <li id="tel"><img alt="telephone of TrueGrade Metals" class="contactslogo" itemprop="image" src="../image/tellogo.svg" loading="lazy"/><div class="contact-div">Tel: +1 (555) 000-0000</div></li>
      <li id="fax"><img alt="fax TrueGrade Metals" class="contactslogo" itemprop="image" src="../image/faxlogo.svg" loading="lazy"/><div class="contact-div">Fax: +1 (555) 000-0001</div></li>
    </ul>
    <div id="float-back"></div>
  </div>
</aside>
<aside id="input-copy">
  <label for="copy-input">Our E-mail</label>
  <input id="copy-input" type="text" value="info@truegrademetals.com"/>
</aside>
<aside id="tariff">
  <div id="tariff-head">
    <img alt="American Flag" src="../image/countries/US.svg" loading="lazy"/>
    <p>To All U.S. Customers:</p>
  </div>
  <div id="tariff-body">
    <p>To celebrate the return of normal trade between China and the United States, we have prepared a <b class="click-event"><u>2.5% Discount</u></b> for all U.S. customers (valid for one month). If you have any inquiries, please don't hesitate to <b class="click-event"><u>Contact Us</u></b>.</p>
  </div>
</aside>

<!-- Global Footer -->
<div id="global-footer"></div>
<script src="/tgm/components/global-footer.js"></script>
<script src="/tgm/tgm-core.js"></script>
<script src="/tgm/product-enterprise.js"></script>
</body>
</html>"""


def collect_unmatched_sections(soup):
    """Preserve any sections not explicitly handled."""
    handled_ids = {
        "main-page", "description-catalogue-1", "specifications-features-1",
        "grades-page", "process-formula-1", "technical-sheet-1",
        "mechanical-properties-1", "equivalent-grades-1", "quality-inspection-1",
        "package-logistics-1", "faq", "popular-products", "related-products-1",
        "related-products"
    }
    out = []
    main = soup.find("main")
    if main:
        for child in main.find_all("section", recursive=False):
            sid = child.get("id", "")
            if sid not in handled_ids:
                out.append(str(child))
    return "\n".join(out)


def convert_product(path, log_file):
    try:
        html = path.read_text(encoding="utf-8")
    except Exception as e:
        log_file.write(f"READ_ERROR {path.name}: {e}\n")
        return False

    soup = BeautifulSoup(html, "lxml")
    slug = path.name
    canonical = f"https://www.truegrademetals.com/tgm/products/{slug}"

    head = build_head(soup, slug, canonical)
    hero, product_name, main_photo_html, thumb_photo_html = build_hero(soup)

    parts = [
        head,
        hero,
        build_quick_spec(soup),
        build_gallery(main_photo_html, thumb_photo_html, product_name),
        build_overview(soup),
        build_benefits(soup),
        build_applications(soup),
        build_grades_section(soup),
        build_technical_sheet(soup),
        build_process(soup),
        build_standards(soup),
        build_quality(soup),
        build_downloads(soup),
        build_package_logistics(soup),
        build_faq(soup),
        build_related_products(soup),
        build_resources(),
        build_rfq(product_name),
        build_final_cta(product_name),
    ]

    unmatched = collect_unmatched_sections(soup)
    if unmatched:
        parts.append(f"<!-- Preserved additional sections -->\n{unmatched}")

    parts.append(build_footer())

    output = "\n".join(p for p in parts if p)
    path.write_text(output, encoding="utf-8")
    log_file.write(f"OK {path.name}\n")
    return True


def main():
    files = sorted(PRODUCTS_DIR.glob("*.html"))

    ok = 0
    failed = []
    with LOG_PATH.open("w", encoding="utf-8") as log:
        log.write(f"Processing {len(files)} product pages\n")
        for path in files:
            if convert_product(path, log):
                ok += 1
            else:
                failed.append(path.name)

    print(f"Done. Converted {ok}/{len(files)} product pages.")
    if failed:
        print(f"Failed ({len(failed)}):", failed[:10])


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        # Run on a representative sample of 10 products
        sample_names = [
            "nickel-alloy-elbow.html",
            "nickel-alloy-round-bar-rod.html",
            "nickel-alloy-sheet.html",
            "nickel-alloy-wire.html",
            "monel-400-nickel-alloy-seamless-pipe-tube.html",
            "inconel-625-nickel-alloy-plate.html",
            "hastelloy-C-276-nickel-alloy-wire.html",
            "incoloy-825-nickel-alloy-reducer.html",
            "nickel-alloy-capillary-tube.html",
            "nickel-alloy-coil.html",
        ]
        files = [PRODUCTS_DIR / n for n in sample_names if (PRODUCTS_DIR / n).exists()]
        ok = 0
        failed = []
        with LOG_PATH.open("w", encoding="utf-8") as log:
            log.write(f"SAMPLE MODE: Processing {len(files)} product pages\n")
            for path in files:
                if convert_product(path, log):
                    ok += 1
                else:
                    failed.append(path.name)
        print(f"Sample done. Converted {ok}/{len(files)} product pages.")
        if failed:
            print("Failed:", failed)
    else:
        main()
