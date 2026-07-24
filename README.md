# TrueGrade Metals — Website Delivery

Ready-to-launch static website. No build step, no server-side code — upload the contents of this folder to any web host (cPanel, Nginx, Apache, Netlify, Vercel, S3 + CloudFront) and point `truegrademetals.com` at it.

## Structure
```
index.html        Landing page (conversion funnel, RFQ form, SEO schema)
categories.html   Full product catalog — 6 categories, 22 sub-products, 70+ grades
product.html      Seamless pipe & tube product page (template for all products)
about.html        About & Contact — team, values, contact form
404.html          Not-found page
robots.txt        Crawl rules
sitemap.xml       Submit to Google Search Console after launch
assets/           site.css, site.js, leadgen.js, all images, favicon,
                  grade-selection-guide.pdf (lead magnet)
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
3. **Form delivery** — RFQ forms open the visitor's email client with a pre-filled message