#!/usr/bin/env python3
"""Blog generator — index + article pages."""
exec(open('/mnt/agents/output/app/_gen.py').read().split("# ── render product pages ──")[0])

ARTICLES = {
 'inconel-625-vs-hastelloy-c276': dict(
   cat='Alloy Knowledge', date='2026-07-10', img='prod-pipes', read=7,
   title='Inconel 625 vs. Hastelloy C-276: Which Alloy for Your Service?',
   desc='A metallurgist\'s side-by-side: chemistry, strength, corrosion performance, weldability and cost — plus the decision rule we use with buyers.',
   body='''
<p>These are the two alloys buyers compare most often — and the two most often mis-specified. Both are nickel-chromium-molybdenum workhorses, but they were designed for different enemies. Here's how to choose without overspending or under-protecting.</p>
<h2>The chemistry difference that decides everything</h2>
<p>Inconel 625 (UNS N06625) carries 8–10% molybdenum and 3.15–4.15% niobium. The niobium is the key: it strengthens the matrix by solid-solution hardening, giving 625 its remarkable strength without any heat treatment. Hastelloy C-276 (UNS N10276) drops the niobium and raises molybdenum to 15–17% plus 3–4.5% tungsten. That extra Mo and W buy it near-immunity to the most aggressive chemical environments.</p>
<ul>
<li><strong>Choose 625 when</strong> you need strength and corrosion resistance together — subsea hardware, marine exhausts, aerospace ducting, high-pressure systems. Yield 414 MPa, service to 982 °C.</li>
<li><strong>Choose C-276 when</strong> corrosion is the only enemy and it's a bad one — wet chlorine, hypochlorites, ferric chloride, mixed oxidizing/reducing acids. PREN ≈ 68 vs 625's ≈ 51.</li>
</ul>
<h2>Strength and temperature</h2>
<p>625 wins decisively on strength: 414 MPa minimum yield vs 355 MPa for C-276, and it holds useful strength past 800 °C. C-276 is actually rated for higher maximum temperature on paper (1040 °C), but in practice it's chosen for corrosion, not heat — at high temperatures its strength advantage over 625 disappears.</p>
<h2>Corrosion: the honest comparison</h2>
<p>In clean seawater and chloride service, 625 is already overqualified — pitting and crevice corrosion resistance is excellent and it costs less. Move into flue-gas desulfurization, bleach plants, or mixed acid streams and C-276 earns its premium. If your 316L is failing and you're stepping up, ask yourself: is it pitting (either works, 625 is cheaper) or general/mixed-acid attack (C-276)?</p>
<h2>Weldability and fabrication</h2>
<p>Both weld beautifully with matching filler (ERNiCrMo-3 for 625, ERNiCrMo-4 for C-276). 625's niobium makes it slightly more prone to microfissuring on heavy restraint — nothing a competent weld procedure can't handle. Both form and machine similarly: tough, work-hardening, but predictable.</p>
<h2>Cost</h2>
<p>C-276 typically runs 15–25% above 625, driven by molybdenum and tungsten content. Don't pay it unless your environment demands it — and don't save it if your environment does. A corroded reactor costs more than the alloy delta.</p>
<div class="callout"><strong>Our rule of thumb:</strong> seawater / marine / high strength → 625. Chemical plant worst-case corrosion → C-276. When in doubt, send us your medium, concentration, temperature and pH — grade verification is free and takes under 24 hours.</div>
'''),
 'understanding-mtc-en-10204': dict(
   cat='Quality & Standards', date='2026-06-28', img='qc-caliper', read=6,
   title='MTC EN 10204 3.1 vs 3.2: What Buyers Must Check Before Accepting Material',
   desc='The mill test certificate is your only legal proof of what you bought. Here\'s how to read one — and the 5 checks that catch 95% of certificate problems.',
   body='''
<p>Every year, buyers accept container-loads of nickel alloy on certificates that wouldn't survive a 5-minute audit. The EN 10204 standard defines exactly what a mill test certificate (MTC) must contain — here's how to use it to protect yourself.</p>
<h2>What EN 10204 actually defines</h2>
<p>The standard ranks inspection documents by who validates them:</p>
<ul>
<li><strong>2.1 / 2.2</strong> — the mill's own declaration. No independent test results. Not sufficient for pressure or safety service.</li>
<li><strong>3.1</strong> — validated by the mill's <em>independent inspection department</em> (independent of production). Actual test results for your specific heat. This is the industrial standard for pressure equipment and our default on every order.</li>
<li><strong>3.2</strong> — validated by an <em>independent third party</em> (BV, SGS, TÜV) or the buyer's own inspector, who witnesses the testing. Required for critical service: nuclear, subsea, many EPC specs.</li>
</ul>
<h2>The 5 checks that catch 95% of problems</h2>
<ul>
<li><strong>1. Heat number match.</strong> The number stamped on the material must appear on the MTC. No match = no traceability.</li>
<li><strong>2. Standard match.</strong> The MTC must cite the same standard revision as your PO (e.g. ASTM B444, not just "ASTM").</li>
<li><strong>3. Chemistry in range.</strong> Every element's result must fall inside the standard's limits — not just "conform". For 625: Ni ≥ 58%, Cr 20–23%, Mo 8–10%, Nb+Ta 3.15–4.15%.</li>
<li><strong>4. Mechanical results present.</strong> Tensile, yield and elongation must be actual measured values for your heat, not minimums copied from the standard.</li>
<li><strong>5. Signature and independence.</strong> A 3.1 must be signed by the inspection department — and a 3.2 must name the third-party witness and their stamp.</li>
</ul>
<h2>Red flags</h2>
<p>Certificates issued weeks after shipment, "typical values" instead of test results, missing heat numbers, or PDFs that look edited. Any of these and the material should be quarantined until resolved. We issue the MTC <em>before</em> shipment precisely so your incoming inspection can pre-verify.</p>
<div class="callout"><strong>Buying tip:</strong> ask for a sample MTC with your quotation. A supplier who hesitates to show their documentation format before the order is telling you something.</div>
'''),
 'seamless-vs-welded-pipe': dict(
   cat='Metal Technology', date='2026-06-15', img='prod-fittings', read=5,
   title='Seamless vs. Welded Nickel Alloy Pipe: An Honest Engineering Comparison',
   desc='Welded pipe costs 20–35% less — so when is seamless non-negotiable? The pressure, temperature and corrosion rules we give our own customers.',
   body='''
<p>As a manufacturer of both, we have no reason to oversell either. Here's the decision framework we actually use when buyers ask.</p>
<h2>What the weld seam changes</h2>
<p>A welded pipe starts as plate or strip, formed and welded longitudinally. The weld seam is a metallurgical discontinuity — even a perfect one. It affects four things:</p>
<ul>
<li><strong>Pressure integrity.</strong> Seamless has uniform hoop strength everywhere; welded concentrates stress and potential defects at the seam. For very high pressure or cyclic pressure, seamless is the safe default.</li>
<li><strong>Corrosion.</strong> The weld zone has different microstructure. With proper matching filler and full solution anneal, modern welded pipe performs nearly identically in most media — but in the most aggressive environments, seamless removes the question entirely.</li>
<li><strong>NDT confidence.</strong> Seamless pipe is volumetrically testable (ET/UT of the full body). Welded pipe's seam gets 100% testing, but the test is localized to the seam.</li>
<li><strong>Price and availability.</strong> Welded is 20–35% cheaper and available in larger diameters (to 1219 mm) and longer lengths (to 18 m) that seamless simply can't reach economically.</li>
</ul>
<h2>The decision rules</h2>
<ul>
<li><strong>Choose seamless</strong> for: pressure classes above roughly Class 600, severe thermal cycling, subsea and safety-critical lines, the most aggressive media (hot acids, wet chlorine), small diameters and thick walls.</li>
<li><strong>Choose welded</strong> for: large diameters (NPS 8"+), thin walls, long straight runs, low-to-moderate pressure utility and process lines, scrubbers, ducting, casing.</li>
<li><strong>The middle ground:</strong> welded pipe with 100% radiographic testing of the seam closes most of the integrity gap at a fraction of the seamless premium — ask us to quote both.</li>
</ul>
<div class="callout"><strong>Bottom line:</strong> never downgrade to welded purely on price for critical service — but don't pay seamless prices for ducting either. Send us pressure, temperature and medium and we'll quote the right construction, honestly.</div>
'''),
 'choose-nickel-alloy-grade-5-questions': dict(
   cat='Alloy Knowledge', date='2026-05-30', img='prod-bars', read=6,
   title='How to Choose a Nickel Alloy Grade: The 5 Questions Our Metallurgists Ask',
   desc='Skip the 40-page handbooks. Answer these five questions and the right grade family usually selects itself.',
   body='''
<p>Buyers often arrive with a grade number they got from a drawing made in 1998. Sometimes it's right. Sometimes the environment changed and nobody re-checked. These are the five questions our metallurgists ask before confirming any grade — answer them and the alloy usually selects itself.</p>
<h2>1. What's the medium — exactly?</h2>
<p>"Acid" is not an answer; "15% sulfuric at 60 °C with 200 ppm chlorides" is. Chlorides point to high-Mo alloys (625, C-276). Reducing acids like HCl point to the B-family. Sulfuric and phosphoric favor 825 and G-30. Seawater and HF favor Monel 400.</p>
<h2>2. What's the temperature — continuous and peak?</h2>
<p>Temperature kills alloys two ways: it accelerates corrosion, and it destroys strength. Above ~500 °C you leave stainless territory. Above 700 °C you're choosing between 600/601/617/800H on oxidation behavior. Cyclic service adds fatigue to the equation — tell us about the cycling, not just the setpoint.</p>
<h2>3. What's the mechanical load?</h2>
<p>Pressure, structural load, vibration? If strength matters, the shortlist changes completely: 718 and K-500 (age-hardened) deliver 2–3× the yield of annealed grades. 625 offers the best strength-per-corrosion-resistance compromise without heat treatment.</p>
<h2>4. How will it be fabricated?</h2>
<p>Heavy welding? Deep forming? Machining? Some grades form beautifully (Monel 400, 45% elongation), others machine better (R-405 is free-machining), and all nickel alloys work-harden — so your fabricator's experience with the specific family matters.</p>
<h2>5. What's the failure cost?</h2>
<p>Be honest about consequence. A corroded muffler is an annoyance; a leaking subsea umbilical is a catastrophe. Higher failure cost justifies higher alloy margin — and certified material with third-party witnessed testing (EN 10204 3.2).</p>
<div class="callout"><strong>The shortcut:</strong> send us these five answers and we'll return a verified grade recommendation with alternatives at different price points — free, within 24 hours. That's the whole service.</div>
'''),
 'why-nickel-alloys-corrosion': dict(
   cat='Chemical Elements', date='2026-05-12', img='prod-sheets', read=5,
   title='Why Nickel Alloys Resist Corrosion: The Chemistry in Plain English',
   desc='What chromium, molybdenum, copper and niobium each actually do inside the alloy — and why no single element works alone.',
   body='''
<p>Stainless steel rusts in seawater. Nickel alloys don't — for years. The difference isn't magic; it's four elements doing four specific jobs. Understanding them makes every grade datasheet readable at a glance.</p>
<h2>Nickel: the foundation</h2>
<p>Nickel itself is the matrix — inherently more noble than iron, stable across a huge pH range, and (critically) able to dissolve large amounts of the other alloying elements without forming brittle phases. It's the solvent that makes everything else possible. It also gives the alloys their toughness and resistance to chloride stress-corrosion cracking, the failure mode that quietly kills austenitic stainless steels.</p>
<h2>Chromium: the shield</h2>
<p>Chromium forms a passive chromium-oxide film on the surface — the same trick stainless uses. This film resists <em>oxidizing</em> environments: nitric acid, hot air, oxidizing salts. More Cr (600 has 15%, C-22 has 22%) means better oxidizing-media and high-temperature oxidation resistance.</p>
<h2>Molybdenum (and tungsten): the pitting killers</h2>
<p>Here's where nickel alloys leave stainless behind. Molybdenum dramatically improves resistance to <em>reducing</em> acids and to chloride pitting and crevice attack — the localized corrosion that punches holes through passive films. This is why 625 (9% Mo) shrugs off seawater and C-276 (16% Mo + 4% W) survives environments that dissolve everything else. The PREN formula (Cr + 3.3×Mo) is really measuring this.</p>
<h2>Copper and niobium: the specialists</h2>
<p>Copper (31% in Monel 400, 2% in Incoloy 825) improves resistance to reducing, non-aerated acids — hydrofluoric and sulfuric especially. Niobium does a different job entirely: in 625 and 718 it locks into the matrix and strengthens it, no heat treatment needed — which is why 625 combines high strength with high corrosion resistance, a pairing that's rare in metallurgy.</p>
<h2>Why they must work together</h2>
<p>No single element covers all corrosion types: Cr handles oxidizing, Mo handles reducing and pitting, Cu handles reducing non-oxidizing acids, Nb adds strength. Grade families are just different recipes balancing these four — which is why "which alloy?" is always really "which environment?"</p>
<div class="callout"><strong>Reading datasheets:</strong> next time you see a composition table, scan Cr (oxidizing), Mo+W (pitting/reducing), Cu (reducing acids), Nb (strength). You'll predict the alloy's personality before you read a single property value.</div>
'''),
}

