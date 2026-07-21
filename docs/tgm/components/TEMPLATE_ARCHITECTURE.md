# TrueGrade Metals — Website Information Architecture & Template Strategy

> Discovery output for Phase 3. This document maps every page type, identifies reusable templates, and defines the minimum template set needed to turn the site into one coherent enterprise platform.
>
> Companion doc: [`DESIGN_SYSTEM.md`](./DESIGN_SYSTEM.md)

---

## 1. Discovery summary

| Metric | Value |
|---|---|
| Total HTML pages in `/tgm/` | **1,583** |
| Pages using global nav/footer | **1,581** (all except `tgm/index.html` redirect) |
| Pages using `tgm-core.js` | **1,580** |
| Legacy `<header>` / `<footer id="footer-nav">` blocks | **0** |
| Aeether / old email references | **0** |

The site is now structurally unified at the chrome level (header + footer). The next stage is to unify the **content-area templates** so every page of the same type shares one layout, component order, and design language.

---

## 2. Page inventory & page types

| # | Page type | Count | URL pattern | Canonical example | Current template | Status |
|---|---|---|---|---|---|---|
| 1 | **Homepage** | 1 | `/index.html` | `/index.html` | Inline / bespoke | ✅ Global chrome only; content area is custom |
| 2 | **Product form category** | 6 | `/tgm/nickel-alloy*.html` | `/tgm/nickel-alloy-pipes.html` | `category-page-template.html` | ✅ 1 converted; 5 legacy remain |
| 3 | **Product detail** | 1,270 | `/tgm/products/*.html` | `/tgm/products/nickel-alloy-seamless-pipe-tube.html` | `product-page-template.html` | ✅ 1 converted; 1,269 legacy remain |
| 4 | **Grade / material family** | 106 | `/tgm/grades/*.html` | `/tgm/grades/400.html` | Inline / bespoke | ⚠️ Old layout, needs template |
| 5 | **Industry / solution** | 12 | `/tgm/solutions/*.html` | `/tgm/solutions/aerospace.html` | Inline / bespoke | ⚠️ Old layout, needs template |
| 6 | **Engineering tool** | 9 | `/tgm/tools/*.html` | `/tgm/tools/nickel-alloy-weight-calculator.html` | Inline / bespoke | ⚠️ Old layout, needs template |
| 7 | **Media article** | 145 | `/tgm/media/media-*/media.html` | `/tgm/media/media-1/media.html` | Inline / bespoke | ⚠️ Old layout, needs article template |
| 8 | **Media category index** | 6 | `/tgm/media/*/index.html` | `/tgm/media/alloy-knowledge/index.html` | Inline / bespoke | ⚠️ Old layout |
| 9 | **Hub / listing page** | 6 | `/tgm/{grades,solutions,tools,media,gallery,blog}.html` | `/tgm/blog.html` | Inline / bespoke | ⚠️ Mixed old layouts |
| 10 | **Gallery page** | 5 | `/tgm/gallery/*.html` | `/tgm/gallery/pipe-tube.html` | Inline / bespoke | ⚠️ Old layout |
| 11 | **Company / legal** | 5 | `/tgm/{about-us,contact-us,disclaimer,privacy-policy,sitemap}.html` | `/tgm/about-us.html` | Inline / bespoke | ⚠️ Old layout |
| 12 | **Redirect** | 1 | `/tgm/index.html` | `/tgm/index.html` | N/A | ✅ Redirect only |

**Total accounted for:** 1,582 pages. The remainder are component/template files in `/tgm/components/`.

---

## 3. URL architecture

```
/                              → Homepage
/tgm/index.html                → Redirect to /

/tgm/nickel-alloy.html         → Master product category
/tgm/nickel-alloy-pipes.html   → Product-form category (Pipes & Tubes)
/tgm/nickel-alloy-fittings.html
/tgm/nickel-alloy-bars.html
/tgm/nickel-alloy-sheets.html
/tgm/nickel-alloy-wires.html

/tgm/products/*.html           → Product detail pages (1,270)
/tgm/grades/*.html             → Grade / material-family pages (106)
/tgm/solutions/*.html          → Industry / application pages (12)
/tgm/tools/*.html              → Engineering calculators & price pages (9)

/tgm/media/*/index.html        → Media category hubs (6)
/tgm/media/media-*/media.html  → Media articles (145)
/tgm/blog.html                 → Blog index
/tgm/blog-1.html … blog-8.html → Blog pagination

/tgm/gallery.html              → Gallery hub
/tgm/gallery/*.html            → Gallery sub-pages (5)

/tgm/about-us.html             → Company
/tgm/contact-us.html           → Contact / RFQ
/tgm/disclaimer.html           → Legal
/tgm/privacy-policy.html       → Legal
/tgm/sitemap.html              → SEO sitemap page
```

