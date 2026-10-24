# Round 2: Gemini task 2, part 01 of 17 (100 businesses, rows 1084 to 1183)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 1183: reply in that chat "Continue with
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
1084,C,Home Styles Builders LLC,"Bell, CA",(323) 484-0076,"4253 E Florence Ave, Bell, CA 90201",https://www.google.com/maps/place/?q=place_id:ChIJ3XGLjN3PwoAR10V1yW2QwNU&hl=en,none,https://www.instagram.com/homestylesbuildersllc,none,none
1085,C,Cabinets By Nichols,"Bargersville, IN",(317) 670-0888,"40 W Old Plank Rd, Bargersville, IN 46106",https://www.google.com/maps/place/?q=place_id:ChIJgbe1W7Zma4gRgwSXUJnFStk&hl=en,https://www.facebook.com/CabinetsByNichols,none,none,none
1086,C,The Cabinet Brothers,"La Vergne, TN",(615) 712-8913,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJEbqwhiBpZIgR9pZOg79Zm4E&hl=en,https://www.facebook.com/TheCabinetBrosTN,none,none,none
1087,C,Hopper Construction & Remodeling,"Poplar Bluff, MO",(573) 714-3542,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJk1prqQi714cR7GVtiMouHqQ&hl=en,https://www.facebook.com/HopperConstructionRemodelingandRepair,none,none,none
1088,C,Big Solution Kitchens and Bath LLC.,"Kissimmee, FL",(407) 844-6091,"1864 Katz Crossing Dr, Kissimmee, FL 34744",https://www.google.com/maps/place/?q=place_id:ChIJ9VS00zSF3YgRLRRXB80VwjE&hl=en,none,https://www.instagram.com/bigsolutionss_,none,none
1089,C,Keystone Kitchen and Bath LLC.,"Rocky River, OH",(216) 200-8686,"21019 Westway Dr Suite 6, Rocky River, OH 44116",https://www.google.com/maps/place/?q=place_id:ChIJMZoUv8PtMIgREdi1NYp-n34&hl=en,https://p.facebook.com/Keystone-Kitchen-and-Bath-LLC-100152921668258,none,none,none
1090,C,Dream Kitchens Plus,"Safford, AZ",(928) 428-8764,"437 S 5th Ave, Safford, AZ 85546",https://www.google.com/maps/place/?q=place_id:ChIJUZZa4y3j14YRKpdSMJSJz0c&hl=en,https://www.facebook.com/dreamkitchensplus,none,none,none
1091,C,Spaulding Home Solutions llc,"North Ridgeville, OH",(440) 371-4164,"7278 Case Rd, North Ridgeville, OH 44039",https://www.google.com/maps/place/?q=place_id:ChIJUfCOtcGZMIgR13EtXgdNeLE&hl=en,https://www.facebook.com/spauldinghomesolutions,none,none,none
1092,C,River Valley Renovations,"Minden, LA",(318) 505-5603,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJn-mj8prUjQQRC8vV4g5a79g&hl=en,https://m.facebook.com/rivervalleyrenovations,none,none,none
1093,C,Precision Bath and Carpentry,"Foley, AL",(251) 229-2074,"9775 Carnoustie Ct, Foley, AL 36535",https://www.google.com/maps/place/?q=place_id:ChIJdxtAxM4PmogRh29tYe1IRP8&hl=en,http://www.facebook.com/precisioncarpentryal,none,none,none
1094,C,AJ's Home Improvement Services,"Tonawanda, NY",(716) 867-5976,"249 Abbington Ave, Tonawanda, NY 14223",https://www.google.com/maps/place/?q=place_id:ChIJwbH4g4Ft04kRTfjOeXwxgFM&hl=en,http://facebook.com/ajshomeimprovementbuffalo,none,none,none
1095,C,Black Cat Restoration,"Tonawanda, NY",(716) 602-2620,"2250 Military Rd, Tonawanda, NY 14150",https://www.google.com/maps/place/?q=place_id:ChIJvao5COJt04kRfyUuBkMnAAI&hl=en,none,https://instagram.com/blackcatrestoration,none,none
1096,C,Cutting Edge Woodwork,"Skiatook, OK",(918) 578-5013,"2102 W Rogers Blvd, Skiatook, OK 74070",https://www.google.com/maps/place/?q=place_id:ChIJEfeJ5VTntocR2QiEDitepJw&hl=en,https://www.facebook.com/CuttingEdgeWoodworkLLC,none,none,none
1097,C,Tremain’s Top Tile,"Winona, MN",(608) 385-8312,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJa6DG029t-YcRhcA6IxHPGfE&hl=en,http://facebook.com/tremainstoptile,none,none,none
1098,C,Cavinder Remodeling,"Hopkinsville, KY",(270) 305-9520,"1156 Sanderson Dr, Hopkinsville, KY 42240",https://www.google.com/maps/place/?q=place_id:ChIJY9PTZrA1ZYgRB8VeuCTWbbc&hl=en,http://www.facebook.com/cavinderremodeling,none,none,none
1099,C,Blue Collar Countertops,"Mt Vernon, OH",(567) 233-3133,"10 S Norton St, Mt Vernon, OH 43050",https://www.google.com/maps/place/?q=place_id:ChIJp6pwnh5TOIgRinoCpaG2XsA&hl=en,https://www.facebook.com/profile.php?id=100085189553543,none,none,none
1100,C,Very Good Carpentry,"St. Martinville, LA",(337) 380-6913,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQcoyx0uTsioRVVeuf_38D5w&hl=en,none,https://www.instagram.com/very_good_carpentry_llc,none,none
1101,C,Pueblo Remodeling Company LLC,"Pueblo, CO",(719) 994-6008,"1216 Mass St, Pueblo, CO 81001",https://www.google.com/maps/place/?q=place_id:ChIJ00OwBzRd_QgRtu7ZTUtWmHM&hl=en,none,https://www.instagram.com/puebloremodelingcompanyllc,none,none
1102,C,J&S Custom Cabinets,"Joshua, TX",(817) 202-4603,"4701 County Rd 1017, Joshua, TX 76058",https://www.google.com/maps/place/?q=place_id:ChIJyb9n561BToYReUIXnFYVM1I&hl=en,https://www.facebook.com/JSCustomCabinets0015,none,none,none
1103,C,Creative Design Services Inc.,"Miami, FL",(786) 732-4046,"8760 SW 132nd St, Miami, FL 33176",https://www.google.com/maps/place/?q=place_id:ChIJ8YspV6vH2YgRq1xA-zxNGvg&hl=en,none,https://www.instagram.com/creative_design_services,none,none
1104,C,Jake Jordan Remodeling,"Kendallville, IN",(260) 341-2741,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdbtgJgUQFogRpudhy_245Nc&hl=en,https://www.facebook.com/Jake-Jordan-Remodeling-1040064359369363,none,none,none
1105,C,D’mendez tile and Tub Reglazing LLC,"Waterbury, CT",(347) 478-2222,"119 Store Ave, Waterbury, CT 06705",https://www.google.com/maps/place/?q=place_id:ChIJE9RBT2AVpwwRDU22S04f0Kc&hl=en,none,https://www.instagram.com/dmendeztileandtubreglazing,none,none
1106,C,PCH LATINO TILE & FLOORING LLC,"Auburn, AL",(334) 758-3193,"425 Webster Rd #124, Auburn, AL 36832",https://www.google.com/maps/place/?q=place_id:ChIJE8Pj1Gn1jIgRpp8Q38jgZFU&hl=en,https://www.facebook.com/profile.php?id=100092286463498,none,none,none
1107,C,SEK Construction,"Goshen, IN",(574) 226-9243,"57000 Downy Ct, Goshen, IN 46528",https://www.google.com/maps/place/?q=place_id:ChIJccRLjEHoFogR9lm_7djAVW8&hl=en,https://www.facebook.com/sekconstructionllc,none,none,none
1108,C,Chapman's Marble & Cabinets,"Morrilton, AR",(501) 354-1605,"121 W Railroad Ave, Morrilton, AR 72110",https://www.google.com/maps/place/?q=place_id:ChIJe6fFog91zYcRgkf30cEkQvI&hl=en,https://www.facebook.com/ChapmanFlooring1,none,none,none
1109,C,Hardwick Home Services,"Batesville, AR",(870) 806-4839,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJBx-SLQHI14ERpn_FZGS5as0&hl=en,http://facebook.com/Hardwickhomeservices,none,none,none
1110,C,Rusteberg Design,"Edwardsville, IL",(636) 575-3825,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJU-GOEg7ddYgRasOWCNuzGws&hl=en,https://www.facebook.com/RustebergDesign,none,none,none
1111,C,IG Remodeling Inc.,"Wauconda, IL",(773) 543-7509,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAX2WEqgs8mUReTOJW2YVPvw&hl=en,https://www.facebook.com/igremodelinginc,none,none,none
1112,C,"Quality Design Construction, Inc.","Conway, AR",(501) 391-2257,"1182 Lollie Rd, Conway, AR 72034",https://www.google.com/maps/place/?q=place_id:ChIJUbfp2nt8zYcRhsKKBrtzTe0&hl=en,https://www.facebook.com/pg/embermillwork/about,none,none,none
1113,C,Penobscot Granite,"Veazie, ME",(207) 573-4548,"1506 State St, Veazie, ME 04401",https://www.google.com/maps/place/?q=place_id:ChIJC_yAiZqzr0wRc98E3u-gK78&hl=en,https://www.facebook.com/penobscotGranite,none,none,none
1114,C,A1 Home Renovations,"Rochester, PA",(724) 709-1306,"127a Maple St, Rochester, PA 15074",https://www.google.com/maps/place/?q=place_id:ChIJNWCgiR1xNIgR96Cx2Ncxadw&hl=en,https://www.facebook.com/jasonrenovation,none,none,none
1115,C,Davis Design Cabinets & More,"Grove, OK",(918) 791-3996,"745 Circle Dr, Grove, OK 74344",https://www.google.com/maps/place/?q=place_id:ChIJ80HsMR03yIcRJu5F29rUFi0&hl=en,https://www.facebook.com/davisdesigncabinets,none,none,none
1116,C,Cerullo Tile,"Belmont, NH",(603) 409-6767,"7 Fruite St, Belmont, NH 03220",https://www.google.com/maps/place/?q=place_id:ChIJv0Tk3H4zs0wRUCgR-U2Rg9M&hl=en,https://www.facebook.com/profile.php?id=61555639482089,none,none,none
1117,C,AML Stoneworks Countertops,"Turlock, CA",(209) 622-7884,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJYdn3EywHkYARmuepXd6Ccdc&hl=en,none,https://instagram.com/amlstoneworks209,none,none
1118,C,4Shore Home Improvement,"Hazlet, NJ",(732) 500-5767,"59 Mobile Manor, Hazlet, NJ 07730",https://www.google.com/maps/place/?q=place_id:ChIJBc7EWNk1wokRmMZIvlL92-M&hl=en,https://www.facebook.com/profile.php?id=100057495157788,none,none,none
1119,C,Fort Bend Remodeling,"Rosenberg, TX",(281) 673-0303,"2003 Bishop Hollow Ln, Rosenberg, TX 77471",https://www.google.com/maps/place/?q=place_id:ChIJr1Zw_rcbQYYR6tPXHfNxJow&hl=en,https://www.facebook.com/profile.php?id=100063913850748,none,none,none
1120,C,Webb Cabinet Company,"Menomonie, WI",(715) 704-9188,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZcsiDeE0TQERdYS5TWdPctg&hl=en,https://www.facebook.com/webb.cabinet.company,none,none,none
1121,C,Integrity Tile LLC,"Titusville, FL",(321) 225-1849,"1851 Cashew Courtway, Titusville, FL 32780",https://www.google.com/maps/place/?q=place_id:ChIJc5i1jo9N54gRZHttwQjfqAE&hl=en,https://m.facebook.com/profile.php?id=100095384689175,none,none,none
1122,C,Hanz Remodeling LLC,"Framingham, MA",(774) 732-2404,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJi4rQLevIvwsRE2XLVB_mr24&hl=en,https://www.facebook.com/profile.php?id=61574741487444,none,none,none
1123,C,Martin & Sons Custom Contracting LLC,"Central Point, OR",(541) 450-4969,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-cqhxq2V-owR3mGyAC11h3Q&hl=en,https://www.facebook.com/profile.php?id=61553331241360,none,none,none
1124,C,Oconee Tile And Renovations,"Eatonton, GA",(706) 816-7780,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZweeYzST9ogRN__XKkn2ca8&hl=en,https://www.facebook.com/OconeeTileLLC,none,none,none
1125,C,Joint Purpose Remodeling Company,"New Albany, OH",(419) 937-7740,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGUl9nrTr2WYRxMtQFIqBdz4&hl=en,none,https://www.instagram.com/jointpurposeremodeling,none,none
1126,C,Unique Kitchens & Baths,"Chapmanville, WV",(304) 855-7896,"45 Commerce Park Rd, Chapmanville, WV 25508",https://www.google.com/maps/place/?q=place_id:ChIJQWEZncBoT4gRrNGc3Xzew_c&hl=en,https://www.facebook.com/UniqueKitchensinc,none,none,none
1127,C,Arnold Custom Cabinets,"Krum, TX",(214) 931-8647,"1200 E McCart St #11, Krum, TX 76249",https://www.google.com/maps/place/?q=place_id:ChIJWwRE0p23TYYRW4V_k8F0aN8&hl=en,https://www.facebook.com/ArnoldCustomCabinets,none,none,none
1128,C,"Lakes Granite, LLC","Portales, NM",(575) 268-9109,"601 S Avenue C, Portales, NM 88130",https://www.google.com/maps/place/?q=place_id:ChIJpetqKqnHAocR4y_iG-qMXWs&hl=en,https://www.facebook.com/profile.php?id=100068979499060,none,none,none
1129,C,Ortega Remodeling,"Norco, CA",(562) 618-3424,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ2zfh0IwVwSERnURdLn1iMUk&hl=en,none,https://www.instagram.com/ortegaremodeling,none,none
1130,C,Next Level Custom Cabinets & Woodwork LLC,"Humboldt, TN",(731) 343-4160,"2227 Eastend Dr, Humboldt, TN 38343",https://www.google.com/maps/place/?q=place_id:ChIJFVTMPFlFyC0R_pRl-PT0jC4&hl=en,https://www.facebook.com/profile.php?id=61588511438269,none,none,none
1131,C,Petra kitchen and bath,"Melbourne, FL",(321) 301-6644,"340 Stan Dr Unit f, Melbourne, FL 32904",https://www.google.com/maps/place/?q=place_id:ChIJQxxmNSl0zW0RUPdY9B5byAE&hl=en,none,none,none,none
1132,C,Ramos Kitchen Cabinets,"Florida City, FL",(786) 349-8953,"113 NW 12th St, Florida City, FL 33034",https://www.google.com/maps/place/?q=place_id:ChIJL7_heDfn2YgRFBQBSeLshv8&hl=en,none,none,none,none
1133,C,Sharps Cabinets and More (Small Building on the Right when Pulling in the Parking lot),"Michigan City, IN",(219) 874-3230,"8472 US-20, Michigan City, IN 46360",https://www.google.com/maps/place/?q=place_id:ChIJpRl261cIEYgRq3eS3rZWrgo&hl=en,none,none,none,none
1134,C,Jacuzzi Bath Remodel of Boise,"Boise, ID",(208) 656-1998,"4242 S Eagleson Rd, Boise, ID 83705",https://www.google.com/maps/place/?q=place_id:ChIJ-6IrhP9XrlQRJpbmxy0IYFs&hl=en,none,none,none,none
1135,C,Ray Tile LLC,"Avon Park, FL",(863) 241-3823,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ8Xqx3wkwp4gRA5ZlJd8e3UI&hl=en,none,none,none,none
1136,C,Crown Tubs and Tiles Refinishing,"Brentwood, CA",(424) 414-6283,"4550 Balfour Rd #436, Brentwood, CA 94513",https://www.google.com/maps/place/?q=place_id:ChIJldxLakD_j4ARATYtyrCRfwg&hl=en,none,none,none,none
1137,C,MEK Granite kitchen inc.,"Hialeah, FL",(786) 514-7320,"2495 W 80th St #6, Hialeah, FL 33016",https://www.google.com/maps/place/?q=place_id:ChIJKVHMoTq72YgRhsTrKZm05u8&hl=en,none,none,none,none
1138,C,FreshStart Kitchen & Bath,"Santa Monica, CA",(424) 337-6571,"2118 Wilshire Blvd Ste 788, Santa Monica, CA 90403",https://www.google.com/maps/place/?q=place_id:ChIJde9zrEW7woARc8CAwhAb-Fw&hl=en,none,none,none,none
1139,C,La Popular Tile,"Rio Grande City, TX",(833) 567-5955,"5470 E US Hwy 83, Rio Grande City, TX 78582",https://www.google.com/maps/place/?q=place_id:ChIJs4aYPUZDZIYRJpmvv1aHaqE&hl=en,none,none,none,none
1140,C,Modern Kitchen Remodeling,"Alhambra, CA",(626) 921-6189,"1411 S Garfield Ave #407, Alhambra, CA 91801",https://www.google.com/maps/place/?q=place_id:ChIJZWWNv0TFwoARkLk49BU7YkA&hl=en,none,none,none,none
1141,C,"Elmanahry , Home Improvement & Remodeling Kitchen and bathroom","San Dimas, CA",(626) 208-7547,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ8-wu-awnw4ARgBCEkatMC0o&hl=en,none,none,none,none
1142,C,Yates Group Construction,"West Palm Beach, FL",(561) 248-5155,"1645 Palm Beach Lakes Blvd Ste 1200, West Palm Beach, FL 33401",https://www.google.com/maps/place/?q=place_id:ChIJedVLUCbX2IgRrqnQk6MJViU&hl=en,none,none,none,none
1143,C,Bathroom&KitchenRemodelingToday.,"Granada Hills, CA",(818) 936-5405,"10650 Balboa Blvd, Granada Hills, CA 91344",https://www.google.com/maps/place/?q=place_id:ChIJN2DT2JybwoARJWMlgRvpEJc&hl=en,none,none,none,none
1144,C,PRO Cabinet And Stone,"Pinellas Park, FL",(727) 256-1642,"6401 49th Street N, Pinellas Park, FL 33781",https://www.google.com/maps/place/?q=place_id:ChIJux91X4TkwogRf_eKaleT4EY&hl=en,none,none,none,none
1145,C,Rivers Edge Countertops Inc,"Oklahoma City, OK",(405) 306-9906,"11701 S Portland Ave, Oklahoma City, OK 73170",https://www.google.com/maps/place/?q=place_id:ChIJXT1VMtttsocRVzFgQumUyW0&hl=en,none,none,none,none
1146,C,Walker’s Epoxy Countertops & Tables,"Canonsburg, PA",(724) 206-3688,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJUchK2jDPw00R9QyFzhhRDk4&hl=en,none,none,none,none
1147,C,Spartan Kitchen & Bath,"Smyrna, GA",(770) 333-9918,"2870 Plant Atkinson Rd, Smyrna, GA 30080",https://www.google.com/maps/place/?q=place_id:ChIJa6MumMoQ9YgRnt3YyqYQCgM&hl=en,none,none,none,none
1148,C,Modern shower innovations,"Portage, OH",(419) 391-0214,"468 E Main St, Portage, OH 43451",https://www.google.com/maps/place/?q=place_id:ChIJqTsK3B1gSWARC1EXiBPAmaY&hl=en,none,none,none,none
1149,C,ABC Bathtub & Counter Restore,"Miami, FL",(786) 574-3160,"11225 SW 1st St, Miami, FL 33174",https://www.google.com/maps/place/?q=place_id:ChIJMYRd3Ce_2YgRvCl3Vib8Pxo&hl=en,none,none,none,none
1150,C,LA Kitchen & Bath,"Mission Hills, CA",(818) 936-5177,"15515 Devonshire St, Mission Hills, CA 91345",https://www.google.com/maps/place/?q=place_id:ChIJbzaomG6RwoARPzrRhPlVogw&hl=en,none,none,none,none
1151,C,Piedmont Surfaces of the Triad,"Eden, NC",(336) 627-7790,"615 Monroe St, Eden, NC 27288",https://www.google.com/maps/place/?q=place_id:ChIJ4Z7rherqUogRNOML6V3_BMw&hl=en,none,none,none,none
1152,C,Tri-Star Refinishing,"Struthers, OH",(330) 787-6231,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJWYSknKb6M4gR45xupDt_0L4&hl=en,none,none,none,none
1153,C,"D & B Kitchens, Closets and More – Custom Cabinets","St Cloud, FL",(786) 454-0835,"1407 Belladonna Pl, St Cloud, FL 34771",https://www.google.com/maps/place/?q=place_id:ChIJL54Y4MGP3YgRbGiOutN28tk&hl=en,none,none,none,none
1154,C,Charlotte Y Home Improvement,"Meriden, CT",(203) 666-1042,"35 Willow St, Meriden, CT 06450",https://www.google.com/maps/place/?q=place_id:ChIJb3B2TaHL54kRxDFbwtHtmkY&hl=en,none,none,none,none
1155,C,Presko Remodeling and Design Center,"Kansas City, MO",(816) 215-7430,"8111 N Oak Trafficway, Kansas City, MO 64118",https://www.google.com/maps/place/?q=place_id:ChIJ9f9BwwD5wIcR5llu-qI921Y&hl=en,none,none,none,none
1156,C,Tile Setters Paradise,"Antioch, CA",(925) 778-0132,"1866 Verne Roberts Cir, Antioch, CA 94509",https://www.google.com/maps/place/?q=place_id:ChIJzaafM5VZhYARizgRJtrIo04&hl=en,none,none,none,none
1157,C,Monarch Cabinetry & Flooring,"Sterling Heights, MI",(248) 590-2944,"39064 Van Dyke Ave, Sterling Heights, MI 48313",https://www.google.com/maps/place/?q=place_id:ChIJhdWMWrK3KAMRdeCc3YqlC8M&hl=en,none,none,none,none
1158,C,My Kitchen Remodeling,"Chatsworth, CA",(818) 936-5675,"10239 CA-27, Chatsworth, CA 91311",https://www.google.com/maps/place/?q=place_id:ChIJiUpqMbidwoARJTDmFl2fQOA&hl=en,none,none,none,none
1159,C,KVO Cabinets Inc,"Ammon, ID",(208) 542-2450,"3968 E Sunnyside Rd, Ammon, ID 83406",https://www.google.com/maps/place/?q=place_id:ChIJ6SKmCwtfVFMRqZvaN-gPGSo&hl=en,none,none,none,none
1160,C,Kitchen Remodeling LA,"Reseda, CA",(818) 936-5289,"6944 Reseda Blvd, Reseda, CA 91335",https://www.google.com/maps/place/?q=place_id:ChIJ3T53J9CZwoARjnELz1q7ixU&hl=en,none,none,none,none
1161,C,Quality Cabinet Distributors,"Carrollton, GA",(770) 832-8598,"4552 Carrollton Villa Rica Hwy, Carrollton, GA 30116",https://www.google.com/maps/place/?q=place_id:ChIJ0euXo90qi4gRomBIUWe2Pd4&hl=en,none,none,none,none
1162,C,"MetaBath and Closet, Shower door & Vanity cabinet","South El Monte, CA",(626) 289-6888,"2112 Rosemead Blvd, South El Monte, CA 91733",https://www.google.com/maps/place/?q=place_id:ChIJw5bEva3RwoARv4Aaq2bZL44&hl=en,none,none,none,none
1163,C,Paul's Quality Kitchens,"Fall River, MA",(508) 324-9464,"18 Pelham St, Fall River, MA 02721",https://www.google.com/maps/place/?q=place_id:ChIJh3yccs745IkRsc-kC3nNAR8&hl=en,none,none,none,none
1164,C,Cutting Edge Tile and Flooring LLC,"Burlington, WI",(262) 374-8135,"417 Origen St, Burlington, WI 53105",https://www.google.com/maps/place/?q=place_id:ChIJsat5nddZD4gRj6Sw9Pv-YoY&hl=en,none,none,none,none
1165,C,Granite Palace Tops & Lv Cabinetry,"Saginaw, MI",(989) 341-1008,"600 S Outer Dr, Saginaw, MI 48601",https://www.google.com/maps/place/?q=place_id:ChIJQ_G5NgF3PIgRDjAZLihLURA&hl=en,none,none,none,none
1166,C,Magnolia Kitchen & Bath Remodeling Gardena,"Gardena, CA",(424) 424-2156,"1699 Artesia Blvd, Gardena, CA 90247",https://www.google.com/maps/place/?q=place_id:ChIJ4VGrT3u1woARG10IFr6LzVc&hl=en,none,none,none,none
1167,C,Max Kitchen & Bath,"Freeport, NY",(516) 868-8838,"149 Sunrise Hwy, Freeport, NY 11520",https://www.google.com/maps/place/?q=place_id:ChIJp7AE5Al8wokRm3ElC8HZZtE&hl=en,none,none,none,none
1168,C,Better Home Improvements,"Salem, VA",(540) 387-2223,"358 Apperson Dr, Salem, VA 24153",https://www.google.com/maps/place/?q=place_id:ChIJW-IxnDEKTYgRU99JbUuFDd0&hl=en,none,none,none,none
1169,C,C&M Cabinets and Granite,"Collierville, TN",(901) 854-7007,"320 S Mt Pleasant Rd, Collierville, TN 38017",https://www.google.com/maps/place/?q=place_id:ChIJER3xAdW8f4gRXI1AMEEWP4A&hl=en,none,none,none,none
1170,C,GRANADOS HOME REMODELZ LLC,"Austell, GA",(678) 732-7428,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJkarpnkZpq2YRP-tetNSgH7Q&hl=en,none,none,none,none
1171,C,Tile by Smrz,"Lombard, IL",(630) 261-5149,"30 S Westmore Ave, Lombard, IL 60148",https://www.google.com/maps/place/?q=place_id:ChIJIapJJ2FNDogR7-jWVU-MeRA&hl=en,none,none,none,none
1172,C,Mario's Granite Installation,"Melvindale, MI",(313) 982-7434,"19123 Allen Rd, Melvindale, MI 48122",https://www.google.com/maps/place/?q=place_id:ChIJLY5IF5Y1O4gRjvzjqElKtHs&hl=en,none,none,none,none
1173,C,Superior Cabinets and Granite,"Pocatello, ID",(208) 251-2474,"609 W Maple St, Pocatello, ID 83201",https://www.google.com/maps/place/?q=place_id:ChIJpwALvyZPVVMRyT8iZ7dioVc&hl=en,none,none,none,none
1174,C,The Granite Shop,"Russellville, AR",(479) 967-7625,"3010 Bernice Ave, Russellville, AR 72802",https://www.google.com/maps/place/?q=place_id:ChIJ7_c6KLGszYcRDDXNYUKCTvw&hl=en,none,none,none,none
1175,C,Orange Superior Kitchen Renovations,"Orange, CA",(657) 701-2224,"2575 N Tustin St, Orange, CA 92865",https://www.google.com/maps/place/?q=place_id:ChIJ77NYzi3X3IAR8baz1H9ziJ8&hl=en,none,none,none,none
1176,C,Boutique Kitchen Bathroom Remodeling West Hollywood,"West Hollywood, CA",(323) 457-3298,"8935 CA-2, West Hollywood, CA 90069",https://www.google.com/maps/place/?q=place_id:ChIJry246vW7woAR987IQ31IbmQ&hl=en,none,none,none,none
1177,C,Budget kitchen cabinets,"Mt Vernon, NY",(917) 600-2665,"134 Gramatan Ave, Mt Vernon, NY 10550",https://www.google.com/maps/place/?q=place_id:ChIJ7dxKqhSNwokR3OzsMYpWUy0&hl=en,none,none,none,none
1178,C,Lilia's Kitchen & Tile,"Santa Maria, CA",(805) 349-0026,"111 E Donovan Rd, Santa Maria, CA 93458",https://www.google.com/maps/place/?q=place_id:ChIJHxhoiYNr7IAR7OCMAfha79k&hl=en,none,none,none,none
1179,C,H.I.S. Contractors,"Copperas Cove, TX",(254) 547-8227,"216 S Main St, Copperas Cove, TX 76522",https://www.google.com/maps/place/?q=place_id:ChIJ5zGdnjqxWoYR485RM_9RI78&hl=en,none,none,none,none
1180,C,"Handyman Remodeling GABRIEL GENERAL CONTRACTOR LIC 1100927 HOME BUILDING DESIGN, RESTORATION bath and kitchen","Hesperia, CA",(760) 900-2370,"14456 Willow St at, Hesperia, CA 92345",https://www.google.com/maps/place/?q=place_id:ChIJz6U7RHxnw4ARnd_VkvNFsaE&hl=en,none,none,none,none
1181,C,AAA Bathtub Reglazing,"Moncks Corner, SC",(843) 814-0248,"105 Oak Crest Dr, Moncks Corner, SC 29461",https://www.google.com/maps/place/?q=place_id:ChIJY9IOJ21f_ogRIk8w6O8w7WY&hl=en,none,none,none,none
1182,C,Save Wood Kitchen Cabinet Refinishers,"Plainfield, IL",(630) 922-9714,"10059 Bode St, Plainfield, IL 60585",https://www.google.com/maps/place/?q=place_id:ChIJF2_TC872DogR-s5vbtoTKHo&hl=en,none,none,none,none
1183,C,Noble Construction - Breckenridge Kitchen and Bath Remodeler,"Breckenridge, CO",(970) 368-2429,"305 S Ridge St, Breckenridge, CO 80424",https://www.google.com/maps/place/?q=place_id:ChIJe7UyuPSdq6sR6s5Ed-KbNnA&hl=en,none,none,none,none
```
