# Remodel 100: final report (run date 2026-10-14)

**Result: 18 verified prospects, not 100.** The list was not padded. Every prospect passed all nine hard gates on
evidence, and each gate-critical claim is in `evidence.csv`.

## Counts
| | |
|---|---|
| Discovered (unique companies after dedupe; 23,711 Maps rows from 1,182 searches in 538 towns) | 11,180 |
| Duplicates merged in the second pass (same final website after redirects) | 17 |
| Screened past the pre-gate (has a website, Maps category in niche) | 9,374 |
| **Passed all gates** (`prospects100.csv`) | **18** |
| Contact-only (everything except a published email) | 3 |
| Bench-vendor (failed only G3; vendor named; G8 defect measured) | 3 |
| Rejected (`rejected.csv`) | 11,139 |

## Rejections per gate (first failing gate, waterfall order)
| Gate | Rejected | What it was |
|---|---|---|
| G1 | 0 | The exclusion block in the brief held only the unfilled placeholder, so nothing could be matched. |
| G2 | 2,406 | 1,210 had no website on Google; 94 listed or redirected to a social or directory page; 48 domains do not resolve (confirmed by DNS-over-HTTPS); 18 parked or placeholder; 1,031 failed all three fetch routes (requests, curl, US Chromium); 5 not completed. |
| G3 | 2,839 | Agency or vendor credit, an agency theme author, an agency platform (Duda, GoHighLevel, HubSpot, Tilda, Next.js and others), or a vendor credit the agents found on the page. |
| G4 | 4,140 | 2,969 had no dated signal in the visible Google reviews or in dated site content. 1,122 had one signal and also failed a later automated gate, so no second signal was searched. 41 were searched by an agent and still had fewer than two types. 8 profiles are marked closed. |
| NICHE | 1,599 | Pre-gate Maps category, site text, or the agents' reading of the site. |
| G5 | 140 | Franchises, dealer networks, corporate parents. |
| G6 | 10 | No named decision maker on any page the company controls. |
| G7 | 3 | Fewer than 8 images I could confirm as original photographs (renderings, AI or stock imagery). |
| G8 | 2 | The 1 MB-image defect did not reproduce on re-measurement and there was no other measured defect. |

**The real filter is G4, then G3.** G4 dominates because anonymous Google Maps shows only 3 relevance-ordered
reviews per profile (see "Could not check").

## Top 10 by score (out of 25)
No trigger event within 9 months was evidenced for any of the 18, so every trigger line below reads "none
evidenced". The score points come from the other components.
1. **Ann Arbor Remodeling** (MI), 13: trigger none evidenced; owner replied to a review within 60 days.
2. **Craft Home Remodeling** (CA), 13: trigger none evidenced; owner replied within 60 days.
3. **Boss Design Center** (MD/VA), 12: trigger none evidenced; live Operations Manager posting.
4. **Semper Fi Custom Remodeling** (Asheville NC), 12: trigger none evidenced; live job posting.
5. **Wade Design & Construction** (Mequon WI), 12: trigger none evidenced; live job posting.
6. **Five Fold Solutions** (Overland Park KS), 10: trigger none evidenced; owner replied within 60 days.
7. **ARIID Build & Remodel** (Kirkland WA), 9: trigger none evidenced; careers page taking applications.
8. **Kellow Construction** (OR), 9: trigger none evidenced; drafter posting dated 2026-08-31.
9. **RIKB Design Build** (RI), 9: trigger none evidenced; sales-consultant posting live.
10. **A+ Custom Builders / Build With A Plus** (MA), 8: trigger none evidenced.

## Most common defect and trigger
- **Defect:** gallery images over 1 MB each (14 of 18). I re-measured them by full download with both a browser
  and a curl Accept header. The other 4 are horizontal overflow at a 375 px phone width. No PSI score could be measured.
- **Trigger:** none. Zero of the 18 have an evidenced trigger. One candidate trigger (PLF's new service line) was on a
  firm that failed G7. Another (Wright's "new" repairs page) was disallowed as an inference (see below).
- Paid-spend signal: a Google Ads conversion tag on 10, a Meta Pixel on 6, CallRail on 1, Buildertrend on 1.

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
- **Triggers:** Wright's Renovations' repairs page was created 2026-09-04, but the page never says the service is
  new, so I removed the +5. Plumberry's undated move notice and a 403-blocked Carmel news article were not scored.
- **Imagery:** I rejected PLF (styled renderings), Frontier and King (stock or AI-style images), and the side-list
  firms River City, Imagine and Mr. Bath on G7, because 8 originals could not be confirmed without assuming.
- **Related entities:** HomeSource permits filed under a different company name, and a business-for-sale listing
  matching Canyon Cabinetry's showroom size. Neither was attributed.

## Could not check, and why
- **G1 not enforced.** The brief's exclusion block was the unfilled placeholder. Run the 18 against your contacted
  list before any outreach.
- **PageSpeed Insights:** the keyless API returned HTTP 429 (daily quota exhausted) on every call, and the retry was
  also 429. `PSI_TIMEOUT` is recorded for every tested URL, and G8 was satisfied by the other measured checks.
- **Phone not dial-tested.** I checked only that the number is published on the Google profile and on the site.
- **Google reviews:** anonymous Google Maps serves a "limited view": 3 reviews in relevance order with relative
  timestamps and no sort by newest. Active businesses whose recent reviews are not among those 3 were rejected at G4.
  The Google Places API (needs a key) or a logged-in browser would recover many of them.
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
