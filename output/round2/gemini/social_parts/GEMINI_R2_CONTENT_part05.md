# Round 2 homepage content dive, part 05 of 12 (10 businesses)

## What to do
1. A NEW Gemini chat for this part (Agent mode or Deep Research), upload this file, send "Do the task in this file."
2. Run all parts at the same time if you like. Send me all the CSVs (or reports) together.
3. If one stops early, reply "Continue with the next business, same rules, same columns".

## The task (Gemini: follow this exactly)
```
You are collecting real content to build a homepage for each small kitchen and bath remodeling business in the table
below. Use Google Search, Google Maps, Facebook and Instagram. For EVERY business, open its Google Maps listing, its
Facebook page (facebook_url) and its Instagram profile (instagram_url). If a link is "none", search for the account
by name + town + phone and use it only if it clearly belongs to this business.

Output THREE kinds of rows for each business, all in ONE CSV:

1) kind = summary (one row per business)
- logo_url: direct image link of the business logo (the Facebook profile picture or Instagram profile picture,
  full size), and logo_text: the words and colours you see in the logo
- cover_photo_url: direct image link of the Facebook cover photo
- brand_colors: the 2 or 3 main colours of the logo / cover / truck / signs, as hex codes if you can (e.g. #1F3A5F)
- tagline: a slogan they use (exact words) or UNKNOWN
- about_text: Facebook Intro/About and Instagram bio, copied exactly
- services: every service they show or name, separated by semicolons
- service_towns: every town, county or area they name, separated by semicolons
- owner_name, team_names, years_in_business, licence_or_insurance, warranty, free_estimate, financing, hours,
  phone, email: only what a page states (exact words for licence, warranty, years)
- google_rating, google_review_count, facebook_followers, instagram_followers
- videos_summary: what their videos/reels show (one line each, up to 5)

2) kind = post (up to 30 per platform, newest first)
- platform, post_url, post_date (as shown), caption (exact, up to 300 characters), project_type (kitchen, bathroom,
  shower, cabinets, countertops, tile, flooring, other), town (only if named)
- image_urls: the DIRECT full-size image links of the photos in the post (links that end in .jpg/.png or come from
  scontent / fbcdn / cdninstagram), separated by spaces. These are the most important part: I need the real project
  photos.
- is_before_after: yes or no

3) kind = review (up to 15 per business: Google reviews first, then Facebook recommendations)
- platform (google or facebook), reviewer (first name and last initial only), review_date (as shown), stars,
  review_text (exact), owner_reply (exact, or none)

RULES
- Never guess or invent. Unknown means UNKNOWN. Copy text exactly.
- Plain full URLs only (no [text](url), no google.com redirect links).
- Process every business in this file; do not stop to ask me. If you run out of room, finish the business you are
  on and end with: LAST_ROW_DONE: <row>.

OUTPUT: CSV in one ```csv block with exactly this header (put text containing commas in double quotes):
row,kind,platform,post_url,post_date,caption,project_type,town,image_urls,is_before_after,reviewer,review_date,stars,review_text,owner_reply,logo_url,logo_text,cover_photo_url,brand_colors,tagline,about_text,services,service_towns,owner_name,team_names,years_in_business,licence_or_insurance,warranty,free_estimate,financing,hours,phone,email,google_rating,google_review_count,facebook_followers,instagram_followers,videos_summary
Keep the business's row number on every line.
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
