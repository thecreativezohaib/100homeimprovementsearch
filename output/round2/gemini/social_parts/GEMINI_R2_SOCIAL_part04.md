# Round 2: Facebook, Instagram and Maps deep dive, part 04 of 12 (10 businesses)

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
2349,L H Carpentry,+19365563053,"3057 Co Rd 723, Nacogdoches, TX 75964, United States",https://www.google.com/maps/place/?q=place_id:ChIJAVJPSxv1N4YRyb2cB_hbu-0&hl=en,https://www.facebook.com/hoffman02,https://www.instagram.com/lukehusbandscarpentry
2237,Jaime's Custom Cabinets,+12098196013,"3514 Atwater Blvd C, City of Atwater, CA 95301, United States",https://www.google.com/maps/place/?q=place_id:ChIJc2j4wrtrkYARzq923spm3NE&hl=en,https://www.facebook.com/jaime.orozc.96,https://www.instagram.com/jaimes_cabinets
2265,King Custom Cabinets,+15308452614,"367 Burns Dr #3, Yuba City, CA 95991, United States",https://www.google.com/maps/place/?q=place_id:ChIJZerDpttSm4ARfpUDGFr3kR4&hl=en,https://www.facebook.com/KingCustomCabinetry,https://www.instagram.com/kingcabinet313
15,Jota Handyman Remodeling LLC,+13125866495,service area,https://www.google.com/maps/place/?q=place_id:ChIJtwjg8zJ6riIRmnl_ANJAtfk&hl=en,https://www.facebook.com/jotahandyman,none
103,Turnmire Eco Construction,+15092204367,"3478-B Moore Rd, Kettle Falls, WA 99141, United States",https://www.google.com/maps/place/?q=place_id:ChIJNbYkumoinlQR0LcW-M1Ocsk&hl=en,https://www.facebook.com/Turnmire-Eco-Construction-1800289366922206,none
179,Empire Cabinets,+12259550299,"9445 Prince Charles St, Denham Springs, LA 70726, United States",https://www.google.com/maps/place/?q=place_id:ChIJfQgKuJa_JoYR5mXzt8qpR1Y&hl=en,https://www.facebook.com/empirecabinetshop,none
1261,Danny's Top Shop,+16369316606,"793 American Legion Dr, Festus, MO 63028, United States",https://www.google.com/maps/place/?q=place_id:ChIJeyfhYOru2IcR7NvUvk-a3aU&hl=en,https://www.facebook.com/pages/Dannys-Top-Shop/155218027850507,none
1292,Oak Ridge Custom Cabinets,+19204998855,"2660 N Packerland Dr, Green Bay, WI 54303, United States",https://www.google.com/maps/place/?q=place_id:ChIJD4-1tlP3AogRzFnoL7CRxEA&hl=en,https://www.facebook.com/p/Oak-Ridge-Custom-Cabinets-61552742624482,none
1307,"LMG Remodeling, LLC",+12409199294,"823 Woodland Way, Hagerstown, MD 21742, United States",https://www.google.com/maps/place/?q=place_id:ChIJt_ISwH3tyYkRsyVgRv6tHbE&hl=en,https://www.facebook.com/LMGRemodelingLLC,none
1339,The Cabinet Shop,+19562023893,"21168 FM508, Harlingen, TX 78550, United States",https://www.google.com/maps/place/?q=place_id:ChIJRyqwkMR4b4YRQJRuZSQ6uzE&hl=en,none,https://www.instagram.com/thecabinetshops
```
