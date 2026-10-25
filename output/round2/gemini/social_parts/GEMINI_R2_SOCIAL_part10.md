# Round 2: Facebook, Instagram and Maps deep dive, part 10 of 12 (10 businesses)

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
1324,Wolston Tile Designs,+15804674399,"1927 Ridgeway Cir, Duncan, OK 73533, United States",https://www.google.com/maps/place/?q=place_id:ChIJ1_ZG79NcrYcRcTZvvxJGAXA&hl=en,https://www.facebook.com/WolstonTileDesigns,https://www.instagram.com/wolstontiledesigns
1365,B&J Refinishing,+12545235754,service area,https://www.google.com/maps/place/?q=place_id:ChIJAQBEOTuHT4YR-GyLN4ILpeg&hl=en,https://www.facebook.com/bjrefinishing254,https://www.instagram.com/b_and_j_refinishing
1509,Trophy Tile and Bathroom Renovations,+16789239568,service area,https://www.google.com/maps/place/?q=place_id:ChIJpzFpO20lsygR0oa3U3auQB4&hl=en,https://www.facebook.com/trophytile,https://www.instagram.com/protileandrenovations
1705,"Swing Cabinets, LLC",+19316843576,"331 Pinkston Rd, Shelbyville, TN 37160, United States",https://www.google.com/maps/place/?q=place_id:ChIJ8fa121_pY4gRWb8ZnmjO4Zs&hl=en,https://www.facebook.com/swingscustomcabinets,https://www.instagram.com/henryscabinets
475,Janke Custom Tile,+19894755452,"3390 Dobson Dr, Bay City, MI 48706, United States",https://www.google.com/maps/place/?q=place_id:ChIJzdVt7JDhI4gRgrQV2gYey7k&hl=en,https://www.facebook.com/Jankecustoms,none
1816,Kelly's Kitchen and Bath,+16366970380,service area,https://www.google.com/maps/place/?q=place_id:ChIJYylCmJe_LGYRKB_2vEUF56A&hl=en,https://www.facebook.com/kellyskandb,https://www.instagram.com/kellyskitchenandbath
202,A.C.E Carpentry,+15406993098,service area,https://www.google.com/maps/place/?q=place_id:ChIJXWc4RC-_tIkRmdthhelSsNk&hl=en,https://www.facebook.com/RCBwaterACE,none
2122,"Happy Home Remodeling, LLC",+17207133443,service area,https://www.google.com/maps/place/?q=place_id:ChIJV6zawm3BYVMRmbuxYIjibv0&hl=en,https://www.facebook.com/people/Happy-Home-Remodeling-LLC/100069758931766,https://www.instagram.com/happyhomeremodelingllc
2177,Hilton Head Home Solutions,+18432274087,"18 Executive Park Rd #3, Hilton Head Island, SC 29928, United States",https://www.google.com/maps/place/?q=place_id:ChIJ8WU2zzx5_IgRR6X27DaD6V0&hl=en,https://www.facebook.com/hiltonheadhomesolutions,https://www.instagram.com/hiltonheadhomesolutions
2183,Watson Construction,+16627031991,"700 Sewanee St, Greenville, MS 38701, United States",https://www.google.com/maps/place/?q=place_id:ChIJo85lEXXtK4YR9Di2pGa29FE&hl=en,https://www.facebook.com/Watson-Construction-760115234045721,https://www.instagram.com/watsonconstructionco
```