def article_schema(slug, a):
    return json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Blog","item":f"{BASE}/blog.html"},
        {"@type":"ListItem","position":3,"name":a['title'],"item":f"{BASE}/blog-{slug}.html"}]},
      {"@type":"Article","headline":a['title'],"description":a['desc'],
       "image":f"{BASE}/assets/{a['img']}.jpg","datePublished":a['date'],
       "author":{"@type":"Organization","name":"TrueGrade Metals"},
       "publisher":{"@type":"Organization","name":"TrueGrade Metals"},
       "mainEntityOfPage":f"{BASE}/blog-{slug}.html"}
    ]}, indent=2)

def render_article(slug, a):
    others = [ (k,v) for k,v in ARTICLES.items() if k != slug ][:2]
    rel = ''.join(f'''<a href="blog-{k}.html" class="card sub-card" style="display:block">
      <span class="blog-card-cat">{E(v['cat'])}</span><h3 style="font-size:.98rem">{E(v['title'])}</h3>
      <span style="font-size:.84rem;font-weight:600;color:var(--accent)">Read →</span></a>''' for k,v in others)
    body = f'''
{breadcrumb([('Home','index.html'),('Blog','blog.html'),(a['title'][:40]+'…',None)])}
<section class="section" style="padding-top:36px">
  <div class="container article-body reveal in">
    <span class="blog-card-cat">{E(a['cat'])}</span>
    <h1 style="font-size:clamp(1.9rem,4vw,2.7rem);margin:12px 0 10px">{E(a['title'])}</h1>
    <p class="blog-card-meta">{a['date']} · {a['read']} min read · TrueGrade Metals engineering team</p>
    <div class="article-hero"><img src="assets/{a['img']}.jpg" alt="{E(a['title'])}"></div>
    {a['body']}
    <div class="callout" style="margin-top:34px"><strong>Need material for this application?</strong> Send your spec — a named metallurgist replies with a certified quote within 24 hours. <a href="index.html#rfq" style="color:var(--accent-dark);font-weight:700">Request quote →</a></div>
  </div>
</section>
<section class="section section-white" style="padding-top:48px">
  <div class="container">
    <div class="section-head reveal"><h2>Keep reading.</h2></div>
    <div class="sub-grid">{rel}</div>
  </div>
</section>
'''
    write(f'blog-{slug}.html', body, f"{a['title']} | TrueGrade Metals Blog", a['desc'], article_schema(slug, a), active='blog')

