# TrueGrade Metals — Enterprise SEO Strategy

> Objective: make TrueGrade Metals the definitive engineering materials resource in search results while preserving every existing URL and content element.

---

## 1. Current audit findings

| Issue | Severity | Evidence |
|---|---|---|
| **No canonical tags** | High | 0 of 13 sampled pages have `<link rel="canonical">` |
| **Multiple H1 tags** | High | Product pages have 3 H1s (float-form header, product title, footer title) |
| **Footer title as H1** | High | Legacy footer markup uses `<h1>` for the company name |
| **Weak internal linking in category pages** | Medium | Converted category page has only 1 counted internal link in content area |
| **Missing OG title on homepage** | Medium | `og:title` absent on root `index.html` |
| **Missing breadcrumb on homepage / tools** | Low | No `ol#breadol` on homepage or tool pages |
| **Images without alt text** | Medium | Homepage has 12 images without `alt`; other pages generally clean |
| **Schema inconsistency** | Medium | Some pages use only `Organization`/`FAQPage`; Product/Breadcrumb schemas missing or malformed |
| **No XML sitemap** | Medium | Only `sitemap.html` exists; search engines prefer `sitemap.xml` |
| **Nav industry links point to generic hub** | Medium | Mega-menu links every industry to `/tgm/solutions.html` instead of dedicated pages |

---

## 2. Strategic principles

1. **Preserve URLs and content** — every slug, image, table and paragraph stays exactly where it is.
2. **One H1 per page** — the page topic. Company names and footer titles must not be H1.
3. **Canonical self-references** — every page points to its own canonical HTTPS URL.
4. **Schema graph** — every page includes `Organization`, `WebPage` and `BreadcrumbList`; product pages add `Product`; FAQ pages add `FAQPage`; guides/articles add `TechArticle`.
5. **Evidence-based copy** — replace generic claims with specific documentation, standards and process evidence.
6. **Topic clusters** — link product pages → category pages → grade pages → industry pages → guides, forming clear semantic groups.
7. **No keyword stuffing** — anchor text should be descriptive and natural.

---

## 3. Page-type SEO requirements

### Homepage
- One H1: value proposition.
- Add canonical, OG title, OG URL.
- Add WebSite + Organization schema.
- Add breadcrumb (single-item or omit if not needed).
- Fix missing image alt text.

### Category pages
- One H1: category name.
- Canonical self-reference.
- Organization + WebPage + BreadcrumbList + ItemList schema.
- Link to child product pages, related categories, grade family pages and industry pages.
- Include trust signals (MTC, traceability, global shipping).

### Product pages
- One H1: product name.
- Canonical self-reference.
- Organization + WebPage + BreadcrumbList + Product + FAQPage schema.
- Link to parent category, related grades, related industries and related resources.
- Remove footer-title H1.

### Grade pages
- One H1: grade name.
- Canonical self-reference.
- Organization + WebPage + BreadcrumbList + Product (for popular products) schema.
- Link to category pages, related grades, applications/industries.

### Industry / solution pages
- One H1: industry + alloy application.
- Canonical self-reference.
- Organization + WebPage + BreadcrumbList schema.
- Link to relevant grades, categories and product pages.
- Update global nav mega-menu to point to dedicated URLs.

### Engineering guides / resources
- One H1: guide title.
- Canonical self-reference.
- Organization + WebPage + BreadcrumbList + TechArticle + FAQPage schema.
- Link to related products, categories, grades and industries.

### Tools
- One H1: tool name.
- Add breadcrumb.
- Canonical self-reference.
- Organization + WebPage + BreadcrumbList + SoftwareApplication schema.

### Company / legal pages
- One H1.
- Canonical self-reference.
- Organization + WebPage + BreadcrumbList schema.

---

## 4. Internal linking architecture

### Primary clusters

