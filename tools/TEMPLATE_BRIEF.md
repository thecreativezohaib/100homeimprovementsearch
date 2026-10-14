# Remodel 100 — top-30 template content capture (subagent)

Run date 2026-10-14. You receive verified prospects (all hard gates already passed). For each, capture the
content below in EXACTLY this shape so one website template can be filled 100 times. Use only their own site
(and the Google reviews given in the packet). Every field: source URL + verbatim text. Quotes are copied exactly.
Banned words in any field: likely, appears to, probably, presumably, seems, suggests. Unevidenced = "UNKNOWN".

Fields (one JSON object per prospect, appended as one line to the output file you are given):
- `id`
- `hero_headline_source`: {url, quote} — their own words describing what they do (home page H1/hero or tagline).
- `services_3`: list of 3 {name, url} — their three most prominent services, in their wording (nav order / home order).
- `gallery_urls_8`: use the 8 URLs given in the packet (`g7_urls`); replace any that do not load with others from
  their gallery, master size (Wix: drop `/v1/fill/...`; Squarespace: drop `?format=`; WordPress: drop `-WxH`).
- `before_after_pairs`: list of {before_url, after_url, page} where the site labels images as before/after; [] if none.
- `reviews_3`: 3 × {first_name, date, quote, source}. Use the Google reviews in the packet (reviewer FIRST name only;
  date = the Google relative timestamp plus "as of 2026-10-14") or dated testimonials on their site. Quote ≤ 20 words.
- `service_area`: {url, quote} — towns/counties they state they serve.
- `phone`: as published on their site, with URL.
- `cta_wording`: {url, quote} — their existing call to action button/heading text.
- `years_in_business`: {url, quote} ONLY if stated on their site, else "UNKNOWN".
- `licences_awards`: VERBATIM list of {text, url} for every licence number, award, certification, membership they
  publish (NARI, NKBA, BBB, Houzz awards, state licence numbers, Best of ...). If none, "NONE". Never add anything
  they have not published themselves.
- `outreach_angle`: 2–3 sentences, labelled OPINION, built from the measured G8 defect and any trigger event in the
  packet. Do not claim the defect costs them customers; state the defect.
