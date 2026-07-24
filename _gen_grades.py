#!/usr/bin/env python3
"""Grade hub pages generator — one page per alloy grade (70+)."""
exec(open('/mnt/agents/output/app/_gen.py').read().split("# ── render product pages ──")[0])

# G(name, slug, uns, family, dens, chem, yield, tensile, temp, traits[], apps[], forms[], desc)
# Properties left None are omitted from the table (never invented).
def G(name, slug, uns, fam, dens, chem, y, t, temp, traits, apps, forms, desc):
    return dict(name=name, slug=slug, uns=uns, fam=fam, dens=dens, chem=chem, y=y, t=t,
                temp=temp, traits=traits, apps=apps, forms=forms, desc=desc)

MONEL = [
 G('Monel 400','monel-400','UNS N04400','Monel','8.80','Ni ≥ 63% · Cu 28–34% · Fe ≤ 2.5%','240 MPa','550 MPa','480 °C',
   ['Excellent seawater & brine resistance','Immune to chloride stress-corrosion cracking','Resists hydrofluoric acid','High ductility (~45% elongation)'],
   ['Seawater valves, pumps & propeller shafts','Marine piping & heat exchangers','HF acid alkylation units','Brine heaters & evaporators'],
   ['pipe','fitting','bar','sheet','wire'],
   'The classic Ni-Cu marine alloy — in continuous seawater service for over a century.'),
 G('Monel 401','monel-401','UNS N04401','Monel','8.89','Ni ~43% · Cu bal. · low Fe','—','—','—',
   ['Low Curie temperature variant','Good brazing & soldering behavior','Non-magnetic at room temperature'],
   ['Electronic components','Instrumentation parts','Brazed assemblies'],
   ['bar','wire'],
   'A lower-nickel Monel variant tuned for electronics and instrument applications.'),
 G('Monel 404','monel-404','UNS N04404','Monel','8.91','Ni ~55% · Cu bal. · very low Fe','—','—','—',
   ['Curie temperature near room temperature','Excellent for waveguide & electronic parts','Readily brazed'],
   ['Waveguides','Electronic devices','Instrument components'],
   ['bar','wire'],
   'Electronics-grade Monel with a deliberately low Curie point.'),
 G('Monel R-405','monel-r405','UNS N04405','Monel','8.80','Monel 400 base + controlled S','—','—','480 °C',
   ['Free-machining version of Monel 400','Sulfur addition improves chip breaking','Same corrosion resistance as 400'],
   ['Screw-machine parts','Valve stems & fittings','High-volume turned components'],
   ['bar','rod'],
   'The machinist\u2019s Monel — all of 400\u2019s corrosion resistance with free-cutting behavior.'),
 G('Monel K-500','monel-k500','UNS N05500','Monel','8.44','Ni ~66% · Cu ~29% · Al 2.3–3.15% · Ti 0.35–0.85%','690 MPa','965 MPa','480 °C',
   ['Age-hardened — ~3× the strength of Monel 400','Retains 400\u2019s seawater resistance','Non-magnetic to −100 °C','Excellent fatigue resistance'],
   ['Pump & propeller shafts','Subsea fasteners & springs','Valve stems','Doctor blades & scrapers'],
   ['bar','rod','wire','forging'],
   'Monel 400 plus aluminum and titanium — precipitation hardening delivers high strength without losing seawater performance.'),
 G('Monel 502','monel-502','UNS N05502','Monel','8.44','Ni ~65% · Cu ~28% · Al ~2.8%','—','—','—',
   ['Age-hardenable like K-500','Improved machinability over K-500'],
   ['Machined components needing age-hardened strength','Fasteners','Valve parts'],
   ['bar','rod'],
   'A machinable, age-hardenable Ni-Cu grade for precision components.'),
]