| Cluster | Hub | Spokes |
|---|---|---|
| **Nickel alloy products** | `/tgm/nickel-alloy.html` | Pipes, fittings, bars, sheets, wires category pages |
| **Pipes & tubes** | `/tgm/nickel-alloy-pipes.html` | Seamless, welded, capillary, coil, thick-walled product pages |
| **Bars & rods** | `/tgm/nickel-alloy-bars.html` | Round, flat, square, hexagon product pages |
| **Sheets & plates** | `/tgm/nickel-alloy-sheets.html` | Sheet, plate, strip, coil product pages |
| **Wires** | `/tgm/nickel-alloy-wires.html` | Wire, wire rod, welding electrode product pages |
| **Grades** | `/tgm/grades.html` | Individual grade pages |
| **Industries** | `/tgm/solutions.html` | Aerospace, oil & gas, marine, chemical, power, automotive |
| **Resources** | `/tgm/media.html` | Guides, articles, tools, gallery |

### Linking rules
1. Every product page links up to its parent category and across to its grade page.
2. Every category page links down to its product pages and across to related categories.
3. Every grade page links to product pages that are commonly supplied in that grade.
4. Every industry page links to the grades and categories most relevant to that sector.
5. Every guide links to the products, categories, grades and industries it mentions.
6. Footer provides cluster navigation for materials, industries and resources.

### Anchor-text guidelines
- Use the exact product/category/grade name as anchor text where natural.
- Avoid exact-match keyword anchors like "buy nickel alloy pipes" more than once per page.
- Use descriptive CTAs: "View Inconel 625 specifications", "Browse nickel alloy pipes".

---

## 5. Schema graph pattern

Every page should include a JSON-LD `@graph` containing:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "Organization", "@id": "https://www.truegrademetals.com/#organization", ...},
    {"@type": "WebSite", "@id": "https://www.truegrademetals.com/#website", ...},
    {"@type": "WebPage", "@id": "{{CANONICAL}}#webpage", "isPartOf": {"@id": "https://www.truegrademetals.com/#website"}, ...},
    {"@type": "BreadcrumbList", "@id": "{{CANONICAL}}#breadcrumb", ...},
    {"@type": "Product|FAQPage|TechArticle|ItemList", ...}
  ]
}
```

Use `@id` references to avoid duplicating Organization data on every page while keeping each page self-contained.

---

## 6. Technical SEO actions

### Canonical tags
Add `<link rel="canonical" href="https://www.truegrademetals.com{{PATH}}">` to every HTML page.

### XML sitemap
Generate `/sitemap.xml` with all public URLs, lastmod dates and priority hints:
- Homepage: 1.0
- Categories: 0.9
- Products: 0.8
- Grades: 0.8
- Industries: 0.8
- Guides/resources: 0.7
- Tools: 0.6
- Company/legal: 0.5

### Robots.txt
Ensure `/robots.txt` exists and points to `/sitemap.xml`:

```
User-agent: *
Allow: /
Sitemap: https://www.truegrademetals.com/sitemap.xml
```

### Image optimization
- Ensure every `<img>` has a meaningful `alt` attribute or empty `alt=""` for decorative images.
- Add `loading="lazy"` for below-the-fold images.
- Add explicit `width` and `height` where possible to prevent layout shift.

### Heading hierarchy
- Exactly one H1 per page.
- No skipped levels (H1 → H2 → H3, not H1 → H3).
- Footer/utility headings must be H2 or lower, never H1.

### Open Graph
Every page must have:
- `og:title`
- `og:description`
- `og:url` (matching canonical)
- `og:type` (website | product | article)
- `og:image`

---

## 7. Files & components

| File | Purpose |
|---|---|
| `tgm/components/seo-helpers.html` | Reusable schema JSON-LD snippets |
| `scripts/apply_seo.py` | Automated canonical/schema/heading/alt fixes |
| `scripts/generate_sitemap.py` | Generate `/sitemap.xml` from all HTML files |
| `/robots.txt` | Crawl directives and sitemap reference |
| `tgm/components/SEO_STRATEGY.md` | This document |

---

## 8. Measurement

After implementation, verify:
- 100% of pages have canonical tags.
- 100% of pages have exactly one H1.
- 100% of images have alt text.
- 100% of pages have BreadcrumbList schema.
- Product pages have Product schema.
- FAQ sections have FAQPage schema.
- `/sitemap.xml` exists and is valid.
- No internal 404 links in a sampled crawl.

Use Lighthouse, Google Search Console and an XML sitemap validator for final checks.
