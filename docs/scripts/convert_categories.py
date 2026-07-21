#!/usr/bin/env python3
"""
convert_categories.py
Apply the enterprise category template to the 5 remaining legacy category pages.
Reference implementation: tgm/nickel-alloy-pipes.html
"""
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

BASE = Path("C:/Users/WIN10/STEELCHINA/docs/tgm")
SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "category_config.json"

TARGETS = [
    "nickel-alloy.html",
    "nickel-alloy-fittings.html",
    "nickel-alloy-bars.html",
    "nickel-alloy-sheets.html",
    "nickel-alloy-wires.html",
]

TRUST_PILL_SVG = {
    "cert": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>',
    "size": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "quality": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><path d="M21 12c0 4.97-4.03 9-9 9s-9-4.03-9-9 4.03-9 9-9 9 4.03 9 9z"/></svg>',
    "delivery": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
}


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


def get_section_html(soup, section_id):
    sec = soup.find("section", id=section_id)
    if not sec:
        return ""
    # unwrap section, return inner content
    return "".join(str(c) for c in sec.contents)


def build_head(soup, slug, cfg, generic, canonical):
    title = extract_title(soup) or f"China Nickel Alloy {cfg['category_name']} Supplier & Manufacturer -- TrueGrade Metals"
    keywords = extract_meta(soup, "keywords") or "Nickel Alloy"
    description = extract_meta(soup, "description") or generic["applications"]["intro"]
    og_title = extract_meta(soup, prop="og:title") or title
    og_desc = extract_meta(soup, prop="og:description") or description
    og_image = extract_meta(soup, prop="og:image") or "https://www.truegrademetals.com/tgm/image/products/seamless-pipe-tube/main-photo-1.jpg"
    og_url = extract_meta(soup, prop="og:url") or canonical

    # Preserve existing JSON-LD or generate fallback
    scripts = soup.find_all("script", type="application/ld+json")
    schema_blocks = []
    for s in scripts:
        txt = s.get_text(strip=True)
        if txt:
            schema_blocks.append(txt)
    if not schema_blocks:
        schema_blocks.append(json.dumps({
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Organization",
                    "@id": "https://www.truegrademetals.com/",
                    "name": "TrueGrade Metals",
                    "url": "https://www.truegrademetals.com/",
                    "brand": {"@type": "Brand", "name": "TrueGrade Metals"},
                    "logo": "https://www.truegrademetals.com/tgm/LOGO.svg",
                    "description": "Leading Nickel Alloy / Superalloy (Monel, Inconel, Incoloy & Hastelloy) Supplier in China",
                    "email": "info@truegrademetals.com",
                    "telephone": "+1 (555) 000-0000",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": "TrueGrade Metals HQ, Industrial District",
                        "addressLocality": "Houston",
                        "addressRegion": "TX",
                        "postalCode": "77001",
                        "addressCountry": "US"
                    },
                    "sameAs": ["https://www.truegrademetals.com"]
                },
                {
                    "@type": "WebSite",
                    "@id": "https://www.truegrademetals.com/",
                    "url": "https://www.truegrademetals.com/",
                    "name": "TrueGrade Metals",
                    "publisher": {"@id": "https://www.truegrademetals.com/"}
                },
                {
                    "@type": "WebPage",
                    "@id": canonical,
                    "url": canonical,
                    "name": title,
                    "description": description,
                    "inLanguage": "en",
                    "isPartOf": {"@id": "https://www.truegrademetals.com/"}
                }
            ]
        }, ensure_ascii=False))

    schemas = "\n".join(f'<script type="application/ld+json">\n{b}\n</script>' for b in schema_blocks)

    head = f"""<!DOCTYPE HTML>
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
<link href="favicon.ico" rel="shortcut icon"/>
<link href="favicon.ico" rel="Bookmark"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&amp;family=Inter:wght@300;400;500;600;700&amp;family=Space+Grotesk:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="/tgm/components/tgm-tokens.css" rel="stylesheet"/>
<link href="category-enterprise.css" rel="stylesheet"/>
<link href="/tgm/components/tgm-tables-graphs.css" rel="stylesheet"/>
<link href="chemical-all.css" rel="stylesheet"/>
{schemas}
</head>"""
    return head


