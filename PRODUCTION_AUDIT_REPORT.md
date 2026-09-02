# CEC Website Production Readiness Audit

**Audit date:** 2 September 2026  
**Scope:** 25 HTML pages, 9 CSS files, 4 JavaScript files, local media, navigation, forms, SEO, accessibility, security, performance, and deployment readiness.

## Executive summary

**Release recommendation: NOT READY for public production deployment.**

The static site is structurally usable: all 25 pages include viewport metadata, local page and asset references resolve, tested fragments resolve, images have alternative text, CSS braces are balanced, and all four JavaScript files pass syntax checks. The release should nevertheless be blocked until the contact form is connected, the repository is brought into a clean and reproducible state, and the largest media assets are optimized.

## Release blockers (P0)

### 1. Contact form does not send messages

The contact form prevents the normal submit event and only displays: “Online submission is not connected yet.” A visitor can complete the form but CEC receives nothing.

**Recommendation:** Connect the form to a server-side endpoint or established form service; add server-side validation, spam protection, rate limiting, success/error handling, and delivery monitoring. Do not put mail-service secrets in browser JavaScript.

### 2. The Git working tree is not release-safe

Many production files are modified and a substantial number of project pages, styles, and images are untracked. A deployment from Git could omit untracked pages/assets or differ from the audited local copy.

**Recommendation:** Review the complete diff, remove accidental files, add intended files, commit a known release revision, tag it, and deploy only that immutable commit. Confirm that CI builds from a clean clone.

### 3. No deployment or hosting configuration exists

The repository has no detected hosting manifest, build configuration, redirects, security-header configuration, `robots.txt`, or sitemap. The README contains almost no operating information.

**Recommendation:** Select the hosting platform and add explicit production configuration for HTTPS, redirects, caching, compression, headers, custom 404 handling, and deployment rollback. Document the release procedure and required DNS records.

## High-priority findings (P1)

### Performance and page weight

- Repository payload is approximately **86 MB**.
- Homepage/project video is **34,838,251 bytes (~33.2 MB)**.
- `Marineservice.jpg` is **~9.75 MB**.
- `nkora-mhpp.jpg` is **~8.58 MB**.
- `cyimbili-mhpp.jpg` is **~6.02 MB**.
- Only **12 of 161** image elements use `loading="lazy"`.
- The homepage video uses a normal `src`, so the JavaScript intended to defer a `data-src` video does not defer it.

**Recommendation:** Convert photographs to appropriately sized AVIF/WebP variants, generate responsive `srcset`/`sizes`, lazy-load below-the-fold imagery, provide explicit image dimensions, and compress/transcode video for web delivery. Target a sub-2 MB initial mobile transfer and test on throttled 4G.

### Third-party asset reliability

Important visual content is hotlinked from Wix, EPC Africa, Unsplash, Google, jsDelivr, Unpkg, and Google Fonts. Remote image changes, rate limiting, CORS/security policy changes, or outages can break the site.

**Recommendation:** Obtain permission and host business-critical images locally or in a controlled CDN. Pin third-party library versions, add fallbacks, and monitor external resources.

### Incomplete CDN integrity protection

Bootstrap Subresource Integrity attributes appear on only 4 CSS references and 4 JavaScript references; most pages load the same CDN assets without integrity metadata. AOS is included on several pages even though no `data-aos` attributes were detected.

**Recommendation:** Standardize dependency markup, add correct SRI and `crossorigin` attributes everywhere or self-host pinned assets, and remove unused AOS downloads.

### Duplicate HTML ID

`services/allservices.html` contains the ID `contact` more than once. Duplicate IDs can break fragment navigation and assistive-technology relationships.

**Recommendation:** Give every ID a unique semantic name and retest all in-page links.

### Placeholder social links

Approximately 40 footer social links use `href="#"`. They do not lead to a social profile and may jump visitors to the top of the page.

**Recommendation:** Replace them with verified official profile URLs or remove the icons until profiles are available.

## Medium-priority findings (P2)

### SEO metadata is incomplete