INCONEL = [
 G('Inconel 600','inconel-600','UNS N06600','Inconel','8.47','Ni ≥ 72% · Cr 14–17% · Fe 6–10%','240 MPa','655 MPa','1095 °C',
   ['Oxidation resistance to 1095 °C','Resists chloride-ion stress-corrosion cracking','Good carburization resistance','Non-magnetic'],
   ['Heat-treat furnaces & fixtures','Nuclear steam generators (historical)','Chemical & food processing','Electronic components'],
   ['pipe','bar','sheet','wire'],
   'The original high-nickel workhorse for furnace and oxidation service.'),
 G('Inconel 601','inconel-601','UNS N06601','Inconel','8.11','Ni 58–63% · Cr 21–25% · Al 1–1.7%','205 MPa','550 MPa','1150 °C',
   ['Aluminum addition forms a tenacious oxide scale','Outstanding cyclic oxidation resistance','Good carburization & nitriding resistance'],
   ['Radiant tubes','Furnace rollers & muffles','Catalyst support grids','Heat-treat baskets'],
   ['pipe','bar','sheet','wire'],
   '600 with aluminum — the standard for severe thermal-cycling furnace service.'),
 G('Inconel 601GC','inconel-601gc','UNS N06601 (GC)','Inconel','8.11','601 base · grain-controlled','—','—','1150 °C',
   ['Grain-size-controlled 601 variant','Optimized high-temperature fatigue life'],
   ['Industrial furnace components','Thermal processing fixtures'],
   ['pipe','bar','sheet'],
   'A grain-controlled variant of 601 for demanding furnace applications.'),
 G('Inconel 602CA','inconel-602ca','UNS N06025','Inconel','8.11','Ni ~63% · Cr ~25% · Al ~2.2% · Y ~0.1%','270 MPa','680 MPa','1200 °C',
   ['Yttrium-enhanced oxide scale adhesion','Best-in-class cyclic oxidation to 1200 °C','Excellent carburization resistance'],
   ['Radiant tubes for continuous furnaces','Calcining kilns','Automotive & steel heat treatment'],
   ['pipe','bar','sheet'],
   'The premium furnace alloy — micro-alloyed yttrium keeps the protective scale attached through thousands of cycles.'),
 G('Inconel 603XL','inconel-603xl','—','Inconel','—','Ni-Cr base · proprietary','—','—','—',
   ['High-temperature structural alloy','Oxidation & carburization resistant'],
   ['Furnace & thermal processing equipment'],
   ['bar','sheet'],
   'A proprietary high-temperature Inconel variant; specs confirmed per inquiry.'),
 G('Inconel 617','inconel-617','UNS N06617','Inconel','8.36','Ni ~53% · Cr ~22% · Co ~12.5% · Mo ~9%','300 MPa','750 MPa','1100 °C',
   ['Ni-Cr-Co-Mo for exceptional 1100 °C strength','Excellent oxidation & carburization resistance','Good weldability'],
   ['Gas turbine combustion cans & ducting','USC boiler superheaters','Petrochemical catalyst tubes'],
   ['pipe','bar','sheet','wire'],
   'Cobalt-strengthened for the hottest sections of turbines and advanced boilers.'),
 G('Inconel 625','inconel-625','UNS N06625','Inconel','8.44','Ni ≥ 58% · Cr 20–23% · Mo 8–10% · Nb+Ta 3.15–4.15%','414 MPa','827 MPa','982 °C',
   ['Niobium solid-solution strengthening — no heat treatment needed','Outstanding pitting & crevice corrosion resistance (PREN ≈ 51)','Immune to chloride stress-corrosion cracking','High fatigue strength'],
   ['Subsea umbilicals & flowlines','Marine exhaust & seawater systems','Aerospace ducting & exhausts','Chemical transfer lines'],
   ['pipe','fitting','bar','sheet','wire'],
   'The all-rounder: strength, corrosion resistance and fabricability in one alloy — the most specified nickel alloy in the world.'),
 G('Inconel 625LCF','inconel-625lcf','UNS N06626','Inconel','8.44','625 base · low-cycle-fatigue optimized','—','—','982 °C',
   ['Modified for superior low-cycle fatigue life','Same corrosion performance as 625'],
   ['Bellows & expansion joints','Aerospace ducting subject to thermal cycling'],
   ['sheet','strip'],
   'A 625 variant optimized for bellows and other fatigue-critical formed parts.'),
 G('Inconel 686','inconel-686','UNS N06686','Inconel','8.73','Ni ~59% · Cr ~20.5% · Mo ~16.3% · W ~3.8%','360 MPa','760 MPa','—',
   ['Single-phase Ni-Cr-Mo-W — exceptional all-round corrosion resistance','PREN ≈ 65','Resists mixed acid & halide media'],
   ['Flue-gas desulfurization','Waste incineration','Aggressive chemical processing'],
   ['pipe','sheet','bar','wire'],
   'A corrosion super-alloy bridging the Inconel and Hastelloy families.'),
 G('Inconel 690','inconel-690','UNS N06690','Inconel','8.19','Ni ~58% · Cr ~30% · Fe ~9%','240 MPa','585 MPa','—',
   ['Very high chromium for oxidizing acids & caustics','The standard for nuclear steam-generator tubing','Resists stress-corrosion cracking in primary water'],
   ['Nuclear steam generator tubes','Nitric acid service','Radioactive waste processing'],
   ['pipe','tube','bar','sheet'],
   'High-chromium grade developed for nuclear steam generators and oxidizing chemical service.'),
 G('Inconel 693','inconel-693','UNS N06693','Inconel','8.19','Ni ~61% · Cr ~29% · Al ~3.3%','—','—','—',
   ['Best-in-class metal-dusting resistance','High-Cr + Al oxide protection'],
   ['Syngas & petrochemical reformers','Metal-dusting-prone environments'],
   ['pipe','bar','sheet'],
   'Engineered specifically against metal dusting in high-carbon-activity gases.'),
 G('Inconel 706','inconel-706','UNS N09706','Inconel','8.05','Ni ~42% · Fe ~37% · Nb ~2.9%','—','—','700 °C',
   ['Precipitation-hardenable like 718, easier to forge','Good elevated-temperature strength'],
   ['Turbine discs & shafts','Large forged components'],
   ['bar','forging'],
   'A forgeable precipitation-hardened alloy for large turbine components.'),
 G('Inconel 718','inconel-718','UNS N07718','Inconel','8.19','Ni 50–55% · Cr 17–21% · Nb+Ta 4.75–5.5% · Mo 2.8–3.3% · Ti 0.65–1.15% · Al 0.2–0.8%','1035 MPa','1240 MPa','700 °C',
   ['Highest-strength nickel superalloy in common use','Age-hardenable (gamma double-prime)','Exceptional strength to 700 °C','Good weldability for a superalloy'],
   ['Turbine discs, shafts & blades','Aerospace fasteners','High-pressure valve bodies','Downhole tools'],
   ['bar','wire','sheet','forging'],
   'The aerospace superalloy — roughly half of all superalloy tonnage produced worldwide is 718.'),
 G('Inconel 718SPF','inconel-718spf','UNS N07718 (SPF)','Inconel','8.19','718 base · fine-grain SPF condition','—','—','700 °C',
   ['Fine-grained for superplastic forming','Complex shapes at lower tooling cost'],
   ['Superplastically formed aerospace panels','Complex sheet structures'],
   ['sheet'],
   'A fine-grain 718 condition enabling superplastic forming of complex aerospace shapes.'),
 G('Inconel 725','inconel-725','UNS N07725','Inconel','8.31','Ni ~57% · Cr ~21% · Mo ~8% · Nb ~3.4%','—','—','—',
   ['Age-hardenable 625 derivative','High strength plus 625-like corrosion resistance','Sour-service capable'],
   ['Sour gas wellhead & downhole parts','Marine fasteners','High-strength corrosion-resistant hardware'],
   ['bar','wire'],
   '625 chemistry made age-hardenable — strength of 718-class with marine corrosion resistance.'),
 G('Inconel 740H','inconel-740h','UNS N07740','Inconel','8.05','Ni ~50% · Cr ~25% · Co ~20% · Nb ~1.5%','—','—','760 °C+',
   ['Developed for advanced ultra-supercritical boilers','Coal-ash corrosion resistant','Age-hardenable'],
   ['A-USC superheater & reheater tubes','High-temperature headers'],
   ['pipe','tube'],
   'Purpose-built for the 760 °C steam conditions of next-generation power plants.'),
 G('Inconel X-750','inconel-x750','UNS N07750','Inconel','8.28','Ni ~70% · Cr ~15% · Ti ~2.5% · Al ~0.7% · Nb ~1%','635 MPa','1100 MPa','700 °C',
   ['Age-hardenable spring alloy','Excellent relaxation resistance to 700 °C','Good oxidation resistance'],
   ['Springs & fasteners','Gas turbine blades','Nuclear reactor internals'],
   ['wire','bar','sheet','strip'],
   'The standard age-hardened alloy for high-temperature springs and fasteners.'),
 G('Inconel 751','inconel-751','UNS N07751','Inconel','8.22','Ni ~70% · Cr ~15% · Ti ~2.3% · Al ~1.2%','—','—','870 °C',
   ['Higher Al/Ti than X-750 for greater hardness','Excellent hot hardness for exhaust valves'],
   ['Internal combustion engine exhaust valves','Rotors & hot fasteners'],
   ['bar','wire'],
   'The exhaust-valve alloy — hot hardness where valves meet 870 °C combustion gas.'),
 G('Inconel MA754','inconel-ma754','UNS N07754','Inconel','8.3','Ni ~78% · Cr ~20% · Y₂O₃ dispersion','—','—','1100 °C',
   ['Oxide-dispersion-strengthened (ODS)','Exceptional creep strength at very high temperature'],
   ['Turbine vanes','High-temperature guides'],
   ['bar'],
   'Mechanically alloyed ODS material — strength where conventional alloys creep.'),
 G('Inconel MA758','inconel-ma758','UNS N07758','Inconel','8.14','Ni-Cr base · Y₂O₃ dispersion · age-hardenable','—','—','—',
   ['ODS plus age hardening combined','Higher strength than MA754 at intermediate temperatures'],
   ['Turbine components','Extreme-service hardware'],
   ['bar'],
   'An ODS alloy that also accepts precipitation hardening — rare combination.'),
 G('Inconel 783','inconel-783','UNS N07783','Inconel','7.8','Ni-Co-Fe base · Al ~5.4% · Nb ~3%','—','—','700 °C',
   ['Low-expansion superalloy','Oxidation resistant without coatings'],
   ['Gas turbine casings & rings','Clearance-control components'],
   ['bar','forging'],
   'A controlled-expansion superalloy for tight turbine clearances.'),
]