### Findings
- The global nav **Industries mega menu** currently links every industry to `/tgm/solutions.html` instead of the dedicated `/tgm/solutions/{slug}.html` pages. This should be corrected as part of template rollout.
- Media article breadcrumbs point to `/tgm/blog.html`, which groups articles with blog pagination. Consider whether `/tgm/media.html` or `/tgm/blog.html` should be the canonical parent.

---

## 4. Master template

Every page type should inherit from one **master template** that contains only the global chrome and a content placeholder.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- GTM, charset, viewport, SEO meta -->
  <!-- Fonts + tgm-tokens.css -->
  <!-- Page-type CSS -->
</head>
<body>
  <!-- Global nav -->
  <div id="global-nav" style="min-height:122px"></div>
  <script src="/tgm/components/global-nav.js"></script>

  <main id="main-content">
    <!-- Page-type template content -->
  </main>

  <!-- Global footer -->
  <div id="global-footer"></div>
  <script src="/tgm/components/global-footer.js"></script>
  <script src="/tgm/tgm-core.js"></script>
  <!-- Page-type JS -->
</body>
</html>
```

### Known deviations to fix
- `index.html` loads components with relative paths (`tgm/components/global-nav.js`) and does not load `tgm-core.js`.
- `tgm/index.html` is a redirect; no content.

---

## 5. Page-type templates & component mapping

### 5.1 Product form category template
**Canonical:** `/tgm/nickel-alloy-pipes.html`  
**Files:** `category-page-template.html`, `category-enterprise.css`, `category-enterprise.js`

Sections (in order):
1. Hero — H1 + grade chips + key advantages
2. Introduction — category overview
3. Product grid — sub-forms (seamless, welded, capillary, coil, etc.)
4. Trust band — sourcing confidence pills
5. Grades available — material overview carousel
6. Applications — where the form is used
7. Industries — sector cards
8. Tools & resources — calculators, downloads
9. Quick links — related categories
10. FAQ — procurement FAQ
11. Gallery — product photos
12. Related categories — cross-link grid

**Reusable components:** Hero, Advantage chips, Product grid card, Trust pill, Grade chip, Industry card, Resource card, FAQ accordion, Gallery, Related-category card.

### 5.2 Product detail template
**Canonical:** `/tgm/products/nickel-alloy-seamless-pipe-tube.html`  
**Files:** `product-page-template.html`, `product-enterprise.css`, `product-enterprise.js`

Sections (in order):
1. Hero — H1 + grade chips + advantages
2. Quick specification summary
3. Product gallery
4. Product overview
5. Engineering benefits
6. Applications
7. Grades available
8. Technical data sheet / tables / graphs
9. Manufacturing process
10. Standards & equivalent grades
11. Quality assurance
12. Downloads / catalogue
13. Packaging
14. Logistics
15. FAQ
16. Popular products
17. Related resources

**Reusable components:** Hero, Spec table, Gallery, Benefit card, Application card, Grade chip, Technical table, Graph wrapper, Process timeline, Standard badge, Download card, Package/logistics block, FAQ accordion, Product mini-card, Resource card.

### 5.3 Grade / material-family template *(needed)*
**Canonical:** `/tgm/grades/400.html`

Current sections observed:
- Hero
- Popular products grid
- Grade introduction
- Chemical composition table
- Standards
- Data sheet / mechanical properties
- Applications
- FAQ
- Related article
- More grades

**Recommended template:** Hybrid of product + category. Use product-detail template with a "grade hero" and swap "product gallery" for "grade snapshot / composition".

### 5.4 Industry / solution template *(needed)*
**Canonical:** `/tgm/solutions/aerospace.html`

Current sections observed:
- Hero
- Description
- Grade sections by alloy family (Inconel, Incoloy, Hastelloy)
- Product grid
- Other applications

**Recommended template:** Reuse the **category template** with a solution-focused hero and alloy-family subsections instead of product-form subsections.

### 5.5 Engineering tool template *(needed)*
**Canonical:** `/tgm/tools/nickel-alloy-weight-calculator.html`

Current sections observed:
- Hero with title
- Calculator form
- Results area

**Recommended template:** Simple focused template — hero + calculator card + explanatory notes + related tools.

### 5.6 Media article template *(needed)*
**Canonical:** `/tgm/media/media-1/media.html`

Current sections observed:
- Hero image (`#pagepicture`)
- Breadcrumb
- Article body
- Schema.org `Article` markup potential