def render_blog_index():
    cards = ''.join(f'''<a href="blog-{k}.html" class="card blog-card reveal">
      <img src="assets/{v['img']}.jpg" alt="{E(v['title'])}" loading="lazy">
      <div class="blog-card-body"><span class="blog-card-cat">{E(v['cat'])}</span><h3>{E(v['title'])}</h3>
      <p>{E(v['desc'])}</p><span class="blog-card-meta">{v['date']} · {v['read']} min read</span></div></a>''' for k,v in ARTICLES.items())
    schema = json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Blog","item":f"{BASE}/blog.html"}]},
      {"@type":"Blog","name":"TrueGrade Metals Engineering Blog","url":f"{BASE}/blog.html",
       "blogPost":[{"@type":"BlogPosting","headline":v['title'],"url":f"{BASE}/blog-{k}.html","datePublished":v['date']} for k,v in ARTICLES.items()]}
    ]}, indent=2)
    body = f'''
{breadcrumb([('Home','index.html'),('Blog',None)])}
<section class="p-hero" style="padding-bottom:40px">
  <div class="container">
    <div class="reveal in" style="max-width:760px">
      <div class="eyebrow">Engineering blog</div>
      <h1>Written by metallurgists, <em>not marketers.</em></h1>
      <p class="p-hero-sub">Practical alloy selection, standards decoded and sourcing tactics — the same advice our engineers give on the phone, published free.</p>
    </div>
  </div>
</section>
<section class="section section-white" style="padding-top:56px">
  <div class="container">
    <div class="blog-grid">{cards}</div>
  </div>
</section>
{cta_band('Have a question for our metallurgists?', 'Send your service conditions — we answer technical questions within 24 hours, free, whether or not you buy.')}
'''
    write('blog.html', body, 'Nickel Alloy Engineering Blog | TrueGrade Metals',
          'Practical nickel alloy knowledge: grade selection, MTC standards, seamless vs welded pipe and corrosion chemistry — written by metallurgists.',
          schema, active='blog')

for k, v in ARTICLES.items():
    render_article(k, v)
render_blog_index()
print('BLOG DONE')
