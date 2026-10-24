# Round 2: Gemini task 2, part 04 of 17 (100 businesses, rows 1384 to 1483)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 1483: reply in that chat "Continue with
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
1384,C,Oshkosh Kitchen Remodeler,"Oshkosh, WI",(920) 605-8180,"837 N Main St, Oshkosh, WI 54901",https://www.google.com/maps/place/?q=place_id:ChIJB0ZKfNTjA4gRU2WE2EXIoJc&hl=en,none,none,none,none
1385,C,Shady Grove Cabinet Shop,"Greencastle, PA",(717) 597-7855,"3030 Buchanan Trail E, Greencastle, PA 17225",https://www.google.com/maps/place/?q=place_id:ChIJAzzPO9eQyYkRp5dEPjvYPnc&hl=en,none,none,none,none
1386,C,Prestige Kitchen and Bath,"Pasadena, CA",(626) 460-8660,"241 S Rosemead Blvd Unit a, Pasadena, CA 91107",https://www.google.com/maps/place/?q=place_id:ChIJc-u4Z3rbwoARBtQYOOrvN9Q&hl=en,none,none,none,none
1387,C,Prestige Tile Remodeling,"Savannah, TX",(469) 237-4866,"1817 Mercer Way, Savannah, TX 76227",https://www.google.com/maps/place/?q=place_id:ChIJufZr4Eg5TIYRmAmmv7WpY9g&hl=en,none,none,none,none
1388,C,Kyra Homes Kitchen & Bath Remodeling,"Spring, TX",(832) 798-6641,"19523 Enchanted Oaks Dr, Spring, TX 77388",https://www.google.com/maps/place/?q=place_id:ChIJo4TcYdQ0R4YR_b0yyEDYpt8&hl=en,none,none,none,none
1389,C,Garibay Flooring Co,"Brenham, TX",(281) 640-4906,"2406 S Chappell Hill St, Brenham, TX 77833",https://www.google.com/maps/place/?q=place_id:ChIJ3Tlzg0WpRoYRod7ezAVAN3U&hl=en,none,none,none,none
1390,C,Clinton Floor & Cabinet Shop,"Clinton, TN",(865) 457-9255,"442 N Main St, Clinton, TN 37716",https://www.google.com/maps/place/?q=place_id:ChIJuSJVnMU3XIgRDOnC3f1HRiw&hl=en,none,none,none,none
1391,C,House of Kitchens Ltd,"Sioux City, IA",(712) 255-2552,"308 S Floyd Blvd, Sioux City, IA 51101",https://www.google.com/maps/place/?q=place_id:ChIJ19V9tp39jYcRWzLQ31nc0XM&hl=en,none,none,none,none
1392,C,Big John's Remodeling Inc,"Sappington, MO",(314) 830-6401,"9901 Watson Rd Ste 139, Sappington, MO 63126",https://www.google.com/maps/place/?q=place_id:ChIJKcRm_-o334cRvv44paRCg7s&hl=en,none,none,none,none
1393,C,Torres kitchen designs & cabinets,"Hallandale Beach, FL",(786) 492-9090,"229 NW 8th Ave Apt 102, Hallandale Beach, FL 33009",https://www.google.com/maps/place/?q=place_id:ChIJLYVQZNCt2YgRwg3od20U9cs&hl=en,none,none,none,none
1394,C,BathTastic,"Flat Rock, MI",(734) 778-5653,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJly1kwk4_O4gR5o7CNWAQ_Jw&hl=en,none,none,none,none
1395,C,My Honest Builder Inc | Kitchen & Bathroom Remodeling,"Citrus Heights, CA",(916) 917-9122,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJwbf-wpLyT6kRRxVUu1_X_GM&hl=en,none,none,none,none
1396,C,The Best Kitchen & Bath Design,"Floral Park, NY",(516) 488-2111,"235 Jericho Tpke, Floral Park, NY 11001",https://www.google.com/maps/place/?q=place_id:ChIJpQ2OlNpjwokRpozwmY9LMj4&hl=en,none,none,none,none
1397,C,Best kitchen Bath Renovation Santa Fe Springs,"Santa Fe Springs, CA",(562) 222-5136,"11718 Burke St, Santa Fe Springs, CA 90670",https://www.google.com/maps/place/?q=place_id:ChIJz-bqikzSwoARwuyQkMFmgmE&hl=en,none,none,none,none
1398,C,Precision Custom Cabinets LLC,"Heyburn, ID",(208) 650-0366,"1610 US-30, Heyburn, ID 83336",https://www.google.com/maps/place/?q=place_id:ChIJaUyaiFc3q1QRh32sLmHNljc&hl=en,none,none,none,none
1399,C,Reddick Marble & Granite.,"Brookland, AR",(870) 932-2551,"12221 US 49 S, Brookland, AR 72417",https://www.google.com/maps/place/?q=place_id:ChIJhVhxcfh-1ocRC_6QThNlFiA&hl=en,none,none,none,none
1400,C,"Shoals Kitchen and Bath, LLC","Tuscumbia, AL",(256) 577-6144,"202 W 3rd St, Tuscumbia, AL 35674",https://www.google.com/maps/place/?q=place_id:ChIJXSjfc9lFfYgRe3nbfdsajaQ&hl=en,none,none,none,none
1401,C,EZ Kitchen Design,"Palm Coast, FL",(386) 603-3111,"4984 Palm Coast Pkwy NW, Palm Coast, FL 32137",https://www.google.com/maps/place/?q=place_id:ChIJASgsMYeT5ogRj824CkGhyVk&hl=en,none,none,none,none
1402,C,West Chester Bathroom Remodeling,"West Chester, PA",(484) 319-7135,"300 Willowbrook Ln Suite 310, West Chester, PA 19382",https://www.google.com/maps/place/?q=place_id:ChIJJUqOFlp2CG4RqIIhgkSDjRQ&hl=en,none,none,none,none
1403,C,Wright brothers remodeling LLC.,"Cache, OK",(580) 704-6058,"801 N 5th St, Cache, OK 73527",https://www.google.com/maps/place/?q=place_id:ChIJpdRoVtnnrIcR7milUvAlvgw&hl=en,none,none,none,none
1404,C,MACCS FLOOR COVERING LLC,"Fairview, OR",(971) 804-3469,"320 Lincoln St Apt 203, Fairview, OR 97024",https://www.google.com/maps/place/?q=place_id:ChIJKxAJfSejlVQR51bT6dVFFGw&hl=en,none,none,none,none
1405,C,CRUSH IT Renovations LLC,"South Pasadena, FL",(727) 490-9451,"email. crushitrenovate@gmail.com, 7882 Sailboat Key Blvd S, South Pasadena, FL 33707",https://www.google.com/maps/place/?q=place_id:ChIJIcX5Ijj9wogR1SFH2eMXMmU&hl=en,none,none,none,none
1406,C,Norton Remodeling & Home Improvement,"Maryville, TN",(865) 340-9456,"214 John Helton Rd, Maryville, TN 37804",https://www.google.com/maps/place/?q=place_id:ChIJowPCjSoeXIgRHEeq0PRIsO8&hl=en,none,none,none,none
1407,C,LCN Kitchen And Bath,"Windsor, CT",(860) 683-8521,"1695 Poquonock Ave, Windsor, CT 06095",https://www.google.com/maps/place/?q=place_id:ChIJk3OIJkT-5okRDEQ9wvGgz8k&hl=en,none,none,none,none
1408,C,Custom showers & Flooring,"Mandeville, LA",(985) 224-5022,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJH9509Z5ZJ4YRFUY9hStXLa4&hl=en,none,none,none,none
1409,C,The Interior,"Walla Walla, WA",(509) 525-1588,"15 S Spokane St, Walla Walla, WA 99362",https://www.google.com/maps/place/?q=place_id:ChIJYceCh2JqolQRdzTbEh5P5pk&hl=en,none,none,none,none
1410,C,Northridge Kitchen Remodeling,"Northridge, CA",(818) 918-2110,"18771 Labrador St, Northridge, CA 91324",https://www.google.com/maps/place/?q=place_id:ChIJfwWVjLObwoARmq5DpXG5pPA&hl=en,none,none,none,none
1411,C,AH RESTORATION LLC,"Struthers, OH",(330) 957-9739,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJq55QnbzxM4gRPg5ksJ3keto&hl=en,none,none,none,none
1412,C,Jimenez Tile and Bath LLC,"East Chicago, IN",(219) 654-3890,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJH5YowsfDEYgRa_q8Q7gUVCc&hl=en,none,none,none,none
1413,C,Route 80 Lumber & Millwork,"North Branford, CT",(203) 483-9800,"2296 Foxon Rd, North Branford, CT 06471",https://www.google.com/maps/place/?q=place_id:ChIJwXNwfQvT54kRfYrp6kJVSW4&hl=en,none,none,none,none
1414,C,Best Miami Home Remodeling,"North Miami, FL",(305) 317-6370,"1820 NE 146th St, North Miami, FL 33181",https://www.google.com/maps/place/?q=place_id:ChIJuba_M-it2YgRbz79SZBRNSM&hl=en,none,none,none,none
1415,C,Lowken Renovations LLC,"Bakersfield, CA",(661) 328-0477,"3154 Landco Dr D, Bakersfield, CA 93308",https://www.google.com/maps/place/?q=place_id:ChIJTWG2a6BD6oARRhfM2TAhapw&hl=en,none,none,none,none
1416,C,EP Custom Renovations,"Oakland Park, FL",(954) 501-5603,"822 NE 40th Ct, Oakland Park, FL 33334",https://www.google.com/maps/place/?q=place_id:ChIJJ1Qp-0p7w2URtniWGbrFClc&hl=en,none,none,none,none
1417,C,Tommy Slade Construction and Remodeling,"Prattville, AL",(334) 819-6146,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJD89SIStG8EYRafVd1sLFRZM&hl=en,none,none,none,none
1418,C,J&A Custom Tile and Stone,"Pineville, LA",(318) 446-5711,"420 Garnet St, Pineville, LA 71360",https://www.google.com/maps/place/?q=place_id:ChIJO48ly3KzOoYR8gjhNe2BHFg&hl=en,none,none,none,none
1419,C,"Kitchen remodeler in Mercer Island, WA | New Era Construction",serves the best. We specialize in creating highly functional,(253) 402-7311,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbaOmVQJYzC4RgNqZUqjjzeI&hl=en,none,none,none,none
1420,C,Milestone Kitchen & Bath Inc,"Laguna Hills, CA",(949) 590-9999,"25381 Alicia Pkwy Ste i, Laguna Hills, CA 92653",https://www.google.com/maps/place/?q=place_id:ChIJ9buUq3vp3IARk2XuLi7ijp8&hl=en,none,none,none,none
1421,C,HSP Bathroom Remodel,"Auburn, WA",(253) 600-4140,"511 M St NE unit 206, Auburn, WA 98002",https://www.google.com/maps/place/?q=place_id:ChIJS61CdVpZkFQRacMN07bsukM&hl=en,none,none,none,none
1422,C,Shepherds Construction LLC,"Amherst, OH",(419) 631-2836,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ36BMzearCIURwHLiGF9bwKE&hl=en,none,none,none,none
1423,C,Crossover Renovation & Remodeling LLC,"Westminster, CO",(303) 513-5156,"10041 Lewis St, Westminster, CO 80021",https://www.google.com/maps/place/?q=place_id:ChIJXyB10Jl87UAR8MDr-TkL2vM&hl=en,none,none,none,none
1424,C,Edg Solutions,"Lyndon, KY",(502) 767-5413,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJR5k2ZQh1aYgRRDmMDdJZoo8&hl=en,none,none,none,none
1425,C,Verser's Cabinet Shop LLC,"Rogers, AR",(479) 636-3941,"2351 W Hudson Rd, Rogers, AR 72756",https://www.google.com/maps/place/?q=place_id:ChIJ8yTcKq0QyYcRdWB2-AmPOak&hl=en,none,none,none,none
1426,C,Brown's Renovations and Home Improvements,"Flint, MI",(810) 293-5042,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgY5X8bsUyGYRefc75rKP57A&hl=en,none,none,none,none
1427,C,Adagio Kitchen and Bath,"Northbrook, IL",(847) 480-6300,"3394 Commercial Ave, Northbrook, IL 60062",https://www.google.com/maps/place/?q=place_id:ChIJEdHVkVC_D4gR2583u2CyY78&hl=en,none,none,none,none
1428,C,Muse Bath,"Webster Groves, MO",(314) 408-2708,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ92N9VgOnWysR5RsEogg-eKM&hl=en,none,none,none,none
1429,C,Home improvement Vis & Ink,"Dunedin, FL",(727) 687-1356,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZd6dgLOvLygRyg4ot36hylY&hl=en,none,none,none,none
1430,C,Colorado Renovations Plus,"Gunnison, CO",(970) 281-5570,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0_BkHB1pGS4R_45hRmGHPOE&hl=en,none,none,none,none
1431,C,MDS Project Management,"Indian Harbour Beach, FL",(678) 308-4708,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOX5FgDwR3ogRgJf31qa7BQk&hl=en,none,none,none,none
1432,C,"Eastern Renovation Group, LLC","Fayetteville, NC",(702) 817-1177,"6529 Jacobs Creek Cir, Fayetteville, NC 28306",https://www.google.com/maps/place/?q=place_id:ChIJ2e7boxAVq4kRuAJFBKUte8U&hl=en,none,none,none,none
1433,C,MaxPro Renovations Inc,"Pineville, NC",(916) 595-9778,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJd-l68o851kwR0hZxexfPgFc&hl=en,none,none,none,none
1434,C,MANNY AND BROTHERS TILE INC,"West New York, NJ",(201) 926-4820,"325 53rd St, West New York, NJ 07093",https://www.google.com/maps/place/?q=place_id:ChIJQaVsxSFZwokRKm3cSVxcqR8&hl=en,none,none,none,none
1435,C,Tropical House Transformations LLC,"Safety Harbor, FL",(727) 565-6385,"2463 Philippe Pkwy, Safety Harbor, FL 34695",https://www.google.com/maps/place/?q=place_id:ChIJTbU0l0gpNwARJB08Wru5BwE&hl=en,none,none,none,none
1436,C,JB Home Remodeling,"Manassas, VA",(703) 717-8315,"7831 Manassas Dr, Manassas, VA 20111",https://www.google.com/maps/place/?q=place_id:ChIJ__-qG5pctokRyaHF2U8LTO4&hl=en,none,none,none,none
1437,C,"Edgewater Refinishing, LLC","Edgewater, FL",(386) 478-8890,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJH1QaP5Mv54gRwMiHP-PBuG4&hl=en,none,none,none,none
1438,C,Flores Cabinet Makers,"South Houston, TX",(713) 944-0815,"1315 Illinois St, South Houston, TX 77587",https://www.google.com/maps/place/?q=place_id:ChIJHxiWYZaXQIYRC5F_gRL2ctg&hl=en,none,none,none,none
1439,C,Align Cabinets and Doors,"City of Atwater, CA",(209) 357-2159,"490 Airpark Rd, City of Atwater, CA 95301",https://www.google.com/maps/place/?q=place_id:ChIJl-MXlpBrkYARf6-7lI7b6uw&hl=en,none,none,none,none
1440,C,Custom Granite Quartz Marble Kitchen Countertops,"South Holland, IL",(847) 702-2598,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJN4JbhqQfDogRy_ffyPGy6-w&hl=en,none,none,none,none
1441,C,Tile & Decor Inc,"Mission, TX",(956) 580-7442,"4006 N Conway Ave, Mission, TX 78573",https://www.google.com/maps/place/?q=place_id:ChIJw1WtV6OoZYYRXEfi9U29KRk&hl=en,none,none,none,none
1442,C,Luxury Modern Baths & Kitchens,"Naugatuck, CT",(203) 617-5239,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJs6Darm3q_28RaEDtenaIjFE&hl=en,none,none,none,none
1443,C,Aryeh's Home Improvements,"Morrisville, NC",(984) 286-4371,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvQ1v4YIKYyQRU8gyRfAkLN8&hl=en,none,none,none,none
1444,C,MK Stones and Cabinets,"Wellington, FL",(561) 452-3551,"3132 Fortune Way d9, Wellington, FL 33414",https://www.google.com/maps/place/?q=place_id:ChIJ5wTmbPwl2YgRs_AR-_7-KHY&hl=en,none,none,none,none
1445,C,JN Granite,"Carthage, MO",(417) 358-4800,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJa7LpA9iFyIcRA_k4sDStl3M&hl=en,none,none,none,none
1446,C,Dad's Tile and More,"Wolfforth, TX",(806) 544-3610,"718 Indiana St, Wolfforth, TX 79382",https://www.google.com/maps/place/?q=place_id:ChIJ_zM5kBlt_oYRHanOVQxiDRE&hl=en,none,none,none,none
1447,C,H&I kitchen/bathroom remodeling Llc,"Selma, NC",(919) 740-2104,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpdJ_hLiSZ6IRSh0Z8odh1mY&hl=en,none,none,none,none
1448,C,Newport Coast Bathroom Remodeling Pros,"Corona Del Mar, CA",(949) 773-2519,"3800 East Coast Hwy, Corona Del Mar, CA 92625",https://www.google.com/maps/place/?q=place_id:ChIJhVsEbQ_h3IAR0m384qedz8M&hl=en,none,none,none,none
1449,C,Dunkin's Custom Cabinets,"Fort Worth, TX",(817) 560-9908,"3005 Marquita Dr, Fort Worth, TX 76116",https://www.google.com/maps/place/?q=place_id:ChIJZeCK29MMToYR31fGmk6sens&hl=en,none,none,none,none
1450,C,Mufasaleez Construction & Remodeling LLC,"Miami Gardens, FL",(305) 690-3964,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJA3wOpIJCKWYRItDIxtGPE6Q&hl=en,none,none,none,none
1451,C,DelMar Builders,"Deerfield Beach, FL",(954) 806-2136,"90 NE 19th Ave, Deerfield Beach, FL 33441",https://www.google.com/maps/place/?q=place_id:ChIJ2c7Lj-rj2IgRVC_m41-XgZA&hl=en,none,none,none,none
1452,C,Key's Tile & Stone,"Marathon, FL",(305) 743-7053,"6681 Overseas Hwy, Marathon, FL 33050",https://www.google.com/maps/place/?q=place_id:ChIJy0jwjfPe0IgRoFiJx95UDUk&hl=en,none,none,none,none
1453,C,Top Marble,"Alabaster, AL",(205) 664-0480,"130 Commercial Ct, Alabaster, AL 35007",https://www.google.com/maps/place/?q=place_id:ChIJix8YGZ4viYgRvsz34QBre-s&hl=en,none,none,none,none
1454,C,Brookside Contractors LLC,"Newark, DE",(302) 333-7722,"1 Penfield Dr, Newark, DE 19713",https://www.google.com/maps/place/?q=place_id:ChIJkdmsGQZasKERn7URKSQPoYE&hl=en,none,none,none,none
1455,C,Design Pros Home Renovations,"Columbia, MO",(573) 395-6982,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_8_jwToPNKwRU2_UA9zptvI&hl=en,none,none,none,none
1456,C,"Masterpiece Cabinetry, Inc.","Ormond Beach, FL",(386) 212-9724,"623 S Yonge St, Ormond Beach, FL 32174",https://www.google.com/maps/place/?q=place_id:ChIJac_V2Qzb5ogR9RI-axHRu4s&hl=en,none,none,none,none
1457,C,Elevated Creations and Tile,"Woodland Park, CO",(719) 355-9136,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_TBJwYFoNAwRHA10cu-mmAM&hl=en,none,none,none,none
1458,C,Crofoot’s Remodels and Repairs LLC,"Lindale, TX",(903) 519-6523,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJEyWlx-qMMqgRXhoPlkMWlwU&hl=en,none,none,none,none
1459,C,Benito Torres Flooring and Tile Services,"Bay City, TX",(979) 245-3588,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVXHaHJrqE6QR2kGvh9n1FBI&hl=en,none,none,none,none
1460,C,L P Decorative Plumbing,"Daly City, CA",(415) 769-5000,"6073 Mission St, Daly City, CA 94014",https://www.google.com/maps/place/?q=place_id:ChIJD8pG_1t-j4ARdIdaSrVyKWU&hl=en,none,none,none,none
1461,C,Akron Bath Remodeling,"Tallmadge, OH",(234) 231-9167,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhdPRdiMpMYgRqeZIwe1_pX4&hl=en,none,none,none,none
1462,C,Raise Up Home Solutions,"Manalapan Township, NJ",(973) 757-8782,"113 Rumford Way, Manalapan Township, NJ 07726",https://www.google.com/maps/place/?q=place_id:ChIJ1bsFfNWJC24RXMnqCtRmiRs&hl=en,none,none,none,none
1463,C,McGuire Contracting,"Ridley Park, PA",(610) 462-0508,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJRQK_Ymksfk0RSnmh8uN-3nY&hl=en,none,none,none,none
1464,C,My Word Remodeling LLC.,"Lovejoy, GA",(770) 468-7682,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpS4PYgL39IgRVQ1XlnqKdHg&hl=en,none,none,none,none
1465,C,Funke's Custom Cabinets,"Clarkston, WA",(509) 758-7339,"1482 16th Ave, Clarkston, WA 99403",https://www.google.com/maps/place/?q=place_id:ChIJ3bnCU33KoVQRAmrUxpNq9Os&hl=en,none,none,none,none
1466,C,Affordable Kitchens,"Camas, WA",(360) 896-0850,"2011 NW Sierra Ln, Camas, WA 98607",https://www.google.com/maps/place/?q=place_id:ChIJq6qqqs6xlVQR7uj4Cav7Qz0&hl=en,none,none,none,none
1467,C,Goodwin Construction LLC,"Cedar Falls, IA",(319) 464-7483,"5850 Timber Ridge Rd, Cedar Falls, IA 50613",https://www.google.com/maps/place/?q=place_id:ChIJA-LacDcA8IcR_EzSxDFF1dM&hl=en,none,none,none,none
1468,C,Aaron and Son Custom Cabinets,"Muskogee, OK",(918) 441-8510,"920 N Main St, Muskogee, OK 74401",https://www.google.com/maps/place/?q=place_id:ChIJg1q7wNvmtYcRoiRJYHkFEqw&hl=en,none,none,none,none
1469,C,Central Mortar & Grout,"Muskogee, OK",(918) 683-3003,"1300 S 43rd St E, Muskogee, OK 74403",https://www.google.com/maps/place/?q=place_id:ChIJHQ5layritYcRaJy8NcV-72Q&hl=en,none,none,none,none
1470,C,Yoder Cabinets,"Sylacauga, AL",(256) 249-2236,"508 W 4th St, Sylacauga, AL 35150",https://www.google.com/maps/place/?q=place_id:ChIJW26cTGL9i4gRZs7RylFVHhA&hl=en,none,none,none,none
1471,C,New Again Kitchen Remodeling,"Chico, CA",(530) 899-2888,"1108 Mangrove Ave, Chico, CA 95926",https://www.google.com/maps/place/?q=place_id:ChIJR-y1uSYmg4ARb983iBQ6CTE&hl=en,none,none,none,none
1472,C,Randy's Cabinets & Woodwork,"Soddy-Daisy, TN",(423) 332-3846,"233 Industrial Park Dr E, Soddy-Daisy, TN 37379",https://www.google.com/maps/place/?q=place_id:ChIJI8mQ5G2MYIgReJLVh6oyQ0Q&hl=en,none,none,none,none
1473,C,Wyoming Windows & Cabinets,"Lander, WY",(307) 332-2372,"3011 US-287, Lander, WY 82520",https://www.google.com/maps/place/?q=place_id:ChIJAQBQ87b_WIcRVJ3Y92pSBSA&hl=en,none,none,none,none
1474,C,FACT : Flooring And Cabinet Tradecenter,"Florence, SC",(843) 283-8001,"254 N Flea Market Rd, Florence, SC 29506",https://www.google.com/maps/place/?q=place_id:ChIJ3d8nv1BcVYgRZucekrGyhbI&hl=en,none,none,none,none
1475,C,Kitchen Cabinet & Granite,"Kennewick, WA",(509) 783-9500,"7903 W Grandridge Blvd Ste J, Kennewick, WA 99336",https://www.google.com/maps/place/?q=place_id:ChIJ3aHZ9PF5mFQRA6lVj_7Ym9c&hl=en,none,none,none,none
1476,C,"Housers Cabinet Shop, Inc.","Lincolnton, NC",(704) 735-5755,"3325 NC-27, Lincolnton, NC 28092",https://www.google.com/maps/place/?q=place_id:ChIJv2mMWsnRVogRGcQTwK_raGw&hl=en,none,none,none,none
1477,C,Tile Unlimited,"Shelbyville, TN",(931) 685-4303,"109 Noblitt St, Shelbyville, TN 37160",https://www.google.com/maps/place/?q=place_id:ChIJg50fBWDCY4gR7u6eAY44Xew&hl=en,none,none,none,none
1478,C,Natural Stone and Granite,"White Settlement, TX",(817) 244-1600,"and D, 230 S Grants Ln Ste C2, White Settlement, TX 76108",https://www.google.com/maps/place/?q=place_id:ChIJh6JTO0wMToYRT-OKcQOJvyI&hl=en,none,none,none,none
1479,C,Herrera Custom Cabinets,"McGregor, TX",(254) 709-5497,"379 Val Verde Rd, McGregor, TX 76657",https://www.google.com/maps/place/?q=place_id:ChIJXR14vBGJT4YRCGcC9ClEsWA&hl=en,none,none,none,none
1480,C,Rochon - New York / Master Kitchen Designer,"Greenvale, NY",(516) 626-0480,"50 Glen Cove Rd, Greenvale, NY 11548",https://www.google.com/maps/place/?q=place_id:ChIJbYOfELtiwokRwR-OayHHg-E&hl=en,none,none,none,none
1481,C,Venture Kitchen & Bath Showroom Roofing and Design Center,"Plymouth, MI",(734) 656-7179,"44191 Plymouth Oaks Blvd #1300, Plymouth, MI 48170",https://www.google.com/maps/place/?q=place_id:ChIJ-W4S_ietJIgRLTkBQL1hISw&hl=en,none,none,none,none
1482,C,Soggy Bottoms Bathtub Refinishing,"Jonesboro, AR",(870) 926-2729,"153 CR-769, Jonesboro, AR 72405",https://www.google.com/maps/place/?q=place_id:ChIJ10VJXEuA1ocRgpHnsWkklaA&hl=en,none,none,none,none
1483,C,"A-AFFORDABLE REMODELING - Remodeling Service, House Remodeling, Siding Repair, Bathroom Remodel","Daphne, AL",(850) 346-0357,"25895a Friendship Rd Ste e, Daphne, AL 36526",https://www.google.com/maps/place/?q=place_id:ChIJzTZYmYpDmogRLsVaFFZC9oE&hl=en,none,none,none,none
```
