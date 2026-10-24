# Round 2: Gemini task 3, part 03 of 22 (50 businesses: 50 F)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1709, reply in that chat "Continue with the businesses
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
1065,F,Daily Grind,"Spanish Fork, UT",(801) 717-6405,"230 E 300 S, Spanish Fork, UT 84660",https://www.google.com/maps/place/?q=place_id:ChIJXZgctm29TYcRznt8ey7yEJo&hl=en,http://www.facebook.com/cdailygrind,none,none,none,none
1066,F,Delta Renovations LLC,"Walnut Ridge, AR",(870) 919-4701,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJg2irt_XuciAR1jHzUseoEWg&hl=en,https://www.facebook.com/DeltaRenovationsLLC,none,none,none,none
1067,F,"Hartel Construction Group, Inc.","New Cumberland, PA",(717) 774-1212,"601 Walnut Alley #2, New Cumberland, PA 17070",https://www.google.com/maps/place/?q=place_id:ChIJKYb_MkrAyIkRjdWr71_jKz8&hl=en,https://www.facebook.com/profile.php?id=100068267392119,none,none,Martin (Marcin) Hartel,http://Hartelgrp.com
1069,F,O2 Homes Remodeling,"Miami Springs, FL",(786) 759-9564,"Miami Springs, FL 33266",https://www.google.com/maps/place/?q=place_id:ChIJfcHByaG72YgRkbVjxa5Q-mM&hl=en,https://www.facebook.com/o2homeimprovement,none,none,none,none
1070,F,Coneys Remodeling LLC,"Accord, NY",(845) 423-0045,"19 Mettacahonts Rd, Accord, NY 12404",https://www.google.com/maps/place/?q=place_id:ChIJKWg6d_Dh3IkRhSC05Pwce_0&hl=en,http://www.facebook.com/coneysremodeling,none,none,none,none
1071,F,"Custom Bathrooms By Design, LLC","Naples, FL",(239) 470-5869,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXQRmJSEl3QARp1mJNT_Luz4&hl=en,http://www.facebook.com/ericperez13244,none,none,Eric Perez,none
1072,F,Turn Key Creations,"Jefferson City, TN",(865) 296-9868,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJn-jSbThLFm4RmzPI7AmKO6Q&hl=en,https://www.facebook.com/CreationsByTurnKey,none,none,none,none
1073,F,K & K Remodeling & Home Services,"Marana, AZ",(303) 819-0285,"11514 W Kalamansi Dr, Marana, AZ 85653",https://www.google.com/maps/place/?q=place_id:ChIJ7R6xrtIP1oYRh9_eeNDpanw&hl=en,http://www.facebook.com/kkremodel,none,none,Kyle Dugan and Kristopher Croddy,none
1074,F,Hardt’s Kitchen & Bath Center,"Lewiston, ME",(207) 333-5006,"located off, 1567 Lisbon Street Suite 3, Under the Blue Awning, Commercial St side, Lewiston, ME 04240",https://www.google.com/maps/place/?q=place_id:ChIJD_RkJAhvskwRoI4A4ZEtRMA&hl=en,https://www.facebook.com/Hardtskitchens,none,none,none,none
1075,F,Fernis LeBlanc Tile Inc,"Houma, LA",(985) 851-6092,"238 S Hollywood Rd, Houma, LA 70360",https://www.google.com/maps/place/?q=place_id:ChIJARE2mKoaIYYRIsNit8vreQE&hl=en,https://www.facebook.com/fernisleblanctile,none,none,Fernis LeBlanc,none
1077,F,The JLH Co. LLC,"Fremont, OH",(419) 559-9449,"3251 Port Clinton Rd #9494, Fremont, OH 43420",https://www.google.com/maps/place/?q=place_id:ChIJaY7yIXa4O4gRqmcH9wYBoxU&hl=en,https://www.facebook.com/jlh442,none,none,Jonathan L. Horn,none
1078,F,GET THINGS DUNN,"California, KY",(513) 630-2979,"2481 Carthage Rd #9224, California, KY 41007",https://www.google.com/maps/place/?q=place_id:ChIJq6quIkmhQYgR7ztvsjyo_DY&hl=en,http://www.facebook.com/GetThingsDunn,none,none,Jeff Dunn,none
1079,F,Sergio's Remodeling and Paint,"Wylie, TX",(214) 258-8688,"275 Jena Ave, Wylie, TX 75098",https://www.google.com/maps/place/?q=place_id:ChIJCTi3_lcbTIYRx4gRqomiVoQ&hl=en,https://www.facebook.com/profile.php?id=100046967262304,none,none,Sergio Garcia,none
1082,F,Sullivan's Custom Tile and Floor,"Graham, TX",(325) 370-9302,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJA9ut0X4M1gQRcJS7TLlwuz0&hl=en,https://www.facebook.com/profile.php?id=61588252824452,none,none,Lyle Sullivan,none
1083,F,DnD tile installations LLC bathroom remodeling and flooring in san antonio,"San Antonio, TX",(210) 693-8289,"242 Moonstone Dr, San Antonio, TX 78233",https://www.google.com/maps/place/?q=place_id:ChIJzaCh7hiNXIYRYSQVUHwLT28&hl=en,none,https://www.instagram.com/dndtile,none,none,none
1084,F,Home Styles Builders LLC,"Bell, CA",(323) 484-0076,"4253 E Florence Ave, Bell, CA 90201",https://www.google.com/maps/place/?q=place_id:ChIJ3XGLjN3PwoAR10V1yW2QwNU&hl=en,none,https://www.instagram.com/homestylesbuildersllc,none,none,none
1085,F,Cabinets By Nichols,"Bargersville, IN",(317) 670-0888,"40 W Old Plank Rd, Bargersville, IN 46106",https://www.google.com/maps/place/?q=place_id:ChIJgbe1W7Zma4gRgwSXUJnFStk&hl=en,https://www.facebook.com/CabinetsByNichols,none,none,"Rob Nichols, David Blount, and Randy Bunton",none
1086,F,The Cabinet Brothers,"La Vergne, TN",(615) 712-8913,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJEbqwhiBpZIgR9pZOg79Zm4E&hl=en,https://www.facebook.com/TheCabinetBrosTN,none,none,none,none
1087,F,Hopper Construction & Remodeling,"Poplar Bluff, MO",(573) 714-3542,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJk1prqQi714cR7GVtiMouHqQ&hl=en,https://www.facebook.com/HopperConstructionRemodelingandRepair,none,none,"Chris D Hopper, Owner; Christina Hopper, Co-Owner",none
1088,F,Big Solution Kitchens and Bath LLC.,"Kissimmee, FL",(407) 844-6091,"1864 Katz Crossing Dr, Kissimmee, FL 34744",https://www.google.com/maps/place/?q=place_id:ChIJ9VS00zSF3YgRLRRXB80VwjE&hl=en,none,https://www.instagram.com/bigsolutionss_,none,none,none
1089,F,Keystone Kitchen and Bath LLC.,"Rocky River, OH",(216) 200-8686,"21019 Westway Dr Suite 6, Rocky River, OH 44116",https://www.google.com/maps/place/?q=place_id:ChIJMZoUv8PtMIgREdi1NYp-n34&hl=en,https://www.facebook.com/Keystone-Kitchen-and-Bath-LLC-100152921668258,none,none,none,none
1090,F,Dream Kitchens Plus,"Safford, AZ",(928) 428-8764,"437 S 5th Ave, Safford, AZ 85546",https://www.google.com/maps/place/?q=place_id:ChIJUZZa4y3j14YRKpdSMJSJz0c&hl=en,https://www.facebook.com/dreamkitchensplus,none,none,none,https://dreamkitchensplus.com
1091,F,Spaulding Home Solutions llc,"North Ridgeville, OH",(440) 371-4164,"7278 Case Rd, North Ridgeville, OH 44039",https://www.google.com/maps/place/?q=place_id:ChIJUfCOtcGZMIgR13EtXgdNeLE&hl=en,https://www.facebook.com/spauldinghomesolutions,none,none,none,http://clevelandhomeremodeler.com
1092,F,River Valley Renovations,"Minden, LA",(318) 505-5603,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJn-mj8prUjQQRC8vV4g5a79g&hl=en,https://www.facebook.com/rivervalleyrenovations,none,none,none,none
1093,F,Precision Bath and Carpentry,"Foley, AL",(251) 229-2074,"9775 Carnoustie Ct, Foley, AL 36535",https://www.google.com/maps/place/?q=place_id:ChIJdxtAxM4PmogRh29tYe1IRP8&hl=en,http://www.facebook.com/precisioncarpentryal,none,none,none,none
1094,F,AJ's Home Improvement Services,"Tonawanda, NY",(716) 867-5976,"249 Abbington Ave, Tonawanda, NY 14223",https://www.google.com/maps/place/?q=place_id:ChIJwbH4g4Ft04kRTfjOeXwxgFM&hl=en,http://facebook.com/ajshomeimprovementbuffalo,none,none,none,none
1095,F,Black Cat Restoration,"Tonawanda, NY",(716) 602-2620,"2250 Military Rd, Tonawanda, NY 14150",https://www.google.com/maps/place/?q=place_id:ChIJvao5COJt04kRfyUuBkMnAAI&hl=en,none,https://instagram.com/blackcatrestoration,none,none,none
1096,F,Cutting Edge Woodwork,"Skiatook, OK",(918) 578-5013,"2102 W Rogers Blvd, Skiatook, OK 74070",https://www.google.com/maps/place/?q=place_id:ChIJEfeJ5VTntocR2QiEDitepJw&hl=en,https://www.facebook.com/CuttingEdgeWoodworkLLC,none,none,none,none
1097,F,Tremain’s Top Tile,"Winona, MN",(608) 385-8312,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJa6DG029t-YcRhcA6IxHPGfE&hl=en,http://facebook.com/tremainstoptile,none,none,Richard R Tremain,none
1098,F,Cavinder Remodeling,"Hopkinsville, KY",(270) 305-9520,"1156 Sanderson Dr, Hopkinsville, KY 42240",https://www.google.com/maps/place/?q=place_id:ChIJY9PTZrA1ZYgRB8VeuCTWbbc&hl=en,http://www.facebook.com/cavinderremodeling,none,none,none,none
1099,F,Blue Collar Countertops,"Mt Vernon, OH",(567) 233-3133,"10 S Norton St, Mt Vernon, OH 43050",https://www.google.com/maps/place/?q=place_id:ChIJp6pwnh5TOIgRinoCpaG2XsA&hl=en,https://www.facebook.com/profile.php?id=100085189553543,none,none,none,none
1100,F,Very Good Carpentry,"St. Martinville, LA",(337) 380-6913,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQcoyx0uTsioRVVeuf_38D5w&hl=en,none,https://www.instagram.com/very_good_carpentry_llc,none,none,none
1195,F,ROME RESTORATIONS LLC,"Rome, GA",(706) 622-8121,"111 S Elm St SW, Rome, GA 30165",https://www.google.com/maps/place/?q=place_id:ChIJHeM_Ux6jiogRJZAT1kYNPHw&hl=en,https://www.facebook.com/romerestorationsllc,none,none,Victor,none
1199,F,Boatman Family Cabinetry,"Woodlawn, VA",(276) 733-9288,"58 Crystal Ln, Woodlawn, VA 24381",https://www.google.com/maps/place/?q=place_id:ChIJGzABe5kdUogR2Sfhc087D8c&hl=en,https://www.facebook.com/100048942117140/,none,none,David Boatman,none
1216,F,Skyward Cabinetry and Construction LLC,"Yukon, OK",(405) 245-5737,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJi20bCfgJsocR9FB7W5-qsmM&hl=en,https://www.facebook.com/Skywardcustoms,none,none,Skyler Ward,none
1387,F,Prestige Tile Remodeling,"Savannah, TX",(469) 237-4866,"1817 Mercer Way, Savannah, TX 76227",https://www.google.com/maps/place/?q=place_id:ChIJufZr4Eg5TIYRmAmmv7WpY9g&hl=en,https://www.facebook.com/61551394273659/,none,none,Marco,http://prestigetileremodeling.com
1400,F,"Shoals Kitchen and Bath, LLC","Tuscumbia, AL",(256) 577-6144,"202 W 3rd St, Tuscumbia, AL 35674",https://www.google.com/maps/place/?q=place_id:ChIJXSjfc9lFfYgRe3nbfdsajaQ&hl=en,https://www.facebook.com/shoalskitchenandbath,none,none,none,none
1415,F,Lowken Renovations LLC,"Bakersfield, CA",(661) 328-0477,"3154 Landco Dr D, Bakersfield, CA 93308",https://www.google.com/maps/place/?q=place_id:ChIJTWG2a6BD6oARRhfM2TAhapw&hl=en,https://www.facebook.com/100064912473260/,none,none,Eric R. (Founder); Vanessa Arreola (Office Manager),none
1417,F,Tommy Slade Construction and Remodeling,"Prattville, AL",(334) 819-6146,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJD89SIStG8EYRafVd1sLFRZM&hl=en,https://www.facebook.com/TommySladeConstruction,none,none,Tommy Slade,none
1491,F,Pro Elegant Installations,"Niles, MI",(574) 226-1079,"1831 Terminal Rd, Niles, MI 49120",https://www.google.com/maps/place/?q=place_id:ChIJgbh79DaufQcRhqZpimLSTKM&hl=en,https://www.facebook.com/100065213161295/,none,none,Angel Favela,none
1499,F,Tempo Kitchens,"Davie, FL",(954) 793-0112,"5071 FL-7 #706, Davie, FL 33314",https://www.google.com/maps/place/?q=place_id:ChIJU3pvppWp2YgRFeH19FYYy-k&hl=en,https://www.facebook.com/tempokitchens/,none,none,Yaniv Zahavi,http://www.tempokitchens.com
1595,F,Kinch Customs LLC,"Thomasville, GA",(229) 234-7939,"423 Commercial Dr C, Thomasville, GA 31757",https://www.google.com/maps/place/?q=place_id:ChIJt3LkAgV5NIUR1VuEwEdPiW4&hl=en,https://www.facebook.com/jake.kinch.2025,none,none,Jake Kinch,none
1598,F,"Hood's Custom Renovations, LLC","Wellsville, PA",(717) 991-3999,"14 York St, Wellsville, PA 17365",https://www.google.com/maps/place/?q=place_id:ChIJ-bnsQeHxyIkRhm8v8A6HQ_o&hl=en,https://www.facebook.com/hoodscustomrenovations,none,none,Andrew Hood,http://hoodscustomrenovations.com
1602,F,Laguna Granite & Quartz,"Liberty Hill, TX",(512) 501-9339,"1775 County Rd 279, Liberty Hill, TX 78642",https://www.google.com/maps/place/?q=place_id:ChIJ073PodgpW4YR8Bo3NWze5LA&hl=en,https://www.facebook.com/100078683774698,none,none,none,none
1624,F,Di Vinci Tile Inc,"Lockport, IL",(630) 885-4562,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6Y55SUDtYG4RbUhYMm72_9Q&hl=en,https://www.facebook.com/61570616373401,none,none,none,none
1657,F,Grenada Cabinet & Furniture Co,"Grenada, MS",(662) 417-4271,"2217 McCormick Rd, Grenada, MS 38901",https://www.google.com/maps/place/?q=place_id:ChIJ0XAnT8PLgYgRf7qs3yRyDTQ&hl=en,https://www.facebook.com/GrenadaCabinets,none,none,none,none
1658,F,David's Tile and Laminate,"Cortez, CO",(970) 560-6202,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ9ZygJsZ4wmERNsGGzTLB2L4&hl=en,https://www.facebook.com/100048681617408,none,none,David,none
1695,F,Guy Mouton Carpentry - Remodeling and Home Maintenance,"Woodstock, IL",(847) 774-5989,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQ3DM_LBpD4gRdRBL-0ESz6g&hl=en,https://www.facebook.com/100057380142440,none,none,Guy Mouton,none
1703,F,PR Fonseca,"Justin, TX",(469) 903-7944,"18001 Cindy's Ln, Justin, TX 76247",https://www.google.com/maps/place/?q=place_id:ChIJK3p7bQzFTYYRQB44p7Z4ZdI&hl=en,https://www.facebook.com/61566245334864,none,none,Jose Fonseca,none
1709,F,Utter Clutter - Cabinet Painting & Specialty Finishes,"Madison, AL",(256) 479-1589,"7670 Old Madison Pike, Madison, AL 35758",https://www.google.com/maps/place/?q=place_id:ChIJISYFJm5vYogRNpfFv9TAgRY&hl=en,https://www.facebook.com/uttercluttervintage,none,none,none,none
```
