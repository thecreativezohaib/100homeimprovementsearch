# Round 2 homepage content dive, part 11 of 12 (10 businesses)

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
268,LCR Home Solutions LLC,+17203501984,"579 Jewel St, Lochbuie, CO 80603, United States",https://www.google.com/maps/place/?q=place_id:ChIJxch48Z-3gYERtOwPsQyA72A&hl=en,none,https://www.instagram.com/lcr_home_solutions_llc
2301,Upper Left Construction,+15096702392,"125 N Wilson St, Wenatchee, WA 98801, United States",https://www.google.com/maps/place/?q=place_id:ChIJVVUxf7zMm1QRK1Hgf3g_rOU&hl=en,https://www.facebook.com/upperleftconstruction,https://www.instagram.com/upperleftconstructionllc
2324,Jackson Woodworks,+14066004443,"34598 Courville Trail, Polson, MT 59860, United States",https://www.google.com/maps/place/?q=place_id:ChIJCVSyEWp3Z1MRcFM7qTSiw00&hl=en,https://www.facebook.com/p/Jackson-Woodworks-100069990757827,https://www.instagram.com/jackson_woodworks
1117,AML Stoneworks Countertops,+12096227884,service area,https://www.google.com/maps/place/?q=place_id:ChIJYdn3EywHkYARmuepXd6Ccdc&hl=en,https://www.facebook.com/amlstoneworks,https://www.instagram.com/amlstoneworks209
1129,Ortega Remodeling,+15626183424,service area,https://www.google.com/maps/place/?q=place_id:ChIJ2zfh0IwVwSERnURdLn1iMUk&hl=en,https://www.facebook.com/Ortega-Remodeling-830350580667998,https://www.instagram.com/ortegaremodeling
50,FJ Remodeling,,service area,https://www.google.com/maps/place/?q=place_id:ChIJ67Far3obMKgR_InMD0D5ewg&hl=en,https://www.facebook.com/61555036028034,none
88,S&M customs (home solutions),+19013154970,"1287 Nelson Dr, Brighton, TN 38011, United States",https://www.google.com/maps/place/?q=place_id:ChIJBwD-34QTf4gRKWmwl1UBNao&hl=en,https://www.facebook.com/SandMCustoms,none
356,DMP Remodels,+17084151719,service area,https://www.google.com/maps/place/?q=place_id:ChIJxbx5VKWOgaoRcAZF2fVGpuI&hl=en,https://www.facebook.com/100067586964837,none
274,Queen City Renovation LLC,+17049893052,"10227 Connell Rd, Mint Hill, NC 28227, United States",https://www.google.com/maps/place/?q=place_id:ChIJ-c2S_FgXVIgRumc6GT6zVlU&hl=en,none,https://www.instagram.com/queencityrenovation
581,Cabinet & Countertop Solutions LLC,+19104741447,"899 US-1, Rockingham, NC 28379, United States",https://www.google.com/maps/place/?q=place_id:ChIJi3b3-fXDVIgR8PmZ00MfBfM&hl=en,https://www.facebook.com/share/19syQLQuqK,none
```
