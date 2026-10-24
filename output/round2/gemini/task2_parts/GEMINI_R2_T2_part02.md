# Round 2: Gemini task 2, part 02 of 17 (100 businesses, rows 1184 to 1283)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 1283: reply in that chat "Continue with
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
1184,C,Tile Works,"Stokesdale, NC",(336) 601-9125,"7102 Lambert Lake Rd, Stokesdale, NC 27357",https://www.google.com/maps/place/?q=place_id:ChIJQXmX4Bz9UogRfffcv1colw4&hl=en,none,none,none,none
1185,C,Jaks Home Supply,"Lansdowne, PA",(610) 622-1363,"500 E Baltimore Ave E, Lansdowne, PA 19050",https://www.google.com/maps/place/?q=place_id:ChIJm6qeb1HBxokRm5g2yWlnACo&hl=en,none,none,none,none
1186,C,"Compass Bath and Remodel, LLC","West Point, UT",(801) 678-2880,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP-JvxkctuGIR9teEWLRyujs&hl=en,none,none,none,none
1187,C,EverGreen Kitchen & Bathroom Remodeling,"Danville, CA",(925) 429-9992,"495 Church St, Danville, CA 94526",https://www.google.com/maps/place/?q=place_id:ChIJC-3ErL3WzScR2k5FEPHxnFY&hl=en,none,none,none,none
1188,C,Farrell's Top Shop & Cabinets,"Athens, TN",(423) 745-5235,"931 Co Rd 172, Athens, TN 37303",https://www.google.com/maps/place/?q=place_id:ChIJnamg8_cUXogR8f5OyXw_Xnc&hl=en,none,none,none,none
1189,C,"JJ Tile Solution, LLC","Farmington, UT",(385) 389-9180,"20 S 1100 W, Farmington, UT 84025",https://www.google.com/maps/place/?q=place_id:ChIJCQcmTecBU4cRhQqhXXiSWIM&hl=en,none,none,none,none
1190,C,Pro Design,"Wellington, CO",(970) 568-7829,"8013 First St, Wellington, CO 80549",https://www.google.com/maps/place/?q=place_id:ChIJ5SzxHpjMbocRXQa_-eL16w8&hl=en,none,none,none,none
1191,C,ARTLINE KITCHEN & BATH LLC.,"Ridgefield, NJ",(201) 208-4300,"840 Banta Pl, Ridgefield, NJ 07657",https://www.google.com/maps/place/?q=place_id:ChIJ0z7ReAn3wokRCHxuBy5DI1s&hl=en,none,none,none,none
1192,C,Home Solutions Inc,"Albemarle, NC",(704) 985-1080,"1915 E Main St, Albemarle, NC 28001",https://www.google.com/maps/place/?q=place_id:ChIJ-SLrFMh8VIgRZhlzpVNFoB4&hl=en,none,none,none,none
1193,C,Tim's Custom Cabinets,"Sequim, WA",(360) 683-7648,"5231 Woodcock Rd, Sequim, WA 98382",https://www.google.com/maps/place/?q=place_id:ChIJdwlNogG_j1QRiyS8IRwLY9c&hl=en,none,none,none,none
1194,C,NJ Home Design Studio,"Teaneck, NJ",(201) 530-7467,"1372 Teaneck Rd, Teaneck, NJ 07666",https://www.google.com/maps/place/?q=place_id:ChIJu6LsZunwwokRJQ8Xx9ATCao&hl=en,none,none,none,none
1195,C,ROME RESTORATIONS LLC,"Rome, GA",(706) 622-8121,"111 S Elm St SW, Rome, GA 30165",https://www.google.com/maps/place/?q=place_id:ChIJHeM_Ux6jiogRJZAT1kYNPHw&hl=en,none,none,none,none
1196,C,Seacoast Resurfacing Inc,"Hampton, NH",(603) 997-1481,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ68Iw4M9ux4UR9fERBSt74Eg&hl=en,none,none,none,none
1197,C,THE TUB WIZARD LLC,"Parma Heights, OH",(216) 676-4535,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJmXvrwQXsMIgRKPky9wEFqC4&hl=en,none,none,none,none
1198,C,Creekside Cabinets,"Tremonton, UT",(435) 230-0955,"8769 W 10400 N, Tremonton, UT 84337",https://www.google.com/maps/place/?q=place_id:ChIJF3ZsdYaYVIcR8y_ErqrPqEM&hl=en,none,none,none,none
1199,C,Boatman Family Cabinetry,"Woodlawn, VA",(276) 733-9288,"58 Crystal Ln, Woodlawn, VA 24381",https://www.google.com/maps/place/?q=place_id:ChIJGzABe5kdUogR2Sfhc087D8c&hl=en,none,none,none,none
1200,C,Masco Builder Cabinet Group,"Duncanville, TX",(972) 298-6101,"515 Big Stone Gap Rd, Duncanville, TX 75137",https://www.google.com/maps/place/?q=place_id:ChIJeyx69t-RToYR0xgSwKR2Eeg&hl=en,none,none,none,none
1201,C,JB's Builders Surplus,"Elizabethtown, KY",(270) 735-9202,"7126 S Wilson Rd, Elizabethtown, KY 42701",https://www.google.com/maps/place/?q=place_id:ChIJnxHoj9HnaIgRF5YaAogCANc&hl=en,none,none,none,none
1202,C,Shur-Form Countertop Surfaces,"Franklin, OH",(937) 746-0567,"221 N Main St, Franklin, OH 45005",https://www.google.com/maps/place/?q=place_id:ChIJCyAEZ7thQIgRkxKqEhOfbxA&hl=en,none,none,none,none
1203,C,Stone & Cabinets,"Braintree, MA",(617) 409-9773,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-UBtJq-h5IkRXnh6DHgaJAY&hl=en,none,none,none,none
1204,C,C&H Kitchen & Bath | Cabinetry and Stones,"Norcross, GA",(678) 221-7617,"4519 S Old Peachtree Rd, Norcross, GA 30071",https://www.google.com/maps/place/?q=place_id:ChIJQaqGn0-j9YgRM5BxJIsCLKQ&hl=en,none,none,none,none
1205,C,Alaniz Custom Cabinets,"Corpus Christi, TX",(361) 403-3085,"118 Gibson Ln #3, Corpus Christi, TX 78406",https://www.google.com/maps/place/?q=place_id:ChIJT6mvumlgaIYR2spkYky0wm0&hl=en,none,none,none,none
1206,C,Kustom Granite,"Radcliff, KY",(270) 351-5551,"2511 S Dixie Blvd, Radcliff, KY 40160",https://www.google.com/maps/place/?q=place_id:ChIJF2aoTEPnaIgRm6-BQRcsfnw&hl=en,none,none,none,none
1207,C,Apex Construction & Remodeling,"Highland, IN",(219) 923-3336,"2743 Highway Ave, Highland, IN 46322",https://www.google.com/maps/place/?q=place_id:ChIJ_7dDHLXgEYgRzS3HdN9Vck8&hl=en,none,none,none,none
1208,C,Dream Kitchen & Bath,"Magnolia, TX",(832) 934-1600,"6911 FM 1488 # C, Magnolia, TX 77354",https://www.google.com/maps/place/?q=place_id:ChIJK_1SOPcvR4YRVnYxjKGc-5k&hl=en,none,none,none,none
1209,C,Express Kitchen Cabinets,"Hickory Hills, IL",(708) 859-4000,"9909 S 78th Ave, Hickory Hills, IL 60457",https://www.google.com/maps/place/?q=place_id:ChIJWbJmkbtJDogRU0ETOomtIxg&hl=en,none,none,none,none
1210,C,"Kuba-Tech Industries, Llc","White Settlement, TX",(817) 924-5520,"801 Ozona Ave, White Settlement, TX 76108",https://www.google.com/maps/place/?q=place_id:ChIJDRieZLAMToYRoKP1Ukm4PPo&hl=en,none,none,none,none
1211,C,Matrix Bathroom Systems,"Denver, CO",(303) 222-9729,"501 S Cherry St Ste 1100, Denver, CO 80246",https://www.google.com/maps/place/?q=place_id:ChIJ8d24heV_bIcRylxhP3M1X_k&hl=en,none,none,none,none
1212,C,Decora Design Cabinets Stone,"Brandon, FL",(813) 324-9732,"742 W Brandon Blvd, Brandon, FL 33511",https://www.google.com/maps/place/?q=place_id:ChIJmZBwzlLNwogRVhmpRCvjJLw&hl=en,none,none,none,none
1213,C,Specialty Woodworks Inc.,"Van Buren, AR",(479) 474-4522,"3700 Kibler Rd, Van Buren, AR 72956",https://www.google.com/maps/place/?q=place_id:ChIJkz1t3oK2y4cRYrcI2rLbDgI&hl=en,none,none,none,none
1214,C,Unlimited Cabinets and Doors,"Longview, TX",(903) 297-0829,"114 Stevens St, Longview, TX 75604",https://www.google.com/maps/place/?q=place_id:ChIJ6eR7tNg7NoYRI_rpus4Wwg0&hl=en,none,none,none,none
1215,C,DC Kitchen & Bath,"Westbury, NY",(516) 280-7988,"896 Old Country Rd, Westbury, NY 11590",https://www.google.com/maps/place/?q=place_id:ChIJmVhyF0qHwokRc3zcruhDbbk&hl=en,none,none,none,none
1216,C,Skyward Cabinetry and Construction LLC,"Yukon, OK",(405) 245-5737,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJi20bCfgJsocR9FB7W5-qsmM&hl=en,none,none,none,none
1217,C,Pimentel Kitchen and Bath,"Hialeah, FL",(786) 806-1904,"715 W 27th St, Hialeah, FL 33010",https://www.google.com/maps/place/?q=place_id:ChIJjYre_OW72YgR9yPlC18fqEE&hl=en,none,none,none,none
1218,C,All About Kitchens,"Modesto, CA",(209) 521-4490,"531 Kansas Ave Unit D, Modesto, CA 95351",https://www.google.com/maps/place/?q=place_id:ChIJ-8F8LfFTkIARkf-LKu9U5R0&hl=en,none,none,none,none
1219,C,Uxbridge Cabinet Center,"Uxbridge, MA",(508) 278-6551,"706 Quaker Hwy, Uxbridge, MA 01569",https://www.google.com/maps/place/?q=place_id:ChIJxwpifPsU5IkRoPvln3VuUUA&hl=en,none,none,none,none
1220,C,Custom Carpentry,"Grand Haven, MI",(616) 502-0506,"12596 Lakeshore Ave, Grand Haven, MI 49417",https://www.google.com/maps/place/?q=place_id:ChIJoUB9C7CHGYgRQFZ2RBRPX_o&hl=en,none,none,none,none
1221,C,Bolon's Custom Kitchens and Baths,"North Canton, OH",(330) 499-0092,"6287 Promler Ave NW, North Canton, OH 44720",https://www.google.com/maps/place/?q=place_id:ChIJab5HUK3WNogR14QZVyWKvCQ&hl=en,none,none,none,none
1222,C,KM Kitchen and Bath,"New Hyde Park, NY",(516) 739-5555,"2374 Jericho Tpke, New Hyde Park, NY 11040",https://www.google.com/maps/place/?q=place_id:ChIJLSxucz9jwokR7Aap6IPvpEE&hl=en,none,none,none,none
1223,C,Thompson Cabinet Refacing and Countertops,"Flint, MI",(810) 701-4239,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJYZlKMtuBI4gRgFrcB1lgwcs&hl=en,none,none,none,none
1224,C,Reliable Renovation,"Corona, CA",(866) 278-6886,"3075 Palisades Dr, Corona, CA 92880",https://www.google.com/maps/place/?q=place_id:ChIJXU0YCtvI3IARj1zBVOriHmA&hl=en,none,none,none,none
1225,C,Midwest Top Shop,"Fort Dodge, IA",(515) 955-5337,"115 S 21st St, Fort Dodge, IA 50501",https://www.google.com/maps/place/?q=place_id:ChIJ5csP1Wd28ocRzp-jz8_JGd4&hl=en,none,none,none,none
1226,C,Bathtub Wizard,"Jermyn, PA",(570) 332-8922,"31 Valley View Estates, Jermyn, PA 18433",https://www.google.com/maps/place/?q=place_id:ChIJH4UNz3obxYkRLId4cly9GrQ&hl=en,none,none,none,none
1227,C,GS Custom Remodelers LLC,"Manassas, VA",(703) 656-5244,"Manassas, VA 20108",https://www.google.com/maps/place/?q=place_id:ChIJ6UtWBxFbtokRFPWV8IAxW34&hl=en,none,none,none,none
1228,C,A Step Above Kitchen & Bath Design,"Herrin, IL",(618) 942-2000,"3108 S Park Ave, Herrin, IL 62948",https://www.google.com/maps/place/?q=place_id:ChIJbdRr7Xw8d4gREZLz-NUePhY&hl=en,none,none,none,none
1229,C,A&J Kitchen Design LLC,"East Lansdowne, PA",(610) 626-7386,"806 E Baltimore Ave, East Lansdowne, PA 19050",https://www.google.com/maps/place/?q=place_id:ChIJy93X6NDBxokR2edZFOu43F4&hl=en,none,none,none,none
1230,C,Sablotny Cabinetry and Design,"Springfield, IL",(217) 370-1496,"3304 Cockrell Ln, Springfield, IL 62711",https://www.google.com/maps/place/?q=place_id:ChIJo7x3c1ZHdYgR5pvcRPjuXSA&hl=en,none,none,none,none
1231,C,Quality Renovation LLC,"Smithfield, RI",(401) 480-0110,"2 Farnum Pike, Smithfield, RI 02917",https://www.google.com/maps/place/?q=place_id:ChIJQWMQtcdG5IkRH9AJgIVNEME&hl=en,none,none,none,none
1232,C,WQX Kitchen and Bath,"Covington, LA",(985) 302-5083,"70 Park Pl b, Covington, LA 70433",https://www.google.com/maps/place/?q=place_id:ChIJzfq_JKVdJ4YRPxsUc-Ztv1U&hl=en,none,none,none,none
1233,C,PWG's One Stop Shop Home Improvement Store,"LaGrange, GA",(678) 997-8144,"1618 Hamilton Rd, LaGrange, GA 30240",https://www.google.com/maps/place/?q=place_id:ChIJLx4vXHBWi4gR0XfpFVUt73M&hl=en,none,none,none,none
1234,C,Bath and kitchen remodeling I All New Remodeling,"Jacksonville, FL",(904) 226-7611,"13048 Gran Bay Pkwy, Jacksonville, FL 32258",https://www.google.com/maps/place/?q=place_id:ChIJCQ-lal7N5YgRn8WL5k87b3c&hl=en,none,none,none,none
1235,C,Mountain City Cabinets,"Frostburg, MD",(301) 689-5070,"18513 Martin Run Rd SW, Frostburg, MD 21532",https://www.google.com/maps/place/?q=place_id:ChIJnVXVhcyQyokRjqdAff2by1M&hl=en,none,none,none,none
1236,C,Premier Bathroom Remodeling,"Gainesville, GA",(678) 203-8350,"8835 Forest Path Dr, Gainesville, GA 30506",https://www.google.com/maps/place/?q=place_id:ChIJKwaUlVOX9YgRgajdaEJiIB4&hl=en,none,none,none,none
1237,C,Elegant Granite & Cabinets,"Gonzales, LA",(985) 318-2009,"311 S Burnside Ave, Gonzales, LA 70737",https://www.google.com/maps/place/?q=place_id:ChIJzdGYBXy1JoYR_JqC4ZyLM98&hl=en,none,none,none,none
1238,C,Options In Granite,"Collegeville, PA",(484) 902-8713,"134 2nd Ave, Collegeville, PA 19426",https://www.google.com/maps/place/?q=place_id:ChIJz_nMQLmQxokRsB5jdDRTNVA&hl=en,none,none,none,none
1239,C,Futura Custom Kitchen,"Warren, MI",(586) 576-7524,"2929 John B Ave, Warren, MI 48091",https://www.google.com/maps/place/?q=place_id:ChIJBb8RWqXRJIgRNwvjRB608Hc&hl=en,none,none,none,none
1240,C,Florida Cabinets Of Stuart,"Stuart, FL",(772) 324-8277,"257 SE Monterey Rd, Stuart, FL 34994",https://www.google.com/maps/place/?q=place_id:ChIJX9oiPBfd3ogRy-0XAqykrqU&hl=en,none,none,none,none
1241,C,Davis Interior Surfaces,"Tahlequah, OK",(918) 456-3500,"13813 US-62, Tahlequah, OK 74464",https://www.google.com/maps/place/?q=place_id:ChIJGcvGm_3_yYcR92Ord4iIe3Q&hl=en,none,none,none,none
1242,C,Cabinet Mania,"Munster, IN",(800) 531-8720,"822 Ridge Rd, Munster, IN 46321",https://www.google.com/maps/place/?q=place_id:ChIJX7QjumXgEYgRXyUjozqXuUA&hl=en,none,none,none,none
1243,C,Modern Cabinet & Construction,"Altoona, PA",(814) 942-1000,"110 Frankstown Rd, Altoona, PA 16602",https://www.google.com/maps/place/?q=place_id:ChIJm00VJGyRy4kRAsjj95Ypqtw&hl=en,none,none,none,none
1244,C,Conrads Cabinets & Doors,"Longview, TX",(903) 234-8348,"812 McKesson Dr, Longview, TX 75604",https://www.google.com/maps/place/?q=place_id:ChIJERroB5hHNoYRN76rOmrmnZo&hl=en,none,none,none,none
1245,C,Dynamic Cabinetry & Design,"Hewlett, NY",(516) 792-5855,"1195 Railroad Ave, Hewlett, NY 11557",https://www.google.com/maps/place/?q=place_id:ChIJQzRyncBlwokRgbH3v9c9M_E&hl=en,none,none,none,none
1246,C,Todd's Cabinets,"Mapleton, UT",(801) 489-0590,"50 S 1600 W, Mapleton, UT 84664",https://www.google.com/maps/place/?q=place_id:ChIJd6uuJku8TYcRtuJot_gkjo0&hl=en,none,none,none,none
1247,C,William Olsen Designs,"Phoenix, OR",(541) 326-1652,"216 Houston Rd, Phoenix, OR 97535",https://www.google.com/maps/place/?q=place_id:ChIJS83TeXp3z1QR_9eD07R6wss&hl=en,none,none,none,none
1248,C,Tri-Tex Cabinets - work,"Pilot Point, TX",(940) 686-2617,"900 US-377, Pilot Point, TX 76258",https://www.google.com/maps/place/?q=place_id:ChIJmxKkxcFPTIYRp5ItyYaJ9Po&hl=en,none,none,none,none
1249,C,RDB Bathroom Remodel,"Huron, SD",(206) 456-3329,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMUcIp44xJ4gRcY8C8pZAwro&hl=en,none,none,none,none
1250,C,Cabinets Kitchens,"Covington, GA",(770) 787-7211,"7187 Washington St SW, Covington, GA 30014",https://www.google.com/maps/place/?q=place_id:ChIJTY_D9EQ09IgR-ieanX9BXHM&hl=en,none,none,none,none
1251,C,Brandom Manufacturing of Texas,"Hillsboro, TX",(254) 580-1200,"404 Hawkins St, Hillsboro, TX 76645",https://www.google.com/maps/place/?q=place_id:ChIJpyUHYFioT4YRsHO-X6ouT0s&hl=en,none,none,none,none
1252,C,Home Remodel Boutique,"Edison, NJ",(732) 543-2022,"400 US-1, Edison, NJ 08817",https://www.google.com/maps/place/?q=place_id:ChIJ230SWHbJw4kRKfxLsFNVEnY&hl=en,none,none,none,none
1253,C,Tom's Cabinetry,"New Baltimore, MI",(586) 749-5700,"53377 Gratiot Ave, New Baltimore, MI 48051",https://www.google.com/maps/place/?q=place_id:ChIJq5IkWjMZJYgRXasN6zTubE4&hl=en,none,none,none,none
1254,C,"Meeder Design & Remodeling, Inc","Oak Brook, IL",(630) 709-3800,"1301 W 22nd St, Oak Brook, IL 60523",https://www.google.com/maps/place/?q=place_id:ChIJof3x3axMDogR9SFYWhaZroc&hl=en,none,none,none,none
1255,C,Q&P Woodcraft,"Seminole, TX",(432) 201-0182,"606 SE 4th St, Seminole, TX 79360",https://www.google.com/maps/place/?q=place_id:ChIJbS50Z-5n_IYR4_bD9wRLadA&hl=en,none,none,none,none
1256,C,Bath Planet of SW Florida,"Fort Myers, FL",(239) 427-0541,"11350 Metro Pkwy #104, Fort Myers, FL 33966",https://www.google.com/maps/place/?q=place_id:ChIJcywn-04V24gRjLH1lMAUrMo&hl=en,none,none,none,none
1257,C,"Easy Bath Solutions, LLC","Hatboro, PA",(267) 456-7300,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ1VdbvnKvxokRj4FhZrmn7xI&hl=en,none,none,none,none
1258,C,Acosta & Sons Inc,"Oakdale, CA",(209) 322-3181,"736 Wakefield Ct, Oakdale, CA 95361",https://www.google.com/maps/place/?q=place_id:ChIJvzsoHIoCkYARix_5qdJqIA4&hl=en,none,none,none,none
1259,C,Frederickson Flooring and Bath Renovations,"Miamisburg, OH",(937) 245-2579,"26 N Main St, Miamisburg, OH 45342",https://www.google.com/maps/place/?q=place_id:ChIJJ5KEd_pjQIgRUS87RKsW2OA&hl=en,none,none,none,none
1260,C,"Gulf Coast Cabinetry, LLC","Ponchatoula, LA",(985) 956-7097,"18228 S I-12 Service Rd, Ponchatoula, LA 70454",https://www.google.com/maps/place/?q=place_id:ChIJ9cZUcEchJ4YREU2kvqIdl3g&hl=en,none,none,none,none
1261,C,Danny's Top Shop,"Festus, MO",(636) 931-6606,"793 American Legion Dr, Festus, MO 63028",https://www.google.com/maps/place/?q=place_id:ChIJeyfhYOru2IcR7NvUvk-a3aU&hl=en,none,none,none,none
1262,C,Ric's Kitchen & Bath Showroom,"Castro Valley, CA",(510) 733-5543,"3664 Castro Valley Blvd, Castro Valley, CA 94546",https://www.google.com/maps/place/?q=place_id:ChIJU73eMTCSj4ARciFdKe_3Nlk&hl=en,none,none,none,none
1263,C,Luxe Haus Kitchen & Bath Remodeling,"Fort Worth, TX",(939) 633-2833,"640 Taylor St Suite 1200, Fort Worth, TX 76102",https://www.google.com/maps/place/?q=place_id:ChIJ969TWCFxToYRzQ0RD1RPt-c&hl=en,none,none,none,none
1264,C,Nordhouse Remodeling & Renovation,"Normandy Park, WA",(916) 275-0039,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJjxllcOqujAcR-C_4EwwRNoQ&hl=en,none,none,none,none
1265,C,"Alpha Stone, LLC","Swannanoa, NC",(828) 777-1965,"2576 US-70, Swannanoa, NC 28778",https://www.google.com/maps/place/?q=place_id:ChIJ1RcyxhaMWYgRkNGLXZVPkjY&hl=en,none,none,none,none
1266,C,Gordy's Custom Cabinets,"East Bethel, MN",(763) 434-7071,"1861 Viking Blvd NE, East Bethel, MN 55011",https://www.google.com/maps/place/?q=place_id:ChIJ6WqoA1IZs1IRbAWPibeAX0w&hl=en,none,none,none,none
1267,C,KM Construction & Remodeling,"Lock Haven, PA",(570) 660-9303,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJsaO36zrt-UYRWnzaUQHMQjY&hl=en,none,none,none,none
1268,C,Brothers Flooring,"Pocahontas, AR",(870) 892-2525,"1805 Old County Rd, Pocahontas, AR 72455",https://www.google.com/maps/place/?q=place_id:ChIJoVC5EKfA1ocRptqMOAbIYlc&hl=en,none,none,none,none
1269,C,Her Renovations llc,"East Cleveland, OH",(216) 815-2626,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhyx-lyC5YqcRY8y3ie1xK8g&hl=en,none,none,none,none
1270,C,Kitchen & Bath Inspirations,"Clinton, IA",(563) 241-1918,"1845 Manufacturing Dr # C, Clinton, IA 52732",https://www.google.com/maps/place/?q=place_id:ChIJ-6K4U69m4ocRa75dT5KnHyA&hl=en,none,none,none,none
1271,C,Remodeling Expo,"Downers Grove, IL",(630) 724-9000,"412 75th St, Downers Grove, IL 60516",https://www.google.com/maps/place/?q=place_id:ChIJkSJDy_NPDogRZpU_6pkqUGg&hl=en,none,none,none,none
1272,C,Qualified Home Solutions LLC,"Barnesville, GA",(678) 572-4459,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ98ChK_mP9IgRAAUERCzitvY&hl=en,none,none,none,none
1273,C,MGB remodeling LLC,"Independence, KY",(859) 446-3934,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvXLCBI_HQYgRpU5HQ10nFmg&hl=en,none,none,none,none
1274,C,Heart of the Home Design-Build,"Winchester, VA",(540) 877-0429,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJrxjopsPutYkRgpDHeVs1oXA&hl=en,none,none,none,none
1275,C,A&S Home Remodeling LLC,"Kissimmee, FL",(954) 701-2546,"4751 Luminous Loop, Kissimmee, FL 34746",https://www.google.com/maps/place/?q=place_id:ChIJV9DPvHep2YgRaGsz1fW0C1Y&hl=en,none,none,none,none
1276,C,Orchard Home Designs,"Hickory Creek, TX",(469) 247-7758,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMfHTKfa4R4gRTBHeYvOTAN0&hl=en,none,none,none,none
1277,C,Kujos Custom LLC,"Sealy, TX",(832) 788-0019,"1789 Lezak Rd, Sealy, TX 77474",https://www.google.com/maps/place/?q=place_id:ChIJcxoBz8g4QYYRqI3YC_ms0dE&hl=en,none,none,none,none
1278,C,The Ramsay Group INC,"Naples, FL",(239) 778-5570,"3437 Westview Dr, Naples, FL 34104",https://www.google.com/maps/place/?q=place_id:ChIJBWKnRGbj2ogRt0d6owwWJXg&hl=en,none,none,none,none
1279,C,Tussey Mountain Custom Kitchen,"Meadville, PA",(814) 337-6733,"1061 Park Ave, Meadville, PA 16335",https://www.google.com/maps/place/?q=place_id:ChIJi68ZYA1XMogR-NP4jofaH7o&hl=en,none,none,none,none
1280,C,Wentzell Cabinet Shop Inc,"Birmingham, AL",(205) 836-5999,"2804 Woodwork Way, Birmingham, AL 35210",https://www.google.com/maps/place/?q=place_id:ChIJazC6VIwNiYgRry5Qs9l48wo&hl=en,none,none,none,none
1281,C,Martinez Complete Remodeling Services LLC,"DeBary, FL",(315) 992-3667,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJha7ler2OVYERblbd9kfENvg&hl=en,none,none,none,none
1282,C,Corner Cabinet,"Neosho, MO",(417) 451-2363,"12628 State Hwy 86, Neosho, MO 64850",https://www.google.com/maps/place/?q=place_id:ChIJo0TaAA1gyIcRIfL6j7svuzA&hl=en,none,none,none,none
1283,C,GP RemodelingServices,"Kyle, TX",(512) 756-3469,"181 Maroon Ln, Kyle, TX 78640",https://www.google.com/maps/place/?q=place_id:ChIJ6z2da-JTW4YRx6c9fvopoYw&hl=en,none,none,none,none
```
