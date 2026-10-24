# Round 2: Gemini task 2, part 14 of 17 (100 businesses, rows 2384 to 294)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 294: reply in that chat "Continue with
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
2384,C,Refinement Remodeling & Design,"Goose Creek, SC",(203) 260-1733,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJixDcqqY5cyoRBd_YUZV3q8k&hl=en,none,none,none,none
2385,C,Georgia Granite Countertops,"Rome, GA",(352) 215-3819,"2520 Shorter Ave NW, Rome, GA 30165",https://www.google.com/maps/place/?q=place_id:ChIJ8XMI1fajiogR4EWXb6Ffngk&hl=en,none,none,none,none
2386,C,Sam's Cabinets Inc.,"Salisbury, NC",(704) 754-0096,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6YeCUvqLU4gRmP_mxP46FYI&hl=en,none,none,none,none
2387,C,B & B Cabinet & Trim,"Lufkin, TX",(936) 632-5743,"2864 FM325, Lufkin, TX 75901",https://www.google.com/maps/place/?q=place_id:ChIJN38z0L88OIYRo2ptWz-1WzY&hl=en,none,none,none,none
2388,C,DNB Remodeling - Bathrooms & Kitchens,"Meridian, ID",(208) 859-8291,"2020 S Luxury Ln h106, Meridian, ID 83642",https://www.google.com/maps/place/?q=place_id:ChIJpyu6PkhRrlQR22t_s4xmst8&hl=en,none,none,none,none
2389,C,"H&A Remodeler | Home, Deck & Kitchen Remodeling North End","Boise, ID",(208) 469-2691,"1515 N 13th St, Boise, ID 83702",https://www.google.com/maps/place/?q=place_id:ChIJ5yWIiiz5rlQRXwpJiXqZqpQ&hl=en,none,none,none,none
2390,C,Danisil Corp.,"Ozark, AL",(334) 498-8040,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJoy-YfPAvc64Rzwn2-E5HD_0&hl=en,none,none,none,none
2391,C,Mertz Family Homes,"Manhattan, KS",(785) 251-3050,"1701 Cassell Rd, Manhattan, KS 66502",https://www.google.com/maps/place/?q=place_id:ChIJ74XNKJMV_EIRuQ-aFe-fXYo&hl=en,none,none,none,none
2392,C,"DC Remodeling & Construction,LLC","Boerne, TX",(210) 328-9924,"726 FM474, Boerne, TX 78006",https://www.google.com/maps/place/?q=place_id:ChIJIbRVvTjHW2kRgb0t1fKXI8U&hl=en,none,none,none,none
2393,C,Victor's Granite & Tile,"Ukiah, CA",(707) 462-9640,"275 E Kunzler Ranch Rd, Ukiah, CA 95482",https://www.google.com/maps/place/?q=place_id:ChIJ3Q70jgtkgYARB4HiQp1a8fw&hl=en,none,none,none,none
2394,C,Grouted Tile And Flooring,"Williston, ND",(228) 229-4846,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhc_75SbfD28RHytAgzz7EjA&hl=en,none,none,none,none
2395,C,"Walter Allen Custom Kitchens, LLC","Brooksville, FL",(352) 544-8120,"16335 Tampa St, Brooksville, FL 34604",https://www.google.com/maps/place/?q=place_id:ChIJhbiE-T4c6IgRZs-GaP2lh5E&hl=en,none,none,none,none
2396,C,Almaraz Remodeling LLC,"Denver, CO",(720) 581-4619,"1755 S Beeler St, Denver, CO 80247",https://www.google.com/maps/place/?q=place_id:ChIJxY9FR-UOAUoRzk8dRifikJA&hl=en,none,none,none,none
2397,C,Kitchen and Bath Drawings..,"Maricopa, AZ",(844) 752-1614,"18851 N Arbor Dr, Maricopa, AZ 85138",https://www.google.com/maps/place/?q=place_id:ChIJH306jvf7KocRX4UZjgWGt8M&hl=en,none,none,none,none
2398,C,Coffee Talk Kitchens,"Hopatcong, NJ",(973) 598-1414,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6fmvdux1w4kR9_xQ5zz4qaQ&hl=en,none,none,none,none
2399,C,Hercules Granite & Remodel,"Great Falls, VA",(571) 699-6838,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJk-LhpaeAtqQRee4kEl5BV0Y&hl=en,none,none,none,none
255,D,S&A Excellence Kitchen Remodeling,"Laguna Woods, CA",(657) 236-3305,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJlfg16sb6zUoRb1DfS5oeYNU&hl=en,none,none,none,none
419,D,Leonardo’s Enterprise Granite,"Enterprise, AL",(334) 489-4067,"301 E Lee St, Enterprise, AL 36330",https://www.google.com/maps/place/?q=place_id:ChIJ7S0mI5BukogRIq1nB5x3ep4&hl=en,none,none,none,none
554,D,"Wrightway Home Remodeling, LLC","Norfolk, VA",(757) 375-3051,"1023 Fishermans Rd, Norfolk, VA 23503",https://www.google.com/maps/place/?q=place_id:ChIJgS_c1OCRuokRpXJy1EAB-Qc&hl=en,none,none,none,none
413,D,Steve Rossino Remodeling & Carpentry,"Gloucester City, NJ",(609) 230-3166,"10 Cat Briar Ct, Sicklerville, NJ 08081",https://www.google.com/maps/place/?q=place_id:ChIJRxAvyIHTxokRFUjs4cC7aOc&hl=en,none,none,none,none
433,D,Jrs Home Improvement,"Crystal Lake, IL",(815) 217-8800,"821 Perry Dr, Algonquin, IL 60102",https://www.google.com/maps/place/?q=place_id:ChIJeznTf6dxD4gRqiXCZubgBes&hl=en,none,none,none,none
522,D,JMC Luxury Countertops LLC,"Burlington, NC",(336) 437-3953,"106 W Hanover Rd, Graham, NC 27253",https://www.google.com/maps/place/?q=place_id:ChIJF0o8g5ErU4gRVeXY-STmRtc&hl=en,none,none,none,none
118,D,Veteran Tile Works,"Beaumont, CA",(909) 561-7249,"1001 Palm Ave, Beaumont, CA 92223",https://www.google.com/maps/place/?q=place_id:ChIJmQoAr9wxw4ARhf0Qrd92uqk&hl=en,none,none,none,none
159,D,HomePride Bath,"Manitou Springs, CO",(719) 286-5215,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ47MluLRPE4cRKcSOlVqwefw&hl=en,none,none,none,none
220,D,Paul the Tileman LLC,"Country Club Hills, IL",(773) 877-0071,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJJzDPoCEXDogRHScmRhtwKMk&hl=en,none,none,none,none
248,D,HomePride Bath,"Edgewater, CO",(720) 770-7944,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDVb6lzyBa4cRUmDm_tafwiY&hl=en,none,none,none,none
321,D,Hopkins Renovation & Design,"Atlanta, GA",(404) 563-9716,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJo6QFhIAf9YgR9gFj9By10_E&hl=en,none,none,none,none
517,D,Dr. Cabinet NYC,"Englewood, NJ",(917) 338-9617,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJCXqUxPePt6YRP4GgklaaXmg&hl=en,none,none,none,none
265,D,Top Dawg Remodel LLC,"Yuma, AZ",(213) 448-4035,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ44mSRJ4VZwYRyaxw32LtNxc&hl=en,none,none,none,none
408,D,Distinguished Home LLC | DBA Madison Cabinets,"Salt Lake City, UT",(801) 887-7277,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ03B9FCPzUocRIma-T7vI3yQ&hl=en,none,none,none,none
457,D,Elegant Stone & Cabinet,"Pomona, CA",(909) 594-0455,"690 S Reservoir St, Pomona, CA 91766",https://www.google.com/maps/place/?q=place_id:ChIJsXNxLeiWwoARhdGUgQVOBMA&hl=en,none,none,none,none
62,D,Raccoon Stone & Tile Works,"Fort Valley, GA",(478) 956-2222,"2347 GA-247CONN, Byron, GA 31008",https://www.google.com/maps/place/?q=place_id:ChIJ-ZisyzXm84gRug4KD2uOJak&hl=en,none,none,none,none
117,D,My Bathroom Remodel Of Oakland.,"Alameda, CA",(415) 991-3613,"2450 W 14th St, Oakland, CA 94607",https://www.google.com/maps/place/?q=place_id:ChIJFSS9hBaBj4ARdwg7b1NmBbw&hl=en,none,none,none,none
121,D,Renovations F&W,"Kissimmee, FL",(321) 290-2884,"2802 E Irlo Bronson Memorial Hwy, Kissimmee, FL 34744",https://www.google.com/maps/place/?q=place_id:ChIJ419031OKJKER3EaZQ5pf1zs&hl=en,none,none,none,none
154,D,Artisan Tile,"Big Bear Lake, CA",(909) 900-5095,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ3Rn8Ebi1xIARemqVFUBvvw4&hl=en,none,none,none,none
226,D,Hand Remodeling,"Prattville, AL",(334) 440-4216,"1158 Josephine Ave, Prattville, AL 36066",https://www.google.com/maps/place/?q=place_id:ChIJ0XhgEjxTFwARaOqbjYv6q8I&hl=en,none,none,none,none
458,D,INFINITY,"Davenport, FL",(516) 590-9208,"1496 Eucalyptus Wy, Davenport, FL 33837",https://www.google.com/maps/place/?q=place_id:ChIJb5b8-WBx3YgRmsYahFvkem4&hl=en,none,none,none,none
216,D,Express Baths & Glass,"Garner, NC",(919) 661-4262,"9141 Sauls Rd, Raleigh, NC 27603",https://www.google.com/maps/place/?q=place_id:ChIJI0YjHQ1grIkRTxxd9MAwr3U&hl=en,none,none,none,none
412,D,GB Tile,"Wallington, NJ",(201) 898-4432,"110 Halstead Ave, Wallington, NJ 07057",https://www.google.com/maps/place/?q=place_id:ChIJAdDmayj5wokR_bjjFSdXPyM&hl=en,none,none,none,none
452,D,Cook House Kitchen Remodeling,"Beverly Hills, CA",(424) 404-5674,"623 N Rexford Dr, Beverly Hills, CA 90210",https://www.google.com/maps/place/?q=place_id:ChIJW6E1DZO9woAROxeWZrAhd0w&hl=en,none,none,none,none
224,D,LuxeBasin Bathroom Remodeler,"Pasadena, CA",(626) 669-3164,"1008 Bell St, Pasadena, CA 91104",https://www.google.com/maps/place/?q=place_id:ChIJM47wVhzDwoARQiNOpTQNvi4&hl=en,none,none,none,none
239,D,Full House Kitchen Remodeling,"The Woodlands, TX",(832) 810-7817,"2001 Timberloch Pl Ste 409, The Woodlands, TX 77380",https://www.google.com/maps/place/?q=place_id:ChIJVQ6-Y443R4YRtQ7jZtnEBeY&hl=en,none,none,none,none
326,D,Continental Wood and Stone Company,"Defiance, OH",(419) 789-9765,"919 Grove St, Defiance, OH 43512",https://www.google.com/maps/place/?q=place_id:ChIJRd0cVpHRPYgRHy6row9OrAE&hl=en,none,none,none,none
393,D,THE THREE BROTHERS GENERAL REMODELING,"Angleton, TX",(832) 656-9041,"2609 S Front St, Angleton, TX 77515",https://www.google.com/maps/place/?q=place_id:ChIJ-5suwqJdQIYRVTnp_swBAt8&hl=en,none,none,none,none
15,D,Jota Handyman Remodeling LLC,"Roselle, IL",(312) 586-6495,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJtwjg8zJ6riIRmnl_ANJAtfk&hl=en,none,none,none,none
244,D,ToughTop Bathroom Remodeling,"Imperial, CA",(323) 455-2415,"200 W 99th St, Los Angeles, CA 90003",https://www.google.com/maps/place/?q=place_id:ChIJG-ixhPrJwoARp5eSg4-0sLg&hl=en,none,none,none,none
331,D,Aesthetics Cabinetry LLC,"DeLand, FL",(386) 320-2806,"1510 Old Daytona Cir, DeLand, FL 32724",https://www.google.com/maps/place/?q=place_id:ChIJxVlofXEd54gROjGwg0wJJA0&hl=en,none,none,none,none
347,D,CK Tile and Home Repair LLC,"Crystal, MN",(952) 356-7295,"6530 57th Ave N, Minneapolis, MN 55428",https://www.google.com/maps/place/?q=place_id:ChIJpfecVL83s1IRjPur556CnvQ&hl=en,none,none,none,none
428,D,"MIAMI KITCHENS & BATHS, INC.","Cutler Bay, FL",(786) 759-7294,"12451 SW 203rd Terrace, Miami, FL 33177",https://www.google.com/maps/place/?q=place_id:ChIJ8cnp4wPD2YgRqrAYgxo7Cas&hl=en,none,none,none,none
40,D,New Life Home Improvements,"Fort Pierce, FL",(786) 303-0559,"5006 Elm Ave, Fort Pierce, FL 34982",https://www.google.com/maps/place/?q=place_id:ChIJy15awGLv3ogRlBEcBt65Rrc&hl=en,none,none,none,none
76,D,"White's Quality Homes and Remodeling, LLC","Farmington, MO",(573) 880-2488,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpWJLneNF2IcRyEKTzsKcdZo&hl=en,none,none,none,none
217,D,Edward Walker Home Improvement,"Bucyrus, OH",(567) 370-9583,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJJSvgft_rOYgRbuLWyC_jgOM&hl=en,none,none,none,none
287,D,Siana Remodeling LLC,"Denham Springs, LA",(225) 288-9786,"28257 Gaylord Rd, Walker, LA 70785",https://www.google.com/maps/place/?q=place_id:ChIJ9fkqFFSjJoYRVTIZAGL4QPQ&hl=en,none,none,none,none
124,D,"Modern Tile & Design, LLC","Fuquay-Varina, NC",(919) 696-1384,"Whitted Rd, Fuquay-Varina, NC 27526",https://www.google.com/maps/place/?q=place_id:ChIJK2CGTuiPrIkRdc_B_aJMKY0&hl=en,none,none,none,none
403,D,RD&CS,"Clarksville, IN",(651) 802-8519,"8098 Hynes Ave S, Cottage Grove, MN 55016",https://www.google.com/maps/place/?q=place_id:ChIJvZQ3T9zb94cRh_QOEYoizAw&hl=en,none,none,none,none
500,D,Gladden Remodeling Bath & Kitchen LLC,"Riverdale, UT",(713) 201-5851,"21435 Park Villa Dr, Katy, TX 77450",https://www.google.com/maps/place/?q=place_id:ChIJOZyX_LUgQYYR4mVQWn334PE&hl=en,none,none,none,none
562,D,Allied Countertops and Cabinets,"Visalia, CA",(559) 713-6582,"9745 W Grove Ave, Visalia, CA 93291",https://www.google.com/maps/place/?q=place_id:ChIJzcfooucnlYAR3G4scCuOSjk&hl=en,none,none,none,none
71,D,Graphene Stone Home Repairs LLC,"Hialeah, FL",,"4577 W 13th Ln, Hialeah, FL 33012",https://www.google.com/maps/place/?q=place_id:ChIJdRIkNHC72YgRJ1kQ0vX3vxk&hl=en,none,none,none,none
128,D,MVP Remodeling & Painting,"Downers Grove, IL",(312) 342-0669,"1071 Candlewood Dr, Downers Grove, IL 60515",https://www.google.com/maps/place/?q=place_id:ChIJpWCjb0qV04QRnsbxkWjFCG0&hl=en,none,none,none,none
340,D,Los Álvarez y Reyes Floor Service,"Balch Springs, TX",(972) 876-5474,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ79FxlQg-GqkRHLJqP5SDV1Q&hl=en,none,none,none,none
409,D,Sloan Stone/ south coast stone,"Victoria, TX",(361) 572-8498,"2498 Guadalupe Rd, Victoria, TX 77905",https://www.google.com/maps/place/?q=place_id:ChIJy_GpQItlQoYRz6my6Rj2H5U&hl=en,none,none,none,none
543,D,R3J Residential Services - Remodeling & Renovations,"Woodburn, OR",(503) 516-4507,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJifk7UHNllVQRHc1Zp8pp8WU&hl=en,none,none,none,none
267,D,Diamond Bathroom Remodeling,"Simi Valley, CA",(820) 502-2226,"2160 Connell Ave, Simi Valley, CA 93063",https://www.google.com/maps/place/?q=place_id:ChIJT7mL2_Mp6IARyCYppp9jah4&hl=en,none,none,none,none
269,D,Prestige Custom Stone,"Crown Point, IN",(219) 661-8335,"665 Madison St, Crown Point, IN 46307",https://www.google.com/maps/place/?q=place_id:ChIJJdw31zLuEYgRLnYrmxHAqtA&hl=en,none,none,none,none
348,D,Flavor Point Kitchen Remodeling,"Port Hueneme, CA",(805) 457-9990,"2034 Ravoli Dr, Oxnard, CA 93035",https://www.google.com/maps/place/?q=place_id:ChIJ9bgP2ENP6IARKwG1BcBPi-E&hl=en,none,none,none,none
511,D,Aguilar & Son Inc.,"Fletcher, NC",(828) 962-2092,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbzUHDhCmvwQRcy-q7XNZRig&hl=en,none,none,none,none
44,D,A French Handyman,"West Lafayette, IN",(765) 236-6669,"180 Glenn Ct, West Lafayette, IN 47906",https://www.google.com/maps/place/?q=place_id:ChIJdRauMxExdYgRSmKTERh5Yc0&hl=en,none,none,none,none
89,D,"Kapal Cabinets, Granite & Quartz","Brownsville, TX",(956) 461-0692,"2025 N Minnesota Ave, Brownsville, TX 78521",https://www.google.com/maps/place/?q=place_id:ChIJ0XA-rTC_b4YRDbH-L5b092s&hl=en,none,none,none,none
345,D,V&M Granite and Remodeling LLC,"Seagoville, TX",(214) 974-1515,"2741 US-175 Frontage Rd, Seagoville, TX 75159",https://www.google.com/maps/place/?q=place_id:ChIJu0L7IQm7ToYRYF9Wp0pDqhs&hl=en,none,none,none,none
371,D,"RS Construction Solutions-kitchen,bathroom remodeler/excavation","Hermitage, PA",(724) 456-3396,"3871 Saranac Dr, Sharpsville, PA 16150",https://www.google.com/maps/place/?q=place_id:ChIJccZaGbfQEqIR-QkEnIpAc60&hl=en,none,none,none,none
472,D,Jay's Home Improvement,"Huntsville, AL",(256) 945-2548,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJja101ZNrYogR8144Ftw2PGM&hl=en,none,none,none,none
510,D,Master Kitchen & Bath,"Pembroke Park, FL",(954) 699-3229,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJp5qM-iCDAWERs0tdDJq_ims&hl=en,none,none,none,none
528,D,Fresh Horizon Kitchen Remodeling,"Pasadena, CA",(626) 663-3509,"244 N Oakland Ave, Pasadena, CA 91101",https://www.google.com/maps/place/?q=place_id:ChIJJ3vUkPLDwoARVV0aqZPr-0Q&hl=en,none,none,none,none
565,D,Rethink Creative,"Clarksville, TN",(678) 899-2594,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGbJ0s4ZcuWkRBOhJXJU1qOQ&hl=en,none,none,none,none
53,D,The Tile Pro's,"Clemmons, NC",(336) 995-7102,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJFYYNGXWxU4gR3DGr792aPYw&hl=en,none,none,none,none
137,D,Atlantic Home Improvement Inc,"Ocean City, MD",,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJyff2kUL6t4kR3jeaWevyRPw&hl=en,none,none,none,none
144,D,Columbus Counter Tops,"Columbus, MS",(662) 327-8677,"3546 MS-50, Columbus, MS 39702",https://www.google.com/maps/place/?q=place_id:ChIJwaz7AXfuhogRkxnLMjadyKE&hl=en,none,none,none,none
197,D,Sierra Home Remodel LLC,"La Porte, IN",(219) 455-9017,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJH7GqSKVnyykRQm15NZ4Qc-E&hl=en,none,none,none,none
218,D,"K & K REMODELING, INC.","Plymouth, MI",(248) 476-0816,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJyVbpysmzJIgR_g7X6_tXrfg&hl=en,none,none,none,none
289,D,Dikici Design Consultants,"Ennis, TX",(760) 792-3509,"315 S Rogers St #4, Waxahachie, TX 75165",https://www.google.com/maps/place/?q=place_id:ChIJxwKolp3ZTYYRbi15anXmwoo&hl=en,none,none,none,none
315,D,Carrara Kitchen Countertops,"Marlborough, MA",(508) 579-5857,"729 Farm Rd Ste H, Marlborough, MA 01752",https://www.google.com/maps/place/?q=place_id:ChIJL8mIqzjzAWMRtR03Xa9GQNA&hl=en,none,none,none,none
527,D,Creese Management Inc.,"Aliquippa, PA",(724) 462-0291,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJR85t4eDJG6oRRSufjpCJ5tc&hl=en,none,none,none,none
23,D,Sami's Countertops LLC,"Port Arthur, TX",(409) 548-0373,"3988 Gulfway Dr, Port Arthur, TX 77642",https://www.google.com/maps/place/?q=place_id:ChIJAz40Xly7PoYR1qwQwFw3-FA&hl=en,none,none,none,none
67,D,The Final Touch Design,"Panama City Beach, FL",(850) 588-6142,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJU6qvBv6Mk4gR9HaqXAKjlqI&hl=en,none,none,none,none
72,D,Elegant Stone Cabinet LLC,"Mobile, AL",(251) 378-1855,"7535 Old Shell Rd, Mobile, AL 36608",https://www.google.com/maps/place/?q=place_id:ChIJhe599nOym4gRd3LyPY4Z9Hc&hl=en,none,none,none,none
80,D,Windsor Kitchen & Bath - Kitchen Cabinets - Edison,"Metuchen, NJ",(732) 985-5958,"800 US-1, Edison, NJ 08817",https://www.google.com/maps/place/?q=place_id:ChIJL39mnWrIw4kRnrdH_iEDb9E&hl=en,none,none,none,none
196,D,Strickland Homes & Remodeling,"Ozark, MO",(417) 848-1671,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvSDjGOvS3g4Rlx4UoLJl4cE&hl=en,none,none,none,none
305,D,All About Kitchen and Bathroom remodel,"Perth Amboy, NJ",(732) 376-7878,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJt_V8lH61w4kRRJG9bPgfH8Y&hl=en,none,none,none,none
399,D,The Bath and Kitchen Connection,"Hazelwood, MO",(314) 528-2270,"11976 Dorsett Rd, Maryland Heights, MO 63043",https://www.google.com/maps/place/?q=place_id:ChIJCY8Xmjkz34cRGij2MmvkgEQ&hl=en,none,none,none,none
502,D,Modern Kitchen Design And Build.,"Danville, CA",(925) 492-3069,"152 W Linda Mesa Ave, Danville, CA 94526",https://www.google.com/maps/place/?q=place_id:ChIJ5VtOKDvzj4ARJkU9P76I3v8&hl=en,none,none,none,none
28,D,Modern Wave Bathrooms,"Alameda, CA",(341) 222-3443,"1050 Forselles Way, Hayward, CA 94544",https://www.google.com/maps/place/?q=place_id:ChIJj2LOiX6Vj4ARhNG3DjqPGPg&hl=en,none,none,none,none
65,D,The Grout Savior,"Dumont, NJ",(201) 598-1555,"35 Washington Ave, Dumont, NJ 07628",https://www.google.com/maps/place/?q=place_id:ChIJW1xdZDfwwokRhi_ParzPAaA&hl=en,none,none,none,none
81,D,Roots & Risers Home Remodeling,"Pottsville, PA",(570) 481-1004,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOYeUjHrCxYkRpmd0g0xWM3Q&hl=en,none,none,none,none
195,D,Riley Home Remodel,"Wadsworth, OH",(330) 592-6988,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJPyLsXRDSMIgR_AKINkbThds&hl=en,none,none,none,none
211,D,Lee & Sons Remodeling LLC,"Highland, CA",(909) 252-3592,"4655 N D St, San Bernardino, CA 92407",https://www.google.com/maps/place/?q=place_id:ChIJcXuVqNFTw4ARJtOfe0qEjkY&hl=en,none,none,none,none
346,D,M&R Tile & Remodel,"Santa Paula, CA",(805) 660-2094,"103 S 13th St, Santa Paula, CA 93060",https://www.google.com/maps/place/?q=place_id:ChIJ08d9WIW16YARM3L3PtV2Ksg&hl=en,none,none,none,none
363,D,HomePride Bath of Grand Junction,"Grand Junction, CO",(970) 387-4248,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ8YQ-_HAdR4cRoCKcu6rYftg&hl=en,none,none,none,none
531,D,Painting & Remodeling By Lizardo's,"Lacy-Lakeview, TX",(254) 717-6169,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJRTu6X9yDT4YRihpEvxMoqeE&hl=en,none,none,none,none
143,D,Cabinet Coating Perfection,"DeBary, FL",(407) 927-1372,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqQ5LzgTfpEERsJXlrejA5Qs&hl=en,none,none,none,none
294,D,BaumStone Customs,"Buhl, ID",(208) 431-3427,"1561 Eldridge Ave, Twin Falls, ID 83301",https://www.google.com/maps/place/?q=place_id:ChIJzX6G6v-9rFQRgg-tbuC21DM&hl=en,none,none,none,none
```
