# Round 2: Gemini task 2, part 12 of 17 (100 businesses, rows 2184 to 2283)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 2283: reply in that chat "Continue with
   the businesses after LAST_ROW_DONE, same rules, same columns" and keep that report too.

## The task (Gemini: follow this exactly)
```
You are doing a long research task on 100 small kitchen and bathroom remodeling businesses in the United
States. Each one has a Google Business Profile but no working website. For each one I need: a contact email that the
business itself has published, and its Facebook page and/or Instagram profile. Work through the table at the end of
this file from top to bottom, in that order, and do NOT skip any.

The "task" column:
- C and D: new businesses. Do all the checks below for every one.

CHECKS FOR EACH BUSINESS (do every step; do not stop at the first result):
1. Facebook: search Google for "<business_name>" <town> facebook, and for the phone number in quotes
   (for example "(352) 988-7800" and "352-988-7800"). Open the page and confirm it is the same business (same name
   AND same phone, town or owner). If known_facebook is given, open it. Read the Intro, About, Page transparency and
   contact info, and the captions of its latest posts and photos. Small contractors often write their email in a
   post caption, a photo caption, a flyer or a business card photo. Note followers and the newest post date.
2. Instagram: search "<business_name>" instagram and the handle from the Facebook page. Read the bio, the contact
   button and the latest captions. Note followers and the newest post date.
3. Email: search Google for the phone number together with "@gmail.com", "@yahoo.com", "@aol.com", "@outlook.com",
   "@hotmail.com" and "email". Then check the Google Business Profile, BBB, Yelp, Houzz, Angi, HomeAdvisor,
   Thumbtack, Nextdoor, Porch, BuildZoom, Manta, Alignable, Birdeye, MapQuest, Chamber of Commerce listings, the state
   contractor licence lookup, the state business registry, local newspaper articles, and supplier "find an
   installer" pages.
4. Website check: search "<business_name>" <town> and the phone number. If the business has its own website that
   loads and shows the business, put it in website_found and write website_status = live. If a site exists but is
   down, parked, "launching soon", expired or a "domain not connected" page, put it in website_found and write
   website_status = dead. A Facebook, Instagram, Linktree, Yelp or directory page is NOT a website. If none: NONE.

RULES
- Never guess or build an email from a name pattern. Only copy an email you actually saw on a page, with that page's
  URL (email_source_url) and a quote of 20 words or fewer from that page that contains it (email_source_quote).
  People-search and email-finder sites (ContactOut, RocketReach, ZoomInfo, Whitepages and similar) do NOT count.
- Accept a Facebook page, Instagram profile or email only if it clearly belongs to THIS business (same name and the
  same phone, town or owner). If unsure, leave it out and say why in notes.
- Plain full URLs only: no [text](url) links, no google.com redirect links, no shortened links.
- sources_checked: every source you actually opened for that business, separated by semicolons.
- Keep each business's row number from the table.
- Do not stop to ask me anything and do not write long prose. Spend your effort on the research. A short summary at
  the top is enough.
- If you run out of room before the last business, finish the one you are on, output everything so far, and end
  with the line LAST_ROW_DONE: <row number>.

OUTPUT
End the report with ONE CSV block (in a ```csv code block) with exactly this header:
row,business_name,facebook_url,instagram_url,email,email_source_url,email_source_quote,website_found,website_status,owner_name,facebook_followers,facebook_latest_post_date,instagram_followers,instagram_latest_post_date,photo_posts,sources_checked,notes
- One line for every business where you found at least one of: a Facebook page, an Instagram profile, an email or
  a website. Unknown fields are UNKNOWN. Put any text containing a comma in double quotes.
- After the CSV block, one line: NOTHING_FOUND: followed by the row numbers you researched and found nothing for,
  separated by commas.
