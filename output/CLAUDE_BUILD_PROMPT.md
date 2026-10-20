I have attached two folders:

1. **homepage_kit/**: data and finished homepage copy for 100 kitchen and bath remodeling companies.
   - `README.md`: what every file is, plus the list of all 100 businesses (site 1 is the first row).
   - `content/<id>.json`: the finished homepage copy for each business (SEO tags, hero, services, about,
     process, gallery, reviews, service area, FAQ, call to action, footer, schema), with `facts_used`,
     `missing` and `conversion_notes`.
   - `data/<id>.json`: everything gathered for each business: every page of their current site (text,
     headings, every image URL with alt text and size), their Google Business Profile (address, phone, rating,
     reviews), social links, owner, original project photos and measured problems with their current site.
   - `ALL_100_content.json`: all 100 in one file. `CONTENT_BRIEF.md`: the rules the copy follows.
2. **pack/** (design references): `DESIGN_REFERENCES.md` is the design guide. Read all of it. Open
   `index.html` to see every reference. The folders are `sites/` (the two sites I chose: Harlow & Birch and
   Interior ST), `sections/`, `pinterest/` and `concepts/`.

## Your job
Design ONE premium, high-converting, fully responsive homepage template, then use it to build a homepage for
each of the 100 businesses. Every site uses that business's own brand colours, logo, photos, reviews and facts.

## Workflow
**Step 1. Study.** Read `pack/DESIGN_REFERENCES.md` completely and look through all the reference images. Then
read `homepage_kit/README.md`, `CONTENT_BRIEF.md` and the content and data files for site 1.

**Step 2. Design the master template.** Follow "How to use these references" in the design guide:
- Blend many references. Never copy one. The result must be a unique design of its own.
- Take the structure and conversion features from Harlow & Birch and the editorial look from Interior ST, then
  use the section recipes in the guide.
- Build the design system first: tokens, then components, then sections. All colours and fonts must come from
  a small set of CSS variables so each business can be re-skinned.
- Keep the section order of the content files. Every section must still look finished when content is missing
  (few photos, 2 reviews, no prices, no owner photo, no street address).
- Follow the responsive rules in the guide: mobile first, test from 360 px to 1440 px wide, tap-to-call in the
  sticky header and a bottom Call / Estimate bar on phones.
- Use plain HTML and CSS with a little vanilla JavaScript (or Astro if you prefer). It must be fast: target a
  mobile PageSpeed score of 90+, with no heavy libraries.

**Step 3. Build site 1 only, then stop.** Site 1 is the first business in `homepage_kit/README.md`
(MJ Kitchen & Bath, `mj-kitchens.com`).
- **Content:** use `content/mj-kitchens.com.json` exactly as written. Do not invent facts. If something is in
  `missing`, leave it out.
- **Brand:** take their colours and logo from their current site. Look at their logo and site images in
  `data/mj-kitchens.com.json` (images and crawled pages) and pick their main brand colour, a dark, a light and an
  accent. Map these to the template's CSS variables, check that text contrast passes WCAG AA, and keep the
  premium feel (adjust shades if needed, never fight their brand).
- **Images:** use only their own photos (the image URLs in the content file and `images_on_site` /
  `original_project_photos` in the data file). Download them into the site's folder, resize and compress them,
  and serve them with `srcset`, set dimensions and lazy loading. Use the alt text from the content file.
- **Details:** name, address and phone exactly as in the content file (the Google profile). Phone as a tap-to-call
  link. Real reviews only. SEO title, meta description, headings and the JSON-LD schema from the content file.
- **Output:** `template/` (the shared template and design tokens) and `sites/mj-kitchens.com/` (index.html and
  assets).
- **Check your work:** take screenshots at 390 px (phone), 820 px (tablet) and 1440 px (desktop) and review them
  yourself. Fix anything broken or cramped. Then show me the screenshots and a short list of the design choices
  you made and which references inspired each section.
- **Stop here and wait for my approval.** Do not build any other site until I say so. I may ask for changes to
  site 1 first.

**Step 4. After I approve site 1, build the other 99** using the same approved template. Do not redesign.
- For each business, swap in its own content file, brand colours and logo, photos and details, exactly as in
  step 3.
- Work in batches of 10 in README order. After each batch, check phone and desktop screenshots of every site,
  fix problems, and give me a short report: which sites are done, and any issue such as very few photos, a
  missing logo or colours that needed adjusting.
- Keep every site's content unique to that business. Never reuse text, photos or reviews between businesses.

## Rules for every site
- Facts only from that business's own files. No invented years, licences, awards, prices or warranties.
- No stock photos, no placeholder text, no em dashes, no filler phrases.
- The phone number and the free estimate or consultation button are visible on every screen size at every scroll
  position.
- One H1, ordered headings, labelled form fields, visible focus states and AA contrast.

Start now with steps 1 to 3 (study, design the template, build site 1), then stop and show me site 1.