INCOLOY = [
 G('Incoloy 800','incoloy-800','UNS N08800','Incoloy','8.02','Ni 30–35% · Cr 19–23% · Fe bal.','205 MPa','520 MPa','1100 °C',
   ['High-temperature strength & oxidation resistance','Resists carburization','Cost-efficient vs high-nickel grades'],
   ['Furnace parts & heat-treat equipment','Petrochemical process piping','Electric heating element sheaths'],
   ['pipe','tube','sheet','bar'],
   'The original Ni-Fe-Cr alloy — economical high-temperature service.'),
 G('Incoloy 800H','incoloy-800h','UNS N08810','Incoloy','8.02','800 base · controlled C 0.05–0.10% · Al+Ti ≤ 0.7%','170 MPa','450 MPa (creep-optimized)','1100 °C',
   ['Controlled carbon for creep-rupture strength','Coarse-grain high-temperature structure'],
   ['HRSG & reformer tubes','Ethylene cracker tubes','High-temperature pressure vessels'],
   ['pipe','tube','sheet','bar'],
   '800 with controlled carbon and grain size — the pressure-vessel code version for creep service.'),
 G('Incoloy 800HT','incoloy-800ht','UNS N08811','Incoloy','8.02','800H base · Al+Ti 0.85–1.2%','170 MPa','450 MPa (creep-optimized)','1100 °C',
   ['Highest creep strength of the 800 family','Long-term structural stability > 700 °C'],
   ['Steam-methane reformer tubes','High-temperature headers & manifolds'],
   ['pipe','tube','sheet','bar'],
   'The strongest creep variant of the 800 series — reformer industry standard.'),
 G('Incoloy 803','incoloy-803','UNS N08803','Incoloy','7.9','Ni ~33% · Cr ~27% · Fe bal.','—','—','—',
   ['Higher chromium than 800','Improved oxidation & sulfidation resistance'],
   ['Thermal processing equipment','Industrial furnace parts'],
   ['bar','sheet'],
   'A high-chromium member of the 800 family for severe furnace atmospheres.'),
 G('Incoloy 825','incoloy-825','UNS N08825','Incoloy','8.14','Ni 38–46% · Cr 19.5–23.5% · Mo 2.5–3.5% · Cu 1.5–3% · Ti 0.6–1.2%','241 MPa','586 MPa','540 °C',
   ['Copper addition resists sulfuric acid','Molybdenum resists pitting','Resists stress-corrosion cracking'],
   ['Sulfuric & phosphoric acid plants','Tank heating coils','Pollution control equipment','Offshore produced-water systems'],
   ['pipe','fitting','sheet','bar','wire'],
   'The acid-plant standard — sulfuric and phosphoric service worldwide.'),
 G('Incoloy 832','incoloy-832','UNS N08832','Incoloy','—','Ni-Fe-Cr base · proprietary','—','—','—',
   ['Specialized high-temperature corrosion resistance'],
   ['Industrial heating & furnace applications'],
   ['bar','sheet'],
   'A specialized Incoloy variant; specifications confirmed per inquiry.'),
 G('Incoloy 864','incoloy-864','UNS N08864','Incoloy','—','Ni-Fe-Cr base · proprietary','—','—','—',
   ['High-temperature structural alloy'],
   ['Thermal processing & furnace service'],
   ['bar','sheet'],
   'A specialized Incoloy variant; specifications confirmed per inquiry.'),
 G('Incoloy 890','incoloy-890','UNS N08890','Incoloy','—','Ni-Fe-Cr base · proprietary','—','—','—',
   ['High-temperature corrosion-resistant alloy'],
   ['Furnace & petrochemical service'],
   ['bar','sheet'],
   'A specialized Incoloy variant; specifications confirmed per inquiry.'),
 G('Incoloy 903','incoloy-903','UNS N19903','Incoloy','8.1','Ni ~38% · Fe-Co bal. · Nb ~3%','—','—','650 °C',
   ['Controlled low thermal expansion','Age-hardenable high strength'],
   ['Aerospace structural components','Precision tooling for hot service'],
   ['bar','sheet','wire'],
   'A low-expansion superalloy for dimensionally stable hot structures.'),
 G('Incoloy 907','incoloy-907','UNS N19907','Incoloy','8.2','Ni-Fe-Co base · Nb ~4.7%','—','—','650 °C',
   ['Low expansion plus improved stress-rupture life'],
   ['Gas turbine rings & casings','Clearance-critical aerospace parts'],
   ['bar','forging'],
   'Controlled-expansion alloy with enhanced rupture life for turbine structures.'),
 G('Incoloy 908','incoloy-908','UNS N19908','Incoloy','8.2','Ni-Fe-Co base · Nb ~3%','—','—','—',
   ['Low-expansion superalloy developed for superconductor sheathing'],
   ['Superconducting magnet structures','Cryogenic-to-hot precision structures'],
   ['bar','sheet'],
   'Developed for Nb₃Sn superconductor conduit — precise expansion match.'),
 G('Incoloy 909','incoloy-909','UNS N19909','Incoloy','8.2','Ni-Fe-Co base · Nb+Ti','—','—','650 °C',
   ['Low expansion with high strength & toughness','Resists thermal fatigue'],
   ['Rocket engine components','Turbine seals & rings'],
   ['bar','forging'],
   'A strong, tough low-expansion alloy for demanding aerospace structures.'),
 G('Incoloy 925','incoloy-925','UNS N09925','Incoloy','8.08','Ni ~44% · Cr ~21% · Mo ~3% · Ti ~2% · Cu ~1.8%','810 MPa','1170 MPa (aged)','540 °C',
   ['Age-hardenable 825 derivative','High strength plus acid resistance','NACE sour-service capable'],
   ['Sour gas downhole components','Valves & hangers','High-strength acid-service hardware'],
   ['bar','wire'],
   '825 with titanium for age hardening — strength where acids meet pressure.'),
 G('Incoloy 926','incoloy-926','UNS N08926','Incoloy','8.1','Ni ~25% · Cr ~21% · Mo ~6.5% · N ~0.2%','295 MPa','650 MPa','—',
   ['Super-austenitic with 6.5% Mo + nitrogen','PREN ≈ 47 — seawater & chloride resistant','Cost-effective vs nickel-base alloys'],
   ['Seawater systems & desalination','FGD components','Pulp & paper bleach plants'],
   ['pipe','sheet','bar','wire'],
   'A super-austenitic bridge between stainless and nickel alloys — strong chloride performance at lower cost.'),
 G('Incoloy 945','incoloy-945','UNS N09945','Incoloy','8.2','Ni ~50% · Cr ~21% · Mo ~3.5% · Nb ~2.5%','—','—','—',
   ['Age-hardenable high-strength corrosion alloy','Sour-service NACE compliant'],
   ['Deep sour-gas well components','High-pressure high-temperature hardware'],
   ['bar','wire'],
   'A modern age-hardenable alloy for extreme HPHT sour wells.'),
 G('Incoloy 945X','incoloy-945x','UNS N09946','Incoloy','8.2','945 base · enhanced','—','—','—',
   ['Enhanced version of 945','Improved ductility & toughness'],
   ['Sour-service fasteners','HPHT well hardware'],
   ['bar','wire'],
   'An enhanced-ductility development of 945 for critical fasteners.'),
 G('Incoloy MA956','incoloy-ma956','UNS S67956','Incoloy','7.2','Fe ~74% · Cr ~20% · Al ~4.5% · Y₂O₃ dispersion','—','—','1300 °C',
   ['Oxide-dispersion-strengthened Fe-Cr-Al','Exceptional oxidation resistance to 1300 °C'],
   ['Furnace & kiln components','High-temperature fixtures'],
   ['bar','sheet','wire'],
   'An iron-base ODS alloy for the most extreme oxidizing heat.'),
 G('Alloy A-286','alloy-a286','UNS S66286','Incoloy','7.94','Ni ~26% · Cr ~15% · Fe bal. · Ti ~2% · Mo ~1.3%','590 MPa','900 MPa (aged)','700 °C',
   ['Iron-based age-hardenable superalloy','High strength to 700 °C at lower cost than 718','Excellent notch ductility'],
   ['Jet engine fasteners & rotors','Turbocharger components','High-temperature bolting'],
   ['bar','wire','sheet'],
   'The workhorse iron-nickel superalloy — 718 performance class at a friendlier price.'),
]

