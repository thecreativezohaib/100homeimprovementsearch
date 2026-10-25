# Round 2 homepage content dive, part 01 of 12 (10 businesses)

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
