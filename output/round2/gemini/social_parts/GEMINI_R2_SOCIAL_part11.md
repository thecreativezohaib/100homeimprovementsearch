# Round 2: Facebook, Instagram and Maps deep dive, part 11 of 12 (10 businesses)

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
268,LCR Home Solutions LLC,+17203501984,"579 Jewel St, Lochbuie, CO 80603, United States",https://www.google.com/maps/place/?q=place_id:ChIJxch48Z-3gYERtOwPsQyA72A&hl=en,none,https://www.instagram.com/lcr_home_solutions_llc
2301,Upper Left Construction,+15096702392,"125 N Wilson St, Wenatchee, WA 98801, United States",https://www.google.com/maps/place/?q=place_id:ChIJVVUxf7zMm1QRK1Hgf3g_rOU&hl=en,https://www.facebook.com/upperleftconstruction,https://www.instagram.com/upperleftconstructionllc
2324,Jackson Woodworks,+14066004443,"34598 Courville Trail, Polson, MT 59860, United States",https://www.google.com/maps/place/?q=place_id:ChIJCVSyEWp3Z1MRcFM7qTSiw00&hl=en,https://www.facebook.com/p/Jackson-Woodworks-100069990757827,https://www.instagram.com/jackson_woodworks
1117,AML Stoneworks Countertops,+12096227884,service area,https://www.google.com/maps/place/?q=place_id:ChIJYdn3EywHkYARmuepXd6Ccdc&hl=en,https://www.facebook.com/amlstoneworks,https://www.instagram.com/amlstoneworks209
1129,Ortega Remodeling,+15626183424,service area,https://www.google.com/maps/place/?q=place_id:ChIJ2zfh0IwVwSERnURdLn1iMUk&hl=en,https://www.facebook.com/Ortega-Remodeling-830350580667998,https://www.instagram.com/ortegaremodeling
50,FJ Remodeling,,service area,https://www.google.com/maps/place/?q=place_id:ChIJ67Far3obMKgR_InMD0D5ewg&hl=en,https://www.facebook.com/61555036028034,none
88,S&M customs (home solutions),+19013154970,"1287 Nelson Dr, Brighton, TN 38011, United States",https://www.google.com/maps/place/?q=place_id:ChIJBwD-34QTf4gRKWmwl1UBNao&hl=en,https://www.facebook.com/SandMCustoms,none
356,DMP Remodels,+17084151719,service area,https://www.google.com/maps/place/?q=place_id:ChIJxbx5VKWOgaoRcAZF2fVGpuI&hl=en,https://www.facebook.com/100067586964837,none
274,Queen City Renovation LLC,+17049893052,"10227 Connell Rd, Mint Hill, NC 28227, United States",https://www.google.com/maps/place/?q=place_id:ChIJ-c2S_FgXVIgRumc6GT6zVlU&hl=en,none,https://www.instagram.com/queencityrenovation
581,Cabinet & Countertop Solutions LLC,+19104741447,"899 US-1, Rockingham, NC 28379, United States",https://www.google.com/maps/place/?q=place_id:ChIJi3b3-fXDVIgR8PmZ00MfBfM&hl=en,https://www.facebook.com/share/19syQLQuqK,none
```