HASTELLOY = [
 G('Hastelloy B','hastelloy-b','UNS N10001','Hastelloy','9.24','Ni ~65% · Mo ~28% · Fe ~5%','—','—','—',
   ['Original Ni-Mo reducing-acid alloy','Resists hydrochloric acid at all concentrations'],
   ['HCl service equipment','Reducing chemical processing'],
   ['pipe','bar','sheet'],
   'The original nickel-molybdenum alloy for hydrochloric acid service.'),
 G('Hastelloy B-2','hastelloy-b2','UNS N10665','Hastelloy','9.22','Ni ~69% · Mo ~28% · Fe ≤ 2% · Cr ≤ 1%','417 MPa','895 MPa','—',
   ['Reduced Fe/Cr vs B for better fabricability','Outstanding in reducing HCl, H₂SO₄, H₃PO₄'],
   ['Hydrochloric acid plants','Reducing-acid reactors'],
   ['pipe','bar','sheet'],
   'The fabricable Ni-Mo alloy for severe reducing acids.'),
 G('Hastelloy B-3','hastelloy-b3','UNS N10675','Hastelloy','9.22','Ni ~68% · Mo ~28.5% · Cr ~1.5% · Fe ~1.5%','417 MPa','895 MPa','—',
   ['Improved thermal stability over B-2','Better fabrication & service reliability in reducing acids'],
   ['HCl & reducing-acid service','Reactor vessels & piping'],
   ['pipe','bar','sheet'],
   'B-2 refined — same reducing-acid performance with better manufacturing stability.'),
 G('Hastelloy C','hastelloy-c','UNS N10002','Hastelloy','8.94','Ni ~59% · Mo ~16% · Cr ~16% · W ~4%','—','—','—',
   ['Original Ni-Cr-Mo corrosion alloy','Historic predecessor of C-276'],
   ['Severe chemical service (legacy equipment)'],
   ['pipe','bar','sheet'],
   'The original C-type alloy; C-276 is its modern low-carbon successor.'),
 G('Hastelloy C-4','hastelloy-c4','UNS N06455','Hastelloy','8.64','Ni ~65% · Mo ~16% · Cr ~16% · very low C','355 MPa','790 MPa','—',
   ['Exceptional thermal stability — resists sensitization','Good for as-welded service'],
   ['Chemical reactors used as-welded','Hot corrosive service'],
   ['pipe','sheet','bar'],
   'A thermally stable C-type that shrugs off welding heat.'),
 G('Hastelloy C-22','hastelloy-c22','UNS N06022','Hastelloy','8.69','Ni ~56% · Cr ~22% · Mo ~13% · W ~3%','355 MPa','760 MPa','—',
   ['Higher chromium than C-276 — better oxidizing-media resistance','PREN ≈ 65','Versatile across mixed streams'],
   ['Chloride process streams','Bleach plants','Pollution control'],
   ['pipe','fitting','sheet','wire'],
   'The oxidizing-side C-type — first choice when streams alternate between oxidizing and reducing.'),
 G('Hastelloy C-22HS','hastelloy-c22hs','UNS N07022','Hastelloy','8.7','C-22 base · age-hardenable','—','—','—',
   ['Age-hardenable C-22 derivative','Double the strength with similar corrosion resistance'],
   ['High-strength corrosion-resistant shafts & fasteners'],
   ['bar','wire'],
   'C-22 chemistry made hardenable — corrosion resistance at high strength.'),
 G('Hastelloy C-276','hastelloy-c276','UNS N10276','Hastelloy','8.89','Ni bal. · Mo 15–17% · Cr 14.5–16.5% · W 3–4.5% · Fe 4–7%','355 MPa','790 MPa','1040 °C',
   ['The universal corrosion alloy — oxidizing AND reducing media','PREN ≈ 68, pitting & crevice immune','Resists wet chlorine & hypochlorites','Excellent fabricability'],
   ['FGD scrubbers & stack liners','Chemical reactors & piping','Bleach & chlor-alkali plants','Waste treatment'],
   ['pipe','fitting','sheet','bar','wire'],
   'The default answer when nothing else survives — the most specified corrosion alloy in chemical processing.'),
 G('Hastelloy C-2000','hastelloy-c2000','UNS N06200','Hastelloy','8.5','Ni ~59% · Cr ~23% · Mo ~16% · Cu ~1.6%','360 MPa','790 MPa','—',
   ['Copper addition boosts sulfuric-acid resistance','Outstanding across the widest media range of any C-type'],
   ['Mixed-acid plants','Pharmaceutical processing','Versatile chemical service'],
   ['pipe','fitting','sheet','wire'],
   'The most versatile C-type — copper-bearing for sulfuric service on top of full C-22 capability.'),
 G('Hastelloy G-3','hastelloy-g3','UNS N06985','Hastelloy','8.14','Ni ~44% · Cr ~22% · Mo ~7% · Cu ~2%','—','—','—',
   ['Improved G — phosphoric & sulfuric service','Resists weld-zone corrosion'],
   ['Phosphoric acid plants','Fertilizer production','Sour gas service'],
   ['pipe','sheet','bar'],
   'The phosphate-industry standard with improved weldability over the original G.'),
 G('Hastelloy G-30','hastelloy-g30','UNS N06030','Hastelloy','8.22','Ni ~43% · Cr ~30% · Mo ~5.5% · Cu ~2% · W ~2.5%','—','—','—',
   ['Very high chromium — exceptional in phosphoric acid & oxidizing media','Resists fertilizer-plant corrosion'],
   ['Phosphoric acid evaporators','Fertilizer plants','Mixed-acid service'],
   ['pipe','sheet','bar','wire'],
   'High-chromium G-type — the phosphoric acid specialist.'),
 G('Hastelloy G-35','hastelloy-g35','UNS N06035','Hastelloy','8.18','Ni ~50% · Cr ~33% · Mo ~8%','—','—','—',
   ['Developed for wet-process phosphoric acid','Excellent in oxidizing acids with halides'],
   ['Phosphoric acid production','Flue-gas scrubbers'],
   ['pipe','sheet','bar'],
   'An improved G-30-class alloy for the harshest fertilizer-plant conditions.'),
 G('Hastelloy N','hastelloy-n','UNS N10003','Hastelloy','8.86','Ni ~71% · Mo ~16% · Cr ~7%','—','—','—',
   ['Designed for molten fluoride salts','Good high-temperature strength'],
   ['Molten-salt reactor systems','High-temperature salt handling'],
   ['pipe','bar','sheet'],
   'Born for the molten-salt reactor program — fluoride-salt corrosion specialist.'),
 G('Hastelloy S','hastelloy-s','UNS N06635','Hastelloy','8.75','Ni ~67% · Cr ~16% · Mo ~15%','—','—','1095 °C',
   ['Excellent high-temperature strength & thermal stability','Low thermal expansion'],
   ['Gas turbine hot-section parts','Heating furnace components'],
   ['bar','sheet'],
   'A high-temperature Hastelloy for turbine and furnace heat.'),
 G('Hastelloy W','hastelloy-w','UNS N10004','Hastelloy','8.8','Ni ~63% · Mo ~24% · Cr ~5% · Fe ~6%','—','—','—',
   ['Primarily a welding filler alloy','Joins dissimilar nickel & iron alloys'],
   ['Dissimilar-metal weld filler','Overlay welding'],
   ['wire'],
   'Best known as filler metal for dissimilar nickel-alloy joints.'),
 G('Hastelloy X','hastelloy-x','UNS N06002','Hastelloy','8.22','Ni ~47% · Cr ~22% · Mo ~9% · Fe ~18% · Co ~1.5%','340 MPa','760 MPa','1200 °C',
   ['Outstanding oxidation resistance to 1200 °C','Exceptional fabricability for a superalloy','Good carburization & nitriding resistance'],
   ['Gas turbine combustion zones','Industrial furnace parts','Afterburners & tailpipes'],
   ['bar','sheet','wire'],
   'The fabricable high-temperature alloy — combustion sections worldwide.'),
]

