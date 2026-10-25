# Round 2: Facebook, Instagram and Maps deep dive, part 01 of 12 (10 businesses)

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
210,INNOVATION Cabinetry Installs,+19095454322,service area,https://www.google.com/maps/place/?q=place_id:ChIJy58vzdDSgkgRV23ocMCkXVc&hl=en,none,https://www.instagram.com/innocabs/
118,Veteran Tile Works,+19095617249,"1001 Palm Ave, Beaumont, CA 92223, United States",https://www.google.com/maps/place/?q=place_id:ChIJmQoAr9wxw4ARhf0Qrd92uqk&hl=en,https://www.facebook.com/100070009914829,none
371,"RS Construction Solutions-kitchen,bathroom remodeler/excavation",+17244563396,"3871 Saranac Dr, Sharpsville, PA 16150, United States",https://www.google.com/maps/place/?q=place_id:ChIJccZaGbfQEqIR-QkEnIpAc60&hl=en,https://www.facebook.com/61575161177205,none
279,Kinley Remodeling,+17243017571,"1411 Chelsea Ave, Erie, PA 16505, United States",https://www.google.com/maps/place/?q=place_id:ChIJ0VrJYiiDH2URDoefrZi6jjE&hl=en,https://www.facebook.com/profile.php?id=61553011979286,none
411,Melling Granite & More,+14358670099,"260 N Westview Dr, Cedar City, UT 84720, United States",https://www.google.com/maps/place/?q=place_id:ChIJ7TvD-aNhtYARi-iZaLA6TOg&hl=en,https://www.facebook.com/100063594431333,none
429,Forney Home Services,+18722484243,"2401 S Mt Juliet Rd, Mt. Juliet, TN 37122, United States",https://www.google.com/maps/place/?q=place_id:ChIJqbK5mzZuSoQRhqjNBH2ps9E&hl=en,https://www.facebook.com/forneyhomeservices/,none
69,McMichael Home Repair,+13145685888,service area,https://www.google.com/maps/place/?q=place_id:ChIJw8zFTsEr34cRhVzNQGrwRuk&hl=en,none,https://www.instagram.com/steph.mcmichael
1010,"Preferred Tile, LLC",+19127647767,"9 N Zetterower Ave, Statesboro, GA 30458, United States",https://www.google.com/maps/place/?q=place_id:ChIJSxA_xrg7-ogRaw31xjnUsE8&hl=en,https://www.facebook.com/PreferredTileLlc,none
1011,The Countertop Shop,+15802347131,"310 S 42nd St, Enid, OK 73701, United States",https://www.google.com/maps/place/?q=place_id:ChIJ0wn_UwbVr4cRG91blFc0T2s&hl=en,https://www.facebook.com/enidcountertopshop,none
347,CK Tile and Home Repair LLC,+19523567295,"6530 57th Ave N, Minneapolis, MN 55428, United States",https://www.google.com/maps/place/?q=place_id:ChIJpfecVL83s1IRjPur556CnvQ&hl=en,https://www.facebook.com/p/CK-Tile-Home-Repair-LLC-100076686626703,none
```
