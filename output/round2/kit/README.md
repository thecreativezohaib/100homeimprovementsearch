# Round 2 homepage kit: first websites for kitchen and bath businesses

95 businesses are ready (folder `ready/`), 25 are kept for reference in `do_not_contact/`.

Each business folder holds:
- `content.json`: the full homepage copy in the master structure (`content_schema_r2.json`): SEO tags, hero, intro,
  services, why choose us, about, process, gallery, testimonials, service area, FAQ, final call to action, footer,
  schema markup, brand, outreach angle, `facts_used` (every claim with its source) and `missing` (what was not found)
- `content.md`: the same page as readable text
- `images/`: their own photos from Google Maps, Facebook and Instagram, `logo.jpg` and `cover.jpg` when found
  (check `images_not_to_use` in content.json and `brand.logo_file` before using a logo)
- `images.json`: where each photo came from; `contact_sheet.jpg`: all photos on one sheet
- `brand.json` and the `brand` block in content.json: palette, fonts, tagline
- `research.json`: everything collected about the business

Files at the top:
- `R2_KIT_INDEX.csv`: every business, contact details, keyword, counts and flags
- `CONFIRM_BEFORE_OUTREACH.csv`: ready businesses with something to confirm (town, email spelling, possible domain)
- `CONTENT_BRIEF_R2.md` and `content_schema_r2.json`: the rules and structure every page was written to

Notes
- Every review on the pages is quoted exactly from Google; Gemini's "reviews" were unrelated web text and none were used.
- No licence numbers, years, warranties or prices were invented; when not found they are listed under `missing`.
- `do_not_contact/` reasons: the email belongs to another business, the business already has a live website, or it
  does no kitchen and bath work. Their pages are written in case a correct email turns up.