SPECIALTY = [
 G('Alloy 20','alloy-20','UNS N08020','Specialty','8.08','Ni ~33% · Cr ~20% · Cu ~3.5% · Mo ~2.5% · Nb ~0.5%','241 MPa','550 MPa','—',
   ['Copper + niobium for sulfuric-acid resistance','Resists stress-corrosion cracking'],
   ['Sulfuric acid plants','Chemical & pharmaceutical processing','Food & dye production'],
   ['pipe','bar','sheet','wire'],
   'Carpenter 20 — the sulfuric-acid classic between stainless and nickel alloys.'),
 G('Alloy 28','alloy-28','UNS N08028','Specialty','8.0','Ni ~31% · Cr ~27% · Mo ~3.5% · Cu ~1%','—','—','—',
   ['High-Cr super-austenitic','Resists phosphoric & mixed acids plus chlorides'],
   ['Phosphoric acid evaporators','Sour-gas tubing','Seawater coolers'],
   ['pipe','sheet','bar'],
   'A super-austenitic for mixed acid-chloride service.'),
 G('Alloy DS','alloy-ds','UNS N08330 (DS)','Specialty','8.0','Ni ~36% · Cr ~18% · Si ~1.2%','—','—','—',
   ['Silicon-enhanced heat resistance','Resists carburizing & oxidizing atmospheres'],
   ['Furnace fixtures & muffles','Heat-treat equipment'],
   ['bar','sheet','wire'],
   'A silicon-bearing heat-resistant alloy for furnace atmospheres.'),
 G('Alloy 330','alloy-330','UNS N08330','Specialty','8.0','Ni ~36% · Cr ~18% · Si ~1%','205 MPa','585 MPa','1150 °C',
   ['Classic heat-resistant Ni-Fe-Cr','Resists oxidation & carburization to 1150 °C','Good thermal-fatigue resistance'],
   ['Furnace muffles & retorts','Heat-treat baskets & fixtures','Radiant tubes'],
   ['pipe','bar','sheet','wire'],
   'The furnace-industry veteran for cyclic high-temperature service.'),
 G('Alloy 25-6HN','alloy-25-6hn','UNS N08367 (6Mo class)','Specialty','8.06','Ni ~25% · Cr ~21% · Mo ~6.5% · N ~0.2%','310 MPa','690 MPa','—',
   ['6Mo super-austenitic with nitrogen','PREN ≈ 47 — severe seawater & chloride service'],
   ['Desalination plants','Offshore seawater systems','FGD absorbers'],
   ['pipe','sheet','bar','wire'],
   'The 6% molybdenum super-austenitic — AL-6XN-class chloride performance.'),
 G('Alloy 27-7MO','alloy-27-7mo','UNS S31277','Specialty','8.0','Ni ~27% · Cr ~22% · Mo ~7% · N ~0.35%','360 MPa','770 MPa','—',
   ['7Mo + high nitrogen super-austenitic','PREN ≈ 54 — approaches nickel-alloy corrosion resistance'],
   ['Severe FGD & scrubber service','Chloride-rich chemical streams'],
   ['pipe','sheet','bar'],
   'The strongest super-austenitic — near-625 corrosion resistance at lower nickel cost.'),
 G('Nickel 200','nickel-200','UNS N02200','Pure Nickel','8.90','Ni ≥ 99.0%','148 MPa','462 MPa','600 °C',
   ['Commercially pure nickel','Excellent in caustic soda & alkaline media','High thermal & electrical conductivity','Magnetic'],
   ['Caustic production & handling','Food processing','Electronic & battery components'],
   ['pipe','bar','sheet','wire'],
   'Pure nickel — the caustic-service standard.'),
 G('Nickel 201','nickel-201','UNS N02201','Pure Nickel','8.90','Ni ≥ 99.0% · C ≤ 0.02%','103 MPa','403 MPa','600 °C',
   ['Low-carbon Nickel 200 for service above 315 °C','Prevents graphitic embrittlement'],
   ['High-temperature caustic service','Caustic evaporators'],
   ['pipe','bar','sheet','wire'],
   'Low-carbon pure nickel for hot caustic duty.'),
]

