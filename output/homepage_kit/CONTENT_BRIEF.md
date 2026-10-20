# Homepage content brief (one master template, 100 unique homepages)

This brief is what every homepage in `content/` was written to. Give it to the builder together with the data files.

## Who the pages are for
Independent kitchen and bath remodellers in the US. Their buyers are homeowners planning a project worth tens of
thousands of dollars. They compare two or three firms, read Google reviews, look at real project photos, and want
to know who will actually run the job. Most of these firms already have the raw material (good reviews, real photos,
a named owner) but their current sites are slow on mobile, bury the phone number, or never say where they work.
The new homepage fixes that and turns visits into calls and quote requests.

## Section order of the master template
Every `content/<id>.json` fills these keys in this order. Keep the order in the template; the copy inside each key
is unique per business.

| Key | What goes there | Length |
|---|---|---|
| `seo.title_tag` | primary service + main city + brand | 50 to 60 characters |
| `seo.meta_description` | what they do, where, one proof point, call to action | 140 to 160 characters |
| `seo.primary_keyword`, `seo.secondary_keywords` | one main phrase, 5 to 8 supporting local phrases | |
| `hero.eyebrow` | short location or specialty line | under 40 characters |
| `hero.h1` | primary keyword and city, in plain words | under 70 characters |
| `hero.subheadline` | who they are and why them, from facts | 1 to 2 sentences |
| `hero.primary_cta`, `hero.secondary_cta` | call and quote buttons with the real phone number | |
| `hero.trust_badges` | 3 to 4 short facts (Google rating and count, year founded, licence, owner-led) | only evidenced facts |
| `hero.image` | one of their own original project photos, with alt text | |
| `intro` | H2 and two short paragraphs on the firm's angle | 100 to 150 words |
| `services` | 3 to 6 services they actually list, each with a 35 to 55 word blurb and a photo | |
| `why_choose_us` | 4 points, each tied to a fact from their site or reviews | 20 to 40 words each |
| `about` | owner or founder story, naming the owner and role | 80 to 120 words |
| `process` | 4 or 5 steps, from their own process page when they have one | 15 to 30 words each |
| `gallery` | 6 to 8 of their own photos with descriptive alt text and short captions | |
| `testimonials` | 3 real Google reviews, quoted exactly, first name and last initial only | |
| `service_area` | H2, a short paragraph and only the towns they name or their GBP city | 60 to 100 words |
| `faq` | 5 local questions homeowners ask, answered from their facts | 40 to 70 words each |
| `final_cta` | closing H2, one line, button, phone | |
| `footer` | name, address, phone, email, socials | |
| `schema_jsonld` | LocalBusiness / HomeAndConstructionBusiness markup with real values only | |
| `conversion_notes` | the measured defects of their current site and what this homepage changes | for you, not for the page |
| `facts_used` | every factual claim on the page with the URL it came from | for checking |
| `missing` | facts the page would use but that were not found (left out, not invented) | for you to fill |

## SEO rules
- One clear primary keyword per page, built from their main service and main city (for example "kitchen remodeling
  Raleigh"). Use it in the title tag, H1, first paragraph, one H2 and the image alt text of the hero, and nowhere it
  reads unnaturally.
- Secondary keywords are real local variations: the second service (bathroom remodel, walk-in shower), nearby towns
  they name, and intent phrases (contractor, company, near me only once).
- Name, address and phone written exactly as on the Google Business Profile (NAP consistency).
- Real reviews and real photos only. Google ignores self-serving review markup on a business's own site, so
  `schema_jsonld` carries no `aggregateRating`; the rating appears as visible text in the trust badges instead.
- Headings in order (one H1, then H2s per section). Short paragraphs. Plain, specific language a homeowner uses.
- Every photo gets descriptive alt text naming the room, a material or feature, and the town when known.
- Phone number as a tap-to-call link at the top and bottom; a short quote form is the secondary action.

## Writing rules
- Facts only. Every number, year, licence, award, warranty, price or town must come from the firm's own site, its
  Google profile or its reviews, and is listed in `facts_used`. If something is not known, leave it out and list it
  under `missing`. Never invent a year founded, a licence number, an award, a warranty term or a price.
- Unique per business. Build the page around what is specific to that firm: the owner's background, their specialty
  (one-day baths, custom cabinetry, aging-in-place, design-build, showroom), the towns they work in, the projects in
  their photos and the words their customers use in reviews. Two pages in this kit should never share a paragraph.
- Testimonials are quoted exactly (trimmed only at sentence boundaries), with first name and last initial.
- No em dashes. No filler phrases ("look no further", "one-stop shop", "we pride ourselves", "dream home" more than
  once, "second to none"). Reading level around grade 8. American spelling.
- Calls to action name the next step plainly ("Call Mike at (614) 555-0100", "Request a free design consultation"),
  and only promise what the firm itself offers on its site (for example a free estimate only if they say so).

## Files
- `data/<id>.json`: everything gathered for one business: the full crawl of its own site (every page's text,
  headings, meta tags, every image URL with alt text and size, outbound social links, JSON-LD), the Google Business
  Profile (address, phone, rating, category, overview text, captured reviews), the verified research (owner, email,
  services evidence, dated activity, original project photos, measured site defects, template capture) and its tier.
- `content/<id>.json`: the homepage copy in the structure above.
- `ALL_100.json`: all 100 businesses in one file (data summary plus content).
