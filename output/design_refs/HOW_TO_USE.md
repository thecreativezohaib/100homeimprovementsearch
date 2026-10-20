
## How to use these references to build the template

### The one rule: synthesize, never copy
Do not rebuild any single reference, and do not let one reference dominate. The goal is an original design system
that feels like it belongs in the same premium family as Harlow & Birch and Interior ST, yet is clearly its own.
Work like this:

1. **Study everything first.** Look through `sites/`, `sections/`, `pinterest/` and `concepts/` before drawing
   anything. Note what keeps coming back across many references (warm dark and cream rhythm, editorial serif or
   condensed caps, rounded photo cards, proof near every call to action). Recurring patterns are the genre; use
   them. One-off tricks are signatures; borrow at most one per reference and change it.
2. **Take ideas, not layouts.** From each reference take a principle ("price chips on service cards", "rating
   summary as the first testimonial tile", "script initial inside caps headline"), never its exact grid, spacing,
   wording, colours or images.
3. **Mix at least three references per section.** Every section below lists its main sources. Combine the structure
   of one, the visual treatment of another and the conversion device of a third, then adjust until it no longer
   resembles any of them.
4. **Change at least three of these from any reference you lean on:** layout geometry, type pairing, colour values,
   corner radius, image shape, ornament or divider style, motion. If a section could be mistaken for its source, it
   is too close.
5. **Invent two or three signature elements of your own** that appear across the page and make it recognisable, for
   example: a thin brass rule with a small monospace label that opens every section; a consistent photo frame (one
   rounded corner, one square); a numbered index style (01 / 05) shared by services, process and FAQ; a small
   stamp-like badge for the warranty. Keep them subtle and reusable for all 100 firms.
6. **Design the system before the page.** Define tokens and components first (below), then assemble sections from
   them. A consistent system is what makes the page feel premium; one-off sections make it feel like a collage.

### Step-by-step build process
1. **Mood and principles:** write five words for the design (for example: warm, crafted, editorial, calm,
   trustworthy) and pick the two or three signature elements.
2. **Design tokens** (CSS custom properties, so each firm can be re-skinned):
   - Colour: `--bg` (cream or warm white), `--surface` (white or sand), `--ink` (espresso or near black),
     `--ink-soft`, `--accent` (amber, terracotta or the firm's brand colour), `--accent-ink` (text on accent),
     `--line` (hairlines), `--dark` (espresso band background), `--on-dark`. Check WCAG AA contrast for every pair.
   - Type: one display face (a high-contrast serif or a condensed grotesk; an optional script for single initials
     or one accent word), one text sans, one optional monospace for eyebrows and chips. Use Google Fonts or system
     fallbacks. Fluid sizes with `clamp()`: H1 about 40px on phones to 88px on desktop; H2 30px to 56px; body 16px
     to 18px; small text never below 14px.
   - Space: an 8px scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128). Section padding about 64px on phones, 96px on
     tablets, 128px on desktop.
   - Shape and depth: one corner radius family (for example 4px for inputs, 16px to 24px for cards and photos, full
     pill for buttons and chips), one soft shadow, hairline borders.
   - Motion: short fades and small upward moves (200ms to 400ms), respect `prefers-reduced-motion`, no scroll
     hijacking and nothing that hides content until it animates.
3. **Components:** buttons (primary, secondary, ghost on dark, text link), chips (rating, price, timeline, town),
   eyebrow label, section header, photo card, service card, stat, testimonial card, step, accordion item, form
   fields and the multi-step estimate form, sticky header, mobile bottom bar, footer columns.
4. **Sections:** assemble the 13 sections from the components using the recipes below.
5. **Fill it with three real firms** from the homepage kit (`homepage_kit/content/`, delivered separately) (one with rich content, one average, one sparse with few
   photos and no prices) and fix whatever breaks.
6. **Responsive pass and QA** with the checklist at the end.

### Section recipes (sources to blend)
File names refer to folders in this pack. "Harlow" means `sites/01_harlow-template_framer_website/`; "Interior ST"
means `sites/02_tpl_interior_st/`.

1. **Header and utility bar.** Structure from Harlow (announcement bar with licence and hours, then nav with phone
   and a Free estimate button), the boxed hairline nav of `pinterest/23_interior-st_full-homepage_pin99.jpg`, and the
   floating pill nav of `pinterest/03_harlow_full-homepage_pin292.jpg`. Sticky: shrink on scroll, keep logo, phone
   and estimate button. Mobile: logo, round phone button, menu button; full-screen menu in the spirit of
   `pinterest/50_alt_mobile_pin815.jpg` and `sections/mobile_menu_or_header/`.
2. **Hero.** Proof stack from Harlow (rating chip above the H1, two buttons, a proof row under them). Typography
   from Interior ST and `pinterest/19_interior-st_full-homepage_pin117.jpg` (caps with one script letter) or
   `pinterest/54_alt_section_pin520.jpg` (sans plus serif italic word). Composition ideas: the frosted text card of
   `pinterest/01_harlow_full-homepage_pin96.jpg`, the staggered photos of
   `pinterest/25_interior-st_full-homepage_pin527.jpg`, the recent-projects strip of
   `pinterest/11_harlow_section_pin116.jpg`. Pick one composition and make it work with a single firm photo.
3. **Trust strip.** Rating, licence, warranty and years as a quiet row (Harlow proof row, `sections/trust_bar/`),
   with the certifications grid idea from Harlow and award rows from `pinterest/05_harlow_full-homepage_pin210.jpg`.
4. **Intro.** Large statement paragraph with an eyebrow, as in `pinterest/18_interior-st_full-homepage_pin143.jpg`
   and `pinterest/17_interior-st_full-homepage_pin165.jpg`; optional stats in the style of
   `pinterest/10_harlow_responsive-mockup_pin843.jpg`.
5. **Services.** Cards with photo, name, short blurb and optional price and timeline chips (Harlow,
   `pinterest/43_alt_full-homepage_pin323.jpg`, `sections/services/`), or the tabbed version of
   `pinterest/01_harlow_full-homepage_pin96.jpg`, or the accordion beside a photo of
   `pinterest/21_interior-st_full-homepage_pin155.jpg`. Chips show only when the firm publishes the data.
6. **Why choose us.** Four numbered promises in the shared index style; references: numbered values in
   `pinterest/18_interior-st_full-homepage_pin143.jpg`, Harlow's icon promises and the dark guarantee band.
7. **About the owner.** Named owner with a real photo and a short story, crew portraits when available (Harlow
   `sections/about_owner/`, team blocks in `pinterest/02_harlow_full-homepage_pin55.jpg`). Without an owner photo,
   fall back to a project photo with a signed quote.
8. **Process.** Numbered steps with an expectation chip each (Harlow `sections/process/`), with ideas from the
   expanding step of `pinterest/09_harlow_full-homepage_pin521.jpg`, the ring of
   `pinterest/12_harlow_section_pin307.jpg` and `concepts/26_dribbble_three-step-process.jpg`.
9. **Gallery and before/after.** Before/after slider (`sections/before_after/`, `concepts/17_dribbble_palo-alto-kitchen-before-after.jpg`, `concepts/18_dribbble_fixpro-before-after-slider.jpg`, `concepts/19_webflow_hearth-before-after-pairs.jpg`), project
   rows with a meta line (`pinterest/47_alt_full-homepage_pin548.jpg`), the details mosaic of
   `pinterest/52_alt_section_pin311.jpg`, the bath project sheet of `pinterest/35_interior-st_section_pin904.jpg`.
   Must look good with 5 photos and with 8.
10. **Testimonials.** Rating summary tile first (`pinterest/15_harlow_section_pin589.jpg`), then quote cards; the
    overlapping quote card over a photo from Interior ST `sections/testimonials/`; numbered soft cards from
    `pinterest/36_interior-st_section_pin608.jpg`. Works with 2 or 3 reviews.
11. **Service area.** Town chips beside the FAQ (Harlow `sections/service_area/`) or a map-like panel with a "check
    your address" action (`pinterest/04_harlow_full-homepage_pin349.jpg`, `sections/service_area/rebath_com__*`).
12. **FAQ.** Accordion with hairlines (Interior ST `sections/faq/`, `pinterest/37_interior-st_section_pin688.jpg`,
    `concepts/25_dribbble_faq-serif-accordion.jpg`) beside a human contact card (`concepts/24_dribbble_faq-book-a-call.jpg`,
    `sections/faq/tpl_interiia__*`).
13. **Final call to action and estimate form.** Multi-step estimate form with icon tiles (`concepts/21_framer_harlow-estimate-form.jpg`),
    the "what happens next" column of `pinterest/58_alt_section_pin728.jpg`, the warm closing band of Interior ST
    (`sections/cta_band/`). Always show phone and hours next to the form.
14. **Footer.** Name, address, phone, email, hours table, service towns, socials, licence; a large wordmark in the
    spirit of Harlow and `pinterest/38_interior-st_section_pin750.jpg`, kept short on mobile.

### Responsive rules
Design mobile first, then expand. Test at 360, 390, 430, 768, 1024, 1280 and 1440 px wide.

**Breakpoints:** phone below 640px, large phone and small tablet 640px to 1023px, laptop 1024px to 1279px, desktop
1280px and up. Content max width about 1280px with fluid side gutters of 16px (phones), 32px (tablets) and 48px or
more (desktop).

**Global behaviour:**
- Fluid type and spacing with `clamp()`; no text smaller than 14px; line length 45 to 75 characters for body.
- CSS grid with `auto-fit` and `minmax()` so cards reflow without breakpoint hacks; no horizontal page scroll at any
  width.
- Images: `srcset` and `sizes`, `aspect-ratio` set on every image box, `object-fit: cover`, lazy loading below the
  fold, the hero image preloaded. Art-direct the hero crop for portrait phones.
- Tap targets at least 44 by 44px; spacing between links; no hover-only information (hover is a bonus on desktop).
- Sticky header on all sizes. On phones add a bottom bar with Call and Free estimate that appears after the hero and
  never covers form fields or the footer content (add bottom padding equal to its height).
- Forms: one column on phones, correct input types (`tel`, `email`), autocomplete attributes, large inputs, the
  submit button full width.
- Respect `prefers-reduced-motion` and safe areas (`env(safe-area-inset-bottom)` for the bottom bar).

**Section behaviour:**

| Section | Phone | Tablet | Desktop |
|---|---|---|---|
| Header | logo, phone icon, menu icon; full-screen menu | logo, phone number, estimate button, menu | full nav, phone, estimate button, utility bar |
| Hero | photo on top or behind with overlay, H1 at most 4 lines, buttons stacked full width, proof row as 2x2 grid | text over photo or split, buttons inline | split or full-bleed composition, proof row in one line |
| Trust strip | horizontal scroll of chips or 2x2 grid | one row, wraps | one row |
| Services | single column cards or a swipe carousel with visible next card | 2 columns | 3 columns or tabs |
| Why us | stacked list | 2x2 | 4 across |
| About | photo then text | side by side | side by side with crew row |
| Process | vertical numbered timeline | vertical or 2 columns | horizontal steps or expanding list |
| Gallery | swipe carousel or 2-column grid, before/after full width | 2 or 3 columns | mosaic or 3 to 4 columns |
| Testimonials | swipe cards, rating summary first | 2 columns | 3 columns or large single quote |
| Service area | chips wrap, map hidden | chips plus small map | chips beside FAQ or map panel |
| FAQ | full-width accordion, contact card after | accordion plus card | two columns: card and accordion |
| Final CTA and form | form steps full width, phone and hours above | form plus side info | form beside "what happens next" and contact details |
| Footer | stacked groups, short wordmark | 2 columns | 4 columns plus wordmark |

### Gaps the design must survive
Every section must handle: no owner photo, 5 project photos, 2 reviews, no prices, no street address (city only),
no email, long business names and long town lists, and a logo that is only text. Hide empty parts cleanly and keep
the rhythm of dark and light bands intact when a section is missing.

### Final checklist
- Does the page look original next to every reference? Compare side by side; change anything that is a near copy.
- Is the phone and the estimate action visible on every screen size at every scroll position?
- Do three different firms (rich, average, sparse) all look finished?
- Mobile PageSpeed 90 or more, no layout shift from images or fonts, AA contrast, keyboard and screen reader
  friendly (one H1, ordered headings, labelled form fields, visible focus states).
- No em dashes, filler copy or placeholder images anywhere in the template.
