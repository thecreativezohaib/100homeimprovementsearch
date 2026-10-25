# Round 2: Facebook, Instagram and Maps deep dive, part 08 of 12 (10 businesses)

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
1674,"Reel and Sons, LLC",+19195783330,"2255 Quakenbush Rd, Snow Camp, NC 27349, United States",https://www.google.com/maps/place/?q=place_id:ChIJKSZDrZHJaogRjnUSanY_p6o&hl=en,https://www.facebook.com/ReelandSonsLLC,none
1675,Above & Beyond Construction and Renovations LLC,+13365051120,"1215 Birch Hill Dr, Kernersville, NC 27284, United States",https://www.google.com/maps/place/?q=place_id:ChIJm7wqx1YHU4gRsFuCjq1qGAQ&hl=en,https://www.facebook.com/people/Above-Beyond-Construction-and-Renovations/100075956689834/,none
1215,DC Kitchen & Bath,+15162807988,"896 Old Country Rd, Westbury, NY 11590, United States",https://www.google.com/maps/place/?q=place_id:ChIJmVhyF0qHwokRc3zcruhDbbk&hl=en,https://www.facebook.com/dcKitchenAndBath,https://www.instagram.com/dckitchenbath
259,Lk Kitchen,+19293749031,"118 N Washington Ave, Dunellen, NJ 08812, United States",https://www.google.com/maps/place/?q=place_id:ChIJS4ndqOe5w4kRNaRjXkt-yTs&hl=en,https://www.facebook.com/lkkitchenproducts,https://www.instagram.com/l.k_kitchen
1783,Solid Surfaces,+19125308595,"1909 Odum Hwy, Jesup, GA 31546, United States",https://www.google.com/maps/place/?q=place_id:ChIJ1fJPf3TH-ogRfqjOk4dE0A8&hl=en,https://www.facebook.com/solidsurfacesinc/,none
1909,Independence Renovations LLC.,+14849254872,"2315 N Charlotte St, Pottstown, PA 19464, United States",https://www.google.com/maps/place/?q=place_id:ChIJFcdjXD2FxokRARFDmxZGs9A&hl=en,https://www.facebook.com/61566535718088/,none
1231,Quality Renovation LLC,+14014800110,"2 Farnum Pike, Smithfield, RI 02917, United States",https://www.google.com/maps/place/?q=place_id:ChIJQWMQtcdG5IkRH9AJgIVNEME&hl=en,https://www.facebook.com/qualityrens,https://www.instagram.com/qualityflooringrenovation
17,"New Creation Kitchen, Bath and Flooring",+16072380366,"800 Valley Plaza Ste 1, Johnson City, NY 13790, United States",https://www.google.com/maps/place/?q=place_id:ChIJJ-uP-2Hv2okR3mLeBfuCbUg&hl=en,https://www.facebook.com/61579421676549,none
534,ARM Home Care,+19733489915,service area,https://www.google.com/maps/place/?q=place_id:ChIJ75loAqejw4kRQnUDsQrtplk&hl=en,https://www.facebook.com/armhomecare,https://www.instagram.com/armhomecare
36,Dynasty Home Improvement LLC,+18607104602,"7A Windham Ave, Colchester, CT 06415, United States",https://www.google.com/maps/place/?q=place_id:ChIJD2cHR6pp5okRI-_s7du6UpA&hl=en,https://www.facebook.com/dynastyhomerenovation,https://www.instagram.com/dynasty.home.renovation
```
