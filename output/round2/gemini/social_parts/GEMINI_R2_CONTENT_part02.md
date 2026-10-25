# Round 2 homepage content dive, part 02 of 12 (10 businesses)

## What to do
1. A NEW Gemini chat for this part (Agent mode or Deep Research), upload this file, send "Do the task in this file."
2. Run all parts at the same time if you like. Send me all the CSVs (or reports) together.
3. If one stops early, reply "Continue with the next business, same rules, same columns".

## The task (Gemini: follow this exactly)
```
You are collecting real content to build a homepage for each small kitchen and bath remodeling business in the table
below. Use Google Search, Google Maps, Facebook and Instagram. For EVERY business, open its Google Maps listing, its
Facebook page (facebook_url) and its Instagram profile (instagram_url). If a link is "none", search for the account
by name + town + phone and use it only if it clearly belongs to this business.

Output THREE kinds of rows for each business, all in ONE CSV:

1) kind = summary (one row per business)
- logo_url: direct image link of the business logo (the Facebook profile picture or Instagram profile picture,
  full size), and logo_text: the words and colours you see in the logo
- cover_photo_url: direct image link of the Facebook cover photo
- brand_colors: the 2 or 3 main colours of the logo / cover / truck / signs, as hex codes if you can (e.g. #1F3A5F)
- tagline: a slogan they use (exact words) or UNKNOWN
- about_text: Facebook Intro/About and Instagram bio, copied exactly
- services: every service they show or name, separated by semicolons
- service_towns: every town, county or area they name, separated by semicolons
- owner_name, team_names, years_in_business, licence_or_insurance, warranty, free_estimate, financing, hours,
  phone, email: only what a page states (exact words for licence, warranty, years)
- google_rating, google_review_count, facebook_followers, instagram_followers
- videos_summary: what their videos/reels show (one line each, up to 5)

2) kind = post (up to 30 per platform, newest first)
- platform, post_url, post_date (as shown), caption (exact, up to 300 characters), project_type (kitchen, bathroom,
  shower, cabinets, countertops, tile, flooring, other), town (only if named)
- image_urls: the DIRECT full-size image links of the photos in the post (links that end in .jpg/.png or come from
  scontent / fbcdn / cdninstagram), separated by spaces. These are the most important part: I need the real project
  photos.
- is_before_after: yes or no

3) kind = review (up to 15 per business: Google reviews first, then Facebook recommendations)
- platform (google or facebook), reviewer (first name and last initial only), review_date (as shown), stars,
  review_text (exact), owner_reply (exact, or none)

RULES
- Never guess or invent. Unknown means UNKNOWN. Copy text exactly.
- Plain full URLs only (no [text](url), no google.com redirect links).
- Process every business in this file; do not stop to ask me. If you run out of room, finish the business you are
  on and end with: LAST_ROW_DONE: <row>.

OUTPUT: CSV in one ```csv block with exactly this header (put text containing commas in double quotes):
row,kind,platform,post_url,post_date,caption,project_type,town,image_urls,is_before_after,reviewer,review_date,stars,review_text,owner_reply,logo_url,logo_text,cover_photo_url,brand_colors,tagline,about_text,services,service_towns,owner_name,team_names,years_in_business,licence_or_insurance,warranty,free_estimate,financing,hours,phone,email,google_rating,google_review_count,facebook_followers,instagram_followers,videos_summary
Keep the business's row number on every line.
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
