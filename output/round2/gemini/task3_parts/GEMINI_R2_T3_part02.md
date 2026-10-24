# Round 2: Gemini task 3, part 02 of 22 (50 businesses: 50 F)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1064, reply in that chat "Continue with the businesses
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
1012,F,Ball Design Co.,"Alsip, IL",(708) 476-1938,"12620 S Holiday Dr Ste B, Alsip, IL 60803",https://www.google.com/maps/place/?q=place_id:ChIJpYtlcY47DogR_x-4s3cFtjk&hl=en,https://www.facebook.com/BallDesignCo.57,none,none,none,http://balldesigncomp.wix.com/balldesign
1014,F,J&J TUB AND WALL RENOVATION,"Camden, NJ",(609) 752-4780,"3204 Mitchell St, Camden, NJ 08105",https://www.google.com/maps/place/?q=place_id:ChIJxe-2NBLsraQRhmvycnpce7Y&hl=en,https://www.facebook.com/Jj-tub-and-wall-renovation-102115422400794,none,none,none,none
1016,F,Wilson Tile,"Pleasant Grove, UT",(801) 404-1990,"773 W 550 N St, Pleasant Grove, UT 84062",https://www.google.com/maps/place/?q=place_id:ChIJm1AkfOj3UocRT4ZQU4K1eo4&hl=en,https://www.facebook.com/WilsonTileUtah,none,none,none,none
1017,F,Affordable Tile & Stone,"Banning, CA",(951) 385-5759,"707 N Allen St, Banning, CA 92220",https://www.google.com/maps/place/?q=place_id:ChIJu7luA6q-gwARzxSauoR5NLQ&hl=en,https://www.facebook.com/profile.php?id=100091551977436,none,none,none,none
1018,F,Kipstyle Quality Construction,"Spartanburg, SC",(864) 594-2753,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ36eBrooZ74ARyEHd-fGhOHA&hl=en,none,https://www.instagram.com/kipstyle.qc,none,none,none
1019,F,Southern Quality Remodeling LLC,"Albany, GA",(229) 869-3708,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJs91KA8CH8ogRtArJfhcd0NY&hl=en,https://www.facebook.com/Southern-Quality-Remodeling-100359855439089,none,none,Kaleb,none
1020,F,Platinum Tile & Stone .LLC,"Pleasant Prairie, WI",(262) 945-7568,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJg68_SusStScRjlC9wUumjAI&hl=en,https://www.facebook.com/profile.php?id=100076524662418,none,none,Myles J. Pestka,none
1021,F,Innovative Kitchen Transformations,"Tallahassee, FL",(850) 688-0986,"2785 Capital Cir NE, Tallahassee, FL 32308",https://www.google.com/maps/place/?q=place_id:ChIJAx9Umudf7IgRcQ_pwpJRMfI&hl=en,https://www.facebook.com/InnovativeKitchenTransformations,none,none,none,none
1022,F,JG Tile & More,"Albemarle, NC",(704) 985-3499,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxx4gn4Ont2ARa-vZstD6upA&hl=en,https://www.facebook.com/JGTileandmore,none,none,none,none
1023,F,Kinslee Design and Installation,"Bozeman, MT",(406) 581-5504,"13 Sunny Side Trail, Bozeman, MT 59715",https://www.google.com/maps/place/?q=place_id:ChIJH_LPgtFIWKMRLp1EcydqGZI&hl=en,http://facebook.com/kinslee123,none,none,none,none
1024,F,3 J's Renovations and Remodeling LLC,"Fond du Lac, WI",(920) 952-0444,"20 Forest Ave, Fond du Lac, WI 54935",https://www.google.com/maps/place/?q=place_id:ChIJ7wtU0riLA4gR0GC62x6LyuI&hl=en,https://www.facebook.com/fondyhomerenovations,none,none,Jeffrey A. Olschewske,none
1025,F,Midnight Sun Remodel,"Post Falls, ID",(208) 827-1986,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_V22bxcONa8RMg4waSrgmLE&hl=en,https://www.facebook.com/MidnightSunRemodel,none,none,none,none
1026,F,MurrayMade Cabinetry,"Sheboygan, WI",(920) 980-7909,"4634 Frontage Rd, Sheboygan, WI 53081",https://www.google.com/maps/place/?q=place_id:ChIJ73br90tnHkIREaQloDrdzXs&hl=en,https://www.facebook.com/profile.php?id=100076389412272,none,none,none,none
1027,F,Superior Building and Remodeling,"Cedar Hill, TX",(817) 455-0526,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-3Xy8HfzToYR7b9kECFyI5o&hl=en,https://www.facebook.com/superiorbuildingandremodeling,none,none,none,none
1028,F,Rodocker's Custom Cabinets,"Highland, CA",(909) 907-5532,"6933 Palm Ave, Highland, CA 92346",https://www.google.com/maps/place/?q=place_id:ChIJUfVZKjtVw4ARSkLHCI4MQ_Y&hl=en,https://www.facebook.com/Rodockers-Custom-Cabinets-436077873228571,none,none,MichaelRodocker,none
1029,F,LR Remodeling & Decks Llc,"Griffin, GA",(678) 603-7589,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJIdUVmpbAnaQRfNj3qEjcF4M&hl=en,none,https://www.instagram.com/lrremodeling_,none,none,none
1030,F,Spokane Craftsman Inc,"Spokane Valley, WA",(509) 939-9407,"2406 S Cherry Ct, Spokane Valley, WA 99216",https://www.google.com/maps/place/?q=place_id:ChIJ26Ga9PognlQRHMQVMFX2ftI&hl=en,none,http://instagram.com/chris3of11,none,Chris Mace Nielsen,http://spokane-craftsman-inc.business.site
1031,F,"Beyond Remodeling and Design, LLC","Middleburg Heights, OH",(419) 541-7259,"16419 Parklawn Ave, Middleburg Heights, OH 44130",https://www.google.com/maps/place/?q=place_id:ChIJ9_jVZkVXwIQR2NzlqaxJa48&hl=en,https://www.facebook.com/profile.php?id=100065159606212,none,none,none,none
1032,F,208 Marble & Granite LLC,"Middleton, ID",(208) 250-7226,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJX_6xh96xr1QRox8868MVjn8&hl=en,http://facebook.com/208marbleandgranite,none,none,Jesus Soto Rodriguez,none
1033,F,Heritage Hills Kitchen and Bath LLC,"Narvon, PA",(941) 600-3900,"5867 Thistle Dr, Narvon, PA 17555",https://www.google.com/maps/place/?q=place_id:ChIJ4Q9scVezbwwRYalsZN1CeGU&hl=en,none,https://www.instagram.com/heritage_hills_pa,none,none,none
1034,F,Top Notch Construction & Remodels,"Springfield, MO",(417) 322-3203,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJC-wgsK9XxYcRP_JgrnEORnw&hl=en,https://www.facebook.com/ghormz21,none,none,none,none
1035,F,Quality Cabinet Co,"Hernando, MS",(662) 429-1411,"1662 Hwy 51 S, Hernando, MS 38632",https://www.google.com/maps/place/?q=place_id:ChIJ231Qq2b1f4gRT9bwFs8zlxY&hl=en,http://www.facebook.com/qualitycabinetcoinc,none,none,Amanda Mason Cook,http://greatcabinets.com
1036,F,BMF Cabinet Company Kitchen & Bathroom Remodeling,"Willow Park, TX",(817) 386-0434,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDYf_SNMHToYRpDUf6DDs97s&hl=en,http://www.facebook.com/bmfcabinets,none,none,none,none
1037,F,"Shawn's Bathrooms, Tile and Flooring Edmond","Edmond, OK",(405) 349-6010,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOQqCfOIAsocRXZES_1ORYXw&hl=en,https://www.facebook.com/ShawnsBathroomsTileandFlooringEdmond,none,none,Eric Shawn Skidgel,none
1039,F,Sevas construction LLC,"Tacoma, WA",(253) 302-2871,"9330 S Steele St, Tacoma, WA 98444",https://www.google.com/maps/place/?q=place_id:ChIJzUuAvxUBkVQRCJFjFNaIDmU&hl=en,none,https://www.instagram.com/sevas__construction_llc,none,Hryhorii Sevastian,none
1040,F,"Nova Home, LLC","Newnan, GA",(386) 451-3592,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJIYkiGTHH9IgRIo-xw1DtqLQ&hl=en,https://www.facebook.com/novahomecabinetry,none,none,none,none
1041,F,"TW Construction & Renovation, LLC","North Tonawanda, NY",(716) 247-8657,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ95ctwcNt04kRgKjxHQMnEqk&hl=en,none,https://www.instagram.com/t_w_construction,none,none,none
1042,F,Modern Day Design,"Rockford, MI",(616) 822-9684,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJjxWPIh7_GIgRJ-xF9Uwalrs&hl=en,https://www.facebook.com/Modern-Day-Design-106535427728382,none,none,none,none
1043,F,Galicia’s remodeling,"Sealy, TX",(903) 471-6931,"120 Lux Rd, Sealy, TX 77474",https://www.google.com/maps/place/?q=place_id:ChIJM_O8I10aCmERNAzqBEhYPpA&hl=en,https://www.facebook.com/profile.php?id=100082987585975,none,none,none,none
1044,F,"Wades Home Improvements, LLC","Gulf Breeze, FL",(850) 361-3241,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhXOiJAS532sRpeYv1imJUaE&hl=en,https://www.facebook.com/profile.php?id=100083299700535,none,none,none,none
1045,F,"C & E Cabinets Design, LLC","Edgewater, FL",(407) 660-0100,"137 W Marion Ave Ste 7, Edgewater, FL 32132",https://www.google.com/maps/place/?q=place_id:ChIJOUPOl39l54gRSbp2Ssf-VDo&hl=en,https://www.facebook.com/CECabinetsDesign,none,none,Eduardo Sanchez and Maria Sanchez,none
1046,F,"JB's Home Solutions, LLC","Maple Grove, MN",(763) 443-6145,"14041 80th Ave N, Maple Grove, MN 55311",https://www.google.com/maps/place/?q=place_id:ChIJad8FjxhIs1IRpRfK8fDAL2U&hl=en,https://www.facebook.com/jbshomesolutions,none,none,none,none
1047,F,Hammer Family Designs,"Lake Havasu City, AZ",(928) 412-5909,"2113 W Acoma Blvd, Lake Havasu City, AZ 86403",https://www.google.com/maps/place/?q=place_id:ChIJAzAe3w7t0YARYi3_MkVlyfk&hl=en,https://www.facebook.com/Hammer-family-103958781583817,none,none,none,none
1048,F,Burrell Tile & Remodeling,"Starkville, MS",(662) 769-2230,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ09rvxcHz-WUR0gu2Mh3vuxo&hl=en,https://www.facebook.com/profile.php?id=61563381084236,none,none,none,none
1049,F,Crystal Coast Tile,"New Bern, NC",(252) 379-1936,"N Glenburnie Rd, New Bern, NC 28560",https://www.google.com/maps/place/?q=place_id:ChIJmTO-OaLTqIkRZNVAFZLxDhg&hl=en,https://www.facebook.com/profile.php?id=61583493998607,none,none,none,none
1050,F,920 Bath & Tile,"Green Bay, WI",(920) 604-5225,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJtz5p1kKuz64RA49Ytrfd8rg&hl=en,https://www.facebook.com/920BathandTile,none,none,none,none
1051,F,Premier Kitchen & Bath,"Hannibal, MO",(573) 600-9850,"6 Northport Plaza, Hannibal, MO 63401",https://www.google.com/maps/place/?q=place_id:ChIJq5Tcrxzv3YcR8f44Jbh71ow&hl=en,https://www.facebook.com/profile.php?id=100089105223362,none,none,none,none
1052,F,Molina Handyman & Construction,"Burley, ID",(208) 312-5139,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-2BWriEvq1QR_WsdQOggMx8&hl=en,https://www.facebook.com/profile.php?id=61566467840754,none,none,David Molina and Alvino Molina,none
1053,F,Red's Construction,"Boaz, AL",(256) 393-3253,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJD_2qcWQRiogRaCzaLh9ZvFc&hl=en,https://www.facebook.com/redsconstruction1,none,none,none,none
1054,F,AMD Tile,"Homewood, IL",(708) 990-4686,"18133 Center Ave, Homewood, IL 60430",https://www.google.com/maps/place/?q=place_id:ChIJ427rO6xwOSIRW3KmJMad6X4&hl=en,https://www.facebook.com/AMDTILELLC,none,none,none,none
1055,F,D.E. Tile Design & Construction,"Lompoc, CA",(805) 865-3563,"3936 Saturn Ave, Lompoc, CA 93436",https://www.google.com/maps/place/?q=place_id:ChIJv40sAqQf7IAROAZFX-iH954&hl=en,https://www.facebook.com/davidervin87,none,none,David Ervin,none
1056,F,"N.R.P. Home Remodeling, Inc.","Hot Springs, AR",(501) 547-4030,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0R_4JP7ua20Ri8g4SGpfYcw&hl=en,https://www.facebook.com/NRPHomeRemodeling,none,none,none,none
1057,F,"Shore Tile and Stone, LLC","Easton, MD",(410) 829-3313,"29652 Lexington St, Easton, MD 21601",https://www.google.com/maps/place/?q=place_id:ChIJiSnm0RlBuIkRnOv6s6J31Js&hl=en,https://m.facebook.com/Shore-Tile-and-Stone-100946181768371,none,none,none,none
1058,F,E & R Services,"Breckenridge, TX",(940) 514-5718,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGwJp9OHhU4YRYEqq8PYxG5s&hl=en,http://www.facebook.com/erservicesbrecktx,none,none,Erick Williamson,none
1059,F,McElroy Renovations LLC,"Hamilton, OH",(513) 349-8118,"104 Mill St, Hamilton, OH 45011",https://www.google.com/maps/place/?q=place_id:ChIJwad-33FBQIgRtOkSGyOtSX4&hl=en,https://www.facebook.com/people/McElroy-Renovations-LLC/100085436481586,none,none,DerrickMcElroy,none
1060,F,Celeste's Construction Service,"Longview, TX",(903) 240-8549,"5220 W Marshall Ave, Longview, TX 75604",https://www.google.com/maps/place/?q=place_id:ChIJYTsuKZo7NoYRyw0G1oQt92g&hl=en,https://www.facebook.com/Celeste.Constrution.Service,none,none,none,none
1061,F,Crow Remodeling & Design,"Monroe, NC",(704) 465-7701,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJCVV5rFg6VIgRWwhOdHud5RA&hl=en,https://www.facebook.com/CrowRemodelingDesign,none,none,Sean R. Pond,none
1062,F,Kavs Renovations and Home Improvement,"Bloomington, IL",(309) 207-0587,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJlxnQ6LHw7akRgNpewJKZ_y4&hl=en,https://www.facebook.com/KavsRenovations,none,none,Heath R Kavanaugh,none
1063,F,Ramos Development,"Clearlake, CA",(707) 972-7449,"3820 Baylis Ave, Clearlake, CA 95422",https://www.google.com/maps/place/?q=place_id:ChIJ4525BsmLg4ARLq_qAIV6FhU&hl=en,none,https://www.instagram.com/r_development707,none,none,none
1064,F,JM Kitchen & Bath Remodeling,"Marlin, TX",(254) 231-1806,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJiS_ImLwGhUkRFiPN8B8gjs4&hl=en,https://www.facebook.com/profile.php?id=61550093585675,none,none,none,none
```
