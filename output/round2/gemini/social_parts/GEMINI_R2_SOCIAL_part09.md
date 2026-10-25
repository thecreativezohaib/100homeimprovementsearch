# Round 2: Facebook, Instagram and Maps deep dive, part 09 of 12 (10 businesses)

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
2290,Neptoon Tile Company,+18594140962,service area,https://www.google.com/maps/place/?q=place_id:ChIJY0q_gqS9Q4gRgRUNWQ7NqVk&hl=en,https://www.facebook.com/61552925813095/,none
2294,Oak Lane Remodeling,+17404039449,service area,https://www.google.com/maps/place/?q=place_id:ChIJ79l4LNovI4URsaQSp7supRI&hl=en,https://www.facebook.com/p/Oak-Lane-Remodeling-61590518469403/,none
2307,Florida Cabinet Solutions Co.,+17862534556,"20951 SW 336th St, Homestead, FL 33034, United States",https://www.google.com/maps/place/?q=place_id:ChIJC8o-Zi-72YgRUcTrtEWGXUk&hl=en,https://www.facebook.com/100028262186780/,none
2311,KGF Home Improvement,+17345024805,service area,https://www.google.com/maps/place/?q=place_id:ChIJP3Njd6WpYSkRbtiDFfzPd88&hl=en,https://www.facebook.com/p/KGF-Home-Improvement-61590314420204/,none
111,Quality Kitchens & Baths,+17314319944,"7657 Hwy 45 S, Martin, TN 38237, United States",https://www.google.com/maps/place/?q=place_id:ChIJ0QZqHuZgeYgRwpmHgtxuLOc&hl=en,https://www.facebook.com/p/Quality-Kitchens-and-Baths-100057212929391,https://www.instagram.com/qualitykitchenbathny
175,Antonio's Tile,+17346233274,"2770 Eastlawn Ave, Ypsilanti, MI 48197, United States",https://www.google.com/maps/place/?q=place_id:ChIJS-bSy4ypPIgRUmh71lU0ers&hl=en,https://www.facebook.com/AntoniosTileCo,none
1003,The Kitchen Connection LLC.,+15737015101,"Home Office Please Call First To Setup An Appointment, 720 Grey Fox, Farmington, MO 63640, United States",https://www.google.com/maps/place/?q=place_id:ChIJmX01BhpF2IcRGX5FV25qFn8&hl=en,https://www.facebook.com/TheKitchenConnectionLLC,none
182,Devlin Remodeling LLC,+18593800370,service area,https://www.google.com/maps/place/?q=place_id:ChIJlf1PclQ-DKMR0SgmTvKjGPI&hl=en,https://www.facebook.com/devlinremodeling,none
1294,Model Tile LLC,+14257721918,"11608 29th Ave SE, Everett, WA 98208, United States",https://www.google.com/maps/place/?q=place_id:ChIJrdoJ1-0HkFQRrR0J0X61XRQ&hl=en,https://www.facebook.com/modeltilellc,https://www.instagram.com/model_tile
1312,Cape Cod Tileworks,+15082466324,"705 Main St, Harwich, MA 02645, United States",https://www.google.com/maps/place/?q=place_id:ChIJrYMydbU_-4kR5mNXhUz01SA&hl=en,https://www.facebook.com/capecodtileworks,https://www.instagram.com/explore/locations/1022474710/cape-cod-tileworks
```
