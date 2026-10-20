# Design references: premium kitchen and bath remodeling homepage

## What this pack is for
These references are for designing ONE master homepage template that will be filled with the content in
`homepage_kit/` for 100 independent US kitchen and bath remodelers. The page sells a $20k to $200k project to a
homeowner who is comparing two or three firms. It has to feel like a premium studio and still work as a
lead-generation page: the phone number and one clear "free estimate" action must never be more than a thumb away,
especially on a phone.

## The two sites the client chose
The client reviewed twelve shortlisted sites and chose these two. Design from them first; everything else in this
pack supports them.

1. **Harlow & Birch** (https://harlow-template.framer.website/, `sites/01_harlow-template_framer_website/`): the
   structure and the conversion system. Warm craftsman premium: espresso dark sections alternating with cream and
   white, honey-amber buttons, rounded photo cards, monospace eyebrows with a short rule, tight grotesk headlines.
   Header with announcement bar, phone and "Free estimate" always visible; a rating chip above the H1; two hero
   buttons and a proof row; service cards with timeline and "from" price chips; a before/after slider with a short
   case story; named owners and crew portraits; a numbered process with an expectation chip per step; a big rating
   block; a certifications grid; a dark guarantee band (fixed price, clean site, warranty) with both buttons; FAQ
   paired with "where we work" town chips; a multi-step estimate form with icon tiles; a closing band and a footer
   with an hours table.
2. **Interior ST** (https://interior-st-wbs.framer.website/, `sites/02_tpl_interior_st/`): the premium editorial
   layer. Dark espresso and warm cream with a terracotta accent; condensed uppercase headlines with a single swash
   script initial; testimonial with a photo and an overlapping terracotta quote card plus "4.9/5 average rating";
   three priced packages with inclusions; a dark FAQ accordion with hairlines; stats beside a cluster of rotated
   project photos; a closing call to action over a warm photo.

**The blend:** Harlow & Birch's page structure and conversion features, dressed with Interior ST's editorial
typography, dark/cream rhythm and terracotta or amber accent. Both are template demos with placeholder content and
stock or AI-looking photos: copy their layout, type and mechanics, not their words or images.

## Rules the template must follow
1. **Built for gaps.** Firms differ: some have 5 photos, 2 reviews, no owner photo, no street address, no prices.
   Every section must look complete with less content, and hide cleanly when its content is missing (no empty
   cards, no placeholder images). Price and timeline chips appear only when a firm publishes them.
2. **Re-skinnable.** Colours and fonts come from a few tokens (background, surface, ink, accent, accent ink, heading
   font, body font) so one layout works for every firm's brand colour and logo.
3. **Real photos.** Expect the firms' own, uneven project photos (phone shots, mixed light). Use consistent aspect
   ratios with object-fit crops, warm overlays for text, no tiny thumbnails.
4. **Mobile first.** Required on mobile: tap-to-call and estimate in the sticky header, plus a bottom Call / Estimate
   bar (both chosen sites lack it; add it), hero text and both buttons above the fold, 44px tap targets, large form
   inputs, no hover-only interactions.
5. **Fast.** No heavy video heroes or scroll-jacking. Subtle fades at most. Target a mobile PageSpeed score of 90+.
6. **Sections in this order** (matches the content files): header and utility bar, hero with trust badges, intro,
   services, why choose us, about the owner, process, gallery, testimonials, service area, FAQ, final call to
   action, footer.

## How to read this pack
1. `DESIGN_REFERENCES.md` (this file): the direction, the two chosen sites with full notes, every section crop with
   one line on why it is there, the Pinterest picks and the other gallery concepts with their source links.
2. `index.html`: the same material as a visual gallery. Open it in a browser.
3. `sites/`: the two chosen sites at desktop (1440 px), tablet (820 px) and mobile (390 px at 2x), full page plus
   the first screen and a scrolled screen.
4. `sections/<section>/`: section examples cut from live sites, desktop and mobile. Crops from sites other than the
   two chosen ones are there for one specific mechanic each (noted in the guide), not for their overall look.
5. `pinterest/`: the best designs found on Pinterest across 48 searches, chosen by eye.
6. `concepts/`: design concepts from Dribbble, Behance, Pinterest, Awwwards, One Page Love and the Framer and Webflow
   marketplaces.

## Avoid
- The loud mass-market look (heavy red blocks, many competing buttons) and the generic contractor template look
  (hard hats, stock handshakes, orange and grey).
- SaaS-looking pages: plain grotesk on white with no warmth. Keep the espresso, cream and amber or terracotta mood.
- Text over busy photos without an overlay; thin light-grey text; long titles that overflow on mobile.
