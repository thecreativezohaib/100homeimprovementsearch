# Round 2: Gemini task 3, part 12 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1471, reply in that chat "Continue with the businesses
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
1422,N,Shepherds Construction LLC,"Amherst, OH",(419) 631-2836,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ36BMzearCIURwHLiGF9bwKE&hl=en,none,none,none,none,none
1423,N,Crossover Renovation & Remodeling LLC,"Westminster, CO",(303) 513-5156,"10041 Lewis St, Westminster, CO 80021",https://www.google.com/maps/place/?q=place_id:ChIJXyB10Jl87UAR8MDr-TkL2vM&hl=en,none,none,none,none,none
1424,N,Edg Solutions,"Lyndon, KY",(502) 767-5413,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJR5k2ZQh1aYgRRDmMDdJZoo8&hl=en,none,none,none,none,none
1425,N,Verser's Cabinet Shop LLC,"Rogers, AR",(479) 636-3941,"2351 W Hudson Rd, Rogers, AR 72756",https://www.google.com/maps/place/?q=place_id:ChIJ8yTcKq0QyYcRdWB2-AmPOak&hl=en,none,none,none,none,none
1426,N,Brown's Renovations and Home Improvements,"Flint, MI",(810) 293-5042,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgY5X8bsUyGYRefc75rKP57A&hl=en,none,none,none,none,none
1427,N,Adagio Kitchen and Bath,"Northbrook, IL",(847) 480-6300,"3394 Commercial Ave, Northbrook, IL 60062",https://www.google.com/maps/place/?q=place_id:ChIJEdHVkVC_D4gR2583u2CyY78&hl=en,none,none,none,none,none
1428,N,Muse Bath,"Webster Groves, MO",(314) 408-2708,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ92N9VgOnWysR5RsEogg-eKM&hl=en,none,none,none,none,none
1429,N,Home improvement Vis & Ink,"Dunedin, FL",(727) 687-1356,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZd6dgLOvLygRyg4ot36hylY&hl=en,none,none,none,none,none
1430,N,Colorado Renovations Plus,"Gunnison, CO",(970) 281-5570,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0_BkHB1pGS4R_45hRmGHPOE&hl=en,none,none,none,none,none
1431,N,MDS Project Management,"Indian Harbour Beach, FL",(678) 308-4708,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOX5FgDwR3ogRgJf31qa7BQk&hl=en,none,none,none,none,none
1432,N,"Eastern Renovation Group, LLC","Fayetteville, NC",(702) 817-1177,"6529 Jacobs Creek Cir, Fayetteville, NC 28306",https://www.google.com/maps/place/?q=place_id:ChIJ2e7boxAVq4kRuAJFBKUte8U&hl=en,none,none,none,none,none
1433,N,MaxPro Renovations Inc,"Pineville, NC",(916) 595-9778,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJd-l68o851kwR0hZxexfPgFc&hl=en,none,none,none,none,none
1434,N,MANNY AND BROTHERS TILE INC,"West New York, NJ",(201) 926-4820,"325 53rd St, West New York, NJ 07093",https://www.google.com/maps/place/?q=place_id:ChIJQaVsxSFZwokRKm3cSVxcqR8&hl=en,none,none,none,none,none
1435,N,Tropical House Transformations LLC,"Safety Harbor, FL",(727) 565-6385,"2463 Philippe Pkwy, Safety Harbor, FL 34695",https://www.google.com/maps/place/?q=place_id:ChIJTbU0l0gpNwARJB08Wru5BwE&hl=en,none,none,none,none,none
1436,N,JB Home Remodeling,"Manassas, VA",(703) 717-8315,"7831 Manassas Dr, Manassas, VA 20111",https://www.google.com/maps/place/?q=place_id:ChIJ__-qG5pctokRyaHF2U8LTO4&hl=en,none,none,none,none,none
1437,N,"Edgewater Refinishing, LLC","Edgewater, FL",(386) 478-8890,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJH1QaP5Mv54gRwMiHP-PBuG4&hl=en,none,none,none,none,none
1438,N,Flores Cabinet Makers,"South Houston, TX",(713) 944-0815,"1315 Illinois St, South Houston, TX 77587",https://www.google.com/maps/place/?q=place_id:ChIJHxiWYZaXQIYRC5F_gRL2ctg&hl=en,none,none,none,none,none
1439,N,Align Cabinets and Doors,"City of Atwater, CA",(209) 357-2159,"490 Airpark Rd, City of Atwater, CA 95301",https://www.google.com/maps/place/?q=place_id:ChIJl-MXlpBrkYARf6-7lI7b6uw&hl=en,none,none,none,none,none
1440,N,Custom Granite Quartz Marble Kitchen Countertops,"South Holland, IL",(847) 702-2598,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJN4JbhqQfDogRy_ffyPGy6-w&hl=en,none,none,none,none,none
1441,N,Tile & Decor Inc,"Mission, TX",(956) 580-7442,"4006 N Conway Ave, Mission, TX 78573",https://www.google.com/maps/place/?q=place_id:ChIJw1WtV6OoZYYRXEfi9U29KRk&hl=en,none,none,none,none,none
1442,N,Luxury Modern Baths & Kitchens,"Naugatuck, CT",(203) 617-5239,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJs6Darm3q_28RaEDtenaIjFE&hl=en,none,none,none,none,none
1443,N,Aryeh's Home Improvements,"Morrisville, NC",(984) 286-4371,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvQ1v4YIKYyQRU8gyRfAkLN8&hl=en,none,none,none,none,none
1444,N,MK Stones and Cabinets,"Wellington, FL",(561) 452-3551,"3132 Fortune Way d9, Wellington, FL 33414",https://www.google.com/maps/place/?q=place_id:ChIJ5wTmbPwl2YgRs_AR-_7-KHY&hl=en,none,none,none,none,none
1445,N,JN Granite,"Carthage, MO",(417) 358-4800,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJa7LpA9iFyIcRA_k4sDStl3M&hl=en,none,none,none,none,none
1446,N,Dad's Tile and More,"Wolfforth, TX",(806) 544-3610,"718 Indiana St, Wolfforth, TX 79382",https://www.google.com/maps/place/?q=place_id:ChIJ_zM5kBlt_oYRHanOVQxiDRE&hl=en,none,none,none,none,none
1447,N,H&I kitchen/bathroom remodeling Llc,"Selma, NC",(919) 740-2104,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpdJ_hLiSZ6IRSh0Z8odh1mY&hl=en,none,none,none,none,none
1448,N,Newport Coast Bathroom Remodeling Pros,"Corona Del Mar, CA",(949) 773-2519,"3800 East Coast Hwy, Corona Del Mar, CA 92625",https://www.google.com/maps/place/?q=place_id:ChIJhVsEbQ_h3IAR0m384qedz8M&hl=en,none,none,none,none,none
1449,N,Dunkin's Custom Cabinets,"Fort Worth, TX",(817) 560-9908,"3005 Marquita Dr, Fort Worth, TX 76116",https://www.google.com/maps/place/?q=place_id:ChIJZeCK29MMToYR31fGmk6sens&hl=en,none,none,none,none,none
1450,N,Mufasaleez Construction & Remodeling LLC,"Miami Gardens, FL",(305) 690-3964,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJA3wOpIJCKWYRItDIxtGPE6Q&hl=en,none,none,none,none,none
1451,N,DelMar Builders,"Deerfield Beach, FL",(954) 806-2136,"90 NE 19th Ave, Deerfield Beach, FL 33441",https://www.google.com/maps/place/?q=place_id:ChIJ2c7Lj-rj2IgRVC_m41-XgZA&hl=en,none,none,none,none,none
1452,N,Key's Tile & Stone,"Marathon, FL",(305) 743-7053,"6681 Overseas Hwy, Marathon, FL 33050",https://www.google.com/maps/place/?q=place_id:ChIJy0jwjfPe0IgRoFiJx95UDUk&hl=en,none,none,none,none,none
1453,N,Top Marble,"Alabaster, AL",(205) 664-0480,"130 Commercial Ct, Alabaster, AL 35007",https://www.google.com/maps/place/?q=place_id:ChIJix8YGZ4viYgRvsz34QBre-s&hl=en,none,none,none,none,none
1454,N,Brookside Contractors LLC,"Newark, DE",(302) 333-7722,"1 Penfield Dr, Newark, DE 19713",https://www.google.com/maps/place/?q=place_id:ChIJkdmsGQZasKERn7URKSQPoYE&hl=en,none,none,none,none,none
1455,N,Design Pros Home Renovations,"Columbia, MO",(573) 395-6982,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_8_jwToPNKwRU2_UA9zptvI&hl=en,none,none,none,none,none
1456,N,"Masterpiece Cabinetry, Inc.","Ormond Beach, FL",(386) 212-9724,"623 S Yonge St, Ormond Beach, FL 32174",https://www.google.com/maps/place/?q=place_id:ChIJac_V2Qzb5ogR9RI-axHRu4s&hl=en,none,none,none,none,none
1457,N,Elevated Creations and Tile,"Woodland Park, CO",(719) 355-9136,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_TBJwYFoNAwRHA10cu-mmAM&hl=en,none,none,none,none,none
1458,N,Crofoot’s Remodels and Repairs LLC,"Lindale, TX",(903) 519-6523,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJEyWlx-qMMqgRXhoPlkMWlwU&hl=en,none,none,none,none,none
1459,N,Benito Torres Flooring and Tile Services,"Bay City, TX",(979) 245-3588,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVXHaHJrqE6QR2kGvh9n1FBI&hl=en,none,none,none,none,none
1460,N,L P Decorative Plumbing,"Daly City, CA",(415) 769-5000,"6073 Mission St, Daly City, CA 94014",https://www.google.com/maps/place/?q=place_id:ChIJD8pG_1t-j4ARdIdaSrVyKWU&hl=en,none,none,none,none,none
1461,N,Akron Bath Remodeling,"Tallmadge, OH",(234) 231-9167,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhdPRdiMpMYgRqeZIwe1_pX4&hl=en,none,none,none,none,none
1462,N,Raise Up Home Solutions,"Manalapan Township, NJ",(973) 757-8782,"113 Rumford Way, Manalapan Township, NJ 07726",https://www.google.com/maps/place/?q=place_id:ChIJ1bsFfNWJC24RXMnqCtRmiRs&hl=en,none,none,none,none,none
1463,N,McGuire Contracting,"Ridley Park, PA",(610) 462-0508,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJRQK_Ymksfk0RSnmh8uN-3nY&hl=en,none,none,none,none,none
1464,N,My Word Remodeling LLC.,"Lovejoy, GA",(770) 468-7682,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpS4PYgL39IgRVQ1XlnqKdHg&hl=en,none,none,none,none,none
1465,N,Funke's Custom Cabinets,"Clarkston, WA",(509) 758-7339,"1482 16th Ave, Clarkston, WA 99403",https://www.google.com/maps/place/?q=place_id:ChIJ3bnCU33KoVQRAmrUxpNq9Os&hl=en,none,none,none,none,none
1466,N,Affordable Kitchens,"Camas, WA",(360) 896-0850,"2011 NW Sierra Ln, Camas, WA 98607",https://www.google.com/maps/place/?q=place_id:ChIJq6qqqs6xlVQR7uj4Cav7Qz0&hl=en,none,none,none,none,none
1467,N,Goodwin Construction LLC,"Cedar Falls, IA",(319) 464-7483,"5850 Timber Ridge Rd, Cedar Falls, IA 50613",https://www.google.com/maps/place/?q=place_id:ChIJA-LacDcA8IcR_EzSxDFF1dM&hl=en,none,none,none,none,none
1468,N,Aaron and Son Custom Cabinets,"Muskogee, OK",(918) 441-8510,"920 N Main St, Muskogee, OK 74401",https://www.google.com/maps/place/?q=place_id:ChIJg1q7wNvmtYcRoiRJYHkFEqw&hl=en,none,none,none,none,none
1469,N,Central Mortar & Grout,"Muskogee, OK",(918) 683-3003,"1300 S 43rd St E, Muskogee, OK 74403",https://www.google.com/maps/place/?q=place_id:ChIJHQ5layritYcRaJy8NcV-72Q&hl=en,none,none,none,none,none
1470,N,Yoder Cabinets,"Sylacauga, AL",(256) 249-2236,"508 W 4th St, Sylacauga, AL 35150",https://www.google.com/maps/place/?q=place_id:ChIJW26cTGL9i4gRZs7RylFVHhA&hl=en,none,none,none,none,none
1471,N,New Again Kitchen Remodeling,"Chico, CA",(530) 899-2888,"1108 Mangrove Ave, Chico, CA 95926",https://www.google.com/maps/place/?q=place_id:ChIJR-y1uSYmg4ARb983iBQ6CTE&hl=en,none,none,none,none,none
```