**Recommended template:** Article template — hero image, breadcrumb, author/date, article content, related articles, CTA.

### 5.7 Media category index template *(needed)*
**Canonical:** `/tgm/media/alloy-knowledge/index.html`

Current sections observed:
- Hero image
- Category description
- Article grid/list

**Recommended template:** Hub/listing template — hero + intro + card grid + pagination.

### 5.8 Hub / listing template *(needed)*
**Pages:** `grades.html`, `solutions.html`, `tools.html`, `media.html`, `gallery.html`, `blog.html`

**Recommended template:** Reuse media-category-index template with a card grid of child sections.

### 5.9 Gallery page template *(needed)*
**Canonical:** `/tgm/gallery/pipe-tube.html`

**Recommended template:** Image grid / masonry + lightbox.

### 5.10 Company / utility template *(needed)*
**Canonical:** `/tgm/about-us.html`, `/tgm/contact-us.html`

**Recommended template:** Simple content template — hero + prose + contact blocks / form + trust panel.

### 5.11 Homepage template
**Canonical:** `/index.html`

Already enterprise-grade and bespoke. Should remain a one-off but use the same master chrome and tokens.

---

## 6. Reusable component library

These components should be extracted or standardised so every template can share them:

| Component | Used in | Notes |
|---|---|---|
| `Hero` | All | H1 + background/image + breadcrumb + meta line |
| `AdvantageChips` | Category, Product | 4-point value prop icons |
| `GradeChips` | Category, Product, Grade | Monel / Inconel / Incoloy / Hastelloy links |
| `ProductGridCard` | Category, Industry, Grade | Image + title + short desc + CTA |
| `TrustPillBand` | Category, Product, Company | 3–4 trust signals |
| `IndustryCard` | Category, Product | Icon + title + short description |
| `ResourceCard` | Category, Product, Hub | Icon + title + link |
| `SpecTable` | Product, Grade, Tool | Styled responsive table |
| `GraphWrapper` | Product, Grade | Container for existing technical graphs |
| `ProcessTimeline` | Product | Horizontal supply-chain timeline |
| `FAQAccordion` | Category, Product, Grade | `<details>` based, one open at a time |
| `DownloadCard` | Product, Grade | PDF / catalogue download |
| `GalleryGrid` | Gallery, Category, Product | Image grid with lazy loading |
| `RelatedCard` | Category, Product, Grade | Cross-link mini card |
| `ContactForm` | Contact, Company, Tool | RFQ / inquiry form |
| `ArticleCard` | Media hub, Blog | Thumbnail + title + excerpt |
| `Breadcrumb` | All | `ol#breadol` schema-compatible |

---

## 7. Content preservation rules

No template rollout may remove or hide:

- Existing URLs, slugs, or file paths
- Images and their `alt` attributes
- Technical tables (chemical composition, mechanical properties, tolerances, standards)
- Existing graphs / charts
- PDF / catalogue download links
- Schema.org JSON-LD (Organization, WebSite, WebPage, BreadcrumbList, Product, FAQPage, Article)
- Internal links between grades, products, categories, and solutions
- Existing H1 / title / meta description / keywords
- Product specifications and equivalent-grade data

Presentation, order, and visual hierarchy may be improved; content must not be rewritten or reduced.

---

## 8. Recommended implementation order

