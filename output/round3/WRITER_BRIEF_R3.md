# Round 3 writer brief (read fully before writing)

You write one complete homepage per business folder under /home/user/100homeimprovementsearch/output/round3/kit/.
These are small kitchen and bath remodeling businesses with no working website.

Read first:
- /home/user/100homeimprovementsearch/output/round2/kit/CONTENT_BRIEF_R2.md (rules, section order, lengths, image plan)
- /home/user/100homeimprovementsearch/output/round2/kit/content_schema_r2.json (JSON shape of content.json)
- Format examples only (never copy wording): /home/user/100homeimprovementsearch/output/round3/kit/028_tile-envy-installation-co/content.json and content.md

Each folder has research.json, images/ (their own Google Maps photos, may be few or none), images.json and
contact_sheet.jpg (when there are images). Look at the contact sheet and individual images (Read tool) before placing any.

## Sources and honesty (strict)
- Facts come only from research.json "google" (category, rating_label, address, phone, service_area, hours,
  overview_text, about_text) and the Google reviews. overview_text and about_text often hold Google's description,
  services, service area and "From the business" text: read them.
- "antigravity_notes_unverified" came from another AI that mixed up businesses. Use a fact from it only if Google data
  or a review confirms it; otherwise leave it out and add to "missing": "to confirm with owner: <fact>".
- Town: if Google has an address, use it. If not, use the town from antigravity_notes_unverified only when the phone's
  area code belongs to that town's area (for example 919 Raleigh NC, 501 Little Rock AR). Then put the town in the title,
  H1, intro, service area, footer ("Serving <town>, <ST>") and schema areaServed, and add to missing: "town from earlier
  research, matches the phone's area code: confirm with owner". If it does not match, name no town and say so in missing.
- Testimonials: the Google reviews in research.json, word for word (never edited or shortened into new wording), name
  as first name plus last initial (Jane D.; a single name stays as written), source "Google", date exactly as shown.
  Use every positive review available, up to 6. A business with 1 or 2 reviews gets 1 or 2 testimonials. Never leave a
  review out because of its wording: the banned-phrase rule applies only to our own copy.
- A clearly negative review (1 or 2 stars, accusations) is never quoted; put a short warning at the top of missing.
- Footer email = research.json email.address. Add to missing: "confirm email <address> (published at <published_at>)".
  If the email, Facebook link or Instagram link carries a clearly different business name than Google's title, also put
  "email/social may belong to a different business: <detail>" at the top of missing and leave that social link out of
  footer.socials and schema sameAs.
- No invented numbers, years, licences, warranties, prices or towns. "Free estimate" only if a source says so;
  otherwise "Request an estimate".
- Name, address and phone exactly as on Google. Phone links tel:+1XXXXXXXXXX.
- Write plain, warm, specific American English. Lead with what is specific to this business (what its reviews and
  photos show). Every page and every service blurb must be different; never reuse a sentence across services or
  pages. Proper capitalisation. No em dashes. Never in our own copy: "look no further", "one-stop shop", "we pride
  ourselves", "second to none", "top-notch", "unparalleled".
- No aggregateRating in schema_jsonld.
- If Google's category or reviews show the business does little or no kitchen or bath work (only painting, roofing,
  decks, etc.), still write the page around what they do, and add "kitchen and bath work not shown on Google" at the
  top of missing.

## Image plan
Key image_plan, plus the matching image fields inside hero, services, about, gallery and final_cta.
- Real photos from images/ wherever one fits: hero = their best finished kitchen or bath; service card = a photo of
  that service; about = team, truck, shop or a project; gallery = all usable real project photos (6 to 10 if they have
  them; fewer is fine), each with descriptive alt and a short caption.
- Skip photos that are not their work, are poor, or come from a negative review; list them in images_not_to_use with
  the reason.
- Where no real photo fits (never in the gallery): "file": null, "source": "ai", "ai_file_name" (for example
  ai_service_showers.jpg) and "ai_prompt": one paragraph starting "Photorealistic photo of", a finished space matching
  the service, the local housing style and the page palette, natural light, ending "no people, no faces, no text, no
  logos, no brand names" and the aspect ratio (hero 16:9, service 4:3, about 4:5, CTA 21:9). AI alt text describes the
  scene plainly and never claims it is their work.
- With fewer than 6 real project photos, the gallery is shorter (or empty) and missing says "needs project photos".
- brand: logo only if images/ has a real logo; palette (4 hex) from the logo or their photos (or proposed from the
  trade and region when there are no photos) with palette_note saying where it came from; Google Fonts pairing;
  tagline null unless they have one; style_direction.
- If Google lists a website for them that no longer works, mention it in outreach.angle ("the website on your Google
  listing no longer loads").

## Output and checks
Write content.json (valid JSON, schema keys, "id" = folder name) and content.md (readable page: each section with its
copy and the image file for each slot, then image plan, facts_used with sources, and missing) into each folder.
Before finishing, check every content.json: valid JSON; every "file" in image_plan exists; no em dash anywhere; no
banned phrase in our own copy; title_tag 50 to 60 characters; meta_description 140 to 160 and a complete sentence;
H1 under 70 characters; every testimonial text appears exactly in research.json google.reviews; footer phone digits
equal google.phone digits; no aggregateRating.
Reply with one line per folder: folder, real photos used, AI slots, testimonials, and anything important unresolved.
