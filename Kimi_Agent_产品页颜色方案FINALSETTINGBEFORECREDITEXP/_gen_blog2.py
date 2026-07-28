#!/usr/bin/env python3
"""Blog batch 2 — 10 more articles; re-renders index with all 15."""
src = open('/mnt/agents/output/app/_gen_blog.py').read()
exec(src.split("for k, v in ARTICLES.items():")[0])  # loads ARTICLES + renderers, no side effects

B2 = {
 'monel-400-vs-inconel-625-marine': dict(
   cat='Alloy Knowledge', date='2026-07-18', img='prod-pipes', read=6,
   title='Monel 400 vs. Inconel 625 for Marine Service: Which One Survives Seawater?',
   desc='Both are marine legends — but they fight different battles. Seawater velocity, biofouling, temperature and budget decide this one.',
   body='''
<p>Ask any marine engineer to name two nickel alloys and you'll hear these two. Both have decades of seawater service behind them — and both get misapplied, usually by substituting one for the other on price. Here's the real dividing line.</p>
<h2>Monel 400: the seawater specialist</h2>
<p>Monel 400 (UNS N04400) is a 67% nickel / 31% copper alloy with a century of marine history. Its superpower is <em>flowing</em> seawater: excellent resistance to pitting and stress-corrosion cracking, near-zero corrosion rates in fast-moving water, and outstanding resistance to biofouling (marine organisms dislike copper). It's also the default for hydrofluoric acid and a favorite for propeller shafts, pump components and seawater valves.</p>
<p>Its weakness is just as specific: <strong>stagnant seawater</strong>. Under deposits or in crevices where flow stops, Monel 400 can pit. And its strength is modest — 240 MPa yield in the annealed condition.</p>
<h2>Inconel 625: the deep-water all-rounder</h2>
<p>Inconel 625 (UNS N06625) attacks the problem from the other side: 9% molybdenum plus niobium gives it a PREN around 51 — effectively immune to pitting and crevice corrosion in seawater, flowing or stagnant, warm or cold. It also delivers 414 MPa yield without heat treatment, which is why subsea engineering adopted it wholesale: risers, umbilicals, manifold hardware, fasteners on splash-zone structures.</p>
<p>The catch is cost — 625 typically runs 2–3× the price of Monel 400 — and it's less resistant to biofouling than the copper-bearing alloy.</p>
<h2>The decision rules we give customers</h2>
<ul>
<li><strong>Flowing seawater, general marine hardware, tight budget</strong> → Monel 400. Add cathodic protection or ensure flow if stagnation is possible.</li>
<li><strong>Stagnant seawater, crevices, warm water, subsea or high-stress service</strong> → 625. Its crevice-corrosion immunity removes the failure mode that kills Monel.</li>
<li><strong>Hydrofluoric acid</strong> → Monel 400, no contest — 625 is not the right tool there.</li>
<li><strong>Strength-critical marine parts</strong> (shafts under high load, subsea fasteners) → 625 or age-hardened Monel K-500.</li>
</ul>
<div class="callout"><strong>Field note:</strong> the most expensive Monel-400 failure we see is stagnant-seawater pitting under gaskets. If your design has crevices it cannot avoid, that's the argument for 625 — made before the order, not after the leak.</div>
'''),
 'hastelloy-c22-vs-c276': dict(
   cat='Alloy Knowledge', date='2026-07-14', img='prod-fittings', read=6,
   title='Hastelloy C-22 vs. C-276: The Chemical Industry\'s Toughest Choice',
   desc='C-276 is the famous one; C-22 is often the better one. Oxidizing vs. reducing chemistry decides — here\'s how to tell which side your process is on.',
   body='''
<p>Inside chemical plants, the argument over C-22 versus C-276 has been running for thirty years. Both are nickel-chromium-molybdenum alloys with elite corrosion resistance. The difference is six elements of chemistry — and knowing which one your process needs saves either money or equipment.</p>
<h2>The chemistry gap in one line</h2>
<p>C-276 (UNS N10276): 16% Mo, 4% W, ~15.5% Cr. C-22 (UNS N06022): 13% Mo, 3% W, ~22% Cr. In plain terms — <strong>C-276 bets on molybdenum, C-22 bets on chromium.</strong></p>
<h2>What that means in the plant</h2>
<ul>
<li><strong>Reducing acids</strong> (hot HCl, sulfuric without oxidizers): molybdenum rules. C-276 has the edge — it's the historical champion of reducing service.</li>
<li><strong>Oxidizing media</strong> (ferric chloride, cupric chloride, nitric-bearing mixes, wet chlorine gas, hypochlorite): chromium rules. C-22's 22% Cr makes it clearly superior — this is why bleach plants and FGD systems standardized on it.</li>
<li><strong>Mixed or upset-prone streams:</strong> real processes drift between oxidizing and reducing. C-22's balanced chemistry tolerates excursions better, which is why many EPCs now specify it as the "insurance" grade.</li>
<li><strong>Pitting/crevice (PREN):</strong> C-276 ≈ 68, C-22 ≈ 65 — effectively a tie. Both laugh at seawater.</li>
</ul>
<h2>Fabrication and price</h2>
<p>Both weld well with matching fillers (ERNiCrMo-4 / ERNiCrMo-10) and both resist weld-zone corrosion better than nearly anything else on the market. C-22 is slightly more resistant to intermetallic precipitation during welding — a real advantage on heavy sections. Pricing is usually within a few percent; availability of the exact product form often decides.</p>
<h2>Our honest recommendation</h2>
<p>If your medium is a known, stable reducing acid — C-276, the proven answer. If your stream is oxidizing, mixed, or simply <em>not fully characterized</em> — C-22 is the safer default. When a customer sends us an analysis that contains both chlorides and oxidizing ions, we quote C-22.</p>
<div class="callout"><strong>Shortcut:</strong> send the medium, concentration, temperature and any oxidizing species (Fe³⁺, Cu²⁺, dissolved O₂, hypochlorite). We'll confirm the grade in writing within 24 hours — free.</div>
'''),
 'inconel-718-vs-625-aerospace': dict(
   cat='Alloy Knowledge', date='2026-07-08', img='prod-bars', read=6,
   title='Inconel 718 vs. 625 in Aerospace: Strength, Temperature and the 650 °C Wall',
   desc='718 is the most-used superalloy on Earth; 625 is the most trusted. The 650 °C boundary between them is the most important line in aerospace materials.',
   body='''
<p>Between them, Inconel 718 and 625 account for an enormous share of aerospace nickel alloy consumption. They are not competitors so much as neighbors with a hard border: <strong>650 °C</strong>. Understanding why that border exists tells you which alloy your part needs.</p>
<h2>718: the strength king (below 650 °C)</h2>
<p>Inconel 718 (UNS N07718) is age-hardenable: niobium and titanium form γ″ and γ′ precipitates during heat treatment that pin dislocations and drive yield strength past 1,100 MPa. No other widely available superalloy combines that strength with such good weldability — which is why roughly half the weight of a modern jet engine is 718: disks, shafts, casings, fasteners, rocket motor cases.</p>
<p>The same precipitates are its ceiling. Above ~650 °C the γ″ phase over-ages and dissolves, and strength falls off a cliff. 718's kingdom ends there.</p>
<h2>625: the endurance champion</h2>
<p>Inconel 625 (UNS N06625) takes the opposite route: solid-solution strengthening from molybdenum and niobium, no heat treatment needed, no precipitates to dissolve. Yield is "only" 414 MPa, but it keeps useful strength to 800 °C+ and survives oxidation to 982 °C. Add near-immunity to corrosion and you get the alloy of exhaust systems, ducting, bellows, seals and marine/aero fasteners in corrosive zones.</p>
<h2>The practical selection table</h2>
<ul>
<li><strong>Rotating parts, high stress, &lt;650 °C</strong> (disks, shafts, bolts) → 718, aged to AMS 5662/5663.</li>
<li><strong>Hot structures, corrosive zones, welded assemblies</strong> (exhaust, ducting, bellows) → 625.</li>
<li><strong>Parts that are both highly stressed AND hot?</strong> → This is where buyers get into trouble. Neither alloy fits; you're in Waspaloy / Rene territory. Tell us early.</li>
<li><strong>Repair welding on aged 718?</strong> Possible but requires re-solution and re-aging — plan the heat treatment with the repair, not after it.</li>
</ul>
<h2>Buyer's note on certification</h2>
<p>Aerospace 718 is bought to a specification, not a grade name: AMS 5662/5663 (bars), AMS 5596 (sheet), with tensile, stress-rupture and microstructure data per heat. Every 718 bar and forging we ship carries full MTC EN 10204 3.1 traceability with the spec revision stated on the certificate — because in aerospace, the paperwork <em>is</em> the product.</p>
<div class="callout"><strong>Rule of thumb:</strong> strength decides → 718. Temperature or corrosion decides → 625. Both decide → call us before you commit the drawing.</div>
'''),
 'nickel-alloy-welding-guide': dict(
   cat='Metal Technology', date='2026-07-02', img='prod-wires', read=8,
   title='Welding Nickel Alloys: Filler Selection, Heat Input and the Mistakes That Crack Welds',
   desc='Nickel alloys weld beautifully — if you respect three rules. Filler matching, heat input control and cleanliness decide whether the joint outlasts the pipe.',
   body='''
<p>Fabrication shops either love nickel alloys or fear them, and the difference is almost always procedure discipline. The metallurgy is forgiving; the process is not. Here is the condensed version of the welding guide we give customer fabrication teams.</p>
<h2>Rule 1: Match the filler to the service, not just the base metal</h2>
<ul>
<li><strong>625</strong> → ERNiCrMo-3. Also the universal dissimilar-metal filler — welding 625 to stainless, or stainless to carbon steel, usually uses 625 filler.</li>
<li><strong>C-276</strong> → ERNiCrMo-4; <strong>C-22</strong> → ERNiCrMo-10. In mixed service the C-22 filler often wins even on C-276 joints.</li>
<li><strong>Monel 400</strong> → ERNiCu-7. Never use a Cr-bearing filler on Monel — it invites cracking.</li>
<li><strong>825</strong> → ERNiFeCr-1 (alloy 65) for corrosion matching.</li>
<li><strong>718</strong> → matching 718 filler, and plan post-weld heat treatment — the weld zone loses the aged strength until re-treated.</li>
</ul>
<h2>Rule 2: Heat input is a corrosion variable, not just a distortion variable</h2>
<p>Keep heat input low (typically under 1.5 kJ/mm) and interpass temperature under 150 °C. Overheating does two kinds of damage: it grows the heat-affected zone where carbides and intermetallics precipitate (killing corrosion resistance locally), and it raises hot-cracking risk. Stringer beads, no weaving, no exceptions on corrosion-critical joints.</p>
<h2>Rule 3: Cleanliness is non-negotiable</h2>
<p>Sulfur, lead, phosphorus and oil cause hot cracking in nickel alloys at concentrations that would be harmless on carbon steel. Degrease before welding, use dedicated stainless brushes, and keep the nickel work area physically separated from carbon steel grinding — embedded iron particles become rust spots and pitting sites in service.</p>
<h2>The mistakes we actually see in failed joints</h2>
<ul>
<li>Carbon steel wire brush or shared grinding discs → embedded iron → pitting initiation sites.</li>
<li>High heat input "to make it flow" → HAZ sensitization → knife-line attack in acid service.</li>
<li>Wrong filler for dissimilar joints (308L on stainless-to-625) → diluted, crack-sensitive weld metal.</li>
<li>Skipped purge on the root side → sugared root → crevice corrosion starter notch.</li>
</ul>
<div class="callout"><strong>Free resource:</strong> ordering pipe, fittings or flanges from us? Ask for the matching welding-consumables recommendation sheet for your grade — we include it with the MTC on request.</div>
'''),
 'nickel-alloy-machining-guide': dict(
   cat='Metal Technology', date='2026-06-24', img='prod-bars', read=7,
   title='Machining Nickel Alloys: Speeds, Tooling and Why They Work-Harden Against You',
   desc='Nickel alloys aren\'t hard to machine — they\'re hard to machine twice. Tool geometry, feed discipline and coolant strategy from our shop floor.',
   body='''
<p>Every machining guide for nickel alloys says "low speeds, high feeds, rigid setups." True, but incomplete. The shops that succeed understand <em>why</em>: these alloys work-harden at the surface the instant a tool rubs instead of cuts. The second pass over a rubbed surface is machining something much harder than the bar you bought.</p>
<h2>The physics in one paragraph</h2>
<p>Nickel alloys have low thermal conductivity (heat stays in the tool tip, not the chip), high toughness (the chip doesn't want to break), and extreme work-hardening response. Your entire strategy is: get the heat out with the chip, keep the tool cutting — never rubbing — and never let a dull edge touch the workpiece.</p>
<h2>Practical parameters (carbide tooling, general guidance)</h2>
<ul>
<li><strong>Turning:</strong> 20–50 m/min on age-hardened grades (718, K-500), 30–70 m/min on annealed grades (625, 400). Feed ≥ 0.15 mm/rev — stay <em>under</em> the work-hardened skin, never skim it.</li>
<li><strong>Tooling:</strong> sharp positive-rake carbide, PVD-coated, honed edge for roughing. CBN or ceramic only for finishing aged 718 at speed. Rigid, short overhang — chatter is a hardening machine.</li>
<li><strong>Coolant:</strong> high-pressure through-tool emulsion where possible; flood as a minimum. Dry machining nickel alloys is a false economy except with ceramics on 718.</li>
<li><strong>Drilling:</strong> peck, positive feed, cobalt or carbide split-point. A dwell of one second at hole bottom work-hardens it beyond the next tool's patience.</li>
</ul>
<h2>Grade-by-grade difficulty (easiest first)</h2>
<ul>
<li><strong>Monel R-405</strong> — the free-machining grade, sulfurized on purpose. Closest thing to "easy" in this family.</li>
<li><strong>Monel 400, Nickel 200</strong> — gummy but predictable; sharp tools and positive feed.</li>
<li><strong>625, C-276, 825</strong> — mid-pack; standard nickel-alloy discipline works.</li>
<li><strong>718 aged, Waspaloy, K-500</strong> — the hard end. Machine in the solution-annealed condition where possible and age afterward; finish with rigid setups and sharp ceramics/CBN.</li>
</ul>
<div class="callout"><strong>Procurement tip:</strong> if your part is heavily machined, tell us at enquiry. We can supply bar in the optimal condition (annealed vs. aged) and straightness for your process — it often matters more than the cutting parameters.</div>
'''),
 'heat-treatment-nickel-alloys': dict(
   cat='Metal Technology', date='2026-06-18', img='prod-sheets', read=7,
   title='Heat Treatment of Nickel Alloys: Solution Anneal, Aging and What Your PO Must Specify',
   desc='The same alloy can be delivered soft, hard, or ruined — depending on heat treatment. What the terms mean and what to write on your purchase order.',
   body='''
<p>Two bars of Inconel 718 from the same heat can have yield strengths of 450 MPa or 1,100 MPa. The difference is nothing but heat treatment — and if your purchase order doesn't specify it, you get whatever the mill had in stock. Here's what the terms mean and how to specify them.</p>
<h2>Solution annealing: the soft reset</h2>
<p>Heating to 950–1,200 °C (grade-dependent) dissolves precipitates and homogenizes the structure; rapid cooling (water quench or fast air cool) locks it in. Result: the softest, most ductile, most corrosion-resistant condition — best for forming, welding and corrosion service. Grades like 625, C-276, 400 and 825 are <em>only</em> used in the solution-annealed condition; their properties come from chemistry, not heat treatment.</p>
<h2>Age hardening: the strength recipe</h2>
<p>A precipitation-hardening grade (718, K-500, X-750, Waspaloy) is solution-annealed first, then aged at 600–800 °C for hours. Tiny γ′/γ″ precipitates form and multiply strength 2–3×. The classic 718 cycle: 980 °C solution + 720 °C/8h, furnace cool to 620 °C/8h, air cool (per AMS 5662). Get the aging wrong — too hot, too long, wrong cool rate — and you either under-age (soft) or over-age (soft again, but permanently).</p>
<h2>Stress relieving: the quiet one</h2>
<p>A lower-temperature bake (400–650 °C) that reduces residual stress from machining or cold work without changing the basic condition. Often specified for springs and formed parts. Note: stress-relieving a heavily cold-worked part at the wrong temperature can trigger unwanted precipitation — check the grade datasheet first.</p>
<h2>What to write on the PO</h2>
<ul>
<li><strong>Condition, explicitly:</strong> "solution annealed" / "annealed + aged per AMS 5662" / "cold drawn, stress relieved". Never just the grade name.</li>
<li><strong>The governing spec:</strong> AMS/ASTM with revision. The spec defines the cycle, the mechanical requirements and the test method — it is the heat treatment contract.</li>
<li><strong>Test evidence:</strong> tensile results per heat (and per lot for aged material), hardness survey where relevant. On our MTCs the heat-treatment batch is traceable to the mechanical results line by line.</li>
</ul>
<div class="callout"><strong>Common failure:</strong> a drawing calls "Inconel 718" and the buyer orders whatever is cheapest — receiving annealed bar at half the expected strength. The fix costs a heat-treatment cycle, weeks, and sometimes the part. Specify condition; verify on the MTC.</div>
'''),
 'pren-pitting-resistance-explained': dict(
   cat='Alloy Knowledge', date='2026-06-10', img='prod-sheets', read=5,
   title='PREN Explained: The One Number That Predicts Pitting Resistance (and Its Limits)',
   desc='Pitting Resistance Equivalent Number lets you rank alloys for chloride service in seconds — if you know what it measures and what it ignores.',
   body='''
<p>Every datasheet in the chloride world quotes PREN, and most buyers use it exactly right: as a fast ranking tool. A few use it as a guarantee — and that ends in crevice corrosion. Here is the number, honestly explained.</p>
<h2>The formula</h2>
<p>PREN = %Cr + 3.3×%Mo + 16×%N (some versions add 30×%W). It compresses the three pitting-fighting elements into one score. Chromium maintains the passive film; molybdenum (weighted 3.3× because it works far above its percentage) blocks pit growth; nitrogen strengthens both effects.</p>
<h2>The reference points worth memorizing</h2>
<ul>
<li><strong>316L stainless:</strong> PREN ≈ 24 — marginal in seawater, fails in warm chloride service.</li>
<li><strong>PREN ≥ 40:</strong> the traditional "seawater-worthy" threshold (super duplex just crosses it).</li>
<li><strong>Alloy 625:</strong> ≈ 51 — comfortably immune to seawater pitting at ambient temperature.</li>
<li><strong>C-276:</strong> ≈ 68 — near the top of the practical scale.</li>
</ul>
<h2>What PREN ignores — and why it matters</h2>
<ul>
<li><strong>Crevice corrosion</strong> starts at lower thresholds than pitting and is the more common field failure. A PREN-51 alloy that never pits can still crevice-attack under a gasket.</li>
<li><strong>Temperature.</strong> PREN is computed from chemistry; it knows nothing about your 80 °C process stream. Pitting resistance falls as temperature rises.</li>
<li><strong>pH and oxidizing species.</strong> The formula assumes chloride attack. Hot reducing acids are a molybdenum game with different rules.</li>
<li><strong>Microstructure.</strong> PREN uses nominal chemistry. Segregation, sigma phase or a bad weld HAZ can drag the <em>local</em> PREN far below the certificate number — one more reason heat input control matters in fabrication.</li>
</ul>
<h2>How to use it properly</h2>
<p>Use PREN to build a shortlist, never to close the decision. Rank the candidates, then overlay crevice geometry, temperature, pH and weld condition. For seawater at ambient temperature with tight crevices, we start the conversation at PREN 50+ — and for anything warmer or more aggressive, we move to corrosion-rate data in the actual medium, which we maintain for the grades we sell.</p>
<div class="callout"><strong>Quick tool:</strong> our <a href="tools.html" style="color:var(--accent-dark);font-weight:700">grade comparison tool</a> ranks 11 common alloys by PREN, yield and temperature limit side by side — the same table our engineers use.</div>
'''),
 'sourcing-nickel-alloys-from-china': dict(
   cat='Buying Guides', date='2026-06-02', img='packing', read=8,
   title='Sourcing Nickel Alloys from China: A Buyer\'s Risk Checklist That Actually Works',
   desc='China supplies a growing share of the world\'s nickel alloy — at real savings, with real risks. The 8-point verification process we run on ourselves.',
   body='''
<p>Let us be transparent: we are a Chinese manufacturer writing this guide, and we wrote it as the checklist we wish every buyer applied to every supplier — including us. Chinese nickel alloy quality now spans the full range from world-class to unacceptable. The price advantage is real (typically 15–30% below Western mills); the variance is real too. Verification is what converts the price advantage into value.</p>
<h2>The 8-point checklist</h2>
<ul>
<li><strong>1. Demand EN 10204 3.1 minimum — before shipment.</strong> Actual heat-specific results, issued with the packing photos, not weeks later. We issue the MTC before the container closes, every order.</li>
<li><strong>2. Verify chemistry against the standard, not "conform".</strong> Every element's measured value must sit inside the ASTM/AMS range. Learn the key elements for your grade (for 625: Ni ≥58, Cr 20–23, Mo 8–10, Nb+Ta 3.15–4.15).</li>
<li><strong>3. Check heat-number traceability.</strong> Stamped on the product, printed on the MTC, matching on the packing list. Three documents, one number.</li>
<li><strong>4. Use third-party inspection on first orders.</strong> SGS/BV/TÜV witnessing (upgrade to 3.2) costs a few hundred dollars and settles the trust question permanently. Any supplier who resists it has answered your question.</li>
<li><strong>5. Audit the test equipment claim.</strong> PMI (XRF) for chemistry, UT/ET for defects, hydrostatic for pipe — ask for calibration certificates or a video of your material being tested.</li>
<li><strong>6. Order samples before containers.</strong> A short length of pipe or bar, tested in your own lab, costs little and validates chemistry, mechanicals and surface quality at once.</li>
<li><strong>7. Specify the standard revision.</strong> "ASTM B444" without a year leaves room for interpretation; "ASTM B444-19" does not.</li>
<li><strong>8. Watch the packaging.</strong> Seaworthy export packing — wooden cases, end caps, waterproof wrapping — is a visible proxy for how a mill treats invisible things.</li>
</ul>
<h2>The economics, honestly</h2>
<p>With verification in place, buyers typically save 15–30% against Western mill pricing, even after inspection and freight. Without verification, the expected cost of one bad heat — rejected material, project delay, rework — exceeds years of savings. The checklist above is the difference between the two outcomes.</p>
<div class="callout"><strong>Our standing offer:</strong> apply all 8 points to us. Third-party inspection welcome at our cost on qualifying first orders; MTC issued pre-shipment; sample lengths available on every stock grade. <a href="about.html" style="color:var(--accent-dark);font-weight:700">Meet the team and facility →</a></div>
'''),
 'nickel-alloy-price-drivers': dict(
   cat='Buying Guides', date='2026-05-22', img='prod-sheets', read=6,
   title='What Drives Nickel Alloy Prices: LME Nickel, Molybdenum and the Surcharge System',
   desc='Why your quote moved 12% since last quarter — and how to time, hedge and structure nickel alloy purchases intelligently.',
   body='''
<p>Nickel alloy pricing confuses buyers because it moves on multiple clocks at once: the LME nickel price (daily), molybdenum and chromium (weekly/monthly), mill capacity (quarterly) and energy costs. Understanding the structure won't make alloys cheap — but it will make your quotes predictable and your timing smarter.</p>
<h2>The alloy surcharge mechanism</h2>
<p>Mills price most nickel alloys as a <strong>base price + alloy surcharge</strong>. The surcharge is a transparent formula: each element's percentage × its market price, summed monthly. When LME nickel moves, the surcharge moves. For a 60%-nickel alloy, roughly 60% of the metal value tracks the LME directly — which is why alloy prices feel volatile even when the mill's conversion cost is stable.</p>
<h2>The elements that actually move your quote</h2>
<ul>
<li><strong>Nickel (LME):</strong> the dominant driver for everything in this catalog. Historically the LME has swung between roughly $15,000 and $45,000/t in recent years — a 3× range that flows straight into pricing.</li>
<li><strong>Molybdenum:</strong> small percentages, big impact. C-276 at 16% Mo and 625 at 9% Mo feel every moly spike; Monel 400 (no Mo) doesn't.</li>
<li><strong>Chromium, iron, niobium, cobalt:</strong> secondary but real — niobium especially for 625/718.</li>
</ul>
<h2>Why high-alloy grades move more</h2>
<p>The more alloy content, the more of the price is raw material and the less is conversion cost. A doubling of nickel moves a Nickel 200 price far more than an Incoloy 800 price. This also explains why C-276 (nickel + moly + tungsten) can decouple from 625 (nickel + moly + niobium) when one element runs.</p>
<h2>Practical buying tactics</h2>
<ul>
<li><strong>Ask for quote validity windows.</strong> We hold quotes firm for a stated period tied to the surcharge month — use it to lock pricing during approval cycles.</li>
<li><strong>Time large orders to surcharge resets.</strong> Buying just after a downward monthly adjustment captures the fall immediately.</li>
<li><strong>Consider scheduled releases.</strong> For programs, lock a quantity with quarterly releases priced on a defined surcharge formula — you get budget predictability and we get production planning. Everyone wins.</li>
<li><strong>Compare total landed cost, not mill price.</strong> Freight, duty, inspection and lead-time risk belong in the comparison. A 3% cheaper quote with 4 extra weeks of lead time is usually more expensive.</li>
</ul>
<div class="callout"><strong>Transparent pricing:</strong> our quotes state the validity window and the pricing basis. If the market falls before your order ships, ask — we re-quote honestly. That's how 24-month customers are made.</div>
'''),
 'mtc-vs-coc-certificates': dict(
   cat='Quality & Standards', date='2026-05-15', img='qc-caliper', read=5,
   title='MTC vs. CoC: Why a Certificate of Conformance Is Not a Mill Test Certificate',
   desc='Three letters of difference, one lawsuit of consequence. What each document proves, what it doesn\'t, and which one your application requires.',
   body='''
<p>Every quarter, somewhere, a buyer discovers that the "certificate" backing their pressure-system material is a Certificate of Conformance — a one-line declaration — rather than a Mill Test Certificate with actual heat-specific results. The material may be fine. The legal position is not.</p>
<h2>What each document is</h2>
<ul>
<li><strong>CoC (Certificate of Conformance):</strong> the supplier's statement that the material "conforms" to the specification. No test results, no heat data, sometimes no heat number. Under EN 10204 it corresponds to type 2.1/2.2. It is a promise.</li>
<li><strong>MTC (Mill Test Certificate / Mill Test Report):</strong> the actual measured chemistry and mechanical properties of the specific heat your material came from, validated by the mill's independent inspection department (3.1) or a witnessed third party (3.2). It is evidence.</li>
</ul>
<h2>When a CoC is acceptable</h2>
<p>For non-critical, non-pressure, non-safety applications where the specification allows it — architectural uses, general fabrication, prototypes. Many buyers accept CoCs for commercial-grade material and the practice is legitimate <em>when everyone understands what they hold</em>.</p>
<h2>When it absolutely is not</h2>
<ul>
<li><strong>Pressure equipment</strong> under ASME, PED or GB codes — 3.1 is the floor; many EPC specs demand it contractually.</li>
<li><strong>Safety-critical service</strong> — subsea, aerospace, nuclear-adjacent: 3.2 witnessed is common.</li>
<li><strong>Anywhere failure analysis matters.</strong> If a part fails in service, the MTC is the document investigators reach for. A CoC tells them nothing and leaves you holding the liability.</li>
</ul>
<h2>The tell-tale signs on the document</h2>
<p>A real 3.1 MTC lists: heat number, full chemical analysis with measured values, mechanical test results (tensile, yield, elongation, hardness where specified), the standard and revision, product form and dimensions, and the inspection department's signature. If your document is missing measured values, it is not a 3.1 — whatever the filename says.</p>
<div class="callout"><strong>Our policy:</strong> EN 10204 3.1 MTC with actual heat-specific results on every order, issued before shipment — CoCs are not in our vocabulary. Third-party witnessed 3.2 available on request. <a href="blog-understanding-mtc-en-10204.html" style="color:var(--accent-dark);font-weight:700">How to audit an MTC →</a></div>
'''),
 'nickel-alloy-for-subsea-oil-gas': dict(
   cat='Industry Insights', date='2026-05-06', img='prod-pipes', read=7,
   title='Nickel Alloys for Subsea Oil & Gas: Where 625, 825 and 925 Earn Their Keep',
   desc='Three kilometers down, seawater outside and sour crude inside — the material decisions behind risers, umbilicals and downhole hardware.',
   body='''
<p>Subsea is the harshest mainstream service on Earth for metals: aerated seawater and biofouling on the outside, hot sour hydrocarbons with H₂S, CO₂ and chlorides on the inside, and a repair bill that starts with mobilizing a vessel. This is where nickel alloys stopped being a premium and became the default. Here's where each grade earns its place.</p>
<h2>Alloy 625: the subsea workhorse</h2>
<p>If one alloy defines subsea engineering, it's 625. Seawater-facing and structural: manifold piping, valve bodies, flange facings (as weld overlay), riser and jumper components, fasteners in splash zones. Its combination — PREN ≈ 51 against the seawater side, high strength without heat treatment, superb fatigue and weldability — has no economical rival. Weld-overlay of 625 onto low-alloy steel bodies is the industry's standard cost optimization: corrosion resistance exactly where needed, strength from the substrate.</p>
<h2>Alloy 825: the process-side answer</h2>
<p>Where the enemy is the produced fluid rather than the sea — hot, chloride-rich, mildly sour brines — 825's molybdenum-copper-titanium chemistry resists both chloride pitting and stress-corrosion cracking at a lower cost than 625. Common in flowlines, chemical-injection lines and downhole tubing for moderately sour wells.</p>
<h2>Alloy 925 and 718: the strength grades</h2>
<p>Downhole hardware — packers, safety valves, mandrels — needs yield strengths north of 700 MPa plus NACE MR0175/ISO 15156 sour-service compliance. Age-hardened 925 (an 825 derivative hardened with Ti/Al) and carefully conditioned 718 fill that slot. The critical word is "conditioned": sour service caps hardness and dictates heat treatment per NACE, and the MTC must show it. This is paperwork that prevents hydrogen-embrittlement failures.</p>
<h2>The specification traps we see</h2>
<ul>
<li>Calling "625" without the overlay thickness and dilution limits for clad components.</li>
<li>Omitting NACE MR0175 compliance for sour service — not all nickel alloys qualify in all conditions, and hardness limits are grade-specific.</li>
<li>Under-specifying fastener grade: a 625 flange with carbon-steel bolts is a corrosion battery waiting for seawater.</li>
<li>Skipping PMI verification on mixed shipments — one swapped heat number in a manifold is a multi-million-dollar failure mode.</li>
</ul>
<div class="callout"><strong>Subsea supply:</strong> we manufacture 625 and 825 pipe, fittings, flanges and bar with NACE-compliant options, 100% PMI, and EN 10204 3.2 witnessed inspection for critical orders. <a href="industry-oil-gas.html" style="color:var(--accent-dark);font-weight:700">Oil & gas capability →</a></div>
'''),
}

# Newest first in the index; merge batch 2 ahead of batch 1
ARTICLES = dict(list(B2.items()) + list(ARTICLES.items()))

for k, v in ARTICLES.items():
    render_article(k, v)
render_blog_index()
print('BLOG2 DONE:', len(ARTICLES), 'articles')
