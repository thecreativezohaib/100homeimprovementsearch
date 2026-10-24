# Round 2: Gemini task 2, part 07 of 17 (100 businesses, rows 1684 to 1783)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 1783: reply in that chat "Continue with
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
1684,C,G & G Maintenance and Repair,"Wasco, CA",(661) 529-5973,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzyFpRku4LIsRVQOEne0Y-Eo&hl=en,none,none,none,none
1685,C,D&E Remodeling,"Riverdale, GA",(470) 302-7375,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJUTiiyJ9okoERuF3ATW4y5Hk&hl=en,none,none,none,none
1686,C,Rhino Tile,"Shoreview, MN",(651) 226-1254,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-WslCSAhMqoRGg4TH8rQlBs&hl=en,none,none,none,none
1687,C,Home Accents,"Rancho Cucamonga, CA",(909) 481-1147,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJPbCjc-E1w4ARUMIIp5UvVHY&hl=en,none,none,none,none
1688,C,Classic Contracting LLC,"Beachwood, NJ",(732) 503-9608,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJuZfZFDMk-kcR-5MvxsqF8Wg&hl=en,none,none,none,none
1689,C,Natural Surroundings Remodeling,"Monroeville, PA",(412) 855-3402,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ___LT_nBNIgR-hiqgQmHcDg&hl=en,none,none,none,none
1690,C,Flip Flop Kitchen Refresh,"Leland, NC",(910) 988-3306,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZSecEqwyCy4ROv78-iCfjrQ&hl=en,none,none,none,none
1691,C,Kelly Interior & Exterior Remodeling,"Cleveland, TN",(423) 331-1099,"211 Burl Oaks Dr NE, Cleveland, TN 37323",https://www.google.com/maps/place/?q=place_id:ChIJbeyEqN7vvgURoCL84BM_8Fs&hl=en,none,none,none,none
1692,C,Do it Right Remodeling,"Hudson Oaks, TX",(817) 903-9228,"208 Rob Ln, Hudson Oaks, TX 76087",https://www.google.com/maps/place/?q=place_id:ChIJNyYFpvINToYR5CzztqsgxjQ&hl=en,none,none,none,none
1693,C,West Covina Bathroom & Kitchen Remodel,"West Covina, CA",(626) 317-6060,"235 N Azusa Ave g, West Covina, CA 91791",https://www.google.com/maps/place/?q=place_id:ChIJq9CfSp8pw4ARSTmEDCbn-oA&hl=en,none,none,none,none
1694,C,Mr. Backsplash,"Rosemount, MN",(651) 341-2226,"15146 Cimarron Ct, Rosemount, MN 55068",https://www.google.com/maps/place/?q=place_id:ChIJFRlfkYA09ocROqR4VeW_q-k&hl=en,none,none,none,none
1695,C,Guy Mouton Carpentry - Remodeling and Home Maintenance,"Woodstock, IL",(847) 774-5989,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQ3DM_LBpD4gRdRBL-0ESz6g&hl=en,none,none,none,none
1696,C,Granite Repair,"Versailles, KY",(769) 867-4450,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXxYpbyVFAk4RnZROo9B28zI&hl=en,none,none,none,none
1697,C,Etowah Cabinet Shop,"Attalla, AL",(256) 538-9698,"2600 US-11, Attalla, AL 35954",https://www.google.com/maps/place/?q=place_id:ChIJwR0nnoYkiogR8pyNQFygE_s&hl=en,none,none,none,none
1698,C,One Project Llc,"Wayne, MI",(248) 795-9161,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJrQgBhjtNO4gR8cigVLBNKZ8&hl=en,none,none,none,none
1699,C,Elevated Services LLC,"Ruidoso, NM",(575) 937-3752,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ66PU6uOT-KMROivkoNxEays&hl=en,none,none,none,none
1700,C,Alpha Omega Construction,"Pico Rivera, CA",(562) 569-0765,"5213 Calico Ave, Pico Rivera, CA 90660",https://www.google.com/maps/place/?q=place_id:ChIJHca3LYXxEgwRc1vFUDwL6fs&hl=en,none,none,none,none
1701,C,Sanctum Inc,"Mequon, WI",(262) 900-5500,"12502 N River Rd, Mequon, WI 53092",https://www.google.com/maps/place/?q=place_id:ChIJ69wuvryoeUkR2MsZTlwoiUY&hl=en,none,none,none,none
1702,C,RTH REMODELING LLC,"Tucker, GA",(770) 866-2478,"4083 Adrian St, Tucker, GA 30084",https://www.google.com/maps/place/?q=place_id:ChIJOzFjlXGn9YgRBM0yPw5CYtA&hl=en,none,none,none,none
1703,C,PR Fonseca,"Justin, TX",(469) 903-7944,"18001 Cindy's Ln, Justin, TX 76247",https://www.google.com/maps/place/?q=place_id:ChIJK3p7bQzFTYYRQB44p7Z4ZdI&hl=en,none,none,none,none
1704,C,Mica-Jim’s kitchen & Bath,"Port Richey, FL",(727) 845-8719,"7922 Grand Blvd, Port Richey, FL 34668",https://www.google.com/maps/place/?q=place_id:ChIJS7F0BheQwogRKBNRpsSdtLY&hl=en,none,none,none,none
1705,C,"Swing Cabinets, LLC","Shelbyville, TN",(931) 684-3576,"331 Pinkston Rd, Shelbyville, TN 37160",https://www.google.com/maps/place/?q=place_id:ChIJ8fa121_pY4gRWb8ZnmjO4Zs&hl=en,none,none,none,none
1706,C,Rocha's Cabinets,"Manteca, CA",(209) 239-2367,"108 Industrial Park Dr, Manteca, CA 95012",https://www.google.com/maps/place/?q=place_id:ChIJzVnEOQBBkIARq0pkx1tYtSM&hl=en,none,none,none,none
1707,C,Galux Custom Cabinets,"Franklin Park, IL",(773) 440-5950,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJafESmhW1D4gRprNwDdcqLxA&hl=en,none,none,none,none
1708,C,"D & N Cabinetry, Inc.","Sebring, FL",(863) 471-1500,"2920 Kenilworth Blvd, Sebring, FL 33870",https://www.google.com/maps/place/?q=place_id:ChIJQ1026E9X3IgRKk2vyUipLTU&hl=en,none,none,none,none
1709,C,Utter Clutter - Cabinet Painting & Specialty Finishes,"Madison, AL",(256) 479-1589,"7670 Old Madison Pike, Madison, AL 35758",https://www.google.com/maps/place/?q=place_id:ChIJISYFJm5vYogRNpfFv9TAgRY&hl=en,none,none,none,none
1710,C,"Pacific Building Resources, Inc.","Sammamish, WA",(206) 458-1908,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJT3JfpB930EURlUl8WLggkNg&hl=en,none,none,none,none
1711,C,White Rose City Remodeling Co,"York, PA",(717) 722-9373,"250 Cross Farm Ln, York, PA 17406",https://www.google.com/maps/place/?q=place_id:ChIJr260aNCTyIkR9UGHn872hSM&hl=en,none,none,none,none
1712,C,Shamrock Cabinets,"Jasper, IN",(812) 482-7969,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJr6zFXldkbogRqeDy7HTGAlA&hl=en,none,none,none,none
1713,C,M2 Renovations LLC,"East Point, GA",(404) 788-0387,"2568 Semmes St, East Point, GA 30344",https://www.google.com/maps/place/?q=place_id:ChIJNzB5waQd9YgR9ZE0HBFCL2A&hl=en,none,none,none,none
1714,C,Full Service Remodeling,"Dublin, GA",(478) 279-7725,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJrzx33e7d8IgR1RLK5kTCT-Y&hl=en,none,none,none,none
1715,C,Up 2 You cabinets designs and renovations,"Seagoville, TX",(682) 406-3938,"1503 Bruce Way, Seagoville, TX 75159",https://www.google.com/maps/place/?q=place_id:ChIJ0aL8biOnToYR7YmppeWXrws&hl=en,none,none,none,none
1716,C,"J. Miller Cabinet Company, Inc.","Columbia City, IN",(260) 691-2032,"5874 N 350 E, Columbia City, IN 46725",https://www.google.com/maps/place/?q=place_id:ChIJSTgDaml3FogRHzVzEhydZ_w&hl=en,none,none,none,none
1717,C,Gabinetto Modern,"Lighthouse Point, FL",(786) 229-0288,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJjZmBJjTj2IgRVGTFzGG3B-g&hl=en,none,none,none,none
1718,C,Kitchen Makeover Express,"Massapequa Park, NY",(855) 569-7737,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ3TvK9MyMsAwRmVQq1Y6-kVk&hl=en,none,none,none,none
1719,C,Windows & Wood LLC,"Milledgeville, GA",(478) 443-4589,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ4cVspLZLSCQRWLRo6DAsU6Q&hl=en,none,none,none,none
1720,C,Spahn Cabinets,"Van Buren, AR",(479) 474-8024,"2620 Kibler Rd, Van Buren, AR 72956",https://www.google.com/maps/place/?q=place_id:ChIJi2EV1jC0y4cR55GAbZQO9vA&hl=en,none,none,none,none
1721,C,Axia Construction Co,"Union City, NJ",(201) 970-1973,"902 17th St, Union City, NJ 07087",https://www.google.com/maps/place/?q=place_id:ChIJ31KgiI9XwokRF7KvwsFqr9A&hl=en,none,none,none,none
1722,C,Bath Remodel Pro Inc.,"Watervliet, NY",(518) 838-0798,"7 Maple Ave, Watervliet, NY 12189",https://www.google.com/maps/place/?q=place_id:ChIJO4G1wEwO3okRtkSXNGE1qWk&hl=en,none,none,none,none
1723,C,"KirkBath, Kirk Kitchen","Albany, OR",(541) 758-0776,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJK_I1CZJAwFQRblNfWzIqJTA&hl=en,none,none,none,none
1724,C,Kitchen Kit,"Montclair, NJ",(973) 606-8282,"666 Bloomfield Ave, Montclair, NJ 07042",https://www.google.com/maps/place/?q=place_id:ChIJTQGMj8D_wokR4ZMLM3Z7Bwg&hl=en,none,none,none,none
1725,C,Roundabout Capital Bath Remodeling Co,"Carmel, IN",(463) 273-3781,"11708 N College Ave, Carmel, IN 46032",https://www.google.com/maps/place/?q=place_id:ChIJARob1hqtFIgRdG7m6nHKUb8&hl=en,none,none,none,none
1726,C,Maracaibo Closets Llc,"Opa-locka, FL",(786) 569-2415,"14103 NW 19th Ave, Opa-locka, FL 33054",https://www.google.com/maps/place/?q=place_id:ChIJPRLqtCOv2YgRjKLhwvV_yHM&hl=en,none,none,none,none
1727,C,Unique By Design,"Van Alstyne, TX",(214) 661-0905,"239 S John Douglas Rd, Van Alstyne, TX 75495",https://www.google.com/maps/place/?q=place_id:ChIJv2auWR9wTIYR_j33nAtZoOE&hl=en,none,none,none,none
1728,C,Strong Line LLC,"Everett, WA",(425) 539-8773,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZ2Ofy_ZAfy8R1DbDxTo-1k4&hl=en,none,none,none,none
1729,C,Shaker Flooring & Remodel,"Warrensville Heights, OH",(216) 488-1180,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJKWFRewO2KgwR-QYcYDkPi5Y&hl=en,none,none,none,none
1730,C,Right Way Renovations,"St. Marys, GA",(470) 383-6597,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ90Z__3YagEARqEkiMsKrIHc&hl=en,none,none,none,none
1731,C,"CHIC Services, LLC","Cicero, IL",(312) 690-1292,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTxTkVnI1DogRNeDqbbrRj5A&hl=en,none,none,none,none
1732,C,Nik Home Solutions LLC,"Apopka, FL",(407) 552-9515,"903 Haas Ave, Apopka, FL 32703",https://www.google.com/maps/place/?q=place_id:ChIJz1lFzuB354gRGBTWu_dCNkw&hl=en,none,none,none,none
1733,C,DFW Trade Pros,"Everman, TX",(817) 666-2978,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTauLBwhjsYwRdKlAXxnlWlg&hl=en,none,none,none,none
1734,C,MARIO TILES LLC,"Wharton, NJ",(862) 291-6672,"163 Baker Ave, Wharton, NJ 07885",https://www.google.com/maps/place/?q=place_id:ChIJrw5eUSzVogkReo5ovpQc9IU&hl=en,none,none,none,none
1735,C,Navisa Custom Countertops LLC,"DeSoto, TX",(214) 586-4875,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ07_k1nhNHCsRUyfFf_HRGuI&hl=en,none,none,none,none
1736,C,Improved Space LLC,"Norton, MA",(781) 897-1730,"255 S Worcester St, Norton, MA 02766",https://www.google.com/maps/place/?q=place_id:ChIJ10ZiRW1444kRcV_8ViNcQhY&hl=en,none,none,none,none
1737,C,Roberts Stone Products,"Shelbyville, KY",(502) 844-2107,"1073 Brooks Industrial Rd, Shelbyville, KY 40065",https://www.google.com/maps/place/?q=place_id:ChIJDYOWPxDAaYgRHTNA7RN2tx0&hl=en,none,none,none,none
1738,C,Rub A Dub Tub Reglazing Baltimore County,"Taneytown, MD",(443) 790-4974,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJObp27DBLyIkRtSe7GbEm6e0&hl=en,none,none,none,none
1739,C,Newtown Kitchen and Bath,"Southbury, CT",(203) 887-1177,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-7Xq8-u0r2sR8VwUU34lFkY&hl=en,none,none,none,none
1740,C,J&M floor and Bathroom Construction,"Palmetto Bay, FL",(786) 608-0337,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbxLHaDTF2YgRZG6U8L1I5uA&hl=en,none,none,none,none
1741,C,VAV Construction Corp- Remodeling- Contractor,"Calumet City, IL",(872) 238-9920,"1215 Hirsch Ave, Calumet City, IL 60409",https://www.google.com/maps/place/?q=place_id:ChIJ99l6UBCzhqURnhMf-gQRhrk&hl=en,none,none,none,none
1742,C,Granite State Contracting,"Litchfield, NH",(603) 831-6166,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6fnoQcPL44kRFeYrfjjnZLI&hl=en,none,none,none,none
1743,C,"Neches Construction Group, LLC","Beaumont, TX",(409) 293-2791,"3195 Dowlen Rd, Beaumont, TX 77706",https://www.google.com/maps/place/?q=place_id:ChIJgzTYI2dNnC4RojgyQEvp5xQ&hl=en,none,none,none,none
1744,C,Diamond Remodeling,"Syracuse, NY",(315) 256-2012,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJz94vH6KI3QsRLQJqkOXR1do&hl=en,none,none,none,none
1745,C,Smart Home Construction Inc.,"Wheeling, IL",(847) 220-6680,"3000 Burlington Cir, Wheeling, IL 60090",https://www.google.com/maps/place/?q=place_id:ChIJ10ulQT2_D4gRYZXFjsQvOEA&hl=en,none,none,none,none
1746,C,RBK Wood Gallery,"Ridgefield Park, NJ",(201) 281-1191,"30 Paulison Ave, Ridgefield Park, NJ 07660",https://www.google.com/maps/place/?q=place_id:ChIJAQCcQWD3wokRiRm8WmDj7rI&hl=en,none,none,none,none
1747,C,"RT Custom Cabinets, Trim, & Remodels","Eufaula, OK",(918) 689-0202,"328 Hamilton Rd 5 Miles East Of Eufaula On, OK-9, Eufaula, OK 74432",https://www.google.com/maps/place/?q=place_id:ChIJt36vAPyltYcRkI8iMyCQcf0&hl=en,none,none,none,none
1748,C,Kitchen & Bathroom Remodel Lakewood,"Signal Hill, CA",(562) 512-6691,"2619 Lime Ave CA  #4, Signal Hill, CA 90755",https://www.google.com/maps/place/?q=place_id:ChIJS-rbJcgz3YARmwxGWX6aKfg&hl=en,none,none,none,none
1749,C,Perque Cabinets and Counter tops,"Houma, LA",(985) 360-3450,"6189 W Main St, Houma, LA 70360",https://www.google.com/maps/place/?q=place_id:ChIJ1Qz1e3UQIYYR1uU00WNlqaU&hl=en,none,none,none,none
1750,C,"Inspired Touches, LLC","Douglasville, GA",(404) 468-1869,"3848 Willow Ridge Ct, Douglasville, GA 30135",https://www.google.com/maps/place/?q=place_id:ChIJmZj_QQMn9YgRciawWx9qbmQ&hl=en,none,none,none,none
1751,C,The Cabinet Store,"Pascagoula, MS",(228) 627-1943,"1404 Live Oak Ave, Pascagoula, MS 39567",https://www.google.com/maps/place/?q=place_id:ChIJuX9CyM_om4gRen_tukTSzwc&hl=en,none,none,none,none
1752,C,Battin Kitchen Designs,"Cochranton, PA",(814) 573-2780,"156 N Franklin St, Cochranton, PA 16314",https://www.google.com/maps/place/?q=place_id:ChIJjX65iFP-MogRcqQ_LYCHrBI&hl=en,none,none,none,none
1753,C,Barry's Kitchen Cabinets & More,"Chippewa Falls, WI",(715) 703-3160,"16904 Co Hwy X, Chippewa Falls, WI 54729",https://www.google.com/maps/place/?q=place_id:ChIJyzBHpfyp-IcREqqnZcWVpMw&hl=en,none,none,none,none
1754,C,R&S Home Remodelers,"Manchester, NH",(603) 361-1138,"500 Harvey Rd #201, Manchester, NH 03103",https://www.google.com/maps/place/?q=place_id:ChIJ93gaeW9F4okRYzRikkeWWCc&hl=en,none,none,none,none
1755,C,Chesapeake Perma Glaze South Inc.,"Bel Air, MD",(410) 688-4740,"1202 Glastonbury Way, Bel Air, MD 21014",https://www.google.com/maps/place/?q=place_id:ChIJq7KuvEbcx4kRlJVM9Fqklcg&hl=en,none,none,none,none
1756,C,Cabinets By Springfield,"Miami, OK",(918) 540-0505,"300 E BJ Tunnell Blvd, Miami, OK 74354",https://www.google.com/maps/place/?q=place_id:ChIJSTVawZcXyIcRe7wbiTRlSKk&hl=en,none,none,none,none
1757,C,"C & C Home Improvement, LLC","Moline, IL",(563) 449-6941,"1837 32nd St, Moline, IL 61265",https://www.google.com/maps/place/?q=place_id:ChIJzb9LbBwx4ocRMrDim-xOCK8&hl=en,none,none,none,none
1758,C,Remodeling fx,"Garfield Heights, OH",(216) 440-6347,"4962 E 71st St, Garfield Heights, OH 44125",https://www.google.com/maps/place/?q=place_id:ChIJ9y1OvRjlMIgRPeHNkpWtvTI&hl=en,none,none,none,none
1759,C,Mr Remodeler,"Kansas City, MO",(816) 453-3049,"4163 NE Winn Rd, Kansas City, MO 64117",https://www.google.com/maps/place/?q=place_id:ChIJtfMWjQX5wIcRw6dJOs9W9ls&hl=en,none,none,none,none
1760,C,Amazing Baths Bathroom Remodeling,"Londonderry, NH",(603) 932-7288,"73 Rockingham Rd Ste 2, Londonderry, NH 03053",https://www.google.com/maps/place/?q=place_id:ChIJYY_cvvZT4okRnMGetyNVNT4&hl=en,none,none,none,none
1761,C,Silverline Kitchens & Bath Inc,"Mamaroneck, NY",(718) 581-7567,"360 Mt Pleasant Ave # D, Mamaroneck, NY 10543",https://www.google.com/maps/place/?q=place_id:ChIJk9aUkPeRwokR9pc9HCvN7po&hl=en,none,none,none,none
1762,C,"Better Bath of NWA, Inc.","Camden, AR",(855) 932-3883,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDS1o1GAPyYcRHtqa4RMu1pI&hl=en,none,none,none,none
1763,C,Home Improvement Options,"Oxford, MA",(508) 987-3384,"193 Sutton Ave, Oxford, MA 01540",https://www.google.com/maps/place/?q=place_id:ChIJE1UEtugb5IkRL14vrPX_fo8&hl=en,none,none,none,none
1764,C,CleghornCabinets,"Warner Robins, GA",(478) 953-6996,"108 Constitution Dr, Warner Robins, GA 31088",https://www.google.com/maps/place/?q=place_id:ChIJ-V7d-tPm84gRK1eFqWnASnY&hl=en,none,none,none,none
1765,C,Fernando's Custom Cabinets,"Madera, CA",(559) 673-5712,"17463 Rd 26, Madera, CA 93638",https://www.google.com/maps/place/?q=place_id:ChIJ2Yg4Xk4JlIARCL0gyj2HL4I&hl=en,none,none,none,none
1766,C,MHDS Renovations,"Indiana, PA",(724) 427-5075,"494 Stannard Ave, Indiana, PA 15701",https://www.google.com/maps/place/?q=place_id:ChIJlxGgDP1by4kRLT7iOVCn7FY&hl=en,none,none,none,none
1767,C,Taylor's Tile and Flooring,"Arizona City, AZ",(480) 269-1464,"15861 Sunland Gin Rd, Arizona City, AZ 85123",https://www.google.com/maps/place/?q=place_id:ChIJY0MeTAB7KocRq-A8nUdGMNY&hl=en,none,none,none,none
1768,C,Spinks Stone Shop Granite and More,"Arkadelphia, AR",(870) 210-6199,"119 Malvern Rd, Arkadelphia, AR 71923",https://www.google.com/maps/place/?q=place_id:ChIJjWGsh3XfMoYRUlH3zwMl2-4&hl=en,none,none,none,none
1769,C,Woodshop,"Middlesboro, KY",(606) 248-7711,"705 19th St, Middlesboro, KY 40965",https://www.google.com/maps/place/?q=place_id:ChIJFYrvT9OEXIgRPmmCRwVMFvw&hl=en,none,none,none,none
1770,C,My Granite Company,"Dade City, FL",(813) 239-6040,"14923 US-301, Dade City, FL 33523",https://www.google.com/maps/place/?q=place_id:ChIJDRbmsECrwogRs3qq48-j_oo&hl=en,none,none,none,none
1771,C,Bates Home Improvement,"Ardmore, OK",(580) 264-0264,"16 S Washington St, Ardmore, OK 73401",https://www.google.com/maps/place/?q=place_id:ChIJ8SeBpcMvTYYRjlM7E5APoL8&hl=en,none,none,none,none
1772,C,Ray's Custom Cabinets & Remodeling Inc.,"Beaumont, TX",(409) 842-0866,"3675 S 11th St, Beaumont, TX 77705",https://www.google.com/maps/place/?q=place_id:ChIJpx2K9wrLPoYRJAY7Cw7_kkk&hl=en,none,none,none,none
1773,C,M G BATHTUB REPAIR,"Victorville, CA",(760) 900-6743,"12653 Field Way, Victorville, CA 92395",https://www.google.com/maps/place/?q=place_id:ChIJpS60CuyBt4cRLkTc1NKirIo&hl=en,none,none,none,none
1774,C,JCI Resurfacing,"Greenacres, FL",(561) 541-6215,"220 Fleming Ave, Greenacres, FL 33463",https://www.google.com/maps/place/?q=place_id:ChIJ55_I6Nkt2YgRKjIzD8lxdmw&hl=en,none,none,none,none
1775,C,Musk Construction Kitchen Remodeling Palo Alto,"Palo Alto, CA",(650) 668-0526,"335 Bryant St Ste 300, Palo Alto, CA 94301",https://www.google.com/maps/place/?q=place_id:ChIJscCbAogJaYgRic9wJ9TtC3w&hl=en,none,none,none,none
1776,C,Homes Restored,"Hutchinson, KS",(620) 931-6060,"5909 S Sandcreek Rd, Hutchinson, KS 67501",https://www.google.com/maps/place/?q=place_id:ChIJVZpMDRHJpIcRXiB0cw40rGk&hl=en,none,none,none,none
1777,C,Double Dog Construction,"Escanaba, MI",(906) 420-4163,"403 S 13th St, Escanaba, MI 49829",https://www.google.com/maps/place/?q=place_id:ChIJAy_wJp28TU0RislgcMGeqLw&hl=en,none,none,none,none
1778,C,Schmitt Renovations,"Stow, OH",(330) 696-9769,"2094 Samira Rd, Stow, OH 44224",https://www.google.com/maps/place/?q=place_id:ChIJrY_Bpy4nMYgRJB5ZqIdi3S8&hl=en,none,none,none,none
1779,C,HSP Bathroom Remodel,"Bremerton, WA",(360) 868-8279,"1015 9th St Unit C, Bremerton, WA 98337",https://www.google.com/maps/place/?q=place_id:ChIJUSEP97Q3kFQRWvo46nuFdCk&hl=en,none,none,none,none
1780,C,Heber City Utah Kitchen Remodeling,"Heber City, UT",(435) 236-3299,"136 S Main St, Heber City, UT 84032",https://www.google.com/maps/place/?q=place_id:ChIJSa69XwD1TYcRyagyYZ6tw1Y&hl=en,none,none,none,none
1781,C,Quad State Upgrades,"Joplin, MO",(417) 439-1352,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTaSEQ_YLKosRvUQDRYcGbG0&hl=en,none,none,none,none
1782,C,Renovations R&RLLC,"San Marcos, TX",(839) 263-7104,"1270 Willis Way, San Marcos, TX 78666",https://www.google.com/maps/place/?q=place_id:ChIJL-Bf64VZW4YR-bk9oT2VEDA&hl=en,none,none,none,none
1783,C,Solid Surfaces,"Jesup, GA",(912) 530-8595,"1909 Odum Hwy, Jesup, GA 31546",https://www.google.com/maps/place/?q=place_id:ChIJ1fJPf3TH-ogRfqjOk4dE0A8&hl=en,none,none,none,none
```
