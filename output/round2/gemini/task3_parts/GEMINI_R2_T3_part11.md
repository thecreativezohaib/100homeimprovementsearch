# Round 2: Gemini task 3, part 11 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1421, reply in that chat "Continue with the businesses
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
1337,N,Revive Renovations,"Salem, UT",(801) 376-7326,"650 E Salem Canal Rd, Salem, UT 84653",https://www.google.com/maps/place/?q=place_id:ChIJ0Q79xLuFTYcR592ZOMAhCbk&hl=en,none,none,none,none,none
1338,N,WA Pro Builders LLC,"Redmond, WA",(206) 804-1196,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDVnuYVeLz64RqhlUW6YqQHI&hl=en,none,none,none,none,none
1339,N,The Cabinet Shop,"Harlingen, TX",(956) 202-3893,"21168 FM508, Harlingen, TX 78550",https://www.google.com/maps/place/?q=place_id:ChIJRyqwkMR4b4YRQJRuZSQ6uzE&hl=en,none,none,none,none,none
1340,N,S&A Excellence Bathroom Remodeling,"Brea, CA",(949) 850-6772,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxc0viDsInK8RnfTfF8Piw6Q&hl=en,none,none,none,none,none
1341,N,Costa Mesa Bathroom Remodeling Pros,"Costa Mesa, CA",(949) 669-7950,"369 E 17th St, Costa Mesa, CA 92627",https://www.google.com/maps/place/?q=place_id:ChIJF5AHpHLf3IAR72hdBaa7geM&hl=en,none,none,none,none,none
1342,N,Fred's Cabinet Shop,"Dadeville, AL",(256) 825-6875,"2728 Horseshoe Bend Rd, Dadeville, AL 36853",https://www.google.com/maps/place/?q=place_id:ChIJ8UMOX4NwjIgRaB6qotV093M&hl=en,none,none,none,none,none
1343,N,Robinson's Restoration & Remodeling,"Locust Grove, GA",(770) 668-6907,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ9wOaHL1e9IgRx-dBajiXqe4&hl=en,none,none,none,none,none
1344,N,DANE COOK cook enterprises interior and exterior solutions,"Brockport, NY",(585) 315-6016,"9373 W Ridge Rd, Brockport, NY 14420",https://www.google.com/maps/place/?q=place_id:ChIJzZE8L3YD1IkRpUGF1y8a464&hl=en,none,none,none,none,none
1345,N,Orangeburg Tile LLC,"Orangeburg, SC",(803) 662-9803,"1644 St Matthews Rd NE, Orangeburg, SC 29118",https://www.google.com/maps/place/?q=place_id:ChIJc8I1rFnU-IgRW0_AdEYdMUo&hl=en,none,none,none,none,none
1346,N,Coleman's Refinishing,"Denham Springs, LA",(504) 252-6238,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJV2KDmzH162MRU88H1F-7wmU&hl=en,none,none,none,none,none
1347,N,AMS Remodeling Inc.,"Loves Park, IL",(847) 971-3041,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJoe5eZAILE6wRRoreuezF_q4&hl=en,none,none,none,none,none
1348,N,Shamrock Tile LLC,"DeBary, FL",(407) 388-5511,"748 Costa Ln, DeBary, FL 32713",https://www.google.com/maps/place/?q=place_id:ChIJB_PXxZsT54gRd7-pDLiGrMY&hl=en,none,none,none,none,none
1349,N,Kitchen Innovations,"Fort Walton Beach, FL",(850) 796-3000,"44 Beal Pkwy SW, Fort Walton Beach, FL 32548",https://www.google.com/maps/place/?q=place_id:ChIJQwvovCM_kYgRtp4vg68e4K8&hl=en,none,none,none,none,none
1350,N,Creative Countertops,"Goleta, CA",(805) 946-0681,"178 Aero Camino, Goleta, CA 93117",https://www.google.com/maps/place/?q=place_id:ChIJ23wEZ5tA6YARTm5033BA7hg&hl=en,none,none,none,none,none
1351,N,Legacy Kitchens and Bath Plus,"Hollywood, FL",(954) 477-7080,"1918 Harrison St Ste 102, Hollywood, FL 33020",https://www.google.com/maps/place/?q=place_id:ChIJKzxHJ7ir2YgRCAlNH_ovqlM&hl=en,none,none,none,none,none
1352,N,Berza Group Corp,"Boynton Beach, FL",(954) 297-2126,"1020 Audace Ave, Boynton Beach, FL 33426",https://www.google.com/maps/place/?q=place_id:ChIJydf_4GCaFo4RBPuTU1khTas&hl=en,none,none,none,none,none
1353,N,Houss Build Remodel Repair,"St Cloud, FL",(689) 307-3646,"4640 Glencrest Loop, St Cloud, FL 34772",https://www.google.com/maps/place/?q=place_id:ChIJC19B23phJkcRhGSWsTh59V0&hl=en,none,none,none,none,none
1354,N,"MC Bathroom Remodeling, LLC","Kansas City, KS",(913) 963-9603,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTQzAyR6GGUcRFQ0A5yr_03k&hl=en,none,none,none,none,none
1355,N,Vinsicks' Flooring Design,"Indianola, IA",(515) 808-0465,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbxdZdO6PHQcR_kRflLC2yxU&hl=en,none,none,none,none,none
1356,N,Brian's Remodeling,"Ardmore, OK",(580) 264-0202,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJB-yR4FLVgkwR8otf40h6qG0&hl=en,none,none,none,none,none
1357,N,Mason's Renovations,"Utqia?vik, AK",(907) 671-1630,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ276BAJ0sqKcROoYFmSqaSz8&hl=en,none,none,none,none,none
1358,N,LW | Kitchen Remodeling of St Charles,"St. Charles, IL",(630) 228-1255,"306 S 2nd St, St. Charles, IL 60174",https://www.google.com/maps/place/?q=place_id:ChIJkW1Cx30DD4gRRXTagTH-9nM&hl=en,none,none,none,none,none
1359,N,Mattfield Renovations LLC,"Bemidji, MN",(218) 556-1257,"3495 Buchanan Ave SW, Bemidji, MN 56601",https://www.google.com/maps/place/?q=place_id:ChIJkS4Skbwm0qcRzJiLUl1s1ZA&hl=en,none,none,none,none,none
1360,N,MASTERCRAFT TILING LLC,"Westfield, IN",(463) 254-8517,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJO38a_rhxXaERtobiXf5ql28&hl=en,none,none,none,none,none
1361,N,Pruitt Home Renovations LLC,"Minden, LA",(318) 225-0817,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ66pVTOUVMYYR6-Ty3X1ETcY&hl=en,none,none,none,none,none
1362,N,Wilson's Cabinet Shop,"Glasgow, KY",(270) 651-7271,"812 Columbia Ave, Glasgow, KY 42141",https://www.google.com/maps/place/?q=place_id:ChIJObq-5q89ZogRvlRc4mkoRVw&hl=en,none,none,none,none,none
1363,N,Creative Finishes By Kelly,"Middletown, KY",(502) 649-0654,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJr6WIu2JRvS8Ro5otI-uxzLU&hl=en,none,none,none,none,none
1364,N,Miami Baths Refinishing,"Plantation, FL",(754) 291-6664,"499 NW 70th Ave suite: 300, Plantation, FL 33317",https://www.google.com/maps/place/?q=place_id:ChIJ_5n-Z64H2YgRB1tZH5GNBps&hl=en,none,none,none,none,none
1365,N,B&J Refinishing,"Woodway, TX",(254) 523-5754,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAQBEOTuHT4YR-GyLN4ILpeg&hl=en,none,none,none,none,none
1366,N,HSP Kitchen Remodel,"Everett, WA",(425) 616-3222,"125 W Casino Rd Unit 16, Everett, WA 98204",https://www.google.com/maps/place/?q=place_id:ChIJn8SMBlUBkFQRVGYNF4BMXmw&hl=en,none,none,none,none,none
1367,N,MKB HOME DESIGN,"Bell Gardens, CA",(562) 862-0279,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJB0pD2ZnNwoARr2tgyd9l5Jw&hl=en,none,none,none,none,none
1368,N,Haynes Services & Construction,"Alvin, TX",(979) 264-1220,"1108 E Hwy 6 Ste J, Alvin, TX 77511",https://www.google.com/maps/place/?q=place_id:ChIJw3L9S0aPQIYRZxZF7934EKQ&hl=en,none,none,none,none,none
1369,N,B & C Kitchens 'n Moore,"Groveland, FL",(352) 552-0448,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJkVMoibSN54gRV7aSILoPOiY&hl=en,none,none,none,none,none
1370,N,Woodlands Home Remodeling,"The Woodlands, TX",(281) 305-5267,"25275 Budde Rd Ste 28, The Woodlands, TX 77380",https://www.google.com/maps/place/?q=place_id:ChIJb8zRhSQ0R4YR-rB0n6zr5ec&hl=en,none,none,none,none,none
1371,N,Brandon Joseph Custom Bath & Interiors,"Ferndale, MI",(248) 602-0248,"744 Laprairie St, Ferndale, MI 48220",https://www.google.com/maps/place/?q=place_id:ChIJr2sIdfg-jE4RYA18M9DWcWc&hl=en,none,none,none,none,none
1372,N,Eagle valley design,"Saratoga Springs, UT",(801) 854-8762,"228 West Lariat Blvd, Saratoga Springs, UT 84045",https://www.google.com/maps/place/?q=place_id:ChIJ1dhmPix5TYcRB1TE05vhFEg&hl=en,none,none,none,none,none
1373,N,Kitchen Works of Cabot,"Ward, AR",(501) 941-3955,"13905 Hwy 31, Ward, AR 72176",https://www.google.com/maps/place/?q=place_id:ChIJTUS-Yuru0ocRw6RzwGu7fiE&hl=en,none,none,none,none,none
1374,N,Frick & Sons,"Chehalis, WA",(253) 878-2205,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJFb3SP__mDmcR4TjYhkAiGsU&hl=en,none,none,none,none,none
1375,N,Superior Renovations,"Albany, OH",(740) 517-8795,"27480 Old State Rte 346, Albany, OH 45710",https://www.google.com/maps/place/?q=place_id:ChIJcaBV2avRR4gRYVM-LASPDys&hl=en,none,none,none,none,none
1376,N,Sal's Painting and Remodeling,"Sansom Park, TX",(682) 270-3049,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-QDkaujvpGQRiHgwOrltEVE&hl=en,none,none,none,none,none
1377,N,Reflect,"Longview, WA",(360) 846-3273,"1305 California Way Ste C, Longview, WA 98632",https://www.google.com/maps/place/?q=place_id:ChIJo6C3vNbvWyUR15EfS2mPxXg&hl=en,none,none,none,none,none
1378,N,A-1 Shower Repair,"South Houston, TX",(713) 947-7457,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOyxH-0SYQIYR7_79eO9zEpQ&hl=en,none,none,none,none,none
1379,N,Trusted Contracting,"Appleton, WI",(920) 851-3225,"5550 W Edgewood Dr, Appleton, WI 54913",https://www.google.com/maps/place/?q=place_id:ChIJcwfy3QDLA4gRRrTlLMVau94&hl=en,none,none,none,none,none
1380,N,Alabama Countertop Co,"Cullman, AL",(256) 739-5505,"20 Nesmith Rd, Cullman, AL 35058",https://www.google.com/maps/place/?q=place_id:ChIJ8RQ2V_bMiYgRx49u10ZAClU&hl=en,none,none,none,none,none
1381,N,Paradise Globe Kitchen and Bath Cabinet Sales,"Lauderhill, FL",(954) 394-2954,"3541 NW 7th Pl, Lauderhill, FL 33311",https://www.google.com/maps/place/?q=place_id:ChIJuyx3NSb6wKIRmHwf5BwAl9g&hl=en,none,none,none,none,none
1382,N,Grace Home Kitchen & Bath,"Jamaica, NY",(929) 922-7877,"112-05 Rockaway Blvd, Jamaica, NY 11420",https://www.google.com/maps/place/?q=place_id:ChIJM9OKvF1nwokRUrwky9-K5lg&hl=en,none,none,none,none,none
1383,N,Elite Tile LLC,"La Grande, OR",(541) 429-3555,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJd67FfsLKHyARV7NZ2LAMD3I&hl=en,none,none,none,none,none
1419,N,"Kitchen remodeler in Mercer Island, WA | New Era Construction",serves the best. We specialize in creating highly functional,(253) 402-7311,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbaOmVQJYzC4RgNqZUqjjzeI&hl=en,none,none,none,none,none
1420,N,Milestone Kitchen & Bath Inc,"Laguna Hills, CA",(949) 590-9999,"25381 Alicia Pkwy Ste i, Laguna Hills, CA 92653",https://www.google.com/maps/place/?q=place_id:ChIJ9buUq3vp3IARk2XuLi7ijp8&hl=en,none,none,none,none,none
1421,N,HSP Bathroom Remodel,"Auburn, WA",(253) 600-4140,"511 M St NE unit 206, Auburn, WA 98002",https://www.google.com/maps/place/?q=place_id:ChIJS61CdVpZkFQRacMN07bsukM&hl=en,none,none,none,none,none
```