def build_hero(soup, cfg):
    category_name = cfg["category_name"]
    eyebrow = cfg.get("eyebrow", "Nickel Alloy")
    value_prop = cfg.get("value_prop", f"TrueGrade Metals supplies a full range of nickel alloy {category_name.lower()}.")

    # Try to preserve breadcrumb from legacy
    breadcrumb = ""
    bread = soup.find("ol", id="breadol")
    if bread:
        breadcrumb = str(bread)
    else:
        breadcrumb = f"""<ol id="breadol">
        <li><a href="../index.html"><b>TrueGrade Metals</b></a></li>
        <li><a href="nickel-alloy.html"><b>PRODUCTS</b></a></li>
        <li>{category_name}</li>
        </ol>"""

    hero = f"""<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-M2WGSR9" style="display:none;visibility:hidden" width="0"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<!-- Global Navigation -->
<div id="global-nav" style="min-height:122px"></div>
<script src="/tgm/components/global-nav.js"></script>

<main id="main-content">
  <!-- HERO -->
  <section id="main-page">
    <div id="title-bread">
      {breadcrumb}
      <h1><span>{eyebrow}</span> <br/>{category_name}</h1>
    </div>
    <div id="detail-description">
      <p>{value_prop}</p>
      <div class="grade-point">
        <a class="monel-point" href="grades/monel.html">MONEL</a>
        <a class="inconel-point" href="grades/inconel.html">INCONEL</a>
        <a class="incoloy-point" href="grades/incoloy.html">INCOLOY</a>
        <a class="hastelloy-point" href="grades/hastelloy.html">HASTELLOY</a>
      </div>
    </div>
    <div class="cat-hero-trust" aria-label="Sourcing confidence">
      <span class="cat-hero-trust-item">{TRUST_PILL_SVG['cert']} MTC included</span>
      <span class="cat-hero-trust-item">{TRUST_PILL_SVG['size']} Full traceability</span>
      <span class="cat-hero-trust-item">{TRUST_PILL_SVG['delivery']} Global shipping</span>
      <span class="cat-hero-trust-item">{TRUST_PILL_SVG['quality']} Engineering support</span>
    </div>
    <div class="cat-hero-cta">
      <button class="click-event" id="contactbutton" type="button">
        <img alt="Get a quote" src="image/emaillogo.svg"/>
        <p>Get a Free Quote NOW</p>
      </button>
      <a class="cat-hero-secondary" href="contact-us.html">Speak to an engineer</a>
    </div>
  </section>"""
    return hero


def build_introduction(cfg, generic):
    overview = cfg.get("overview", "")
    cards = generic["authority_cards"]
    cards_html = "\n".join(
        f"""<article class="cat-authority-card">
        <div class="cat-authority-icon" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg></div>
        <h3>{c['title']}</h3>
        <p>{c['desc']}</p>
      </article>"""
        for c in cards
    )
    return f"""<!-- INTRODUCTION -->
  <section id="cat-introduction" aria-labelledby="cat-intro-heading">
    <div class="cat-section-head">
      <h2 id="cat-intro-heading"><span>Overview</span>{cfg['category_name']}</h2>
      <p>{overview}</p>
    </div>
    <div class="cat-authority-grid">
      {cards_html}
    </div>
    <div class="cat-section-cta">
      <button class="cat-btn click-event" type="button">Request a quote</button>
      <a class="cat-btn-ghost" href="grades.html">Explore grades</a>
    </div>
  </section>"""


def build_product_forms(soup):
    content = get_section_html(soup, "choose-page")
    if not content:
        return ""
    return f"""<!-- PRODUCT FORMS -->
  <section id="choose-page">
    {content}
  </section>"""


def build_trust_band(generic):
    t = generic["trust_band"]
    return f"""<!-- TRUST BAND -->
  <section id="cat-trust-band" aria-label="Sourcing confidence">
    <div class="cat-trust-inner">
      <div class="cat-trust-item">
        <div class="cat-trust-icon" aria-hidden="true">{TRUST_PILL_SVG['cert']}</div>
        <div><h4>{t['title1']}</h4><p>{t['desc1']}</p></div>
      </div>
      <div class="cat-trust-item">
        <div class="cat-trust-icon" aria-hidden="true">{TRUST_PILL_SVG['size']}</div>
        <div><h4>{t['title2']}</h4><p>{t['desc2']}</p></div>
      </div>
      <div class="cat-trust-item">
        <div class="cat-trust-icon" aria-hidden="true">{TRUST_PILL_SVG['quality']}</div>
        <div><h4>{t['title3']}</h4><p>{t['desc3']}</p></div>
      </div>
      <div class="cat-trust-item">
        <div class="cat-trust-icon" aria-hidden="true">{TRUST_PILL_SVG['delivery']}</div>
        <div><h4>{t['title4']}</h4><p>{t['desc4']}</p></div>
      </div>
    </div>
  </section>
  <div class="cat-section-cta cat-contained">
    <button class="cat-btn click-event" type="button">Request quote for this product form</button>
    <a class="cat-btn-ghost" href="contact-us.html">Speak to an engineer</a>
  </div>"""


