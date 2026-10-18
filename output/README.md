# Remodel 100: output guide

Run date: 2026-10-14, updated 2026-10-17 (PSI with an API key; Google review dates you supplied, see `review_requests/`). Retrieval dates are 2026-10-14 unless a row says otherwise.

| File | Contents |
|---|---|
| `prospects100.csv` | The verified prospects (49 so far, not 100: see `REPORT.md`). One column per gate and per score component, sorted by score. |
| `priority30.csv` | The top 30 by score with the template content capture and the outreach angle. |
| `rejected.csv` | Every candidate screened and rejected: failed gate, the evidence that failed, and any later gates also known to fail. |
| `contact-only.csv` | Passed everything except a published email. |
| `bench-vendor.csv` | Failed only G3 (incumbent web vendor named), with a measured G8 defect. |
| `evidence.csv` | One row per gate-critical claim for each verified prospect: field, value, source URL, quote or measurement method, retrieval date. |
| `logs/R1.csv` … `logs/R5.csv` | Per-region screening log: every ledger entry with its outcome. |
| `ledger.csv` | The shared master ledger (deduplicated on normalised root domain and normalised business name). |
| `funnel.json`, `REPORT_data.json` | Machine-readable counts behind the report. |

Raw evidence lives in `../data/` (site checks, Maps captures, browser measurements, agent verification lines in
`data/manual/`, template captures in `data/template/`, contact sheets in `data/montage/`). The code that produced
everything is in `../tools/` (`decide.py` holds the gate logic; `final.py` writes these files).

## Method, in brief
1. **Discovery.** Google Maps searches ("kitchen remodeler", "bathroom remodeler", and in round 1 also "kitchen and
   bath remodeler") across 538 affluent suburbs and secondary cities in the five regions: 1,182 searches, 23,711 rows.
2. **Ledger.** Rows were merged on the normalised root domain, Maps place ID and normalised name (name merges only when
   the websites did not conflict). A second pass merged records whose sites redirect to the same final domain.
   Result: 11,180 unique companies. All five regions fed this one ledger before any verification began.
3. **Automated gates.** The checks ran on each company's own site (python requests, then curl, then a US-egress
   Chromium render as the retry routes). They covered G2 resolve/parked/redirect, G3 vendor fingerprints (asset domains,
   meta generator, script hosts, WordPress theme header, footer credits and footer links), G5 franchise phrases, G6 email
   extraction (mailto, entities, Cloudflare data-cfemail), G7 image inventory, G8 measurements and G9 pixels. Google
   Business Profile data came from Google Maps for G4 activity and scoring.
4. **Regional verification.** Five regional subagents (R1–R5) ran four waves over the 171 candidates that cleared every
   automated gate and had at least one dated activity signal. They confirmed the niche, found the second G4 signal
   type, confirmed independence, found the named decision maker and verified the email. They also re-checked footers
   for vendor credits and researched the score components.
5. **Coordinator checks.** For every passer: strict G7 re-verification with a visual review of a contact sheet
   (renderings, AI or stock imagery, badges and duplicates excluded); a G8 re-measurement of 1 MB images by full
   download with two client profiles; a banned-word audit; and a 20-word quote audit.
6. **Top-30 capture.** The regional subagents captured the template content for every passer.
