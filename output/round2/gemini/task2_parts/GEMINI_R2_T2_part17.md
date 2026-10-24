# Round 2: Gemini task 2, part 17 of 17 (96 businesses, rows 519 to 553)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 553: reply in that chat "Continue with
   the businesses after LAST_ROW_DONE, same rules, same columns" and keep that report too.

## The task (Gemini: follow this exactly)
```
You are doing a long research task on 96 small kitchen and bathroom remodeling businesses in the United
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

## Businesses (96, in order)
```csv
row,task,business_name,town,phone,address,google_maps,known_facebook,known_instagram,known_email,dead_website
519,D,TGP Home Services LLC,"Chamblee, GA",(404) 966-5583,"5126 Peachtree Blvd, Chamblee, GA 30341",https://www.google.com/maps/place/?q=place_id:ChIJdwHQPtMJ9YgRp7FsSmwv_Ak&hl=en,none,none,none,none
534,D,ARM Home Care,"Mendham, NJ",(973) 348-9915,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ75loAqejw4kRQnUDsQrtplk&hl=en,none,none,none,none
539,D,Granite Mastercraft,"Shelby, NC",(336) 410-2260,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJUQZOI3zEZSoRpTahP1j42Mw&hl=en,none,none,none,none
20,D,Team Worx Remodeling,"Roxboro, NC",(919) 384-5147,"4595 Helena Moriah Rd, Rougemont, NC 27572",https://www.google.com/maps/place/?q=place_id:ChIJq6omVH0QrYkR5SIJ8NyZowU&hl=en,none,none,none,none
37,D,Stone Rosario,"Country Club Hills, IL",(708) 250-2144,"4941 173rd St, Country Club Hills, IL 60478",https://www.google.com/maps/place/?q=place_id:ChIJ695DLSUXDogRnVNzmT4qDRU&hl=en,none,none,none,none
50,D,FJ Remodeling,"Balch Springs, TX",,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ67Far3obMKgR_InMD0D5ewg&hl=en,none,none,none,none
101,D,Liberty Remodeling Inc,"San Clemente, CA",(949) 373-5494,"San Clemente, CA 92672",https://www.google.com/maps/place/?q=place_id:ChIJc7bBIzL13IARA1X_xPK1Mhg&hl=en,none,none,none,none
109,D,Atleorenovations LLC,"Morrow, GA",(404) 423-9078,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbVvQx5G02SMRxxtNwpEB6rc&hl=en,none,none,none,none
110,D,Clinton Premier Painting,"Clinton, NC",(910) 835-9881,"546 5 Bridge Rd, Clinton, NC 28328",https://www.google.com/maps/place/?q=place_id:ChIJT3PJIZyVq4kRThA3PHeyPEY&hl=en,none,none,none,none
111,D,Quality Kitchens & Baths,"Humboldt, TN",(731) 431-9944,"7657 Hwy 45 S, Martin, TN 38237",https://www.google.com/maps/place/?q=place_id:ChIJ0QZqHuZgeYgRwpmHgtxuLOc&hl=en,none,none,none,none
112,D,JJ Renovations Plus LLC,"Dahlonega, GA",(706) 570-5162,"224 Claystone Walk, Cleveland, GA 30528",https://www.google.com/maps/place/?q=place_id:ChIJ1__oBNVDX4gR_qe8aXI1qKA&hl=en,none,none,none,none
130,D,KJs Glass & Bath Enhancements LLC,"Goose Creek, SC",(843) 364-8085,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJRVEMq2eCz08RF2S0IICYe6o&hl=en,none,none,none,none
134,D,Tim’s Total,"Muscle Shoals, AL",(256) 762-5262,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdZszLGYIKk4RFPIPcpSRIdY&hl=en,none,none,none,none
138,D,Enliven Remodeling,"Cheney, WA",(208) 982-5460,"5522 N Farmfield Rd, Newman Lake, WA 99025",https://www.google.com/maps/place/?q=place_id:ChIJ3x2QIejdYVMRJlSSgakQRKU&hl=en,none,none,none,none
142,D,AFFORDABLE FLOOR & MORE REMODELING,"Palmetto Bay, FL",(352) 232-9138,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJCUHKbT_d2YgRQNhvodlOP-c&hl=en,none,none,none,none
165,D,RS Remodeling Services LLC,"Lauderhill, FL",(954) 444-1974,"3901 W Broward Blvd #121236, Fort Lauderdale, FL 33312",https://www.google.com/maps/place/?q=place_id:ChIJh3HXvuccAQMRA9XTKUfpEKs&hl=en,none,none,none,none
167,D,Classic Kitchens,"Kaukauna, WI",(920) 540-7006,"N 3740 Uni Dr, Kaukauna, WI 54130",https://www.google.com/maps/place/?q=place_id:ChIJOUJkMEOtA4gRL5U4vaaK-bE&hl=en,none,none,none,none
190,D,Jose's Tiles,"Glenwood Springs, CO",(970) 452-7256,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJWQxRlmkUpaERLx_5h7ig7Fg&hl=en,none,none,none,none
198,D,Cruz Home Improvement RI,"Pawtucket, RI",(401) 256-9207,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdw1nuFicTogRf4pp1hy5Gdg&hl=en,none,none,none,none
208,D,Greencastle Construction llc,"Waynesboro, PA",(717) 643-1923,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_dBqj_WPyYkR4riTjUghdqs&hl=en,none,none,none,none
222,D,JNG Floors And More LLC.,"Valparaiso, IN",(219) 669-9782,"1454 W US Hwy 30, Valparaiso, IN 46385",https://www.google.com/maps/place/?q=place_id:ChIJE79iTGCREYgRQmcjp8kXoHM&hl=en,none,none,none,none
233,D,Glamorous Kitchens & Bath,"Belle Glade, FL",(727) 999-1959,"147 E Oakwood St, Tarpon Springs, FL 34689",https://www.google.com/maps/place/?q=place_id:ChIJPfimy93zwogREhO39NcMgwU&hl=en,none,none,none,none
252,D,"BSWB, Inc.","Sellersburg, IN",(812) 246-5619,"860 S Penn Ave, Sellersburg, IN 47172",https://www.google.com/maps/place/?q=place_id:ChIJdzlaLz5waYgRHiDVAouQGGs&hl=en,none,none,none,none
308,D,Kitchen Remodel Denver,"Commerce City, CO",(720) 726-1820,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJIX98McV4bIcR7LGjEUCsgZQ&hl=en,none,none,none,none
334,D,Bath Remodeling Home Contractor G&S Construction,"Diamond Bar, CA",(626) 536-2959,"2041 Gladstone St, Glendora, CA 91740",https://www.google.com/maps/place/?q=place_id:ChIJTyei5Esvw4ARJxWl6-N8Yn4&hl=en,none,none,none,none
336,D,CSContractingINC.,"Manassas Park, VA",(703) 996-6238,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJyUWzwoIEr6cRXUNh2b_vKdA&hl=en,none,none,none,none
353,D,Gravitas Services,"Richmond Hill, GA",(912) 730-4038,"200 Edsel Dr, Richmond Hill, GA 31324",https://www.google.com/maps/place/?q=place_id:ChIJA79n_BUP-4gRO9ldCuuZp94&hl=en,none,none,none,none
392,D,Precision Craft Woodworks LLC,"Terrell, TX",(972) 872-1708,"7723 Colquitt Rd, Terrell, TX 75160",https://www.google.com/maps/place/?q=place_id:ChIJyZc64alTSYYR1wBu9DR_LRg&hl=en,none,none,none,none
398,D,Platt Painting and Renovations LLC.,"Chapel Hill, NC",(919) 418-7601,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJCcbaLJnErIkR3QJJVg01Hok&hl=en,none,none,none,none
421,D,Braley Home Renovations,"Nashua, NH",(603) 953-4969,"230 Amherst St, Nashua, NH 03063",https://www.google.com/maps/place/?q=place_id:ChIJb_zFUZG244kRwCDvPtnCmXw&hl=en,none,none,none,none
425,D,A V Remodeling LLC,"Ashwaubenon, WI",(920) 217-3137,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJV-Shyo39AogRcWSMRUP_tWs&hl=en,none,none,none,none
427,D,Kitchen Gallery Showroom,"Ormond Beach, FL",(386) 677-2999,"205 S Yonge St, Ormond Beach, FL 32174",https://www.google.com/maps/place/?q=place_id:ChIJATaZgGnb5ogRssM60uBVkFg&hl=en,none,none,none,none
454,D,Better Call Mike,"Sartell, MN",(320) 290-2535,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJA7SNnBHBg4wRp7jTBRODdxk&hl=en,none,none,none,none
512,D,Murphy's Tileworks,"Inverness, FL",(352) 322-3218,"6925 E Turner Camp Rd, Inverness, FL 34453",https://www.google.com/maps/place/?q=place_id:ChIJtRyW2lG2-IMRxxFSEHNq39U&hl=en,none,none,none,none
5,D,DFW BATH & SHOWER EXPERTS LLC,"Northlake, TX",(972) 505-0032,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJffyRdR73Sy0RKnZSMkJlKZg&hl=en,none,none,none,none
8,D,Farhad Designs Remodeling,"San Clemente, CA",(949) 448-9009,"San Clemente, CA 92673",https://www.google.com/maps/place/?q=place_id:ChIJ_df0iWLx3IARtg27bu7WMBY&hl=en,none,none,none,none
14,D,"Integrity Home Remodeling, LLC","Maple Heights, OH",(812) 306-1988,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ9zHH2702EK4RVgsYUbSet1c&hl=en,none,none,none,none
26,D,"Blessed Remodeling Home Improvements, LLC","Lake Grove, NY",(631) 836-1186,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJn5boVEfJ2UkRTDjQO8qbGmw&hl=en,none,none,none,none
56,D,Designer Kitchen and Bath,"Bellaire, TX",(713) 724-7306,"5238 Imogene St, Houston, TX 77096",https://www.google.com/maps/place/?q=place_id:ChIJbxF9ShebXhQRTSm-Qlsaap8&hl=en,none,none,none,none
57,D,CasaCrew Remodeling,"Buda, TX",(512) 413-4287,"505 Wild Pecan Lp, Mustang Ridge, TX 78610",https://www.google.com/maps/place/?q=place_id:ChIJZ4CLmehqByERSFfuGJ4vGhE&hl=en,none,none,none,none
85,D,H & S Remodeling and Painting l.l.c.,"Marysville, OH",(614) 795-1733,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJr5cZb17FOIgRJsFv7ab6LrU&hl=en,none,none,none,none
140,D,PISCHEDDA CONSTRUCTION,"Shawnee, OK",(405) 788-9902,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJA6Y4fzO4s4cRRYUorjHRiew&hl=en,none,none,none,none
147,D,Uncle Brian's Home Improvements,"Firestone, CO",(720) 336-9278,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVVVVVRVzbIcRFoBlD4LH9nM&hl=en,none,none,none,none
152,D,HD CONTRACTING INC,"Puyallup, WA",,"10105 122nd St E, Puyallup, WA 98373",https://www.google.com/maps/place/?q=place_id:ChIJZzHbD_njkFQRYpF6N3b3VeY&hl=en,none,none,none,none
160,D,"Veneto Construction | Porcelain Slab, Tile, Marble, Bathroom and Kitchen Renovation","Harrison, NJ",(347) 990-5981,"530 Harrison Ave Apt 2L, Harrison, NJ 07029",https://www.google.com/maps/place/?q=place_id:ChIJqwXztk9VwokRClITtkyPusI&hl=en,none,none,none,none
161,D,Brandon Kitchen & Bath,"Rutherford, NJ",(973) 477-0138,"228 Main Ave, Clifton, NJ 07014",https://www.google.com/maps/place/?q=place_id:ChIJfSp_l0f_wokRxiuw7ILk_1k&hl=en,none,none,none,none
166,D,Enhanced Remodeling,"Albany, GA",(229) 733-8301,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJBS5L8ECyZaoRXjpXyvk0BoU&hl=en,none,none,none,none
174,D,JTC Remodeling Inc,"Glens Falls, NY",(518) 378-8101,"Queensbury, NY 12804",https://www.google.com/maps/place/?q=place_id:ChIJOR7jJePP34kRr_czxioOSaw&hl=en,none,none,none,none
191,D,Kitchen And Bath Remodels,"Raymondville, TX",(956) 533-0839,"604 W Park Ave, Pharr, TX 78577",https://www.google.com/maps/place/?q=place_id:ChIJrTE50GKhZYYR3l_3HL5ZIq4&hl=en,none,none,none,none
192,D,AL Wood & Remodeling,"Magna, UT",(801) 573-5582,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXW9dgx3Rc24R8KwZgVhxFEI&hl=en,none,none,none,none
199,D,SS4 Construction LLC,"Passaic, NJ",(201) 681-7351,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJPfeZaBDEUmMRn42T8HXurms&hl=en,none,none,none,none
212,D,Filipe Custom Wood Work Inc,"Linden, NJ",(908) 486-0033,"1600 E Edgar Rd, Linden, NJ 07036",https://www.google.com/maps/place/?q=place_id:ChIJP5Ffvc-yw4kR0SL09MDlrkE&hl=en,none,none,none,none
228,D,TMX Improvements and Remodeling,"Windcrest, TX",(210) 992-5995,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJuwWTNPDzXIYRwxTVZ02rQTE&hl=en,none,none,none,none
236,D,Modern Bath Company LLC,"Tacoma, WA",(425) 345-5194,"708 Broadway #106, Tacoma, WA 98402",https://www.google.com/maps/place/?q=place_id:ChIJmemzKBBfkVQR2TN8jY6UBWY&hl=en,none,none,none,none
262,D,Proficient Remodeling Services,"Pasadena, TX",(281) 761-9296,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJCUbXzvc8g0ARq9X805JJ76c&hl=en,none,none,none,none
291,D,G's Remodeling and Construction,"Stephenville, TX",(254) 334-8195,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJx1sWOTsVUYYRVAvjZAkgtWs&hl=en,none,none,none,none
303,D,Crincoli Kitchens,"Elizabeth, NJ",(908) 352-9312,"160 Spring St, Elizabeth, NJ 07201",https://www.google.com/maps/place/?q=place_id:ChIJUxbw0FlNwokRj14E-RQJKBU&hl=en,none,none,none,none
343,D,Pro Carpentry,"South Houston, TX",(713) 875-8313,"8521 Mosley Rd Unit 5, Houston, TX 77075",https://www.google.com/maps/place/?q=place_id:ChIJRV5yzxCRQIYRtUbVSmSY1Uo&hl=en,none,none,none,none
356,D,DMP Remodels,"Batavia, IL",(708) 415-1719,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxbx5VKWOgaoRcAZF2fVGpuI&hl=en,none,none,none,none
370,D,"Natural Wonders Marble & Granite, Inc.","Tuttle, OK",(405) 381-9796,"2713 OK-37, Tuttle, OK 73089",https://www.google.com/maps/place/?q=place_id:ChIJAykoPGt1socRGxWUWH3PIG4&hl=en,none,none,none,none
396,D,Kitchen Remodel,"Pacific, WA",(253) 332-2361,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJfWA_8Pb0DSgRr5ZpA9sQ71w&hl=en,none,none,none,none
401,D,Aiello Home Remodeling LLC,"Zion, IL",(262) 577-1345,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzXJcbC9fBYgRHKKqNTVFqgg&hl=en,none,none,none,none
410,D,DD 214 Remodeling,"Rosenberg, TX",,"6607 Kearney Dr, Richmond, TX 77469",https://www.google.com/maps/place/?q=place_id:ChIJXVGNOxvjQIYRZcS6NyHB3C4&hl=en,none,none,none,none
417,D,LER Home Improvement,"Linden, NJ",(908) 414-2087,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAw9EXYIeHYERxdiZ8wIH9Jk&hl=en,none,none,none,none
447,D,Remodels R Us,"South Houston, TX",(832) 819-7424,"15255 Gulf Fwy #176b, Houston, TX 77034",https://www.google.com/maps/place/?q=place_id:ChIJtTDN77WZQIYRmzkCN5l3h8o&hl=en,none,none,none,none
465,D,Viks Quality Construction,"Sioux Falls, SD",(701) 934-3146,"402 S Van Eps Ave, Sioux Falls, SD 57103",https://www.google.com/maps/place/?q=place_id:ChIJxwluToC1jocRxJQvMaDJJkg&hl=en,none,none,none,none
523,D,Statler Kitchen Bath & Home Center,"Sturgis, MI",(269) 273-4315,"52946 US-131, Three Rivers, MI 49093",https://www.google.com/maps/place/?q=place_id:ChIJ6TfBClEIF4gRQlICrsG41xQ&hl=en,none,none,none,none
530,D,Custom Kitchen & Bath Stone,"Cutler Bay, FL",(305) 975-3777,"10912 SW 188th St, Cutler Bay, FL 33157",https://www.google.com/maps/place/?q=place_id:ChIJuQIBT0rD2YgR_rIvnAPMEWo&hl=en,none,none,none,none
549,D,Areté Wood and Cabinetry,"Philomath, OR",(541) 231-0242,"950 Clemens Mill Rd, Philomath, OR 97370",https://www.google.com/maps/place/?q=place_id:ChIJQ7YDwJFHwFQRMuv_j-Vnjsw&hl=en,none,none,none,none
9,D,Red Beard Renovations,"Unalaska, AK",(907) 521-5596,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqYMc_r_fyFYRpQuhX7TRfeQ&hl=en,none,none,none,none
77,D,Home Design & Luxury,"Tampa, FL",(786) 752-7604,"610 W Waters Ave B, Tampa, FL 33604",https://www.google.com/maps/place/?q=place_id:ChIJwVUvtaPHwogR27xPDLSw0Kk&hl=en,none,none,none,none
83,D,Simply Rachael’s Creations LLC,"Elk River, MN",(763) 300-2920,"19262 Ogden St NW, Elk River, MN 55330",https://www.google.com/maps/place/?q=place_id:ChIJcRGviT1vs1IRGOASY_DXoL8&hl=en,none,none,none,none
84,D,Jerusalem Construction Co,"North Olmsted, OH",,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJb63pa0jrMIgRxJyOCGlc2xE&hl=en,none,none,none,none
103,D,Turnmire Eco Construction,"Connell, WA",(509) 220-4367,"3478-B Moore Rd, Kettle Falls, WA 99141",https://www.google.com/maps/place/?q=place_id:ChIJNbYkumoinlQR0LcW-M1Ocsk&hl=en,none,none,none,none
107,D,Quaker Maid Kitchens Inc,"Reading, PA",(610) 921-2045,"4203 Pottsville Pike A, Reading, PA 19605",https://www.google.com/maps/place/?q=place_id:ChIJsbvTFsh3xokRmoQdIUxc8bA&hl=en,none,none,none,none
123,D,TR Construction,"Fayetteville, NC",(910) 978-2941,"801 Katie St, Fayetteville, NC 28306",https://www.google.com/maps/place/?q=place_id:ChIJbcGghXYTq4kRMy7iyaMjNKg&hl=en,none,none,none,none
201,D,Finish Right Construction LLC,"Rumson, NJ",(732) 690-1585,"269 Jeffrey St, Long Branch, NJ 07740",https://www.google.com/maps/place/?q=place_id:ChIJpzNDcB0lwokRMq7pjm4W8BA&hl=en,none,none,none,none
205,D,GEOTOWER CONSTRUCTION LLC,"Mahwah, NJ",(973) 931-6931,"915 Tuliptree Ct, Mahwah, NJ 07430",https://www.google.com/maps/place/?q=place_id:ChIJd9DrbWvhwokRrmtUhZdHY80&hl=en,none,none,none,none
230,D,Smith Rock Interiors LLC,"Keizer, OR",(503) 931-7461,"3602 Cherry Ave NE, Keizer, OR 97303",https://www.google.com/maps/place/?q=place_id:ChIJxUd5XBr_v1QRNijMwYTShV0&hl=en,none,none,none,none
232,D,EZR Building,"Muscle Shoals, AL",(256) 284-5513,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-bYh4N2Fvi4RgEGS444pDc4&hl=en,none,none,none,none
286,D,MG Bathroom Renovations,"Mont Belvieu, TX",(832) 556-9016,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ02lkQTSVna4Rbv2fCbigaW0&hl=en,none,none,none,none
330,D,Mancebo Home Renovations LLC,"North Lauderdale, FL",(954) 226-3522,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGWQMZWGwFwAR5nl4o2ZkUpA&hl=en,none,none,none,none
332,D,San Marcos Tile & Flooring,"Luling, TX",(512) 831-9190,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJrY9Y3zipXIYRdd7nsRUgqSg&hl=en,none,none,none,none
337,D,Carl's Renovations,"Belle Isle, FL",(321) 231-6733,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJc7s63qxk54gRITxNezJZDlo&hl=en,none,none,none,none
339,D,A&O Wood Design LLC,"Clovis, NM",(575) 749-5657,"216 Mitchell St, Clovis, NM 88101",https://www.google.com/maps/place/?q=place_id:ChIJPz3jW_DfAocRiwU3rt5I8Bo&hl=en,none,none,none,none
344,D,Sans Construction and Design: Remodeling,"Rancho Santa Margarita, CA",(949) 235-6540,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJr45CNAzp3IARvg2ap8j6U70&hl=en,none,none,none,none
397,D,A1 Tiled Customs & Remodeling,"Union Gap, WA",(509) 367-2193,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJA5TOa5DjEogRqlMDC0jneVg&hl=en,none,none,none,none
404,D,Ace Tile and Finishing LLC,"Haddonfield, NJ",(609) 553-6942,"104 Linden Ave, Haddonfield, NJ 08033",https://www.google.com/maps/place/?q=place_id:ChIJuYPKYwvMxokRosY3s7JSAK8&hl=en,none,none,none,none
407,D,Hawksview Services,"Cheshire, CT",(203) 809-1133,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJO8NLpW7H54kREKrhFXuxPoM&hl=en,none,none,none,none
414,D,Kitchen korner Inc,"Airmont, NY",(845) 426-4661,"15 Dana Rd, Monsey, NY 10952",https://www.google.com/maps/place/?q=place_id:ChIJp7EkG2TdwokRt_uSDsxSyUE&hl=en,none,none,none,none
418,D,Tile Home Renovations,"Kearny, NJ",(929) 236-8766,"399 Maple St, Kearny, NJ 07032",https://www.google.com/maps/place/?q=place_id:ChIJ0fOaCC9VwokRGwZcXHl16CI&hl=en,none,none,none,none
422,D,"BLB Construction, LLC","Ionia, MI",(616) 902-8427,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJWdvVYGHoHYwRVsyxnftUPx8&hl=en,none,none,none,none
464,D,J D Restorations,"Pickerington, OH",(220) 204-9438,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ4-JEIOQq60AR7CP4ZGUkenM&hl=en,none,none,none,none
499,D,Tyson and Sons Remodeling LLC,"Camden, AR",(501) 960-7408,"7201 Stevenson Dr B, Little Rock, AR 72209",https://www.google.com/maps/place/?q=place_id:ChIJJajH9Wiv0ocRL2RB3QVWhhc&hl=en,none,none,none,none
550,D,A&E PROPERTY MAINTENANCE LLC,"West Carrollton, OH",(937) 580-4948,"231 E Shannon Ave, West Carrollton, OH 45449",https://www.google.com/maps/place/?q=place_id:ChIJU--_-XKHQIgRpdyqMsg3UAQ&hl=en,none,none,none,none
553,D,Panhandle Pros,"Panama City Beach, FL",(850) 319-6563,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJl2FFC6ONk4gRaT7esgPLS6U&hl=en,none,none,none,none
```
