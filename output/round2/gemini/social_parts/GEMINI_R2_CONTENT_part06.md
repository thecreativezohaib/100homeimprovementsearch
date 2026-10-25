# Round 2 homepage content dive, part 06 of 12 (10 businesses)

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
1100,Very Good Carpentry,+13373806913,service area,https://www.google.com/maps/place/?q=place_id:ChIJQcoyx0uTsioRVVeuf_38D5w&hl=en,none,https://www.instagram.com/very_good_carpentry_llc
2027,Majestic Marble,+15053262447,"2801 La Plata Hwy C, Farmington, NM 87401, United States",https://www.google.com/maps/place/?q=place_id:ChIJu5ikMi-QO4cRyD7fAYn96Zc&hl=en,https://www.facebook.com/majestic.marble.94,none
2077,Rommy's Kitchens & Closets by Design,+16195757707,"2260 Main St Ste 7, Chula Vista, CA 91911, United States",https://www.google.com/maps/place/?q=place_id:ChIJdZ9dU8dN2YAR8x_0XKwVUBQ&hl=en,none,https://www.instagram.com/rommysdesigns
2168,Hcs Kitchen And Bath,+19013848755,"7560 A E Beaty Dr, Memphis, TN 38133, United States",https://www.google.com/maps/place/?q=place_id:ChIJVVVltYOdf4gRW0xZ9YPCudI&hl=en,https://www.facebook.com/p/HCS-Kitchen-and-Bath-100057523176660,none
556,LUXURY REFINISHING INC,+17862364294,service area,https://www.google.com/maps/place/?q=place_id:ChIJaxFEPhW72YgROy7vEw_2D68&hl=en,https://www.facebook.com/100057533765730,none
2297,Hyde Studio,+14055515386,service area,https://www.google.com/maps/place/?q=place_id:ChIJbXlIP8NbgYURrZ_raFncdiE&hl=en,https://www.facebook.com/61589386452664,none
2254,Modern Design Center,+18562881300,"912 Haddonfield Rd B, Cherry Hill Township, NJ 08002, United States",https://www.google.com/maps/place/?q=place_id:ChIJFUVZWDvjb0AR6_uVFxOXBio&hl=en,https://www.facebook.com/ModernDesignCenter,none
1186,"Compass Bath and Remodel, LLC",+18016782880,service area,https://www.google.com/maps/place/?q=place_id:ChIJP-JvxkctuGIR9teEWLRyujs&hl=en,https://www.facebook.com/profile.php?id=100083363486803,none
275,DG Home Improvement LLC PA,+12674232617,service area,https://www.google.com/maps/place/?q=place_id:ChIJ4fIaWlVhUAQRMzcizUTipHA&hl=en,https://www.facebook.com/dghomeimprovementdg,none
45,Aguirre's Tile Services,+12144072403,"University Dr, Forney, TX 75126, United States",https://www.google.com/maps/place/?q=place_id:ChIJs6htyuysToYR9zeJVGiovUQ&hl=en,https://www.facebook.com/aguirrestileservices,none
```
