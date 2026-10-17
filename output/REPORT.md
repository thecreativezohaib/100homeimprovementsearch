# Remodel 100: final report (run date 2026-10-14, updated 2026-10-17)

**Result: 24 verified prospects, not 100.** The list was not padded. Every prospect passed all nine hard gates on
evidence, and each gate-critical claim is in `evidence.csv`.

**What changed on 2026-10-17 (18 to 24):**
- PageSpeed Insights now runs with an API key. 20 of the 24 have a measured mobile performance score below 60.
  allrd.com (38) and Hamlett Renovations (55) had dropped out at G8 and now pass.
- You supplied the newest Google review dates for 109 firms that had one non-review activity signal and nothing
  else failing except G8 (`output/review_requests/`, gathered with Gemini). 21 showed a review on or after
  2026-07-16. After PSI, agent verification, the photo review and template capture, 4 of those 21 pass: MJ Kitchen
  & Bath, Renovating KC, Gayler Design Build and S&W Kitchens.
- These 4 rely on a review date I did not open myself. You confirmed on 2026-10-17, signed in to Google, that all 4
  show a recent review. `evidence.csv` records this in `source_note`.

## Counts
| | |
|---|---|
| Discovered (unique companies after dedupe; 23,711 Maps rows from 1,182 searches in 538 towns) | 11,180 |
| Duplicates merged in the second pass (same final website after redirects) | 17 |
| Screened past the pre-gate (has a website, Maps category in niche) | 9,374 |
| **Passed all gates** (`prospects100.csv`) | **24** |
| Contact-only (everything except a published email) | 3 |
| Bench-vendor (failed only G3; vendor named; G8 defect measured) | 4 |
| Rejected (`rejected.csv`) | 11,132 |

## Rejections per gate (first failing gate, waterfall order)
| Gate | Rejected | What it was |
|---|---|---|
| G1 | 0 | The exclusion block in the brief held only the unfilled placeholder, so nothing could be matched. |
| G2 | 2,406 | 1,210 had no website on Google; 94 listed or redirected to a social or directory page; 48 domains do not resolve (confirmed by DNS-over-HTTPS); 18 parked or placeholder; 1,031 failed all three fetch routes (requests, curl, US Chromium); 5 not completed. |
| G3 | 2,840 | Agency or vendor credit, an agency theme author, an agency platform (Duda, GoHighLevel, HubSpot, Tilda, Next.js and others), or a vendor credit the agents found on the page. |
| G4 | 4,119 | 2,969 had no dated signal in the visible Google reviews or in dated site content. 1,102 had one signal and also failed a later automated gate, so no second signal was searched. 40 were searched by an agent and still had fewer than two types. 8 profiles are marked closed. |
| NICHE | 1,602 | Pre-gate Maps category, site text, or the agents' reading of the site. |
| G5 | 151 | Franchises, dealer networks, corporate parents, plus candidates never verified because a later gate fails (marked "[not completed]"). 11 of these now pass G4 on your review data but fail G8: PSI 60 or higher and no other measured defect. |
| G6 | 11 | No named decision maker on any page the company controls. |
| G7 | 3 | Fewer than 8 images I could confirm as original photographs (renderings, AI or stock imagery). |

**The real filter is G4, then G3.** G4 dominates because anonymous Google Maps shows only 3 relevance-ordered
reviews per profile (see "Could not check"). G8 no longer rejects anyone: every remaining G8 failure sits behind an
earlier failing gate.

## Top 10 by score (out of 25)
Only one of the 24 has a trigger event evidenced within 9 months.
1. **MJ Kitchen & Bath** (Plymouth MI), 17: trigger, new showroom open 2026-06-29 ("6.29.26 Our new Showroom is now open!").
2. **Ann Arbor Remodeling** (MI), 13: trigger none evidenced; owner replied to a review within 60 days.
3. **Craft Home Remodeling** (CA), 13: trigger none evidenced; owner replied within 60 days.
4. **Hamlett Renovations** (Wayne NJ), 13: trigger none evidenced; owner replied within 60 days.
5. **ALL Renovation & Design** (Manheim PA), 12: trigger none evidenced; live job posting.
6. **Boss Design Center** (MD/VA), 12: trigger none evidenced; live Operations Manager posting.
7. **Semper Fi Custom Remodeling** (Asheville NC), 12: trigger none evidenced; live job posting.
8. **Wade Design & Construction** (Mequon WI), 12: trigger none evidenced; live job posting.
9. **Five Fold Solutions** (Overland Park KS), 10: trigger none evidenced; owner replied within 60 days.
10. **ARIID Build & Remodel** (Kirkland WA), 9: trigger none evidenced; careers page taking applications.

## Most common defect and trigger
- **Defect:** a PageSpeed Insights mobile performance score below 60 (20 of 24; scores 28 to 59, measured
  2026-10-17). The others: gallery images over 1 MB (2) and horizontal overflow at a 375 px phone width (2).
