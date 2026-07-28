#!/usr/bin/env python3
"""Industry pages generator — imports shared chrome from _gen."""
import sys, json, html
sys.path.insert(0, '/mnt/agents/output/app')
# reuse chrome by exec-ing the shared portion of _gen (it renders product pages on import — acceptable)
exec(open('/mnt/agents/output/app/_gen.py').read().split("# ── render product pages ──")[0])

INDUSTRIES = {
 'aerospace': dict(name='Aerospace', img='prod-pipes',
   h1='Nickel alloys certified for <em>flight-critical</em> service.',
   sub='Turbine, exhaust, ducting and fastener alloys supplied under EN 9100 aerospace quality management — full traceability from melt to delivery.',
   apps=[('Engine exhaust systems','Inconel 625/718 ducting, bellows and liners for hot-section exhaust.'),('Fuel & hydraulic lines','Seamless capillary and instrumentation tube to AMS-equivalent specs.'),('Fasteners & structures','718, A-286 and Waspaloy bar for high-load airframe hardware.')],
   grades=['Inconel 718','Inconel 625','Inconel X-750','A-286','Waspaloy','Inconel 600'],
   why=[('EN 9100 QMS','Aerospace-grade quality management across production and documentation.'),('Full traceability','Heat number tracked from melt shop to packing list — audit-ready.'),('Third-party witness','BV / SGS / TÜV witnessed testing (EN 10204 3.2) on request.')]),
 'oil-gas': dict(name='Oil & Gas', img='factory',
   h1='Alloys that survive <em>sour service</em> and the seabed.',
   sub='Downhole tubing, subsea umbilicals, flowlines and valve trim in 625, 718, 825 and 925 — NACE MR0175-compliant material on request.',
   apps=[('Subsea umbilicals & flowlines','Inconel 625 tube for hydraulic and chemical injection lines.'),('Downhole tubing & hangers','825 and 925 for sour wells with H₂S and chloride.'),('Valve trim & wellhead parts','718 and K-500 bar machined to OEM drawings.')],
   grades=['Inconel 625','Inconel 718','Incoloy 825','Incoloy 925','Monel K-500','Hastelloy C-276'],
   why=[('NACE compliance','MR0175 / ISO 15156 hardness-controlled material on request.'),('Deep-stock heats','Pre-smelted 625 and 825 heats for emergency shut-down orders.'),('Coordinated logistics','Sea-air combined freight to hit rig windows.')]),
 'chemical-processing': dict(name='Chemical Processing', img='prod-fittings',
   h1='The last line of defense against <em>mixed acids.</em>',
   sub='Hastelloy C-276, C-22, B-3 and G-30 for reactors, scrubbers and transfer lines where stainless fails in weeks.',
   apps=[('Reactor & vessel internals','C-276 plate and bar for agitators, baffles and linings.'),('Scrubbers & flue gas','C-276 / C-22 sheet for quench and absorber sections.'),('Acid transfer piping','B-3 for HCl, G-30 for phosphoric service.')],
   grades=['Hastelloy C-276','Hastelloy C-22','Hastelloy B-3','Hastelloy G-30','Incoloy 825','Alloy 20'],
   why=[('Environment matching','Send your medium, concentration, temperature — we verify the grade free.'),('Weld-quality filler','Matching ERNiCrMo filler wire from the same supply system.'),('Fast remakes','If a part is damaged on site, stock heats enable quick replacement.')]),
 'marine': dict(name='Marine & Offshore', img='prod-bars',
   h1='Seawater is our <em>home environment.</em>',
   sub='Monel 400/K-500 and Inconel 625 for propulsion, piping and subsea hardware — proven against pitting, crevice and chloride SCC.',
   apps=[('Propeller shafts & blades','Monel K-500 forged bar, straightness guaranteed.'),('Seawater piping & coolers','Monel 400 and 625 seamless tube, cupronickel alternatives.'),('Subsea fasteners','K-500 and 718 bolting with full traceability.')],
   grades=['Monel 400','Monel K-500','Inconel 625','Incoloy 926','Hastelloy C-276'],
   why=[('Marine track record','Material in service on vessels and platforms worldwide.'),('Cathodic compatibility','Grade selection advice for galvanic couples with hull materials.'),('Seaworthy packing','Wooden-case export packing standard; VCI protection on request.')]),
 'power-generation': dict(name='Power Generation', img='prod-sheets',
   h1='From boiler tubes to <em>turbine hardware.</em>',
   sub='High-temperature alloys for USC boilers, HRSGs, gas turbines and nuclear balance-of-plant — 600, 617, 690, 740H, 800H.',
   apps=[('Superheater & reheater tubes','Inconel 617 and 740H for ultra-supercritical service.'),('HRSG & waste heat','800H/800HT tube and pipe for thermal cycling.'),('Nuclear steam generators','Inconel 690 tube with full documentation.')],
   grades=['Inconel 617','Inconel 740H','Inconel 690','Incoloy 800H','Incoloy 800HT','Inconel 600'],
   why=[('Creep data support','Long-term creep-rupture data shared for design review.'),('Outage-speed delivery','Stocked heats for planned and unplanned outages.'),('PED certification','PED 2014/68/EU material for European pressure equipment.')]),
 'automotive': dict(name='Automotive & Motorsport', img='prod-wires',
   h1='Exhaust heat, <em>handled.</em>',
   sub='Turbocharger, exhaust and EGR alloys — Inconel 625/718/751 sheet, strip, tube and wire for performance and durability programs.',
   apps=[('Turbo & exhaust manifolds','625 and 751 sheet and tube for thin-wall hot parts.'),('Valve train','751 and 80A bar for exhaust valves.'),('Sensors & fittings','Capillary tube and machined fittings to drawing.')],
   grades=['Inconel 625','Inconel 751','Inconel 718','Nimonic 80A','Incoloy 800'],
   why=[('Small-batch friendly','Low MOQs for development and motorsport programs.'),('Fast iteration','Cut-to-size blanks shipped in days for dyno testing.'),('Consistent temper','Strip and wire supplied to specified temper for forming.')]),
 'thermal-processing': dict(name='Thermal Processing', img='prod-bars',
   h1='Furnace parts that <em>outlast the campaign.</em>',
   sub='Radiant tubes, muffles, baskets and rollers in 600, 601, 602CA and 330 — oxidation and carburization resistance to 1200 °C.',
   apps=[('Radiant tubes','601 / 602CA centrifugal and fabricated tubes.'),('Muffles & retorts','600/601 sheet fabricated to drawing.'),('Baskets & fixtures','330 and 600 bar, mesh and wire for charge fixtures.')],
   grades=['Inconel 600','Inconel 601','Inconel 602CA','Alloy 330','Incoloy 800H','Inconel 617'],
   why=[('Atmosphere expertise','Grade selection for carburizing, nitriding and hydrogen atmospheres.'),('Fabrication support','Weld procedure guidance for furnace fabricators.'),('Repeat-order pricing','Blanket orders for furnace OEMs with scheduled releases.')]),
 'pollution-waste': dict(name='Pollution Control & Waste', img='prod-fittings',
   h1='FGD and incineration environments <em>eat stainless alive.</em>',
   sub='C-276, C-22 and 686 for quenchers, absorbers, ducting and stack liners facing chlorides, fluorides and sulfuric dewpoints.',
   apps=[('FGD absorber internals','C-276 sheet, pipe and fittings for wet scrubbers.'),('Waste incineration','686 / C-2000 for mixed halide service.'),('Stack liners & ducting','Thin-gauge C-276 sheet with matching filler.')],
   grades=['Hastelloy C-276','Hastelloy C-22','Inconel 686','Hastelloy C-2000','Hastelloy G-35'],
   why=[('Dewpoint experience','Grade selection across the acid dewpoint zones of your process.'),('Sheet + filler packages','Plate, sheet and matching welding consumables in one PO.'),('Retrofit speed','Cut-to-size panels for outage retrofits on short notice.')]),
 'electrical-resistance': dict(name='Electrical & Resistance Heating', img='prod-wires',
   h1='Resistance alloys, <em>drawn to spec.</em>',
   sub='Ni-Cr and Fe-Cr-Al resistance wire, ribbon and strip for heating elements — plus pure nickel for batteries and electronics.',
   apps=[('Heating elements','80/20 and 70/30 Ni-Cr wire and ribbon to your resistance spec.'),('Fe-Cr-Al elements','0Cr25Al5-type alloys for higher-temperature elements.'),('Battery & electronics','Nickel 200/201 strip, wire and mesh.')],
   grades=['Ni-Cr 80/20','Ni-Cr 70/30','Fe-Cr-Al','Nickel 200','Nickel 201','Monel 400'],
   why=[('Resistance tolerance','Wire drawn to specified Ω/m with test certificates.'),('Small MOQ','Kilogram quantities for element development.'),('Consistent temper','Annealed wire for coiling and forming.')]),
 'petro-processing': dict(name='Petrochemical & Refining', img='prod-pipes',
   h1='Crude, catalyst and <em>corrosion loops — covered.</em>',
   sub='Tube and pipe for hydroprocessing, reforming and sour-water service — 825, 625, 400 and 800H with refinery-grade documentation.',
   apps=[('Hydrocracker & reformer tubes','800H and 625 for high-pressure hot service.'),('Sour water & amine','825 and 400 for corrosive overhead systems.'),('Heat exchangers','Seamless and U-bent tube bundles to TEMA requirements.')],
   grades=['Incoloy 800H','Inconel 625','Incoloy 825','Monel 400','Hastelloy C-276'],
   why=[('TEMA familiarity','U-tube bending and bundle documentation for exchanger shops.'),('Turnaround slots','Production slots reserved for turnaround seasons.'),('Full NDT options','ET, UT, hydro and PMI to your specification.')]),
 'electric-telecom': dict(name='Electronics & Telecom', img='prod-wires',
   h1='Precision alloys for <em>precision signals.</em>',
   sub='Controlled-expansion and soft-magnetic alloys — 4J36 (Invar), 4J42, 1J50/1J79 — plus pure nickel for connectors and shielding.',
   apps=[('Hermetic packaging','4J42 / 4J50 strip and wire for glass-to-metal seals.'),('Magnetic shielding','1J79 / 1J50 high-permeability strip and fabricated shields.'),('Connectors & springs','Nickel 200 and Monel wire for corrosion-stable contacts.')],
   grades=['4J36 (Invar)','4J42','1J50','1J79','Nickel 200','Monel 400'],
   why=[('Precision strip','Tight thickness and flatness tolerance for stamping.'),('Batch consistency','Controlled chemistry for repeatable CTE and permeability.'),('Small reels','Lab and pilot quantities for R&D programs.')]),
 'welding-products': dict(name='Welding & Fabrication', img='prod-wires',
   h1='Filler metal that <em>matches the heat.</em>',
   sub='A full range of nickel-alloy welding consumables — ERNiCrMo-3, ENiCrMo-3, ERNi-1, ERNiCu-7 — with MTCs welders and inspectors both accept.',
   apps=[('TIG / MIG filler','Spooled and cut-length filler for all major nickel grades.'),('SMAW electrodes','Coated electrodes, vacuum packed, batch certified.'),('Overlay & cladding','Strip and wire for corrosion-resistant overlay.')],
   grades=['ERNiCrMo-3','ENiCrMo-3','ERNi-1','ERNiCu-7','ERNiCr-3','ENiCrFe-3'],
   why=[('AWS classified','A5.14 / A5.11 classifications with certificates per batch.'),('Base-metal advice','Dissimilar-weld guidance from our metallurgists.'),('Kilogram sales','No MOQ on stocked classifications for repair work.')]),
}

