#!/usr/bin/env python3
"""Long-tail grade × form pages — programmatic expansion across all grades with data."""
import os
os.chdir('/mnt/agents/output/app')

gen = open('_gen.py').read().split("# ── render product pages ──")[0]
exec(gen)  # FORMS, render helpers, write(), schemas

grad_src = open('_gen_grades.py').read().split("for g in ALL_GRADES:")[0]
exec(grad_src)  # ALL_GRADES, FAMILIES

FORM_MAP = {'pipe':'pipes', 'fitting':'fittings', 'bar':'bars', 'sheet':'sheets', 'wire':'wires'}
FORM_KEY = {'pipes':'welded-pipe','bars':'bars','fittings':'fittings','sheets':'sheets','wires':'wires'}
FORM_NOUN = {'pipes':'pipe & tube','bars':'bar & rod','fittings':'fittings & flanges','sheets':'sheet & plate','wires':'wire & electrodes'}

def lt_schema(slug, g, f, title, faqs):
    return json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Product Categories","item":f"{BASE}/categories.html"},
        {"@type":"ListItem","position":3,"name":title,"item":f"{BASE}/{slug}"}]},
      {"@type":"Product","name":title,
       "description":f"{g['name']} {f['short'].lower()} supplied by TrueGrade Metals with EN 10204 3.1 MTC. {g['desc']}",
       "brand":{"@type":"Brand","name":"TrueGrade Metals"},
       "material":f"{g['name']} ({g['uns']})","category":f['short'],
       "url":f"{BASE}/{slug}","image":f"{BASE}/assets/{f['img']}.jpg",
       "offers":{"@type":"Offer","availability":"https://schema.org/InStock","priceCurrency":"USD","price":"0","description":"Request quotation — response within 24 hours"}},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
    ]}, indent=2)

def render_lt(g, fkey):
    f = FORMS[FORM_KEY[fkey]]
    slug = f"{g['slug']}-{fkey}.html"
    title_name = f"{g['name']} {f['short']}"
    app = '; '.join(g['apps'][:2])
    traits = ''.join(f'<li>{CHECK}<span>{E(t)}</span></li>' for t in g['traits'][:4])
    page_title = f"{g['name']} {f['short']} ({g['uns']}) — Supplier | TrueGrade Metals"
    desc = f"{g['name']} {f['short'].lower()} supplier — {g['uns']}. Yield {g['y']}, service to {g['temp']}. EN 10204 3.1 MTC, quote in 24 hours."
    faqs = [
      (f"What sizes of {g['name']} {FORM_NOUN[fkey]} do you supply?",
       f"Standard sizes per the {f['short'].lower()} range (see supply range above) are stocked or on a frequent smelting schedule for {g['name']}. Non-standard dimensions are made to order — confirm with your inquiry."),
      (f"What certificate comes with {g['name']} ({g['uns']})?",
       "Every heat ships with EN 10204 3.1 MTC: ladle + product chemistry, mechanical results, dimensional data and heat number. Third-party witnessed 3.2 available on request."),
      (f"Is {g['name']} right for my application?",
       f"Typical uses: {app}. If your medium, temperature or pressure differs, our metallurgists verify grade selection free of charge before quoting."),
    ]
    specs = ''.join(f'<div class="spec"><strong>{E(v)}</strong><span>{E(k)}</span></div>' for k,v in
        [('UNS', g['uns'].replace('UNS ','')),('Min. yield', g['y']),('Min. tensile', g['t']),('Max service', g['temp'])])
    mech_rows = ''.join(f'<tr><td>{E(k)}</td><td>{E(v)}</td></tr>' for k,v in
        [('Density', g['dens'] + ' g/cm³'),('Min. yield strength (annealed)', g['y']),('Min. tensile strength (annealed)', g['t']),('Max service temperature', g['temp']),('Nominal chemistry', g['chem'])])
    body = f'''
{breadcrumb([('Home','index.html'),('Products','categories.html'),(f['short'],f['slug']),(g['name'],None)])}
<section class="p-hero">
  <div class="container">
    <div class="p-hero-grid">
      <div class="reveal in">
        <div class="eyebrow">{E(title_name)}</div>
        <h1>{E(g['name'])} {E(FORM_NOUN[fkey])}, <em>certified and in stock.</em></h1>
        <p class="p-hero-sub"><strong>{E(g['uns'])}</strong> — {E(g['desc'])}</p>
        <div class="p-hero-actions">
          <a href="index.html#rfq" class="btn btn-primary btn-lg">Quote {E(g['name'])} {E(FORM_NOUN[fkey])} →</a>
          <a href="grade-{g['slug']}.html" class="btn btn-ghost btn-lg">Full grade data →</a>
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
    <div class="section-head reveal"><div class="eyebrow">Why this grade</div>
      <h2>What {E(g['name'])} brings to the service.</h2>
    </div>
    <ul class="feat-list">{traits}</ul>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Supply range</div>
      <h2>Dimensions &amp; standards.</h2>
    </div>
    <div class="sub-grid">
      <div class="card sub-card reveal"><h3>Available range</h3><p>{' · '.join(E(v) for _,v in f['specs'])}</p><a href="{f['slug']}">Full {E(f['short'].lower())} page →</a></div>
      <div class="card sub-card reveal d1"><h3>Governing standards</h3><p>{E(' · '.join(f['standards']))}</p><a href="index.html#rfq">Confirm your standard →</a></div>
      <div class="card sub-card reveal d2"><h3>Other forms in {E(g['name'])}</h3><p>Pipe, fittings, bar, sheet, wire and forgings — consolidated into one PO with matching heats.</p><a href="grade-{g['slug']}.html">{E(g['name'])} grade hub →</a></div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Typical applications</div><h2>Where {E(g['name'])} {E(FORM_NOUN[fkey])} goes to work.</h2></div>
    <ul class="feat-list">{''.join(f'<li>{CHECK}<span>{E(a)}</span></li>' for a in g['apps'][:4])}</ul>
  </div>
</section>

{LEAD_BLOCK}

<section class="section section-white">
  <div class="container" style="max-width:820px">
    <div class="section-head center reveal"><div class="eyebrow">FAQ</div><h2>Common questions.</h2></div>
    {faq_block(faqs)}
  </div>
</section>

{cta_band(f'Quote {E(g["name"])} {E(FORM_NOUN[fkey])} in 24 hours.', 'Dimensions, quantity, standard — that is all we need. A named metallurgist replies with pricing, lead time and MTC sample.')}
'''
    write(slug, body, page_title, desc, lt_schema(slug, g, f, title_name, faqs))
    return slug

made = []
for g in ALL_GRADES:
    if g['y'] == '—':
        continue  # only grades with verified mechanical data
    for ff in g['forms']:
        fkey = FORM_MAP.get(ff)
        if not fkey:
            continue
        slug = f"{g['slug']}-{fkey}.html"
        if os.path.exists(slug):
            continue  # hand-built page wins
        made.append(render_lt(g, fkey))

print('LONGTAIL DONE:', len(made), 'new pages')
open('_longtail_pages.txt','w').write('\n'.join(made))
