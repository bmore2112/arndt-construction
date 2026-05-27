# Arndt Construction — Website

Single-page marketing site for **Arndt Construction**, a family-owned roofing & siding contractor serving Calvert County and Southern Maryland.

- Live: TBD
- Real site source: [arndtconstructionmd.com](https://arndtconstructionmd.com/)
- Owner: Nathaniel Arndt — MHIC #115973
- Address: 11410 Rawhide Road, Lusby, MD 20657
- Phone: (443) 624-7508
- Email: nathanielarndtconstruction@gmail.com

## Stack

Pure static HTML/CSS/JS. No build step, no framework. Open `arndt-construction.html` in any browser or serve the folder with any static file server.

```bash
# Local preview
python -m http.server 8000
# then visit http://localhost:8000/arndt-construction.html
```

## Sections

1. Hero — branded truck + tagline
2. Services — Roofing, Siding, Storm Damage, Gutters
3. Insurance Claims — 5-step educational guide
4. Gallery — 9 real before/after job photos in a 3×3 grid
5. Reviews — 6 real Facebook recommendations (screenshot embeds) + "Leave us a Review" modal (Google / Facebook / Yelp)
6. Service Area — Google Maps embed centered on Lusby
7. Blog — placeholder cards for upcoming posts
8. FAQ — 4 expandable answers
9. Contact — meta strip + estimate form
10. Footer — sitemap, hours, license, socials

## Assets

| File | Purpose |
|------|---------|
| `arndt-logo-cropped.png` | Transparent logo lock-up, nav + footer |
| `arndt-hero.jpg` | Hero background (branded truck) |
| `svc-*.png` | Service card photos (roofing / siding / storm / gutters) |
| `job-1.png` … `job-9.png` | Gallery before/after shots |
| `fb-review-*.png` | Facebook review screenshots |

## Hosting

Drop the folder into any static host: Netlify, Vercel, Cloudflare Pages, GitHub Pages. No server required.

For GitHub Pages: Settings → Pages → Branch: `main`, folder: `/ (root)`. The site will be at `https://bmore2112.github.io/arndt-construction/arndt-construction.html`.
