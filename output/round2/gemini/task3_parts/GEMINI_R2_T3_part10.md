# Round 2: Gemini task 3, part 10 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1336, reply in that chat "Continue with the businesses
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
1287,N,Design Fine Rock Granite & Marble,"Bridgeview, IL",(708) 441-7408,"8928 S Octavia Ave, Bridgeview, IL 60455",https://www.google.com/maps/place/?q=place_id:ChIJ__8P2dgwDogRFeBwP6J3I8k&hl=en,none,none,none,none,none
1288,N,StoneCraft of Santa Rosa,"Santa Rosa, CA",(707) 566-9800,"3485 Airway Dr Ste a, Santa Rosa, CA 95403",https://www.google.com/maps/place/?q=place_id:ChIJRah8ANs5hIARuvUG4wIOhnk&hl=en,none,none,none,none,none
1289,N,Elite Surfaces,"Marietta, OH",(740) 336-8619,"20080 OH-550, Marietta, OH 45750",https://www.google.com/maps/place/?q=place_id:ChIJaZI9YUbLSYgRxBaKlTrcJCk&hl=en,none,none,none,none,none
1290,N,Trexx Construction LLC,"Jacksonville, NC",(910) 546-5132,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTdqsqo4bqYkRfV7zs4BG4_I&hl=en,none,none,none,none,none
1291,N,CH Cabinet & Design,"Columbus, GA",(706) 580-1612,"7560 Kayne Blvd, Columbus, GA 31909",https://www.google.com/maps/place/?q=place_id:ChIJf1PwMmfLjIgRKmY1sqnV2c0&hl=en,none,none,none,none,none
1292,N,Oak Ridge Custom Cabinets,"Green Bay, WI",(920) 499-8855,"2660 N Packerland Dr, Green Bay, WI 54303",https://www.google.com/maps/place/?q=place_id:ChIJD4-1tlP3AogRzFnoL7CRxEA&hl=en,none,none,none,none,none
1293,N,RandyMan Services,"Vici, OK",(580) 747-5605,"58671 N2060 Rd, Vici, OK 73859",https://www.google.com/maps/place/?q=place_id:ChIJp3H38b8pqYcR5_Hdflbrqp8&hl=en,none,none,none,none,none
1294,N,Model Tile LLC,"Everett, WA",(425) 772-1918,"11608 29th Ave SE, Everett, WA 98208",https://www.google.com/maps/place/?q=place_id:ChIJrdoJ1-0HkFQRrR0J0X61XRQ&hl=en,none,none,none,none,none
1295,N,Start Tile,"Manteca, CA",(209) 276-4667,"1046 Eleanor Ln, Manteca, CA 95337",https://www.google.com/maps/place/?q=place_id:ChIJcx7269RFkIARYNUz_UZTtp0&hl=en,none,none,none,none,none
1296,N,Reed Remodel and Design,"Tuttle, OK",(405) 436-1042,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGXQ5gUaLrYcRC_vuk58nQM4&hl=en,none,none,none,none,none
1297,N,Zaxx Cabinets,"New Richmond, WI",(800) 660-0408,"453 Wisconsin Dr, New Richmond, WI 54017",https://www.google.com/maps/place/?q=place_id:ChIJgX5tareoslIR3RlfdkgBN94&hl=en,none,none,none,none,none
1298,N,Delight Renovations,"Kirby, TX",(210) 209-3873,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJN1zjdoD1XIYRUSPSN2dVJRA&hl=en,none,none,none,none,none
1299,N,Huff's Home Improvements,"North Augusta, SC",(803) 278-5459,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJC5XZAGYz-IgRn7mF2xI9XNU&hl=en,none,none,none,none,none
1300,N,Yuiry Kitchen & Bathroom Remodeling,"Hewlett, NY",(516) 340-3707,"1318 Broadway, Hewlett, NY 11557",https://www.google.com/maps/place/?q=place_id:ChIJyaIGGlNlwokRmZAnUb95PiY&hl=en,none,none,none,none,none
1301,N,"Blake Renovations, LLC","Madison, IN",(810) 434-5255,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ52SS2bbPJIgR1h5JbqtJ-Ik&hl=en,none,none,none,none,none
1302,N,Colonial Home Improvement LLC,"South Hadley, MA",(413) 275-4293,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7ZUGMpBBRKQRf_WhYijTrl8&hl=en,none,none,none,none,none
1303,N,Remodel Interiors USA,"Artesia, CA",(949) 749-4206,"18708 Clarkdale Ave, Artesia, CA 90701",https://www.google.com/maps/place/?q=place_id:ChIJh-Ca95ct3YAR-GPHzicPyIk&hl=en,none,none,none,none,none
1304,N,JN Home Remodeling LLC,"Charlotte, NC",(980) 989-4669,"672 Fielding Rd, Charlotte, NC 28214",https://www.google.com/maps/place/?q=place_id:ChIJvRSL_IbWwAwRGh2SGmuirq8&hl=en,none,none,none,none,none
1305,N,JAF HANDYMAN AND REMODELING,"Mt Clemens, MI",(586) 588-1868,"108 Logan St, Mt Clemens, MI 48043",https://www.google.com/maps/place/?q=place_id:ChIJFxE5dGh_IgkR4Vzjshh8b_0&hl=en,none,none,none,none,none
1306,N,Barefoot's Cabinet Inc,"Macon, GA",(478) 207-4141,"333 Stratton St, Macon, GA 31201",https://www.google.com/maps/place/?q=place_id:ChIJTfRvrC3884gRkUE3vJTuVR0&hl=en,none,none,none,none,none
1307,N,"LMG Remodeling, LLC","Hagerstown, MD",(240) 919-9294,"823 Woodland Way, Hagerstown, MD 21742",https://www.google.com/maps/place/?q=place_id:ChIJt_ISwH3tyYkRsyVgRv6tHbE&hl=en,none,none,none,none,none
1308,N,"Renov8 Design+Build, LLC.","Pea Ridge, AR",(479) 640-4237,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJcW3zScrkiUQRT5-1knrxK1o&hl=en,none,none,none,none,none
1309,N,Cultured Marble of Cullman,"Cullman, AL",(256) 734-1739,"3544 AL-157, Cullman, AL 35058",https://www.google.com/maps/place/?q=place_id:ChIJQ1-7kgjMiYgRVuKC1Le2zZw&hl=en,none,none,none,none,none
1310,N,Thiel Cabinet Shop,"St John, IN",(219) 365-5152,"9520 Joliet St, St John, IN 46373",https://www.google.com/maps/place/?q=place_id:ChIJF-_uEHvjEYgRVARZiNYw39I&hl=en,none,none,none,none,none
1311,N,Estate Cabinetry,"Croton-On-Hudson, NY",(914) 862-4747,"1380 Albany Post Rd, Croton-On-Hudson, NY 10520",https://www.google.com/maps/place/?q=place_id:ChIJUWL0bl3GwokRJ84uMZdQt4k&hl=en,none,none,none,none,none
1312,N,Cape Cod Tileworks,"Harwich, MA",(508) 246-6324,"705 Main St, Harwich, MA 02645",https://www.google.com/maps/place/?q=place_id:ChIJrYMydbU_-4kR5mNXhUz01SA&hl=en,none,none,none,none,none
1313,N,Trim Line Inc,"Pilot Point, TX",(940) 686-2099,"1017 N Industrial Blvd, Pilot Point, TX 76258",https://www.google.com/maps/place/?q=place_id:ChIJEx5iaupPTIYRPDDS2vG67tQ&hl=en,none,none,none,none,none
1314,N,Kitchens & More by Melissa,"Arthur, IA",(712) 330-6513,"6509 IA-175, Arthur, IA 51431",https://www.google.com/maps/place/?q=place_id:ChIJkaiDfyqjkocRVovChXHcRbU&hl=en,none,none,none,none,none
1315,N,Jalisco Tile,"Perris, CA",(951) 657-4885,"187 E 3rd St, Perris, CA 92570",https://www.google.com/maps/place/?q=place_id:ChIJxwFrKtSh3IARsnFJOImVm2U&hl=en,none,none,none,none,none
1316,N,Designs By Nika,"Wood-Ridge, NJ",(973) 464-7125,"263 Hackensack St, Wood-Ridge, NJ 07075",https://www.google.com/maps/place/?q=place_id:ChIJP1cu3sn5wokR69VPtKUgRX0&hl=en,none,none,none,none,none
1317,N,Bancroft Kitchen & Bath,"Yorktown, VA",(757) 988-1100,"6605 George Washington Memorial Hwy, Yorktown, VA 23692",https://www.google.com/maps/place/?q=place_id:ChIJ48BhOX1-sIkRa0UdhYeUbSQ&hl=en,none,none,none,none,none
1318,N,U-Save Kitchen & Bath,"Fremont, CA",(510) 770-9908,"45200 Industrial Dr Ste 1, Fremont, CA 94538",https://www.google.com/maps/place/?q=place_id:ChIJG5-DDgHHj4ARhmQZR1Yld0c&hl=en,none,none,none,none,none
1319,N,S & M Kitchen & Bath,"Montclair, NJ",(973) 685-6892,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzVVp6CJVwokR-lr5ECbiXRk&hl=en,none,none,none,none,none
1320,N,Affordable Shower & Tub Remodeling,"San Antonio, TX",(210) 500-3024,"1533 Austin Hwy Ste 102-477, San Antonio, TX 78218",https://www.google.com/maps/place/?q=place_id:ChIJV3hs_cX1XIYRztIXPcin5KI&hl=en,none,none,none,none,none
1321,N,M&M Kitchen & Bath,"Waco, TX",(254) 848-9272,"6175 N State Hwy 6, Waco, TX 76712",https://www.google.com/maps/place/?q=place_id:ChIJlyLnJpyPT4YRVooF_aEwPHs&hl=en,none,none,none,none,none
1322,N,Burgos Tile,"Porterville, CA",(559) 781-7568,"492 W Olive Ave, Porterville, CA 93257",https://www.google.com/maps/place/?q=place_id:ChIJY76Wi2u46oARmui5XJPCxYM&hl=en,none,none,none,none,none
1323,N,Oak Ridge Customs- Cabinetry & Homes,"Brownwood, TX",(325) 203-8196,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJlQVXdy_BUIYRzQ4YjjCSgCI&hl=en,none,none,none,none,none
1324,N,Wolston Tile Designs,"Duncan, OK",(580) 467-4399,"1927 Ridgeway Cir, Duncan, OK 73533",https://www.google.com/maps/place/?q=place_id:ChIJ1_ZG79NcrYcRcTZvvxJGAXA&hl=en,none,none,none,none,none
1325,N,MPI Services - Kitchen Cabinet Installation Services,"Athens, GA",(941) 500-2523,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJU6CuRMweoEwRC7Y3pG0fYxg&hl=en,none,none,none,none,none
1326,N,Five Star Bath Solutions of Providence,"North Providence, RI",(401) 356-3819,"1006 Charles St unit 9a, North Providence, RI 02904",https://www.google.com/maps/place/?q=place_id:ChIJLa30_CZF5IkRuU6ylXDGC_Y&hl=en,none,none,none,none,none
1327,N,1 Day Bath-HSU,"Holmdel, NJ",(877) 955-2284,"670 N Beers St Bldg 4, Holmdel, NJ 07733",https://www.google.com/maps/place/?q=place_id:ChIJs6qtbN8zwokRzsRVxMxpS4c&hl=en,none,none,none,none,none
1328,N,A-Master Builders & Remodeling,"Bellmawr, NJ",(856) 430-4043,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqYmp_fLPxokRPPPVCILUx-g&hl=en,none,none,none,none,none
1329,N,All Home Remodeling,"Westchester, IL",(708) 624-1986,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ43vWK1u_SSsRF7DP95S-Xxg&hl=en,none,none,none,none,none
1330,N,Emery Design | Build,"Northville, MI",(248) 573-5700,"16857 Northville Rd, Northville, MI 48168",https://www.google.com/maps/place/?q=place_id:ChIJ5fB9xLCtJIgRataBY6XOO1Y&hl=en,none,none,none,none,none
1331,N,Five Star Bath of Evansville,"Evansville, IN",(812) 366-7447,"312 NW Martin Luther King Jr Blvd #203, Evansville, IN 47708",https://www.google.com/maps/place/?q=place_id:ChIJvQPAuj_VcYgRx2jtqdUikAs&hl=en,none,none,none,none,none
1332,N,Black Forest Construction LLC,"Rathdrum, ID",(208) 691-5482,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJSY2B7ZjrYVMRW0hWTm-kKYs&hl=en,none,none,none,none,none
1333,N,"Lotz Home & Office, LLC","Crest Hill, IL",(815) 260-6773,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqTE9MjL1DogRBPUulugHRNU&hl=en,none,none,none,none,none
1334,N,Hudson Remodeling Contractors NY LLC,"Yonkers, NY",(914) 313-8409,"61 Garfield St, Yonkers, NY 10701",https://www.google.com/maps/place/?q=place_id:ChIJtWzCUYHywokRK_4U_mvIaZw&hl=en,none,none,none,none,none
1335,N,Fuentes Carpentry & Remodeling Services,"Richmond, TX",(832) 520-5925,"6714 Pickett Dr, Richmond, TX 77469",https://www.google.com/maps/place/?q=place_id:ChIJ7zoF77zjQIYRDlCALMR5s4U&hl=en,none,none,none,none,none
1336,N,L&D DANNY’S NEW BUILDING AND RENOVATIONS,"Fort Worth, TX",(817) 271-9465,"5607 Humbert Ave, Fort Worth, TX 76107",https://www.google.com/maps/place/?q=place_id:ChIJtxqxTMlzToYR5TjDakzkBns&hl=en,none,none,none,none,none
```
