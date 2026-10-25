# Round 2: Facebook, Instagram and Maps deep dive, part 05 of 12 (10 businesses)

## What to do
1. A NEW Gemini chat for this part (Deep Research, or Agent mode), upload this file, send "Do the task in this file."
2. Run as many parts at the same time as you like. Send me all the reports (or CSVs) together.
3. If a report stops early, reply "Continue with the next business, same rules, same columns".

## Prompt
```
Use Google Search, Google Maps, Facebook and Instagram. For EVERY business in the table below, open its Facebook page
(facebook_url) and Instagram profile (instagram_url) and read as many posts, reels and videos as you can (aim for the
latest 30 on each). Use Google Maps too: read the listing's "From the business" text, services and the newest reviews. Then output ONE row per post plus ONE summary row per business, as described below.

Summary row (kind = summary), one per business:
- about_text: the Facebook Intro / About text and the Instagram bio, copied exactly
- services: every service the business shows or names (for example: kitchen remodel, bathroom remodel, tub to shower
  conversion, walk-in shower, custom cabinets, countertops, tile, flooring, vanity install), separated by semicolons
- service_towns: every town or area they name, separated by semicolons
- owner_name and team_names: only if a page or post names them
- years_in_business, licence_or_insurance, warranty, free_estimate, financing: only if a page or post says so, with
  the exact words in quotes
- hours, phone, email, messenger_or_booking_link: as shown on the pages
- facebook_recommendations: up to 5 Facebook recommendations or review texts, copied exactly with the reviewer's
  first name and last initial and the date shown
- videos_summary: what their videos and reels show (one line each, up to 5)

Post rows (kind = post), up to 30 per platform per business:
- platform (facebook or instagram), post_url, post_date (as shown), caption (copied exactly, up to 300 characters)
- project_type (kitchen, bathroom, shower, cabinets, countertops, tile, other), town (only if the caption names it)
- image_urls: the direct image links of the photos in the post if you can see them, separated by spaces
- is_before_after: yes or no

Rules:
- Never guess or invent anything. Unknown means UNKNOWN. Copy text exactly.
- Plain URLs only (no [text](url), no google.com redirect links).
- Process EVERY business in this chat and return ONE file. Work through them on your own; do not stop to ask me.
  If a reply runs out of room, continue in the next reply until every business is done.
- Best: one table, "Export to Sheets", so I can download a CSV.

Output: CSV only, with exactly this header:
row,kind,platform,post_url,post_date,caption,project_type,town,image_urls,is_before_after,about_text,services,service_towns,owner_name,team_names,years_in_business,licence_or_insurance,warranty,free_estimate,financing,hours,phone,email,messenger_or_booking_link,facebook_recommendations,videos_summary
Keep the business's row number on every line. Put text containing a comma in double quotes.
```


## Businesses
```csv
row,business_name,phone,address,google_maps,facebook_url,instagram_url
1340,S&A Excellence Bathroom Remodeling,+19498506772,service area,https://www.google.com/maps/place/?q=place_id:ChIJxc0viDsInK8RnfTfF8Piw6Q&hl=en,https://www.facebook.com/BreaBathroomRemodeling,none
42,VL Granite & Marble LLC,+13035917523,"1865 W Union Ave Ste J, Sheridan, CO 80110, United States",https://www.google.com/maps/place/?q=place_id:ChIJW-H0U6-Ba4cR6WfSqeIULMo&hl=en,https://www.facebook.com/vlgraniteandmarblellc,https://www.instagram.com/vlmarble
1479,Herrera Custom Cabinets,+12547095497,"379 Val Verde Rd, McGregor, TX 76657, United States",https://www.google.com/maps/place/?q=place_id:ChIJXR14vBGJT4YRCGcC9ClEsWA&hl=en,https://www.facebook.com/p/Herreras-Cabinets-100035478173495,none
1542,Lakeside Renovations LLC,+14145786916,service area,https://www.google.com/maps/place/?q=place_id:ChIJ6QAxC1jZHEgRimzlvdlxgQ4&hl=en,https://www.facebook.com/Lakeside-Renovations-LLC-107487992665813,none
1611,JCS TILE & MARBLE,+13606433344,service area,https://www.google.com/maps/place/?q=place_id:ChIJI_p0UbdccQkRaNtKt5PYLPA&hl=en,https://www.facebook.com/jcs.tile.and.marble,none
1553,JC James Remodeling,+17328404456,service area,https://www.google.com/maps/place/?q=place_id:ChIJ7UoUVnqEwYkRRthC_a-TnvM&hl=en,https://www.facebook.com/people/JC-James-Remodeling-LLC/100063670685539,none
1740,J&M floor and Bathroom Construction,+17866080337,service area,https://www.google.com/maps/place/?q=place_id:ChIJbxLHaDTF2YgRZG6U8L1I5uA&hl=en,https://www.facebook.com/100067487492434,none
377,The Expert Touch,+17328206720,"1021 NJ-37 Unit D, Toms River, NJ 08755, United States",https://www.google.com/maps/place/?q=place_id:ChIJk-_1sBt2wYkRxBE8cFc8Z0A&hl=en,https://www.facebook.com/people/The-Expert-Touch/100057405493125/,none
1862,United Kitchen & Bath,+15047808400,"2304 Marietta St, Kenner, LA 70062, United States",https://www.google.com/maps/place/?q=place_id:ChIJ78IcAjO3IIYR42xroOpzZ_g&hl=en,https://www.facebook.com/UnitedKitchenBath,none
573,Jersey Shore Tub and Tile Reglazing,+16093396239,"1040 NJ-166 Apt. 1408, Toms River, NJ 08753, United States",https://www.google.com/maps/place/?q=place_id:ChIJX2U4smadwYkRvmq-g7bEfMQ&hl=en,https://www.facebook.com/100083580752257,none
```