1. **Category template rollout** — apply `category-page-template.html` to the 5 remaining legacy category pages (`nickel-alloy.html`, `nickel-alloy-fittings.html`, `nickel-alloy-bars.html`, `nickel-alloy-sheets.html`, `nickel-alloy-wires.html`).
2. **Industry template** — create a solution/industry template (based on category template) and apply to all 12 `/tgm/solutions/*.html` pages.
3. **Tool template** — create a focused calculator/tool template and apply to all 9 `/tgm/tools/*.html` pages.
4. **Hub template** — create a generic listing/hub template for `grades.html`, `solutions.html`, `tools.html`, `media.html`, `gallery.html`, `blog.html`.
5. **Media article template** — create an article template and apply to all 145 `/tgm/media/media-*/media.html` pages.
6. **Media category index template** — apply hub template to the 6 `/tgm/media/*/index.html` pages.
7. **Gallery template** — apply gallery template to the 5 `/tgm/gallery/*.html` pages.
8. **Company / utility template** — apply content template to `about-us.html`, `contact-us.html`, `disclaimer.html`, `privacy-policy.html`, `sitemap.html`.
9. **Grade template** — create a grade-specific template and apply to all 106 `/tgm/grades/*.html` pages.
10. **Product template rollout** — apply `product-page-template.html` to the remaining ~1,269 `/tgm/products/*.html` pages via script.
11. **Homepage polish** — standardise paths to absolute `/tgm/...` and add `tgm-core.js`.
12. **Navigation fix** — update global nav Industries mega menu to point to dedicated `/tgm/solutions/{slug}.html` URLs.

---

## 10. Technical guide templates (new)

A new reusable guide system was added to support the transition from supplier to engineering knowledge platform.

| Template | File | Purpose |
|---|---|---|
| Technical guide master | `tgm/components/technical-guide-template.html` | One template for material comparisons, grade equivalency, selection guides, heat treatment, machining, welding, corrosion, property references, downloads and engineering FAQs |
| Guide styles | `tgm/components/tgm-guides.css` | Shared guide typography, cards, tables, downloads, FAQ, CTA |

### Sections included
1. Hero with guide type, title, lead, reading time, last updated and applicable grades
2. Sticky table of contents
3. Breadcrumb
4. Introduction
5. "When to use this guide" checklist
6. Material comparison table
7. Grade equivalency table
8. Material selection decision cards
9. Heat treatment guidance
10. Machining guidance
11. Welding guidance
12. Corrosion resistance guidance
13. Material property reference table
14. Standards & specifications cards
15. Technical downloads
16. Engineering FAQ (schema-ready)
17. Related products, categories, industries and grades
18. RFQ CTA

### Internal linking strategy
Every guide section should link naturally to:
- **Product pages** — when a specific form is mentioned
- **Category pages** — when a product family is referenced
- **Grade pages** — whenever a grade number appears
- **Industry pages** — when applications are discussed
- **Tools** — when calculations or conversions are relevant

Remove any section that is not relevant to a specific guide rather than leaving placeholder content.

---

## 11. Procurement trust layer (new)

A reusable trust system was added so every page can reduce buyer uncertainty with evidence-based content.

| Component | File | Purpose |
|---|---|---|
| Trust styles | `tgm/components/tgm-trust.css` | Cards, timelines, stats, docs, pills, CTAs |
| Trust section snippets | `tgm/components/trust-sections.html` | Copy-paste sections for QA, traceability, MTC, inspection, manufacturing, packaging, logistics, export, engineering and after-sales support |
| Trust landing page | `tgm/why-trust-truegrade-metals.html` | Standalone procurement-confidence page |

### Trust sections included
1. Quality Assurance
2. Material Traceability
3. Mill Test Certificates
4. Third-Party Inspection
5. Manufacturing Process
6. Packaging Standards
7. Shipping &amp; Logistics
8. Export Experience
9. Engineering Support
10. After Sales Support

### Usage
- Copy any `<section>` from `trust-sections.html` into a category, product, guide or company page.
- Load `tgm-trust.css` in the page `<head>` after `tgm-tokens.css`.
- Replace placeholder metrics (e.g. `{{COUNTRIES}}`) with real values or remove stat blocks if data is not available.

---

## 12. Files created / updated during this phase

- `tgm/components/DESIGN_SYSTEM.md` (existing, referenced)
- `tgm/components/TEMPLATE_ARCHITECTURE.md` (this document)
- `tgm/components/technical-guide-template.html` (new)
- `tgm/components/tgm-guides.css` (new)
- `tgm/components/technical-guide-template.html` (new)
- `tgm/components/tgm-trust.css` (new)
- `tgm/components/trust-sections.html` (new)
- `tgm/why-trust-truegrade-metals.html` (new)

No existing HTML pages were modified during this design phase.
