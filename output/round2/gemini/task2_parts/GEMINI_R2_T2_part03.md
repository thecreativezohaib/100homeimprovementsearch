# Round 2: Gemini task 2, part 03 of 17 (100 businesses, rows 1284 to 1383)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 1383: reply in that chat "Continue with
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
1284,C,Petrey's Cabinet Shop,"Science Hill, KY",(606) 423-2002,"923 Stringtown Rd, Science Hill, KY 42553",https://www.google.com/maps/place/?q=place_id:ChIJlcCpQrC0QogRtJk7qTwRby0&hl=en,none,none,none,none
1285,C,Resurrection Contracting LLC,"Flowery Branch, GA",(470) 266-7320,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJPS9PfIopd0IR0H8__pNfiYk&hl=en,none,none,none,none
1286,C,"Arnold's Custom Renovations, LLC","Chesapeake, VA",(757) 227-8910,"1140 Sharon Dr, Chesapeake, VA 23320",https://www.google.com/maps/place/?q=place_id:ChIJ7wxgAi-9uokRNB3xBChSAmY&hl=en,none,none,none,none
1287,C,Design Fine Rock Granite & Marble,"Bridgeview, IL",(708) 441-7408,"8928 S Octavia Ave, Bridgeview, IL 60455",https://www.google.com/maps/place/?q=place_id:ChIJ__8P2dgwDogRFeBwP6J3I8k&hl=en,none,none,none,none
1288,C,StoneCraft of Santa Rosa,"Santa Rosa, CA",(707) 566-9800,"3485 Airway Dr Ste a, Santa Rosa, CA 95403",https://www.google.com/maps/place/?q=place_id:ChIJRah8ANs5hIARuvUG4wIOhnk&hl=en,none,none,none,none
1289,C,Elite Surfaces,"Marietta, OH",(740) 336-8619,"20080 OH-550, Marietta, OH 45750",https://www.google.com/maps/place/?q=place_id:ChIJaZI9YUbLSYgRxBaKlTrcJCk&hl=en,none,none,none,none
1290,C,Trexx Construction LLC,"Jacksonville, NC",(910) 546-5132,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTdqsqo4bqYkRfV7zs4BG4_I&hl=en,none,none,none,none
1291,C,CH Cabinet & Design,"Columbus, GA",(706) 580-1612,"7560 Kayne Blvd, Columbus, GA 31909",https://www.google.com/maps/place/?q=place_id:ChIJf1PwMmfLjIgRKmY1sqnV2c0&hl=en,none,none,none,none
1292,C,Oak Ridge Custom Cabinets,"Green Bay, WI",(920) 499-8855,"2660 N Packerland Dr, Green Bay, WI 54303",https://www.google.com/maps/place/?q=place_id:ChIJD4-1tlP3AogRzFnoL7CRxEA&hl=en,none,none,none,none
1293,C,RandyMan Services,"Vici, OK",(580) 747-5605,"58671 N2060 Rd, Vici, OK 73859",https://www.google.com/maps/place/?q=place_id:ChIJp3H38b8pqYcR5_Hdflbrqp8&hl=en,none,none,none,none
1294,C,Model Tile LLC,"Everett, WA",(425) 772-1918,"11608 29th Ave SE, Everett, WA 98208",https://www.google.com/maps/place/?q=place_id:ChIJrdoJ1-0HkFQRrR0J0X61XRQ&hl=en,none,none,none,none
1295,C,Start Tile,"Manteca, CA",(209) 276-4667,"1046 Eleanor Ln, Manteca, CA 95337",https://www.google.com/maps/place/?q=place_id:ChIJcx7269RFkIARYNUz_UZTtp0&hl=en,none,none,none,none
1296,C,Reed Remodel and Design,"Tuttle, OK",(405) 436-1042,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGXQ5gUaLrYcRC_vuk58nQM4&hl=en,none,none,none,none
1297,C,Zaxx Cabinets,"New Richmond, WI",(800) 660-0408,"453 Wisconsin Dr, New Richmond, WI 54017",https://www.google.com/maps/place/?q=place_id:ChIJgX5tareoslIR3RlfdkgBN94&hl=en,none,none,none,none
1298,C,Delight Renovations,"Kirby, TX",(210) 209-3873,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJN1zjdoD1XIYRUSPSN2dVJRA&hl=en,none,none,none,none
1299,C,Huff's Home Improvements,"North Augusta, SC",(803) 278-5459,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJC5XZAGYz-IgRn7mF2xI9XNU&hl=en,none,none,none,none
1300,C,Yuiry Kitchen & Bathroom Remodeling,"Hewlett, NY",(516) 340-3707,"1318 Broadway, Hewlett, NY 11557",https://www.google.com/maps/place/?q=place_id:ChIJyaIGGlNlwokRmZAnUb95PiY&hl=en,none,none,none,none
1301,C,"Blake Renovations, LLC","Madison, IN",(810) 434-5255,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ52SS2bbPJIgR1h5JbqtJ-Ik&hl=en,none,none,none,none
1302,C,Colonial Home Improvement LLC,"South Hadley, MA",(413) 275-4293,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7ZUGMpBBRKQRf_WhYijTrl8&hl=en,none,none,none,none
1303,C,Remodel Interiors USA,"Artesia, CA",(949) 749-4206,"18708 Clarkdale Ave, Artesia, CA 90701",https://www.google.com/maps/place/?q=place_id:ChIJh-Ca95ct3YAR-GPHzicPyIk&hl=en,none,none,none,none
1304,C,JN Home Remodeling LLC,"Charlotte, NC",(980) 989-4669,"672 Fielding Rd, Charlotte, NC 28214",https://www.google.com/maps/place/?q=place_id:ChIJvRSL_IbWwAwRGh2SGmuirq8&hl=en,none,none,none,none
1305,C,JAF HANDYMAN AND REMODELING,"Mt Clemens, MI",(586) 588-1868,"108 Logan St, Mt Clemens, MI 48043",https://www.google.com/maps/place/?q=place_id:ChIJFxE5dGh_IgkR4Vzjshh8b_0&hl=en,none,none,none,none
1306,C,Barefoot's Cabinet Inc,"Macon, GA",(478) 207-4141,"333 Stratton St, Macon, GA 31201",https://www.google.com/maps/place/?q=place_id:ChIJTfRvrC3884gRkUE3vJTuVR0&hl=en,none,none,none,none
1307,C,"LMG Remodeling, LLC","Hagerstown, MD",(240) 919-9294,"823 Woodland Way, Hagerstown, MD 21742",https://www.google.com/maps/place/?q=place_id:ChIJt_ISwH3tyYkRsyVgRv6tHbE&hl=en,none,none,none,none
1308,C,"Renov8 Design+Build, LLC.","Pea Ridge, AR",(479) 640-4237,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJcW3zScrkiUQRT5-1knrxK1o&hl=en,none,none,none,none
1309,C,Cultured Marble of Cullman,"Cullman, AL",(256) 734-1739,"3544 AL-157, Cullman, AL 35058",https://www.google.com/maps/place/?q=place_id:ChIJQ1-7kgjMiYgRVuKC1Le2zZw&hl=en,none,none,none,none
1310,C,Thiel Cabinet Shop,"St John, IN",(219) 365-5152,"9520 Joliet St, St John, IN 46373",https://www.google.com/maps/place/?q=place_id:ChIJF-_uEHvjEYgRVARZiNYw39I&hl=en,none,none,none,none
1311,C,Estate Cabinetry,"Croton-On-Hudson, NY",(914) 862-4747,"1380 Albany Post Rd, Croton-On-Hudson, NY 10520",https://www.google.com/maps/place/?q=place_id:ChIJUWL0bl3GwokRJ84uMZdQt4k&hl=en,none,none,none,none
1312,C,Cape Cod Tileworks,"Harwich, MA",(508) 246-6324,"705 Main St, Harwich, MA 02645",https://www.google.com/maps/place/?q=place_id:ChIJrYMydbU_-4kR5mNXhUz01SA&hl=en,none,none,none,none
1313,C,Trim Line Inc,"Pilot Point, TX",(940) 686-2099,"1017 N Industrial Blvd, Pilot Point, TX 76258",https://www.google.com/maps/place/?q=place_id:ChIJEx5iaupPTIYRPDDS2vG67tQ&hl=en,none,none,none,none
1314,C,Kitchens & More by Melissa,"Arthur, IA",(712) 330-6513,"6509 IA-175, Arthur, IA 51431",https://www.google.com/maps/place/?q=place_id:ChIJkaiDfyqjkocRVovChXHcRbU&hl=en,none,none,none,none
1315,C,Jalisco Tile,"Perris, CA",(951) 657-4885,"187 E 3rd St, Perris, CA 92570",https://www.google.com/maps/place/?q=place_id:ChIJxwFrKtSh3IARsnFJOImVm2U&hl=en,none,none,none,none
1316,C,Designs By Nika,"Wood-Ridge, NJ",(973) 464-7125,"263 Hackensack St, Wood-Ridge, NJ 07075",https://www.google.com/maps/place/?q=place_id:ChIJP1cu3sn5wokR69VPtKUgRX0&hl=en,none,none,none,none
1317,C,Bancroft Kitchen & Bath,"Yorktown, VA",(757) 988-1100,"6605 George Washington Memorial Hwy, Yorktown, VA 23692",https://www.google.com/maps/place/?q=place_id:ChIJ48BhOX1-sIkRa0UdhYeUbSQ&hl=en,none,none,none,none
1318,C,U-Save Kitchen & Bath,"Fremont, CA",(510) 770-9908,"45200 Industrial Dr Ste 1, Fremont, CA 94538",https://www.google.com/maps/place/?q=place_id:ChIJG5-DDgHHj4ARhmQZR1Yld0c&hl=en,none,none,none,none
1319,C,S & M Kitchen & Bath,"Montclair, NJ",(973) 685-6892,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzVVp6CJVwokR-lr5ECbiXRk&hl=en,none,none,none,none
1320,C,Affordable Shower & Tub Remodeling,"San Antonio, TX",(210) 500-3024,"1533 Austin Hwy Ste 102-477, San Antonio, TX 78218",https://www.google.com/maps/place/?q=place_id:ChIJV3hs_cX1XIYRztIXPcin5KI&hl=en,none,none,none,none
1321,C,M&M Kitchen & Bath,"Waco, TX",(254) 848-9272,"6175 N State Hwy 6, Waco, TX 76712",https://www.google.com/maps/place/?q=place_id:ChIJlyLnJpyPT4YRVooF_aEwPHs&hl=en,none,none,none,none
1322,C,Burgos Tile,"Porterville, CA",(559) 781-7568,"492 W Olive Ave, Porterville, CA 93257",https://www.google.com/maps/place/?q=place_id:ChIJY76Wi2u46oARmui5XJPCxYM&hl=en,none,none,none,none
1323,C,Oak Ridge Customs- Cabinetry & Homes,"Brownwood, TX",(325) 203-8196,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJlQVXdy_BUIYRzQ4YjjCSgCI&hl=en,none,none,none,none
1324,C,Wolston Tile Designs,"Duncan, OK",(580) 467-4399,"1927 Ridgeway Cir, Duncan, OK 73533",https://www.google.com/maps/place/?q=place_id:ChIJ1_ZG79NcrYcRcTZvvxJGAXA&hl=en,none,none,none,none
1325,C,MPI Services - Kitchen Cabinet Installation Services,"Athens, GA",(941) 500-2523,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJU6CuRMweoEwRC7Y3pG0fYxg&hl=en,none,none,none,none
1326,C,Five Star Bath Solutions of Providence,"North Providence, RI",(401) 356-3819,"1006 Charles St unit 9a, North Providence, RI 02904",https://www.google.com/maps/place/?q=place_id:ChIJLa30_CZF5IkRuU6ylXDGC_Y&hl=en,none,none,none,none
1327,C,1 Day Bath-HSU,"Holmdel, NJ",(877) 955-2284,"670 N Beers St Bldg 4, Holmdel, NJ 07733",https://www.google.com/maps/place/?q=place_id:ChIJs6qtbN8zwokRzsRVxMxpS4c&hl=en,none,none,none,none
1328,C,A-Master Builders & Remodeling,"Bellmawr, NJ",(856) 430-4043,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqYmp_fLPxokRPPPVCILUx-g&hl=en,none,none,none,none
1329,C,All Home Remodeling,"Westchester, IL",(708) 624-1986,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ43vWK1u_SSsRF7DP95S-Xxg&hl=en,none,none,none,none
1330,C,Emery Design | Build,"Northville, MI",(248) 573-5700,"16857 Northville Rd, Northville, MI 48168",https://www.google.com/maps/place/?q=place_id:ChIJ5fB9xLCtJIgRataBY6XOO1Y&hl=en,none,none,none,none
1331,C,Five Star Bath of Evansville,"Evansville, IN",(812) 366-7447,"312 NW Martin Luther King Jr Blvd #203, Evansville, IN 47708",https://www.google.com/maps/place/?q=place_id:ChIJvQPAuj_VcYgRx2jtqdUikAs&hl=en,none,none,none,none
1332,C,Black Forest Construction LLC,"Rathdrum, ID",(208) 691-5482,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJSY2B7ZjrYVMRW0hWTm-kKYs&hl=en,none,none,none,none
1333,C,"Lotz Home & Office, LLC","Crest Hill, IL",(815) 260-6773,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqTE9MjL1DogRBPUulugHRNU&hl=en,none,none,none,none
1334,C,Hudson Remodeling Contractors NY LLC,"Yonkers, NY",(914) 313-8409,"61 Garfield St, Yonkers, NY 10701",https://www.google.com/maps/place/?q=place_id:ChIJtWzCUYHywokRK_4U_mvIaZw&hl=en,none,none,none,none
1335,C,Fuentes Carpentry & Remodeling Services,"Richmond, TX",(832) 520-5925,"6714 Pickett Dr, Richmond, TX 77469",https://www.google.com/maps/place/?q=place_id:ChIJ7zoF77zjQIYRDlCALMR5s4U&hl=en,none,none,none,none
1336,C,L&D DANNY’S NEW BUILDING AND RENOVATIONS,"Fort Worth, TX",(817) 271-9465,"5607 Humbert Ave, Fort Worth, TX 76107",https://www.google.com/maps/place/?q=place_id:ChIJtxqxTMlzToYR5TjDakzkBns&hl=en,none,none,none,none
1337,C,Revive Renovations,"Salem, UT",(801) 376-7326,"650 E Salem Canal Rd, Salem, UT 84653",https://www.google.com/maps/place/?q=place_id:ChIJ0Q79xLuFTYcR592ZOMAhCbk&hl=en,none,none,none,none
1338,C,WA Pro Builders LLC,"Redmond, WA",(206) 804-1196,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDVnuYVeLz64RqhlUW6YqQHI&hl=en,none,none,none,none
1339,C,The Cabinet Shop,"Harlingen, TX",(956) 202-3893,"21168 FM508, Harlingen, TX 78550",https://www.google.com/maps/place/?q=place_id:ChIJRyqwkMR4b4YRQJRuZSQ6uzE&hl=en,none,none,none,none
1340,C,S&A Excellence Bathroom Remodeling,"Brea, CA",(949) 850-6772,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxc0viDsInK8RnfTfF8Piw6Q&hl=en,none,none,none,none
1341,C,Costa Mesa Bathroom Remodeling Pros,"Costa Mesa, CA",(949) 669-7950,"369 E 17th St, Costa Mesa, CA 92627",https://www.google.com/maps/place/?q=place_id:ChIJF5AHpHLf3IAR72hdBaa7geM&hl=en,none,none,none,none
1342,C,Fred's Cabinet Shop,"Dadeville, AL",(256) 825-6875,"2728 Horseshoe Bend Rd, Dadeville, AL 36853",https://www.google.com/maps/place/?q=place_id:ChIJ8UMOX4NwjIgRaB6qotV093M&hl=en,none,none,none,none
1343,C,Robinson's Restoration & Remodeling,"Locust Grove, GA",(770) 668-6907,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ9wOaHL1e9IgRx-dBajiXqe4&hl=en,none,none,none,none
1344,C,DANE COOK cook enterprises interior and exterior solutions,"Brockport, NY",(585) 315-6016,"9373 W Ridge Rd, Brockport, NY 14420",https://www.google.com/maps/place/?q=place_id:ChIJzZE8L3YD1IkRpUGF1y8a464&hl=en,none,none,none,none
1345,C,Orangeburg Tile LLC,"Orangeburg, SC",(803) 662-9803,"1644 St Matthews Rd NE, Orangeburg, SC 29118",https://www.google.com/maps/place/?q=place_id:ChIJc8I1rFnU-IgRW0_AdEYdMUo&hl=en,none,none,none,none
1346,C,Coleman's Refinishing,"Denham Springs, LA",(504) 252-6238,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJV2KDmzH162MRU88H1F-7wmU&hl=en,none,none,none,none
1347,C,AMS Remodeling Inc.,"Loves Park, IL",(847) 971-3041,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJoe5eZAILE6wRRoreuezF_q4&hl=en,none,none,none,none
1348,C,Shamrock Tile LLC,"DeBary, FL",(407) 388-5511,"748 Costa Ln, DeBary, FL 32713",https://www.google.com/maps/place/?q=place_id:ChIJB_PXxZsT54gRd7-pDLiGrMY&hl=en,none,none,none,none
1349,C,Kitchen Innovations,"Fort Walton Beach, FL",(850) 796-3000,"44 Beal Pkwy SW, Fort Walton Beach, FL 32548",https://www.google.com/maps/place/?q=place_id:ChIJQwvovCM_kYgRtp4vg68e4K8&hl=en,none,none,none,none
1350,C,Creative Countertops,"Goleta, CA",(805) 946-0681,"178 Aero Camino, Goleta, CA 93117",https://www.google.com/maps/place/?q=place_id:ChIJ23wEZ5tA6YARTm5033BA7hg&hl=en,none,none,none,none
1351,C,Legacy Kitchens and Bath Plus,"Hollywood, FL",(954) 477-7080,"1918 Harrison St Ste 102, Hollywood, FL 33020",https://www.google.com/maps/place/?q=place_id:ChIJKzxHJ7ir2YgRCAlNH_ovqlM&hl=en,none,none,none,none
1352,C,Berza Group Corp,"Boynton Beach, FL",(954) 297-2126,"1020 Audace Ave, Boynton Beach, FL 33426",https://www.google.com/maps/place/?q=place_id:ChIJydf_4GCaFo4RBPuTU1khTas&hl=en,none,none,none,none
1353,C,Houss Build Remodel Repair,"St Cloud, FL",(689) 307-3646,"4640 Glencrest Loop, St Cloud, FL 34772",https://www.google.com/maps/place/?q=place_id:ChIJC19B23phJkcRhGSWsTh59V0&hl=en,none,none,none,none
1354,C,"MC Bathroom Remodeling, LLC","Kansas City, KS",(913) 963-9603,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTQzAyR6GGUcRFQ0A5yr_03k&hl=en,none,none,none,none
1355,C,Vinsicks' Flooring Design,"Indianola, IA",(515) 808-0465,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbxdZdO6PHQcR_kRflLC2yxU&hl=en,none,none,none,none
1356,C,Brian's Remodeling,"Ardmore, OK",(580) 264-0202,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJB-yR4FLVgkwR8otf40h6qG0&hl=en,none,none,none,none
1357,C,Mason's Renovations,"Utqia?vik, AK",(907) 671-1630,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ276BAJ0sqKcROoYFmSqaSz8&hl=en,none,none,none,none
1358,C,LW | Kitchen Remodeling of St Charles,"St. Charles, IL",(630) 228-1255,"306 S 2nd St, St. Charles, IL 60174",https://www.google.com/maps/place/?q=place_id:ChIJkW1Cx30DD4gRRXTagTH-9nM&hl=en,none,none,none,none
1359,C,Mattfield Renovations LLC,"Bemidji, MN",(218) 556-1257,"3495 Buchanan Ave SW, Bemidji, MN 56601",https://www.google.com/maps/place/?q=place_id:ChIJkS4Skbwm0qcRzJiLUl1s1ZA&hl=en,none,none,none,none
1360,C,MASTERCRAFT TILING LLC,"Westfield, IN",(463) 254-8517,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJO38a_rhxXaERtobiXf5ql28&hl=en,none,none,none,none
1361,C,Pruitt Home Renovations LLC,"Minden, LA",(318) 225-0817,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ66pVTOUVMYYR6-Ty3X1ETcY&hl=en,none,none,none,none
1362,C,Wilson's Cabinet Shop,"Glasgow, KY",(270) 651-7271,"812 Columbia Ave, Glasgow, KY 42141",https://www.google.com/maps/place/?q=place_id:ChIJObq-5q89ZogRvlRc4mkoRVw&hl=en,none,none,none,none
1363,C,Creative Finishes By Kelly,"Middletown, KY",(502) 649-0654,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJr6WIu2JRvS8Ro5otI-uxzLU&hl=en,none,none,none,none
1364,C,Miami Baths Refinishing,"Plantation, FL",(754) 291-6664,"499 NW 70th Ave suite: 300, Plantation, FL 33317",https://www.google.com/maps/place/?q=place_id:ChIJ_5n-Z64H2YgRB1tZH5GNBps&hl=en,none,none,none,none
1365,C,B&J Refinishing,"Woodway, TX",(254) 523-5754,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAQBEOTuHT4YR-GyLN4ILpeg&hl=en,none,none,none,none
1366,C,HSP Kitchen Remodel,"Everett, WA",(425) 616-3222,"125 W Casino Rd Unit 16, Everett, WA 98204",https://www.google.com/maps/place/?q=place_id:ChIJn8SMBlUBkFQRVGYNF4BMXmw&hl=en,none,none,none,none
1367,C,MKB HOME DESIGN,"Bell Gardens, CA",(562) 862-0279,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJB0pD2ZnNwoARr2tgyd9l5Jw&hl=en,none,none,none,none
1368,C,Haynes Services & Construction,"Alvin, TX",(979) 264-1220,"1108 E Hwy 6 Ste J, Alvin, TX 77511",https://www.google.com/maps/place/?q=place_id:ChIJw3L9S0aPQIYRZxZF7934EKQ&hl=en,none,none,none,none
1369,C,B & C Kitchens 'n Moore,"Groveland, FL",(352) 552-0448,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJkVMoibSN54gRV7aSILoPOiY&hl=en,none,none,none,none
1370,C,Woodlands Home Remodeling,"The Woodlands, TX",(281) 305-5267,"25275 Budde Rd Ste 28, The Woodlands, TX 77380",https://www.google.com/maps/place/?q=place_id:ChIJb8zRhSQ0R4YR-rB0n6zr5ec&hl=en,none,none,none,none
1371,C,Brandon Joseph Custom Bath & Interiors,"Ferndale, MI",(248) 602-0248,"744 Laprairie St, Ferndale, MI 48220",https://www.google.com/maps/place/?q=place_id:ChIJr2sIdfg-jE4RYA18M9DWcWc&hl=en,none,none,none,none
1372,C,Eagle valley design,"Saratoga Springs, UT",(801) 854-8762,"228 West Lariat Blvd, Saratoga Springs, UT 84045",https://www.google.com/maps/place/?q=place_id:ChIJ1dhmPix5TYcRB1TE05vhFEg&hl=en,none,none,none,none
1373,C,Kitchen Works of Cabot,"Ward, AR",(501) 941-3955,"13905 Hwy 31, Ward, AR 72176",https://www.google.com/maps/place/?q=place_id:ChIJTUS-Yuru0ocRw6RzwGu7fiE&hl=en,none,none,none,none
1374,C,Frick & Sons,"Chehalis, WA",(253) 878-2205,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJFb3SP__mDmcR4TjYhkAiGsU&hl=en,none,none,none,none
1375,C,Superior Renovations,"Albany, OH",(740) 517-8795,"27480 Old State Rte 346, Albany, OH 45710",https://www.google.com/maps/place/?q=place_id:ChIJcaBV2avRR4gRYVM-LASPDys&hl=en,none,none,none,none
1376,C,Sal's Painting and Remodeling,"Sansom Park, TX",(682) 270-3049,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-QDkaujvpGQRiHgwOrltEVE&hl=en,none,none,none,none
1377,C,Reflect,"Longview, WA",(360) 846-3273,"1305 California Way Ste C, Longview, WA 98632",https://www.google.com/maps/place/?q=place_id:ChIJo6C3vNbvWyUR15EfS2mPxXg&hl=en,none,none,none,none
1378,C,A-1 Shower Repair,"South Houston, TX",(713) 947-7457,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOyxH-0SYQIYR7_79eO9zEpQ&hl=en,none,none,none,none
1379,C,Trusted Contracting,"Appleton, WI",(920) 851-3225,"5550 W Edgewood Dr, Appleton, WI 54913",https://www.google.com/maps/place/?q=place_id:ChIJcwfy3QDLA4gRRrTlLMVau94&hl=en,none,none,none,none
1380,C,Alabama Countertop Co,"Cullman, AL",(256) 739-5505,"20 Nesmith Rd, Cullman, AL 35058",https://www.google.com/maps/place/?q=place_id:ChIJ8RQ2V_bMiYgRx49u10ZAClU&hl=en,none,none,none,none
1381,C,Paradise Globe Kitchen and Bath Cabinet Sales,"Lauderhill, FL",(954) 394-2954,"3541 NW 7th Pl, Lauderhill, FL 33311",https://www.google.com/maps/place/?q=place_id:ChIJuyx3NSb6wKIRmHwf5BwAl9g&hl=en,none,none,none,none
1382,C,Grace Home Kitchen & Bath,"Jamaica, NY",(929) 922-7877,"112-05 Rockaway Blvd, Jamaica, NY 11420",https://www.google.com/maps/place/?q=place_id:ChIJM9OKvF1nwokRUrwky9-K5lg&hl=en,none,none,none,none
1383,C,Elite Tile LLC,"La Grande, OR",(541) 429-3555,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJd67FfsLKHyARV7NZ2LAMD3I&hl=en,none,none,none,none
```
