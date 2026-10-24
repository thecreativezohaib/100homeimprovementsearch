# Round 2: Gemini task 3, part 18 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 2166, reply in that chat "Continue with the businesses
   after LAST_ROW_DONE, same rules, same columns" and keep that report too.

## The task (Gemini: follow this exactly)
```
You are doing a research task on 50 small kitchen and bathroom remodeling businesses in the United States. Each one
has a Google Business Profile but no working website. I need, for each one: a contact email that the business itself
has published, and its own Facebook page and/or Instagram profile. Work through the table at the end of this file
from top to bottom and do NOT skip any. Research every row BEFORE you write the report.

The "task" column says what each row needs:
- E: the email is already known (known_email). Find ONLY the business's own Facebook page and Instagram profile.
  Search "<business_name>" <town> facebook, "<business_name>" instagram, the phone number in quotes, the known email
  in quotes, and the owner's name (known_owner) with the business name. Check the Facebook and Instagram links shown
  on its Yelp, Houzz, Angi, BBB, Nextdoor, Thumbtack and Birdeye pages. Copy the known email into the email columns.
- F: the Facebook/Instagram is already known. Find ONLY a published email. Open the known page and read the Intro,
  About, contact info, Page transparency, and the captions of its posts, photos, flyers and business card images.
  Then search the phone number in quotes together with "@gmail.com", "@yahoo.com", "@aol.com", "@outlook.com",
  "@hotmail.com", "@icloud.com" and "email"; search "<business_name>" email; search the owner's name with "@".
  Check BBB, Yelp, Houzz, Angi, HomeAdvisor, Thumbtack, Nextdoor, Porch, BuildZoom, Manta, Alignable, Birdeye,
  Chamber of Commerce listings, the state contractor licence lookup, the state business registry (annual reports
  often show an email), USDOT/FMCSA records, local newspapers, church bulletins, realtor "preferred vendor" pages and
  supplier "find an installer" pages. If dead_website is given, read its archived pages on the Wayback Machine.
- N: new. Do all of the above: find the Facebook page, the Instagram profile and the email, and check for a website.

WEBSITE CHECK (every row): if the business has its own website that loads and shows the business, put it in
website_found with website_status = live. If a site exists but is down, parked, "coming soon", expired or a "domain not
connected" page, write website_status = dead. Facebook, Instagram, Linktree and directory pages are NOT websites.

RULES
- Never guess or build an email from a name pattern. Only copy an email you actually saw, with the page URL
  (email_source_url) and a quote of 20 words or fewer from that page containing it (email_source_quote).
- People-search and email-finder sites (ContactOut, RocketReach, ZoomInfo, Whitepages, TruePeopleSearch,
  FastPeopleSearch and similar) do NOT count.
- Accept a page, profile or email only if it clearly belongs to THIS business (same name and the same phone, town or
  owner). If unsure, leave it out and say why in notes.
- Plain full URLs only. sources_checked: every source you opened, separated by semicolons. Keep the row numbers.
- Keep the written part of the report to a few lines. Spend your effort on research, not on writing.
- If you run out of room, finish the business you are on and end with LAST_ROW_DONE: <row number>.

OUTPUT
End with ONE CSV block (in a ```csv code block) with exactly this header:
row,business_name,facebook_url,instagram_url,email,email_source_url,email_source_quote,website_found,website_status,owner_name,facebook_followers,facebook_latest_post_date,instagram_followers,instagram_latest_post_date,photo_posts,sources_checked,notes
- One line for EVERY business in the table (also when nothing was found: then use UNKNOWN). Text containing a comma
  goes in double quotes.
