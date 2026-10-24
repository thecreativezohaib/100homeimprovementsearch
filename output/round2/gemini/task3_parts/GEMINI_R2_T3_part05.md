# Round 2: Gemini task 3, part 05 of 22 (50 businesses: 50 F)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 17, reply in that chat "Continue with the businesses
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
196,F,Strickland Homes & Remodeling,"Ozark, MO",(417) 848-1671,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvSDjGOvS3g4Rlx4UoLJl4cE&hl=en,https://www.facebook.com/61584099000599,none,none,Riley Strickland,none
365,F,EG Custom Countertops LLC,"Cedartown, GA",(678) 901-7995,"1187 East Ave, Cedartown, GA 30125",https://www.google.com/maps/place/?q=place_id:ChIJLVdjco7BiogRDmYLqttY7LU&hl=en,https://www.facebook.com/Egpreciousgranite/,none,none,none,none
559,F,"Stone Specialists, LLC","Marathon, FL",(305) 923-0343,"10641 Aviation Blvd Bldg E, Marathon, FL 33050",https://www.google.com/maps/place/?q=place_id:ChIJ81Lya47b0IgRrGjflIp3cAM&hl=en,https://www.facebook.com/61565056436198,none,none,none,none
229,F,Tepaco Applications & More,"Brownsburg, IN",(317) 654-0832,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJa2K4aPOtbIgRA5t7Y9nZS2c&hl=en,https://www.facebook.com/100089659981411,none,none,none,none
310,F,Home and Space Contracting,"Pine Hill, NJ",(856) 230-1419,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJy7uIRmWvZUARdyZcyzASaPo&hl=en,https://www.facebook.com/100076784266794,none,none,Fred,none
569,F,The Tile Dad NC,"Lincolnton, NC",(704) 530-6161,"1053 Creekside Dr, Lincolnton, NC 28092",https://www.google.com/maps/place/?q=place_id:ChIJA3nXf7PPVogRx2FJs5BsSTs&hl=en,none,https://www.instagram.com/thetiledadnc/,none,Casey Hullette,none
299,F,Jocelyn Pankey Cabinetry & Design,"Clinton, IA",(309) 236-2235,"104 E 6th St, DeWitt, IA 52742",https://www.google.com/maps/place/?q=place_id:ChIJKfhzaOxT4ocRn13Gj3xeMFw&hl=en,https://www.facebook.com/jocelynpankeycabinetry/,none,none,Jocelyn Pankey,https://jocelyn-pankey-cabinetry-design.business.site/
506,F,NEPA Remodeling,"Scranton, PA",(570) 650-6372,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ2RVVwGUgxYkRWpR0vqSlXvQ&hl=en,https://www.facebook.com/neparemodeling/,none,none,Phil Cavanagh,none
155,F,C&K Beachside Remodeling LLC,"Indian Harbour Beach, FL",(321) 426-5073,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgX_PAgpwA44RtWQunoNQAbk&hl=en,https://www.facebook.com/100069972542858,none,none,none,none
249,F,Aser's home remodeling,"Manitou Springs, CO",(719) 722-6831,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJicWZnwJFE4cRw4B1EhnKIaM&hl=en,https://www.facebook.com/AsersHomeRemodeling/,none,none,none,none
460,F,"Easy's Granite, LLC.","Moxee, WA",(509) 759-5153,"109 N Iler St, Moxee, WA 98936",https://www.google.com/maps/place/?q=place_id:ChIJq_WqI9HVmVQRRh1O9yT-8H8&hl=en,https://www.facebook.com/EasysGraniteLLC/,none,none,none,none
466,F,Sowela's Construction LLC,"Elkhart, IN",(574) 217-1968,"Osolo Rd, Elkhart, IN 46514",https://www.google.com/maps/place/?q=place_id:ChIJu2i8QyvdFogROBYSCFHUqNQ&hl=en,https://www.facebook.com/61553150461869,none,none,Chris,none
513,F,Enid Cabinetry and Woodwork,"Enid, OK",(580) 747-2983,"1026 Kline Cir, Enid, OK 73701",https://www.google.com/maps/place/?q=place_id:ChIJjQ9xda1eN2gRRBRKUpF_g-0&hl=en,https://www.facebook.com/61573976371972,none,none,none,none
533,F,Home Investment Solutions LLC,"Clover, SC",(803) 818-1204,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJYcuRTT_tVogRSIeh8k7f2rY&hl=en,https://www.facebook.com/homeinvestmentsolutionsllc/,none,none,Michael W. Avore,none
4,F,G Remodeling Services Llc,"Kennedale, TX",(682) 248-2703,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJX8ojzveJToYR2ddcxdh6pEs&hl=en,https://www.facebook.com/GRemodelingServices/,none,none,Hector Garcia,none
49,F,Martinez Stone Inc,"Nacogdoches, TX",(936) 329-5997,"3007 NW Stallings Dr, Nacogdoches, TX 75964",https://www.google.com/maps/place/?q=place_id:ChIJl73oUICLN4YReRPTliD6AP4&hl=en,https://www.facebook.com/Martinezstone/,none,none,Antonio Martinez,none
519,F,TGP Home Services LLC,"Chamblee, GA",(404) 966-5583,"5126 Peachtree Blvd, Chamblee, GA 30341",https://www.google.com/maps/place/?q=place_id:ChIJdwHQPtMJ9YgRp7FsSmwv_Ak&hl=en,https://www.facebook.com/100063646568336,none,none,Gillermo,none
50,F,FJ Remodeling,"Balch Springs, TX",,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ67Far3obMKgR_InMD0D5ewg&hl=en,https://www.facebook.com/61555036028034/,none,none,none,none
134,F,Tim’s Total,"Muscle Shoals, AL",(256) 762-5262,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdZszLGYIKk4RFPIPcpSRIdY&hl=en,https://www.facebook.com/floorsandmore,none,none,Tim,none
222,F,JNG Floors And More LLC.,"Valparaiso, IN",(219) 669-9782,"1454 W US Hwy 30, Valparaiso, IN 46385",https://www.google.com/maps/place/?q=place_id:ChIJE79iTGCREYgRQmcjp8kXoHM&hl=en,https://www.facebook.com/jngfloors,none,none,none,none
512,F,Murphy's Tileworks,"Inverness, FL",(352) 322-3218,"6925 E Turner Camp Rd, Inverness, FL 34453",https://www.google.com/maps/place/?q=place_id:ChIJtRyW2lG2-IMRxxFSEHNq39U&hl=en,https://www.facebook.com/61574160899531/,none,none,Eric,none
356,F,DMP Remodels,"Batavia, IL",(708) 415-1719,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxbx5VKWOgaoRcAZF2fVGpuI&hl=en,https://www.facebook.com/100067586964837,none,none,none,none
447,F,Remodels R Us,"South Houston, TX",(832) 819-7424,"15255 Gulf Fwy #176b, Houston, TX 77034",https://www.google.com/maps/place/?q=place_id:ChIJtTDN77WZQIYRmzkCN5l3h8o&hl=en,https://www.facebook.com/RemodelsRUSLLC,none,none,none,http://remodelsrus.net
123,F,TR Construction,"Fayetteville, NC",(910) 978-2941,"801 Katie St, Fayetteville, NC 28306",https://www.google.com/maps/place/?q=place_id:ChIJbcGghXYTq4kRMy7iyaMjNKg&hl=en,https://www.facebook.com/TRConstructionNC,none,none,Thomas Raynor,none
286,F,MG Bathroom Renovations,"Mont Belvieu, TX",(832) 556-9016,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ02lkQTSVna4Rbv2fCbigaW0&hl=en,https://www.facebook.com/MgRenovationsTx,none,none,none,none
397,F,A1 Tiled Customs & Remodeling,"Union Gap, WA",(509) 367-2193,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJA5TOa5DjEogRqlMDC0jneVg&hl=en,https://www.facebook.com/tile.works.496954,none,none,Felipe Jardinez,none
481,F,ProBuild Construction SC LLC.,"Lyman, SC",(864) 504-5280,"196 Crow Rd, Inman, SC 29349",https://www.google.com/maps/place/?q=place_id:ChIJy6BGlrGDV4gRmO25zlxWoyQ&hl=en,https://www.facebook.com/probuildconstructionsc,https://www.instagram.com/spprecisionwoodworks,none,none,none
193,F,Granite Innovations,"Van Buren, AR",(479) 279-0497,"1007 Fayetteville Rd, Van Buren, AR 72956",https://www.google.com/maps/place/?q=place_id:ChIJOU0U4lC0y4cRsCkSCvN5Kv8&hl=en,https://www.facebook.com/graniteinnovationsar,none,none,Sam Gallardo,none
381,F,Celebrity Appliance Contractors LLC,"Boonton, NJ",(973) 402-8484,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQRLkc318noERzfW0YcuOOpk&hl=en,none,https://www.instagram.com/celebrityappliances/,none,none,none
93,F,EM Woodwork & Tile - Bathroom Remodeling - Traverse City,"Traverse City, MI",(231) 920-5211,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHTavdO65H4gRN2JN3pwTBzA&hl=en,https://www.facebook.com/emwoodworkandtile,none,none,none,none
373,F,Just Bathrooms Remodeling Inc,"West Haven, UT",(801) 882-9718,"763 Marshall Way N, Layton, UT 84041",https://www.google.com/maps/place/?q=place_id:ChIJH2l-PgIDU4cRcdWemRzrBtA&hl=en,http://www.facebook.com/jbremodelings/,none,none,none,none
374,F,Best Kitchen,"Paterson, NJ",(201) 773-6412,"34-15 Broadway, Fair Lawn, NJ 07410",https://www.google.com/maps/place/?q=place_id:ChIJOe0pRp_7wokRN1CorN4zJZc&hl=en,none,https://www.instagram.com/bestkitchen_nj,none,none,none
479,F,Mr. Remodel,"Papillion, NE",(402) 536-9490,"12370 Cooper St, Papillion, NE 68046",https://www.google.com/maps/place/?q=place_id:ChIJJz-XDif1k4cRLDU7OkVS1Io&hl=en,https://www.facebook.com/MrRemodelNE,none,none,Drew M. Pankow,none
574,F,180 Remodeling,"Morristown, TN",(423) 307-6934,"736 Rainbow Cir, Morristown, TN 37814",https://www.google.com/maps/place/?q=place_id:ChIJDdSEsJaRW4gRnwUOeJw4DrY&hl=en,https://www.facebook.com/180paintingremodeling&more/,none,none,none,none
185,F,Tiler construction LLC,"Kissimmee, FL",(407) 686-2381,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJfyvoQNeF3YgR4HCNI2mlzts&hl=en,https://www.facebook.com/tilerconstruction,https://www.instagram.com/tilerconstruction,none,none,none
486,F,Ackerman Renovations,"Urbana, OH",(614) 619-4561,"14875 US Hwy 36, Marysville, OH 43040",https://www.google.com/maps/place/?q=place_id:ChIJn5If0Xh05EMRbLxEEcZCgAM&hl=en,https://www.facebook.com/AckermanRenovations,none,none,none,none
319,F,JGM Construction & Remodeling LLC,"Kissimmee, FL",(407) 747-2700,"3826 Bay Club Cir Unit 204, Kissimmee, FL 34741",https://www.google.com/maps/place/?q=place_id:ChIJ4_SVPZuD3YgRYzRr_SRXZ6w&hl=en,none,https://www.instagram.com/jgmconstruction.fl,none,none,none
385,F,Pick a color remodeling,"Sunrise, FL",(954) 770-7651,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJY9k3Py8J2YgRJ45ciMk585U&hl=en,none,https://www.instagram.com/remodelingwithcolor,none,Mari Casanas,none
280,F,Twisted Tile,"Paragould, AR",(870) 450-7947,"201 Gavin Dr, Paragould, AR 72450",https://www.google.com/maps/place/?q=place_id:ChIJeaOiDFfvWwQRJA6BkeUzhIQ&hl=en,https://www.facebook.com/profile.php?id=100057289195028,none,none,none,none
489,F,Escoto Tile & Remodeling LLC,"Roma, TX",(409) 454-0019,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQ2BNVOuhY2oRydp6LKMlnMY&hl=en,https://www.facebook.com/escototilepros/,none,none,none,none
575,F,Bathrooms & Kitchens by J&L Homes,"Statesville, NC",(336) 940-8272,"Winterbell Dr, Mooresville, NC 28115",https://www.google.com/maps/place/?q=place_id:ChIJ-dI7YDH_U4gRIJZrfcUqfqg&hl=en,https://www.facebook.com/kitchenandbathbyJLhomes,none,none,none,none
22,F,Murphy Kitchen and Bath Construction,"Long Valley, NJ",(908) 520-9722,"7 Rinehart Ln, Pottersville, NJ 07979",https://www.google.com/maps/place/?q=place_id:ChIJ0yhsclGRw4kRrWXbP3UgAMM&hl=en,none,https://www.instagram.com/murphykitchenandbath,none,none,none
571,F,Pedro's Custom Cabinets,"Duncan, OK",(580) 470-8436,"243 N 6th St, Duncan, OK 73533",https://www.google.com/maps/place/?q=place_id:ChIJufS7AE5brYcRogqg3XBWx-4&hl=en,https://www.facebook.com/PedrosCustomCabinets,none,none,none,none
94,F,Modern Kitchen & Bath,"Atchison, KS",(816) 646-9246,"9079 County Rd 375, St Joseph, MO 64505",https://www.google.com/maps/place/?q=place_id:ChIJKWTXdh4dwIcRWxMCBvY8ZK0&hl=en,https://www.facebook.com/modernrenovations4u,none,none,none,none
480,F,Delarosa’s refinishing,"Vineland, NJ",(856) 839-5169,"568 Mayer St, Vineland, NJ 08360",https://www.google.com/maps/place/?q=place_id:ChIJ5SeJHxxLEI0Rgvl-XtHQXso&hl=en,https://www.facebook.com/Delarosasrefinishing,https://www.instagram.com/delarosasrefinishingnj,none,none,none
493,F,TTB RESURFACING & MORE LLC,"Warner Robins, GA",(727) 966-1544,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJJ0tIYTRmKKwRZJtmCMnoEwo&hl=en,https://www.facebook.com/ttbresurfacing,https://www.instagram.com/p/CmER24LufmT/,none,Jose D. Hernandez,none
90,F,Blankenberg flooring & more llc,"Norristown, PA",(863) 877-9740,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ5zvPJWtP4KQRAjIS6iLA7FA&hl=en,https://www.facebook.com/BlankenbergFlooringmorellc,none,none,none,none
495,F,Huereca Construction LLC,"Bixby, OK",(918) 900-3621,"1100 W Tucson St, Broken Arrow, OK 74011",https://www.google.com/maps/place/?q=place_id:ChIJc1Ig1L5XVyMRpklACsHFsqg&hl=en,https://www.facebook.com/profile.php?id=100084058331628,none,none,none,none
572,F,Quality Services The King LLC,"Newberry, FL",(352) 281-9137,"136 SW 145th Dr, Newberry, FL 32669",https://www.google.com/maps/place/?q=place_id:ChIJExTqCJi_6IgRQQ7KBy5DN_c&hl=en,https://www.facebook.com/100089190222932,none,none,Javier,none
17,F,"New Creation Kitchen, Bath and Flooring","Binghamton, NY",(607) 238-0366,"800 Valley Plaza Ste 1, Johnson City, NY 13790",https://www.google.com/maps/place/?q=place_id:ChIJJ-uP-2Hv2okR3mLeBfuCbUg&hl=en,https://www.facebook.com/61579421676549,none,none,none,none
```
