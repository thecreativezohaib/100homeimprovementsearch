# Round 2 homepage content dive, part 03 of 12 (10 businesses)

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
1471,New Again Kitchen Remodeling,+15308992888,"1108 Mangrove Ave, Chico, CA 95926, United States",https://www.google.com/maps/place/?q=place_id:ChIJR-y1uSYmg4ARb983iBQ6CTE&hl=en,https://www.facebook.com/profile.php?id=100089638140834,https://www.instagram.com/newagainkitchen1
1515,Nu-Look Kitchens,+15635824680,service area,https://www.google.com/maps/place/?q=place_id:ChIJ795HzbAt44cRRZ1NdIbHFvo&hl=en,https://www.facebook.com/nulook.kitchens.3,https://www.instagram.com/nulook_kitchens
1592,Top Notch Granite solid countertops,+16015400755,"93 Jackson Cir, Florence, MS 39073, United States",https://www.google.com/maps/place/?q=place_id:ChIJkcakxDHTKYYRwD7rUGWdBsM&hl=en,https://www.facebook.com/profile.php?id=100090381580726,https://www.instagram.com/solidworldgranite
1594,Ogden Woodworking,+18056805867,"375 Pine Ave #13, Goleta, CA 93117, United States",https://www.google.com/maps/place/?q=place_id:ChIJ56ix-nhA6YARgr-rdfNSR8U&hl=en,https://www.facebook.com/RickSaria7873,https://www.instagram.com/ogden_woodworking
295,Reliable Remodels,+19076321029,"9701 Elmore Rd, Anchorage, AK 99507, United States",https://www.google.com/maps/place/?q=place_id:ChIJp8xwoo6XyFYRjqsW56zIlqU&hl=en,none,https://www.instagram.com/reliableremodels
1645,Argento Marble & Granite Inc,+19709637070,"1101 Dolores Way, Carbondale, CO 81623, United States",https://www.google.com/maps/place/?q=place_id:ChIJMVj1ZOqrQYcRAT8ewRtWmL8&hl=en,https://www.facebook.com/Argento-Marble-Granite-107866728985834,https://www.instagram.com/cjmarblegranite
1905,M&J Demolition & Remodeling LLC,+18326911171,service area,https://www.google.com/maps/place/?q=place_id:ChIJ13w9NV5RoWsRRkHycDl3x40&hl=en,https://www.facebook.com/RemodelingservicHTX,https://www.instagram.com/mjremodelin
1966,Northern Countertops & Cabinets,+17074673969,"195 Clara Ave Entrance on, Mason St, Ukiah, CA 95482, United States",https://www.google.com/maps/place/?q=place_id:ChIJVWq2mSt7gYARpa4Uxx0jEls&hl=en,https://www.facebook.com/p/Northern-Countertops-Cabinet-Division-100083297713456,https://www.instagram.com/northernplumbingca
62,Raccoon Stone & Tile Works,+14789562222,"2347 GA-247CONN, Byron, GA 31008, United States",https://www.google.com/maps/place/?q=place_id:ChIJ-ZisyzXm84gRug4KD2uOJak&hl=en,https://www.facebook.com/100057276745410,none
86,WOODEYE LLC,+14583568185,"278 E High St, Stayton, OR 97383, United States",https://www.google.com/maps/place/?q=place_id:ChIJZ-lXVzf1v1QR3eG-YiRVN8Y&hl=en,none,https://www.instagram.com/woodeye_woodworking
```
