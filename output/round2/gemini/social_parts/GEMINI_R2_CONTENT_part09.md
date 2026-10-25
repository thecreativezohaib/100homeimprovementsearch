# Round 2 homepage content dive, part 09 of 12 (10 businesses)

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
2290,Neptoon Tile Company,+18594140962,service area,https://www.google.com/maps/place/?q=place_id:ChIJY0q_gqS9Q4gRgRUNWQ7NqVk&hl=en,https://www.facebook.com/61552925813095/,none
2294,Oak Lane Remodeling,+17404039449,service area,https://www.google.com/maps/place/?q=place_id:ChIJ79l4LNovI4URsaQSp7supRI&hl=en,https://www.facebook.com/p/Oak-Lane-Remodeling-61590518469403/,none
2307,Florida Cabinet Solutions Co.,+17862534556,"20951 SW 336th St, Homestead, FL 33034, United States",https://www.google.com/maps/place/?q=place_id:ChIJC8o-Zi-72YgRUcTrtEWGXUk&hl=en,https://www.facebook.com/100028262186780/,none
2311,KGF Home Improvement,+17345024805,service area,https://www.google.com/maps/place/?q=place_id:ChIJP3Njd6WpYSkRbtiDFfzPd88&hl=en,https://www.facebook.com/p/KGF-Home-Improvement-61590314420204/,none
111,Quality Kitchens & Baths,+17314319944,"7657 Hwy 45 S, Martin, TN 38237, United States",https://www.google.com/maps/place/?q=place_id:ChIJ0QZqHuZgeYgRwpmHgtxuLOc&hl=en,https://www.facebook.com/p/Quality-Kitchens-and-Baths-100057212929391,https://www.instagram.com/qualitykitchenbathny
175,Antonio's Tile,+17346233274,"2770 Eastlawn Ave, Ypsilanti, MI 48197, United States",https://www.google.com/maps/place/?q=place_id:ChIJS-bSy4ypPIgRUmh71lU0ers&hl=en,https://www.facebook.com/AntoniosTileCo,none
1003,The Kitchen Connection LLC.,+15737015101,"Home Office Please Call First To Setup An Appointment, 720 Grey Fox, Farmington, MO 63640, United States",https://www.google.com/maps/place/?q=place_id:ChIJmX01BhpF2IcRGX5FV25qFn8&hl=en,https://www.facebook.com/TheKitchenConnectionLLC,none
182,Devlin Remodeling LLC,+18593800370,service area,https://www.google.com/maps/place/?q=place_id:ChIJlf1PclQ-DKMR0SgmTvKjGPI&hl=en,https://www.facebook.com/devlinremodeling,none
1294,Model Tile LLC,+14257721918,"11608 29th Ave SE, Everett, WA 98208, United States",https://www.google.com/maps/place/?q=place_id:ChIJrdoJ1-0HkFQRrR0J0X61XRQ&hl=en,https://www.facebook.com/modeltilellc,https://www.instagram.com/model_tile
1312,Cape Cod Tileworks,+15082466324,"705 Main St, Harwich, MA 02645, United States",https://www.google.com/maps/place/?q=place_id:ChIJrYMydbU_-4kR5mNXhUz01SA&hl=en,https://www.facebook.com/capecodtileworks,https://www.instagram.com/explore/locations/1022474710/cape-cod-tileworks
```
