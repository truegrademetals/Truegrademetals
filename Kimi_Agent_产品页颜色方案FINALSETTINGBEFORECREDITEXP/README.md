# TrueGrade Metals — Website Delivery

Ready-to-launch static website. No build step, no server-side code — upload the contents of this folder to any web host (cPanel, Nginx, Apache, Netlify, Vercel, S3 + CloudFront) and point `truegrademetals.com` at it.

## Structure
```
index.html              Landing page (conversion funnel, RFQ form, SEO schema)
categories.html         Full product catalog — 6 categories, 22 sub-products, 70+ grades
grades.html             Grade library index + 69 grade hub pages (grade-*.html)
about.html              About & Contact — team, values, contact form
tools.html              Interactive pipe schedule calculator + grade comparison
industries.html         Industry index + 12 industry landing pages (industry-*.html)
blog.html               Blog index + 5 engineering articles (blog-*.html)

Product pages (16):
  product.html                    Seamless pipe & tube (the flagship template)
  welded-pipe.html  fittings.html  bars.html  sheets.html  wires.html
  inconel-625-pipes/bars.html     inconel-718-bars.html
  hastelloy-c276-pipes/fittings/sheets.html
  monel-400-pipes/bars.html       incoloy-825-pipes/sheets.html

404.html, robots.txt, sitemap.xml (107 URLs)
assets/                 site.css, site.js, leadgen.js, images, favicon,
                        grade-selection-guide.pdf + 5 form catalogs (catalog-*.pdf)
_gen*.py                page generators — edit data & re-run to regenerate pages
```

## Lead generation (built in)
- **Lead magnet** — `assets/grade-selection-guide.pdf`: a 2-page branded engineering guide given away in exchange for name + email.
- **Exit-intent / scroll modal** — fires once per 7 days per visitor (45% scroll or mouse-leave), captures the lead and auto-downloads the guide.
- **Inline capture blocks** — compact signup strips on landing, categories and product pages.
- **RFQ & contact forms** — every submission is also logged as a lead.
- **Where leads go** — stored in browser localStorage by default. To wire a real CRM, set `LEAD_WEBHOOK_URL` at the top of `assets/leadgen.js` (Formspree, Zapier, HubSpot endpoint…). To export captured leads, open any page with `?leads=export` appended — it downloads a CSV.

## Before going live
1. **Domain** — canonical URLs and schema reference `https://www.truegrademetals.com/`. If the final domain differs, find-and-replace that string across all `.html`, `sitemap.xml` and `robots.txt`.
2. **Contact details** — email (`info@truegrademetals.com`), phone (`+86-519-81809659`) and WhatsApp links (`wa.me/8651981809659`) are placeholders to confirm with sales.
3. **Form delivery** — RFQ forms open the visitor's email client with a pre-filled message (works everywhere, zero maintenance). If you want submissions stored in a CRM instead, point the forms at an endpoint (Formspree, HubSpot, etc.) — the form markup is clearly commented.
4. **Search Console** — after DNS is live, submit `sitemap.xml` and request indexing.

## SEO already included
- JSON-LD schema on every page: Organization, WebSite, BreadcrumbList, FAQPage, ItemList (categories), Product (product page)
- Canonical URLs, meta descriptions, Open Graph + Twitter cards, social share image (`assets/og-image.jpg`)
- Semantic headings, descriptive image alt text, sitemap + robots

## Notes
- Product imagery is AI-generated studio photography — replace with real factory photos when available by overwriting files in `assets/` with the same filenames.
- The product page (`product.html`) is the template for future product pages: copy it, swap the hero image, specs, charts data and FAQ.