FAMILIES = [('Monel®', MONEL), ('Inconel®', INCONEL), ('Incoloy®', INCOLOY), ('Hastelloy®', HASTELLOY), ('Specialty & Pure Nickel', SPECIALTY)]
ALL_GRADES = [g for _, gs in FAMILIES for g in gs]
print('grades in DB:', len(ALL_GRADES))

FORM_LABEL = {'pipe':'Pipes & Tubes','fitting':'Fittings & Flanges','bar':'Bars & Rods','sheet':'Sheets & Plates','wire':'Wires & Electrodes','rod':'Bars & Rods','tube':'Pipes & Tubes','strip':'Sheets & Plates','forging':'Forgings & Custom'}
FORM_LINK = {'pipe':'product.html','fitting':'fittings.html','bar':'bars.html','rod':'bars.html','sheet':'sheets.html','strip':'sheets.html','wire':'wires.html','tube':'welded-pipe.html','forging':'categories.html#custom'}

# ─────────────────────────── renderers ───────────────────────────
def grade_schema(g):
    return json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Grades","item":f"{BASE}/grades.html"},
        {"@type":"ListItem","position":3,"name":g['name'],"item":f"{BASE}/grade-{g['slug']}.html"}]},
      {"@type":"Product","name":g['name'],
       "description":f"{g['name']} ({g['uns']}) — {g['desc']} Supplied by TrueGrade Metals with EN 10204 3.1 MTC.",
       "brand":{"@type":"Brand","name":"TrueGrade Metals"},
       "material":f"{g['name']} ({g['uns']})","category":f"{g['fam']} nickel alloy",
       "url":f"{BASE}/grade-{g['slug']}.html","image":f"{BASE}/assets/prod-bars.jpg",
       "offers":{"@type":"Offer","availability":"https://schema.org/InStock","priceCurrency":"USD","price":"0","description":"Request quotation — response within 24 hours"}},
      {"@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":f"What forms is {g['name']} available in?",
         "acceptedAnswer":{"@type":"Answer","text":f"{g['name']} is supplied as {', '.join(sorted(set(FORM_LABEL[f] for f in g['forms'])))}, plus custom forms on request. Every heat ships with EN 10204 3.1 MTC."}},
        {"@type":"Question","name":f"What is {g['name']} used for?",
         "acceptedAnswer":{"@type":"Answer","text":'Typical applications: ' + '; '.join(g['apps'][:3]) + '.'}}]}
    ]}, indent=2)

