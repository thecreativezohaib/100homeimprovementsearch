# Round 2: Facebook, Instagram and Maps deep dive, part 07 of 12 (10 businesses)

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
1146,Walker’s Epoxy Countertops & Tables,+17242063688,service area,https://www.google.com/maps/place/?q=place_id:ChIJUchK2jDPw00R9QyFzhhRDk4&hl=en,https://www.facebook.com/Walkersepoxy,none
341,Matt's Home Solutions LLC (Matthew Pyles),+12703492054,"120 Reid Cir, Paducah, KY 42003, United States",https://www.google.com/maps/place/?q=place_id:ChIJ4zDp3EYSXYMRLraRtlqwBz0&hl=en,none,none
1007,The Stone Mill,+16019095772,"7312 Rose Farm Rd, Ocean Springs, MS 39564, United States",https://www.google.com/maps/place/?q=place_id:ChIJu_mB4SANnIgRMQANYoEGTC0&hl=en,https://www.facebook.com/stonemillco,none
1219,Uxbridge Cabinet Center,+15082786551,"706 Quaker Hwy, Uxbridge, MA 01569, United States",https://www.google.com/maps/place/?q=place_id:ChIJxwpifPsU5IkRoPvln3VuUUA&hl=en,https://www.facebook.com/100063559844133/,none
582,Davis Renovations,+12075091623,"Silver St, Waterville, ME 04901, United States",https://www.google.com/maps/place/?q=place_id:ChIJQ4q_aNDlsUwRwYCJPzkC5ec&hl=en,https://www.facebook.com/Davis.Renovations21,none
326,Continental Wood and Stone Company,+14197899765,"919 Grove St, Defiance, OH 43512, United States",https://www.google.com/maps/place/?q=place_id:ChIJRd0cVpHRPYgRHy6row9OrAE&hl=en,https://www.facebook.com/pages/Continental-Wood-and-Stone/318654535010316,none
580,JMR Tile & Stone,+19518239939,service area,https://www.google.com/maps/place/?q=place_id:ChIJacRrOQqN4WMRowt3M7g1z6E&hl=en,none,https://www.instagram.com/jmr_tile_and_stone
1389,Garibay Flooring Co,+12816404906,"2406 S Chappell Hill St, Brenham, TX 77833, United States",https://www.google.com/maps/place/?q=place_id:ChIJ3Tlzg0WpRoYRod7ezAVAN3U&hl=en,https://www.facebook.com/100063848353570/,none
1169,C&M Cabinets and Granite,+19018547007,"320 S Mt Pleasant Rd, Collierville, TN 38017, United States",https://www.google.com/maps/place/?q=place_id:ChIJER3xAdW8f4gRXI1AMEEWP4A&hl=en,none,https://www.instagram.com/cmcabinetsgranite
306,Morris Finishing Company LLC,+15406740079,"549 E Main St, Dublin, VA 24084, United States",https://www.google.com/maps/place/?q=place_id:ChIJeambtNbkTYgRSlJ7CU3rEOE&hl=en,https://www.facebook.com/morrisfinishing,https://www.instagram.com/va_finishing
```
