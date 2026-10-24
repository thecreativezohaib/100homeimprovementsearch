# Round 2: Gemini task 2, part 11 of 17 (100 businesses, rows 2084 to 2183)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 2183: reply in that chat "Continue with
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
2084,C,All Around Contractors,"Washington, PA",(724) 350-7153,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJa7McTxmb62QR6KFMtJC0ce0&hl=en,none,none,none,none
2085,C,Strong Remodeling LLC,"Clarkston, GA",(770) 588-4826,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP_b6vc-GaQARIpz18ri-NYw&hl=en,none,none,none,none
2086,C,"H&A Remodeler | Home, Deck & Kitchen Remodeling Highlands","Boise, ID",(208) 877-4791,"3511 N Crane Vw Ln, Boise, ID 83702",https://www.google.com/maps/place/?q=place_id:ChIJe2W6k4z_rlQRcjrOx3SIZ4w&hl=en,none,none,none,none
2087,C,W M Enterprise Custom Woodworking,"Zanesville, OH",(740) 452-2325,"2670 S Pleasant Grove Rd, Zanesville, OH 43701",https://www.google.com/maps/place/?q=place_id:ChIJq-8DVanuN4gR_idC_A_JxUQ&hl=en,none,none,none,none
2088,C,Melton Cabinet Painting,"Kingston, TN",(865) 455-8149,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJX4y06XnZXYgRtR2WG1UeNHI&hl=en,none,none,none,none
2089,C,Sharp Remodeling Specialty.,"Ranburne, AL",(205) 369-1836,"278 3rd Ave N, Ranburne, AL 36273",https://www.google.com/maps/place/?q=place_id:ChIJBxBUkL8MiYgROCfis1WcVOs&hl=en,none,none,none,none
2090,C,Hero Bathroom Remodeling Torrance,"Torrance, CA",(424) 449-2062,"3321 W Carson St, Torrance, CA 90503",https://www.google.com/maps/place/?q=place_id:ChIJaxedxerBtokRP_mtXYzLwkc&hl=en,none,none,none,none
2091,C,Martin Residential Upgrades,"Lebanon, PA",(717) 679-2877,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJlyE3YeG-U4ERXErD8Mg719Y&hl=en,none,none,none,none
2092,C,Home innovations of Augusta,"Martinez, GA",(706) 469-9921,"4812 Technology Dr Building 3, Martinez, GA 30907",https://www.google.com/maps/place/?q=place_id:ChIJ-2iFn6nT-YgRW1o18uaaXHI&hl=en,none,none,none,none
2093,C,UPSTATE YANKEE REMODELING MITIGATION LLC,"Hickory, NC",(828) 238-4570,"2011 Kool Pk Rd NE, Hickory, NC 28601",https://www.google.com/maps/place/?q=place_id:ChIJj7lDNXA7UYgRoTp9kauEips&hl=en,none,none,none,none
2094,C,Home Renovation Solution,"Columbus, GA",(762) 258-3270,"4001 Earline Ave, Columbus, GA 31904",https://www.google.com/maps/place/?q=place_id:ChIJfW3Q19zNjIgRUhQO1-rJueM&hl=en,none,none,none,none
2095,C,Ray Hill Cabinet Shop,"Gardendale, AL",(205) 631-4410,"525 Garst Dr, Gardendale, AL 35071",https://www.google.com/maps/place/?q=place_id:ChIJfRvsL_4DiYgRE-6OwzCNQFw&hl=en,none,none,none,none
2096,C,Anderson Home Renovations,"Fayetteville, TN",(931) 691-9624,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJr7TuC2NtxCQR4GZL5Ib4aQ8&hl=en,none,none,none,none
2097,C,Cervantes Remodeling,"Corsicana, TX",(903) 875-0055,"1901 W 2nd Ave, Corsicana, TX 75110",https://www.google.com/maps/place/?q=place_id:ChIJS2idOhssT4YRt4EPKMehgUA&hl=en,none,none,none,none
2098,C,Whatever It Takes Remodeling,"Taylor, TX",(512) 517-4308,"Taylor, TX 76574",https://www.google.com/maps/place/?q=place_id:ChIJLYWKE9znRIYR5oOIWTXt06E&hl=en,none,none,none,none
2099,C,Legacy Safe Homes,"The Woodlands, TX",(844) 432-8364,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJRTamazgxR4YR9fgOe-EsEv8&hl=en,none,none,none,none
2100,C,Harrison Boulevard Remodeler | Home Remodeling,"Boise, ID",(208) 987-3294,"1612 W Irene St, Boise, ID 83702",https://www.google.com/maps/place/?q=place_id:ChIJi1EmjDz5rlQRHK63w3y1Gr4&hl=en,none,none,none,none
2101,C,East End Remodeler | Home Remodeling,"Boise, ID",(208) 759-1116,"123 N Elm Ave, Boise, ID 83706",https://www.google.com/maps/place/?q=place_id:ChIJRd2SHHr5rlQRhodj9bVFxP4&hl=en,none,none,none,none
2102,C,FLORIDA ALL IN HOME SERVICES LLC,"Palmetto, FL",(941) 462-0653,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7SHvmSbs0m4R-xTd3i0QCRM&hl=en,none,none,none,none
2103,C,"Cherry Homes, Inc.","Harper Woods, MI",(586) 295-0203,"18775 Eastwood Dr, Harper Woods, MI 48225",https://www.google.com/maps/place/?q=place_id:ChIJyz_okVDWJIgRSabFuGBVy5w&hl=en,none,none,none,none
2104,C,THE KITCHEN..,"Dothan, AL",(334) 796-4291,"105 S Woodburn Dr #1, Dothan, AL 36305",https://www.google.com/maps/place/?q=place_id:ChIJQyZ6xZ6NkogRCM-vtwLwuPQ&hl=en,none,none,none,none
2105,C,Paul Allen Construction,"Weatherford, TX",(817) 658-9803,"1839 E Lake Dr, Weatherford, TX 76087",https://www.google.com/maps/place/?q=place_id:ChIJJThHNyQHToYRSekPvP7HwAg&hl=en,none,none,none,none
2106,C,La Plata Diamond,"Durango, CO",(970) 417-7268,"361 S Camino Del Rio #153, Durango, CO 81303",https://www.google.com/maps/place/?q=place_id:ChIJ8cjYJwMDPIcRvXxUEX3fSvw&hl=en,none,none,none,none
2107,C,Primetime Remodeling,"Georgetown, TX",(512) 948-2078,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_X-xHxp2WIIRHd2T8Jxtd50&hl=en,none,none,none,none
2108,C,"Chad's Remodeling, L.L.C.","Lecompte, LA",(318) 290-4730,"1512 Weems Ave, Lecompte, LA 71346",https://www.google.com/maps/place/?q=place_id:ChIJQ8BsWamyUEIROvLldeobyi0&hl=en,none,none,none,none
2109,C,Ironwood Remodeling Co,"Stockton, CA",(209) 210-3915,"1111 N El Dorado St, Stockton, CA 95202",https://www.google.com/maps/place/?q=place_id:ChIJmWQjbF8vAgsRAwXvXfbQu4s&hl=en,none,none,none,none
2110,C,Aqua Lux Bath Systems,"Canton, MI",(734) 272-9465,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJibsyB3apWa4RhMsE46GzEJY&hl=en,none,none,none,none
2111,C,Empire Renovations LLC,"Winter Park, FL",(321) 229-2691,"2830 Forsyth Rd Unit 400, Winter Park, FL 32792",https://www.google.com/maps/place/?q=place_id:ChIJ2zbBcAdKoS0RFjSeMhiUO60&hl=en,none,none,none,none
2112,C,South Texas Supreme Remodel,"Ingleside, TX",(361) 218-7775,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJwW8wIxz3aIYRe22348nHXOU&hl=en,none,none,none,none
2113,C,Ceramic Solutions,"Midwest City, OK",(405) 410-8454,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ5abcuZo8socRAcS2OZqf_bk&hl=en,none,none,none,none
2114,C,Intrinsic Elite Services LLC,"Crestview, FL",(850) 842-8255,"123 Strike Eagle Dr, Crestview, FL 32536",https://www.google.com/maps/place/?q=place_id:ChIJqeyfhC6ZeKoRwgbgspGlHzI&hl=en,none,none,none,none
2115,C,LGR Remodeling LLC,"Burlington, NC",(901) 801-0497,"2303 McKinney St, Burlington, NC 27217",https://www.google.com/maps/place/?q=place_id:ChIJLR8egF0rU4gRed-OUvOeRUA&hl=en,none,none,none,none
2116,C,B&B Unique Remodeling,"West Roxbury, MA",(617) 327-4696,"45 Fairlane Rd, West Roxbury, MA 02132",https://www.google.com/maps/place/?q=place_id:ChIJG8t9691_44kRfbM30UFpTUk&hl=en,none,none,none,none
2117,C,JD Total Renovation,"St. Louis, MO",(314) 532-3259,"4014 S Grand Blvd unit A, St. Louis, MO 63118",https://www.google.com/maps/place/?q=place_id:ChIJVRaeVBu12IcRUfF8QDcm1G4&hl=en,none,none,none,none
2118,C,YNK Renovation LLC,"Douglasville, GA",(404) 510-6153,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJK77cBhoIaAYRjKP-y1Yn5LI&hl=en,none,none,none,none
2119,C,Chapel Cabinet Company,"Russellville, KY",(270) 542-4051,"8072 Morgantown Rd, Russellville, KY 42276",https://www.google.com/maps/place/?q=place_id:ChIJNfjWZeSYZYgR2o-XOV3b_CE&hl=en,none,none,none,none
2120,C,Kerr Cabinet Co DBA Signature Cabinetry by Kerr,"Oxford, AL",(256) 831-8270,"2009 Barry St, Oxford, AL 36203",https://www.google.com/maps/place/?q=place_id:ChIJxZLeTy6xi4gROxPCkRm-fwE&hl=en,none,none,none,none
2121,C,R K Morris & Company,"San Juan Capistrano, CA",(949) 248-0770,"33021 Calle Perfecto, San Juan Capistrano, CA 92675",https://www.google.com/maps/place/?q=place_id:ChIJ66cGSrnx3IARQzQHe7LxIjM&hl=en,none,none,none,none
2122,C,"Happy Home Remodeling, LLC","Post Falls, ID",(720) 713-3443,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJV6zawm3BYVMRmbuxYIjibv0&hl=en,none,none,none,none
2123,C,H&A Remodeler | Home & Kitchen Remodeling Mesa H&A,"Boise, ID",(208) 209-7860,"2067 E Toluka Wy, Boise, ID 83712",https://www.google.com/maps/place/?q=place_id:ChIJG36Nu5_5rlQRsN_8brcKvWQ&hl=en,none,none,none,none
2124,C,"Al Renovations,","El Monte, CA",(626) 627-7498,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJsS9nR4qlRQMRkPthpL_Vd_c&hl=en,none,none,none,none
2125,C,Flathead Granite Fab,"Columbia Falls, MT",(406) 897-3716,"5385 US-2, Columbia Falls, MT 59912",https://www.google.com/maps/place/?q=place_id:ChIJ03-Vd8dBZlMRv8ZXnfoy818&hl=en,none,none,none,none
2126,C,Contraluz Construction,"Veneta, OR",(541) 228-2860,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_6ZChFb5ESoRwJaAI_mL79E&hl=en,none,none,none,none
2127,C,Blissful Bathroom Remodel San Francisco,"Tiburon, CA",(415) 704-7021,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJSXgqh-F8UU0R26smioKAmXs&hl=en,none,none,none,none
2128,C,Supreme Stone LLC,"Romulus, MI",(734) 351-1060,"15570 S Huron River Dr, Romulus, MI 48174",https://www.google.com/maps/place/?q=place_id:ChIJj3FFh4pFO4gRU3l43VfLLOA&hl=en,none,none,none,none
2129,C,LL Home Renovation and Custom Design LLC.,"Mt Clemens, MI",(586) 298-2301,"560 Chippewa St, Mt Clemens, MI 48043",https://www.google.com/maps/place/?q=place_id:ChIJhbQZdY4hJYgRWTMQMIChKzs&hl=en,none,none,none,none
2130,C,Elite Kitchen Remodeling Northwest Suburbs,"Schaumburg, IL",(870) 408-6790,"1051 Perimeter Dr Ste 367, Schaumburg, IL 60173",https://www.google.com/maps/place/?q=place_id:ChIJG7tn9BCvD4gRalSjx-PmiaU&hl=en,none,none,none,none
2131,C,A & B Countertops,"Temple, GA",(770) 459-5055,"1482 US-78, Temple, GA 30179",https://www.google.com/maps/place/?q=place_id:ChIJcQWI0AHViogRYW8WL_X5Zq4&hl=en,none,none,none,none
2132,C,Hayes Remodeling LLC,"Milan, TN",(731) 402-1529,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJn3g7iZkXBgkRtjKohFpUsxE&hl=en,none,none,none,none
2133,C,Moyer Modern Construction,"Bozeman, MT",(484) 925-9120,"404 E Story St, Bozeman, MT 59715",https://www.google.com/maps/place/?q=place_id:ChIJawhq9_jVYwIRBbUibmQRDO8&hl=en,none,none,none,none
2134,C,C & C Home Improvements,"Nicholasville, KY",(859) 881-9257,"3460 Union Mill Rd, Nicholasville, KY 40356",https://www.google.com/maps/place/?q=place_id:ChIJby8-9UhYQogRCqeSt7pZpl0&hl=en,none,none,none,none
2135,C,Fletcher Decorating Inc,"Beatrice, NE",(402) 223-5204,"414 Court St, Beatrice, NE 68310",https://www.google.com/maps/place/?q=place_id:ChIJLcDSugJolocRocBTxLXV0i8&hl=en,none,none,none,none
2136,C,Pompano Beach Remodeling Kitchen and Bathroom Expert,"Pompano Beach, FL",(239) 205-1199,"2500 W Atlantic Blvd, Pompano Beach, FL 33069",https://www.google.com/maps/place/?q=place_id:ChIJeRAeocQD2YgRpbaVjueQOO0&hl=en,none,none,none,none
2137,C,"JG Kitchen, Bath and decking","Dover, DE",(302) 526-6948,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6WaU5I17x4kRRZ3FozcWcVw&hl=en,none,none,none,none
2138,C,Cabinet Designs Unlimited,"Camas, WA",(360) 834-4690,"1738 SE 8th Ave # A, Camas, WA 98607",https://www.google.com/maps/place/?q=place_id:ChIJU5UsGfy8lVQRoLWzzWrUzSI&hl=en,none,none,none,none
2139,C,Butte Cabinet & Supply,"Oroville, CA",(530) 533-8222,"1830 Grace St, Oroville, CA 95966",https://www.google.com/maps/place/?q=place_id:ChIJ89ILbsu1nIARmt4fpxXLFFM&hl=en,none,none,none,none
2140,C,Kansas City Cabinet Restoration | Kitchen & Bath Cabinet Refinishing & Refacing Service,"Shawnee, KS",(816) 290-7284,"12115 Johnson Dr, Shawnee, KS 66216",https://www.google.com/maps/place/?q=place_id:ChIJ781GPCLxwIcRHQAEtqVCDX4&hl=en,none,none,none,none
2141,C,Innovative Renovations LLC,"Slidell, LA",(985) 503-2522,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGXMXu5PnnYgRlW_G205mcGA&hl=en,none,none,none,none
2142,C,Alexander Construction Cabinetry,"Murray, KY",(270) 727-9326,"307 Railroad Ave, Murray, KY 42071",https://www.google.com/maps/place/?q=place_id:ChIJreWD7-rKe4gRdysMW1QOMLY&hl=en,none,none,none,none
2143,C,"Sutton Construction, Inc.","Troy, MI",(248) 808-0286,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxUsvSzDFJIgRRwB5Ldj2eyo&hl=en,none,none,none,none
2144,C,JD's Remodeling & Repair LLC,"Yuma, AZ",(928) 345-8960,"11475 S Prescott Ave, Yuma, AZ 85365",https://www.google.com/maps/place/?q=place_id:ChIJf7ThRWlh1oARAmlPUI_4BKY&hl=en,none,none,none,none
2145,C,K&A Remodeling Services LLC,"Apopka, FL",(407) 494-2474,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJyUcUcluf54gRaAFuC72smaU&hl=en,none,none,none,none
2146,C,Coldwater Building and Renovations LLC,"Milton, FL",(850) 712-1436,"5961 Rustic Ridge Circle, Milton, FL 32570",https://www.google.com/maps/place/?q=place_id:ChIJj3uRcuYwmakRj-qROS6HYy0&hl=en,none,none,none,none
2147,C,Austin's Dream Remodeling,"Cambridge, MD",(443) 521-3448,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0YSeQ9NLuIkRVAmtn9pTDMU&hl=en,none,none,none,none
2148,C,AmaDiaz Installations,serves professionalism!,(214) 632-0395,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAZ5BAOA3TIYRiPBEcFq_7QQ&hl=en,none,none,none,none
2149,C,The Carpenter LLC,"Duncan, OK",(580) 641-2420,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDyV-w7xlPk8RMqkPB8gI8DA&hl=en,none,none,none,none
2150,C,US Kitchen Bath Bathroom Remodeling Thousand Oaks,"Thousand Oaks, CA",(805) 710-8767,"23 E Avenida De Los Arboles, Thousand Oaks, CA 91362",https://www.google.com/maps/place/?q=place_id:ChIJB18HJfIv6IARbWHRRNIlVsE&hl=en,none,none,none,none
2151,C,Rogue Remodel,"Lafayette, OR",(503) 747-8737,"120 W 13th St, Lafayette, OR 97127",https://www.google.com/maps/place/?q=place_id:ChIJt9-YhUdHlVQRsa3PesM9MHs&hl=en,none,none,none,none
2152,C,Coreem Hairston & Son Remodeling & Repairs,"Bayonne, NJ",(201) 779-7954,"17 Chase Ct, Bayonne, NJ 07002",https://www.google.com/maps/place/?q=place_id:ChIJcbewUZ1RwokROkivIzyoSoQ&hl=en,none,none,none,none
2153,C,West GA Refinishing LLC,"Temple, GA",(404) 717-3340,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvzYPvXDViogR-u3146HWvBY&hl=en,none,none,none,none
2154,C,MR Remodeling,"DeSoto, TX",(469) 881-2259,"1009 Gracelane Dr, DeSoto, TX 75115",https://www.google.com/maps/place/?q=place_id:ChIJlwHtLlWTToYREudYPk8yKOI&hl=en,none,none,none,none
2155,C,Cabo Kitchen & Bath,"Spring Valley, NY",(845) 459-2226,"12 Jackson Ave, Spring Valley, NY 10977",https://www.google.com/maps/place/?q=place_id:ChIJA9wgJc7dwokR0x0BTK-D2H0&hl=en,none,none,none,none
2156,C,Project Pros Construction,"Mexico, MO",(573) 721-8717,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVxLKUIVy_4ARqPzHd_Ww7CA&hl=en,none,none,none,none
2157,C,"Reborn Renovation, LLC","Bristol, CT",(860) 506-5399,"77 Daisy Cir, Bristol, CT 06010",https://www.google.com/maps/place/?q=place_id:ChIJXyRyhCWx54kRp_O08S9rQt0&hl=en,none,none,none,none
2158,C,Additions Home Improvement LLC.,"East Hampton, CT",(959) 226-0263,"9 Wildwood Ln, East Hampton, CT 06424",https://www.google.com/maps/place/?q=place_id:ChIJNVSqAryFGyYRBco53fJ8G9A&hl=en,none,none,none,none
2159,C,Aaron’s painting & Remodeling,"Sealy, TX",(832) 660-4541,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhTac0NoaBWARVMopVSF0nT4&hl=en,none,none,none,none
2160,C,Ellett Woodworks,"Burnet, TX",(512) 755-2884,"4956, 1001 Co Rd 335, Burnet, TX 78611",https://www.google.com/maps/place/?q=place_id:ChIJa5KkecvmWoYRRT09VvnhRfY&hl=en,none,none,none,none
2161,C,Cabinet Designs,"Muscle Shoals, AL",(256) 381-1609,"105 Commerce St, Muscle Shoals, AL 35661",https://www.google.com/maps/place/?q=place_id:ChIJ8753Wh5PfYgRIiJo1tWL6sQ&hl=en,none,none,none,none
2162,C,Cruz Right Remodeling LLC,"Thornton, CO",(720) 883-8061,"Colorado Blvd &, E 115th Ave, Thornton, CO 80233",https://www.google.com/maps/place/?q=place_id:ChIJQ7iEuMMPSSYR2MFNioMwj6Q&hl=en,none,none,none,none
2163,C,ANDONEGUI REMODELING,"Fort Worth, TX",(817) 694-5174,"3717 May St, Fort Worth, TX 76110",https://www.google.com/maps/place/?q=place_id:ChIJv1vZccdxToYRqL5BO9NiXH4&hl=en,none,none,none,none
2164,C,H&A Remodeler | Home Remodeling Meridian,"Meridian, ID",(208) 784-7832,"2045 W Overland Rd, Meridian, ID 83642",https://www.google.com/maps/place/?q=place_id:ChIJD90TeMNRrlQRuvfVA4RcE3A&hl=en,none,none,none,none
2165,C,Jorge Builders,"Newington, CT",(959) 201-1448,"130 Waverly Dr, Newington, CT 06111",https://www.google.com/maps/place/?q=place_id:ChIJ_QvtLtyz54kRd2onnFBZoWM&hl=en,none,none,none,none
2166,C,Corbin Cabinetry Inc,"Philomath, OR",(541) 929-4048,"2651 Main St, Philomath, OR 97370",https://www.google.com/maps/place/?q=place_id:ChIJgZ-59HVHwFQRCE37J3ljRRQ&hl=en,none,none,none,none
2167,C,"C H Home Improvements, Inc.","Ankeny, IA",(515) 865-8929,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJuyQNEmL-RG8RopSubgQAENI&hl=en,none,none,none,none
2168,C,Hcs Kitchen And Bath,"Memphis, TN",(901) 384-8755,"7560 A E Beaty Dr, Memphis, TN 38133",https://www.google.com/maps/place/?q=place_id:ChIJVVVltYOdf4gRW0xZ9YPCudI&hl=en,none,none,none,none
2169,C,Cbuildinteriors,"Kingston, NY",(845) 594-7773,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJy4s13YzVdo0RIdEnJ1m0qWs&hl=en,none,none,none,none
2170,C,Home Remodelers in Dallas,"Plano, TX",(469) 210-1139,"5830 Granite Pkwy #100-346, Plano, TX 75024",https://www.google.com/maps/place/?q=place_id:ChIJe4DZ0R_v_IkRz4tlHbE8GYs&hl=en,none,none,none,none
2171,C,Calancea home building,"Ypsilanti, MI",(734) 260-6489,"10382 Martz Rd, Ypsilanti, MI 48197",https://www.google.com/maps/place/?q=place_id:ChIJO7etQFFZO4gRUKh2yFxgesE&hl=en,none,none,none,none
2172,C,Chicago Builders & Remodeling Team,"Addison, IL",(331) 215-8779,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJE-3NIOCtD4gRgjR0I_NUbGI&hl=en,none,none,none,none
2173,C,Exotic Stones,"Carriere, MS",(601) 798-4334,"6985 US-11, Carriere, MS 39426",https://www.google.com/maps/place/?q=place_id:ChIJcerf1ie8nYgR-D6E-yONwXM&hl=en,none,none,none,none
2174,C,"All Builders Millworks, Llc","Ruston, LA",(318) 381-2586,"758 Burgessville Rd, Ruston, LA 71270",https://www.google.com/maps/place/?q=place_id:ChIJNVdMaJbbMYYRC6TAR9nVB7k&hl=en,none,none,none,none
2175,C,"H&A Remodeler | Home, Deck & Kitchen Remodeling Eagle","Eagle, ID",(208) 603-5471,"79 E Aikens Rd, Eagle, ID 83616",https://www.google.com/maps/place/?q=place_id:ChIJe4XM0Iurr1QRKhu3mMzPXMU&hl=en,none,none,none,none
2176,C,R&R Tile Services LLC,"Union Gap, WA",(509) 406-5828,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZbUn-1ElsSARFxj2VV_jb-4&hl=en,none,none,none,none
2177,C,Hilton Head Home Solutions,"Hilton Head Island, SC",(843) 227-4087,"18 Executive Park Rd #3, Hilton Head Island, SC 29928",https://www.google.com/maps/place/?q=place_id:ChIJ8WU2zzx5_IgRR6X27DaD6V0&hl=en,none,none,none,none
2178,C,Our Tops LLC,"Barberton, OH",(330) 396-1974,"846 Coventry Rd, Barberton, OH 44203",https://www.google.com/maps/place/?q=place_id:ChIJywakG5jVMIgRIHhY-qm4gbY&hl=en,none,none,none,none
2179,C,Rodabough Construction,"Layton, UT",(801) 499-2288,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv6mmgod15YsRzJJZNI0FhGM&hl=en,none,none,none,none
2180,C,Handyman Can Utah,"Cedar City, UT",(385) 219-7186,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0wUzgIthtYARGrfbwKnXlI4&hl=en,none,none,none,none
2181,C,Hobbs Property Improvement LLC,"Bath, NY",(607) 684-1346,"13 Hillview Dr, Bath, NY 14810",https://www.google.com/maps/place/?q=place_id:ChIJ63MfQHmv0YkR8gJMyrU9txc&hl=en,none,none,none,none
2182,C,"Elite Tile and Remodeling, LLC","Petersburg, VA",(804) 888-4501,"17917 Sandy Ford Rd, Petersburg, VA 23803",https://www.google.com/maps/place/?q=place_id:ChIJDyzjrRqhsYkRPPh-IBmFiV0&hl=en,none,none,none,none
2183,C,Watson Construction,"Greenville, MS",(662) 703-1991,"700 Sewanee St, Greenville, MS 38701",https://www.google.com/maps/place/?q=place_id:ChIJo85lEXXtK4YR9Di2pGa29FE&hl=en,none,none,none,none
```