def industry_schema(key, ind):
    return json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Industries","item":f"{BASE}/industries.html"},
        {"@type":"ListItem","position":3,"name":ind['name'],"item":f"{BASE}/industry-{key}.html"}]},
      {"@type":"WebPage","name":f"Nickel Alloys for {ind['name']} — TrueGrade Metals","url":f"{BASE}/industry-{key}.html"}
    ]}, indent=2)

def render_industry(key, ind):
    apps = ''.join(f'<div class="card app-card reveal"><h3>{E(t)}</h3><p>{E(d)}</p></div>' for t,d in ind['apps'])
    chips = ''.join(f'<a href="index.html#rfq">{E(g)}</a>' for g in ind['grades'])
    why = feature_list(ind['why'])
    title = f"Nickel Alloys for {ind['name']} | TrueGrade Metals"
    desc = f"Certified nickel alloys for {ind['name'].lower()} applications — {', '.join(ind['grades'][:4])}. EN 10204 3.1 MTC, named metallurgist, quote in 24 hours."
    body = f'''
{breadcrumb([('Home','index.html'),('Industries','industries.html'),(ind['name'],None)])}
<section class="p-hero">
  <div class="container">
    <div class="p-hero-grid">
      <div class="reveal in">
        <div class="eyebrow">Industry — {E(ind['name'])}</div>
        <h1>{ind['h1']}</h1>
        <p class="p-hero-sub">{ind['sub']}</p>
        <div class="p-hero-actions">
          <a href="index.html#rfq" class="btn btn-primary btn-lg">Discuss your application →</a>
          <a href="categories.html" class="btn btn-ghost btn-lg">Browse products</a>
        </div>
      </div>
      <div class="reveal in d1">
        <div class="hero-photo"><img src="assets/{ind['img']}.jpg" alt="Nickel alloys for {E(ind['name'])} — TrueGrade Metals"></div>
      </div>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Applications</div><h2>Where our material works in {E(ind['name'].lower())}.</h2></div>
    <div class="app-grid">{apps}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Recommended grades</div><h2>Alloys we ship into this industry.</h2></div>
    <div class="grade-chips reveal">{chips}</div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Why TrueGrade</div><h2>Industry-specific capability.</h2></div>
    {why}
  </div>
</section>

{cta_band(f'Working in {E(ind["name"].lower())}?', 'Send your service conditions — medium, temperature, pressure. A metallurgist verifies the grade and quotes within 24 hours.')}
'''
    write(f'industry-{key}.html', body, title, desc, industry_schema(key, ind), active='industries')

