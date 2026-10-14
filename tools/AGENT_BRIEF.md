# Remodel 100 — regional verification brief (subagent)

Run date: 2026-10-14. Windows: 90 days = on/after 2026-07-16; 60 days = on/after 2026-08-15; 9 months = on/after 2026-01-14.

You verify candidates that already passed the automated checks (site resolves, no incumbent web vendor detected).
You receive a JSON file of candidates for ONE region. For EACH candidate, work through the steps in order and
STOP at the first failure (record it and move on). Append exactly one JSON line per candidate to your output file.

## Evidence discipline (non-negotiable)
- Every factual field carries a source URL and a verbatim quote of 20 words or fewer, copied from a page you fetched.
- Words BANNED in factual fields: likely, appears to, probably, presumably, seems, suggests.
- Anything you could not evidence is written literally as "UNKNOWN". A check you ran that found nothing is "NONE FOUND".
- Never infer ownership from a surname, an email address or a photograph. A person is a decision maker only if
  a page they control states the role (owner, co-owner, founder, president, CEO, principal) next to the name.
- NEVER construct or guess an email. An email counts only if that exact string is in a page you fetched (mailto:,
  visible text, HTML entity, or Cloudflare data-cfemail). Record the page URL and the raw string.
- If tempted to assume, reject instead and say so in `inference_rejected`.
- Facebook and Instagram return login walls from this environment; Google Search returns a CAPTCHA. Do not claim
  anything from them unless you actually retrieved the content. Use WebSearch (search engine), WebFetch, and
  `curl -sL -A "Mozilla/5.0" <url>` in Bash.

## Steps per candidate
1. **Niche.** Primary advertised work must be kitchen and bathroom remodelling (design-build firms qualify if kitchens
   and baths are their primary advertised work). Reject handymen, plumbers, roofers, flooring-only, cabinet retailers
   with no installation, national franchises, and lead-generation sites that are not a real contractor.
   Record `niche_ok` and `niche_evidence` {url, quote}.
2. **G4 activity.** The candidate record lists `auto_signals` already evidenced. Two DIFFERENT signal types dated
   on/after 2026-07-16 are required. Types: `google_review`, `social_post` (an account they control), `job_posting`,
   `site_dated_content` (a dated project/blog/gallery addition on their own site), `permit` or `licence_renewal`.
   Search for the missing type(s): their site blog/projects pages with visible dates; job boards (Indeed, ZipRecruiter,
   LinkedIn, their careers page) via WebSearch/WebFetch; state contractor licence lookups and city permit portals;
   YouTube/Houzz/Pinterest/LinkedIn pages linked from their site. Each signal needs {type, date YYYY-MM-DD, url, quote}.
   Set `g4_done: true` and summarise what you searched in `g4_notes`. If you cannot evidence two types, stop here.
3. **G5 independent.** Confirm no franchise brand, no corporate parent, no "find a location" locator.
   `g5_pass`, `g5_evidence` {url, quote}.
4. **G6 decision maker + email.** Look in order: contact page, about/team page, footer, /privacy, /privacy-policy,
   /terms. Record `decision_maker` {name, role, url, quote} or null. Record `email_confirm` {email, url, raw, method}
   for the address you saw (prefer the most direct business address). If no published email exists anywhere on
   their site, set `email_confirm: null` and record `contact_form_url`, `phone`, `socials`.
5. **Scoring research** (only if steps 1–4 passed):
   - `trigger`: on/after 2026-01-14 — new owner, acquisition, rebrand, name change, relocation, new showroom, new
     service line, or a public search for a web/marketing vendor. {type, date, url, quote} or "NONE FOUND".
   - `job_posting_live`: a job posting open now. {date, url, quote} or "NONE FOUND".
   - `competitor`: a named direct local competitor within 15 miles with a visibly modern site. Use the
     `competitor_pool` given (same-area firms whose sites passed mobile checks) or your own search.
     {name, url, town, basis}.
   - `owner_account_post_60d`: a named owner's own account that posted on/after 2026-08-15. {account_url, date, quote}
     or "UNKNOWN" if only login-walled platforms exist.
   - `high_ticket`: advertised full kitchen remodel, whole-home renovation, primary bath, additions, or published
     average project value > $30k. {url, quote} or "NONE FOUND".
6. `assessment`: one or two sentences of OPINION (labelled opinion; never used as evidence).

## Output line schema (one JSON object per line)
{"id", "name", "niche_ok", "niche_evidence", "g4_extra_signals": [...], "g4_done", "g4_notes",
 "g5_pass", "g5_evidence", "decision_maker", "email_confirm", "contact_form_url", "phone", "socials",
 "score": {"trigger", "job_posting_live", "competitor", "owner_account_post_60d", "high_ticket"},
 "assessment", "inference_rejected", "could_not_check", "stopped_at"}
Use `stopped_at` = the gate you stopped at ("NICHE", "G4", "G5", "G6") or null if you completed all steps.

## Additions after wave 1 (apply to every candidate)
- **G3 re-check.** While on the site, look at the footer and any /credits page. If you see ANY web/marketing vendor
  credit (with or without the word "by", e.g. "– Top Floor Marketing", "WEB DESIGN Makers Editorial"), record
  `g3_vendor_found`: {vendor, url, quote}. Keep going with the other steps (the coordinator routes it to the bench list).
- **Validate auto signals.** Open every `auto_signals` item of type site_dated_content. If it is spam/injected content,
  a "Hello world" default post, or not a project/blog/gallery addition, list it in `auto_signals_rejected` with the reason.
  A Google review signal is valid only if its timestamp is not prefixed "Edited".
- An email inside a form's hidden recipient field or only in a third-party registry is NOT a published email.
- CT home-improvement licences renew 1 April; they cannot supply a renewal signal in this window.
- Indeed/ZipRecruiter return 401/403 to direct requests; use WebSearch result snippets that show a posting date, or the
  company's own careers page with a date.
