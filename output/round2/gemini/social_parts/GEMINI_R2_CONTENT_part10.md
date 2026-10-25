# Round 2 homepage content dive, part 10 of 12 (10 businesses)

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
1324,Wolston Tile Designs,+15804674399,"1927 Ridgeway Cir, Duncan, OK 73533, United States",https://www.google.com/maps/place/?q=place_id:ChIJ1_ZG79NcrYcRcTZvvxJGAXA&hl=en,https://www.facebook.com/WolstonTileDesigns,https://www.instagram.com/wolstontiledesigns
1365,B&J Refinishing,+12545235754,service area,https://www.google.com/maps/place/?q=place_id:ChIJAQBEOTuHT4YR-GyLN4ILpeg&hl=en,https://www.facebook.com/bjrefinishing254,https://www.instagram.com/b_and_j_refinishing
1509,Trophy Tile and Bathroom Renovations,+16789239568,service area,https://www.google.com/maps/place/?q=place_id:ChIJpzFpO20lsygR0oa3U3auQB4&hl=en,https://www.facebook.com/trophytile,https://www.instagram.com/protileandrenovations
1705,"Swing Cabinets, LLC",+19316843576,"331 Pinkston Rd, Shelbyville, TN 37160, United States",https://www.google.com/maps/place/?q=place_id:ChIJ8fa121_pY4gRWb8ZnmjO4Zs&hl=en,https://www.facebook.com/swingscustomcabinets,https://www.instagram.com/henryscabinets
475,Janke Custom Tile,+19894755452,"3390 Dobson Dr, Bay City, MI 48706, United States",https://www.google.com/maps/place/?q=place_id:ChIJzdVt7JDhI4gRgrQV2gYey7k&hl=en,https://www.facebook.com/Jankecustoms,none
1816,Kelly's Kitchen and Bath,+16366970380,service area,https://www.google.com/maps/place/?q=place_id:ChIJYylCmJe_LGYRKB_2vEUF56A&hl=en,https://www.facebook.com/kellyskandb,https://www.instagram.com/kellyskitchenandbath
202,A.C.E Carpentry,+15406993098,service area,https://www.google.com/maps/place/?q=place_id:ChIJXWc4RC-_tIkRmdthhelSsNk&hl=en,https://www.facebook.com/RCBwaterACE,none
2122,"Happy Home Remodeling, LLC",+17207133443,service area,https://www.google.com/maps/place/?q=place_id:ChIJV6zawm3BYVMRmbuxYIjibv0&hl=en,https://www.facebook.com/people/Happy-Home-Remodeling-LLC/100069758931766,https://www.instagram.com/happyhomeremodelingllc
2177,Hilton Head Home Solutions,+18432274087,"18 Executive Park Rd #3, Hilton Head Island, SC 29928, United States",https://www.google.com/maps/place/?q=place_id:ChIJ8WU2zzx5_IgRR6X27DaD6V0&hl=en,https://www.facebook.com/hiltonheadhomesolutions,https://www.instagram.com/hiltonheadhomesolutions
2183,Watson Construction,+16627031991,"700 Sewanee St, Greenville, MS 38701, United States",https://www.google.com/maps/place/?q=place_id:ChIJo85lEXXtK4YR9Di2pGa29FE&hl=en,https://www.facebook.com/Watson-Construction-760115234045721,https://www.instagram.com/watsonconstructionco
```