# industries index page
def render_industries_index():
    cards = ''.join(f'''<a href="industry-{k}.html" class="card app-card reveal" style="display:block">
      <h3>{E(v['name'])}</h3><p>{E(v['sub'][:110])}…</p>
      <span style="font-size:.86rem;font-weight:600;color:var(--accent)">Explore →</span></a>''' for k,v in INDUSTRIES.items())
    schema = json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Industries","item":f"{BASE}/industries.html"}]},
      {"@type":"ItemList","name":"Industries Served","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":v['name'],"url":f"{BASE}/industry-{k}.html"} for i,(k,v) in enumerate(INDUSTRIES.items())]}
    ]}, indent=2)
    body = f'''
{breadcrumb([('Home','index.html'),('Industries',None)])}
<section class="p-hero" style="padding-bottom:40px">
  <div class="container">
    <div class="reveal in" style="max-width:760px">
      <div class="eyebrow">Industries served</div>
      <h1>Trusted where <em>failure is not an option.</em></h1>
      <p class="p-hero-sub">Twelve industries, one quality system. Each page shows the applications, recommended grades and industry-specific capability — verified by a metallurgist, not a marketing intern.</p>
    </div>
  </div>
</section>
<section class="section section-white" style="padding-top:56px">
  <div class="container">
    <div class="app-grid">{cards}</div>
  </div>
</section>
{cta_band('Not sure which grade your industry needs?', 'Describe your service conditions — medium, temperature, pressure — and get a verified recommendation within 24 hours.')}
'''
    write('industries.html', body, 'Industries Served — Nickel Alloy Applications | TrueGrade Metals',
          'Nickel alloys for aerospace, oil & gas, chemical processing, marine, power generation and 7 more industries. EN 10204 3.1 MTC, quote in 24 hours.',
          schema, active='industries')

for k, v in INDUSTRIES.items():
    render_industry(k, v)
render_industries_index()
print('INDUSTRY PAGES DONE')
