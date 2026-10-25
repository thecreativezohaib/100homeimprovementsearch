# Round 2 homepage content dive, part 07 of 12 (10 businesses)

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
1146,Walker’s Epoxy Countertops & Tables,+17242063688,service area,https://www.google.com/maps/place/?q=place_id:ChIJUchK2jDPw00R9QyFzhhRDk4&hl=en,https://www.facebook.com/Walkersepoxy,none
341,Matt's Home Solutions LLC (Matthew Pyles),+12703492054,"120 Reid Cir, Paducah, KY 42003, United States",https://www.google.com/maps/place/?q=place_id:ChIJ4zDp3EYSXYMRLraRtlqwBz0&hl=en,none,none
1007,The Stone Mill,+16019095772,"7312 Rose Farm Rd, Ocean Springs, MS 39564, United States",https://www.google.com/maps/place/?q=place_id:ChIJu_mB4SANnIgRMQANYoEGTC0&hl=en,https://www.facebook.com/stonemillco,none
1219,Uxbridge Cabinet Center,+15082786551,"706 Quaker Hwy, Uxbridge, MA 01569, United States",https://www.google.com/maps/place/?q=place_id:ChIJxwpifPsU5IkRoPvln3VuUUA&hl=en,https://www.facebook.com/100063559844133/,none
582,Davis Renovations,+12075091623,"Silver St, Waterville, ME 04901, United States",https://www.google.com/maps/place/?q=place_id:ChIJQ4q_aNDlsUwRwYCJPzkC5ec&hl=en,https://www.facebook.com/Davis.Renovations21,none
326,Continental Wood and Stone Company,+14197899765,"919 Grove St, Defiance, OH 43512, United States",https://www.google.com/maps/place/?q=place_id:ChIJRd0cVpHRPYgRHy6row9OrAE&hl=en,https://www.facebook.com/pages/Continental-Wood-and-Stone/318654535010316,none
580,JMR Tile & Stone,+19518239939,service area,https://www.google.com/maps/place/?q=place_id:ChIJacRrOQqN4WMRowt3M7g1z6E&hl=en,none,https://www.instagram.com/jmr_tile_and_stone
1389,Garibay Flooring Co,+12816404906,"2406 S Chappell Hill St, Brenham, TX 77833, United States",https://www.google.com/maps/place/?q=place_id:ChIJ3Tlzg0WpRoYRod7ezAVAN3U&hl=en,https://www.facebook.com/100063848353570/,none
1169,C&M Cabinets and Granite,+19018547007,"320 S Mt Pleasant Rd, Collierville, TN 38017, United States",https://www.google.com/maps/place/?q=place_id:ChIJER3xAdW8f4gRXI1AMEEWP4A&hl=en,none,https://www.instagram.com/cmcabinetsgranite
306,Morris Finishing Company LLC,+15406740079,"549 E Main St, Dublin, VA 24084, United States",https://www.google.com/maps/place/?q=place_id:ChIJeambtNbkTYgRSlJ7CU3rEOE&hl=en,https://www.facebook.com/morrisfinishing,https://www.instagram.com/va_finishing
```