def build_grades(soup):
    content = get_section_html(soup, "grades-page")
    if not content:
        return ""
    # Wrap in template's grades section structure, keeping inner content
    return f"""<!-- GRADES AVAILABLE -->
  <section id="grades-page">
    <div class="cat-section-head">
      <h2><span>Grades Available</span>Material overview</h2>
      <p>Browse the Monel, Inconel, Incoloy and Hastelloy grades available in this product category.</p>
    </div>
    {content}
    <div class="cat-section-cta">
      <a class="cat-btn" href="grades.html">View all grades</a>
      <button class="cat-btn-ghost click-event" type="button">Ask about grade selection</button>
    </div>
  </section>"""


def build_applications(cfg, generic):
    if cfg.get("hide_applications"):
        return ""
    app = generic["applications"]
    cards = "\n".join(
        f"""<a class="cat-info-card" href="{c['href']}">
        <div class="cat-info-icon" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg></div>
        <h3>{c['title']}</h3>
        <p>{c['desc']}</p>
        <span class="cat-info-link">Browse applications →</span>
      </a>"""
        for c in app["cards"]
    )
    return f"""<!-- APPLICATIONS -->
  <section id="cat-applications" aria-labelledby="cat-app-heading">
    <div class="cat-section-head">
      <h2 id="cat-app-heading"><span>Applications</span>{app['heading']}</h2>
      <p>{app['intro']}</p>
    </div>
    <div class="cat-card-grid cat-card-grid-3">
      {cards}
    </div>
    <div class="cat-section-cta">
      <button class="cat-btn click-event" type="button">Discuss your application</button>
      <a class="cat-btn-ghost" href="media/applications/index.html">All applications</a>
    </div>
  </section>"""


def build_industries(cfg, generic):
    if cfg.get("hide_industries"):
        return ""
    ind = generic["industries"]
    cards = "\n".join(
        f"""<a class="cat-industry-card" href="solutions/{c['slug']}.html">
        <img loading="lazy" src="image/solutions/{c['slug']}.jpg" alt="{c['name']}"/>
        <span>{c['name']}</span>
      </a>"""
        for c in ind["cards"]
    )
    return f"""<!-- INDUSTRY CARDS -->
  <section id="cat-industries" aria-labelledby="cat-ind-heading">
    <div class="cat-section-head">
      <h2 id="cat-ind-heading"><span>Industries</span>{ind['heading']}</h2>
      <p>{ind['intro']}</p>
    </div>
    <div class="cat-card-grid cat-card-grid-3">
      {cards}
    </div>
    <div class="cat-section-cta">
      <a class="cat-btn" href="solutions.html">View all industries</a>
    </div>
  </section>"""


def build_resources(cfg, generic):
    if cfg.get("hide_resources"):
        return ""
    res = generic["resources"]
    cards = "\n".join(
        f"""<a class="cat-resource-card" href="{c['href']}">
        <div class="cat-resource-icon" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg></div>
        <h3>{c['title']}</h3>
        <p>{c['desc']}</p>
      </a>"""
        for c in res["cards"]
    )
    return f"""<!-- TECHNICAL RESOURCES -->
  <section id="cat-resources" aria-labelledby="cat-res-heading">
    <div class="cat-section-head">
      <h2 id="cat-res-heading"><span>Tools &amp; Resources</span>{res['heading']}</h2>
      <p>{res['intro']}</p>
    </div>
    <div class="cat-card-grid cat-card-grid-3">
      {cards}
    </div>
    <div class="cat-section-cta">
      <button class="cat-btn click-event" type="button">Get technical help</button>
      <a class="cat-btn-ghost" href="tools.html">All tools</a>
    </div>
  </section>"""


def build_quick_links(cfg):
    links = cfg.get("quick_links", [])
    if not links:
        return ""
    links_html = "\n".join(f'<a href="{l["href"]}">{l["text"]}</a>' for l in links)
    return f"""<!-- QUICK LINKS -->
  <section id="cat-quick-links" aria-label="Related links">
    <div class="cat-quick-links-inner">
      <span>Quick links:</span>
      {links_html}
    </div>
  </section>"""


