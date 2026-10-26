# Round 3 homepage kit (5 businesses)

Each folder: `content.json` (the page in the round 2 structure, with `image_plan`), `content.md` (readable copy, image
plan, facts used, what to confirm), `images/` (their own Google Maps photos, plus their own Facebook photos where they
were verified), `images.json`, `research.json` (Google data and every Google review captured, email and where it was
published), `contact_sheet.jpg`.

- Testimonials are Google reviews quoted word for word with the reviewer and date as shown.
- Facts come from Google and the business's own posts. Anything only another AI reported is left out and listed in
  `missing` as "to confirm with owner". Towns taken from earlier research are used only when the phone's area code
  matches, and are flagged to confirm.
- Emails were published on Facebook or Instagram, which could not be opened from here: each page says "confirm email".
- AI slots (`"source": "ai"`) have a prompt and a file name; `GEMINI_AI_IMAGES.md` generates them all at once
  (names `<folder number>_<file>`). Galleries use real photos only.
- `INDEX.csv`: contacts, keyword, photo / AI / testimonial counts, first items to confirm (0 with lint notes).
- `homepages/`: businesses to contact (INDEX tier "ready", or "ready_check" when Google shows no kitchen and bath work or
  the email was found on another business's page). `reserves/`: pages kept but with a red flag (INDEX reserve_reason).
- `R3_B1_NEEDS.csv`: the batch 1 businesses that need more photos, a Maps link or reviews before a page can be built.