```

## Businesses (100, in order)
```csv
row,task,business_name,town,phone,address,google_maps,known_facebook,known_instagram,known_email,dead_website
2184,C,Affordable Bathrooms by Frank,"Conneautville, PA",(814) 573-4601,"5529 Turkey Track Rd, Conneautville, PA 16406",https://www.google.com/maps/place/?q=place_id:ChIJPSUsuBdHMogR8fbn4Su4DQU&hl=en,none,none,none,none
2185,C,Hast Building and Remodeling llc,"Colchester, CT",(860) 537-5081,"227 Dr Foote Rd, Colchester, CT 06415",https://www.google.com/maps/place/?q=place_id:ChIJtUhhRAVD5okREqb5HnXBzGo&hl=en,none,none,none,none
2186,C,Compass Custom Creations and Concrete Countertops,"Erlanger, KY",(859) 630-7179,"528 Enterprise Dr, Erlanger, KY 41017",https://www.google.com/maps/place/?q=place_id:ChIJy-ZBb1LFQYgRZLtZYTAnLzo&hl=en,none,none,none,none
2187,C,White's Custom Cabinets,"Savannah, TN",(731) 925-9144,"4065 Clifton Rd, Savannah, TN 38372",https://www.google.com/maps/place/?q=place_id:ChIJy0qN84xUfIgRcm788esKCTQ&hl=en,none,none,none,none
2188,C,Real Cabinets,"Bartlesville, OK",(918) 336-0255,"717 W 5th St, Bartlesville, OK 74003",https://www.google.com/maps/place/?q=place_id:ChIJvXYViXcUt4cRO57feFHSuwg&hl=en,none,none,none,none
2189,C,A Best Granite,"Lumberton, TX",(409) 751-0825,"4805 US-69, Lumberton, TX 77657",https://www.google.com/maps/place/?q=place_id:ChIJ3bKS8nIxOYYRosoUdppRKy4&hl=en,none,none,none,none
2190,C,Timeless Interiors,"Grayslake, IL",(847) 886-7166,"419 Center St Ste C, Grayslake, IL 60030",https://www.google.com/maps/place/?q=place_id:ChIJw8Gy3Z6bD4gRhkHccNdgkNU&hl=en,none,none,none,none
2191,C,S & R Florida Flooring LLC,"Miami, FL",(786) 970-2976,"10421 NW 28th St STE D1012, Miami, FL 33172",https://www.google.com/maps/place/?q=place_id:ChIJO0XpVA3B2YgRtgKBEvNh8Ds&hl=en,none,none,none,none
2192,C,BMN Bathroom Remodeling & Basement,"Naperville, IL",(331) 226-1417,"1057 Alder Ln, Naperville, IL 60540",https://www.google.com/maps/place/?q=place_id:ChIJj_v2PURXDogRR8i4QUrkjHU&hl=en,none,none,none,none
2193,C,Mario's Home Pro Services,"Green Cove Springs, FL",(904) 447-8310,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOywZbu3b5YgRf12v2H2lRfs&hl=en,none,none,none,none
2194,C,Grant's Custom Cabinets,"Greenbrier, AR",(501) 472-2923,"199 Linder Rd, Greenbrier, AR 72058",https://www.google.com/maps/place/?q=place_id:ChIJ1ajbe-J90ocRRzd1fYuXQmg&hl=en,none,none,none,none
2195,C,C.Q. Construction,"Jackson, MI",(517) 962-8610,"2716 Page Ave, Jackson, MI 49203",https://www.google.com/maps/place/?q=place_id:ChIJm8UXe5ElPYgR_QRRgjY-AzE&hl=en,none,none,none,none
2196,C,CABINETRY SOLUTIONS OF THE PALM BEACHES LLC,"Lantana, FL",(561) 516-0822,"335 Mockingbird Ln #28, Lantana, FL 33462",https://www.google.com/maps/place/?q=place_id:ChIJt8V1jUTZ2IgRlDkVvXEVAB0&hl=en,none,none,none,none
2197,C,Sadies Custom Surfaces & Design LLC,"Seymour, CT",(475) 354-7545,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVdECl0iQXkQRpT0yUYlgQfo&hl=en,none,none,none,none
2198,C,Kelly Kitchen & Bath,"Greensburg, PA",(724) 858-0394,"5256 US-30 #168, Greensburg, PA 15601",https://www.google.com/maps/place/?q=place_id:ChIJqz9NIMrRNIgRebKmtq6Gd8A&hl=en,none,none,none,none
2199,C,Brenham Area Marble; LLC,"Brenham, TX",(979) 836-1249,"2579 FM389, Brenham, TX 77833",https://www.google.com/maps/place/?q=place_id:ChIJ41-G2pkDRIYRpdrsLy8oAEU&hl=en,none,none,none,none
2200,C,Construction,"Garnerville, NY",(845) 200-4080,"Main St, Garnerville, NY 10923",https://www.google.com/maps/place/?q=place_id:ChIJqzWel27EwokRWlGr0r9xCUQ&hl=en,none,none,none,none
2201,C,Roecker Cabinets & Millwork,"Morton, IL",(309) 222-8300,"300 W Adams St, Morton, IL 61550",https://www.google.com/maps/place/?q=place_id:ChIJl6pkWT__CogRF_w94NU5K2A&hl=en,none,none,none,none
2202,C,Absolute Custom Stone,"Douglas, GA",(912) 389-5083,"89 Autumn Trail, Douglas, GA 31535",https://www.google.com/maps/place/?q=place_id:ChIJwY15TWAq8IgRuBc47bM4QwI&hl=en,none,none,none,none
2203,C,Boman Cabinets,"Baker City, OR",(541) 523-5635,"2710 15th St, Baker City, OR 97814",https://www.google.com/maps/place/?q=place_id:ChIJySKn7UbppFQRVqOyn_r2qwc&hl=en,none,none,none,none
2204,C,A A Low Country Home Builders,"Georgetown, SC",(843) 833-3276,"3030 S Island Rd, Georgetown, SC 29440",https://www.google.com/maps/place/?q=place_id:ChIJncJ2ja_UAYkRuhTPjZZ8eSM&hl=en,none,none,none,none
2205,C,Super Kitchen Services Inc,"Middleton, MA",(978) 539-8095,"3 Ajootian Way UNIT D10, Middleton, MA 01949",https://www.google.com/maps/place/?q=place_id:ChIJwREg7TwO44kRzFqH7py77E0&hl=en,none,none,none,none
2206,C,DM Kitchen Design,"Bel Air, MD",(443) 243-2016,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJYd7jSUzdx4kR-jaQgy3Iqc0&hl=en,none,none,none,none
2207,C,Master's Cabinet Works,"Timmonsville, SC",(843) 679-9800,"2353 Walker Swinton Rd Ste A, Timmonsville, SC 29161",https://www.google.com/maps/place/?q=place_id:ChIJRZ0CR9ljVYgRH9zPWx14vgw&hl=en,none,none,none,none
2208,C,Lebron´s Interior Remodel,"Berwyn, IL",(708) 989-7012,"1334 Wenonah Ave, Berwyn, IL 60402",https://www.google.com/maps/place/?q=place_id:ChIJwQM9A8E1DogRpiarG00Wtf4&hl=en,none,none,none,none
2209,C,CA Cabinets LLC,"Roswell, NM",(619) 200-4366,"112 N Virginia Ave, Roswell, NM 88203",https://www.google.com/maps/place/?q=place_id:ChIJw3tvHb1v4oYRaaWiqx6EaHU&hl=en,none,none,none,none
2210,C,"Southern Home Remodeling, LLC","Bessemer, AL",(205) 369-8610,"301 4th St N, Bessemer, AL 35020",https://www.google.com/maps/place/?q=place_id:ChIJK0URzxbeiIgRt3yjtompC3M&hl=en,none,none,none,none
2211,C,T & M Kitchens,"Kinnelon, NJ",(973) 750-8232,"1167 NJ-23, Kinnelon, NJ 07405",https://www.google.com/maps/place/?q=place_id:ChIJyRkSd8cEw4kRqvv0nIBd29Y&hl=en,none,none,none,none
2212,C,Wise Cabinet Shop,"Morganton, NC",(828) 433-0712,"202 E Parker Rd, Morganton, NC 28655",https://www.google.com/maps/place/?q=place_id:ChIJj9Nj3ZDRUIgRTfbDz59wFS4&hl=en,none,none,none,none
2213,C,Wiggins Construction Custom,"Tifton, GA",(229) 388-9274,"2774 Marshall Dr, Tifton, GA 31793",https://www.google.com/maps/place/?q=place_id:ChIJWeiUzrQB7ogRn-mZqxCR1bc&hl=en,none,none,none,none
2214,C,San Jose Bathroom Remodel,"San Anselmo, CA",(628) 295-7371,"145 Tunstead Ave Ste 12, San Anselmo, CA 94960",https://www.google.com/maps/place/?q=place_id:ChIJ-wXiYQCXhYAROUmy-Ym2Czo&hl=en,none,none,none,none
2215,C,Jt Cabinets & Sons,"Exeter, CA",(559) 799-9192,"815 W Maple St, Exeter, CA 93221",https://www.google.com/maps/place/?q=place_id:ChIJKcK2KuMzlYARQJlLvQ_nuPM&hl=en,none,none,none,none
2216,C,Cabinet Resources,"Auburn, MA",(508) 832-3789,"693 Southbridge St, Auburn, MA 01501",https://www.google.com/maps/place/?q=place_id:ChIJ_2fYllUD5IkRMLKf-AwvZ-A&hl=en,none,none,none,none
2217,C,Blue Mountain Cabinet Suppliers of Hermiston,"Hermiston, OR",(541) 571-7136,"80998 US-395, Hermiston, OR 97838",https://www.google.com/maps/place/?q=place_id:ChIJKxYoU0G5olQRdK88gySom6c&hl=en,none,none,none,none
2218,C,3 Day Kitchens of Arizona,"Sun City, AZ",(623) 512-5893,"11210 W Pueblo Ct, Sun City, AZ 85373",https://www.google.com/maps/place/?q=place_id:ChIJ7dT4dCpDK4cR80nAchUWI6k&hl=en,none,none,none,none
2219,C,Top Tier Bathworks,"Pleasant Hill, IA",(515) 717-1215,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJM0uSu5aV7ocRDcb5tvpAJ2U&hl=en,none,none,none,none
2220,C,William H Robinson Cabinet,"Old Lyme, CT",(860) 526-9876,"313 Joshuatown Rd, Old Lyme, CT 06371",https://www.google.com/maps/place/?q=place_id:ChIJb_fSDzg85okRJeFg7ld9r4Q&hl=en,none,none,none,none
2221,C,Macon County Cabinets,"Decatur, IL",(217) 423-9663,"1001 E Hickory St, Decatur, IL 62526",https://www.google.com/maps/place/?q=place_id:ChIJcfosy9WxdIgRJi395fq3QGU&hl=en,none,none,none,none
2222,C,Paniagua Cabinets,"Hollister, CA",(831) 636-8597,"131 Hillcrest Rd, Hollister, CA 95023",https://www.google.com/maps/place/?q=place_id:ChIJ1_wSCCr2kYAR8kGeF0FAY_E&hl=en,none,none,none,none
2223,C,Horizon Kitchen & Bath Remodeling Culver City,"Culver City, CA",(424) 250-3247,"10811 Washington Blvd, Culver City, CA 90232",https://www.google.com/maps/place/?q=place_id:ChIJXXQwSzi6woARnXVphXfZ8tc&hl=en,none,none,none,none
2224,C,Pride Kitchen Bath Bathroom Remodeling Claremont,"Claremont, CA",(909) 667-8073,"675 W Foothill Blvd, Claremont, CA 91711",https://www.google.com/maps/place/?q=place_id:ChIJUZhYMygww4ARnsVmd4JvVj8&hl=en,none,none,none,none
2225,C,Budget Right Kitchens LTD.,"Oak Park, IL",(877) 507-2126,"1000 N Taylor Ave, Oak Park, IL 60302",https://www.google.com/maps/place/?q=place_id:ChIJDcA4E1bLD4gRuV9sbfbVSHA&hl=en,none,none,none,none
2226,C,Wallace Remodeling,"Blytheville, AR",(870) 206-0878,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJFwih3bgBhQkRxXBg1lzInSU&hl=en,none,none,none,none
2227,C,Custom Tile Installations,"Chino Valley, AZ",(928) 460-2073,"1355 Taft Ave, Chino Valley, AZ 86323",https://www.google.com/maps/place/?q=place_id:ChIJs2O7Jwc3LYcRWzRqgmOz8ZI&hl=en,none,none,none,none
2228,C,Cabinets Plus,"Bemidji, MN",(218) 444-1937,"51243 US-71, Bemidji, MN 56601",https://www.google.com/maps/place/?q=place_id:ChIJe4fiyLgruFIRH2dmYFft-VQ&hl=en,none,none,none,none
2229,C,Montgomery Carpentry & Construction,"Clayton, OH",(937) 216-5413,"5928 W Wenger Rd, Clayton, OH 45315",https://www.google.com/maps/place/?q=place_id:ChIJ34qwfOuBP4gR5cGw8rprhaI&hl=en,none,none,none,none
2230,C,Aiken Tub and Tile Repair and Refinishing,"Aiken, SC",(803) 262-3262,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJSRRb75xL-IgRoLVrLli_hPs&hl=en,none,none,none,none
2231,C,Elegant Kitchens and Home Design,"Staten Island, NY",(718) 967-7700,"20 S Bridge St Ste B, Staten Island, NY 10309",https://www.google.com/maps/place/?q=place_id:ChIJqYGrqKu1w4kRNoHfGS5AHuc&hl=en,none,none,none,none
2232,C,Collins Cabinets,"Russellville, AR",(479) 880-1906,"285 Crow Mountain Rd, Russellville, AR 72802",https://www.google.com/maps/place/?q=place_id:ChIJQQBEYNWszYcRs8-n1rqu8LI&hl=en,none,none,none,none
2233,C,Kitchen and Bath Solutions,"Charlottesville, VA",(434) 466-5232,"1208 E Market St, Charlottesville, VA 22902",https://www.google.com/maps/place/?q=place_id:ChIJr57gmSaJs4kRa0uowZxCm30&hl=en,none,none,none,none
2234,C,Kitchen and Bath Design Center,"Lake Hopatcong, NJ",(973) 810-5300,"820-, 766 NJ-15, Lake Hopatcong, NJ 07849",https://www.google.com/maps/place/?q=place_id:ChIJnwXB3VNzw4kRpjbWliDjUHo&hl=en,none,none,none,none
2235,C,Reliable Remodelers,"St Marys, PA",(814) 389-6866,"134 Robin Rd, St Marys, PA 15857",https://www.google.com/maps/place/?q=place_id:ChIJLQ22DSWtzYkRP6SZOCKMJFo&hl=en,none,none,none,none
2236,C,Mercier's Woodworks,"Ocean Springs, MS",(228) 872-2060,"6521 Sunplex Dr, Ocean Springs, MS 39564",https://www.google.com/maps/place/?q=place_id:ChIJBw-yHan2m4gRNwwUuXZfHWA&hl=en,none,none,none,none
2237,C,Jaime's Custom Cabinets,"City of Atwater, CA",(209) 819-6013,"3514 Atwater Blvd C, City of Atwater, CA 95301",https://www.google.com/maps/place/?q=place_id:ChIJc2j4wrtrkYARzq923spm3NE&hl=en,none,none,none,none
2238,C,Kitchen Brothers,"Riverside, OH",(937) 999-7517,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgc0ezN2FQIgRjlJ0ALd6s28&hl=en,none,none,none,none
2239,C,JC Tile & Home Remodeling llc,"Newton, NC",(704) 201-0015,"504 S Main Ave, Newton, NC 28658",https://www.google.com/maps/place/?q=place_id:ChIJndzsB4Q1UYgRYGYfKydWdWA&hl=en,none,none,none,none
2240,C,Heffner Flooring & Tile LLC,"Greenbrier, AR",(501) 589-5107,"608 AR-25, Greenbrier, AR 72058",https://www.google.com/maps/place/?q=place_id:ChIJ40HhFCb__2UR4Gj7B401se0&hl=en,none,none,none,none
2241,C,Precision Remodeling of IL inc.,"Centralia, IL",(779) 279-9412,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJtdt0i_IpDIgR14oQXEzFeGA&hl=en,none,none,none,none
2242,C,"Kitchens By Design, Inc.","Sterling, MA",(978) 422-6008,"57 Old Princeton Rd W, Sterling, MA 01564",https://www.google.com/maps/place/?q=place_id:ChIJJTPIS8j544kR-cp2gc69LaY&hl=en,none,none,none,none
2243,C,Jason Morris Tile Installer,"Fort Madison, IA",(319) 316-8119,"3178 180th St, Fort Madison, IA 52627",https://www.google.com/maps/place/?q=place_id:ChIJP8ptTMbX5ocR6DpQI2LuMnc&hl=en,none,none,none,none
2244,C,Urban Kitchen and Bath LLC,"Germantown, MD",(240) 370-7656,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzSmpGhMttokRjzaHuNZmcyQ&hl=en,none,none,none,none
2245,C,Kitchen Designs,"Kingsport, TN",(423) 378-5181,"830 W Center St, Kingsport, TN 37660",https://www.google.com/maps/place/?q=place_id:ChIJKX6Cr1ftWogR8UNf1jhdwd4&hl=en,none,none,none,none
2246,C,S&S Home Supplies Inc.,"Daly City, CA",(415) 330-9288,"419 Allan St, Daly City, CA 94014",https://www.google.com/maps/place/?q=place_id:ChIJZ1EriNB-j4ARbK5tpQZir5I&hl=en,none,none,none,none
2247,C,Dericko Remodeling,"Grandview, MO",(816) 342-5742,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJaXi5JwjdwIcRVXjeWN5hDX8&hl=en,none,none,none,none
2248,C,Cedar Rose Woodworks,"Cañon City, CO",(719) 269-9171,"1210 Park Ave, Cañon City, CO 81212",https://www.google.com/maps/place/?q=place_id:ChIJX4SOZnuPFIcRCxSPjlHCXGg&hl=en,none,none,none,none
2249,C,A+ Construction And Remodeling Service,"Zion, IL",(847) 244-4444,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJI_mM28jyD4gREpV0YMPaohE&hl=en,none,none,none,none
2250,C,Cincinnati Bathroom Remodeling Pros,"Cincinnati, OH",(513) 547-6539,"147 E McMicken Ave #2, Cincinnati, OH 45202",https://www.google.com/maps/place/?q=place_id:ChIJNTcXmfyzQYgRd2h2r2bayb4&hl=en,none,none,none,none
2251,C,HERRERA REMODELING LLC,"Indianapolis, IN",(463) 426-0149,"225 N Holmes Ave, Indianapolis, IN 46222",https://www.google.com/maps/place/?q=place_id:ChIJwRbGfwdXa4gR8beYwhRmxus&hl=en,none,none,none,none
2252,C,Strand Home Services LLC,"Marshall, MN",(507) 720-4864,"902 Birch St, Marshall, MN 56258",https://www.google.com/maps/place/?q=place_id:ChIJaWvzsYdZiocRlfE-IkKIVq0&hl=en,none,none,none,none
2253,C,Pinpoint Kitchen & Bath Showroom,"Williston Park, NY",(516) 833-5151,"348 Hillside Ave., Williston Park, NY 11596",https://www.google.com/maps/place/?q=place_id:ChIJVehBh_2HwokR5d2v8nJ5DKg&hl=en,none,none,none,none
2254,C,Modern Design Center,"Cherry Hill Township, NJ",(856) 288-1300,"912 Haddonfield Rd B, Cherry Hill Township, NJ 08002",https://www.google.com/maps/place/?q=place_id:ChIJFUVZWDvjb0AR6_uVFxOXBio&hl=en,none,none,none,none
2255,C,Fort Wayne Bathroom Remodeling Pros,"Fort Wayne, IN",(260) 295-8727,"5420 Lake Ave, Fort Wayne, IN 46815",https://www.google.com/maps/place/?q=place_id:ChIJ___j23v7FYgReedwqE8Vrpk&hl=en,none,none,none,none
2256,C,BP REMODELING AND CONSTRUCTION,"Rosenberg, TX",(832) 509-6933,"5108 Alderney Ct #5686, Rosenberg, TX 77471",https://www.google.com/maps/place/?q=place_id:ChIJDxi2mDMcQYYRF9OwYZU7CxI&hl=en,none,none,none,none
2257,C,Gervais Kitchen Cabinets,"Methuen, MA",(508) 982-5852,"1 Ferndale Ave, Methuen, MA 01844",https://www.google.com/maps/place/?q=place_id:ChIJj_owhdSp44kRtPIZi9G4Dlc&hl=en,none,none,none,none
2258,C,CDUBBS REMODELING,"Big Spring, TX",(432) 213-4095,"1503 Lexington Ave, Big Spring, TX 79720",https://www.google.com/maps/place/?q=place_id:ChIJEfzp0H4j-YYR6h3cuUY5rWE&hl=en,none,none,none,none
2259,C,Gold Remodeling Wildomar.,"Wildomar, CA",(925) 940-1124,"20616 Sydney Ct, Wildomar, CA 92595",https://www.google.com/maps/place/?q=place_id:ChIJTY3ChTib3IARFdDdRjGb9o0&hl=en,none,none,none,none
2260,C,"H&A Remodeler | Home, Deck & Kitchen Remodeling Quail Ridge","Boise, ID",(208) 508-1526,"3835 N Woody Ln, Boise, ID 83703",https://www.google.com/maps/place/?q=place_id:ChIJO-77_Qr_rlQRo4VqF2LMA3I&hl=en,none,none,none,none
2261,C,MT-Bath.INC,"Morton Grove, IL",(224) 715-2854,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJoexOsYetZUMRcduzxXGwzkk&hl=en,none,none,none,none
2262,C,Bulldog Renovations and Solutions LLC,"Pittsford, NY",(585) 416-8720,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ367EH6Zk0KER6sFpNdzkJig&hl=en,none,none,none,none
2263,C,Vanderhoof Custom Cabinets,"Verona, NY",(315) 336-3015,"5317 Old Oneida Rd, Verona, NY 13478",https://www.google.com/maps/place/?q=place_id:ChIJqfcYPa9y2YkR2dqzIh0vlK8&hl=en,none,none,none,none
2264,C,Silver Pine Kitchen Remodeler La Mirada,"La Mirada, CA",(562) 574-2954,"15290 Rosecrans Ave, La Mirada, CA 90638",https://www.google.com/maps/place/?q=place_id:ChIJJeYljeAr3YARehYU0Gm-w40&hl=en,none,none,none,none
2265,C,King Custom Cabinets,"Yuba City, CA",(530) 845-2614,"367 Burns Dr #3, Yuba City, CA 95991",https://www.google.com/maps/place/?q=place_id:ChIJZerDpttSm4ARfpUDGFr3kR4&hl=en,none,none,none,none
2266,C,RPD Construction LLC - Home Improvement Contractor,"Norwich, CT",(860) 884-5921,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgath3bbFyKYRt56K2K5k0G4&hl=en,none,none,none,none
2267,C,Fast Pro Kitchen,"Chelsea, MA",(781) 885-5776,"22B Willow St, Chelsea, MA 02150",https://www.google.com/maps/place/?q=place_id:ChIJKQSuPuNx44kRqX-BQoCUMAI&hl=en,none,none,none,none
2268,C,C&C Quality Home Improvement - Home Renovation Companies Port Chester NY,"Port Chester, NY",(914) 580-4336,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMVBS916XwokRrjwXqIofCIc&hl=en,none,none,none,none
2269,C,Pelaez Renovations LLC,"Leland, NC",(910) 612-0324,"2417 Palisade Ct, Leland, NC 28451",https://www.google.com/maps/place/?q=place_id:ChIJu7P-XeYZqokRHHC35h_ODw4&hl=en,none,none,none,none
2270,C,Superior Home Remodeling,"Morrisville, PA",(609) 310-9260,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJS9IIbYNeb4QRM1ue2tOuUDk&hl=en,none,none,none,none
2271,C,Reliable Home Remodeling & Repair,"Gun Barrel City, TX",(430) 207-0365,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDawuIKF2-ggRu8RKSdqyQZA&hl=en,none,none,none,none
2272,C,Kitchen World Inc.,"Ponte Vedra Beach, FL",(844) 579-0905,"244 Pablo Rd, Ponte Vedra Beach, FL 32082",https://www.google.com/maps/place/?q=place_id:ChIJuYN8cjc35IgRQi7qdabbqe8&hl=en,none,none,none,none
2273,C,Tennessee Craftsmen,"Franklin, TN",(615) 294-2544,"114 Blue Grass Dr, Franklin, TN 37064",https://www.google.com/maps/place/?q=place_id:ChIJm1Ux11J_ZIgRsP8vdHToSwo&hl=en,none,none,none,none
2274,C,Higley Cabinets LLC.,"Heyburn, ID",(208) 679-4630,"2800 Nevada St, Heyburn, ID 83336",https://www.google.com/maps/place/?q=place_id:ChIJPXf46-I2q1QR0IQKuTnNMRw&hl=en,none,none,none,none
2275,C,Donovan Design & Build Inc,"South Bend, IN",(574) 291-9222,"19641 Lucinda St, South Bend, IN 46614",https://www.google.com/maps/place/?q=place_id:ChIJTwzD7gvMFogRt_nLNO_K3z0&hl=en,none,none,none,none
2276,C,Aguilar Remodeling,"South Houston, TX",(832) 933-2852,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHfMGC9x19wURJMkb_caQiRo&hl=en,none,none,none,none
2277,C,SOUTHERN RUSTIC,"Pineville, LA",(318) 277-0808,"1203 Pearce Rd, Pineville, LA 71360",https://www.google.com/maps/place/?q=place_id:ChIJNdxv2Z5LJYYRne2o25bhsbg&hl=en,none,none,none,none
2278,C,Olymp construction,"Bellevue, WA",(425) 410-0023,"15248 SE 39th St, Bellevue, WA 98006",https://www.google.com/maps/place/?q=place_id:ChIJ_Vh5bVswUY0Rysv1X63mHB8&hl=en,none,none,none,none
2279,C,AD Golden Renovation LLC,"Harrisburg, NC",(704) 421-5480,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJUwyhBAAZVIgRe5Qmu9zJ5M0&hl=en,none,none,none,none
2280,C,Signature cabinet company,"Brainerd, MN",(218) 513-9025,"17043 Commercial Park Rd, Brainerd, MN 56401",https://www.google.com/maps/place/?q=place_id:ChIJPczGKvq5tlIRBOpli-mwZEc&hl=en,none,none,none,none
2281,C,Spence Construction LLC,"Runnemede, NJ",(856) 292-5327,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJj_5ry__F5yURATf09hyKyc4&hl=en,none,none,none,none
2282,C,Bazh Re-construction,"Mansfield, TX",(817) 841-2047,"211 Hillcrest St, Mansfield, TX 76063",https://www.google.com/maps/place/?q=place_id:ChIJ0X3FRRRhToYRV5K_aB_69Tk&hl=en,none,none,none,none
2283,C,California Granite & Natural Stone Inc,"Guadalupe, CA",(805) 343-7783,"190 Guadalupe St, Guadalupe, CA 93434",https://www.google.com/maps/place/?q=place_id:ChIJYaVpzCxC7IARGs3HPr7uA_w&hl=en,none,none,none,none
```