def build_faq(generic):
    faq = generic["faq"]
    items = "\n".join(
        f"""<details class="cat-faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <summary itemprop="name">{i['q']}</summary>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">{i['a']}</p>
        </div>
      </details>"""
        for i in faq["items"]
    )
    return f"""<!-- FAQ -->
  <section id="cat-faq" aria-labelledby="cat-faq-heading">
    <div class="cat-section-head">
      <h2 id="cat-faq-heading"><span>FAQ</span>{faq['heading']}</h2>
      <p>{faq['intro']}</p>
    </div>
    <div class="cat-faq-list" itemscope itemtype="https://schema.org/FAQPage">
      {items}
    </div>
    <div class="cat-section-cta">
      <button class="cat-btn click-event" type="button">Ask a question</button>
      <a class="cat-btn-ghost" href="contact-us.html">Contact us</a>
    </div>
  </section>"""


def build_gallery(soup, cfg):
    content = get_section_html(soup, "gallery-page")
    if not content:
        return ""
    return f"""<!-- GALLERY -->
  <section id="gallery-page">
    <div class="cat-section-head">
      <h2><span>Gallery</span>{cfg.get('gallery_heading', 'Gallery')}</h2>
      <p>{cfg.get('gallery_intro', '')}</p>
    </div>
    <div id="gallery-page-2">
      {content}
    </div>
  </section>"""


def build_related_categories(soup, cfg):
    content = get_section_html(soup, "products-page")
    if not content:
        return ""
    return f"""<!-- RELATED CATEGORIES -->
  <section class="products-page-1" id="products-page">
    <div class="cat-section-head">
      <h2 class="products-h2"><span>Related categories</span>Explore related products</h2>
      <p>{cfg.get('related_intro', '')}</p>
    </div>
    <div id="card-frame">
      {content}
    </div>
    <div class="cat-section-cta">
      <button class="cat-btn click-event" type="button">Request a project quote</button>
      <a class="cat-btn-ghost" href="nickel-alloy.html">All nickel alloy products</a>
    </div>
  </section>"""


def build_footer():
    return """</main>

<!-- FLOAT QUOTE FORM -->
<aside id="float-form" itemscope="" itemtype="https://schema.org/WPSideBar">
  <div class="click-event" id="floatbutton">
    <img alt="press and contact us" id="floatlogo" src="image/emaillogo.svg"/>
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
        <p id="errorMessage2">&emsp;</p>
      </div>
    </form>
    <ul id="floatinformation">
      <li id="email">
        <img alt="email TrueGrade Metals" class="contactslogo" itemprop="image" src="image/emaillogo-2.svg"/>
        <div class="contact-div">E-mail: <a href="mailto:info@truegrademetals.com">info@truegrademetals.com</a></div>
        <div class="copy-button"></div>
        <div class="copy-text">✔ E-mail has been Copied</div>
      </li>
      <li id="tel">
        <img alt="telephone of TrueGrade Metals" class="contactslogo" itemprop="image" src="image/tellogo.svg"/>
        <div class="contact-div">Tel: +1 (555) 000-0000</div>
      </li>
      <li id="fax">
        <img alt="fax TrueGrade Metals" class="contactslogo" itemprop="image" src="image/faxlogo.svg"/>
        <div class="contact-div">Fax: +1 (555) 000-0001</div>
      </li>
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
    <img alt="American Flag" src="image/countries/US.svg"/>
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
<script src="category-enterprise.js"></script>
</body>
</html>"""


def convert_category(slug, cfg, generic):
    path = BASE / slug
    if not path.exists():
        print(f"SKIP: {slug} not found")
        return False

    html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")

    canonical = f"https://www.truegrademetals.com/tgm/{slug}"

    parts = [
        build_head(soup, slug, cfg, generic, canonical),
        build_hero(soup, cfg),
        build_introduction(cfg, generic),
        build_product_forms(soup),
        build_trust_band(generic),
        build_grades(soup),
        build_applications(cfg, generic),
        build_industries(cfg, generic),
        build_resources(cfg, generic),
        build_quick_links(cfg),
        build_faq(generic),
        build_gallery(soup, cfg),
        build_related_categories(soup, cfg),
        build_footer(),
    ]

    output = "\n".join(p for p in parts if p)
    path.write_text(output, encoding="utf-8")
    print(f"Converted {slug}")
    return True


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    generic = config["generic"]
    categories = config["categories"]

    converted = 0
    skipped = []
    for slug in TARGETS:
        cfg = categories.get(slug, {})
        if convert_category(slug, cfg, generic):
            converted += 1
        else:
            skipped.append(slug)

    print(f"\nDone. Converted {converted}/{len(TARGETS)} category pages.")
    if skipped:
        print("Skipped:", skipped)


if __name__ == "__main__":
    main()
