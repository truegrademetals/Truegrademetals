# TrueGrade Metals — Enterprise Design System

This design system powers the entire TrueGrade Metals website. Every page, component and template should reuse these tokens, patterns and components so the site feels like one coherent enterprise platform.

---

## 1. Tokens

Load the token file first in every page `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link href="/tgm/components/tgm-tokens.css" rel="stylesheet" />
```

Reference: `tgm/components/tgm-tokens.css`

### Brand colours

| Token | Value | Usage |
|---|---|---|
| `--tgm-navy-900` | `#0B1F33` | Primary text, headings, hero backgrounds |
| `--tgm-navy-800` | `#14304d` | Secondary headings, hover states |
| `--tgm-navy-50`  | `#f2f7fb` | Section backgrounds |
| `--tgm-ember-500`| `#EE5D16` | Primary CTA, accent, links |
| `--tgm-ember-600`| `#c44b10` | CTA hover |
| `--tgm-ember-50` | `#fff6f2` | Accent tints |
| `--tgm-gray-500` | `#6b7280` | Body text, muted copy |
| `--tgm-gray-200` | `#e2e5eb` | Borders, dividers |

### Typography

| Token | Font | Usage |
|---|---|---|
| `--tgm-font-display` | Space Grotesk | Headlines, section headings, cards |
| `--tgm-font-body`    | Inter         | Body copy, UI text, forms |
| `--tgm-font-mono`    | IBM Plex Mono | Specs, grade names, labels, metadata |

### Spacing, radius & shadow

Use the scale in `tgm-tokens.css`. Standard section padding is `100px` top/bottom on desktop, `70px` on mobile. Max content width is `1320px` (`--tgm-max-w`).

---

## 2. Global components

### Navigation
- File: `tgm/components/global-nav.html`
- Loader: `tgm/components/global-nav.js`
- Usage: `<div id="global-nav" style="min-height:122px"></div>` + `<script src="/tgm/components/global-nav.js"></script>`
- Contains utility bar, sticky header, mega menus, search overlay, mobile drawer.

### Footer
- File: `tgm/components/global-footer.html`
- Loader: `tgm/components/global-footer.js`
- Usage: `<div id="global-footer"></div>` + `<script src="/tgm/components/global-footer.js"></script>`
- Contains link architecture, trust panel, certifications, newsletter, final CTA, legal.

### Tables & graphs
- File: `tgm/components/tgm-tables-graphs.css`
- Usage: `<link href="/tgm/components/tgm-tables-graphs.css" rel="stylesheet"/>`
- Styles `.table-container2`, `.tolerence-table`, `.delivery-table`, `.tgm-graph`, `.tgm-process-diagram`.

---

## 3. Page templates

### Category pages
- Canonical example: `tgm/nickel-alloy-pipes.html`
- Template: `tgm/components/category-page-template.html`
- Stylesheet: `tgm/category-enterprise.css`
- Script: `tgm/category-enterprise.js`

Required sections in order:
1. Hero
2. Introduction
3. Product Grid
4. Trust Band
5. Material Overview / Grades
6. Applications
7. Industry Cards
8. Technical Resources
9. Quick Links
10. FAQ
11. Gallery
12. Related Categories

### Product pages
- Canonical example: `tgm/products/nickel-alloy-seamless-pipe-tube.html`
- Template: `tgm/components/product-page-template.html`
- Stylesheet: `tgm/product-enterprise.css`
- Script: `tgm/product-enterprise.js`

Required sections in order:
1. Hero
2. Quick Specification Summary
3. Product Gallery
4. Product Overview
5. Engineering Benefits
6. Applications
7. Chemical Composition
8. Mechanical Properties
9. Technical Graphs
10. Standards & Equivalent Grades
11. Quality Assurance
12. Downloads
13. FAQs
14. Related Products
15. Related Resources
16. RFQ Section
17. Final Trust CTA

---

## 4. Common patterns

### Buttons

Primary button:
```html
<button class="cat-btn click-event" type="button">Request a quote</button>
```

Ghost button:
```html
<a class="cat-btn-ghost" href="grades.html">Explore grades</a>
```

### Section heading

```html
<div class="cat-section-head">
  <h2 id="section-heading"><span>Eyebrow</span>Section title</h2>
  <p>Short supporting sentence.</p>
</div>
```

### Cards

Use `.cat-card-grid` or `.cat-card-grid-3` / `.cat-card-grid-4` for grids of linked cards.

### Tables

Wrap large tables in `.table-container2` or let `product-enterprise.js` auto-wrap `.tolerence-table` / `.delivery-table`.

### Quote form

The floating quote form (`#float-form`) is preserved on category and product pages. Any element with `.click-event` opens it. CTAs can also link to `/tgm/contact-us.html`.

---

## 5. SEO & accessibility rules

- One `<h1>` per page.
- Use logical heading order (`h1` → `h2` → `h3`).
- Include `BreadcrumbList`, `Organization`, `WebSite`, `WebPage` schema on every page.
- Product pages: include `Product` / `ItemList` schema.
- FAQ sections: include `FAQPage` schema.
- Add `loading="lazy"` to below-the-fold images.
- Maintain `alt` text on every image.
- Keep important SEO content visible; do not hide it in tabs or accordions.
- Ensure tap targets are at least 44 × 44 px on mobile.

---

## 6. Performance rules

- Reuse shared CSS/JS; avoid duplicating component styles per page.
- Lazy-load images below the fold.
- Keep animations to `transform` and `opacity`.
- Respect `prefers-reduced-motion`.
- Use inline SVG icons from the global components where possible.

---

## 7. Migration notes

- Legacy `nav.css`, `products.css`, `products-all.css`, `nav.js` and `products.js` are no longer used on templated pages.
- Absolute paths (`/tgm/...`) should be used for shared assets so pages work from both `/tgm/` and `/tgm/products/`.
