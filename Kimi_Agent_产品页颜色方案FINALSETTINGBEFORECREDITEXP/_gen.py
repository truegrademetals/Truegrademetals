#!/usr/bin/env python3
"""TrueGrade Metals — static page generator.
Renders all product-form, grade×form, industry and blog pages from one template
so nav, footer, schema and conversion elements stay consistent everywhere.
"""
import json, html, os

OUT = '/mnt/agents/output/app'
BASE = 'https://www.truegrademetals.com'

E = html.escape

# ─────────────────────────── shared chrome ───────────────────────────
def head(page_title, description, canonical, schema, extra_css=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{E(page_title)}</title>
<meta name="description" content="{E(description)}">
<meta name="robots" content="index, follow">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="canonical" href="{BASE}/{canonical}">
<meta name="theme-color" content="#0F1E2C">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(page_title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:url" content="{BASE}/{canonical}">
<meta property="og:image" content="{BASE}/assets/og-image.jpg">
<meta property="og:site_name" content="TrueGrade Metals">
<script>document.documentElement.classList.add('js')</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
<script type="application/ld+json">
{schema}
</script>
<style>
{PAGE_CSS}
{extra_css}
</style>
</head>
<body>'''

UTILITY = '''<div class="utility-bar">
  <div class="utility-inner">
    <div class="utility-group">
      <span class="utility-pill"><i></i> ISO 9001 · EN 9100 certified</span>
      <span>EN 10204 3.1 MTC · 30+ years</span>
    </div>
    <div class="utility-group">
      <a href="mailto:info@truegrademetals.com">info@truegrademetals.com</a>
      <span>+86-519-81809659</span>
    </div>
  </div>
</div>'''

def header(active='products'):
    links = [('index.html','Home','home'),('categories.html','Products','products'),
             ('index.html#grades','Grades','grades'),('tools.html','Tools','tools'),
             ('industries.html','Industries','industries'),('blog.html','Blog','blog'),
             ('about.html','About','about')]
    nav = '\n      '.join(f'<a href="{u}"{' class="active"' if k==active else ''}>{t}</a>' for u,t,k in links)
    return f'''<header class="header" id="header">
  <div class="header-inner">
    <a href="index.html" class="logo">
      <span class="logo-mark">TG</span>
      <span class="logo-text"><span class="logo-name">TrueGrade Metals</span><span class="logo-tag">Nickel Alloy Specialists</span></span>
    </a>
    <nav class="nav">
      {nav}
    </nav>
    <div class="header-actions">
      <a href="index.html#rfq" class="btn btn-primary"><span class="long">Request Quote — </span>24h ↗</a>
    </div>
  </div>
</header>'''

def breadcrumb(items):
    parts = ' / '.join(f'<a href="{u}">{E(t)}</a>' if u else f'<span>{E(t)}</span>' for t,u in items)
    return f'<div class="container breadcrumb">{parts}</div>'

def footer():
    return '''<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo"><span class="logo-mark">TG</span><span class="logo-text"><span class="logo-name" style="color:#fff">TrueGrade Metals</span><span class="logo-tag">Nickel Alloy Specialists</span></span></a>
        <p>A professional supplier of nickel alloys and superalloys to industrial buyers worldwide — strict quality systems, full material traceability and responsive engineering support.</p>
      </div>
      <div><h4>Products</h4><a href="product.html">Seamless Pipe &amp; Tube</a><a href="welded-pipe.html">Welded Pipe &amp; Tube</a><a href="fittings.html">Fittings &amp; Flanges</a><a href="bars.html">Bars &amp; Rods</a><a href="sheets.html">Sheets &amp; Plates</a><a href="wires.html">Wires &amp; Electrodes</a></div>
      <div><h4>Resources</h4><a href="tools.html">Pipe Schedule Tool</a><a href="tools.html#compare">Grade Comparison</a><a href="blog.html">Engineering Blog</a><a href="categories.html#matrix">Availability Matrix</a><a href="assets/grade-selection-guide.pdf">Grade Selection Guide (PDF)</a></div>
      <div><h4>Company</h4><a href="about.html">About us</a><a href="about.html#contact">Contact</a><a href="mailto:info@truegrademetals.com">info@truegrademetals.com</a><a href="tel:+8651981809659">+86-519-81809659</a><a href="https://wa.me/8651981809659" target="_blank" rel="noopener">WhatsApp</a></div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 TrueGrade Metals · Changzhou, Jiangsu, China · Quote response within 24 hours</span>
      <span>ISO 9001 · ISO 14001 · ISO 45001 · EN 9100 · PED 2014/68/EU</span>
    </div>
  </div>
</footer>'''

STICKY = '''<div class="sticky-bar" id="stickyBar">
  <div class="sticky-bar-inner">
    <div class="sticky-bar-text"><strong>Sourcing nickel alloy for this project?</strong><span>Quotation in under 24 h · MTC EN 10204 3.1 · FOB / CFR / CIF / DAP</span></div>
    <div class="sticky-bar-actions">
      <a href="index.html#rfq" class="btn btn-primary">Request 24h Quote →</a>
      <button class="sticky-bar-close" id="stickyClose" aria-label="Close">✕</button>
    </div>
  </div>
</div>'''

SCRIPTS = '''<script src="assets/site.js"></script>
<script src="assets/leadgen.js"></script>'''

LEAD_BLOCK = '''<section class="section" style="padding-top:0">
  <div class="container"><div class="reveal" data-leadform></div></div>
</section>'''

def cta_band(title, sub):
    return f'''<section class="section section-dark" style="text-align:center">
  <div class="container reveal">
    <div class="eyebrow" style="justify-content:center">Get your price</div>
    <h2 style="font-size:clamp(1.9rem,4vw,2.8rem);margin-bottom:14px">{title}</h2>
    <p style="max-width:620px;margin:0 auto 26px;font-size:1.02rem">{sub}</p>
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:12px">
      <a href="index.html#rfq" class="btn btn-primary btn-lg">Request 24h quote →</a>
      <a href="mailto:info@truegrademetals.com" class="btn btn-ghost-light btn-lg">info@truegrademetals.com</a>
    </div>
  </div>
</section>'''

# shared page CSS (scoped per generated page)
PAGE_CSS = '''
.p-hero{padding:48px 0 60px;background:linear-gradient(180deg,#fff 0%,var(--bg) 100%)}
.p-hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
@media(max-width:1000px){.p-hero-grid{grid-template-columns:1fr}}
.p-hero h1{font-size:clamp(2.1rem,4.4vw,3.2rem);line-height:1.07;margin:0 0 18px}
.p-hero h1 em{font-style:normal;color:var(--accent)}
.p-hero-sub{font-size:1.08rem;line-height:1.7;margin:0 0 26px;max-width:560px}
.p-hero-sub strong{color:var(--ink)}
.p-hero-actions{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:22px}
.p-hero-trustpills{display:flex;flex-wrap:wrap;gap:8px}
.hero-photo{border-radius:16px;overflow:hidden;box-shadow:var(--shadow-lg);border:1px solid var(--border);position:relative}
.hero-photo img{width:100%;height:320px;object-fit:cover;display:block}
.hero-photo-badge{position:absolute;left:16px;bottom:16px;background:rgba(255,255,255,.96);border:1px solid var(--border);border-radius:12px;box-shadow:var(--shadow);padding:10px 15px;display:flex;align-items:center;gap:10px}
.spec-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:34px;padding-top:26px;border-top:1px solid var(--border)}
@media(max-width:800px){.spec-grid{grid-template-columns:repeat(2,1fr)}}
.spec strong{display:block;font-family:var(--font-head);font-size:1.3rem;color:var(--ink);line-height:1.1;margin-bottom:4px}
.spec strong i{font-style:normal;color:var(--accent)}
.spec > span{font-size:.78rem;color:var(--muted);line-height:1.35;display:block}
.std-chips{display:flex;flex-wrap:wrap;gap:8px}
.std-chips span{font-family:var(--font-mono);font-size:.72rem;font-weight:500;color:var(--ink);background:#fff;border:1px solid var(--border);padding:6px 12px;border-radius:var(--pill)}
.sub-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:1000px){.sub-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){.sub-grid{grid-template-columns:1fr}}
.sub-card{padding:24px;display:flex;flex-direction:column;gap:8px}
.sub-card h3{font-size:1.08rem}
.sub-card p{font-size:.86rem;margin:0;line-height:1.55;flex:1;color:var(--body)}
.sub-card a{font-size:.86rem;font-weight:600;color:var(--accent)}
.grade-chips{display:flex;flex-wrap:wrap;gap:8px}
.grade-chips a{font-size:.8rem;font-weight:600;color:var(--ink);background:#fff;border:1px solid var(--border);padding:7px 14px;border-radius:var(--pill);transition:all .2s}
.grade-chips a:hover{border-color:var(--accent);color:var(--accent);background:var(--tint)}
.feat-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:800px){.feat-list{grid-template-columns:1fr}}
.feat-list li{display:flex;gap:10px;background:#fff;border:1px solid var(--border);border-radius:var(--radius-sm);padding:14px 16px;font-size:.88rem;line-height:1.5;color:var(--body)}
.feat-list li svg{color:var(--green);flex-shrink:0;margin-top:2px}
.feat-list strong{color:var(--ink)}
.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
@media(max-width:800px){.gallery-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:520px){.gallery-grid{grid-template-columns:1fr}}
.gallery-grid a{border-radius:var(--radius);overflow:hidden;border:1px solid var(--border);display:block}
.gallery-grid img{width:100%;height:220px;object-fit:cover;display:block;transition:transform .4s ease}
.gallery-grid a:hover img{transform:scale(1.04)}
.app-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:900px){.app-grid{grid-template-columns:1fr}}
.app-card{padding:24px}
.app-card h3{font-size:1.02rem;margin-bottom:8px}
.app-card p{font-size:.86rem;margin:0;line-height:1.55}
.table-scroll{overflow-x:auto;border-radius:var(--radius);border:1px solid var(--border);background:#fff}
.data-table{width:100%;border-collapse:collapse;font-size:.84rem;min-width:640px}
.data-table thead{background:var(--ink);color:#fff}
.data-table th{padding:12px 14px;text-align:left;font-family:var(--font-head);font-weight:600;font-size:.72rem;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap}
.data-table td{padding:10px 14px;border-bottom:1px solid var(--border);color:var(--body);font-variant-numeric:tabular-nums}
.data-table tbody tr:nth-child(even){background:var(--bg)}
.data-table td:first-child{font-weight:600;color:var(--ink)}
.blog-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
@media(max-width:1000px){.blog-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){.blog-grid{grid-template-columns:1fr}}
.blog-card{overflow:hidden;display:flex;flex-direction:column}
.blog-card img{width:100%;height:190px;object-fit:cover;display:block}
.blog-card-body{padding:22px;display:flex;flex-direction:column;gap:8px;flex:1}
.blog-card-cat{font-family:var(--font-mono);font-size:.64rem;text-transform:uppercase;letter-spacing:.1em;color:var(--accent);font-weight:600}
.blog-card h3{font-size:1.05rem;line-height:1.3}
.blog-card p{font-size:.85rem;margin:0;line-height:1.55;flex:1}
.blog-card-meta{font-size:.76rem;color:var(--muted)}
.article-body{max-width:760px}
.article-body h2{font-size:1.6rem;margin:34px 0 14px}
.article-body h3{font-size:1.2rem;margin:26px 0 10px}
.article-body p{font-size:1rem;line-height:1.8;margin:0 0 16px;color:var(--body)}
.article-body ul{margin:0 0 16px;padding-left:22px;line-height:1.8;color:var(--body)}
.article-body li{margin-bottom:6px}
.article-hero{border-radius:var(--radius);overflow:hidden;border:1px solid var(--border);margin:26px 0}
.article-hero img{width:100%;height:340px;object-fit:cover;display:block}
.callout{background:var(--tint);border:1px solid var(--tint-2);border-radius:var(--radius-sm);padding:18px 20px;margin:22px 0;font-size:.92rem;line-height:1.6}
.callout strong{color:var(--accent-dark)}
'''

def write(fname, body_html, page_title, description, schema, active='products', extra_css='', scripts_extra=''):
    html_doc = (head(page_title, description, fname, schema, extra_css)
        + '\n' + UTILITY + '\n' + header(active) + '\n' + body_html + '\n' + footer() + '\n' + STICKY
        + '\n' + SCRIPTS + scripts_extra + '\n</body>\n</html>')
    open(f'{OUT}/{fname}', 'w').write(html_doc)
    print('wrote', fname, len(html_doc))

# ─────────────────────────── data ───────────────────────────
CHECK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 12l5 5L20 6"/></svg>'

FORMS = {
 'welded-pipe': dict(
   name='Nickel Alloy Welded Pipe & Tube', short='Welded Pipe & Tube', img='prod-pipes', slug='welded-pipe.html',
   title='Nickel Alloy Welded Pipe & Tube — Cost-Efficient, Certified | TrueGrade Metals',
   desc='Welded nickel-alloy pipe & tube in Inconel, Monel, Incoloy and Hastelloy. ASTM B705/B626, 100% weld-seam NDT, EN 10204 3.1 MTC. Quote in 24 hours.',
   h1='Welded pipe with the same metallurgy — <em>at a sharper price.</em>',
   sub='For large diameters and long lengths where seamless is uneconomical: strip-formed, TIG/PLASMA welded and <strong>100% eddy-current tested</strong> nickel-alloy pipe with full EN 10204 3.1 certification.',
   standards=['ASTM B705','ASTM B775','ASTM B704','ASTM B751','ASTM B515','ASTM B619','ASTM B626'],
   subs=[('Large-OD welded pipe','OD up to 1219 mm for ducting, scrubbers and low-pressure transfer lines.'),
         ('Welded heat-exchanger tube','Long-length welded tube, annealed and 100% ET/UT tested.'),
         ('Radiographic-tested (RT) pipe','Full X-ray of the weld seam for critical service on request.')],
   features=[('Weld integrity','100% eddy-current or ultrasonic testing of every weld seam; RT on request.'),
             ('Economy','Typically 20–35% below seamless cost for large diameters and thin walls.'),
             ('Lengths','Up to 18 m welded lengths for fewer site joints.'),
             ('Same certification','EN 10204 3.1 MTC with weld-zone PMI verification included.')],
   specs=[('OD range','8 – 1219 mm'),('Wall thickness','0.5 – 20 mm'),('Lengths','up to 18 m'),('Testing','100% ET / UT · RT optional')],
   faqs=[('When should I choose welded over seamless?','Choose welded for large diameters, thin walls and long lengths at lower cost. Choose seamless for extreme pressure, temperature cycling or the most aggressive media. Our engineers will recommend honestly based on your service conditions.'),
         ('Is the weld seam as corrosion-resistant as the parent metal?','Yes when properly made: we use matching filler (e.g. ERNiCrMo-3 for 625), full solution annealing after welding, and 100% NDT of the seam. The MTC covers the welded product.'),
         ('What NDT is included as standard?','100% eddy-current testing of the weld seam is standard. Ultrasonic and full radiographic testing are available on request at quoted cost.')]),
 'fittings': dict(
   name='Nickel Alloy Fittings & Flanges', short='Fittings & Flanges', img='prod-fittings', slug='fittings.html',
   title='Nickel Alloy Fittings & Flanges — Elbows, Tees, Reducers | TrueGrade Metals',
   desc='Butt-weld fittings and flanges in Inconel, Monel, Incoloy and Hastelloy per ASTM B366/B564, matched to your pipe heats. EN 10204 3.1 MTC. Quote in 24 hours.',
   h1='Fittings matched to your pipe heats — <em>one traceable package.</em>',
   sub='Elbows, tees, reducers, caps, stub ends and flanges per <strong>ASTM B366 / B564</strong> — manufactured from the same heats as your tube or pipe so the full system ships with one MTC file.',
   standards=['ASTM B366','ASTM B564','ASTM B462','ASME B16.9','ASME B16.5','MSS SP-43'],
   subs=[('Elbows 45° / 90° / 180°','Long- and short-radius, seamless or welded construction.'),
         ('Tees & crosses','Equal and reducing, per ASME B16.9.'),
         ('Reducers','Concentric and eccentric, all schedules.'),
         ('Caps & stub ends','Matching wall thickness to your pipe schedule.'),
         ('Flanges','Weld-neck, slip-on, blind, socket-weld per ASME B16.5.'),
         ('Custom fittings','Laterals, crosses and special radii to drawing.')],
   features=[('Heat matching','Fittings from the same heat as your pipe — one MTC covers the system.'),
             ('Full forming range','Hot-formed and cold-formed with solution annealing after forming.'),
             ('Dimensional accuracy','Bevelled ends per ASME B16.25, ready to weld.'),
             ('NDT included','100% visual + PT/ET on formed areas; PMI on every piece.')],
   specs=[('Size range','DN15 – DN600'),('Schedules','SCH10 – SCH160 / XXS'),('Types','seamless & welded'),('Standards','B366 · B16.9 · B16.5')],
   faqs=[('Can fittings be supplied from the same heat as my pipe?','Yes — that is our standard practice for system orders. One EN 10204 3.1 certificate package covers pipe and fittings together.'),
         ('Do you make special-radius or custom fittings?','Yes. Laterals, crosses, special-radius elbows and reducing tees are made to drawing. Send the drawing with your inquiry and engineering confirms within 24 hours.'),
         ('Are formed fittings re-annealed?','All hot-formed and cold-formed fittings are solution annealed after forming and before final inspection, restoring full corrosion performance.')]),
 'bars': dict(
   name='Nickel Alloy Bars & Rods', short='Bars & Rods', img='prod-bars', slug='bars.html',
   title='Nickel Alloy Bars & Rods — Round, Flat, Hex, Square | TrueGrade Metals',
   desc='Round bar, flat bar, hexagon and square bar in Inconel 718/625, Monel, Incoloy and Hastelloy per ASTM B446/B574. EN 10204 3.1 MTC. Quote in 24 hours.',
   h1='Bar stock that machines <em>exactly to drawing.</em>',
   sub='Hot-rolled, forged and cold-finished nickel-alloy bar per <strong>ASTM B446 / B164 / B166 / B574</strong> — centerless-ground tolerance options and cut-to-length service for machinists.',
   standards=['ASTM B446','ASTM B164','ASTM B166','ASTM B408','ASTM B425','ASTM B574','ASTM B637'],
   subs=[('Round bar & rod','Ø 3–500 mm, hot-rolled, forged or cold-finished.'),
         ('Flat bar','Rolled and cut flats for structural and machined parts.'),
         ('Hexagon bar','Across-flats sizes for fasteners and valve components.'),
         ('Square bar','Forged and rolled squares, straightness guaranteed.'),
         ('Forged bar','Upset-forged large sections with UT testing.'),
         ('Cut discs & blanks','Sawn discs and machined blanks to your drawing.')],
   features=[('Machining tolerance','h9/h10/h11 cold-finished tolerances; centerless grinding on request.'),
             ('Full UT testing','Ultrasonic testing on forged and large-diameter bars as standard.'),
             ('Cut-to-length','Bandsaw cutting to your blank sizes — no kerf waste at your shop.'),
             ('Heat-treated states','Annealed, solution-treated or aged (718, K-500, 925) per standard.')],
   specs=[('Diameter range','Ø 3 – 500 mm'),('Conditions','hot-rolled · forged · cold-finished'),('Tolerances','h9 / h10 / h11 · ground'),('Testing','100% PMI · UT on forgings')],
   faqs=[('What tolerance can you hold on round bar?','Cold-finished bar ships at h9/h10/h11. Centerless-ground bar to h7/h8 and polished surface is available on request.'),
         ('Can you supply aged Inconel 718 bar?','Yes — 718 is supplied solution-annealed or precipitation-aged per ASTM B637 as required. The heat-treatment state is stated on the MTC.'),
         ('Do you cut bars to blank size?','Yes. Bandsaw cutting to your specified blank lengths is standard at no extra charge for reasonable quantities.')]),
 'sheets': dict(
   name='Nickel Alloy Sheets & Plates', short='Sheets & Plates', img='prod-sheets', slug='sheets.html',
   title='Nickel Alloy Sheets & Plates — Cut to Size | TrueGrade Metals',
   desc='Hot-rolled plate, cold-rolled sheet, strip and coil in Inconel, Monel, Incoloy and Hastelloy per ASTM B443/B575. Cut-to-size. EN 10204 3.1 MTC. Quote in 24 hours.',
   h1='Plate and sheet, <em>cut to your drawing.</em>',
   sub='Hot-rolled plate, cold-rolled sheet, strip and coil per <strong>ASTM B443 / B168 / B409 / B575</strong> — laser, plasma and waterjet profile cutting with certified offcut traceability.',
   standards=['ASTM B443','ASTM B168','ASTM B409','ASTM B424','ASTM B575','ASTM B162','ASTM B906'],
   subs=[('Hot-rolled plate','4–100 mm for pressure vessels and structural use.'),
         ('Cold-rolled sheet','0.3–4 mm with 2B, BA or polished finishes.'),
         ('Strip & coil','Slit strip to your width, annealed and edged.'),
         ('Cut-to-size blanks','Sheared or sawn rectangles to your nesting plan.'),
         ('Profile cutting','Laser / plasma / waterjet shapes to DXF or drawing.'),
         ('Polished finishes','No.4 brush and mirror polish for architectural or hygienic use.')],
   features=[('Flatness guaranteed','Roller-levelled plate; flatness per ASTM or tighter by agreement.'),
             ('Certified cutting','Every cut piece keeps heat-number traceability — no mixed lots.'),
             ('Surface protection','PVC film on polished and cold-rolled surfaces as standard.'),
             ('Edge conditioning','Deburred and machined edges available for welding prep.')],
   specs=[('Thickness','0.3 – 100 mm'),('Width','up to 2500 mm'),('Finishes','HR · 2B · BA · No.4 · mirror'),('Cutting','laser · plasma · waterjet')],
   faqs=[('Can you cut profiles from my DXF file?','Yes. Send DXF or PDF drawings — we nest, cut (laser, plasma or waterjet depending on thickness and edge requirement) and mark every part with its heat number.'),
         ('What finishes are available on sheet?','2B and bright-annealed (BA) as standard; No.4 brushed and mirror polish available. Polished sheet ships with PVC protection film.'),
         ('Is cut-to-size material still certified?','Yes. All blanks and profiles carry the original heat number and are covered by the same EN 10204 3.1 MTC as the parent plate.')]),
 'wires': dict(
   name='Nickel Alloy Wires & Electrodes', short='Wires & Electrodes', img='prod-wires', slug='wires.html',
   title='Nickel Alloy Wire, Filler Metal & Welding Electrodes | TrueGrade Metals',
   desc='Nickel alloy wire, wire rod, TIG/MIG filler metal and welding electrodes — ERNiCrMo-3, ENiCrMo-3 per AWS A5.14/A5.11. EN 10204 3.1 MTC. Quote in 24 hours.',
   h1='Filler metal that matches <em>your base alloy, exactly.</em>',
   sub='Drawn wire, wire rod, spooled TIG/MIG filler and coated electrodes per <strong>AWS A5.14 / A5.11</strong> — chemistry-matched to Monel, Inconel, Incoloy and Hastelloy base metals.',
   standards=['AWS A5.14','AWS A5.11','AWS A5.9','ASTM B166','ASTM B164','ASTM B574'],
   subs=[('Filler wire (TIG)','1 kg / 5 kg tubes, Ø 1.0–3.2 mm, all matching grades.'),
         ('MIG wire (spooled)','D300 spools, Ø 0.8–1.6 mm, layer-wound.'),
         ('Welding electrodes','ENiCrMo-3 and matching SMAW electrodes, vacuum packed.'),
         ('Coil & spring wire','Drawn wire for springs, mesh and cold-heading.'),
         ('Wire rod','Hot-rolled rod for redrawing and fastener stock.'),
         ('Bright & annealed wire','BA finish for weaving, braiding and precision forming.')],
   features=[('Chemistry-matched','Filler compositions matched to base alloy — no dissimilar-weld surprises.'),
             ('AWS classified','ERNiCrMo-3, ENiCrMo-3, ERNi-1, ERNiCu-7 and more in stock.'),
             ('Clean spooling','Layer-wound spools, oiled and sealed for TIG/MIG feedability.'),
             ('Traceable heats','Each spool and tube carries the heat number; MTC included.')],
   specs=[('Wire Ø','0.05 – 15 mm'),('Filler forms','TIG tubes · MIG spools · electrodes'),('Packing','vacuum sealed · spooled'),('Certification','AWS + EN 10204 3.1')],
   faqs=[('Which filler do I use for Inconel 625 welds?','ERNiCrMo-3 (TIG/MIG) or ENiCrMo-3 (SMAW) is the standard matching filler — we stock both. The same applies across grades: tell us your base metal and we confirm the matching classification.'),
         ('Do you supply small quantities of filler wire?','Yes. Filler wire sells by the kilogram with no MOQ on stocked classifications — ideal for qualification welds and repair work.'),
         ('Can you supply spring-temper wire?','Yes. Wire is drawn to your specified temper — annealed, 1/4 hard, 1/2 hard, full hard or spring temper — with tensile values stated on the MTC.')]),
}

GRADES = {
 'inconel-625': dict(name='Inconel 625', uns='UNS N06625', w='W.Nr. 2.4856', dens='8.44',
   chem='Ni ≥ 58% · Cr 20–23% · Mo 8–10% · Nb+Ta 3.15–4.15%',
   yield_='414 MPa', tensile='827 MPa', temp='982 °C',
   app='Subsea umbilicals, marine exhaust, aerospace ducting, chemical transfer — the all-round Ni-Cr-Mo-Nb alloy.'),
 'inconel-718': dict(name='Inconel 718', uns='UNS N07718', w='W.Nr. 2.4668', dens='8.19',
   chem='Ni 50–55% · Cr 17–21% · Nb+Ta 4.75–5.5% · Mo 2.8–3.3% · Ti 0.65–1.15%',
   yield_='1035 MPa', tensile='1240 MPa', temp='700 °C',
   app='Turbine discs, shafts, fasteners and high-load structures — precipitation-hardened for the highest strength in the family.'),
 'hastelloy-c276': dict(name='Hastelloy C-276', uns='UNS N10276', w='W.Nr. 2.4819', dens='8.89',
   chem='Ni bal. · Mo 15–17% · Cr 14.5–16.5% · W 3–4.5% · Fe 4–7%',
   yield_='355 MPa', tensile='790 MPa', temp='1040 °C',
   app='Flue-gas scrubbers, chemical reactors, bleach plants — the default answer for worst-case mixed corrosion.'),
 'monel-400': dict(name='Monel 400', uns='UNS N04400', w='W.Nr. 2.4360', dens='8.80',
   chem='Ni ≥ 63% · Cu 28–34% · Fe ≤ 2.5%',
   yield_='240 MPa', tensile='550 MPa', temp='480 °C',
   app='Seawater valves, pumps, propeller shafts, HF acid service — the marine veteran.'),
 'incoloy-825': dict(name='Incoloy 825', uns='UNS N08825', w='W.Nr. 2.4858', dens='8.14',
   chem='Ni 38–46% · Cr 19.5–23.5% · Mo 2.5–3.5% · Cu 1.5–3% · Ti 0.6–1.2%',
   yield_='241 MPa', tensile='586 MPa', temp='540 °C',
   app='Sulfuric and phosphoric acid plants, tank heating coils, pollution control.'),
}

GRADE_FORM_PAGES = [
 ('inconel-625','pipes'), ('inconel-625','bars'),
 ('inconel-718','bars'),
 ('hastelloy-c276','pipes'), ('hastelloy-c276','fittings'),
 ('monel-400','pipes'), ('monel-400','bars'),
 ('incoloy-825','pipes'), ('incoloy-825','sheets'),
 ('hastelloy-c276','sheets'),
]

FORM_TO_KEY = {'pipes':'welded-pipe','bars':'bars','fittings':'fittings','sheets':'sheets','wires':'wires'}

def form_schema(form):
    return json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Product Categories","item":f"{BASE}/categories.html"},
        {"@type":"ListItem","position":3,"name":form['short'],"item":f"{BASE}/{form['slug']}"}]},
      {"@type":"Product","name":form['name'],
       "description":form['desc'],
       "brand":{"@type":"Brand","name":"TrueGrade Metals"},
       "material":"Nickel Alloy (Monel, Inconel, Incoloy, Hastelloy)",
       "category":form['short'],"url":f"{BASE}/{form['slug']}",
       "image":f"{BASE}/assets/{form['img']}.jpg",
       "offers":{"@type":"Offer","availability":"https://schema.org/InStock","priceCurrency":"USD","price":"0","description":"Request quotation — response within 24 hours"}},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in form['faqs']]}
    ]}, indent=2)

def grade_page_schema(slug, g, form, title, faqs):
    return json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Product Categories","item":f"{BASE}/categories.html"},
        {"@type":"ListItem","position":3,"name":title,"item":f"{BASE}/{slug}"}]},
      {"@type":"Product","name":title,
       "description":f"{g['name']} {form['short'].lower()} supplied by TrueGrade Metals with EN 10204 3.1 MTC. {g['app']}",
       "brand":{"@type":"Brand","name":"TrueGrade Metals"},
       "material":f"{g['name']} ({g['uns']})","category":form['short'],
       "url":f"{BASE}/{slug}","image":f"{BASE}/assets/{form['img']}.jpg",
       "offers":{"@type":"Offer","availability":"https://schema.org/InStock","priceCurrency":"USD","price":"0","description":"Request quotation — response within 24 hours"}},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
    ]}, indent=2)

# ─────────────────────────── renderers ───────────────────────────
def std_chips(standards):
    return '<div class="std-chips">' + ''.join(f'<span>{E(s)}</span>' for s in standards) + '</div>'

def feature_list(features):
    lis = ''.join(f'<li>{CHECK}<span><strong>{E(t)}</strong> — {E(d)}</span></li>' for t,d in features)
    return f'<ul class="feat-list">{lis}</ul>'

def sub_grid(subs):
    cards = ''.join(f'''<div class="card sub-card reveal"><h3>{E(t)}</h3><p>{E(d)}</p>
      <a href="index.html#rfq">Get price →</a></div>''' for t,d in subs)
    return f'<div class="sub-grid">{cards}</div>'

def gallery(images, alts):
    items = ''.join(f'<a href="assets/{i}.jpg" target="_blank"><img src="assets/{i}.jpg" alt="{E(a)}" loading="lazy"></a>' for i,a in zip(images, alts))
    return f'<div class="gallery-grid reveal">{items}</div>'

def faq_block(faqs):
    items = ''.join(f'<details class="faq-item"><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q,a in faqs)
    return f'<div class="reveal" style="display:flex;flex-direction:column;gap:12px">{items}</div>'

def render_form_page(key, f):
    specs = ''.join(f'<div class="spec"><strong>{E(v)}</strong><span>{E(k)}</span></div>' for k,v in f['specs'])
    body = f'''
{breadcrumb([('Home','index.html'),('Products','categories.html'),(f['short'],None)])}
<section class="p-hero">
  <div class="container">
    <div class="p-hero-grid">
      <div class="reveal in">
        <div class="eyebrow">{E(f['short'])}</div>
        <h1>{f['h1']}</h1>
        <p class="p-hero-sub">{f['sub']}</p>
        <div class="p-hero-actions">
          <a href="index.html#rfq" class="btn btn-primary btn-lg">Get a certified quote →</a>
          <a href="assets/grade-selection-guide.pdf" class="btn btn-ghost btn-lg">↓ Grade guide (PDF)</a>
        </div>
        <div class="p-hero-trustpills">
          <span class="trust-pill"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 12l5 5L20 6"/></svg> EN 10204 3.1 MTC</span>
          <span class="trust-pill"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 12l5 5L20 6"/></svg> No MOQ on stock items</span>
          <span class="trust-pill"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 12l5 5L20 6"/></svg> 24h quote SLA</span>
        </div>
        <div class="spec-grid">{specs}</div>
      </div>
      <div class="reveal in d1">
        <div class="hero-photo">
          <img src="assets/{f['img']}.jpg" alt="{E(f['name'])} — TrueGrade Metals">
          <div class="hero-photo-badge"><span style="font-family:var(--font-mono);font-size:.7rem;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:.08em">{E(f['specs'][0][1])}</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Governing standards</div>
      <h2>Fully covered by international standards.</h2>
      <p>Every order states the standard on the PO and the MTC — no ambiguity at incoming inspection.</p>
    </div>
    <div class="reveal">{std_chips(f['standards'])}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Range</div>
      <h2>Sub-products &amp; options.</h2>
    </div>
    {sub_grid(f['subs'])}
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Why TrueGrade</div>
      <h2>What makes our {E(f['short'].lower())} different.</h2>
    </div>
    {feature_list(f['features'])}
  </div>
</section>

<section class="section" style="padding-top:64px">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Gallery</div>
      <h2>The material, up close.</h2>
    </div>
    {gallery([f['img'],'factory','qc-caliper','packing'],[f['name'],'Factory stock','QC dimensional inspection','Export packing'])}
  </div>
</section>

{LEAD_BLOCK}

<section class="section section-white">
  <div class="container" style="max-width:820px">
    <div class="section-head center reveal"><div class="eyebrow">FAQ</div><h2>Common questions.</h2></div>
    {faq_block(f['faqs'])}
  </div>
</section>

{cta_band(f'Quote {E(f["short"])} in 24 hours.', 'Send grade, dimensions, quantity and standard — a named metallurgist replies with pricing, lead time and MTC sample.')}
'''
    write(f['slug'], body, f['title'], f['desc'], form_schema(f))

def render_grade_form(gkey, fkey):
    g = GRADES[gkey]
    f = FORMS[FORM_TO_KEY[fkey]]
    slug = f'{gkey}-{fkey}.html'
    title_name = f"{g['name']} {f['short']}"
    page_title = f"{g['name']} {f['short']} ({g['uns']}) — Supplier | TrueGrade Metals"
    desc = f"{g['name']} {f['short'].lower()} supplier — {g['uns']} / {g['w']}. Yield {g['yield_']}, service to {g['temp']}. EN 10204 3.1 MTC, quote in 24 hours."
    faqs = [
      (f"What sizes of {g['name']} {f['short'].lower()} do you stock?",
       f"Standard sizes per the {f['short'].lower()} range (see table above) are stocked or on a frequent smelting schedule for {g['name']}. Non-standard dimensions are made to order — confirm with your inquiry."),
      (f"What certificate comes with {g['name']} ({g['uns']})?",
       "Every heat ships with EN 10204 3.1 MTC: ladle + product chemistry, mechanical results, dimensional data and heat number. Third-party witnessed 3.2 available on request."),
      (f"Is {g['name']} suitable for my application?",
       f"Typical service for {g['name']}: {g['app']} If your medium, temperature or pressure differs, our metallurgists verify grade selection free of charge before quoting."),
    ]
    specs = ''.join(f'<div class="spec"><strong>{E(v)}</strong><span>{E(k)}</span></div>' for k,v in
        [('UNS', g['uns'].replace('UNS ','')),('Min. yield', g['yield_']),('Min. tensile', g['tensile']),('Max service', g['temp'])])
    mech_rows = ''.join(f'<tr><td>{E(k)}</td><td>{E(v)}</td></tr>' for k,v in
        [('Density', g['dens'] + ' g/cm³'),('Min. yield strength (annealed)', g['yield_']),('Min. tensile strength (annealed)', g['tensile']),('Max service temperature', g['temp']),('Nominal chemistry', g['chem'])])
    body = f'''
{breadcrumb([('Home','index.html'),('Products','categories.html'),(f['short'],f['slug']),(g['name'],None)])}
<section class="p-hero">
  <div class="container">
    <div class="p-hero-grid">
      <div class="reveal in">
        <div class="eyebrow">{E(title_name)}</div>
        <h1>{E(g['name'])} {E(f['short'].lower())}, <em>certified and in stock.</em></h1>
        <p class="p-hero-sub"><strong>{E(g['uns'])} · {E(g['w'])}</strong> — {E(g['app'])}</p>
        <div class="p-hero-actions">
          <a href="index.html#rfq" class="btn btn-primary btn-lg">Quote {E(g['name'])} {E(f['short'].lower())} →</a>
          <a href="assets/grade-selection-guide.pdf" class="btn btn-ghost btn-lg">↓ Datasheet (PDF)</a>
        </div>
        <div class="p-hero-trustpills">
          <span class="trust-pill"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 12l5 5L20 6"/></svg> EN 10204 3.1 MTC</span>
          <span class="trust-pill"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 12l5 5L20 6"/></svg> Heat-lot flexibility</span>
        </div>
        <div class="spec-grid">{specs}</div>
      </div>
      <div class="reveal in d1">
        <div class="hero-photo">
          <img src="assets/{f['img']}.jpg" alt="{E(title_name)} — TrueGrade Metals">
          <div class="hero-photo-badge"><span style="font-family:var(--font-mono);font-size:.7rem;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:.08em">{E(g['uns'])}</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Material data</div>
      <h2>{E(g['name'])} — key properties.</h2>
      <p>Nominal published values for the annealed condition. Certified heat lots ship with actual MTC values.</p>
    </div>
    <div class="table-scroll reveal"><table class="data-table">
      <thead><tr><th>Property</th><th>Value</th></tr></thead>
      <tbody>{mech_rows}</tbody>
    </table></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Supply range</div>
      <h2>Dimensions &amp; standards.</h2>
    </div>
    <div class="sub-grid">
      <div class="card sub-card reveal"><h3>Available range</h3><p>{' · '.join(E(v) for _,v in f['specs'])}</p><a href="{f['slug']}">Full {E(f['short'].lower())} page →</a></div>
      <div class="card sub-card reveal d1"><h3>Governing standards</h3><p>{E(' · '.join(f['standards']))}</p><a href="index.html#rfq">Confirm your standard →</a></div>
      <div class="card sub-card reveal d2"><h3>Other forms in {E(g['name'])}</h3><p>Pipe, fittings, bar, sheet, wire and forgings — consolidated into one PO with matching heats.</p><a href="index.html#rfq">Send full BOM →</a></div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Why TrueGrade</div><h2>What you get on every order.</h2></div>
    {feature_list(f['features'])}
  </div>
</section>

{LEAD_BLOCK}

<section class="section section-white">
  <div class="container" style="max-width:820px">
    <div class="section-head center reveal"><div class="eyebrow">FAQ</div><h2>Common questions.</h2></div>
    {faq_block(faqs)}
  </div>
</section>

{cta_band(f'Quote {E(g["name"])} {E(f["short"].lower())} in 24 hours.', 'Dimensions, quantity, standard — that is all we need. A named metallurgist replies with pricing, lead time and MTC sample.')}
'''
    write(slug, body, page_title, desc, grade_page_schema(slug, g, f, title_name, faqs))

# ── render product pages ──
for k, f in FORMS.items():
    render_form_page(k, f)
for gkey, fkey in GRADE_FORM_PAGES:
    render_grade_form(gkey, fkey)
print('PRODUCT PAGES DONE')
