# Round 2: Facebook, Instagram and Maps deep dive, part 03 of 12 (10 businesses)

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
1471,New Again Kitchen Remodeling,+15308992888,"1108 Mangrove Ave, Chico, CA 95926, United States",https://www.google.com/maps/place/?q=place_id:ChIJR-y1uSYmg4ARb983iBQ6CTE&hl=en,https://www.facebook.com/profile.php?id=100089638140834,https://www.instagram.com/newagainkitchen1
1515,Nu-Look Kitchens,+15635824680,service area,https://www.google.com/maps/place/?q=place_id:ChIJ795HzbAt44cRRZ1NdIbHFvo&hl=en,https://www.facebook.com/nulook.kitchens.3,https://www.instagram.com/nulook_kitchens
1592,Top Notch Granite solid countertops,+16015400755,"93 Jackson Cir, Florence, MS 39073, United States",https://www.google.com/maps/place/?q=place_id:ChIJkcakxDHTKYYRwD7rUGWdBsM&hl=en,https://www.facebook.com/profile.php?id=100090381580726,https://www.instagram.com/solidworldgranite
1594,Ogden Woodworking,+18056805867,"375 Pine Ave #13, Goleta, CA 93117, United States",https://www.google.com/maps/place/?q=place_id:ChIJ56ix-nhA6YARgr-rdfNSR8U&hl=en,https://www.facebook.com/RickSaria7873,https://www.instagram.com/ogden_woodworking
295,Reliable Remodels,+19076321029,"9701 Elmore Rd, Anchorage, AK 99507, United States",https://www.google.com/maps/place/?q=place_id:ChIJp8xwoo6XyFYRjqsW56zIlqU&hl=en,none,https://www.instagram.com/reliableremodels
1645,Argento Marble & Granite Inc,+19709637070,"1101 Dolores Way, Carbondale, CO 81623, United States",https://www.google.com/maps/place/?q=place_id:ChIJMVj1ZOqrQYcRAT8ewRtWmL8&hl=en,https://www.facebook.com/Argento-Marble-Granite-107866728985834,https://www.instagram.com/cjmarblegranite
1905,M&J Demolition & Remodeling LLC,+18326911171,service area,https://www.google.com/maps/place/?q=place_id:ChIJ13w9NV5RoWsRRkHycDl3x40&hl=en,https://www.facebook.com/RemodelingservicHTX,https://www.instagram.com/mjremodelin
1966,Northern Countertops & Cabinets,+17074673969,"195 Clara Ave Entrance on, Mason St, Ukiah, CA 95482, United States",https://www.google.com/maps/place/?q=place_id:ChIJVWq2mSt7gYARpa4Uxx0jEls&hl=en,https://www.facebook.com/p/Northern-Countertops-Cabinet-Division-100083297713456,https://www.instagram.com/northernplumbingca
62,Raccoon Stone & Tile Works,+14789562222,"2347 GA-247CONN, Byron, GA 31008, United States",https://www.google.com/maps/place/?q=place_id:ChIJ-ZisyzXm84gRug4KD2uOJak&hl=en,https://www.facebook.com/100057276745410,none
86,WOODEYE LLC,+14583568185,"278 E High St, Stayton, OR 97383, United States",https://www.google.com/maps/place/?q=place_id:ChIJZ-lXVzf1v1QR3eG-YiRVN8Y&hl=en,none,https://www.instagram.com/woodeye_woodworking
```