def render_grade(g):
    fam_grades = dict(FAMILIES)
    fam_label = next(fl for fl, gs in FAMILIES for gg in gs if gg is g)
    siblings = [gg for fl, gs in FAMILIES for gg in gs if fl == fam_label and gg is not g][:6]

    props = []
    if g['uns'] and g['uns'] != '—': props.append(('UNS number', g['uns'].replace('UNS ','')))
    props.append(('Family', fam_label.replace('®','')))
    if g['chem'] != '—': props.append(('Nominal chemistry', g['chem']))
    if g['y'] != '—': props.append(('Min. yield strength', g['y']))
    if g['t'] != '—': props.append(('Min. tensile strength', g['t']))
    if g['temp'] != '—': props.append(('Max service temperature', g['temp']))
    if g['dens'] != '—': props.append(('Density', g['dens'] + ' g/cm³'))
    prop_rows = ''.join(f'<tr><td>{E(k)}</td><td>{E(v)}</td></tr>' for k,v in props)

    traits = ''.join(f'<li>{CHECK}<span>{E(t)}</span></li>' for t in g['traits'])
    apps = ''.join(f'<div class="card app-card reveal"><p style="margin:0">{E(a)}</p></div>' for a in g['apps'])
    form_chips = ''.join(f'<a href="{FORM_LINK[f]}">{E(FORM_LABEL[f])}</a>' for f in dict.fromkeys(g['forms']))
    rel = ''.join(f'<a href="grade-{gg["slug"]}.html">{E(gg["name"])}</a>' for gg in siblings)

    headline_props = []
    if g['y'] != '—': headline_props.append(('Min. yield', g['y']))
    if g['t'] != '—': headline_props.append(('Min. tensile', g['t']))
    if g['temp'] != '—': headline_props.append(('Max service', g['temp']))
    if g['uns'] and g['uns'] != '—': headline_props.append(('UNS', g['uns'].replace('UNS ','')))
    specs = ''.join(f'<div class="spec"><strong>{E(v)}</strong><span>{E(k)}</span></div>' for k,v in headline_props[:4])

    page_title = f"{g['name']} ({g['uns'].replace('UNS ','') if g['uns']!='—' else g['fam'] + ' alloy'}) — Properties, Forms & Supplier | TrueGrade Metals"
    desc = f"{g['name']} {g['uns']} — {g['desc']} Available as {', '.join(sorted(set(FORM_LABEL[f] for f in g['forms'])))} with EN 10204 3.1 MTC. Quote in 24 hours."

    body = f'''
{breadcrumb([('Home','index.html'),('Grades','grades.html'),(g['name'],None)])}
<section class="p-hero">
  <div class="container">
    <div class="p-hero-grid">
      <div class="reveal in">
        <div class="eyebrow">{E(fam_label)} · {E(g['fam'])} family</div>
        <h1>{E(g['name'])}, <em>certified and in stock.</em></h1>
        <p class="p-hero-sub"><strong>{E(g['uns'])}</strong> — {E(g['desc'])}</p>
        <div class="p-hero-actions">
          <a href="index.html#rfq" class="btn btn-primary btn-lg">Quote {E(g['name'])} →</a>
          <a href="tools.html#compare" class="btn btn-ghost btn-lg">Compare grades</a>
        </div>
        <div class="p-hero-trustpills">
          <span class="trust-pill"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 12l5 5L20 6"/></svg> EN 10204 3.1 MTC</span>
          <span class="trust-pill"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 12l5 5L20 6"/></svg> 24h quote SLA</span>
        </div>
        <div class="spec-grid">{specs}</div>
      </div>
      <div class="reveal in d1">
        <div class="hero-photo">
          <img src="assets/prod-bars.jpg" alt="{E(g['name'])} {E(g['fam'])} alloy — TrueGrade Metals">
          <div class="hero-photo-badge"><span style="font-family:var(--font-mono);font-size:.7rem;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:.08em">{E(g['uns'])}</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Material data</div>
      <h2>{E(g['name'])} — properties at a glance.</h2>
      <p>Nominal published values, annealed condition. Certified heat lots ship with actual MTC values.</p>
    </div>
    <div class="table-scroll reveal"><table class="data-table">
      <thead><tr><th>Property</th><th>Value</th></tr></thead>
      <tbody>{prop_rows}</tbody>
    </table></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Characteristics</div>
      <h2>What {E(g['name'])} does best.</h2>
    </div>
    <ul class="feat-list">{traits}</ul>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Applications</div>
      <h2>Where {E(g['name'])} works.</h2>
    </div>
    <div class="app-grid">{apps}</div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head reveal"><div class="eyebrow">Availability</div>
      <h2>Forms we supply in {E(g['name'])}.</h2>
      <p>All forms consolidated into one PO with matching heats and one MTC package.</p>
    </div>
    <div class="grade-chips reveal">{form_chips}</div>
    <div style="margin-top:40px">
      <div class="eyebrow">Related grades</div>
      <div class="grade-chips reveal">{rel}</div>
    </div>
  </div>
</section>

{LEAD_BLOCK}

{cta_band(f'Quote {E(g["name"])} in 24 hours.', 'Form, dimensions, quantity, standard — that is all we need. A named metallurgist replies with pricing, lead time and MTC sample.')}
'''
    write(f"grade-{g['slug']}.html", body, page_title, desc, grade_schema(g), active='grades')

