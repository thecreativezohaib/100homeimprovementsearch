# Round 2: Gemini task 2, part 16 of 17 (100 businesses, rows 39 to 498)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 498: reply in that chat "Continue with
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
39,D,Pro Crafters,"Perkasie, PA",(267) 245-1587,"393 Acorn Ave, Telford, PA 18969",https://www.google.com/maps/place/?q=place_id:ChIJt5fgOIqhxokRt6Vx-drH4MQ&hl=en,none,none,none,none
48,D,"Shoreline Marble & Tile, Inc.","Kenosha, WI",(262) 308-0510,"3207 63rd St, Kenosha, WI 53142",https://www.google.com/maps/place/?q=place_id:ChIJlar3MHZeBYgReJALoqVnCj0&hl=en,none,none,none,none
49,D,Martinez Stone Inc,"Nacogdoches, TX",(936) 329-5997,"3007 NW Stallings Dr, Nacogdoches, TX 75964",https://www.google.com/maps/place/?q=place_id:ChIJl73oUICLN4YReRPTliD6AP4&hl=en,none,none,none,none
55,D,Timeless Marble & Granite LLC,"Bluffdale, UT",(801) 349-9990,"14587 S 790 W, Bluffdale, UT 84065",https://www.google.com/maps/place/?q=place_id:ChIJRSRf7oSBUocRtzPyg8OIEWE&hl=en,none,none,none,none
100,D,"Logo Renovations, LLC","Parsons, KS",(620) 429-0740,"509 N Kansas Ave, Columbus, KS 66725",https://www.google.com/maps/place/?q=place_id:ChIJSUcEi06id2MRm_7v6uPkfcU&hl=en,none,none,none,none
116,D,"Contaldi Creations, LLC","Wanaque, NJ",(973) 632-1282,"306 Wanaque Ave, Pompton Lakes, NJ 07442",https://www.google.com/maps/place/?q=place_id:ChIJf1VFPVgdw4kRzyE1GIIuih0&hl=en,none,none,none,none
215,D,Styles Kitchen Cabinets,"Cape Coral, FL",(239) 895-2349,"1939 Del Prado Blvd S # E, Cape Coral, FL 33990",https://www.google.com/maps/place/?q=place_id:ChIJCdHgO4tB24gRolAIvqGEXzY&hl=en,none,none,none,none
223,D,Casa Bella Contractors,"Haledon, NJ",(201) 954-4275,"169 5th Ave, Hawthorne, NJ 07506",https://www.google.com/maps/place/?q=place_id:ChIJhcIR4Vj8wokRC8Z6ooNPX9o&hl=en,none,none,none,none
242,D,PNW Tilewerks,"Newberg, OR",(971) 212-1230,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJUeFsUBbAi28RyQe9IQ5ec7Y&hl=en,none,none,none,none
327,D,Tile Decor LLC,"Haledon, NJ",(929) 424-0737,"21 King St, Haledon, NJ 07508",https://www.google.com/maps/place/?q=place_id:ChIJS8eNGfX9wokR_kW6m2QC0RE&hl=en,none,none,none,none
390,D,Creative Surfaces & Design LLC.,"Hooper, UT",(801) 540-4281,"2257 W 875 S, Syracuse, UT 84075",https://www.google.com/maps/place/?q=place_id:ChIJ7T9nkPsbU4cR97TlbwL8E2w&hl=en,none,none,none,none
402,D,Ty-Cour Kitchen & Bath,"Collinsville, IL",(618) 876-2550,"730 Madison Ave, Madison, IL 62060",https://www.google.com/maps/place/?q=place_id:ChIJdXl51HpN34cR1RK_GjG9-nk&hl=en,none,none,none,none
442,D,Cody Runyon Remodeling,"California City, CA",(707) 345-6922,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAX_hoVtif2cR3SvfJkq8kN4&hl=en,none,none,none,none
451,D,Above & Beyond Cabinetry,"Hendersonville, NC",(828) 556-7789,"815 Barbara Blvd, Hendersonville, NC 28739",https://www.google.com/maps/place/?q=place_id:ChIJnZgBxBnBWYgR9oot0ot8zNA&hl=en,none,none,none,none
501,D,Rise Contracting Services,"Manor, TX",(512) 810-2548,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ9S1Ifo3HRIYRU8saMv5ABUY&hl=en,none,none,none,none
537,D,✶ M.D.R. Marble & Granite Inc.,"Clovis, NM",(505) 261-6993,"317 N Walnut St, Clovis, NM 88101",https://www.google.com/maps/place/?q=place_id:ChIJMwKoVeTdAocR-XsS3IUZr8o&hl=en,none,none,none,none
21,D,Best Flooring LLC,"Medfield, MA",(843) 324-7301,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJm4knWM-J44kRz-ysjnUhrBc&hl=en,none,none,none,none
32,D,123 Construction & Remodeling,"Wesley Chapel, FL",(813) 966-5454,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJe8bOd56e4W4RK0HfvPmWvng&hl=en,none,none,none,none
58,D,S&A Excellence Kitchen Remodeling,"San Juan Capistrano, CA",(949) 850-6793,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJh7STnCL7XasR2Dsv_NSYRRc&hl=en,none,none,none,none
68,D,Zion Remodeling and Restoration,"Winfield, IL",(630) 359-7020,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJKZGouLf_DogRQhYLRAz-UIQ&hl=en,none,none,none,none
70,D,Grey Finishes,"Oak Lawn, IL",(872) 216-9168,"9605 S 53rd Ave, Oak Lawn, IL 60453",https://www.google.com/maps/place/?q=place_id:ChIJLz_IEvUnVwIRTlXbgVb0lSw&hl=en,none,none,none,none
106,D,Myers Construction Services,"Zanesville, OH",(740) 607-4184,"6145 Rollins Dr, Nashport, OH 43830",https://www.google.com/maps/place/?q=place_id:ChIJbUHxvHHzN4gRXc9diTx7kAQ&hl=en,none,none,none,none
114,D,Tubs & Tops,"Longview, TX",(903) 235-2422,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJf3R5RKM-NoYRzEoqRfyvYyY&hl=en,none,none,none,none
131,D,Welch Renovations,"Phenix City, AL",(706) 577-0115,"1511 Melanie Ln, Phenix City, AL 36867",https://www.google.com/maps/place/?q=place_id:ChIJ1Qmz2i7NjIgR5emMlPRCfsQ&hl=en,none,none,none,none
146,D,Stone by AJ,"Maumelle, AR",(501) 794-8382,"9211 Maumelle Blvd, North Little Rock, AR 72113",https://www.google.com/maps/place/?q=place_id:ChIJZae0Yomj0ocRwyOfOnW4rHc&hl=en,none,none,none,none
170,D,Nu-Shine Kitchen and Bathroom Refinishing,"Brooksville, FL",(727) 319-8332,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJJXN6YxP7wogRQR7VJWunwnU&hl=en,none,none,none,none
176,D,Operation Renovation LLC,"Massillon, OH",(330) 879-8124,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJfXr4dg8mN4gRYtXVWv93sks&hl=en,none,none,none,none
177,D,Good Choice Works LLC,"Ramsey, MN",(763) 219-2150,"5631 164th Ln NW, Ramsey, MN 55303",https://www.google.com/maps/place/?q=place_id:ChIJzSX9U6kVs1IRfbT_sG1WOTE&hl=en,none,none,none,none
295,D,Reliable Remodels,"Unalaska, AK",(907) 632-1029,"9701 Elmore Rd, Anchorage, AK 99507",https://www.google.com/maps/place/?q=place_id:ChIJp8xwoo6XyFYRjqsW56zIlqU&hl=en,none,none,none,none
306,D,Morris Finishing Company LLC,"Wytheville, VA",(540) 674-0079,"549 E Main St, Dublin, VA 24084",https://www.google.com/maps/place/?q=place_id:ChIJeambtNbkTYgRSlJ7CU3rEOE&hl=en,none,none,none,none
316,D,Builders Direct,"Hazleton, PA",(570) 501-1133,"757 W Broad St, Hazleton, PA 18201",https://www.google.com/maps/place/?q=place_id:ChIJ-c9sD3SkxYkR5sbrh7GsFrY&hl=en,none,none,none,none
325,D,Arnold Improvements LLC,"Ellington, CT",(860) 872-6226,"8 Faith Dr, Vernon, CT 06066",https://www.google.com/maps/place/?q=place_id:ChIJxan55Qr35okRncfsf59apYI&hl=en,none,none,none,none
355,D,Creative Tile and Remodeling LLC,"Gladstone, MO",(816) 337-2374,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQVGpdo75wIcRTnwma3-AUk8&hl=en,none,none,none,none
434,D,Complete Home Remodeling LLC,"Springfield, MO",(417) 761-0675,"227 E Sunshine St Suite 105, Springfield, MO 65807",https://www.google.com/maps/place/?q=place_id:ChIJ8T9mNOdjz4cR33V_FRqHyag&hl=en,none,none,none,none
453,D,Tile co,"Lebanon, OH",(937) 407-5833,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJS5834oyoC0QRVcvn5n2AfXk&hl=en,none,none,none,none
497,D,SnR Remodeling Services LLC,"Kennesaw, GA",(770) 880-8981,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJN7NUUIOJx64RtqJaZKJ5xkk&hl=en,none,none,none,none
507,D,Stone Creations and Cabinetry,"Revere, MA",(617) 390-2110,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0f_udiFx44kRHzdKdTSAQV0&hl=en,none,none,none,none
558,D,Clancy's Custom Cabinets & More,"Seguin, TX",(210) 870-8735,"171 Indian Trail, Seguin, TX 78155",https://www.google.com/maps/place/?q=place_id:ChIJo7lcJrXHXIYRoqZGgMINYT8&hl=en,none,none,none,none
564,D,D'ANGELS HOME REMODELING,"Streamwood, IL",(847) 807-5014,"5 S Victoria Ln, Streamwood, IL 60107",https://www.google.com/maps/place/?q=place_id:ChIJpxgszCmoD4gR1zdErTL2xSk&hl=en,none,none,none,none
12,D,"Fit & Finish HPS,LLC","Jupiter, FL",(561) 888-3381,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ1dgYmjOaNUsRDng7_2Flf2M&hl=en,none,none,none,none
47,D,ERC Renovation LLC,"Braselton, GA",(866) 254-0162,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJs51CkSuKn68RmlyNmUECS9c&hl=en,none,none,none,none
141,D,Ramos Home Renovations,"Balch Springs, TX",(972) 891-4259,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJR2SaX6eXqwQR-3rZaw067aU&hl=en,none,none,none,none
145,D,Atlas Tile Co,"Vineyard, UT",(714) 350-5904,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ5912k1l0BE4Ri50GptGo3W4&hl=en,none,none,none,none
171,D,Matrix Bathroom Systems,"Portage, MI",(269) 575-0079,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJX4EPvDF1F4gR815t4_WbdHg&hl=en,none,none,none,none
203,D,Emerald Remodeling llc.,"Buena Vista, VA",(571) 518-8026,"7367 Cluster House Way, Gainesville, VA 20155",https://www.google.com/maps/place/?q=place_id:ChIJHz0t9g1ntokRfyNu9c79XSE&hl=en,none,none,none,none
247,D,Mr MrHandyDandy Bathroom Renovations,"Hampton, GA",,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbdEpAW_19IgR5avZ8xL_uuA&hl=en,none,none,none,none
259,D,Lk Kitchen,"Dunellen, NJ",(929) 374-9031,"118 N Washington Ave, Dunellen, NJ 08812",https://www.google.com/maps/place/?q=place_id:ChIJS4ndqOe5w4kRNaRjXkt-yTs&hl=en,none,none,none,none
323,D,Mass Remodeling,"Foxborough, MA",(774) 219-7880,"Pratt St, Mansfield, MA 02048",https://www.google.com/maps/place/?q=place_id:ChIJIcFeh19j5IkROxDQhWt7z1A&hl=en,none,none,none,none
366,D,Springbok Remodeling,"Alpine, TX",(830) 446-0095,"Blue Ridge, Comfort, TX 78013",https://www.google.com/maps/place/?q=place_id:ChIJs4WIHex-LW4RA2Sc_8DmGq8&hl=en,none,none,none,none
400,D,DLA SERVICES REPAIR AND REMODELING,"Romulus, MI",(248) 270-5066,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVd7Bh56WqkcRzzXrpWImL2U&hl=en,none,none,none,none
437,D,Cornerstone Remodeling,"Cypress, CA",(800) 998-8983,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDc-LTIHB4AcRTOMpoGcs8ZE&hl=en,none,none,none,none
467,D,Pablo's Remodeling & Painting LLC,"Beaumont, TX",(409) 223-8970,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ10FYAFE1S68RikIajuSr_eY&hl=en,none,none,none,none
545,D,Almonte Home improvement Contractor,"Whitehall, OH",(614) 933-1995,"6107 McNaughten Ctr, Columbus, OH 43232",https://www.google.com/maps/place/?q=place_id:ChIJPWeQAZVjOIgRTOs2cTttYQg&hl=en,none,none,none,none
555,D,Priority Home Works,"Newport News, VA",,"607 Industrial Park Dr Ste FF, Newport News, VA 23608",https://www.google.com/maps/place/?q=place_id:ChIJY7rekiN9sIkRoAcm5W1lkSc&hl=en,none,none,none,none
10,D,Big Sky Bathroom & Kitchen,"Laurel, MT",(406) 964-5116,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7zh40fjfXEURPv023DT0hPw&hl=en,none,none,none,none
30,D,Montco Handyman,"Norristown, PA",(484) 534-7851,"1529 Pine St, Norristown, PA 19401",https://www.google.com/maps/place/?q=place_id:ChIJnf84z969xokRR9-phgkdaJI&hl=en,none,none,none,none
59,D,BAB Construction LLC,"Aurora, CO",(720) 687-7651,"12870 E Idaho Dr, Aurora, CO 80012",https://www.google.com/maps/place/?q=place_id:ChIJaccjaOB9bIcR4XlSnalF97Y&hl=en,none,none,none,none
82,D,ILIRIA REMODELING,"Tinley Park, IL",(708) 673-1671,"Courtyards of 78th Avenue Shopping Center, W 159th St, Tinley Park, IL 60477",https://www.google.com/maps/place/?q=place_id:ChIJTTGPgThExgYRWbCiMugmsiU&hl=en,none,none,none,none
127,D,NB Bath & Remodeling,"Washington, IL",(309) 370-6017,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvbKaHchTCogREEO8y518aEI&hl=en,none,none,none,none
162,D,CTG TILE & HANDYMAN,"Villa Rica, GA",(404) 904-2834,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJExARAF7FoacRMbGEZxA7ydg&hl=en,none,none,none,none
207,D,Zaprala Romano Remodeling,"Gloucester City, NJ",(856) 981-7569,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv1NYTBvSxokRsh-IRDcNwlg&hl=en,none,none,none,none
213,D,Capitol Countertops,"Pearl, MS",(601) 664-2008,"129 Paul Truitt Ln, Pearl, MS 39208",https://www.google.com/maps/place/?q=place_id:ChIJNcQd6DgsKIYRiApHX66nMU4&hl=en,none,none,none,none
246,D,Creative Construction Services Inc,"Santa Maria, CA",(805) 694-6525,"240 S Broadway, Orcutt, CA 93455",https://www.google.com/maps/place/?q=place_id:ChIJA8Dj5Ftt7IARemzvFOtrw9s&hl=en,none,none,none,none
351,D,Patton Family Remodeling llc,"Festus, MO",(314) 620-5172,"308 10th St, Crystal City, MO 63019",https://www.google.com/maps/place/?q=place_id:ChIJn7LNRoHv2IcRlOTNNyU-weU&hl=en,none,none,none,none
468,D,Red Remodeling LLC,"Topeka, KS",(785) 506-5731,"2065 SW Lane St, Topeka, KS 66604",https://www.google.com/maps/place/?q=place_id:ChIJv_7hU-LyXK8RV_nIoA28a0g&hl=en,none,none,none,none
524,D,CT Remodeling,"Ellington, CT",(860) 200-7135,"27 Folkstone Rd Apt C, Broad Brook, CT 06016",https://www.google.com/maps/place/?q=place_id:ChIJF479TdOMOCsR-h-9mTsvh9o&hl=en,none,none,none,none
568,D,Marble & Granite Guys,"Smithfield, NC",(919) 441-3219,"3295 US-70 BUS, Smithfield, NC 27577",https://www.google.com/maps/place/?q=place_id:ChIJsVUqMGQRrIkR6cBm2myuCjk&hl=en,none,none,none,none
6,D,Maverick Remodeling,"University Park, TX",(214) 736-4210,"5730 Anita St, Dallas, TX 75206",https://www.google.com/maps/place/?q=place_id:ChIJV6tLG2mfToYReOUQO8ofojA&hl=en,none,none,none,none
11,D,Innerstone Marble & Granite LLC,"Brookings, OR",(541) 469-3906,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ09bM_zeg2lQRPQLLpUYopFo&hl=en,none,none,none,none
16,D,Elizabeth Kitchen & Granite LLC,"Elizabeth, NJ",(908) 662-9512,"719 Livingston St, Elizabeth, NJ 07201",https://www.google.com/maps/place/?q=place_id:ChIJe0AJP3lNwokRwXb3AJOuG6g&hl=en,none,none,none,none
51,D,T. C. Rich,"North Augusta, SC",(706) 231-1589,"1450 Georgia Ave Ste 6564, North Augusta, SC 29861",https://www.google.com/maps/place/?q=place_id:ChIJEYiutsXN-YgRiqNrYwfSfjo&hl=en,none,none,none,none
108,D,J&C Tile & Marble Renovation LLC,"West New York, NJ",(201) 667-9311,"6619 Bergenline Ave, West New York, NJ 07093",https://www.google.com/maps/place/?q=place_id:ChIJwymjcnFZwokR70BVycWm64M&hl=en,none,none,none,none
120,D,Jireh Remodeling,"Sanford, NC",(919) 895-0275,"322 Oakwood Ave, Sanford, NC 27330",https://www.google.com/maps/place/?q=place_id:ChIJ0RQb7WGnrIkRHUQedRjCpjk&hl=en,none,none,none,none
133,D,Hoosier Custom Cabinet Designs,"Mount Dora, FL",(352) 385-0000,"880 Bay Rd Unit B4, Mt Dora, FL 32757",https://www.google.com/maps/place/?q=place_id:ChIJ8WAtJLKi54gR5g8Me7W9EZo&hl=en,none,none,none,none
150,D,Prime Atlanta Renovations,"Duluth, GA",(770) 823-6474,"3843 Howell Springs Dr, Duluth, GA 30096",https://www.google.com/maps/place/?q=place_id:ChIJNSCkKIaj9YgRnP5U40jOP0I&hl=en,none,none,none,none
163,D,S&A Excellence Bathroom Remodeling,"Laguna Woods, CA",(657) 236-3301,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJkaUSsPdCOmYRPINKFxtDyn4&hl=en,none,none,none,none
202,D,A.C.E Carpentry,"Bridgewater, VA",(540) 699-3098,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXWc4RC-_tIkRmdthhelSsNk&hl=en,none,none,none,none
261,D,Dna remodels llc,"Titusville, FL",(321) 557-0469,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqQJDZwMVjQYRtAvKmbFOoZI&hl=en,none,none,none,none
309,D,B&M Contractors,"The Colony, TX",(469) 826-3636,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZzmkEjAlTIYRBiXnpEKeGsw&hl=en,none,none,none,none
358,D,Giovannis Design and Install Group,"Kenilworth, NJ",(908) 244-4259,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJo5nbmJKtw4kRqAAelBvgOv0&hl=en,none,none,none,none
459,D,Luxury Remodeling LLC,"Falls Church, VA",(571) 505-9854,"2922 Willston Pl, Falls Church, VA 22044",https://www.google.com/maps/place/?q=place_id:ChIJ-aBZwh21t4kRdB9BPtH93ck&hl=en,none,none,none,none
561,D,E &O LLC,"Olathe, KS",(913) 444-0232,"13505 S Mur-Len Rd Ste 105 #145, Olathe, KS 66062",https://www.google.com/maps/place/?q=place_id:ChIJfyNBCnK_wIcRYuR0wKQ8TzE&hl=en,none,none,none,none
36,D,Dynasty Home Improvement LLC,"Montville, CT",(860) 710-4602,"7A Windham Ave, Colchester, CT 06415",https://www.google.com/maps/place/?q=place_id:ChIJD2cHR6pp5okRI-_s7du6UpA&hl=en,none,none,none,none
54,D,Stone Koat Kreations LLC Epoxy Countertops & Floors,"Zachary, LA",(225) 453-2353,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXaHPeA-bJoYRaXooXaGqSOw&hl=en,none,none,none,none
74,D,Better Looks Home Renovations,"Coconut Creek, FL",(561) 662-9099,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJm5IOaH_S1CkRq2JTb1DjLX0&hl=en,none,none,none,none
157,D,All Pro Basements,"Dardenne Prairie, MO",(636) 281-6045,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJRSGSYiDQ3ocRPxeMtycNUpE&hl=en,none,none,none,none
172,D,"Simko Tile & Bath, LLC","Macon, GA",(912) 266-1433,"911 Matthews Dr, Macon, GA 31210",https://www.google.com/maps/place/?q=place_id:ChIJCxzx1GYn5YgRgkTe5GpM7qE&hl=en,none,none,none,none
206,D,A1 Granite & Quartz Inc.,"Wallington, NJ",(973) 815-1170,"34 Midland Ave #1723, Wallington, NJ 07057",https://www.google.com/maps/place/?q=place_id:ChIJT6QRpjz5wokROhFlw8o_iFw&hl=en,none,none,none,none
237,D,Carlson Property Solutions LLC,"Johnstown, CO",,"3751 Summerwood Way, Johnstown, CO 80534",https://www.google.com/maps/place/?q=place_id:ChIJ_____09JaYcRmP2WFvFdPIw&hl=en,none,none,none,none
240,D,Centex Bath,"Round Rock, TX",(512) 592-1203,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMb1U5afTRIYRN5dBWSKynuQ&hl=en,none,none,none,none
251,D,Do All Glaze and Remodel,"Flat Rock, MI",(734) 934-0010,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJtz2Ho4Y_O4gRmwBdnQyRVeI&hl=en,none,none,none,none
256,D,"Essential Home Renovation, Llc","Council Bluffs, IA",(402) 301-7142,"Council Bluffs, IA 51502",https://www.google.com/maps/place/?q=place_id:ChIJ3XUc9miFk4cRj1Csrs_th8Y&hl=en,none,none,none,none
264,D,Northshore Custom Tile and Flooring Inc.,"Covington, LA",(985) 317-9847,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxwO_XoxdJ4YRdWvbEMmNmo8&hl=en,none,none,none,none
268,D,LCR Home Solutions LLC,"Lochbuie, CO",(720) 350-1984,"579 Jewel St, Lochbuie, CO 80603",https://www.google.com/maps/place/?q=place_id:ChIJxch48Z-3gYERtOwPsQyA72A&hl=en,none,none,none,none
317,D,Masters Kitchen and Flooring,"Nicholasville, KY",(859) 813-0727,"2420 Vince Rd, Nicholasville, KY 40356",https://www.google.com/maps/place/?q=place_id:ChIJMwLeaZFfQogR8BO23Z6F1VM&hl=en,none,none,none,none
329,D,Titan Repair LLC,"Billings, MT",(406) 690-0987,"2515 Poly Dr, Billings, MT 59102",https://www.google.com/maps/place/?q=place_id:ChIJny8Poox8SFMRrIi_Vw3LB5Y&hl=en,none,none,none,none
368,D,"Christians Remodeling, LLC","Jeffersonville, IN",(502) 434-0521,"Avondale Ct, Jeffersonville, IN 47130",https://www.google.com/maps/place/?q=place_id:ChIJz32sMM2qY4YRvI47jhUC_E0&hl=en,none,none,none,none
394,D,Greacen Home Repair and Remodeling,"Napa, CA",(315) 706-5591,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ5yDiQbmAZ6wRDyjH4yk7ni8&hl=en,none,none,none,none
416,D,L & N Services,"Great Falls, MT",(406) 402-8181,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhzPeIFtHQlMRBPHRYD-KQP8&hl=en,none,none,none,none
498,D,Total Home Solutions,"Chesapeake, VA",(252) 599-1031,"1029 Long Ridge Rd, Chesapeake, VA 23322",https://www.google.com/maps/place/?q=place_id:ChIJh6xcTQC5uokRC2ItoOJpfq4&hl=en,none,none,none,none
```