- 10 of 25 pages have no meta description.
- The homepage title is only `Homepage`.
- The services listing has no H1.
- No canonical links or Open Graph metadata were detected.
- No `robots.txt` or `sitemap.xml` was detected.

**Recommendation:** Add unique titles/descriptions, one meaningful H1 per page, canonical URLs, Open Graph/Twitter metadata, organization structured data, a sitemap, and robots directives. Use the final production domain consistently.

### Accessibility and readability

- Global `p { text-align: justify !important; }` forces justification even in narrow cards, hero copy, and footer text; this can create uneven spacing and reduce readability.
- Gallery interaction should be verified for keyboard focus, focus return, and screen-reader dialog semantics.
- Form errors set `aria-invalid`, but fields should also reference error text with `aria-describedby`.
- Icon-only social links have accessible labels, but their placeholder destinations make them functionally invalid.

**Recommendation:** Restrict justification to long-form content, use left alignment on mobile, complete dialog focus management, associate validation errors with inputs, and run WCAG 2.2 AA checks with keyboard-only navigation and a screen reader.

### URL and filesystem naming

Names such as `civil&engineering.html`, `MPEP.html`, `CEC LOGO.png`, and the directory `allprojectsdetails.html` are fragile or confusing on case-sensitive production hosts and require URL encoding.

**Recommendation:** Before launch, migrate to lowercase kebab-case URLs and filenames (for example, `civil-engineering.html` and `project-details/`) and configure permanent redirects for any published legacy URLs.

### Maintainability

Navigation and footer markup are duplicated across 25 pages, inline scripts are present, and the shared stylesheet contains repeated/overlapping media rules. Future edits can easily become inconsistent.

**Recommendation:** Introduce a lightweight templating/build step with shared header/footer components, consolidate breakpoints, lint HTML/CSS/JS in CI, and format source consistently.

## Security recommendations

The site is mostly static, which limits server-side attack surface, but production controls are not defined.

- Force HTTPS and redirect HTTP to HTTPS.
- Add CSP, HSTS (after HTTPS is confirmed), `X-Content-Type-Options: nosniff`, a strict referrer policy, frame restrictions, and a permissions policy.
- Account for required Google Maps, fonts, and CDN origins when designing CSP.
- Remove inline event handlers (one was detected) and move inline scripts to versioned files to support a strict CSP.
- Protect the future form endpoint against spam, injection, abuse, and excessive payloads.
- Never expose credentials or API keys in client-side files.

## Checks that passed

- 25 HTML pages detected; all 25 have viewport metadata.
- No missing local file targets were found in `href`/`src` references after HTML entity decoding.
- No broken local fragment links were found.
- All detected `<img>` elements include an `alt` attribute.
- All four JavaScript files pass `node --check`.
- CSS brace counts are balanced.
- No obvious `eval()` or `document.write()` usage was found.
- Representative pages previously returned HTTP 200 from the local server.

## Required pre-release verification

1. Resolve all P0 items.
2. Optimize media and retest initial transfer size, LCP, CLS, and INP on mobile.
3. Test every page at 320, 375, 768, 1024, 1440, and 1920 CSS pixels.
4. Test current Chrome, Edge, Firefox, and Safari, plus iOS Safari and Android Chrome.
5. Verify navigation, filter buttons, galleries/lightboxes, video fallback, all CTAs, telephone/email links, map, and the real contact-form delivery path.
6. Run automated HTML validation, Lighthouse, axe, and a link crawler against the staged HTTPS URL.
7. Confirm production headers, caching, compression, 404 behavior, sitemap, robots rules, analytics consent requirements, DNS, TLS renewal, monitoring, backups, and rollback.
8. Obtain business sign-off for project facts, client names, image rights, contact details, privacy notice, and social links.

## Suggested release gate

Deploy only when there are no open P0 issues, no broken internal links, form delivery is proven end-to-end, key pages meet agreed performance budgets, accessibility has no critical/serious automated violations, and the exact audited commit is reproducibly deployed to staging and then production.
