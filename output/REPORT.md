# Remodel 100: final report (run date 2026-10-14, updated 2026-10-17)

**Result so far: 36 verified prospects, not 100.** The list was not padded. Every prospect passed all nine hard
gates on evidence, every one passed a visual photo review, and each gate-critical claim is in `evidence.csv`. Work
toward 100 is continuing (see "Still in progress").

## How the count grew (18, then 24, then 36)
- **PageSpeed Insights with an API key (2026-10-17).** 32 of the 36 have a mobile performance score below 60 as their
  measured defect.
- **Review dates you supplied through Gemini** for 109 firms. 4 passed that way, and you confirmed all 4 while signed in.
- **Agent waves 6 and 7.** Agents searched 147 firms that had one activity signal for a second kind (dated blog or
  project posts, permits, job posts, social posts), plus independence, owner and email checks. 12 passed after the
  photo review.
- **Automatic social signal.** Dated posts are read from LinkedIn company pages, YouTube channel feeds and Pinterest
  feeds that the firm links from its own website. 113 of 1,500 blocked firms had one in the window.
- **Discovery round 5.** Maps searches in 160 more towns added 2,898 new companies, which are still being screened.

## Counts (current; round-5 firms are still being screened)
| | |
|---|---|
| Discovered (unique companies after dedupe) | 14,078 |
| **Passed all gates** (`prospects100.csv`) | **36** |
| Contact-only (everything except a published email) | 5 |
| Bench-vendor (failed only G3; vendor named; G8 defect measured) | 6 |
| Rejected or not yet completed (`rejected.csv`) | 14,008 |

Rejections by first failing gate: G4 5,072; G3 3,551; G2 3,060 (this includes round-5 sites not yet checked);
NICHE 2,121; G5 174; G6 20; G7 9; G8 1. G4 is still the main filter. 1,005 firms fail only G4, and they are in the
Gemini request file (`review_requests/all/GEMINI_ALL_v2.md`).

## Top 10 by score (out of 25)
1. **MJ Kitchen & Bath** (Plymouth MI), 17: trigger, new showroom open 2026-06-29; live job posting.
2. **Majestic Home Solutions** (Sterling Heights MI), 17: owner replied within 60 days; live job posting.
3. **JDI Construction** (Vancouver WA), 14: owner replied within 60 days; live job posting.
4. **All Exclusive Construction** (Westlake Village CA), 13: owner replied within 60 days.
5. **Ann Arbor Remodeling** (MI), 13: owner replied within 60 days.
6. **Craft Home Remodeling** (San Diego CA), 13: owner replied within 60 days.
7. **Forward Design Build Remodel** (Ann Arbor MI), 13: owner replied within 60 days.
8. **Hamlett Renovations** (Wayne NJ), 13: owner replied within 60 days.
9. **ALL Renovation & Design** (Manheim PA), 12: live job posting.
10. **Boss Design Center** (Bethesda MD), 12: live job posting.

## Most common defect, signal and trigger
- **Defect:** PageSpeed mobile performance below 60 (32 of 36), gallery images over 1 MB (2), horizontal overflow at
  375 px (2).
- **G4 signal types across the 36:** dated site content 29, Google review 24, social post 13, permit 4, job post 2.
- **Trigger:** 1 of 36 (MJ Kitchen & Bath).
- **Paid spend:** Google Ads conversion tag 14, Meta Pixel 13, Houzz Pro 5, CallRail 2, HomeAdvisor 1, Buildertrend 1.

## Still in progress
- Round-5 discovery firms: site checks, then Maps, social, browser and PageSpeed, then agent verification.
- Gemini answers for the 1,005 G4-only firms. `tools/ingest_gemini_all.py` imports review, Facebook and Instagram
  dates. It counts a social account only if it is linked from the firm's own site. It also imports dated job posts,
  and owner and email hints, which agents verify on the firm's own pages.

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
- **Owner from first names or testimonials:** LowCountry Bath Renewal (first name only, on Nextdoor) and Capitalmark
  Interiors (surname only in customer testimonials) were rejected at G6.
- **Permits under another company name:** Callaway Homes (a Nashville permit names "Callaway Home Improvements") was
  not attributed.
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
- **G1 not enforced.** The brief's exclusion block was the unfilled placeholder. Run the list against your contacted
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
- **Login walls and blocks:** Facebook and Instagram are login-walled and Google Search returns a CAPTCHA. Indeed and
  ZipRecruiter return 401/403. LinkedIn company pages, YouTube channel feeds and Pinterest feeds are readable, and
  `tools/social.py` reads them automatically for accounts linked from the firm's own site. `owner_account_post_60d`
  stays UNKNOWN because owners' personal accounts are login-walled.
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
