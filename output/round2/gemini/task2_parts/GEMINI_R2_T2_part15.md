# Round 2: Gemini task 2, part 15 of 17 (100 businesses, rows 365 to 29)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 29: reply in that chat "Continue with
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
365,D,EG Custom Countertops LLC,"Cedartown, GA",(678) 901-7995,"1187 East Ave, Cedartown, GA 30125",https://www.google.com/maps/place/?q=place_id:ChIJLVdjco7BiogRDmYLqttY7LU&hl=en,none,none,none,none
463,D,CRC Remodeling Inc,"Lansing, IL",(219) 292-8518,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgVQR6cbfEYgRpczXo0hCtW4&hl=en,none,none,none,none
551,D,H-Tile Custom Shower Remodeling,"Cypress, TX",(832) 594-1880,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJt26wdNDnQIYRiof2O2DfHxU&hl=en,none,none,none,none
31,D,Nexgen Flooring LLC.,"Statesville, NC",(704) 957-6985,"501 Wilson St, Statesville, NC 28677",https://www.google.com/maps/place/?q=place_id:ChIJHWg9PTmpVogRQ0aLNZTHxAs&hl=en,none,none,none,none
221,D,Iron Rock Design & Build LTD.,"Downers Grove, IL",(630) 470-8410,"1202 75th St, Downers Grove, IL 60516",https://www.google.com/maps/place/?q=place_id:ChIJPyZktHxFDogRqzqCdLG57zw&hl=en,none,none,none,none
260,D,on time kitchen cabinets,"Stonecrest, GA",(404) 552-1655,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAVrMyNmDF2MRJPgfVb3GEVE&hl=en,none,none,none,none
439,D,BestPro Home improvement,"King, NC",(336) 618-1468,"1131 Roy Tuttle Rd, Pinnacle, NC 27043",https://www.google.com/maps/place/?q=place_id:ChIJRQ2oKU7CyEYRGFhcECrlNtI&hl=en,none,none,none,none
446,D,Perfix,"Waxhaw, NC",(704) 607-8062,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJfXWb27kZVIgR8U33fPgtaAQ&hl=en,none,none,none,none
496,D,Hayward Construction and Remodeling,"Bradenton, FL",(941) 526-6157,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP9xEs00Qck8Rp8ctNJb2wzY&hl=en,none,none,none,none
544,D,Cebo Remodeling,"South Milwaukee, WI",(414) 469-9909,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJixStWzoVBYgRL4qVEF8YoJA&hl=en,none,none,none,none
556,D,LUXURY REFINISHING INC,"Miramar, FL",(786) 236-4294,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJaxFEPhW72YgROy7vEw_2D68&hl=en,none,none,none,none
559,D,"Stone Specialists, LLC","Marathon, FL",(305) 923-0343,"10641 Aviation Blvd Bldg E, Marathon, FL 33050",https://www.google.com/maps/place/?q=place_id:ChIJ81Lya47b0IgRrGjflIp3cAM&hl=en,none,none,none,none
35,D,New Era Builders INC.,"Ashland, MA",(508) 782-2098,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzcPOh1F35IkRP2F-9syc9Gw&hl=en,none,none,none,none
122,D,PG Kitchen & Bath,"Weston, FL",(954) 648-1632,"13111 W Sunrise Blvd, Sunrise, FL 33323",https://www.google.com/maps/place/?q=place_id:ChIJPydPlpIK2YgR-9NkX_5_pEg&hl=en,none,none,none,none
148,D,Stronghold Custom Cabinets,"Canyon, TX",(806) 678-8885,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJY8Y4tFkJzKcRyQoerQV_mHs&hl=en,none,none,none,none
229,D,Tepaco Applications & More,"Brownsburg, IN",(317) 654-0832,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJa2K4aPOtbIgRA5t7Y9nZS2c&hl=en,none,none,none,none
266,D,Pure Form Bathrooms,"Fremont, CA",(341) 234-3362,"29000 Hesperian Blvd, Hayward, CA 94545",https://www.google.com/maps/place/?q=place_id:ChIJq0tm1ZGXj4ARE4IdmphObek&hl=en,none,none,none,none
431,D,Western Home Renovations LLC,"White Hall, AR",(210) 315-7030,"325 County Rd 3830, San Antonio, TX 78253",https://www.google.com/maps/place/?q=place_id:ChIJWww80qYcjGMRq_aeVPEIGIA&hl=en,none,none,none,none
445,D,Volcano Natural Stone LLC,"Corsicana, TX",(903) 602-5251,"302 S 7th St, Corsicana, TX 75110",https://www.google.com/maps/place/?q=place_id:ChIJXTBHv5ErT4YRAJPSdZm5SfQ&hl=en,none,none,none,none
540,D,KAS Construction Inc,"Palm Harbor, FL",(727) 935-5306,"35231 US Hwy 19 N, Palm Harbor, FL 34684",https://www.google.com/maps/place/?q=place_id:ChIJS0C3W3jtwogRbnUnYnfMEEM&hl=en,none,none,none,none
567,D,Prenga Construction LLC,"Sterling Heights, MI",(586) 623-0030,"45687 Harry St, Utica, MI 48317",https://www.google.com/maps/place/?q=place_id:ChIJE7C8lb_dJIgRrdhZn8jFy8s&hl=en,none,none,none,none
7,D,Tile of the Mountain LLC,"Highland, UT",(801) 472-4580,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJsxAvhhlqtAMRaZ-rw-ddFBM&hl=en,none,none,none,none
24,D,A Cut Above WoodWorks,"Copperas Cove, TX",(254) 813-4374,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJff4Ix1C-nGQRYd0HtfCNc54&hl=en,none,none,none,none
79,D,marcos custom designs,"Mount Lebanon, PA",(732) 527-9166,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ91jCskOhx28R3jw8jiaiYEU&hl=en,none,none,none,none
164,D,JLJ Construction LLC,"Richmond, VA",(804) 222-0900,"1760 Bickerstaff Rd, Richmond, VA 23231",https://www.google.com/maps/place/?q=place_id:ChIJLQbaCSkYsYkRTH27q1G8FPk&hl=en,none,none,none,none
175,D,Antonio's Tile,"Ypsilanti, MI",(734) 623-3274,"2770 Eastlawn Ave, Ypsilanti, MI 48197",https://www.google.com/maps/place/?q=place_id:ChIJS-bSy4ypPIgRUmh71lU0ers&hl=en,none,none,none,none
290,D,Green Country Marble,"Sapulpa, OK",(918) 322-6103,"600 W 158th St, Glenpool, OK 74033",https://www.google.com/maps/place/?q=place_id:ChIJT04XqyWZtocR7BSdFJKMt4w&hl=en,none,none,none,none
310,D,Home and Space Contracting,"Pine Hill, NJ",(856) 230-1419,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJy7uIRmWvZUARdyZcyzASaPo&hl=en,none,none,none,none
388,D,Elite Remodeling And Construction Llc,"Bradenton, FL",(941) 334-1837,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_YaLYS5zdUwR7gwOaOoZmgo&hl=en,none,none,none,none
476,D,Covenant Remodeling & Restoration,"Pekin, IL",(309) 370-6115,"2422 N 8th St, Pekin, IL 61554",https://www.google.com/maps/place/?q=place_id:ChIJVeSjz7j1CogRnjoc3Qc5Ht4&hl=en,none,none,none,none
526,D,TX Bathroom Remodel Solutions,"Monroe, OH",(512) 554-8478,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJleQsOzzVCy4Rd78E3YfZxbM&hl=en,none,none,none,none
541,D,Cabinet Refinishing Pro,"Durham, NC",(919) 548-0100,"732 9th St, Durham, NC 27705",https://www.google.com/maps/place/?q=place_id:ChIJd4zLvLXlrIkRnOIfBrvdmIM&hl=en,none,none,none,none
557,D,Aftemar Home Gallery,"Doral, FL",(305) 599-0775,"2805 NW 79th Ave, Doral, FL 33122",https://www.google.com/maps/place/?q=place_id:ChIJw-MTcHe52YgRTyP7aMSHN2w&hl=en,none,none,none,none
569,D,The Tile Dad NC,"Lincolnton, NC",(704) 530-6161,"1053 Creekside Dr, Lincolnton, NC 28092",https://www.google.com/maps/place/?q=place_id:ChIJA3nXf7PPVogRx2FJs5BsSTs&hl=en,none,none,none,none
25,D,"T & R Contracting, LLC","Bellmawr, NJ",(856) 673-6548,"314 Plantation Drive, Cinnaminson, NJ 08077",https://www.google.com/maps/place/?q=place_id:ChIJkWMGtyjMxokR8gdbCkkAcVc&hl=en,none,none,none,none
153,D,F&G Granite,"Elizabethton, TN",(423) 747-4966,"2711 Elizabethton Hwy 91, Johnson City, TN 37601",https://www.google.com/maps/place/?q=place_id:ChIJmcoDUFt-WogRVezM3l656G4&hl=en,none,none,none,none
243,D,Bathroom and Kitchen Remodeling Panorama City,"San Fernando, CA",(818) 960-6627,"14650 Roscoe Blvd, Panorama City, CA 91402",https://www.google.com/maps/place/?q=place_id:ChIJg2f6qFaWwoARhQz2P8ezHGA&hl=en,none,none,none,none
245,D,JJ Tile and Stone,"Stoneham, MA",(617) 438-3116,"76 Maple St, Stoneham, MA 02180",https://www.google.com/maps/place/?q=place_id:ChIJiSzNeb3zsCMRcI5_dBt3VHM&hl=en,none,none,none,none
383,D,PTC Remodeling & Construction,"Seagoville, TX",(469) 512-5805,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ3YoHc2Kfa0sRo0OEyd-DFjg&hl=en,none,none,none,none
461,D,CML Tiling & Cleaning Services LLC,"Bexley, OH",(614) 806-0290,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJjX9oUHSJOIgR4Xogx7cbHss&hl=en,none,none,none,none
508,D,ZOCO Construction LLC,"Freeport, FL",(850) 750-2115,"19 Freeport Marina Blvd, Freeport, FL 32439",https://www.google.com/maps/place/?q=place_id:ChIJLTOY15xZkYgR0L43YfICl5k&hl=en,none,none,none,none
529,D,Las Vegas Kitchen Remodeling Pros,"Las Vegas, NV",(702) 725-0018,"5080 E Judson Ave, Las Vegas, NV 89115",https://www.google.com/maps/place/?q=place_id:ChIJMcWtofnnyIARye6OcL5T3WM&hl=en,none,none,none,none
542,D,By The Sea Bathroom Remodeling of Dana Point,"San Juan Capistrano, CA",(949) 628-0820,"34162 Doheny Park Rd, Dana Point, CA 92624",https://www.google.com/maps/place/?q=place_id:ChIJ5QU73xHx3IARzvr1pfFgyP0&hl=en,none,none,none,none
13,D,Keegan Consultants LLC,"Athens, GA",(706) 296-9515,"4273 Lebanon Church Rd, Athens, GA 30607",https://www.google.com/maps/place/?q=place_id:ChIJcf1l740N9ogR8XYoobnIluA&hl=en,none,none,none,none
61,D,Custombilt Counter Tops,"Waycross, GA",(912) 283-5704,"1822 Albany Ave, Waycross, GA 31503",https://www.google.com/maps/place/?q=place_id:ChIJbTowhqn674gRhZrLYxQMw8g&hl=en,none,none,none,none
151,D,Loma Remodeling Services LLC,"Goodyear, AZ",(623) 703-3777,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpya_crzZ1IAR3WkDRe7QzLA&hl=en,none,none,none,none
173,D,CNG Construction Inc,"Kenmore, NY",,"33 Traymore St, Buffalo, NY 14216",https://www.google.com/maps/place/?q=place_id:ChIJL5TKmiFt04kR3TYix_lbNLY&hl=en,none,none,none,none
411,D,Melling Granite & More,"Cedar City, UT",(435) 867-0099,"260 N Westview Dr, Cedar City, UT 84720",https://www.google.com/maps/place/?q=place_id:ChIJ7TvD-aNhtYARi-iZaLA6TOg&hl=en,none,none,none,none
473,D,Tru Grit Renovations,"Poteau, OK",(918) 208-7690,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ46T3uc0cQmAR1kZ0VQ34-yA&hl=en,none,none,none,none
560,D,Consider it Done!,"Garden Ridge, TX",(830) 832-8889,"10724 Dedeke Dr, New Braunfels, TX 78132",https://www.google.com/maps/place/?q=place_id:ChIJj8IrFV29XIYRcV61V9KbGcQ&hl=en,none,none,none,none
33,D,Creative Additions Plus,"East Bethel, MN",(612) 685-5314,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDQG1UPsXs1IRSHeiAQnvpsQ&hl=en,none,none,none,none
158,D,H&R Remodeling LLC NOLA,"Metairie, LA",,"3809 Green Acres Rd, Metairie, LA 70003",https://www.google.com/maps/place/?q=place_id:ChIJdZDUrGQsTK8Rx7_g5Zyoxf4&hl=en,none,none,none,none
299,D,Jocelyn Pankey Cabinetry & Design,"Clinton, IA",(309) 236-2235,"104 E 6th St, DeWitt, IA 52742",https://www.google.com/maps/place/?q=place_id:ChIJKfhzaOxT4ocRn13Gj3xeMFw&hl=en,none,none,none,none
311,D,Renew Space Remodeling,"Alameda, CA",(341) 234-3035,"2489 Industrial Pkwy W, Hayward, CA 94545",https://www.google.com/maps/place/?q=place_id:ChIJC0xSqJeXj4ARsQNAqJJUVBo&hl=en,none,none,none,none
322,D,"Better Edge Tile & Remodeling, LLC","Maple Grove, MN",(612) 978-3569,"8371 Norwood Ln N, Maple Grove, MN 55369",https://www.google.com/maps/place/?q=place_id:ChIJOyTuFjw6s1IR2sLgGdQgy0M&hl=en,none,none,none,none
420,D,M&G Renovations LLC,"Thomasville, NC",(336) 255-5629,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTXrbq9bLR0oRD9Xj_T_aV9A&hl=en,none,none,none,none
429,D,Forney Home Services,"Mount Juliet, TN",(872) 248-4243,"2401 S Mt Juliet Rd, Mt. Juliet, TN 37122",https://www.google.com/maps/place/?q=place_id:ChIJqbK5mzZuSoQRhqjNBH2ps9E&hl=en,none,none,none,none
443,D,FL Bathroom Remodel,"Sedro-Woolley, WA",(786) 863-1969,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJST8ZMO5BRkcR5XJk4EP-CcQ&hl=en,none,none,none,none
462,D,Ceramic Tile Designer LLC,"Slidell, LA",(504) 382-0628,"529 Evergreen Dr, Slidell, LA 70460",https://www.google.com/maps/place/?q=place_id:ChIJR3ooUqrlnYgRCYnh7htohmY&hl=en,none,none,none,none
506,D,NEPA Remodeling,"Scranton, PA",(570) 650-6372,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ2RVVwGUgxYkRWpR0vqSlXvQ&hl=en,none,none,none,none
515,D,Novo Kitchen & Bath,"Lancaster, NY",(516) 731-7888,"3296 Merrick Rd, Wantagh, NY 11793",https://www.google.com/maps/place/?q=place_id:ChIJPSg_jWt_wokR0eSeN1YPJkE&hl=en,none,none,none,none
566,D,Aigle Remodelation LLC,"Skiatook, OK",(918) 760-5439,"6313 N Main St 6313 N, Tulsa, OK 74126",https://www.google.com/maps/place/?q=place_id:ChIJIaWoLcHptocRkivokt6FjXQ&hl=en,none,none,none,none
52,D,3J GRANITE LLC,"Salem, VA",(540) 556-0927,"726 Roanoke St, Salem, VA 24153",https://www.google.com/maps/place/?q=place_id:ChIJO6bFbOQJTYgRHLX3G2fNFyA&hl=en,none,none,none,none
105,D,"PR Quality Construction, LLC","Pacific, WA",(206) 437-4300,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXcmAaH8yvKgRorwDNuPvyYo&hl=en,none,none,none,none
129,D,Home Team Professionals,"Franklin, NH",(508) 960-5692,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJb-XapZH_howRiXqN9NCcV9M&hl=en,none,none,none,none
155,D,C&K Beachside Remodeling LLC,"Indian Harbour Beach, FL",(321) 426-5073,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgX_PAgpwA44RtWQunoNQAbk&hl=en,none,none,none,none
156,D,Sioux City Painting Pros,"South Sioux City, NE",(712) 317-7752,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJwdmtBwqkN0YRn0MgVDL69Hg&hl=en,none,none,none,none
168,D,Piedmont Bay Harbor Remodeling,"Piedmont, CA",(415) 843-7559,"5 Sandringham Pl, Piedmont, CA 94611",https://www.google.com/maps/place/?q=place_id:ChIJo-WMKfKHj4ARpHO4US0ls_I&hl=en,none,none,none,none
194,D,"DREAM KITCHEN and COUNTERTOP, INC","North Salt Lake, UT",(801) 809-9199,"100 N 700 W Suite B, North Salt Lake, UT 84054",https://www.google.com/maps/place/?q=place_id:ChIJaUh7jB_3UocRSHvTloFCJjw&hl=en,none,none,none,none
200,D,Pro Touch Kitchen and Bath Remodeling,"West New York, NJ",(201) 449-8639,"333 Bergen Blvd, Fairview, NJ 07022",https://www.google.com/maps/place/?q=place_id:ChIJf_RLRir-f0kRiP0EAAxzBbY&hl=en,none,none,none,none
249,D,Aser's home remodeling,"Manitou Springs, CO",(719) 722-6831,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJicWZnwJFE4cRw4B1EhnKIaM&hl=en,none,none,none,none
253,D,Construction Pros,"Edina, MN",(612) 396-5216,"7401 Metro Blvd Ste 500, Edina, MN 55439",https://www.google.com/maps/place/?q=place_id:ChIJe73SYarV94cRoGyX2F-WN9w&hl=en,none,none,none,none
257,D,Miller Remodeling,"Elkhart, IN",(574) 596-1476,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMzUkao2NFogRU4JYmJWoe9Y&hl=en,none,none,none,none
298,D,Korte Tile & Remodel,"Hendersonville, TN",(615) 330-5528,"108 Deerwood Dr, Hendersonville, TN 37075",https://www.google.com/maps/place/?q=place_id:ChIJy5wZeGFJZIgRyWBIOL3ubAE&hl=en,none,none,none,none
304,D,Wolfson Construction,"Camden, NJ",(856) 952-3700,"204 W Cedar Ave, Oaklyn, NJ 08107",https://www.google.com/maps/place/?q=place_id:ChIJ6WG2w9zPxokRkx8Ou8aGDf4&hl=en,none,none,none,none
307,D,First Class Concept Design & Remodel,"Inverness, FL",(352) 287-9262,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJeRASRSmss6wRfa3ZInzkDok&hl=en,none,none,none,none
312,D,Morenos Custom Cabinets,"Madera, CA",(559) 416-2084,"17919 Baldwin St #102, Madera, CA 93638",https://www.google.com/maps/place/?q=place_id:ChIJO-mJqZcJlIAR-r36MrwWq6I&hl=en,none,none,none,none
318,D,Absolute Home Solutions LLC,"Mauldin, SC",(864) 704-2678,"Mauldin, SC 29662",https://www.google.com/maps/place/?q=place_id:ChIJ1Zk-oNklWIgRB45U02jzN6o&hl=en,none,none,none,none
435,D,Gracy Cabinets,"Lavon, TX",(972) 843-3123,"10963 State Hwy 205, Lavon, TX 75166",https://www.google.com/maps/place/?q=place_id:ChIJN-vCHtIGTIYRVh1FvNKSa4o&hl=en,none,none,none,none
460,D,"Easy's Granite, LLC.","Moxee, WA",(509) 759-5153,"109 N Iler St, Moxee, WA 98936",https://www.google.com/maps/place/?q=place_id:ChIJq_WqI9HVmVQRRh1O9yT-8H8&hl=en,none,none,none,none
466,D,Sowela's Construction LLC,"Elkhart, IN",(574) 217-1968,"Osolo Rd, Elkhart, IN 46514",https://www.google.com/maps/place/?q=place_id:ChIJu2i8QyvdFogROBYSCFHUqNQ&hl=en,none,none,none,none
470,D,3rd Generation Building and Design,"Cupertino, CA",(408) 834-2318,"21701 Stevens Creek Blvd, Cupertino, CA 95015",https://www.google.com/maps/place/?q=place_id:ChIJteizWBYnyacRgdNCxlvww5c&hl=en,none,none,none,none
477,D,A&A Cabinets And Stone,"Oak Park, MI",(248) 965-2172,"21641 Meyers Rd, Oak Park, MI 48237",https://www.google.com/maps/place/?q=place_id:ChIJqVO8vNLPJIgRnyjhE-L2yJM&hl=en,none,none,none,none
513,D,Enid Cabinetry and Woodwork,"Enid, OK",(580) 747-2983,"1026 Kline Cir, Enid, OK 73701",https://www.google.com/maps/place/?q=place_id:ChIJjQ9xda1eN2gRRBRKUpF_g-0&hl=en,none,none,none,none
532,D,Kitchen & Bath Remodeling LA,"Culver City, CA",(323) 657-6022,"8954 Ellis Ave #8954, Los Angeles, CA 90034",https://www.google.com/maps/place/?q=place_id:ChIJibCYrBO5woARGM78TjzGNnY&hl=en,none,none,none,none
533,D,Home Investment Solutions LLC,"Clover, SC",(803) 818-1204,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJYcuRTT_tVogRSIeh8k7f2rY&hl=en,none,none,none,none
535,D,Strong Renovations,"Sumner, WA",(206) 240-2550,"6526 193rd Ave E, Bonney Lake, WA 98391",https://www.google.com/maps/place/?q=place_id:ChIJ7c7Ymi_7kFQRKjLWDusILPs&hl=en,none,none,none,none
38,D,"Jobak Home Improvement, LLC","Clarkston, MI",(248) 606-0150,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv6eI7U0bEw8R7Xnk6disLBk&hl=en,none,none,none,none
63,D,New Style Tiles,"Midlothian, IL",(708) 698-0090,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJE_Pezpw9DogRpCnedN8M5w0&hl=en,none,none,none,none
98,D,Fix Plus,"Clermont, FL",(352) 242-4330,"121 W Washington St, Minneola, FL 34715",https://www.google.com/maps/place/?q=place_id:ChIJ3eg570SO54gRRkdCF036GFU&hl=en,none,none,none,none
125,D,DIMITRI CONSTRUCTION & REMODELING LLC,"Wheaton, IL",(630) 808-2916,"1691 Valley Forge Ct, Wheaton, IL 60189",https://www.google.com/maps/place/?q=place_id:ChIJe2Ekt_w5BycRva-NYwrCzVs&hl=en,none,none,none,none
126,D,Hall of Fame Home Renovations,"Seven Hills, OH",(440) 781-2740,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJO4wHOHqEA0QRMafvve9D22A&hl=en,none,none,none,none
288,D,Lovell Homes LLC,"West Haven, UT",(801) 678-9455,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJfapO-uqu-ogRcVlOWTzN60w&hl=en,none,none,none,none
301,D,All City Renovations,"Maple Heights, OH",(216) 318-8327,"4890 E 49th St, Cuyahoga Heights, OH 44125",https://www.google.com/maps/place/?q=place_id:ChIJubbMM2-Y8y4RwGIguoj0hYA&hl=en,none,none,none,none
354,D,Victor Smith's Construction,"Edina, MN",(952) 412-4147,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJBw-FOQ9o7qMRnlNfDRC5jxE&hl=en,none,none,none,none
430,D,Deluxe Renovations & Services,"Haines City, FL",(561) 305-5895,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDxuQE1nyQqwR553JeQXKzYw&hl=en,none,none,none,none
449,D,Repair Remodel Contractors LLC,"Salem, OR",(503) 302-3653,"3895 Tulare Ave S, Salem, OR 97302",https://www.google.com/maps/place/?q=place_id:ChIJS5d_wMvqXIERZSRcqBlm1L8&hl=en,none,none,none,none
450,D,Saba Home Remodeling LLC,"Round Rock, TX",(512) 200-8002,"2924 Winchester Dr, Round Rock, TX 78665",https://www.google.com/maps/place/?q=place_id:ChIJ-21-NpDRRIYRMfbj2Q4zphI&hl=en,none,none,none,none
4,D,G Remodeling Services Llc,"Kennedale, TX",(682) 248-2703,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJX8ojzveJToYR2ddcxdh6pEs&hl=en,none,none,none,none
29,D,Signature Bath Solutions,"Union City, CA",(341) 234-2966,"4447 Alice Way, Union City, CA 94587",https://www.google.com/maps/place/?q=place_id:ChIJeznhMDuVj4ARqnP0yzIbWg4&hl=en,none,none,none,none
```
