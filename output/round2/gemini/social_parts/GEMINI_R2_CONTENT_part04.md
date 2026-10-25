# Round 2 homepage content dive, part 04 of 12 (10 businesses)

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
2349,L H Carpentry,+19365563053,"3057 Co Rd 723, Nacogdoches, TX 75964, United States",https://www.google.com/maps/place/?q=place_id:ChIJAVJPSxv1N4YRyb2cB_hbu-0&hl=en,https://www.facebook.com/hoffman02,https://www.instagram.com/lukehusbandscarpentry
2237,Jaime's Custom Cabinets,+12098196013,"3514 Atwater Blvd C, City of Atwater, CA 95301, United States",https://www.google.com/maps/place/?q=place_id:ChIJc2j4wrtrkYARzq923spm3NE&hl=en,https://www.facebook.com/jaime.orozc.96,https://www.instagram.com/jaimes_cabinets
2265,King Custom Cabinets,+15308452614,"367 Burns Dr #3, Yuba City, CA 95991, United States",https://www.google.com/maps/place/?q=place_id:ChIJZerDpttSm4ARfpUDGFr3kR4&hl=en,https://www.facebook.com/KingCustomCabinetry,https://www.instagram.com/kingcabinet313
15,Jota Handyman Remodeling LLC,+13125866495,service area,https://www.google.com/maps/place/?q=place_id:ChIJtwjg8zJ6riIRmnl_ANJAtfk&hl=en,https://www.facebook.com/jotahandyman,none
103,Turnmire Eco Construction,+15092204367,"3478-B Moore Rd, Kettle Falls, WA 99141, United States",https://www.google.com/maps/place/?q=place_id:ChIJNbYkumoinlQR0LcW-M1Ocsk&hl=en,https://www.facebook.com/Turnmire-Eco-Construction-1800289366922206,none
179,Empire Cabinets,+12259550299,"9445 Prince Charles St, Denham Springs, LA 70726, United States",https://www.google.com/maps/place/?q=place_id:ChIJfQgKuJa_JoYR5mXzt8qpR1Y&hl=en,https://www.facebook.com/empirecabinetshop,none
1261,Danny's Top Shop,+16369316606,"793 American Legion Dr, Festus, MO 63028, United States",https://www.google.com/maps/place/?q=place_id:ChIJeyfhYOru2IcR7NvUvk-a3aU&hl=en,https://www.facebook.com/pages/Dannys-Top-Shop/155218027850507,none
1292,Oak Ridge Custom Cabinets,+19204998855,"2660 N Packerland Dr, Green Bay, WI 54303, United States",https://www.google.com/maps/place/?q=place_id:ChIJD4-1tlP3AogRzFnoL7CRxEA&hl=en,https://www.facebook.com/p/Oak-Ridge-Custom-Cabinets-61552742624482,none
1307,"LMG Remodeling, LLC",+12409199294,"823 Woodland Way, Hagerstown, MD 21742, United States",https://www.google.com/maps/place/?q=place_id:ChIJt_ISwH3tyYkRsyVgRv6tHbE&hl=en,https://www.facebook.com/LMGRemodelingLLC,none
1339,The Cabinet Shop,+19562023893,"21168 FM508, Harlingen, TX 78550, United States",https://www.google.com/maps/place/?q=place_id:ChIJRyqwkMR4b4YRQJRuZSQ6uzE&hl=en,none,https://www.instagram.com/thecabinetshops
```
