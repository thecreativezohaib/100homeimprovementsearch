# Remodel 100: final report (run date 2026-10-14, updated 2026-10-17)

**Result so far: 46 verified prospects, not 100.** The list was not padded. Every prospect passed all nine hard
gates on evidence, every one passed a visual photo review, all 46 have template content captured, and each
gate-critical claim is in `evidence.csv`. Work toward 100 is continuing (see "Still in progress").

## How the count grew (18, then 24, 36, 40, 44, 46)
- **PageSpeed Insights with an API key (2026-10-17).** 39 of the 46 have a mobile performance score below 60 as their
  measured defect.
- **Review dates you supplied through Gemini** for 109 firms. 4 passed that way, and you confirmed all 4 while signed in.
- **Agent waves 6 to 11.** Agents verified 455 firms that already had at least one activity signal and passed every
  automated gate. 22 of them (about 1 in 21) passed after the photo review. Most of the others failed on niche (general contractors,
  cabinet sellers, refinishers, design-only studios), on a missing second activity type, or on G6 (no full name and
  role on the firm's own site).
- **Automatic social signal.** Dated posts are read from LinkedIn company pages, YouTube channel feeds and Pinterest
  feeds that the firm links from its own website.
- **Discovery rounds 5 to 7.** Maps searches in 710 more towns. Rounds 5 and 6 added 7,395 companies. Round 7 (300
  towns chosen from Census population data) added 5,159 more.

## Counts (current)
| | |
|---|---|
| Discovered (unique companies after dedupe) | 23,734 |
| **Passed all gates** (`prospects100.csv`) | **46** |
| Contact-only (everything except a published email) | 9 |
| Bench-vendor (failed only G3; vendor named; G8 defect measured) | 9 |
| Rejected or not yet completed (`rejected.csv`) | 23,600 |

Rejections by first failing gate: G4 7,937; G2 5,935; G3 5,546; NICHE 3,855; G5 282; G6 31; G7 13; G8 1. G4 is still
the main filter. About 1,370 firms fail only G4, and they are in the Gemini request files (`review_requests/all/`).

## Top 10 by score (out of 25)
1. **MJ Kitchen & Bath** (Plymouth MI), 17: trigger, new showroom open 2026-06-29; live job posting.
2. **Majestic Home Solutions** (Sterling Heights MI), 17: owner replied within 60 days; live job posting.
3. **AC Remodeling** (Gaithersburg MD), 16: owner replied within 60 days; owner account posted within 60 days.
4. **JDI Construction** (Vancouver WA), 14: owner replied within 60 days; live job posting.
5. **All Exclusive Construction** (Westlake Village CA), 13: owner replied within 60 days.
6. **Ann Arbor Remodeling** (MI), 13: owner replied within 60 days.
7. **Assembly Squad Remodeling** (Chicago IL), 13: owner replied within 60 days.
8. **Craft Home Remodeling** (San Diego CA), 13: owner replied within 60 days.
9. **Forward Design Build Remodel** (Ann Arbor MI), 13: owner replied within 60 days.
10. **Hamlett Renovations** (Wayne NJ), 13: owner replied within 60 days.

## Most common defect, signal and trigger
- **Defect:** PageSpeed mobile performance below 60 (39 of 46), gallery images over 1 MB (5), horizontal
  overflow at 375 px (2).
- **G4 signal types across the 46:** site dated content 39, google review 30, social post 17, permit 4, job posting 2.
- **Trigger:** 1 of 46 (MJ Kitchen & Bath).
- **Paid spend:** Google Ads conversion tag 19, Meta Pixel 15, Houzz Pro 6, CallRail 2, HomeAdvisor 1, Buildertrend 1,
  Microsoft Ads 1, Angi 1.

## Still in progress
- Gemini answers for the G4-only firms (`GEMINI_ALL_v2.md` plus two addenda). `tools/ingest_gemini_all.py` imports
  review, Facebook and Instagram dates. It counts a social account only if it is linked from the firm's own site. It
  also imports dated job posts, and owner and email hints, which agents verify on the firm's own pages.
- Google review dates cannot be read anonymously: Maps shows 3 reviews in "limited view", and the internal review
  endpoints return 403 even inside a browser session.

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
- **Owner from separate first-name and surname mentions:** Sharon Stone Design ("Sharon (the owner)" and "Guy and
  Sharon Katz" on different lines) was rejected at G6 rather than joining the two.
- **Emails only in structured data:** Premium Residential Remodeling (JSON-LD only) was not counted as published.
- **Website-builder accounts:** LinkedIn and YouTube links to Wix's or Squarespace's own pages (template footers) are
  excluded from social signals.
- **Image sizes from re-serialised HTML:** CSS background URLs carried `&amp;`, which disabled the CDN's resizing and
  inflated byte counts. Assembly Squad's 1 MB defect was dropped for this reason and its G8 rests on PSI 48.
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
