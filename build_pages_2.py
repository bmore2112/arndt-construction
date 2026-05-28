"""All non-home pages. Run via build.py's main()."""

DL_ICON = '<svg class="dl-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>'


def page_hero(eyebrow, h1, lede="", bg_image=None):
    lede_html = f'<p class="page-hero-lede">{lede}</p>' if lede else ""
    cls = "page-hero"
    if bg_image:
        cls += " has-bg"
        bg_div = f'<div class="page-hero-media" style="background-image:url(\'{bg_image}\');" aria-hidden="true"></div>'
    else:
        bg_div = '<div class="page-hero-media is-placeholder" aria-hidden="true"></div>'
    return f"""<header class="{cls}">
  {bg_div}
  <div class="container">
    <div class="page-hero-content">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      {lede_html}
    </div>
  </div>
</header>"""


def run(build, breadcrumbs, service_schema, article_schema, faq_schema, crumbs_html, cta_band, REVIEW_MODAL, BASE_URL, SITE_NAME, PHONE, PHONE_HREF, EMAIL, ADDRESS, LICENSE, LOCAL_BUSINESS, download_btn=None):

    # ============================================================
    # ROOFING
    # ============================================================
    roofing_faqs = [
        ("How long does a roof replacement take?",
         "Most single-family re-roofs are a one-day job — tear-off in the morning, underlayment by midday, shingles and ridge by evening. Larger or steeper roofs run two days."),
        ("Do you tear off the old roof or overlay?",
         "We tear off in nearly every case. Overlays trap moisture, void most shingle warranties, and hide deck damage. Tear-off is the right answer for any roof we'd stand behind."),
        ("What shingle warranties do you offer?",
         "Manufacturer warranties on architectural asphalt typically run 30 years to lifetime on the shingles themselves, plus a workmanship warranty from us. We walk you through the specific terms before signing."),
        ("Can you replace a roof in winter?",
         "Yes. Architectural asphalt installs reliably in Mid-Atlantic winter temperatures. We avoid days below freezing with active precipitation, but cold dry days are completely workable."),
    ]
    body = f"""
{crumbs_html([("Home", "/"), ("Services", "/roofing/"), ("Roofing", None)])}
{page_hero("Roofing", "Roof Replacement &amp; Repair in Calvert County, MD",
           "Architectural asphalt, metal, and flat-roof systems for residential and commercial properties. Free inspections, code-compliant installs, and a written workmanship warranty.",
           bg_image="/arndt-hero.jpg")}

<section class="prose">
  <div class="container">
    <div class="prose-grid">
      <div class="prose-main">
        <h2>What we install</h2>
        <p>Arndt Construction installs roofing systems engineered for Maryland weather — high humidity in summer, freeze-thaw cycles in winter, and the wind and hail patterns that come off the Bay. Our crew has been on Calvert County roofs since 2019, and our license (MHIC #115973) is current and verifiable.</p>

        <h3>Architectural asphalt shingles</h3>
        <p>The most common choice for residential re-roofs in Southern Maryland. Architectural shingles last 25-50 years depending on grade, resist wind up to 130 MPH on impact-rated lines, and carry strong manufacturer warranties. We install GAF, CertainTeed, and Owens Corning lines.</p>

        <h3>Standing-seam metal roofing</h3>
        <p>For homeowners who want a 50+ year roof, prefer the look of metal, or live in heavy snow-load areas. Standing-seam systems shed snow cleanly, resist algae and moss, and pair well with solar.</p>

        <h3>Flat-roof systems (TPO, EPDM)</h3>
        <p>For commercial buildings, additions, and porch roofs. TPO membranes give you a 20-30 year service life when installed correctly with proper drainage and seam welding.</p>

        <h3>Roof repair</h3>
        <p>Not every roof needs replacement. We handle isolated repairs — wind-lifted shingles, popped nails, flashing leaks, soft decking, and chimney/skylight seal failures — and we'll tell you honestly if a repair is the right answer instead of pushing for a full re-roof.</p>

        <h2>Our process</h2>
        <ol class="numbered">
          <li><strong>Free on-site inspection.</strong> We walk every plane, document with photos, and check decking, flashing, vents, and ridge.</li>
          <li><strong>Written line-item estimate.</strong> No phone-call ballparks. Materials, labor, code upgrades, dumpster, and cleanup all itemized.</li>
          <li><strong>Schedule and order materials.</strong> Most re-roofs schedule within 1-2 weeks; storm work moves faster.</li>
          <li><strong>Install day.</strong> Tear-off, decking inspection, underlayment, shingles, ridge ventilation, cleanup. One day for most homes.</li>
          <li><strong>Final walk-through.</strong> We walk it with you, hand over warranty paperwork, and leave the site cleaner than we found it.</li>
        </ol>

        <h2>What you should expect from a Maryland roofer</h2>
        <p>An MHIC-licensed contractor (ours: <strong>#{LICENSE.split('#')[-1]}</strong>). Proof of general liability and workers' comp insurance. A written estimate before you sign anything. No upfront deposit larger than legally allowed. A clear timeline. A workmanship warranty in writing. Anyone skipping these basics is not someone you should hire — full stop.</p>
      </div>

      <aside class="prose-aside">
        <div class="aside-card">
          <h4>Free roof inspection</h4>
          <p>We walk it, photograph it, and email you a written report. No obligation.</p>
          <a href="/contact/" class="btn btn-primary">Book inspection</a>
        </div>
        <div class="aside-card">
          <h4>Related services</h4>
          <ul>
            <li><a href="/storm-damage/">Storm damage repair</a></li>
            <li><a href="/insurance-claims/">Insurance claim help</a></li>
            <li><a href="/gutters/">Seamless gutters</a></li>
            <li><a href="/siding/">Siding installation</a></li>
          </ul>
        </div>
        <div class="aside-card">
          <h4>Service area</h4>
          <p>Calvert County and Southern Maryland — including <a href="/service-area/lusby/">Lusby</a>, <a href="/service-area/solomons/">Solomons</a>, and <a href="/service-area/prince-frederick/">Prince Frederick</a>.</p>
        </div>
      </aside>
    </div>

    <h2 style="margin-top:80px">Frequently asked questions</h2>
    <div class="faq-list">
      """ + "\n      ".join([f"""<details class="faq"><summary>{q}<span class="ic"><svg viewBox="0 0 14 14" aria-hidden="true"><path d="M7 1v12M1 7h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span></summary><div class="a">{a}</div></details>""" for q, a in roofing_faqs]) + """
    </div>
  </div>
</section>
""" + cta_band("Need a roof estimate?", "On-site inspection, written quote, no pressure. Same business day callback.", "Book a Free Inspection", "/contact/")

    build("/roofing/",
          "Roof Replacement &amp; Repair in Calvert County MD | Arndt",
          "Architectural shingles, metal, and flat-roof systems installed across Calvert County and Southern Maryland. Free inspections, licensed (MHIC #115973), bonded, insured.",
          body,
          schemas=[
              service_schema("Roof Replacement & Repair",
                             "Residential and commercial roof replacement and repair across Calvert County and Southern Maryland. Architectural asphalt, standing-seam metal, and TPO flat-roof systems.",
                             "/roofing/"),
              faq_schema(roofing_faqs),
              breadcrumbs([("Home", "/"), ("Roofing", "/roofing/")]),
          ])

    # ============================================================
    # SIDING
    # ============================================================
    siding_faqs = [
        ("How long does siding installation take?",
         "Most single-family vinyl re-sides take 3-5 days. Fiber cement (Hardie) takes 5-7 days. We protect landscaping and clean up daily."),
        ("Vinyl, fiber cement, or cedar — which is right for my home?",
         "Vinyl is the most cost-effective and lowest-maintenance choice. Fiber cement (James Hardie) lasts longest and has the most premium look for the cost. Cedar shake is the right answer for historic or coastal homes where character matters."),
        ("Can siding improve energy efficiency?",
         "Yes, particularly when paired with rigid foam insulation behind the siding. Insulated vinyl and house-wrap improvements typically deliver measurable savings on heating and cooling bills."),
    ]
    body = f"""
{crumbs_html([("Home", "/"), ("Services", "/roofing/"), ("Siding", None)])}
{page_hero("Siding", "Vinyl, Fiber Cement &amp; Cedar Shake Siding in Maryland",
           "James Hardie, CertainTeed, and traditional cedar shake — installed across Calvert County and Southern Maryland. Curb appeal and thermal performance, together.",
           bg_image="/svc-siding.png")}

<section class="prose">
  <div class="container">
    <div class="prose-grid">
      <div class="prose-main">
        <h2>Materials we install</h2>

        <h3>Vinyl siding</h3>
        <p>The most popular siding choice in Maryland for good reason: affordable, low-maintenance, available in hundreds of colors and profiles, and warrantied 25+ years. Insulated vinyl adds R-value and helps with utility bills. We install CertainTeed, Mastic, and other proven lines.</p>

        <h3>Fiber cement (James Hardie)</h3>
        <p>Fiber cement is the premium choice — looks like real wood, lasts 50+ years, resists fire, rot, and pests. James Hardie products carry a 30-year non-prorated warranty and come in pre-finished ColorPlus or paintable. Higher upfront cost than vinyl; significantly lower lifetime cost.</p>

        <h3>Cedar shake &amp; shingle</h3>
        <p>For historic homes, coastal cottages, and any project where character drives the design. We install both cedar shake and cedar shingle in Western Red Cedar — naturally weather-resistant, beautifully gray-aging, and the right call for waterfront properties around the Bay.</p>

        <h2>When to replace siding</h2>
        <p>Watch for cracking, warping, bubbling, soft spots, peeling paint, faded color, gaps at seams, and moisture inside the home near exterior walls. If you've patched the same spot more than twice, or if your energy bills keep climbing despite a tight roof and good windows, the envelope is leaking — and siding is usually the cheapest fix.</p>

        <h2>Our siding process</h2>
        <ol class="numbered">
          <li>On-site walkthrough and material selection — we bring samples, you decide.</li>
          <li>Written line-item estimate including tear-off, house-wrap, J-channels, trim, soffit, fascia, and labor.</li>
          <li>Tear-off and inspection of sheathing — any rot gets replaced before new siding goes up.</li>
          <li>Modern house-wrap (Tyvek or equivalent) and optional rigid foam for insulation upgrade.</li>
          <li>Install, trim, soffit, fascia, and final cleanup.</li>
        </ol>
      </div>

      <aside class="prose-aside">
        <div class="aside-card">
          <h4>Free siding estimate</h4>
          <p>On-site measure, material samples, written quote.</p>
          <a href="/contact/" class="btn btn-primary">Book estimate</a>
        </div>
        <div class="aside-card">
          <h4>Related services</h4>
          <ul>
            <li><a href="/roofing/">Roof replacement</a></li>
            <li><a href="/gutters/">Seamless gutters</a></li>
            <li><a href="/storm-damage/">Storm damage</a></li>
          </ul>
        </div>
      </aside>
    </div>

    <h2 style="margin-top:80px">Siding FAQs</h2>
    <div class="faq-list">
      """ + "\n      ".join([f"""<details class="faq"><summary>{q}<span class="ic"><svg viewBox="0 0 14 14" aria-hidden="true"><path d="M7 1v12M1 7h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span></summary><div class="a">{a}</div></details>""" for q, a in siding_faqs]) + """
    </div>
  </div>
</section>
""" + cta_band("Refresh your home's exterior.", "Vinyl, fiber cement, or cedar. We bring samples to your home and quote in writing.", "Book a Free Estimate", "/contact/")

    build("/siding/",
          "Vinyl &amp; Fiber Cement Siding Installation MD | Arndt",
          "Vinyl, fiber cement (James Hardie), and cedar shake siding installation across Calvert County and Southern Maryland. Licensed (MHIC #115973). Free written estimates.",
          body,
          schemas=[
              service_schema("Siding Installation",
                             "Vinyl, fiber cement, and cedar shake siding installation across Calvert County and Southern Maryland.",
                             "/siding/"),
              faq_schema(siding_faqs),
              breadcrumbs([("Home", "/"), ("Siding", "/siding/")]),
          ])

    # ============================================================
    # STORM DAMAGE
    # ============================================================
    storm_faqs = [
        ("What should I do first after storm damage?",
         "Stay off the roof. Photograph everything from ground level — exterior shots, ceiling stains inside, fallen branches, hail-strike marks on gutters and siding. Then call a licensed local roofer for an inspection. Don't call insurance until you know what you have."),
        ("Do you handle emergency tarping?",
         "Yes. If active leaks are threatening your interior, we can be on-site for emergency tarping within 24-48 hours of your call, usually faster during local storm events."),
        ("Will my insurance cover storm damage?",
         "Most standard Maryland homeowner policies cover wind, hail, and falling-object damage subject to your deductible. Whether a specific claim pays depends on the cause, the age of the roof, and policy specifics. We help you document everything correctly so the adjuster has what they need."),
    ]
    body = f"""
{crumbs_html([("Home", "/"), ("Services", "/roofing/"), ("Storm Damage", None)])}
{page_hero("Storm Damage", "Storm Damage Roof Repair in Maryland — Same-Day Response",
           "Hail, wind, and fallen-tree damage. We answer the phone, show up fast, and document everything correctly for your insurance claim.",
           bg_image="/svc-storm.png")}

<section class="prose">
  <div class="container">
    <div class="prose-grid">
      <div class="prose-main">
        <h2>If you have active leaks right now</h2>
        <p><strong>Call <a href="{PHONE_HREF}">{PHONE}</a>.</strong> We answer the phone live during business hours and return after-hours calls promptly. Emergency tarping within 24-48 hours during storm events.</p>

        <h2>What we handle</h2>
        <ul class="checks">
          <li>Wind-lifted, torn, or missing shingles</li>
          <li>Hail damage — granule loss, dented metal, cracked mats</li>
          <li>Fallen tree damage — roof, fascia, soffit, siding, gutters</li>
          <li>Active leaks and interior water damage</li>
          <li>Damaged or detached flashing around chimneys, vents, and skylights</li>
          <li>Storm-damaged gutters and downspouts</li>
          <li>Emergency tarping to prevent further water intrusion</li>
        </ul>

        <h2>The right order of operations</h2>
        <p>Most homeowners call their insurance company first, then a contractor. That order causes more claim problems than anything else we see. Here's what actually works:</p>

        <ol class="numbered">
          <li><strong>Stay off the roof.</strong> Damaged shingles are slippery and decking can be compromised. Document from ground level only.</li>
          <li><strong>Photograph everything fast.</strong> Date-stamped photos from multiple angles. Don't forget interior ceiling stains, fallen branches, hail marks on siding, dented gutters, and downspouts.</li>
          <li><strong>Get a free inspection from a licensed local roofer.</strong> We walk every plane, document with our own photos, and tell you honestly whether the damage meets a claim threshold.</li>
          <li><strong>File the claim with documentation in hand.</strong> Filing blind is how claims get under-paid or denied. We give you the photo report and a line-item estimate to file with.</li>
          <li><strong>Have your contractor meet the adjuster.</strong> This is the single biggest factor in fair payouts. Adjusters miss damage routinely; an experienced roofer on the ladder with them changes outcomes.</li>
          <li><strong>Get the work done by a local licensed contractor.</strong> Not a storm-chaser from out of state who knocked on your door. They disappear the moment the work gets complicated.</li>
        </ol>

        <h2>About storm chasers</h2>
        <p>After every major storm in Calvert County, out-of-state contractors flood the area. They door-knock, offer "free inspections," sometimes climb the roof and create damage that wasn't there, and pressure you to sign before you've thought about it. Real local contractors don't operate this way. If someone shows up uninvited offering to "handle everything," ask for their MHIC license number, verify it on the <a href="https://www.dllr.state.md.us/license/mhic/" target="_blank" rel="noopener">Maryland licensing site</a>, and look up their physical address. The good ones welcome the scrutiny.</p>
      </div>

      <aside class="prose-aside">
        <div class="aside-card urgent">
          <h4>Emergency response</h4>
          <p>Active leak? Call us first.</p>
          <a href="{PHONE_HREF}" class="btn btn-primary">{PHONE}</a>
        </div>
        <div class="aside-card download-card">
          <span class="dl-badge-pill">Free PDF · 2 pages</span>
          <h4>Storm Damage Checklist</h4>
          <p>The 9-point inspection adjusters look for. Print it, fill it out, claim with confidence.</p>
          <a href="/storm-checklist/" class="btn btn-download">{DL_ICON}<span>Download Checklist</span></a>
        </div>
        <div class="aside-card">
          <h4>Storm damage resources</h4>
          <ul>
            <li><a href="/insurance-claims/">Insurance claim guide</a></li>
            <li><a href="/learn/hail-damage-warning-signs/">Hail damage warning signs</a></li>
            <li><a href="/learn/storm-damage-insurance-claim/">How to file a claim</a></li>
          </ul>
        </div>
      </aside>
    </div>

    <h2 style="margin-top:80px">Storm damage FAQs</h2>
    <div class="faq-list">
      """ + "\n      ".join([f"""<details class="faq"><summary>{q}<span class="ic"><svg viewBox="0 0 14 14" aria-hidden="true"><path d="M7 1v12M1 7h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span></summary><div class="a">{a}</div></details>""" for q, a in storm_faqs]) + """
    </div>
  </div>
</section>
""" + cta_band("Active storm damage?", "Same business day response. Free inspection. We handle insurance documentation.", "Get an Emergency Inspection", "/contact/", with_download=True)

    build("/storm-damage/",
          "Storm Damage Roof Repair Maryland | Arndt Construction",
          "Hail, wind, and fallen-tree roof repair across Calvert County and Southern Maryland. Same-day response, emergency tarping, and full insurance documentation.",
          body,
          schemas=[
              service_schema("Storm Damage Roof Repair",
                             "Emergency storm damage repair, tarping, and insurance documentation across Calvert County and Southern Maryland.",
                             "/storm-damage/"),
              faq_schema(storm_faqs),
              breadcrumbs([("Home", "/"), ("Storm Damage", "/storm-damage/")]),
          ])

    # ============================================================
    # GUTTERS
    # ============================================================
    gutters_faqs = [
        ("Seamless or sectional gutters?",
         "Seamless every time. Sectional gutters leak at every joint, every winter. Seamless aluminum is custom-bent on-site to the exact length of your roof line — no joints between corners and downspouts."),
        ("Do leaf guards actually work?",
         "Good ones, yes. Cheap mesh and foam inserts cause more problems than they solve. We install professional-grade leaf guards (LeafFilter, LeafGuard, or comparable) with a screen that holds up to 10+ years of pine needles and oak leaves."),
        ("How often should gutters be cleaned?",
         "Twice a year minimum — late spring (after seed pods) and late fall (after leaf drop). Homes near pine trees may need quarterly cleaning. Properly installed leaf guards reduce this to inspection-only."),
    ]
    body = f"""
{crumbs_html([("Home", "/"), ("Services", "/roofing/"), ("Gutters", None)])}
{page_hero("Gutters", "Seamless Gutter Installation in Calvert County, MD",
           "Custom-bent seamless aluminum gutters with hidden hangers and professional leaf guards — protecting foundations, siding, and landscaping across Southern Maryland.",
           bg_image="/svc-gutters-hero.jpg")}

<section class="prose">
  <div class="container">
    <div class="prose-grid">
      <div class="prose-main">
        <h2>Why gutters matter more than most homeowners think</h2>
        <p>A failed gutter system doesn't just inconvenience you during rainstorms — it actively damages the most expensive parts of your home. Water that should be moving away from the foundation instead drops directly onto landscaping, splashes onto siding, soaks into fascia and soffit, and undermines the soil under your foundation. Over years, this leads to basement leaks, rotted trim, settling cracks in masonry, and expensive structural repairs.</p>

        <p>Good gutters are cheap insurance against all of that.</p>

        <h2>What we install</h2>
        <ul class="checks">
          <li>Seamless aluminum gutters (5" residential, 6" oversized)</li>
          <li>Hidden hangers — no exposed nail heads to rust</li>
          <li>Downspouts sized to your roof area (2x3 or 3x4)</li>
          <li>Splash guards on inside corners and roof valleys</li>
          <li>Professional leaf guards (optional but recommended near trees)</li>
          <li>Buried drainage extensions to move water away from foundation</li>
        </ul>

        <h2>Repair vs. replace</h2>
        <p>If your gutters sag, pull away from fascia, leak at every joint, overflow during normal rain, or are missing downspouts entirely — they should be replaced, not patched. Sectional gutters with 20+ year-old joints simply can't be reliably sealed. Seamless replacement is usually one full day of work.</p>

        <h2>What a good gutter install looks like</h2>
        <p>Proper slope (1/4" per 10 feet toward downspouts). Hidden hangers every 24 inches into solid framing. Downspouts terminated 4-6 feet from the foundation with extensions or buried drains. Splash guards in valleys and inside corners. No exposed sealant doing the work of proper installation.</p>
      </div>

      <aside class="prose-aside">
        <div class="aside-card">
          <h4>Free gutter estimate</h4>
          <p>On-site measure, written quote.</p>
          <a href="/contact/" class="btn btn-primary">Book estimate</a>
        </div>
        <div class="aside-card">
          <h4>Pairs well with</h4>
          <ul>
            <li><a href="/roofing/">New roof install</a></li>
            <li><a href="/siding/">Siding refresh</a></li>
          </ul>
        </div>
      </aside>
    </div>

    <h2 style="margin-top:80px">Gutter FAQs</h2>
    <div class="faq-list">
      """ + "\n      ".join([f"""<details class="faq"><summary>{q}<span class="ic"><svg viewBox="0 0 14 14" aria-hidden="true"><path d="M7 1v12M1 7h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span></summary><div class="a">{a}</div></details>""" for q, a in gutters_faqs]) + """
    </div>
  </div>
</section>
""" + cta_band("Protect your home from the ground up.", "Seamless gutters, custom-bent, professionally installed.", "Book a Free Estimate", "/contact/")

    build("/gutters/",
          "Seamless Gutter Installation Calvert County MD | Arndt",
          "Custom seamless aluminum gutters, hidden hangers, leaf guards, and downspout drainage. Installed across Calvert County and Southern Maryland. MHIC #115973.",
          body,
          schemas=[
              service_schema("Seamless Gutter Installation",
                             "Custom-bent seamless aluminum gutters with hidden hangers, downspouts, and professional leaf guards.",
                             "/gutters/"),
              faq_schema(gutters_faqs),
              breadcrumbs([("Home", "/"), ("Gutters", "/gutters/")]),
          ])

    # Continued in build_pages_3 to keep file readable
    import build_pages_3
    build_pages_3.run(build, breadcrumbs, service_schema, article_schema, faq_schema, crumbs_html, cta_band, page_hero, REVIEW_MODAL, BASE_URL, SITE_NAME, PHONE, PHONE_HREF, EMAIL, ADDRESS, LICENSE, LOCAL_BUSINESS, download_btn=download_btn)