- Then one line: LAST_ROW_DONE: <row number of the last business you finished>.
```

## Businesses (50, in order)
```csv
row,task,business_name,town,phone,address,google_maps,known_facebook,known_instagram,known_email,known_owner,dead_website
2083,N,Residential & Commercial Service LLC,"White Oak, PA",(724) 861-7273,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0UOg-N3nNIgR6CiVnZxHg9U&hl=en,none,none,none,none,none
2118,N,YNK Renovation LLC,"Douglasville, GA",(404) 510-6153,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJK77cBhoIaAYRjKP-y1Yn5LI&hl=en,none,none,none,none,none
2119,N,Chapel Cabinet Company,"Russellville, KY",(270) 542-4051,"8072 Morgantown Rd, Russellville, KY 42276",https://www.google.com/maps/place/?q=place_id:ChIJNfjWZeSYZYgR2o-XOV3b_CE&hl=en,none,none,none,none,none
2120,N,Kerr Cabinet Co DBA Signature Cabinetry by Kerr,"Oxford, AL",(256) 831-8270,"2009 Barry St, Oxford, AL 36203",https://www.google.com/maps/place/?q=place_id:ChIJxZLeTy6xi4gROxPCkRm-fwE&hl=en,none,none,none,none,none
2121,N,R K Morris & Company,"San Juan Capistrano, CA",(949) 248-0770,"33021 Calle Perfecto, San Juan Capistrano, CA 92675",https://www.google.com/maps/place/?q=place_id:ChIJ66cGSrnx3IARQzQHe7LxIjM&hl=en,none,none,none,none,none
2122,N,"Happy Home Remodeling, LLC","Post Falls, ID",(720) 713-3443,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJV6zawm3BYVMRmbuxYIjibv0&hl=en,none,none,none,none,none
2123,N,H&A Remodeler | Home & Kitchen Remodeling Mesa H&A,"Boise, ID",(208) 209-7860,"2067 E Toluka Wy, Boise, ID 83712",https://www.google.com/maps/place/?q=place_id:ChIJG36Nu5_5rlQRsN_8brcKvWQ&hl=en,none,none,none,none,none
2124,N,"Al Renovations,","El Monte, CA",(626) 627-7498,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJsS9nR4qlRQMRkPthpL_Vd_c&hl=en,none,none,none,none,none
2125,N,Flathead Granite Fab,"Columbia Falls, MT",(406) 897-3716,"5385 US-2, Columbia Falls, MT 59912",https://www.google.com/maps/place/?q=place_id:ChIJ03-Vd8dBZlMRv8ZXnfoy818&hl=en,none,none,none,none,none
2126,N,Contraluz Construction,"Veneta, OR",(541) 228-2860,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_6ZChFb5ESoRwJaAI_mL79E&hl=en,none,none,none,none,none
2127,N,Blissful Bathroom Remodel San Francisco,"Tiburon, CA",(415) 704-7021,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJSXgqh-F8UU0R26smioKAmXs&hl=en,none,none,none,none,none
2128,N,Supreme Stone LLC,"Romulus, MI",(734) 351-1060,"15570 S Huron River Dr, Romulus, MI 48174",https://www.google.com/maps/place/?q=place_id:ChIJj3FFh4pFO4gRU3l43VfLLOA&hl=en,none,none,none,none,none
2129,N,LL Home Renovation and Custom Design LLC.,"Mt Clemens, MI",(586) 298-2301,"560 Chippewa St, Mt Clemens, MI 48043",https://www.google.com/maps/place/?q=place_id:ChIJhbQZdY4hJYgRWTMQMIChKzs&hl=en,none,none,none,none,none
2130,N,Elite Kitchen Remodeling Northwest Suburbs,"Schaumburg, IL",(870) 408-6790,"1051 Perimeter Dr Ste 367, Schaumburg, IL 60173",https://www.google.com/maps/place/?q=place_id:ChIJG7tn9BCvD4gRalSjx-PmiaU&hl=en,none,none,none,none,none
2131,N,A & B Countertops,"Temple, GA",(770) 459-5055,"1482 US-78, Temple, GA 30179",https://www.google.com/maps/place/?q=place_id:ChIJcQWI0AHViogRYW8WL_X5Zq4&hl=en,none,none,none,none,none
2132,N,Hayes Remodeling LLC,"Milan, TN",(731) 402-1529,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJn3g7iZkXBgkRtjKohFpUsxE&hl=en,none,none,none,none,none
2133,N,Moyer Modern Construction,"Bozeman, MT",(484) 925-9120,"404 E Story St, Bozeman, MT 59715",https://www.google.com/maps/place/?q=place_id:ChIJawhq9_jVYwIRBbUibmQRDO8&hl=en,none,none,none,none,none
2134,N,C & C Home Improvements,"Nicholasville, KY",(859) 881-9257,"3460 Union Mill Rd, Nicholasville, KY 40356",https://www.google.com/maps/place/?q=place_id:ChIJby8-9UhYQogRCqeSt7pZpl0&hl=en,none,none,none,none,none
2135,N,Fletcher Decorating Inc,"Beatrice, NE",(402) 223-5204,"414 Court St, Beatrice, NE 68310",https://www.google.com/maps/place/?q=place_id:ChIJLcDSugJolocRocBTxLXV0i8&hl=en,none,none,none,none,none
2136,N,Pompano Beach Remodeling Kitchen and Bathroom Expert,"Pompano Beach, FL",(239) 205-1199,"2500 W Atlantic Blvd, Pompano Beach, FL 33069",https://www.google.com/maps/place/?q=place_id:ChIJeRAeocQD2YgRpbaVjueQOO0&hl=en,none,none,none,none,none
2137,N,"JG Kitchen, Bath and decking","Dover, DE",(302) 526-6948,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6WaU5I17x4kRRZ3FozcWcVw&hl=en,none,none,none,none,none
2138,N,Cabinet Designs Unlimited,"Camas, WA",(360) 834-4690,"1738 SE 8th Ave # A, Camas, WA 98607",https://www.google.com/maps/place/?q=place_id:ChIJU5UsGfy8lVQRoLWzzWrUzSI&hl=en,none,none,none,none,none
2139,N,Butte Cabinet & Supply,"Oroville, CA",(530) 533-8222,"1830 Grace St, Oroville, CA 95966",https://www.google.com/maps/place/?q=place_id:ChIJ89ILbsu1nIARmt4fpxXLFFM&hl=en,none,none,none,none,none
2140,N,Kansas City Cabinet Restoration | Kitchen & Bath Cabinet Refinishing & Refacing Service,"Shawnee, KS",(816) 290-7284,"12115 Johnson Dr, Shawnee, KS 66216",https://www.google.com/maps/place/?q=place_id:ChIJ781GPCLxwIcRHQAEtqVCDX4&hl=en,none,none,none,none,none
2141,N,Innovative Renovations LLC,"Slidell, LA",(985) 503-2522,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGXMXu5PnnYgRlW_G205mcGA&hl=en,none,none,none,none,none
2142,N,Alexander Construction Cabinetry,"Murray, KY",(270) 727-9326,"307 Railroad Ave, Murray, KY 42071",https://www.google.com/maps/place/?q=place_id:ChIJreWD7-rKe4gRdysMW1QOMLY&hl=en,none,none,none,none,none
2143,N,"Sutton Construction, Inc.","Troy, MI",(248) 808-0286,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxUsvSzDFJIgRRwB5Ldj2eyo&hl=en,none,none,none,none,none
2144,N,JD's Remodeling & Repair LLC,"Yuma, AZ",(928) 345-8960,"11475 S Prescott Ave, Yuma, AZ 85365",https://www.google.com/maps/place/?q=place_id:ChIJf7ThRWlh1oARAmlPUI_4BKY&hl=en,none,none,none,none,none
2145,N,K&A Remodeling Services LLC,"Apopka, FL",(407) 494-2474,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJyUcUcluf54gRaAFuC72smaU&hl=en,none,none,none,none,none
2146,N,Coldwater Building and Renovations LLC,"Milton, FL",(850) 712-1436,"5961 Rustic Ridge Circle, Milton, FL 32570",https://www.google.com/maps/place/?q=place_id:ChIJj3uRcuYwmakRj-qROS6HYy0&hl=en,none,none,none,none,none
2147,N,Austin's Dream Remodeling,"Cambridge, MD",(443) 521-3448,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0YSeQ9NLuIkRVAmtn9pTDMU&hl=en,none,none,none,none,none
2148,N,AmaDiaz Installations,serves professionalism!,(214) 632-0395,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAZ5BAOA3TIYRiPBEcFq_7QQ&hl=en,none,none,none,none,none
2149,N,The Carpenter LLC,"Duncan, OK",(580) 641-2420,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDyV-w7xlPk8RMqkPB8gI8DA&hl=en,none,none,none,none,none
2150,N,US Kitchen Bath Bathroom Remodeling Thousand Oaks,"Thousand Oaks, CA",(805) 710-8767,"23 E Avenida De Los Arboles, Thousand Oaks, CA 91362",https://www.google.com/maps/place/?q=place_id:ChIJB18HJfIv6IARbWHRRNIlVsE&hl=en,none,none,none,none,none
2151,N,Rogue Remodel,"Lafayette, OR",(503) 747-8737,"120 W 13th St, Lafayette, OR 97127",https://www.google.com/maps/place/?q=place_id:ChIJt9-YhUdHlVQRsa3PesM9MHs&hl=en,none,none,none,none,none
2152,N,Coreem Hairston & Son Remodeling & Repairs,"Bayonne, NJ",(201) 779-7954,"17 Chase Ct, Bayonne, NJ 07002",https://www.google.com/maps/place/?q=place_id:ChIJcbewUZ1RwokROkivIzyoSoQ&hl=en,none,none,none,none,none
2153,N,West GA Refinishing LLC,"Temple, GA",(404) 717-3340,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvzYPvXDViogR-u3146HWvBY&hl=en,none,none,none,none,none
2154,N,MR Remodeling,"DeSoto, TX",(469) 881-2259,"1009 Gracelane Dr, DeSoto, TX 75115",https://www.google.com/maps/place/?q=place_id:ChIJlwHtLlWTToYREudYPk8yKOI&hl=en,none,none,none,none,none
2155,N,Cabo Kitchen & Bath,"Spring Valley, NY",(845) 459-2226,"12 Jackson Ave, Spring Valley, NY 10977",https://www.google.com/maps/place/?q=place_id:ChIJA9wgJc7dwokR0x0BTK-D2H0&hl=en,none,none,none,none,none
2156,N,Project Pros Construction,"Mexico, MO",(573) 721-8717,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVxLKUIVy_4ARqPzHd_Ww7CA&hl=en,none,none,none,none,none
2157,N,"Reborn Renovation, LLC","Bristol, CT",(860) 506-5399,"77 Daisy Cir, Bristol, CT 06010",https://www.google.com/maps/place/?q=place_id:ChIJXyRyhCWx54kRp_O08S9rQt0&hl=en,none,none,none,none,none
2158,N,Additions Home Improvement LLC.,"East Hampton, CT",(959) 226-0263,"9 Wildwood Ln, East Hampton, CT 06424",https://www.google.com/maps/place/?q=place_id:ChIJNVSqAryFGyYRBco53fJ8G9A&hl=en,none,none,none,none,none
2159,N,Aaron’s painting & Remodeling,"Sealy, TX",(832) 660-4541,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhTac0NoaBWARVMopVSF0nT4&hl=en,none,none,none,none,none
2160,N,Ellett Woodworks,"Burnet, TX",(512) 755-2884,"4956, 1001 Co Rd 335, Burnet, TX 78611",https://www.google.com/maps/place/?q=place_id:ChIJa5KkecvmWoYRRT09VvnhRfY&hl=en,none,none,none,none,none
2161,N,Cabinet Designs,"Muscle Shoals, AL",(256) 381-1609,"105 Commerce St, Muscle Shoals, AL 35661",https://www.google.com/maps/place/?q=place_id:ChIJ8753Wh5PfYgRIiJo1tWL6sQ&hl=en,none,none,none,none,none
2162,N,Cruz Right Remodeling LLC,"Thornton, CO",(720) 883-8061,"Colorado Blvd &, E 115th Ave, Thornton, CO 80233",https://www.google.com/maps/place/?q=place_id:ChIJQ7iEuMMPSSYR2MFNioMwj6Q&hl=en,none,none,none,none,none
2163,N,ANDONEGUI REMODELING,"Fort Worth, TX",(817) 694-5174,"3717 May St, Fort Worth, TX 76110",https://www.google.com/maps/place/?q=place_id:ChIJv1vZccdxToYRqL5BO9NiXH4&hl=en,none,none,none,none,none
2164,N,H&A Remodeler | Home Remodeling Meridian,"Meridian, ID",(208) 784-7832,"2045 W Overland Rd, Meridian, ID 83642",https://www.google.com/maps/place/?q=place_id:ChIJD90TeMNRrlQRuvfVA4RcE3A&hl=en,none,none,none,none,none
2165,N,Jorge Builders,"Newington, CT",(959) 201-1448,"130 Waverly Dr, Newington, CT 06111",https://www.google.com/maps/place/?q=place_id:ChIJ_QvtLtyz54kRd2onnFBZoWM&hl=en,none,none,none,none,none
2166,N,Corbin Cabinetry Inc,"Philomath, OR",(541) 929-4048,"2651 Main St, Philomath, OR 97370",https://www.google.com/maps/place/?q=place_id:ChIJgZ-59HVHwFQRCE37J3ljRRQ&hl=en,none,none,none,none,none
```
