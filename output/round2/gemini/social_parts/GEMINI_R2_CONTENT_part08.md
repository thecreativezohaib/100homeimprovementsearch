# Round 2 homepage content dive, part 08 of 12 (10 businesses)

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
1674,"Reel and Sons, LLC",+19195783330,"2255 Quakenbush Rd, Snow Camp, NC 27349, United States",https://www.google.com/maps/place/?q=place_id:ChIJKSZDrZHJaogRjnUSanY_p6o&hl=en,https://www.facebook.com/ReelandSonsLLC,none
1675,Above & Beyond Construction and Renovations LLC,+13365051120,"1215 Birch Hill Dr, Kernersville, NC 27284, United States",https://www.google.com/maps/place/?q=place_id:ChIJm7wqx1YHU4gRsFuCjq1qGAQ&hl=en,https://www.facebook.com/people/Above-Beyond-Construction-and-Renovations/100075956689834/,none
1215,DC Kitchen & Bath,+15162807988,"896 Old Country Rd, Westbury, NY 11590, United States",https://www.google.com/maps/place/?q=place_id:ChIJmVhyF0qHwokRc3zcruhDbbk&hl=en,https://www.facebook.com/dcKitchenAndBath,https://www.instagram.com/dckitchenbath
259,Lk Kitchen,+19293749031,"118 N Washington Ave, Dunellen, NJ 08812, United States",https://www.google.com/maps/place/?q=place_id:ChIJS4ndqOe5w4kRNaRjXkt-yTs&hl=en,https://www.facebook.com/lkkitchenproducts,https://www.instagram.com/l.k_kitchen
1783,Solid Surfaces,+19125308595,"1909 Odum Hwy, Jesup, GA 31546, United States",https://www.google.com/maps/place/?q=place_id:ChIJ1fJPf3TH-ogRfqjOk4dE0A8&hl=en,https://www.facebook.com/solidsurfacesinc/,none
1909,Independence Renovations LLC.,+14849254872,"2315 N Charlotte St, Pottstown, PA 19464, United States",https://www.google.com/maps/place/?q=place_id:ChIJFcdjXD2FxokRARFDmxZGs9A&hl=en,https://www.facebook.com/61566535718088/,none
1231,Quality Renovation LLC,+14014800110,"2 Farnum Pike, Smithfield, RI 02917, United States",https://www.google.com/maps/place/?q=place_id:ChIJQWMQtcdG5IkRH9AJgIVNEME&hl=en,https://www.facebook.com/qualityrens,https://www.instagram.com/qualityflooringrenovation
17,"New Creation Kitchen, Bath and Flooring",+16072380366,"800 Valley Plaza Ste 1, Johnson City, NY 13790, United States",https://www.google.com/maps/place/?q=place_id:ChIJJ-uP-2Hv2okR3mLeBfuCbUg&hl=en,https://www.facebook.com/61579421676549,none
534,ARM Home Care,+19733489915,service area,https://www.google.com/maps/place/?q=place_id:ChIJ75loAqejw4kRQnUDsQrtplk&hl=en,https://www.facebook.com/armhomecare,https://www.instagram.com/armhomecare
36,Dynasty Home Improvement LLC,+18607104602,"7A Windham Ave, Colchester, CT 06415, United States",https://www.google.com/maps/place/?q=place_id:ChIJD2cHR6pp5okRI-_s7du6UpA&hl=en,https://www.facebook.com/dynastyhomerenovation,https://www.instagram.com/dynasty.home.renovation
```
