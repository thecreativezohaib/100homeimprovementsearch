# Round 2: Facebook, Instagram and Maps deep dive, part 02 of 12 (10 businesses)

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
438,Custom By Alvarez,+18634393889,"18720 US-27, Lake Wales, FL 33853, United States",https://www.google.com/maps/place/?q=place_id:ChIJGZvXgLQK3YgRNDwxq3VwTSs&hl=en,https://www.facebook.com/people/Custom-By-Alvarez-Inc/100063639636931,https://www.instagram.com/maryalvarez18720
1013,T & A Cabinet Shop,+14233325635,"148 Bean St, Soddy-Daisy, TN 37379, United States",https://www.google.com/maps/place/?q=place_id:ChIJuyGHg4KOYIgRL-4DtGooyYc&hl=en,https://www.facebook.com/pages/T-A-Cabinet-Shop/161734503848310,none
61,Custombilt Counter Tops,+19122835704,"1822 Albany Ave, Waycross, GA 31503, United States",https://www.google.com/maps/place/?q=place_id:ChIJbTowhqn674gRhZrLYxQMw8g&hl=en,https://www.facebook.com/p/Custombilt-Countertops-100089967218420,https://www.instagram.com/walshcustomsurfaces
173,CNG Construction Inc,,"33 Traymore St, Buffalo, NY 14216, United States",https://www.google.com/maps/place/?q=place_id:ChIJL5TKmiFt04kR3TYix_lbNLY&hl=en,https://www.facebook.com/CNG-Construction-Inc-397140093742152,https://www.instagram.com/cng_contracting
1015,M & L Countertops & More,+13097921886,"3919 17th St, East Moline, IL 61244, United States",https://www.google.com/maps/place/?q=place_id:ChIJV0Nf5kI64ocRmQDKNZOGNK8&hl=en,https://www.facebook.com/mlcountertops,none
316,Builders Direct,+15705011133,"757 W Broad St, Hazleton, PA 18201, United States",https://www.google.com/maps/place/?q=place_id:ChIJ-c9sD3SkxYkR5sbrh7GsFrY&hl=en,https://www.facebook.com/p/Builders-Direct-61577866506751,https://www.instagram.com/buildersdirectusa
1080,Split Rock Remodeling LLC,+12543156551,service area,https://www.google.com/maps/place/?q=place_id:ChIJawPbWCKiuyERvz2xeosbIN8&hl=en,https://www.facebook.com/people/Split-Rock-Remodeling/100070787201400,none
1764,CleghornCabinets,+14789536996,"108 Constitution Dr, Warner Robins, GA 31088, United States",https://www.google.com/maps/place/?q=place_id:ChIJ-V7d-tPm84gRK1eFqWnASnY&hl=en,https://www.facebook.com/pages/Cleghorn-Cabinets/159216867444330,none
16,Elizabeth Kitchen & Granite LLC,+19086629512,"719 Livingston St, Elizabeth, NJ 07201, United States",https://www.google.com/maps/place/?q=place_id:ChIJe0AJP3lNwokRwXb3AJOuG6g&hl=en,https://www.facebook.com/p/Elizabeth-Kitchen-Granite-LLC-100083006333400,https://www.instagram.com/popular/elizabeth-kitchen-granite-llc
1243,Modern Cabinet & Construction,+18149421000,"110 Frankstown Rd, Altoona, PA 16602, United States",https://www.google.com/maps/place/?q=place_id:ChIJm00VJGyRy4kRAsjj95Ypqtw&hl=en,https://www.facebook.com/p/Modern-Cabinet-Construction-Company-Inc-100044638315135,https://www.instagram.com/moderncabinetconstruction
```
