# Round 2 homepage content dive, part 12 of 12 (10 businesses)

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
