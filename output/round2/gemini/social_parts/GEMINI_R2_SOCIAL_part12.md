# Round 2: Facebook, Instagram and Maps deep dive, part 12 of 12 (10 businesses)

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
1247,William Olsen Designs,+15413261652,"216 Houston Rd, Phoenix, OR 97535, United States",https://www.google.com/maps/place/?q=place_id:ChIJS83TeXp3z1QR_9eD07R6wss&hl=en,https://www.facebook.com/williamolsendesigns,none
1317,Bancroft Kitchen & Bath,+17579881100,"6605 George Washington Memorial Hwy, Yorktown, VA 23692, United States",https://www.google.com/maps/place/?q=place_id:ChIJ48BhOX1-sIkRa0UdhYeUbSQ&hl=en,https://www.facebook.com/p/Bancroft-Kitchen-Bath-100092701660124,none
1347,AMS Remodeling Inc.,+18479713041,service area,https://www.google.com/maps/place/?q=place_id:ChIJoe5eZAILE6wRRoreuezF_q4&hl=en,https://www.facebook.com/AMSRemodeling2016,none
1405,CRUSH IT Renovations LLC,+17274909451,"email. crushitrenovate@gmail.com, 7882 Sailboat Key Blvd S, South Pasadena, FL 33707, United States",https://www.google.com/maps/place/?q=place_id:ChIJIcX5Ijj9wogR1SFH2eMXMmU&hl=en,none,https://www.instagram.com/krushinit.fl
1444,MK Stones and Cabinets,+15614523551,"3132 Fortune Way d9, Wellington, FL 33414, United States",https://www.google.com/maps/place/?q=place_id:ChIJ5wTmbPwl2YgRs_AR-_7-KHY&hl=en,https://www.facebook.com/p/MK-Stones-100046432251866,none
1511,GMG HOME SOLUTIONS LLC,+19198139223,service area,https://www.google.com/maps/place/?q=place_id:ChIJQalZlphpZa8RSyPUzHbHPLo&hl=en,none,https://www.instagram.com/gmghomesolutionsllc
1528,Robert Repairs LLC,+18652767363,service area,https://www.google.com/maps/place/?q=place_id:ChIJTaICDqqZ4mMRTvqQB85RgrU&hl=en,none,https://www.instagram.com/robertrepairsllc
1640,DNA CONSTRUCTION 1 LLC,+15515805040,"59 Washington St, Harrison, NJ 07029, United States",https://www.google.com/maps/place/?q=place_id:ChIJQ4PjuKVVwokRnEnrqPolf6g&hl=en,none,https://www.instagram.com/dpremovalservices/reels
1667,Wills Builders,+18147234190,"1513 Pennsylvania Ave W # C, Warren, PA 16365, United States",https://www.google.com/maps/place/?q=place_id:ChIJ2d1zV6ZFzYkRH8g05tVK7k4&hl=en,https://www.facebook.com/p/Wills-Builders-100063765901589,none
1699,Elevated Services LLC,+15759373752,service area,https://www.google.com/maps/place/?q=place_id:ChIJ66PU6uOT-KMROivkoNxEays&hl=en,https://www.facebook.com/100081483460942,none
```
