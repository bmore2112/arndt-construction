"""Remaining pages: insurance-claims, about, contact, reviews, gallery,
service-area + cities, learn + articles, local-partners, privacy, 404."""


def run(build, breadcrumbs, service_schema, article_schema, faq_schema, crumbs_html, cta_band, page_hero, REVIEW_MODAL, BASE_URL, SITE_NAME, PHONE, PHONE_HREF, EMAIL, ADDRESS, LICENSE, LOCAL_BUSINESS):

    # ============================================================
    # INSURANCE CLAIMS
    # ============================================================
    ins_faqs = [
        ("Should I call my insurance company or a roofer first?",
         "A licensed local roofer first. Calling insurance before you know what's actually damaged is the single most common mistake — claims get denied or under-paid because the homeowner couldn't describe what was wrong. A free inspection takes 30 minutes and gives you the documentation to file with."),
        ("Does filing a claim raise my premium?",
         "It depends on your carrier and your claim history. In Maryland, a single weather-related claim typically does not directly raise rates, but multiple claims in a short window can. The bigger risk is filing a claim that gets denied — that still goes on your record. This is exactly why a free inspection first matters."),
        ("What if my claim is denied?",
         "Denials are not final. If we documented damage that meets your policy's threshold and the adjuster missed it, we re-supplement the claim with our photo report and Xactimate-line estimate. Many denials reverse on supplement when the contractor is at the table."),
        ("Do I have to use the contractor my insurance recommends?",
         "No. Maryland law gives you the right to choose your own contractor. Insurance company preferred-vendor programs benefit the insurer, not always you. Pick a licensed local contractor you trust."),
    ]
    body = f"""
{crumbs_html([("Home", "/"), ("Insurance Claims", None)])}
{page_hero("Insurance Claims · Storm Damage",
           "Roof Insurance Claim Help in Maryland",
           "Storm damage? Get inspected first. Most homeowners call their insurance company before they know what's actually wrong — and that's how claims get denied or settled for half what they're worth. Here's the right order of operations.")}

<section class="prose">
  <div class="container">
    <div class="prose-grid">
      <div class="prose-main">
        <h2>The 5-step insurance claim process</h2>

        <ol class="numbered big">
          <li>
            <h3>Get a roof inspection first.</h3>
            <p>Before you ever pick up the phone to your insurer. A licensed contractor walks every plane of the roof and tells you honestly whether you have damage that meets a claim threshold. No damage = no claim filed = no premium hike risk.</p>
          </li>
          <li>
            <h3>Document everything, fast.</h3>
            <p>Exterior shots, ceiling stains inside the house, fallen branches in the yard, hail-strike marks on gutters and siding. Date-stamped. The first 24 hours after damage is when documentation is cleanest and most credible to an adjuster.</p>
          </li>
          <li>
            <h3>Don't sign with the first knock on your door.</h3>
            <p>Real local contractors don't door-chase after a storm. If someone shows up offering to "handle everything" before you've even called your insurer, walk away. Out-of-state storm-chasers disappear the moment work gets complicated.</p>
          </li>
          <li>
            <h3>Have your contractor meet the adjuster.</h3>
            <p>Adjusters miss damage every single day. Having an experienced roofer on the ladder with them is the biggest single factor in whether your claim pays out fairly — or under-pays you by thousands of dollars.</p>
          </li>
          <li>
            <h3>Let your contractor run the project.</h3>
            <p>Once the claim is approved, we manage code upgrades, permits, dumpsters, material delivery, and final inspection. You shouldn't be project-managing your own roof replacement on top of a stressful claim.</p>
          </li>
        </ol>

        <h2>What we do for you, specifically</h2>
        <ul class="checks">
          <li>Free on-site inspection with written photo report</li>
          <li>Xactimate-line estimate that adjusters can actually approve</li>
          <li>Meet with your adjuster on the roof if requested</li>
          <li>Supplement the claim if damage is missed or under-priced</li>
          <li>Manage permits, code upgrades, dumpsters, and material delivery</li>
          <li>Single point of contact from tear-off to final walk-through</li>
          <li>Code-compliant install with manufacturer + workmanship warranty</li>
        </ul>

        <h2>What we never do</h2>
        <ul class="checks bad">
          <li>Pressure you to sign before you've read the contract</li>
          <li>Promise to "waive your deductible" — that's insurance fraud</li>
          <li>File the claim on your behalf without your involvement</li>
          <li>Door-knock after storms</li>
          <li>Take a deposit larger than Maryland law allows</li>
        </ul>

        <h2>Read more</h2>
        <ul class="related">
          <li><a href="/learn/storm-damage-insurance-claim/">How to file a storm damage roof insurance claim — full walkthrough</a></li>
          <li><a href="/learn/hail-damage-warning-signs/">Hail damage on your roof: 7 warning signs to watch for</a></li>
          <li><a href="/storm-damage/">Storm damage repair services</a></li>
        </ul>
      </div>

      <aside class="prose-aside">
        <div class="aside-card urgent">
          <h4>Free claim review</h4>
          <p>30-minute inspection. Written photo report. No obligation.</p>
          <a href="/contact/" class="btn btn-primary">Book Inspection</a>
        </div>
        <div class="aside-card">
          <h4>Trust signals</h4>
          <ul>
            <li>Licensed — MHIC #115973</li>
            <li>Bonded &amp; insured</li>
            <li>Family-owned, Lusby MD</li>
            <li>7+ years on Maryland roofs</li>
          </ul>
        </div>
      </aside>
    </div>

    <h2 style="margin-top:80px">Insurance claim FAQs</h2>
    <div class="faq-list">
      """ + "\n      ".join([f"""<details class="faq"><summary>{q}<span class="ic">+</span></summary><div class="a">{a}</div></details>""" for q, a in ins_faqs]) + """
    </div>
  </div>
</section>
""" + cta_band("Storm damage? Don't call insurance yet.", "Book a free inspection first. We tell you honestly what you have before any claim is filed.", "Book a Free Inspection", "/contact/")

    build("/insurance-claims/",
          "Roof Insurance Claim Help in Maryland | Arndt Construction",
          "Step-by-step guide to filing a storm damage roof insurance claim in Maryland. Free inspection, photo documentation, Xactimate estimates, adjuster meetings. MHIC #115973.",
          body,
          schemas=[
              service_schema("Insurance Claim Assistance",
                             "Storm damage insurance claim assistance — free inspection, written photo report, Xactimate estimates, and on-site adjuster meetings.",
                             "/insurance-claims/"),
              faq_schema(ins_faqs),
              breadcrumbs([("Home", "/"), ("Insurance Claims", "/insurance-claims/")]),
          ])

    # ============================================================
    # ABOUT
    # ============================================================
    body = f"""
{crumbs_html([("Home", "/"), ("About", None)])}
{page_hero("About Arndt Construction",
           "Family-owned. Maryland-based. Roof up.",
           "Arndt Construction was founded by Nathaniel Arndt in Lusby, Maryland, to do contracting the way it should have been done all along — honestly, locally, and on time.")}

<section class="prose">
  <div class="container">
    <div class="prose-grid">
      <div class="prose-main">
        <h2>Who we are</h2>
        <p>Arndt Construction is a family-owned roofing, siding, gutter, and storm-restoration company based in Lusby, Maryland — Calvert County, on the Patuxent side of the Bay. We've been working on Mid-Atlantic roofs since 2019, and we've stayed deliberately small. One owner, one direct phone number, one crew. When you call, you're talking to someone who's been on the roofs we're talking about.</p>

        <h2>Why family-owned matters</h2>
        <p>The roofing industry in the U.S. has consolidated rapidly over the last decade — private-equity-owned roll-ups, national franchises, and out-of-state storm chasers all show up after every weather event. Their model depends on volume, sales pressure, and minimizing time on each job. Our model depends on the opposite: doing it right the first time and earning the next customer through the work itself.</p>

        <p>If you've ever felt rushed, upsold, or talked-down-to by a contractor, you understand why this matters. We answer the phone live during business hours. We give written estimates before you sign anything. We don't pressure-close on the first visit. We do not subcontract the work to crews we don't know.</p>

        <h2>Licensed, bonded, insured — and willing to prove it</h2>
        <ul class="checks">
          <li>Maryland Home Improvement Commission (MHIC) license <strong>#115973</strong> — verifiable on the <a href="https://www.dllr.state.md.us/license/mhic/" target="_blank" rel="noopener">Maryland licensing site</a></li>
          <li>General liability insurance — proof on request</li>
          <li>Workers' compensation coverage on every crew member</li>
          <li>Surety bonded for residential home improvement work</li>
          <li>A+ rating with the Better Business Bureau</li>
        </ul>

        <h2>What we believe about the work</h2>
        <p>A roof is the single most important thing on your house. It protects everything inside, including the most expensive things you own and the people you love most. Doing it cheaply, with bad shingles, by a crew that's gone tomorrow, is not actually saving anyone money — it's deferring a much larger bill onto your future self.</p>

        <p>We install systems with manufacturer warranties, by people who have stood behind their work for years. We use proper underlayment. We replace bad decking when we find it. We install ridge ventilation that actually meets code. We document the install with photos so you have a record. None of that is exotic. It's what every roof installation should be.</p>

        <h2>Where we work</h2>
        <p>Calvert County is home — Lusby, Solomons, Prince Frederick, Huntingtown, Dunkirk, Owings, Chesapeake Beach, St. Leonard. We also serve neighboring counties in Southern Maryland (St. Mary's, Charles), parts of Anne Arundel, Prince George's, and Queen Anne's. If you're a little outside that radius, call us anyway — we travel for the right job, and for storm response we routinely cover further out.</p>

        <p>See the full <a href="/service-area/">service area map</a>.</p>
      </div>

      <aside class="prose-aside">
        <div class="aside-card">
          <h4>Get in touch</h4>
          <p><strong>{PHONE}</strong><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <p>Mon – Sun · 9 AM – 5 PM<br>{ADDRESS}</p>
        </div>
        <div class="aside-card">
          <h4>Reviews</h4>
          <p>Five-star reviews from real Maryland homeowners.</p>
          <a href="/reviews/" class="btn btn-ghost">Read reviews</a>
        </div>
      </aside>
    </div>
  </div>
</section>
""" + cta_band("Want to put us on your project?", "Free on-site inspection, written estimate, same-business-day callback.", "Book an Inspection", "/contact/")

    org_schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": SITE_NAME,
        "url": BASE_URL + "/",
        "logo": BASE_URL + "/arndt-logo-cropped.png",
        "founder": {"@type": "Person", "name": "Nathaniel Arndt"},
        "foundingDate": "2019",
        "address": LOCAL_BUSINESS["address"],
        "telephone": "+14436247508",
        "email": EMAIL,
        "sameAs": LOCAL_BUSINESS["sameAs"],
    }

    build("/about/",
          "About Arndt Construction | Family-Owned MD Roofer",
          "Family-owned Maryland roofing and siding contractor based in Lusby, Calvert County. Founded by Nathaniel Arndt in 2019. Licensed MHIC #115973, bonded, insured.",
          body,
          schemas=[org_schema, breadcrumbs([("Home", "/"), ("About", "/about/")])])

    # ============================================================
    # CONTACT
    # ============================================================
    body = f"""
{crumbs_html([("Home", "/"), ("Contact", None)])}
{page_hero("Contact",
           "Get a hard-honest estimate.",
           "Tell us what's going on with the house. We'll be out within the week with a real number — and the photos to back it up.")}

<section id="contact-page">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-side">
        <div class="contact-meta">
          <div class="meta-row"><span class="k">Call</span><a class="v" href="{PHONE_HREF}">{PHONE}</a></div>
          <div class="meta-row"><span class="k">Email</span><a class="v" href="mailto:{EMAIL}" style="font-size:16px;word-break:break-all">{EMAIL}</a></div>
          <div class="meta-row"><span class="k">Hours</span><span class="v">Mon – Sun · 9 AM – 5 PM</span></div>
          <div class="meta-row"><span class="k">Office</span><span class="v" style="font-size:18px">{ADDRESS}</span></div>
          <div class="meta-row"><span class="k">License</span><span class="v">{LICENSE} · Bonded &amp; Insured</span></div>
        </div>

        <div class="map-wrap" style="margin-top:32px">
          <iframe src="https://www.google.com/maps?q=Lusby,+MD+20657&amp;z=10&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Arndt Construction service area" allowfullscreen></iframe>
        </div>
      </div>

      <form class="estimate" action="mailto:{EMAIL}" method="post" enctype="text/plain">
        <div class="field"><label for="fn">First name</label><input id="fn" name="First name" type="text" required autocomplete="given-name"/></div>
        <div class="field"><label for="ln">Last name</label><input id="ln" name="Last name" type="text" required autocomplete="family-name"/></div>
        <div class="field"><label for="em">Email</label><input id="em" name="Email" type="email" required autocomplete="email"/></div>
        <div class="field"><label for="ph">Phone</label><input id="ph" name="Phone" type="tel" autocomplete="tel"/></div>
        <div class="field full"><label for="ad">Property address</label><input id="ad" name="Property address" type="text" autocomplete="street-address"/></div>
        <div class="field"><label for="sv">Service</label><select id="sv" name="Service"><option>Roofing</option><option>Siding</option><option>Storm damage repair</option><option>Insurance claim</option><option>Gutters</option><option>Not sure — please advise</option></select></div>
        <div class="field"><label for="pt">Property type</label><select id="pt" name="Property type"><option>Residential</option><option>Commercial</option></select></div>
        <div class="field full"><label for="tm">Timeline</label><select id="tm" name="Timeline"><option>Emergency — ASAP</option><option>Within 30 days</option><option>1–3 months</option><option>Just exploring</option></select></div>
        <div class="field full"><label for="ms">What's going on?</label><textarea id="ms" name="Message" rows="3" placeholder="Describe the damage, age of the roof, anything the adjuster said…"></textarea></div>
        <div class="submit-row">
          <span class="fineprint">No spam, no upsell. We answer within one business day. By submitting, you agree to be contacted about your inquiry.</span>
          <button type="submit" class="btn btn-primary btn-lg">Send Estimate Request</button>
        </div>
      </form>
    </div>
  </div>
</section>
"""

    build("/contact/",
          "Contact Arndt Construction | Free Roof Estimate Maryland",
          "Get a free written roof or siding estimate from Arndt Construction. Call (443) 624-7508, email us, or send a request online. Serving Calvert County and Southern Maryland.",
          body,
          schemas=[breadcrumbs([("Home", "/"), ("Contact", "/contact/")])])

    # ============================================================
    # REVIEWS
    # ============================================================
    reviews_data = [
        ("fb-review-1-laurie.png", "Laurie Chrisman Chisenhall", "Dec 2025"),
        ("fb-review-2-shelby.png", "Shelby Jones", "Jul 2025"),
        ("fb-review-3-daniel.png", "Daniel Schlüter", "Jun 2025"),
        ("fb-review-5-brian.png", "Brian Byrnes", "Mar 2023"),
        ("fb-review-4-karen.png", "Karen Phillips", "Apr 2024"),
        ("fb-review-7-christopher.png", "Christopher Hillman", "Oct 2021"),
    ]
    voice_cards = "\n      ".join([
        f"""<a class="voice" href="https://www.facebook.com/ArndtConstruction/reviews/" target="_blank" rel="noopener"><img src="/{img}" alt="{name} recommends Arndt Construction" loading="lazy"/><div class="meta"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12c0-5.5-4.5-10-10-10S2 6.5 2 12c0 5 3.7 9.1 8.4 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7C18.3 21.1 22 17 22 12z"/></svg><span class="who">{name}</span><span class="when">{when}</span></div></a>"""
        for img, name, when in reviews_data
    ])

    body = f"""
{crumbs_html([("Home", "/"), ("Reviews", None)])}
{page_hero("Reviews", "What the neighbors say.",
           "Verified five-star reviews from Maryland homeowners. Real names, real jobs, in their own words. Tap any review to read it on Facebook.")}

<section class="prose">
  <div class="container">
    <div class="sec-head-row">
      <button class="review-trigger" type="button" data-open-review>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279L12 19.446l-7.416 3.967 1.48-8.279L0 9.306l8.332-1.151z"/></svg>
        Leave us a Review
      </button>
    </div>
    <div class="voices">
      {voice_cards}
    </div>

    <div class="prose-block" style="margin-top:80px;text-align:center">
      <h2>Where to find more reviews</h2>
      <p>We're listed on Facebook, Google, and Yelp. Real customer reviews on each.</p>
      <div class="review-options" style="max-width:560px;margin:32px auto 0;display:flex;flex-direction:column;gap:12px">
        <a class="review-opt" href="https://www.facebook.com/ArndtConstruction/reviews/" target="_blank" rel="noopener">
          <div class="icon f"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12c0-5.5-4.5-10-10-10S2 6.5 2 12c0 5 3.7 9.1 8.4 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7C18.3 21.1 22 17 22 12z"/></svg></div>
          <div class="body"><div class="name">Facebook</div><div class="desc">See all reviews on our Facebook page</div></div>
        </a>
        <a class="review-opt" href="https://www.google.com/search?q=Arndt+Construction+Lusby+MD+reviews" target="_blank" rel="noopener">
          <div class="icon g"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg></div>
          <div class="body"><div class="name">Google</div><div class="desc">Find us on Google and leave a review</div></div>
        </a>
        <a class="review-opt" href="https://www.yelp.com/biz/arndt-construction-lusby" target="_blank" rel="noopener">
          <div class="icon y"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14.5 13.6l4.1 1.3c.6.2.9.9.6 1.5l-1.8 3.5c-.3.6-1.1.7-1.6.3l-3.2-2.8c-.7-.6-.3-1.7.6-1.8l1.3-.0zm-1.4-3l3.4-3c.5-.4 1.3-.2 1.6.4l1.6 3.6c.3.6-.2 1.3-.9 1.3l-4.4.4c-.9.1-1.4-1.1-.7-1.7l-.6-1zM12 12l-1-4.1c-.2-.6.3-1.2.9-1.2l4 .2c.7 0 1.1.7.7 1.3l-2.3 3.7c-.4.6-1.4.7-1.8.1l-.5 0zM10 14.1l-2.4 3.5c-.4.6-1.2.5-1.6 0L3.5 14.5c-.4-.5-.1-1.3.5-1.5l4.1-1c.9-.2 1.6.7 1.1 1.5l.8.6zm.6-3.5L7.4 8.1c-.5-.4-.4-1.2.2-1.5l3.5-1.8c.6-.3 1.4.1 1.4.8l.5 4.4c.1.9-1 1.4-1.7.8l-.7-.2z"/></svg></div>
          <div class="body"><div class="name">Yelp</div><div class="desc">Read and leave reviews on Yelp</div></div>
        </a>
      </div>
    </div>
  </div>
</section>
""" + REVIEW_MODAL

    build("/reviews/",
          "Customer Reviews | Arndt Construction Maryland",
          "Five-star reviews from real Maryland homeowners for roofing, siding, and storm damage work by Arndt Construction. Verified Facebook recommendations.",
          body,
          schemas=[breadcrumbs([("Home", "/"), ("Reviews", "/reviews/")])])

    # ============================================================
    # GALLERY
    # ============================================================
    gallery_items = [
        ("job-5.png", "01 · Re-roof", "2-Story Colonial"),
        ("job-3.png", "02 · Full Tear-off", "Architectural Asphalt"),
        ("job-1.png", "03 · Cabin Re-roof", "Wooded Lot"),
        ("job-2.png", "04 · Garage Refresh", "Roof &amp; Siding"),
        ("job-4.png", "05 · Low-Slope Re-roof", "Driveway-Level"),
        ("job-7.png", "06 · Re-roof + Detail", "2-Story Home"),
        ("job-6.png", "07 · Ridge &amp; Cap", "Ventilation"),
        ("job-9.png", "08 · Storm Damage", "Before"),
        ("job-8.png", "09 · Restored", "After"),
    ]
    tiles = "\n      ".join([
        f'<div class="tile"><img src="/{img}" alt="{tag} — {desc}" loading="lazy"/><div class="tile-cap"><span class="tag">{tag}</span><span>{desc}</span></div></div>'
        for img, tag, desc in gallery_items
    ])
    body = f"""
{crumbs_html([("Home", "/"), ("Gallery", None)])}
{page_hero("Recent work",
           "Real homes. Real before-and-afters.",
           "A look at recent re-roofs, siding refreshes, and storm restorations from across Maryland. No stock photos — every shot is from a job we ran ourselves.")}

<section class="prose">
  <div class="container">
    <div class="work-grid">
      {tiles}
    </div>
  </div>
</section>
""" + cta_band("Want your home in the next gallery?", "Book a free on-site inspection. We bring the camera.", "Book a Free Estimate", "/contact/")

    build("/gallery/",
          "Roofing &amp; Siding Project Gallery | Arndt Construction MD",
          "Before-and-after photos of recent roofing, siding, and storm restoration jobs by Arndt Construction across Calvert County and Southern Maryland.",
          body,
          schemas=[breadcrumbs([("Home", "/"), ("Gallery", "/gallery/")])])

    # ============================================================
    # SERVICE AREA HUB
    # ============================================================
    body = f"""
{crumbs_html([("Home", "/"), ("Service Area", None)])}
{page_hero("Service Area",
           "Where we work.",
           "Based in Lusby, MD, we serve Calvert County and the surrounding Southern Maryland region — residential and commercial. Don't see your town? Call us anyway. If we can't help, we'll point you to someone who can.")}

<section class="prose">
  <div class="container">
    <div class="areas-grid">
      <div class="areas-list">
        <h4>Counties</h4>
        <ul>
          <li>Calvert</li><li>St. Mary's</li><li>Charles</li><li>Anne Arundel</li><li>Prince George's</li><li>Queen Anne's</li>
        </ul>
        <h4>Towns we serve</h4>
        <ul class="full">
          <li><a href="/service-area/lusby/">Lusby</a></li>
          <li><a href="/service-area/solomons/">Solomons</a></li>
          <li><a href="/service-area/prince-frederick/">Prince Frederick</a></li>
          <li>Huntingtown</li><li>Dunkirk</li><li>Owings</li>
          <li>Chesapeake Beach</li><li>North Beach</li><li>St. Leonard</li>
          <li>California</li><li>Lexington Park</li><li>Leonardtown</li>
        </ul>
        <div class="areas-cta">
          <strong>Outside this list?</strong> Call <a href="{PHONE_HREF}" style="color:var(--accent);text-decoration:none;font-weight:600">{PHONE}</a> — we travel for the right job and storm response often extends further than our standard service map.
        </div>
      </div>
      <div class="map-wrap">
        <iframe src="https://www.google.com/maps?q=Lusby,+MD+20657&amp;z=9&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Arndt Construction service area centered on Lusby, Maryland" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</section>
""" + cta_band("Schedule across Southern Maryland.", "Free inspection, written estimate, same-business-day callback.", "Book Inspection", "/contact/")

    build("/service-area/",
          "Roofing Service Area: Calvert County &amp; Southern MD",
          "Arndt Construction serves Calvert County and Southern Maryland — Lusby, Solomons, Prince Frederick, Huntingtown, Chesapeake Beach, and the surrounding area.",
          body,
          schemas=[breadcrumbs([("Home", "/"), ("Service Area", "/service-area/")])])

    # ============================================================
    # CITY PAGES
    # ============================================================
    cities = [
        ("lusby", "Lusby", "20657",
         "Lusby sits on the southern tip of Calvert County, surrounded by water on three sides and shaded by mature oak and pine. The combination of waterfront wind exposure and heavy tree cover puts unique demands on local roofs — and we know them well, because it's our own zip code.",
         "Coastal wind exposure and tall pine debris mean ridge ventilation, properly sealed flashing, and routine gutter clearing matter more here than they do further inland. Most Lusby roofs we see are architectural asphalt installed within the last 15-20 years, often showing granule loss along the south-facing slopes.",
         "Cove Point · Drum Point · Solomons-adjacent · Patuxent River corridor"),
        ("solomons", "Solomons", "20688",
         "Solomons is the maritime heart of Calvert County — a tight community of waterfront homes, marinas, and historic cottages around the Solomons Island village. Salt air, hurricane-season winds off the Patuxent, and proximity to the Chesapeake make the local roofing job different from anywhere else in the county.",
         "Many Solomons homes are older with steeper pitches, dormers, and original cedar trim. Replacement roofs need to respect the architectural character while standing up to actual conditions. We install algae-resistant architectural asphalt and copper-treated flashings for salt-air durability.",
         "Solomons Island · Pavilion Park · Calvert Marine Museum area"),
        ("prince-frederick", "Prince Frederick", "20678",
         "Prince Frederick is the county seat — a mix of newer single-family neighborhoods, established subdivisions, and commercial buildings. Larger lots, more sun exposure, and a wider range of roof types make Prince Frederick a fairly typical Maryland suburban roofing market.",
         "We install architectural asphalt across most Prince Frederick neighborhoods, with a growing share of standing-seam metal on newer custom homes. Hail patterns track inland from the Bay, and we frequently document hail damage on Prince Frederick roofs that homeowners missed.",
         "Calvert County Government complex · Calvert Memorial Hospital area · Sixes Road corridor"),
    ]

    for slug, name, zipcode, intro, local_notes, landmarks in cities:
        local_business_city = dict(LOCAL_BUSINESS)
        local_business_city["@id"] = f"{BASE_URL}/service-area/{slug}/#business"
        local_business_city["areaServed"] = [{"@type": "City", "name": f"{name}, MD"}]

        body = f"""
{crumbs_html([("Home", "/"), ("Service Area", "/service-area/"), (name, None)])}
{page_hero(f"{name}, MD · {zipcode}",
           f"Roofing &amp; Siding Contractor in {name}, Maryland",
           intro)}

<section class="prose">
  <div class="container">
    <div class="prose-grid">
      <div class="prose-main">
        <h2>Local roofing notes for {name}</h2>
        <p>{local_notes}</p>

        <h2>Areas we serve around {name}</h2>
        <p>{landmarks}</p>

        <h2>What we install for {name} homes</h2>
        <ul class="checks">
          <li><a href="/roofing/">Architectural shingle &amp; metal roofing</a></li>
          <li><a href="/siding/">Vinyl, fiber cement &amp; cedar siding</a></li>
          <li><a href="/storm-damage/">Storm damage repair &amp; emergency response</a></li>
          <li><a href="/gutters/">Seamless aluminum gutters</a></li>
          <li><a href="/insurance-claims/">Insurance claim documentation</a></li>
        </ul>

        <h2>Why local matters</h2>
        <p>We live in Calvert County. Our MHIC license ({LICENSE}) is registered in Maryland and verifiable on the state site. Our crew can be on a {name} roof within hours of a storm event — not days, like out-of-state contractors who follow storms across the country and disappear when work gets complicated.</p>
      </div>

      <aside class="prose-aside">
        <div class="aside-card">
          <h4>Free inspection in {name}</h4>
          <p>On-site, no obligation, written report.</p>
          <a href="/contact/" class="btn btn-primary">Book inspection</a>
        </div>
        <div class="aside-card">
          <h4>Phone</h4>
          <p><a href="{PHONE_HREF}" style="color:var(--accent);font-weight:600;font-size:18px">{PHONE}</a></p>
          <p>Mon – Sun · 9 AM – 5 PM</p>
        </div>
      </aside>
    </div>
  </div>
</section>
""" + cta_band(f"Need a roofer in {name}?", "Free inspection, written estimate, no pressure.", "Book Inspection", "/contact/")

        build(f"/service-area/{slug}/",
              f"Roofing Contractor in {name}, MD | Arndt Construction",
              f"Local roofing, siding, and storm damage contractor serving {name}, Maryland ({zipcode}). Family-owned, MHIC-licensed (#115973), bonded, insured.",
              body,
              schemas=[
                  local_business_city,
                  breadcrumbs([("Home", "/"), ("Service Area", "/service-area/"), (name, f"/service-area/{slug}/")]),
              ])

    # ============================================================
    # LEARN HUB
    # ============================================================
    body = f"""
{crumbs_html([("Home", "/"), ("Learn", None)])}
{page_hero("Learning Center",
           "Stories from the roof.",
           "Field notes, storm-season guides, and education for Maryland homeowners. Written by people who actually do the work, not SEO writers who've never been on a ladder.")}

<section class="prose">
  <div class="container">
    <div class="posts">
      <a class="post" href="/learn/storm-damage-insurance-claim/">
        <div class="post-meta"><span class="cat">Insurance Claims</span><span class="dot"></span><span>8 min read</span></div>
        <h3>How to file a storm damage roof insurance claim in Maryland.</h3>
        <p>A step-by-step walkthrough of what to do (and what NOT to do) in the first 48 hours after wind or hail damage.</p>
        <span class="post-link">Read the guide</span>
      </a>
      <a class="post" href="/learn/architectural-vs-3tab-shingles/">
        <div class="post-meta"><span class="cat">Roofing 101</span><span class="dot"></span><span>6 min read</span></div>
        <h3>Architectural vs. 3-tab shingles: which lasts longer?</h3>
        <p>Salt air, humid summers, freeze-thaw winters — we break down lifespan, cost, and warranty differences for Mid-Atlantic homes.</p>
        <span class="post-link">Read the guide</span>
      </a>
      <a class="post" href="/learn/hail-damage-warning-signs/">
        <div class="post-meta"><span class="cat">Storm Damage</span><span class="dot"></span><span>7 min read</span></div>
        <h3>Hail damage on your roof: 7 warning signs to watch for.</h3>
        <p>Hail damage isn't always obvious from the ground. Here's what to look for and when to call a contractor.</p>
        <span class="post-link">Read the guide</span>
      </a>
    </div>
  </div>
</section>
""" + cta_band("Have a question we haven't covered?", "Call or send a message — we answer same business day.", "Get in Touch", "/contact/")

    build("/learn/",
          "Roofing &amp; Insurance Learning Center | Arndt Construction",
          "Educational guides for Maryland homeowners on roofing, siding, storm damage, and insurance claims. Written by people who actually do the work.",
          body,
          schemas=[breadcrumbs([("Home", "/"), ("Learn", "/learn/")])])

    # ============================================================
    # LEARN ARTICLES
    # ============================================================
    article_storm_faqs = [
        ("Can I file a roof claim if my roof is 20 years old?", "Yes — age doesn't disqualify a claim. What matters is whether the damage was caused by a covered event (wind, hail, falling object) versus normal wear. A free inspection from a licensed roofer documents which is which."),
        ("How long do I have to file a storm claim in Maryland?", "Most Maryland homeowner policies require notification within a 'reasonable time' after the event — typically 30-365 days depending on the carrier. Don't wait. Older damage gets harder to attribute to a specific storm."),
        ("Do I have to pay my deductible?", "Yes — by Maryland law and federal regulation. Any contractor who offers to 'waive' or 'eat' your deductible is committing insurance fraud and putting you in legal jeopardy. Walk away."),
    ]
    article_storm_body = f"""
{crumbs_html([("Home", "/"), ("Learn", "/learn/"), ("Storm Damage Insurance Claim", None)])}
<article class="article">
  <div class="container">
    <header class="article-head">
      <div class="article-meta"><span class="cat">Insurance Claims</span><span>·</span><span>8 min read</span><span>·</span><time datetime="2026-05-27">Updated May 27, 2026</time></div>
      <h1>How to File a Storm Damage Roof Insurance Claim in Maryland</h1>
      <p class="article-lede">Most homeowners file the wrong way — and lose thousands. Here's the right order of operations, from a licensed Maryland contractor (MHIC #115973) who runs this process every week.</p>
    </header>

    <div class="article-body">
      <p>If you're reading this, something happened to your house. Wind. Hail. A fallen tree. Maybe just an unfamiliar leak. You want to know what to do — and you probably want to know whether your insurance is going to cover any of it.</p>
      <p>Here's the truth: more than half of the homeowner-filed storm damage claims we see come in are filed the wrong way. They get denied, under-paid, or stretched out for months. Not because the damage wasn't real, but because the homeowner called insurance before they had any idea what was actually wrong. Without documentation, without an estimate, without a contractor in their corner.</p>
      <p>This is how to do it right.</p>

      <h2>Step 1: Don't call insurance yet</h2>
      <p>This is the single most counter-intuitive piece of advice in this guide. Every instinct tells you to call your insurance company immediately. Don't.</p>
      <p>Once you open a claim, that claim is on your record whether or not it pays out. A denied or withdrawn claim still counts in your loss history — and in some carriers' calculations, it affects rates. So before you call, you want to be sure:</p>
      <ul class="checks">
        <li>Damage actually exists and meets your deductible threshold</li>
        <li>You have photos that clearly attribute it to a recent storm event</li>
        <li>You have a written estimate of repair cost from a licensed contractor</li>
      </ul>
      <p>If any of those are missing, calling insurance is premature.</p>

      <h2>Step 2: Document everything within 24 hours</h2>
      <p>From the ground, walk the perimeter of your house. Take date-stamped photos of:</p>
      <ul class="checks">
        <li>Every side of the home, including the roof line from a distance</li>
        <li>Any fallen branches, including the ground around them (shows recency)</li>
        <li>Hail-strike marks on gutters, siding, AC condenser fins, and outdoor surfaces</li>
        <li>Interior ceiling stains, especially in attic spaces</li>
        <li>Damaged or detached flashing around chimneys, vents, skylights</li>
        <li>Anything torn, dented, or displaced that wasn't before</li>
      </ul>
      <p>Don't climb on the roof yourself. Damaged shingles are slippery and roof decking can be compromised after a storm. Photograph from windows, balconies, or with a long-pole camera if you have one. The actual roof-walk inspection is the contractor's job.</p>

      <h2>Step 3: Free inspection from a licensed local roofer</h2>
      <p>Pick someone with a verifiable Maryland Home Improvement Commission (MHIC) license, local physical address, real reviews from real homeowners, and the willingness to give you a written report — not just a verbal "looks like you've got hail damage."</p>
      <p>A real inspection takes 30-45 minutes. The roofer walks every plane of the roof, photographs damage with their own camera, checks decking from the attic, and tells you honestly whether what they found meets a claim threshold.</p>
      <p>If it doesn't, don't file. A "maybe" claim is worse than no claim.</p>
      <p>If it does, you now have:</p>
      <ul class="checks">
        <li>A written photo report</li>
        <li>A line-item estimate (Xactimate-style) of repair cost</li>
        <li>An experienced advocate who can be in the room with you and the adjuster</li>
      </ul>

      <h2>Step 4: File the claim with documentation in hand</h2>
      <p>Now you call your insurance company. You tell them the date of the event, what you observed, and that you have photos and a contractor's estimate ready to share. You schedule an adjuster visit.</p>
      <p>The most important question to ask: <em>"When can I have my contractor present for the adjuster's inspection?"</em></p>
      <p>This single question changes outcomes more than anything else in the process. Most homeowners don't know they can have their contractor at the inspection. The adjuster won't volunteer it. But it's allowed under every Maryland policy we've ever seen, and it's the difference between a fair payout and an under-paid one.</p>

      <h2>Step 5: Adjuster + contractor on the roof</h2>
      <p>Adjusters work for the insurance company. They are not roofers. They are not adversaries either — but they are looking for reasons to scope the claim narrowly. An experienced roofer next to them catches damage they miss, documents code-required upgrades they don't know about, and supplements the scope before it's finalized.</p>
      <p>If the adjuster issues a scope you and your contractor disagree with, that's not the end. The contractor submits a supplement with photos and line items. Most reasonable supplements are approved. This is normal, expected, and how the process is designed to work.</p>

      <h2>Step 6: Approval, work, final inspection</h2>
      <p>Once the claim is approved, your contractor handles permits, code upgrades, dumpsters, material delivery, and final inspection. You handle the deductible. You should never pay more than the deductible on an approved claim, and you should never sign anything that says you'll cover overruns.</p>
      <p>Final walk-through with your contractor. Warranty paperwork. Insurance closes the claim. Done.</p>

      <h2>What this looks like in practice</h2>
      <p>A homeowner in Huntingtown called us after a derecho came through Calvert County. Their insurance had visited the day before, told them the damage was "minor," and offered to pay $1,800 toward repairs. The roof was 14 years old, three-tab shingles, with visible hail bruising on the south slope.</p>
      <p>We inspected for free, documented hail strikes across 3 of 4 slopes, photographed dented gutters and AC condenser fins (proving the hail event), wrote a supplemental scope, and met the adjuster on a return visit. Final approved claim: full roof replacement, code upgrades, gutters, and gutter guards. The homeowner paid their deductible. Nothing else.</p>
      <p>That's not unusual. It's what happens when the homeowner has a contractor in their corner from day one.</p>

      <h2>What never to do</h2>
      <ul class="checks bad">
        <li>Sign with a door-knocking contractor in the first 48 hours after a storm</li>
        <li>Let anyone climb on your roof without explicit written permission</li>
        <li>Accept a contractor's offer to "waive your deductible" — insurance fraud, federal crime</li>
        <li>File a claim without an inspection first</li>
        <li>Take the first adjuster scope as final without a contractor's review</li>
      </ul>

      <h2>FAQ</h2>
      <div class="faq-list">
        """ + "\n        ".join([f"""<details class="faq"><summary>{q}<span class="ic">+</span></summary><div class="a">{a}</div></details>""" for q, a in article_storm_faqs]) + """
      </div>
    </div>
  </div>
</article>
""" + cta_band("Storm damage on your home?", "Free inspection. Written photo report. No obligation.", "Book Inspection", "/contact/")

    build("/learn/storm-damage-insurance-claim/",
          "How to File a Storm Damage Roof Insurance Claim in Maryland",
          "Step-by-step guide to filing a storm damage roof insurance claim in Maryland. What to do in the first 48 hours and what mistakes to avoid. From a licensed MD contractor.",
          article_storm_body,
          schemas=[
              article_schema("How to File a Storm Damage Roof Insurance Claim in Maryland",
                             "Step-by-step guide to filing a storm damage roof insurance claim in Maryland.",
                             "/learn/storm-damage-insurance-claim/", "2026-05-27"),
              faq_schema(article_storm_faqs),
              breadcrumbs([("Home", "/"), ("Learn", "/learn/"), ("Storm Damage Claim Guide", "/learn/storm-damage-insurance-claim/")]),
          ],
          og_type="article")

    article_shingle_body = f"""
{crumbs_html([("Home", "/"), ("Learn", "/learn/"), ("Architectural vs. 3-Tab Shingles", None)])}
<article class="article">
  <div class="container">
    <header class="article-head">
      <div class="article-meta"><span class="cat">Roofing 101</span><span>·</span><span>6 min read</span><span>·</span><time datetime="2026-05-27">Updated May 27, 2026</time></div>
      <h1>Architectural vs. 3-Tab Shingles: Which Lasts Longer in Maryland?</h1>
      <p class="article-lede">Salt air, humid summers, freeze-thaw winters — the right shingle for a Mid-Atlantic home is not always the cheapest one. Here's a practical breakdown of the two most common types.</p>
    </header>
    <div class="article-body">
      <h2>The short answer</h2>
      <p>Architectural shingles last roughly twice as long as 3-tab shingles in Maryland's climate, cost about 20-30% more, look significantly better, and carry better warranties. For almost every homeowner reading this, architectural is the right answer.</p>
      <p>The longer answer — and the cases where 3-tab still makes sense — below.</p>

      <h2>3-tab shingles: what they are</h2>
      <p>3-tab shingles are the classic, flat, single-layer asphalt shingles you see on a lot of older homes. Each shingle has three "tabs" cut into it, creating the appearance of three separate shingles in a row. They were the standard residential roofing product from the 1960s through the early 2000s, and they're still available everywhere.</p>
      <p>Typical 3-tab specs:</p>
      <ul class="checks">
        <li>Lifespan: 15-20 years in the Mid-Atlantic (less near the coast)</li>
        <li>Wind rating: 60 MPH standard, 70 MPH with high-wind installation</li>
        <li>Warranty: typically 20-25 years (prorated)</li>
        <li>Cost: roughly $1.50-$2.00 per square foot installed</li>
      </ul>

      <h2>Architectural shingles: what they are</h2>
      <p>Architectural (also called "dimensional" or "laminated") shingles are multi-layer asphalt shingles with a tapered, three-dimensional appearance. They look more like cedar shake or slate from the street, and they're significantly thicker and heavier than 3-tabs.</p>
      <p>Typical architectural specs:</p>
      <ul class="checks">
        <li>Lifespan: 30-50 years in the Mid-Atlantic</li>
        <li>Wind rating: 110-130 MPH on impact-rated lines</li>
        <li>Warranty: 30 years to lifetime (non-prorated on premium lines)</li>
        <li>Cost: roughly $2.00-$3.50 per square foot installed</li>
      </ul>

      <h2>Why architectural wins for Maryland specifically</h2>
      <p>Three Maryland-specific factors push almost every honest contractor to recommend architectural:</p>
      <ol>
        <li><strong>Humidity and algae:</strong> Our summers grow moss and algae fast. Premium architectural lines include copper or zinc strips that fight algae growth. Most 3-tab lines do not.</li>
        <li><strong>Freeze-thaw:</strong> The Mid-Atlantic gets 20-40 freeze-thaw cycles per winter. Thinner 3-tab mats crack and lift faster than thicker architectural mats.</li>
        <li><strong>Wind events:</strong> Derechos, Nor'easters, and remnant hurricanes regularly produce 60+ MPH winds. 3-tab is the first product to lift and tear. Architectural's heavier mat and stronger seal strip hold significantly better.</li>
      </ol>

      <h2>When 3-tab still makes sense</h2>
      <ul class="checks">
        <li>You're listing the house in 6-12 months and just need to pass inspection</li>
        <li>Detached garage, shed, or outbuilding where you don't care about appearance or longevity</li>
        <li>Matching an existing 3-tab roof for a partial replacement (rare; usually full replacement is the better call)</li>
      </ul>
      <p>For your primary residence: skip 3-tab. The total cost-of-ownership math is not close.</p>

      <h2>Brands worth installing</h2>
      <p>We install GAF Timberline (Timberline HDZ is the workhorse for residential), CertainTeed Landmark, and Owens Corning Duration. All three are top-tier manufacturers with strong warranty programs. Brand matters less than installation quality — but those three are the safest defaults.</p>

      <h2>What the cost difference looks like</h2>
      <p>On a typical 2,000 sq ft Calvert County roof, the architectural upgrade adds roughly $1,500-$3,500 over 3-tab. Spread over a 30-year roof life vs. an 18-year roof life, you save money the moment you cross year 19 — and you spend that decade with a roof that looks dramatically better.</p>

      <h2>Want a real number for your home?</h2>
      <p>Book a free <a href="/contact/">on-site inspection</a> and we'll write you a line-item estimate with both options. No pressure to upgrade — just clarity on what each one actually costs.</p>
    </div>
  </div>
</article>
""" + cta_band("Want a roof estimate?", "Free inspection, both shingle options quoted side-by-side.", "Book Inspection", "/contact/")

    build("/learn/architectural-vs-3tab-shingles/",
          "Architectural vs. 3-Tab Shingles: Which Lasts Longer?",
          "Architectural vs. 3-tab shingles in Maryland — lifespan, cost, warranty, and Mid-Atlantic-specific factors that determine which is right for your home.",
          article_shingle_body,
          schemas=[
              article_schema("Architectural vs. 3-Tab Shingles: Which Lasts Longer in Maryland?",
                             "Architectural vs. 3-tab shingles in Maryland.",
                             "/learn/architectural-vs-3tab-shingles/", "2026-05-27"),
              breadcrumbs([("Home", "/"), ("Learn", "/learn/"), ("Architectural vs. 3-Tab", "/learn/architectural-vs-3tab-shingles/")]),
          ],
          og_type="article")

    article_hail_body = f"""
{crumbs_html([("Home", "/"), ("Learn", "/learn/"), ("Hail Damage Warning Signs", None)])}
<article class="article">
  <div class="container">
    <header class="article-head">
      <div class="article-meta"><span class="cat">Storm Damage</span><span>·</span><span>7 min read</span><span>·</span><time datetime="2026-05-27">Updated May 27, 2026</time></div>
      <h1>Hail Damage on Your Roof: 7 Warning Signs to Watch For</h1>
      <p class="article-lede">Hail damage isn't always obvious from the ground. Sometimes a hailstorm passes through and your roof looks identical from the street — but the shingles have already started failing. Here's what to look for.</p>
    </header>
    <div class="article-body">
      <p>Maryland gets hail. Not as much as Texas or Colorado, but enough — particularly during late-spring and early-summer storm fronts moving across the Bay. And unlike wind damage (which usually tears off shingles you can see from the street), hail damage often hides in plain sight until granule loss, mat damage, and accelerated aging show up two or three years later as leaks.</p>
      <p>If a hailstorm passed within the last 12 months, walk your house and look for these seven signs.</p>

      <h2>1. Dents on metal surfaces</h2>
      <p>Hail leaves clear, round dents on soft metal — your gutters, downspouts, AC condenser fins, metal roof flashing, vent caps, and aluminum siding. If any of those show fresh dents that weren't there before, the same storm hit your shingles too. Photograph everything you find.</p>

      <h2>2. Granule loss on shingles</h2>
      <p>Asphalt shingles are coated with mineral granules that protect the underlying mat from UV damage. Hail strikes knock these granules loose. You'll see them collecting at the base of downspouts, on splash blocks, and in your gutters. A handful of new granules in the gutter after a storm is normal weathering. A significant accumulation — enough to fill a coffee cup — is hail damage.</p>

      <h2>3. Bruises and craters on shingles</h2>
      <p>This is the most diagnostic sign — and the one homeowners can't reliably see from the ground. Hail bruises look like dark circular marks on the shingle surface, with the granules either gone or compressed into the mat. They're soft to the touch (you can feel the mat give slightly), unlike normal wear which is flat and hard.</p>
      <p>This is what a contractor is looking for during a hail inspection. If they're not on the roof checking, they're not doing a real inspection.</p>

      <h2>4. Cracks radiating from impact points</h2>
      <p>Larger hailstones can crack the shingle mat in a radial pattern from the impact point. These cracks are bad — they're entry points for water and they spread over time. Cracked shingles are also a clear basis for a full claim, not just a repair.</p>

      <h2>5. Damage to skylights, vent caps, and turbines</h2>
      <p>Plastic skylight domes crack from significant hail. Vent caps split or detach. Turbine vents stop spinning because their bearings have been hit. Walk the roof line from a distance and check whether anything that should be intact looks wrong.</p>

      <h2>6. New leaks 6-18 months after a storm</h2>
      <p>This is the cruel one. Hail can compromise the shingle mat without obvious immediate leaks. The damaged shingles continue to degrade under UV and freeze-thaw cycles, and water starts coming in months later — by which time linking the leak to the storm in an insurance claim is significantly harder.</p>
      <p>This is why post-storm inspections matter even if your roof looks fine. Documentation now beats documentation later.</p>

      <h2>7. Damage to neighbors' homes</h2>
      <p>Hail patterns are localized but not narrow. If your immediate neighbors have visible hail damage, replaced roofs after a recent storm, or active insurance claims in process — your home likely took similar impacts. Walk around the block. Talk to neighbors.</p>

      <h2>What to do if you suspect hail damage</h2>
      <ol class="numbered">
        <li><strong>Don't climb on the roof yourself.</strong> Damaged shingles are slippery.</li>
        <li><strong>Photograph everything from the ground.</strong> Date-stamp, multiple angles.</li>
        <li><strong>Don't call insurance yet.</strong> Get a free inspection first.</li>
        <li><strong>Schedule a free inspection</strong> with a licensed local roofer. <a href="/contact/">We do this for free across Calvert County</a>.</li>
        <li><strong>If damage is confirmed,</strong> file the claim with photos and an estimate ready. See our <a href="/learn/storm-damage-insurance-claim/">full insurance claim guide</a>.</li>
      </ol>

      <h2>When hail damage is too old to claim</h2>
      <p>Most Maryland policies require notification within 30 days to a year of the event, depending on the carrier. Once you can no longer reasonably attribute the damage to a specific storm — usually 12-24 months out — it becomes "wear and tear" and is no longer covered.</p>
      <p>That's why inspecting <em>now</em>, after a recent storm, is the right move. Documented damage is claimable. Two-year-old hidden damage is not.</p>
    </div>
  </div>
</article>
""" + cta_band("Recent hail storm in your area?", "Free roof inspection. We tell you honestly whether you have a claim.", "Book Inspection", "/contact/")

    build("/learn/hail-damage-warning-signs/",
          "Hail Damage on Your Roof: 7 Warning Signs | Arndt MD",
          "How to spot hail damage on your roof in Maryland. 7 warning signs, what to photograph, and how to document damage for an insurance claim.",
          article_hail_body,
          schemas=[
              article_schema("Hail Damage on Your Roof: 7 Warning Signs to Watch For",
                             "How to spot hail damage on your roof in Maryland.",
                             "/learn/hail-damage-warning-signs/", "2026-05-27"),
              breadcrumbs([("Home", "/"), ("Learn", "/learn/"), ("Hail Damage Signs", "/learn/hail-damage-warning-signs/")]),
          ],
          og_type="article")

    # ============================================================
    # LOCAL PARTNERS
    # ============================================================
    partners = [
        ("Plumbing", "Calvert Plumbing &amp; Drain", "Family-run plumbing service across Southern Maryland.", "#", "REPLACE — call partner for site URL"),
        ("Electrical", "Bay Country Electric", "Licensed residential and commercial electrician.", "#", "REPLACE — actual local electrician"),
        ("HVAC", "Patuxent Heating &amp; Air", "HVAC install, service, and emergency repair.", "#", "REPLACE — actual local HVAC contractor"),
        ("Painting", "Chesapeake Painting Co.", "Interior and exterior painting, southern MD.", "#", "REPLACE"),
        ("Landscaping", "Solomons Landscape &amp; Lawn", "Full-service landscaping, tree work, hardscape.", "#", "REPLACE"),
        ("Flooring", "Bay Hardwood &amp; Flooring", "Installation, refinishing, and repair.", "#", "REPLACE"),
        ("Tree Service", "Calvert Tree &amp; Removal", "Storm cleanup, removal, trimming.", "#", "REPLACE"),
        ("Masonry", "Patuxent Masonry &amp; Chimney", "Chimney repair, brick, stone, foundation.", "#", "REPLACE"),
    ]
    partner_cards = "\n      ".join([
        f"""<article class="partner-card"><div class="partner-cat">{cat}</div><h3>{name}</h3><p>{desc}</p><a href="{url}" target="_blank" rel="noopener nofollow" class="partner-link">Visit website</a><!-- {note} --></article>"""
        for cat, name, desc, url, note in partners
    ])
    body = f"""
{crumbs_html([("Home", "/"), ("Local Partners", None)])}
{page_hero("Local Partners",
           "Trusted Maryland trades we recommend.",
           "We're roofers and siders — but a healthy home depends on more than the envelope. Here are the local trades we trust to work alongside us in Calvert County. None of these are paid placements.")}

<section class="prose">
  <div class="container">
    <div class="partner-grid">
      {partner_cards}
    </div>

    <div class="prose-block" style="margin-top:80px">
      <h2>Are you a local trade?</h2>
      <p>We're always looking for additional trades to recommend to clients — particularly local, licensed, and insured businesses with strong reputations across Calvert, St. Mary's, Charles, and Anne Arundel counties. If you'd like to be considered for this page, send a message to <a href="mailto:{EMAIL}">{EMAIL}</a> with your license number, service area, and a few customer references. We vet every partner before listing.</p>
      <p>In exchange, we ask that you keep our number handy when you encounter roofing, siding, or storm-damage questions on your jobs — and that you list us on your "trusted local partners" page if you have one.</p>
    </div>
  </div>
</section>
""" + cta_band("Working on a Calvert County project?", "If we can help with the roofing or siding piece, let us know.", "Book Inspection", "/contact/")

    build("/local-partners/",
          "Trusted Local Trades in Calvert County, MD | Arndt Construction",
          "Local plumbers, electricians, HVAC, painters, and trades we trust across Calvert County and Southern Maryland. Vetted by Arndt Construction.",
          body,
          schemas=[breadcrumbs([("Home", "/"), ("Local Partners", "/local-partners/")])])

    # ============================================================
    # PRIVACY
    # ============================================================
    body = f"""
{crumbs_html([("Home", "/"), ("Privacy", None)])}
{page_hero("Privacy Policy",
           "Privacy Policy",
           "Last updated May 27, 2026.")}

<section class="prose">
  <div class="container" style="max-width:760px">
    <div class="article-body">
      <h2>Who we are</h2>
      <p>This website is operated by Arndt Construction, a family-owned roofing and siding contractor based at {ADDRESS}. License: {LICENSE}. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a> or {PHONE}.</p>

      <h2>What we collect</h2>
      <p>When you submit our estimate request form, we collect: your name, email, phone, property address, requested service type, property type, timeline, and any message you write. This information is sent directly to us by email — it is not stored in a database or shared with third parties.</p>
      <p>Our website does not use behavioral tracking, advertising cookies, or third-party analytics that personally identify you. Embedded content (Google Maps, fonts) may load resources from third-party servers; those services have their own privacy policies.</p>

      <h2>How we use your information</h2>
      <p>We use your contact information solely to respond to your inquiry, schedule an inspection, or follow up about a job we performed. We do not sell, rent, or share your information with marketing partners.</p>

      <h2>Your rights</h2>
      <p>You can request a copy of any information we have about you, ask us to correct it, or ask us to delete it, at any time, by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>. We respond within 30 days.</p>

      <h2>Reviews and testimonials</h2>
      <p>We display Facebook reviews on our site only with the reviewer's implicit permission (Facebook reviews are public). If you posted a review you'd like removed from this site, email us and we'll take it down within one business day.</p>

      <h2>Changes to this policy</h2>
      <p>If we update this policy, we'll update the "last updated" date at the top of this page. Material changes will be announced on our home page for 30 days.</p>
    </div>
  </div>
</section>
"""

    build("/privacy/",
          "Privacy Policy | Arndt Construction",
          "Privacy policy for the Arndt Construction website. What we collect, how we use it, your rights.",
          body,
          schemas=[breadcrumbs([("Home", "/"), ("Privacy", "/privacy/")])])

    # ============================================================
    # 404
    # ============================================================
    from pathlib import Path
    head_404 = """<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page Not Found | Arndt Construction</title><meta name="robots" content="noindex,follow"><link rel="icon" type="image/png" href="/arndt-logo-cropped.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="/styles.css">"""
    body_404 = f"""<header class="page-hero" style="text-align:center">
  <div class="container">
    <span class="eyebrow" style="color:var(--accent)">404 · Page Not Found</span>
    <h1>This roof doesn't exist.</h1>
    <p class="page-hero-lede">The page you're looking for isn't here. It may have moved, or you may have a stale link. Try one of these instead:</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin-top:32px">
      <a href="/" class="btn btn-primary btn-lg">Home</a>
      <a href="/contact/" class="btn btn-ghost btn-lg">Contact Us</a>
      <a href="{PHONE_HREF}" class="btn btn-ghost btn-lg">Call {PHONE}</a>
    </div>
  </div>
</header>"""

    # Use raw 404 (not directory-style)
    html_404 = f"""<!doctype html>
<html lang="en">
<head>
{head_404}
</head>
<body>
<nav class="nav" id="nav"><div class="container nav-inner"><a href="/" class="brand"><img src="/arndt-logo-cropped.png" alt="Arndt Construction"></a></div></nav>
{body_404}
<script src="/app.js" defer></script>
</body>
</html>"""
    Path("404.html").write_text(html_404, encoding="utf-8")
    print(f"  built /404.html                                    -> 404.html")
