# Round 2: Gemini task 3, part 07 of 22 (50 businesses: 9 F, 41 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1141, reply in that chat "Continue with the businesses
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
274,F,Queen City Renovation LLC,"Mint Hill, NC",(704) 989-3052,"10227 Connell Rd, Mint Hill, NC 28227",https://www.google.com/maps/place/?q=place_id:ChIJ-c2S_FgXVIgRumc6GT6zVlU&hl=en,none,https://www.instagram.com/queencityrenovation,none,none,none
277,F,Floor & Remodeling 360 LLC,"Altamonte Springs, FL",(407) 223-7301,"725 Northlake Blvd, Altamonte Springs, FL 32701",https://www.google.com/maps/place/?q=place_id:ChIJYZxn5mZn54gReD9VbjzXc-I&hl=en,https://www.facebook.com/profile.php?id=100044948150087,none,none,none,none
364,F,DJS Home Improvement - Miranda Property Service,"Beverly, MA",(978) 491-7315,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJoX3pQm3pxqARrdd6d1wmcTM&hl=en,none,https://www.instagram.com/djs.homeimprovement,none,Danilo Miranda,none
376,F,Elevation Renovation,"Layton, UT",(801) 510-9993,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJC2V5cPS73KsR9D6EJxcR3iU&hl=en,https://www.facebook.com/61560750775119,https://www.instagram.com/elevation.renovation/,none,BradleyClark,none
581,F,Cabinet & Countertop Solutions LLC,"Rockingham, NC",(910) 474-1447,"899 US-1, Rockingham, NC 28379",https://www.google.com/maps/place/?q=place_id:ChIJi3b3-fXDVIgR8PmZ00MfBfM&hl=en,https://www.facebook.com/share/19syQLQuqK/,none,none,none,none
250,F,Cabinet Refresh,"Norcross, GA",(678) 708-9585,"6350 McDonough Dr NW Suite K, Norcross, GA 30093",https://www.google.com/maps/place/?q=place_id:ChIJFdmr7ZOf9YgRwFBd9zkgN3c&hl=en,https://www.facebook.com/cabrefinishspecialist/,none,none,none,none
169,F,MB GRANITE QUARTZ & MARBLE,"Bossier City, LA",(318) 549-9000,"1009 Pearl Dr, Bossier City, LA 71111",https://www.google.com/maps/place/?q=place_id:ChIJz6gVa8wzMYYRa1ZmtWX2Suk&hl=en,https://www.facebook.com/61558109645015,none,none,none,none
45,F,Aguirre's Tile Services,"Heath, TX",(214) 407-2403,"University Dr, Forney, TX 75126",https://www.google.com/maps/place/?q=place_id:ChIJs6htyuysToYR9zeJVGiovUQ&hl=en,https://www.facebook.com/aguirrestileservices,none,none,none,none
369,F,Knighton Custom Kitchen and Bath LLC,"Ocala, FL",(352) 219-9773,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP8mmr_3SAC8RuEsCjCdhne8&hl=en,https://www.facebook.com/KCKB2022,none,none,none,none
1101,N,Pueblo Remodeling Company LLC,"Pueblo, CO",(719) 994-6008,"1216 Mass St, Pueblo, CO 81001",https://www.google.com/maps/place/?q=place_id:ChIJ00OwBzRd_QgRtu7ZTUtWmHM&hl=en,none,https://www.instagram.com/puebloremodelingcompanyllc,none,none,none
1102,N,J&S Custom Cabinets,"Joshua, TX",(817) 202-4603,"4701 County Rd 1017, Joshua, TX 76058",https://www.google.com/maps/place/?q=place_id:ChIJyb9n561BToYReUIXnFYVM1I&hl=en,https://www.facebook.com/JSCustomCabinets0015,none,none,none,none
1103,N,Creative Design Services Inc.,"Miami, FL",(786) 732-4046,"8760 SW 132nd St, Miami, FL 33176",https://www.google.com/maps/place/?q=place_id:ChIJ8YspV6vH2YgRq1xA-zxNGvg&hl=en,none,https://www.instagram.com/creative_design_services,none,none,none
1104,N,Jake Jordan Remodeling,"Kendallville, IN",(260) 341-2741,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdbtgJgUQFogRpudhy_245Nc&hl=en,https://www.facebook.com/Jake-Jordan-Remodeling-1040064359369363,none,none,none,none
1105,N,D’mendez tile and Tub Reglazing LLC,"Waterbury, CT",(347) 478-2222,"119 Store Ave, Waterbury, CT 06705",https://www.google.com/maps/place/?q=place_id:ChIJE9RBT2AVpwwRDU22S04f0Kc&hl=en,none,https://www.instagram.com/dmendeztileandtubreglazing,none,none,none
1106,N,PCH LATINO TILE & FLOORING LLC,"Auburn, AL",(334) 758-3193,"425 Webster Rd #124, Auburn, AL 36832",https://www.google.com/maps/place/?q=place_id:ChIJE8Pj1Gn1jIgRpp8Q38jgZFU&hl=en,https://www.facebook.com/profile.php?id=100092286463498,none,none,none,none
1107,N,SEK Construction,"Goshen, IN",(574) 226-9243,"57000 Downy Ct, Goshen, IN 46528",https://www.google.com/maps/place/?q=place_id:ChIJccRLjEHoFogR9lm_7djAVW8&hl=en,https://www.facebook.com/sekconstructionllc,none,none,none,none
1108,N,Chapman's Marble & Cabinets,"Morrilton, AR",(501) 354-1605,"121 W Railroad Ave, Morrilton, AR 72110",https://www.google.com/maps/place/?q=place_id:ChIJe6fFog91zYcRgkf30cEkQvI&hl=en,https://www.facebook.com/ChapmanFlooring1,none,none,none,none
1109,N,Hardwick Home Services,"Batesville, AR",(870) 806-4839,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJBx-SLQHI14ERpn_FZGS5as0&hl=en,http://facebook.com/Hardwickhomeservices,none,none,none,none
1110,N,Rusteberg Design,"Edwardsville, IL",(636) 575-3825,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJU-GOEg7ddYgRasOWCNuzGws&hl=en,https://www.facebook.com/RustebergDesign,none,none,none,none
1111,N,IG Remodeling Inc.,"Wauconda, IL",(773) 543-7509,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAX2WEqgs8mUReTOJW2YVPvw&hl=en,https://www.facebook.com/igremodelinginc,none,none,none,none
1112,N,"Quality Design Construction, Inc.","Conway, AR",(501) 391-2257,"1182 Lollie Rd, Conway, AR 72034",https://www.google.com/maps/place/?q=place_id:ChIJUbfp2nt8zYcRhsKKBrtzTe0&hl=en,https://www.facebook.com/pg/embermillwork/about,none,none,none,none
1113,N,Penobscot Granite,"Veazie, ME",(207) 573-4548,"1506 State St, Veazie, ME 04401",https://www.google.com/maps/place/?q=place_id:ChIJC_yAiZqzr0wRc98E3u-gK78&hl=en,https://www.facebook.com/penobscotGranite,none,none,none,none
1114,N,A1 Home Renovations,"Rochester, PA",(724) 709-1306,"127a Maple St, Rochester, PA 15074",https://www.google.com/maps/place/?q=place_id:ChIJNWCgiR1xNIgR96Cx2Ncxadw&hl=en,https://www.facebook.com/jasonrenovation,none,none,none,none
1115,N,Davis Design Cabinets & More,"Grove, OK",(918) 791-3996,"745 Circle Dr, Grove, OK 74344",https://www.google.com/maps/place/?q=place_id:ChIJ80HsMR03yIcRJu5F29rUFi0&hl=en,https://www.facebook.com/davisdesigncabinets,none,none,none,none
1116,N,Cerullo Tile,"Belmont, NH",(603) 409-6767,"7 Fruite St, Belmont, NH 03220",https://www.google.com/maps/place/?q=place_id:ChIJv0Tk3H4zs0wRUCgR-U2Rg9M&hl=en,https://www.facebook.com/profile.php?id=61555639482089,none,none,none,none
1117,N,AML Stoneworks Countertops,"Turlock, CA",(209) 622-7884,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJYdn3EywHkYARmuepXd6Ccdc&hl=en,none,https://instagram.com/amlstoneworks209,none,none,none
1118,N,4Shore Home Improvement,"Hazlet, NJ",(732) 500-5767,"59 Mobile Manor, Hazlet, NJ 07730",https://www.google.com/maps/place/?q=place_id:ChIJBc7EWNk1wokRmMZIvlL92-M&hl=en,https://www.facebook.com/profile.php?id=100057495157788,none,none,none,none
1119,N,Fort Bend Remodeling,"Rosenberg, TX",(281) 673-0303,"2003 Bishop Hollow Ln, Rosenberg, TX 77471",https://www.google.com/maps/place/?q=place_id:ChIJr1Zw_rcbQYYR6tPXHfNxJow&hl=en,https://www.facebook.com/profile.php?id=100063913850748,none,none,none,none
1120,N,Webb Cabinet Company,"Menomonie, WI",(715) 704-9188,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZcsiDeE0TQERdYS5TWdPctg&hl=en,https://www.facebook.com/webb.cabinet.company,none,none,none,none
1121,N,Integrity Tile LLC,"Titusville, FL",(321) 225-1849,"1851 Cashew Courtway, Titusville, FL 32780",https://www.google.com/maps/place/?q=place_id:ChIJc5i1jo9N54gRZHttwQjfqAE&hl=en,https://m.facebook.com/profile.php?id=100095384689175,none,none,none,none
1122,N,Hanz Remodeling LLC,"Framingham, MA",(774) 732-2404,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJi4rQLevIvwsRE2XLVB_mr24&hl=en,https://www.facebook.com/profile.php?id=61574741487444,none,none,none,none
1123,N,Martin & Sons Custom Contracting LLC,"Central Point, OR",(541) 450-4969,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-cqhxq2V-owR3mGyAC11h3Q&hl=en,https://www.facebook.com/profile.php?id=61553331241360,none,none,none,none
1124,N,Oconee Tile And Renovations,"Eatonton, GA",(706) 816-7780,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZweeYzST9ogRN__XKkn2ca8&hl=en,https://www.facebook.com/OconeeTileLLC,none,none,none,none
1125,N,Joint Purpose Remodeling Company,"New Albany, OH",(419) 937-7740,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGUl9nrTr2WYRxMtQFIqBdz4&hl=en,none,https://www.instagram.com/jointpurposeremodeling,none,none,none
1126,N,Unique Kitchens & Baths,"Chapmanville, WV",(304) 855-7896,"45 Commerce Park Rd, Chapmanville, WV 25508",https://www.google.com/maps/place/?q=place_id:ChIJQWEZncBoT4gRrNGc3Xzew_c&hl=en,https://www.facebook.com/UniqueKitchensinc,none,none,none,none
1127,N,Arnold Custom Cabinets,"Krum, TX",(214) 931-8647,"1200 E McCart St #11, Krum, TX 76249",https://www.google.com/maps/place/?q=place_id:ChIJWwRE0p23TYYRW4V_k8F0aN8&hl=en,https://www.facebook.com/ArnoldCustomCabinets,none,none,none,none
1128,N,"Lakes Granite, LLC","Portales, NM",(575) 268-9109,"601 S Avenue C, Portales, NM 88130",https://www.google.com/maps/place/?q=place_id:ChIJpetqKqnHAocR4y_iG-qMXWs&hl=en,https://www.facebook.com/profile.php?id=100068979499060,none,none,none,none
1129,N,Ortega Remodeling,"Norco, CA",(562) 618-3424,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ2zfh0IwVwSERnURdLn1iMUk&hl=en,none,https://www.instagram.com/ortegaremodeling,none,none,none
1130,N,Next Level Custom Cabinets & Woodwork LLC,"Humboldt, TN",(731) 343-4160,"2227 Eastend Dr, Humboldt, TN 38343",https://www.google.com/maps/place/?q=place_id:ChIJFVTMPFlFyC0R_pRl-PT0jC4&hl=en,https://www.facebook.com/profile.php?id=61588511438269,none,none,none,none
1131,N,Petra kitchen and bath,"Melbourne, FL",(321) 301-6644,"340 Stan Dr Unit f, Melbourne, FL 32904",https://www.google.com/maps/place/?q=place_id:ChIJQxxmNSl0zW0RUPdY9B5byAE&hl=en,none,none,none,none,none
1132,N,Ramos Kitchen Cabinets,"Florida City, FL",(786) 349-8953,"113 NW 12th St, Florida City, FL 33034",https://www.google.com/maps/place/?q=place_id:ChIJL7_heDfn2YgRFBQBSeLshv8&hl=en,none,none,none,none,none
1133,N,Sharps Cabinets and More (Small Building on the Right when Pulling in the Parking lot),"Michigan City, IN",(219) 874-3230,"8472 US-20, Michigan City, IN 46360",https://www.google.com/maps/place/?q=place_id:ChIJpRl261cIEYgRq3eS3rZWrgo&hl=en,none,none,none,none,none
1134,N,Jacuzzi Bath Remodel of Boise,"Boise, ID",(208) 656-1998,"4242 S Eagleson Rd, Boise, ID 83705",https://www.google.com/maps/place/?q=place_id:ChIJ-6IrhP9XrlQRJpbmxy0IYFs&hl=en,none,none,none,none,none
1135,N,Ray Tile LLC,"Avon Park, FL",(863) 241-3823,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ8Xqx3wkwp4gRA5ZlJd8e3UI&hl=en,none,none,none,none,none
1136,N,Crown Tubs and Tiles Refinishing,"Brentwood, CA",(424) 414-6283,"4550 Balfour Rd #436, Brentwood, CA 94513",https://www.google.com/maps/place/?q=place_id:ChIJldxLakD_j4ARATYtyrCRfwg&hl=en,none,none,none,none,none
1137,N,MEK Granite kitchen inc.,"Hialeah, FL",(786) 514-7320,"2495 W 80th St #6, Hialeah, FL 33016",https://www.google.com/maps/place/?q=place_id:ChIJKVHMoTq72YgRhsTrKZm05u8&hl=en,none,none,none,none,none
1138,N,FreshStart Kitchen & Bath,"Santa Monica, CA",(424) 337-6571,"2118 Wilshire Blvd Ste 788, Santa Monica, CA 90403",https://www.google.com/maps/place/?q=place_id:ChIJde9zrEW7woARc8CAwhAb-Fw&hl=en,none,none,none,none,none
1139,N,La Popular Tile,"Rio Grande City, TX",(833) 567-5955,"5470 E US Hwy 83, Rio Grande City, TX 78582",https://www.google.com/maps/place/?q=place_id:ChIJs4aYPUZDZIYRJpmvv1aHaqE&hl=en,none,none,none,none,none
1140,N,Modern Kitchen Remodeling,"Alhambra, CA",(626) 921-6189,"1411 S Garfield Ave #407, Alhambra, CA 91801",https://www.google.com/maps/place/?q=place_id:ChIJZWWNv0TFwoARkLk49BU7YkA&hl=en,none,none,none,none,none
1141,N,"Elmanahry , Home Improvement & Remodeling Kitchen and bathroom","San Dimas, CA",(626) 208-7547,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ8-wu-awnw4ARgBCEkatMC0o&hl=en,none,none,none,none,none
```
