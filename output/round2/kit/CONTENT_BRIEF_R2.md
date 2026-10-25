# Round 2 homepage content brief (100 first websites for kitchen and bath businesses)

Each business in this round has no website at all. Its customers find it on Google Maps, Facebook or Instagram.
The homepage is its first real site, so it has to do three jobs: look like the business (its own photos, logo and
colours), prove it with real reviews and real projects, and turn a visit into a call or a quote request.

Same master structure as round 1, so the builder can reuse one template; the copy inside every section is written
from that business's own facts, services, towns, reviews and posts.

## Sources (in this order of trust)
1. Google Business Profile (`maps.json`): name, category, address or service area, phone, hours, rating and count,
   review texts and owner replies, photos.
2. Facebook and Instagram (`social.json` from the Gemini content dive): About text, services, towns, owner, years,
   licence, warranty, post captions and project photos, logo, colours, tagline, more Google reviews.
3. The research record (`research.json`): email and where it was published, owner names found in registries.

## Sections (keys of `content.json`, in this order)
| Key | What goes there | Length |
|---|---|---|
| `seo` | title_tag (main service + main town + name, 50 to 60 chars), meta_description (140 to 160), primary_keyword, 5 to 8 secondary_keywords, og_title, og_description | |
| `hero` | eyebrow (town or specialty), h1 (main service + town), subheadline (who they are, from facts), primary_cta (tap to call with the real phone), secondary_cta (free estimate form, only "free" if they say so), 3 to 4 trust_badges (rating and count, years, licence, owner-led: only evidenced), hero image from their own photos | h1 under 70 chars |
| `intro` | H2 and two short paragraphs on what makes this business different (built from its reviews and posts) | 100 to 150 words |
| `services` | 3 to 6 services they actually do, each with a 35 to 55 word blurb and one of their photos | |
| `why_choose_us` | 4 points, each tied to a fact or to what several reviews say | 20 to 40 words each |
| `about` | the owner or team story with the owner's name and role when known | 80 to 120 words |
| `process` | 4 or 5 steps; use their own words from posts or reviews when they describe how they work, otherwise a plain consultation, design, build, walkthrough flow with no invented promises | 15 to 30 words each |
| `gallery` | 6 to 10 of their own photos with descriptive alt text and short captions (room, material, town when known) | |
| `testimonials` | 3 to 6 real reviews quoted exactly, first name and last initial, source and date as shown | |
| `service_area` | H2, short paragraph, only towns they name or their GBP town and service area | 60 to 100 words |
| `faq` | 5 questions homeowners ask, answered only from their facts (hours, area, services, estimates, licence) | 40 to 70 words each |
| `final_cta` | closing H2, one line, button, phone | |
| `footer` | name, address or "Serving <area>", phone, email, socials, hours | |
| `schema_jsonld` | HomeAndConstructionBusiness with real values only, sameAs = Facebook / Instagram / Maps, no aggregateRating | |
| `brand` | logo file, palette (hex), suggested font pairing, tagline if they have one | |
| `outreach` | for the email: one specific detail of their work to mention, and the angle ("you have 46 five-star reviews and 250 photos but no website") | not on the page |
| `facts_used` | every factual claim with its source (Maps, Facebook post URL, Instagram, registry) | for checking |
| `missing` | facts the page would use but that were not found (left out, never invented) | for you |

## Rules
- Facts only. Every number, year, licence, warranty, price, award or town comes from the sources and is listed in
  `facts_used`. Unknown means left out and listed in `missing`.
- No website exists, so there are no "site defects" to fix: the angle is "your work deserves a site as good as your
  reviews".
- Unique per business: lead with what is specific (IKEA install specialist, tub reglazing, custom cabinet shop,
  veteran-owned, family crew, the curved-wall kitchen a reviewer described).
- One primary keyword (main service + main town), used in title, H1, first paragraph, one H2 and the hero alt text.
- NAP exactly as on Google. Real reviews only, quoted exactly, never edited.
- Plain, specific homeowner language. Short paragraphs. No em dashes. No "we pride ourselves", "second to none",
  "one-stop shop", "look no further".
