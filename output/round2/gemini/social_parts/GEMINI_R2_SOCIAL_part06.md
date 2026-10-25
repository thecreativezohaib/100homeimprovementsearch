# Round 2: Facebook, Instagram and Maps deep dive, part 06 of 12 (10 businesses)

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
1100,Very Good Carpentry,+13373806913,service area,https://www.google.com/maps/place/?q=place_id:ChIJQcoyx0uTsioRVVeuf_38D5w&hl=en,none,https://www.instagram.com/very_good_carpentry_llc
2027,Majestic Marble,+15053262447,"2801 La Plata Hwy C, Farmington, NM 87401, United States",https://www.google.com/maps/place/?q=place_id:ChIJu5ikMi-QO4cRyD7fAYn96Zc&hl=en,https://www.facebook.com/majestic.marble.94,none
2077,Rommy's Kitchens & Closets by Design,+16195757707,"2260 Main St Ste 7, Chula Vista, CA 91911, United States",https://www.google.com/maps/place/?q=place_id:ChIJdZ9dU8dN2YAR8x_0XKwVUBQ&hl=en,none,https://www.instagram.com/rommysdesigns
2168,Hcs Kitchen And Bath,+19013848755,"7560 A E Beaty Dr, Memphis, TN 38133, United States",https://www.google.com/maps/place/?q=place_id:ChIJVVVltYOdf4gRW0xZ9YPCudI&hl=en,https://www.facebook.com/p/HCS-Kitchen-and-Bath-100057523176660,none
556,LUXURY REFINISHING INC,+17862364294,service area,https://www.google.com/maps/place/?q=place_id:ChIJaxFEPhW72YgROy7vEw_2D68&hl=en,https://www.facebook.com/100057533765730,none
2297,Hyde Studio,+14055515386,service area,https://www.google.com/maps/place/?q=place_id:ChIJbXlIP8NbgYURrZ_raFncdiE&hl=en,https://www.facebook.com/61589386452664,none
2254,Modern Design Center,+18562881300,"912 Haddonfield Rd B, Cherry Hill Township, NJ 08002, United States",https://www.google.com/maps/place/?q=place_id:ChIJFUVZWDvjb0AR6_uVFxOXBio&hl=en,https://www.facebook.com/ModernDesignCenter,none
1186,"Compass Bath and Remodel, LLC",+18016782880,service area,https://www.google.com/maps/place/?q=place_id:ChIJP-JvxkctuGIR9teEWLRyujs&hl=en,https://www.facebook.com/profile.php?id=100083363486803,none
275,DG Home Improvement LLC PA,+12674232617,service area,https://www.google.com/maps/place/?q=place_id:ChIJ4fIaWlVhUAQRMzcizUTipHA&hl=en,https://www.facebook.com/dghomeimprovementdg,none
45,Aguirre's Tile Services,+12144072403,"University Dr, Forney, TX 75126, United States",https://www.google.com/maps/place/?q=place_id:ChIJs6htyuysToYR9zeJVGiovUQ&hl=en,https://www.facebook.com/aguirrestileservices,none
```
