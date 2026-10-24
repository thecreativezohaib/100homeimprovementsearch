# Round 2: Gemini task 2, part 06 of 17 (100 businesses, rows 1584 to 1683)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 1683: reply in that chat "Continue with
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
1584,C,Bathrooms Made Easy,"Newport News, VA",(757) 206-5652,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJq6qqqjqAuokREO5bZrG80qg&hl=en,none,none,none,none
1585,C,Meru Design,"Titusville, FL",(321) 468-5208,"7645 US-1, Titusville, FL 32780",https://www.google.com/maps/place/?q=place_id:ChIJq6oW8UdC54gRJGdKOZFqxx4&hl=en,none,none,none,none
1586,C,Metro Cabinets,"Prior Lake, MN",(952) 447-7722,"5418 Cottonwood Ln SE, Prior Lake, MN 55372",https://www.google.com/maps/place/?q=place_id:ChIJmWzVpyI-9ocR37PHebg56MQ&hl=en,none,none,none,none
1587,C,Bueno's construction & Remodeling LLC,"Crosby, TX",(281) 381-4245,"20420 Shady Ln, Crosby, TX 77532",https://www.google.com/maps/place/?q=place_id:ChIJWZUnab-nQIYR4s6hXgpw3vU&hl=en,none,none,none,none
1588,C,Finish Carpentry & Remodeling,"New Boston, MI",(313) 623-6476,"34540 Huron River Dr, New Boston, MI 48164",https://www.google.com/maps/place/?q=place_id:ChIJG7PMgTRFO4gRbuaCStCYqfY&hl=en,none,none,none,none
1589,C,ELES HOMES,"La Habra, CA",(877) 860-0306,"2121 Imperial Hwy., La Habra, CA 90631",https://www.google.com/maps/place/?q=place_id:ChIJPwO54mDSYygRq5pi5SPOil4&hl=en,none,none,none,none
1590,C,Straight Edge Custom Tile & Stone,"Fenton, MI",(810) 701-7384,"15275 Bealfred Dr, Fenton, MI 48430",https://www.google.com/maps/place/?q=place_id:ChIJVQ1-lW6wXysRC2KJ5CPD-ts&hl=en,none,none,none,none
1591,C,Oki Handyman Services,"St. James, NC",(910) 391-1055,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJa5MXOnwHqokRJvqw_CsQhNo&hl=en,none,none,none,none
1592,C,Top Notch Granite solid countertops,"Florence, MS",(601) 540-0755,"93 Jackson Cir, Florence, MS 39073",https://www.google.com/maps/place/?q=place_id:ChIJkcakxDHTKYYRwD7rUGWdBsM&hl=en,none,none,none,none
1593,C,Reeds Remodeling & Cleaning Service,"Peel, AR",(870) 504-2883,"210 Crimson Ln, Peel, AR 72668",https://www.google.com/maps/place/?q=place_id:ChIJ8V3IKtccv4cRh9j4zLbtjYQ&hl=en,none,none,none,none
1594,C,Ogden Woodworking,"Goleta, CA",(805) 680-5867,"375 Pine Ave #13, Goleta, CA 93117",https://www.google.com/maps/place/?q=place_id:ChIJ56ix-nhA6YARgr-rdfNSR8U&hl=en,none,none,none,none
1595,C,Kinch Customs LLC,"Thomasville, GA",(229) 234-7939,"423 Commercial Dr C, Thomasville, GA 31757",https://www.google.com/maps/place/?q=place_id:ChIJt3LkAgV5NIUR1VuEwEdPiW4&hl=en,none,none,none,none
1596,C,B&C REMODELING,"Centralia, WA",(360) 623-6755,"2515 N Pearl St trlr #14, Centralia, WA 98531",https://www.google.com/maps/place/?q=place_id:ChIJ0StlsNxhkVQRJdR6pC0uXbY&hl=en,none,none,none,none
1597,C,Euro Kitchen & Bath Design,"Yonkers, NY",(914) 457-0093,"792 McLean Ave, Yonkers, NY 10704",https://www.google.com/maps/place/?q=place_id:ChIJg-YPLNzywokRgSvCv9G_P88&hl=en,none,none,none,none
1598,C,"Hood's Custom Renovations, LLC","Wellsville, PA",(717) 991-3999,"14 York St, Wellsville, PA 17365",https://www.google.com/maps/place/?q=place_id:ChIJ-bnsQeHxyIkRhm8v8A6HQ_o&hl=en,none,none,none,none
1599,C,Custom Wood Concepts LLC,"Palm Springs, CA",(760) 275-9289,"1251 Montalvo Way d, Palm Springs, CA 92262",https://www.google.com/maps/place/?q=place_id:ChIJg0b0YRYd24AReOHMjapkyCY&hl=en,none,none,none,none
1600,C,Klein Remodeling,"Navasota, TX",(936) 697-0092,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZ-AxmEMCX2MRqP6Elsn8Uhc&hl=en,none,none,none,none
1601,C,"Imagine That Home Improvements, LLC","Twin Falls, ID",(208) 407-2729,"Blue Lakes Blvd, Twin Falls, ID 83301",https://www.google.com/maps/place/?q=place_id:ChIJ1edoCFCjrFQR8Wxh-obkad8&hl=en,none,none,none,none
1602,C,Laguna Granite & Quartz,"Liberty Hill, TX",(512) 501-9339,"1775 County Rd 279, Liberty Hill, TX 78642",https://www.google.com/maps/place/?q=place_id:ChIJ073PodgpW4YR8Bo3NWze5LA&hl=en,none,none,none,none
1603,C,Renovate,"Lynn, MA",(781) 219-8489,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJBe-ZQrRt44kRsm1UO8nogIw&hl=en,none,none,none,none
1604,C,HS Remodeling,"Wilton, CT",(203) 440-7483,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJEUpdR2WSdmwRYQLWv9zqPg0&hl=en,none,none,none,none
1605,C,Schaumkel Renovations,"Tooele, UT",(650) 619-9860,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDbE46KMRp0oRWxK2F6OdyLI&hl=en,none,none,none,none
1606,C,DCH llc,"Willimantic, CT",(860) 514-2516,"136 Chapman St Apt 3, Willimantic, CT 06226",https://www.google.com/maps/place/?q=place_id:ChIJly8ux6dj5okRBAfoEdFG0_Q&hl=en,none,none,none,none
1607,C,Veloso Construction,"Long Branch, NJ",(732) 829-8547,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJCcNW_YzlHQURdR4wOT1Pgag&hl=en,none,none,none,none
1608,C,Polgam Corp.,"Hickory Creek, TX",(972) 333-6154,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ1zlnvxAyTIYRqLIbqAd0bT4&hl=en,none,none,none,none
1609,C,Wright Remodeling Service LLC,"Dublin, GA",(478) 484-2488,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxwolNoxg7goRILADPNxDSPk&hl=en,none,none,none,none
1610,C,New Age Construction,"Kannapolis, NC",(704) 956-9206,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJJTnH63ezrIMRiDFRVBJpPSI&hl=en,none,none,none,none
1611,C,JCS TILE & MARBLE,"Port Townsend, WA",(360) 643-3344,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJI_p0UbdccQkRaNtKt5PYLPA&hl=en,none,none,none,none
1612,C,Emsies Construction & Remodeling,"Poughkeepsie, NY",(845) 745-9582,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJy8AgeLqW-W4RKT-d08mj5Ko&hl=en,none,none,none,none
1613,C,Next Step Remodeling Llc,"Sandy, UT",(801) 698-5482,"10533 Larkspur Dr, Sandy, UT 84094",https://www.google.com/maps/place/?q=place_id:ChIJU60pre2StSsRW68-tvMkUxI&hl=en,none,none,none,none
1614,C,Mobility Bathworks of AZ,"Tolleson, AZ",(908) 930-7894,"10297 W Van Buren St #8, Tolleson, AZ 85353",https://www.google.com/maps/place/?q=place_id:ChIJTQSs7PY_K4cRScSUK2V1HUQ&hl=en,none,none,none,none
1615,C,Patrick's Cabinets,"Yucaipa, CA",(909) 823-2524,"31710 Dunlap Blvd, Yucaipa, CA 92399",https://www.google.com/maps/place/?q=place_id:ChIJA8-LknlX24ARYsGmCgX3cH4&hl=en,none,none,none,none
1616,C,Figueroa Remodeling,"Salisbury, NC",(980) 565-1835,"205 Cornwall Dr, Salisbury, NC 28147",https://www.google.com/maps/place/?q=place_id:ChIJ5eDZSPT1U4gRAy2ZhrRZS6g&hl=en,none,none,none,none
1617,C,FLAWLESS REMODELING LLC,"Panama City, FL",(850) 630-5733,"2100 W Beach Dr, Panama City, FL 32401",https://www.google.com/maps/place/?q=place_id:ChIJnZDDhv-Hk4gRn9UMx0zJeHI&hl=en,none,none,none,none
1618,C,Whole House Rescue,"Elgin, TX",(512) 999-0001,"213 Warner Dr, Elgin, TX 78621",https://www.google.com/maps/place/?q=place_id:ChIJn9CyE3l2_qkR-HtQs08RBaE&hl=en,none,none,none,none
1619,C,Designed By Julie LLC,"Midland, MI",(989) 835-1200,"608 S Saginaw Rd, Midland, MI 48640",https://www.google.com/maps/place/?q=place_id:ChIJwR5h76PVI4gR6L8d8Rc5ZmM&hl=en,none,none,none,none
1620,C,HB Kitchen Designs,"Spring Hill, TN",(317) 599-8744,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0drBA3aCY4gRDxmFq9ZVNIA&hl=en,none,none,none,none
1621,C,Flores Remodeling,"River Grove, IL",(773) 968-8731,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbaJbc93LD4gRt3gIS4LEoME&hl=en,none,none,none,none
1622,C,DANIVAL BUILDERS INC,"St. Cloud, FL",(407) 663-1948,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv_FIxxbtsIsReHuDt5ChHq0&hl=en,none,none,none,none
1623,C,King's Tile,"El Paso, TX",(915) 305-0874,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJp_MHrtxF54YRtk0aGUZYQSg&hl=en,none,none,none,none
1624,C,Di Vinci Tile Inc,"Lockport, IL",(630) 885-4562,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6Y55SUDtYG4RbUhYMm72_9Q&hl=en,none,none,none,none
1625,C,Quality Works LLC,"Glenarden, MD",(954) 496-4066,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJn2MFcdjR84UR_CuLpnLw4vo&hl=en,none,none,none,none
1626,C,Transitions Remodeling,"Farmington Hills, MI",(248) 260-2468,"27260 Haggerty Rd Ste A1, Farmington Hills, MI 48331",https://www.google.com/maps/place/?q=place_id:ChIJ3W2nrcWvJIgRDnHd-dQ63pI&hl=en,none,none,none,none
1627,C,A Tile God,"East Point, GA",(678) 879-2834,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJN5NARLId9YgRQ3uPXnLkBIA&hl=en,none,none,none,none
1628,C,RLS CABINET INSTALLATION,"Cottonwood, AZ",(928) 300-5710,"860 S Oasis Dr, Cottonwood, AZ 86326",https://www.google.com/maps/place/?q=place_id:ChIJKww_gSAFLYcR-aoIzFrX1Nw&hl=en,none,none,none,none
1629,C,Complete Interiors,"Edmond, OK",(405) 820-1039,"2320 S Kelly Ave, Edmond, OK 73013",https://www.google.com/maps/place/?q=place_id:ChIJc00pswUPsocRREPYud92TQU&hl=en,none,none,none,none
1630,C,Unique Woodworks,"Sedalia, MO",(660) 281-2323,"6501 Willow Brook Rd, Sedalia, MO 65301",https://www.google.com/maps/place/?q=place_id:ChIJq_i5_lCBw4cR-7MPdn1jlQ4&hl=en,none,none,none,none
1631,C,CJC Construction LLC,"St. Michael, MN",(612) 203-6322,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJF_2fJQQcSiMRHairLD1Kkfw&hl=en,none,none,none,none
1632,C,Bluey Construction,"East Moline, IL",(309) 944-7800,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQX-W3UOhtQURaXEcyfrKzKo&hl=en,none,none,none,none
1633,C,JYS CUSTOM CABINETS,"Klamath Falls, OR",(541) 331-4228,"4100 Washburn Way, Klamath Falls, OR 97603",https://www.google.com/maps/place/?q=place_id:ChIJuX8ZP9fVyFQRTG8oAgO94aQ&hl=en,none,none,none,none
1634,C,Fancy Granite - Marble Countertop and more,"Madisonville, KY",(404) 732-3451,"1385 Briarwood Dr, Madisonville, KY 42431",https://www.google.com/maps/place/?q=place_id:ChIJu6GxZSb_b4gRnyi7mYCAGEk&hl=en,none,none,none,none
1635,C,Just Countertops,"Flat Rock, MI",(734) 782-1870,"26464 W Huron River Dr, Flat Rock, MI 48134",https://www.google.com/maps/place/?q=place_id:ChIJXQ-mG-BAO4gR3lA2U_IqWYw&hl=en,none,none,none,none
1636,C,A&D Kitchen Bath Remodeling,"Norfolk, VA",(757) 318-8369,"234 A View Ave, Norfolk, VA 23503",https://www.google.com/maps/place/?q=place_id:ChIJ3Yd0_MGQuokR7smaOKl4suk&hl=en,none,none,none,none
1637,C,Arnie's Remodeling,"Harlingen, TX",(956) 659-4499,"517 N P St, Harlingen, TX 78550",https://www.google.com/maps/place/?q=place_id:ChIJ_64v1u6Bb4YRImWe7R1hYMY&hl=en,none,none,none,none
1638,C,Oasis Baths Remodels,"Lakewood, CA",(801) 389-1601,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJIUcKqPZGayMRFathYY2vlcU&hl=en,none,none,none,none
1639,C,TRC REMODELING,"East Cleveland, OH",(216) 858-0728,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJh_x2j3LbBkwRWVzlWlEFfMQ&hl=en,none,none,none,none
1640,C,DNA CONSTRUCTION 1 LLC,"Harrison, NJ",(551) 580-5040,"59 Washington St, Harrison, NJ 07029",https://www.google.com/maps/place/?q=place_id:ChIJQ4PjuKVVwokRnEnrqPolf6g&hl=en,none,none,none,none
1641,C,Garza Surface Co.,"Haskell, AR",(870) 686-7272,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ2aqB4_GnMYgR8ZxGfedMEME&hl=en,none,none,none,none
1642,C,Next Level Lakewood Flooring & Remodel,"Lakewood, OH",(216) 279-9911,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTYNi8G_zMIgRndBJ6-v05-s&hl=en,none,none,none,none
1643,C,Tailored Stone Inc,"Plover, WI",(715) 341-0100,"1411 Contractors Blvd A, Plover, WI 54467",https://www.google.com/maps/place/?q=place_id:ChIJm5k8aABaAIgR-3zjIANQ7wQ&hl=en,none,none,none,none
1644,C,"Exquisite Selection - Tile, Kitchen, Bath, Closets","Marathon, FL",(786) 333-4712,"71 53rd St, Marathon, FL 33050",https://www.google.com/maps/place/?q=place_id:ChIJoe99Wkff0IgRE071FVTi6WY&hl=en,none,none,none,none
1645,C,Argento Marble & Granite Inc,"Carbondale, CO",(970) 963-7070,"1101 Dolores Way, Carbondale, CO 81623",https://www.google.com/maps/place/?q=place_id:ChIJMVj1ZOqrQYcRAT8ewRtWmL8&hl=en,none,none,none,none
1646,C,Adam's Tile & Bathroom Remodels,"Corpus Christi, TX",(361) 429-8813,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdUwZFMf1aIYRbd76S2wl2Ig&hl=en,none,none,none,none
1647,C,Dapper Tile and Remodel,"Ozark, MO",(417) 414-8327,"1405 Frosty Dr, Ozark, MO 65721",https://www.google.com/maps/place/?q=place_id:ChIJ-fZ7oHFxz4cRqhmh5hnOKbk&hl=en,none,none,none,none
1648,C,Shaffer's Cabinets,"Lawrenceburg, TN",(931) 762-1920,"174 Harvester Ave, Lawrenceburg, TN 38464",https://www.google.com/maps/place/?q=place_id:ChIJA8obIDAhY4gReF19jnd7Sk4&hl=en,none,none,none,none
1649,C,Del Rocco Tile,"Raritan, NJ",(908) 268-2296,"400 US-202 S, Raritan, NJ 08869",https://www.google.com/maps/place/?q=place_id:ChIJy35AtS6Vw4kRqx-OiP6Ztl8&hl=en,none,none,none,none
1650,C,Tub Doctor,"Jackson, TN",(731) 927-9000,"2957 Old Medina Rd, Jackson, TN 38305",https://www.google.com/maps/place/?q=place_id:ChIJA6Bj1vGgfogRGUqPFcOMLiQ&hl=en,none,none,none,none
1651,C,Villegas Cabinets,"Edinburg, TX",(956) 688-0460,"1603 Silver St, Edinburg, TX 78542",https://www.google.com/maps/place/?q=place_id:ChIJk9vLysWfZYYRy1TbrNC67yY&hl=en,none,none,none,none
1652,C,Essence Bathroom Remodeling,"Baton Rouge, LA",(225) 370-8011,"6636 Harry Dr, Baton Rouge, LA 70806",https://www.google.com/maps/place/?q=place_id:ChIJq6p6VMKjJoYRMIEIrqxox00&hl=en,none,none,none,none
1653,C,Perez Cabinets & Trim,"Brenham, TX",(979) 203-9444,"4628 FM389, Brenham, TX 77833",https://www.google.com/maps/place/?q=place_id:ChIJ6yCGwQcDRIYRUrU8-pKNH3I&hl=en,none,none,none,none
1654,C,Bath Solutions By Walker,"Bucyrus, OH",(419) 468-5072,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJeYaMw8mZOYgRbWRxNlYDXtg&hl=en,none,none,none,none
1655,C,AP Restoration,"Greenwood, SC",(864) 227-2777,"906 Montague Ave, Greenwood, SC 29649",https://www.google.com/maps/place/?q=place_id:ChIJCerepgcB-IgRWAZbQvMIeas&hl=en,none,none,none,none
1656,C,Stallings Cabinets,"Elizabeth City, NC",(252) 338-6747,"508 N Hughes Blvd, Elizabeth City, NC 27909",https://www.google.com/maps/place/?q=place_id:ChIJz8qyZHZFpYkRbSEbNTS2tHk&hl=en,none,none,none,none
1657,C,Grenada Cabinet & Furniture Co,"Grenada, MS",(662) 417-4271,"2217 McCormick Rd, Grenada, MS 38901",https://www.google.com/maps/place/?q=place_id:ChIJ0XAnT8PLgYgRf7qs3yRyDTQ&hl=en,none,none,none,none
1658,C,David's Tile and Laminate,"Cortez, CO",(970) 560-6202,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ9ZygJsZ4wmERNsGGzTLB2L4&hl=en,none,none,none,none
1659,C,CKD Kitchen & Bath,"Bremen, GA",(404) 886-5944,"1159 Pacific Ave, Bremen, GA 30110",https://www.google.com/maps/place/?q=place_id:ChIJUUSeS1zZiogRVa-iFGyXMGA&hl=en,none,none,none,none
1660,C,Arthur Stone Tile,"Darien, CT",(203) 604-3064,"205 1/2 West Ave, Darien, CT 06820",https://www.google.com/maps/place/?q=place_id:ChIJ7eKFCFeR0CcROXdrogitCkw&hl=en,none,none,none,none
1661,C,long island kitchen and bath in Huntington,"Huntington Station, NY",(631) 905-8083,"E 17th St, Huntington Station, NY 11746",https://www.google.com/maps/place/?q=place_id:ChIJw7lA2rsp6IkRorKc5odkncI&hl=en,none,none,none,none
1662,C,Elite Custom Cabinetry,"Schofield, WI",(715) 355-5007,"6005 Mesker St, Schofield, WI 54476",https://www.google.com/maps/place/?q=place_id:ChIJtbUkT4wlAIgRBco08G2n68Y&hl=en,none,none,none,none
1663,C,Shultz Contracting,"Lima, OH",(567) 712-9571,"1000 S Kemp Rd, Lima, OH 45806",https://www.google.com/maps/place/?q=place_id:ChIJbaELTaz3PogRLBHyK3pJQ-Q&hl=en,none,none,none,none
1664,C,Complete home improvement and kitchens LLC,"Norwalk, CT",(203) 449-3051,"43 Creeping Hemlock Dr, Norwalk, CT 06851",https://www.google.com/maps/place/?q=place_id:ChIJ6bsmJGMO6IkRNkKvZEl02A4&hl=en,none,none,none,none
1665,C,Bell's Cabinetry,"Jacksonville, AR",(501) 982-8225,"1712 General Samuels Rd, Jacksonville, AR 72076",https://www.google.com/maps/place/?q=place_id:ChIJ_zz4nt_q0ocRpBsykvyTeQg&hl=en,none,none,none,none
1666,C,Calhoun Granite Countertops,"Calhoun, GA",(706) 403-9563,"615 W Belmont Dr, Calhoun, GA 30701",https://www.google.com/maps/place/?q=place_id:ChIJ4bVGC90BYIgRcuxbkrXnOdU&hl=en,none,none,none,none
1667,C,Wills Builders,"Warren, PA",(814) 723-4190,"1513 Pennsylvania Ave W # C, Warren, PA 16365",https://www.google.com/maps/place/?q=place_id:ChIJ2d1zV6ZFzYkRH8g05tVK7k4&hl=en,none,none,none,none
1668,C,"Smooth Touch Remodel, LLC","Rogers, AR",(479) 877-1912,"123 W Elm St, Rogers, AR 72756",https://www.google.com/maps/place/?q=place_id:ChIJy6BYlgUXyYcRmnybxS2EmwY&hl=en,none,none,none,none
1669,C,Happy Kitchen and Bath 888 LLC,"Huntsville, AL",(256) 517-8647,"9023 Memorial Pkwy SW, Huntsville, AL 35802",https://www.google.com/maps/place/?q=place_id:ChIJ9zUpRKgTYogR23y0dRoMK4o&hl=en,none,none,none,none
1670,C,Elite Bathroom Remodeling Stockton,"Stockton, CA",(209) 713-5105,"2535 Wigwam Dr, Stockton, CA 95205",https://www.google.com/maps/place/?q=place_id:ChIJ2T1RkLZykIAR916bz3b39K8&hl=en,none,none,none,none
1671,C,Los Angeles Bathroom & Kitchen Remodeling.,"Los Angeles, CA",(213) 808-6909,"322 S Reno St, Los Angeles, CA 90057",https://www.google.com/maps/place/?q=place_id:ChIJqQA4J5fHwoARjaMiqn_mwM0&hl=en,none,none,none,none
1672,C,Z&H Kitchen Cabinetry Inc.,"Weymouth, MA",(781) 812-0738,"373 Washington St, Weymouth, MA 02188",https://www.google.com/maps/place/?q=place_id:ChIJjzUhlwqd5IkRCLjx541f62w&hl=en,none,none,none,none
1673,C,New Vista Rock Marble Granite & Quartz,"Angleton, TX",(281) 508-6932,"349 County Rd 840, Angleton, TX 77515",https://www.google.com/maps/place/?q=place_id:ChIJJdY1iYpDQIYROuaUWWwH0tc&hl=en,none,none,none,none
1674,C,"Reel and Sons, LLC","Snow Camp, NC",(919) 578-3330,"2255 Quakenbush Rd, Snow Camp, NC 27349",https://www.google.com/maps/place/?q=place_id:ChIJKSZDrZHJaogRjnUSanY_p6o&hl=en,none,none,none,none
1675,C,Above & Beyond Construction and Renovations LLC,"Kernersville, NC",(336) 505-1120,"1215 Birch Hill Dr, Kernersville, NC 27284",https://www.google.com/maps/place/?q=place_id:ChIJm7wqx1YHU4gRsFuCjq1qGAQ&hl=en,none,none,none,none
1676,C,B&L HOME RENOVATIONS,"Glastonbury, CT",(860) 328-0618,"2389 Main St Ste 100, Glastonbury, CT 06033",https://www.google.com/maps/place/?q=place_id:ChIJ-_qaI15R5okRoCC1UWcGH0s&hl=en,none,none,none,none
1677,C,Built 2 Suit,"Shelbina, MO",(636) 248-8554,"123 E Walnut St, Shelbina, MO 63468",https://www.google.com/maps/place/?q=place_id:ChIJL6xDS-xt3YcR0ap6KyXyykE&hl=en,none,none,none,none
1678,C,Trinity Kitchen Remodeling,"Fresno, CA",(559) 315-6878,"3604 W Gettysburg Ave, Fresno, CA 93722",https://www.google.com/maps/place/?q=place_id:ChIJr8QH1L9ElIARZDP3eiOnvQI&hl=en,none,none,none,none
1679,C,"Dimensional Contracting Services LLC, Remodeling Contractor","Lauderdale Lakes, FL",(754) 244-8302,"2790 Somerset Dr, Lauderdale Lakes, FL 33311",https://www.google.com/maps/place/?q=place_id:ChIJeeYdNLQG2YgRfZJ4EYrZjqg&hl=en,none,none,none,none
1680,C,Elite Bathrooms LLC,"Jefferson, GA",(678) 382-9323,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdfQXLeIO-CQRaPQYp8Xq1m0&hl=en,none,none,none,none
1681,C,Brothers Cabinetry,"Oneonta, AL",(256) 490-7958,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJK67bGO0yuwgRaoXuMLoSu_8&hl=en,none,none,none,none
1682,C,Highland Handyman Services LLC,"Grantsville, UT",(928) 965-0014,"464 S Madeline Ct, Grantsville, UT 84029",https://www.google.com/maps/place/?q=place_id:ChIJszb86c43B6ERpswhMI9IJLk&hl=en,none,none,none,none
1683,C,HSP Kitchen Remodel,"Renton, WA",(425) 620-7898,"201 Taylor Ave NW Unit 102/b, Renton, WA 98057",https://www.google.com/maps/place/?q=place_id:ChIJB8AL4WRDkFQReG5oJi9LyZU&hl=en,none,none,none,none
```