- **Trigger:** 1 of 24 (MJ Kitchen & Bath, new showroom). Gayler Design Build mentions a "new showroom" but
  publishes no opening date, so it scores 0 for trigger. Tenhulzen (renamed 2026-06-05, second office 2026-06-19)
  failed G6 because no page names an owner or president. Wright's "new" repairs page stays disallowed (see below).
- Paid-spend signal: a Google Ads conversion tag on 13, a Meta Pixel on 7, Houzz Pro on 2, CallRail on 1,
  Buildertrend on 1.

## Where I or the agents were tempted to infer, and rejected instead
460 entries are recorded in the agents' `inference_rejected` fields in `data/manual/`. The main patterns:
- **Owner from a registry, review or surname:** Lunasol (CSLB name), Silverado (NSCB), Residence Design Build (BBB
  summary), Heritage Remodelers ("Scott Smith" only in a customer review), and Imagine Remodel (first names only).
  None was recorded as a decision maker.
- **Emails not truly published:** an address seen only in a search summary (Form LTD), in a hidden form recipient
  (Imagine Remodel) or in schema markup (GJK). None was used. No email was constructed anywhere.
- **Activity dates:** "Edited" Google reviews, undated careers pages, sitemap modified dates, and injected spam posts
  (homexc, S&L, Kedem, SDG Home Concepts). None was counted as activity.
- **Franchise or parent inferred from a mention or filename:** "re-bath" in image filenames, Bath Planet in a
  testimonial. These were not treated as franchises. Real parents (SageHome, Window World group, Luxury Bath, a local
  parent company) were rejected.
- **Undated trigger:** Gayler's "new showroom" has no published date, so it was not scored.
- **Review data from Gemini:** 85 of the 106 dated rows you supplied fall before 2026-07-16 and were not counted.
  Gemini returned no reviewer names or "Edited" flags, so those fields were not used.
- **Triggers:** Wright's Renovations' repairs page was created 2026-09-04, but the page never says the service is
  new, so I removed the +5. Plumberry's undated move notice and a 403-blocked Carmel news article were not scored.
- **Imagery:** I rejected PLF (styled renderings), Frontier and King (stock or AI-style images), and the side-list
  firms River City, Imagine and Mr. Bath on G7, because 8 originals could not be confirmed without assuming.
- **Related entities:** HomeSource permits filed under a different company name, and a business-for-sale listing
  matching Canyon Cabinetry's showroom size. Neither was attributed.

## Could not check, and why
- **G1 not enforced.** The brief's exclusion block was the unfilled placeholder. Run the 18 against your contacted
  list before any outreach.
- **PageSpeed Insights:** on 2026-10-14 the keyless API returned HTTP 429 on every call. On 2026-10-17 it ran with
  a key for the 24 passers, allrd, Hamlett and the 21 review-window firms. Two URLs (adkitchenc.com and
  thebathremodelingcenter.com) returned HTTP 502 twice and stay `PSI_TIMEOUT`. Other firms that failed G8 for
  lack of a PSI score were not re-run, because they also fail an earlier gate.
- **Phone not dial-tested.** I checked only that the number is published on the Google profile and on the site.
- **Google reviews:** anonymous Google Maps serves a "limited view": 3 reviews in relevance order with relative
  timestamps and no sort by newest. Active businesses whose recent reviews are not among those 3 were rejected at G4.
  The Google Places API stayed blocked (`API_KEY_SERVICE_BLOCKED`, no billing). Instead you supplied review dates for
  109 firms through Gemini. When the text of Gemini's "newest" review matched one of my captured reviews (24 rows), its
  date matched my relative timestamp in 21. In 43 rows a review I captured was newer than Gemini's "newest", so
  Gemini did not always sort by newest. That gives false negatives, not false passes.
- **Login walls and blocks:** Facebook, Instagram and LinkedIn are login-walled and Google Search returns a CAPTCHA.
  Indeed and ZipRecruiter return 401/403. As a result `owner_account_post_60d` is UNKNOWN for every prospect, and
  social activity came only from YouTube or Pinterest RSS feeds and Instagram feeds embedded on the company's own site.
- **Not attempted:** Google Ads Transparency Center and Meta Ad Library. G9 relies on the raw HTML and on network
  requests fired on page load.
- **Tool limits:** Apify and Firecrawl were out of credit. The shared web-search budget ran out late in wave 4, so a
  few job-posting checks are UNKNOWN.
- **Licence and permit portals:** many were JavaScript-only, needed an account or token, or blocked us (AZ ROC, MA,
  RI, PA, and several county portals). Open-data permit sets worked for Cary, Raleigh, Asheville, Chicago,
  Indianapolis, Olmsted County, Mesa, San Diego and Oregon CCB.
- **G2 fetch failures:** 1,031 sites failed all three routes. Some of those failures could be transient
  proxy errors under load rather than dead sites.
- **CDN image sizes vary by client.** allrd.com and Hamlett Renovations dropped out when their large images no
  longer measured over 1 MB.
- **Niche close calls** (design-build generalists, bath-only firms) are noted in the agents' lines. Bath-only and
  kitchen-only remodellers were treated as in-niche.
- **Quotes:** a few have typographic apostrophes normalised to straight ones. Agents' superseding correction lines are
  applied last-line-wins.