for g in ALL_GRADES:
    render_grade(g)

# ── grades index ──
def render_grades_index():
    fam_sections = ''
    for fl, gs in FAMILIES:
        chips = ''.join(f'<a href="grade-{g["slug"]}.html" title="{E(g["uns"])}">{E(g["name"])}</a>' for g in gs)
        fam_sections += f'''<div class="reveal" style="margin-bottom:36px">
          <h3 style="font-size:1.3rem;margin-bottom:4px">{E(fl)}</h3>
          <p style="font-size:.86rem;color:var(--muted);margin:0 0 14px">{len(gs)} grades</p>
          <div class="grade-chips">{chips}</div>
        </div>'''
    schema = json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Grades","item":f"{BASE}/grades.html"}]},
      {"@type":"ItemList","name":"Nickel Alloy Grades","numberOfItems":len(ALL_GRADES),
       "itemListElement":[{"@type":"ListItem","position":i+1,"name":g['name'],"url":f"{BASE}/grade-{g['slug']}.html"} for i,g in enumerate(ALL_GRADES)]}
    ]}, indent=2)
    body = f'''
{breadcrumb([('Home','index.html'),('Grades',None)])}
<section class="p-hero" style="padding-bottom:40px">
  <div class="container">
    <div class="reveal in" style="max-width:760px">
      <div class="eyebrow">Grade library</div>
      <h1>{len(ALL_GRADES)} grades. <em>One quality system.</em></h1>
      <p class="p-hero-sub">Every grade page carries chemistry, mechanical properties, characteristics, applications and available forms — with EN 10204 3.1 certification on every heat. Can't find yours? <a href="index.html#rfq" style="color:var(--accent);font-weight:600">Ask — we likely make it.</a></p>
      <div class="p-hero-actions">
        <a href="tools.html#compare" class="btn btn-dark btn-lg">Compare two grades →</a>
        <a href="assets/grade-selection-guide.pdf" class="btn btn-ghost btn-lg">↓ Selection guide (PDF)</a>
      </div>
    </div>
  </div>
</section>
<section class="section section-white" style="padding-top:56px">
  <div class="container">{fam_sections}</div>
</section>
{cta_band('Not sure which grade fits your service?', 'Send medium, temperature, pressure and pH — a metallurgist verifies the grade free of charge within 24 hours.')}
'''
    write('grades.html', body, f'Nickel Alloy Grades — {len(ALL_GRADES)} Grades in Stock | TrueGrade Metals',
          f'{len(ALL_GRADES)} nickel alloy grades: Monel, Inconel, Incoloy, Hastelloy and specialty alloys. Chemistry, properties, applications and forms for each. EN 10204 3.1 MTC, quote in 24 hours.',
          schema, active='grades')

render_grades_index()
print('GRADE PAGES DONE:', len(ALL_GRADES) + 1)
