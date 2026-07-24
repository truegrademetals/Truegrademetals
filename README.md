# TrueGrade Metals — Website Delivery

Ready-to-launch static website. No build step, no server-side code — upload the contents of this folder to any web host (cPanel, Nginx, Apache, Netlify, Vercel, S3 + CloudFront) and point `truegrademetals.com` at it.

## Structure
```
index.html        Landing page (conversion funnel, RFQ form, SEO schema)
categories.html   Product categories + grade × form availability matrix
product.html      Seamless pipe & tube product page (template for all products)
404.html          Not-found page
robots.txt        Crawl rules
sitemap.xml       Submit to Google Search Console after launch
assets/           site.css, site.js, all images, favicon
```

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
