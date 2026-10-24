# Round 2: Gemini task 3, part 08 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1236, reply in that chat "Continue with the businesses
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
1142,N,Yates Group Construction,"West Palm Beach, FL",(561) 248-5155,"1645 Palm Beach Lakes Blvd Ste 1200, West Palm Beach, FL 33401",https://www.google.com/maps/place/?q=place_id:ChIJedVLUCbX2IgRrqnQk6MJViU&hl=en,none,none,none,none,none
1143,N,Bathroom&KitchenRemodelingToday.,"Granada Hills, CA",(818) 936-5405,"10650 Balboa Blvd, Granada Hills, CA 91344",https://www.google.com/maps/place/?q=place_id:ChIJN2DT2JybwoARJWMlgRvpEJc&hl=en,none,none,none,none,none
1144,N,PRO Cabinet And Stone,"Pinellas Park, FL",(727) 256-1642,"6401 49th Street N, Pinellas Park, FL 33781",https://www.google.com/maps/place/?q=place_id:ChIJux91X4TkwogRf_eKaleT4EY&hl=en,none,none,none,none,none
1145,N,Rivers Edge Countertops Inc,"Oklahoma City, OK",(405) 306-9906,"11701 S Portland Ave, Oklahoma City, OK 73170",https://www.google.com/maps/place/?q=place_id:ChIJXT1VMtttsocRVzFgQumUyW0&hl=en,none,none,none,none,none
1146,N,Walker’s Epoxy Countertops & Tables,"Canonsburg, PA",(724) 206-3688,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJUchK2jDPw00R9QyFzhhRDk4&hl=en,none,none,none,none,none
1147,N,Spartan Kitchen & Bath,"Smyrna, GA",(770) 333-9918,"2870 Plant Atkinson Rd, Smyrna, GA 30080",https://www.google.com/maps/place/?q=place_id:ChIJa6MumMoQ9YgRnt3YyqYQCgM&hl=en,none,none,none,none,none
1148,N,Modern shower innovations,"Portage, OH",(419) 391-0214,"468 E Main St, Portage, OH 43451",https://www.google.com/maps/place/?q=place_id:ChIJqTsK3B1gSWARC1EXiBPAmaY&hl=en,none,none,none,none,none
1149,N,ABC Bathtub & Counter Restore,"Miami, FL",(786) 574-3160,"11225 SW 1st St, Miami, FL 33174",https://www.google.com/maps/place/?q=place_id:ChIJMYRd3Ce_2YgRvCl3Vib8Pxo&hl=en,none,none,none,none,none
1150,N,LA Kitchen & Bath,"Mission Hills, CA",(818) 936-5177,"15515 Devonshire St, Mission Hills, CA 91345",https://www.google.com/maps/place/?q=place_id:ChIJbzaomG6RwoARPzrRhPlVogw&hl=en,none,none,none,none,none
1151,N,Piedmont Surfaces of the Triad,"Eden, NC",(336) 627-7790,"615 Monroe St, Eden, NC 27288",https://www.google.com/maps/place/?q=place_id:ChIJ4Z7rherqUogRNOML6V3_BMw&hl=en,none,none,none,none,none
1152,N,Tri-Star Refinishing,"Struthers, OH",(330) 787-6231,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJWYSknKb6M4gR45xupDt_0L4&hl=en,none,none,none,none,none
1153,N,"D & B Kitchens, Closets and More – Custom Cabinets","St Cloud, FL",(786) 454-0835,"1407 Belladonna Pl, St Cloud, FL 34771",https://www.google.com/maps/place/?q=place_id:ChIJL54Y4MGP3YgRbGiOutN28tk&hl=en,none,none,none,none,none
1154,N,Charlotte Y Home Improvement,"Meriden, CT",(203) 666-1042,"35 Willow St, Meriden, CT 06450",https://www.google.com/maps/place/?q=place_id:ChIJb3B2TaHL54kRxDFbwtHtmkY&hl=en,none,none,none,none,none
1155,N,Presko Remodeling and Design Center,"Kansas City, MO",(816) 215-7430,"8111 N Oak Trafficway, Kansas City, MO 64118",https://www.google.com/maps/place/?q=place_id:ChIJ9f9BwwD5wIcR5llu-qI921Y&hl=en,none,none,none,none,none
1156,N,Tile Setters Paradise,"Antioch, CA",(925) 778-0132,"1866 Verne Roberts Cir, Antioch, CA 94509",https://www.google.com/maps/place/?q=place_id:ChIJzaafM5VZhYARizgRJtrIo04&hl=en,none,none,none,none,none
1157,N,Monarch Cabinetry & Flooring,"Sterling Heights, MI",(248) 590-2944,"39064 Van Dyke Ave, Sterling Heights, MI 48313",https://www.google.com/maps/place/?q=place_id:ChIJhdWMWrK3KAMRdeCc3YqlC8M&hl=en,none,none,none,none,none
1158,N,My Kitchen Remodeling,"Chatsworth, CA",(818) 936-5675,"10239 CA-27, Chatsworth, CA 91311",https://www.google.com/maps/place/?q=place_id:ChIJiUpqMbidwoARJTDmFl2fQOA&hl=en,none,none,none,none,none
1159,N,KVO Cabinets Inc,"Ammon, ID",(208) 542-2450,"3968 E Sunnyside Rd, Ammon, ID 83406",https://www.google.com/maps/place/?q=place_id:ChIJ6SKmCwtfVFMRqZvaN-gPGSo&hl=en,none,none,none,none,none
1160,N,Kitchen Remodeling LA,"Reseda, CA",(818) 936-5289,"6944 Reseda Blvd, Reseda, CA 91335",https://www.google.com/maps/place/?q=place_id:ChIJ3T53J9CZwoARjnELz1q7ixU&hl=en,none,none,none,none,none
1161,N,Quality Cabinet Distributors,"Carrollton, GA",(770) 832-8598,"4552 Carrollton Villa Rica Hwy, Carrollton, GA 30116",https://www.google.com/maps/place/?q=place_id:ChIJ0euXo90qi4gRomBIUWe2Pd4&hl=en,none,none,none,none,none
1162,N,"MetaBath and Closet, Shower door & Vanity cabinet","South El Monte, CA",(626) 289-6888,"2112 Rosemead Blvd, South El Monte, CA 91733",https://www.google.com/maps/place/?q=place_id:ChIJw5bEva3RwoARv4Aaq2bZL44&hl=en,none,none,none,none,none
1163,N,Paul's Quality Kitchens,"Fall River, MA",(508) 324-9464,"18 Pelham St, Fall River, MA 02721",https://www.google.com/maps/place/?q=place_id:ChIJh3yccs745IkRsc-kC3nNAR8&hl=en,none,none,none,none,none
1164,N,Cutting Edge Tile and Flooring LLC,"Burlington, WI",(262) 374-8135,"417 Origen St, Burlington, WI 53105",https://www.google.com/maps/place/?q=place_id:ChIJsat5nddZD4gRj6Sw9Pv-YoY&hl=en,none,none,none,none,none
1165,N,Granite Palace Tops & Lv Cabinetry,"Saginaw, MI",(989) 341-1008,"600 S Outer Dr, Saginaw, MI 48601",https://www.google.com/maps/place/?q=place_id:ChIJQ_G5NgF3PIgRDjAZLihLURA&hl=en,none,none,none,none,none
1166,N,Magnolia Kitchen & Bath Remodeling Gardena,"Gardena, CA",(424) 424-2156,"1699 Artesia Blvd, Gardena, CA 90247",https://www.google.com/maps/place/?q=place_id:ChIJ4VGrT3u1woARG10IFr6LzVc&hl=en,none,none,none,none,none
1167,N,Max Kitchen & Bath,"Freeport, NY",(516) 868-8838,"149 Sunrise Hwy, Freeport, NY 11520",https://www.google.com/maps/place/?q=place_id:ChIJp7AE5Al8wokRm3ElC8HZZtE&hl=en,none,none,none,none,none
1168,N,Better Home Improvements,"Salem, VA",(540) 387-2223,"358 Apperson Dr, Salem, VA 24153",https://www.google.com/maps/place/?q=place_id:ChIJW-IxnDEKTYgRU99JbUuFDd0&hl=en,none,none,none,none,none
1169,N,C&M Cabinets and Granite,"Collierville, TN",(901) 854-7007,"320 S Mt Pleasant Rd, Collierville, TN 38017",https://www.google.com/maps/place/?q=place_id:ChIJER3xAdW8f4gRXI1AMEEWP4A&hl=en,none,none,none,none,none
1170,N,GRANADOS HOME REMODELZ LLC,"Austell, GA",(678) 732-7428,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJkarpnkZpq2YRP-tetNSgH7Q&hl=en,none,none,none,none,none
1171,N,Tile by Smrz,"Lombard, IL",(630) 261-5149,"30 S Westmore Ave, Lombard, IL 60148",https://www.google.com/maps/place/?q=place_id:ChIJIapJJ2FNDogR7-jWVU-MeRA&hl=en,none,none,none,none,none
1172,N,Mario's Granite Installation,"Melvindale, MI",(313) 982-7434,"19123 Allen Rd, Melvindale, MI 48122",https://www.google.com/maps/place/?q=place_id:ChIJLY5IF5Y1O4gRjvzjqElKtHs&hl=en,none,none,none,none,none
1173,N,Superior Cabinets and Granite,"Pocatello, ID",(208) 251-2474,"609 W Maple St, Pocatello, ID 83201",https://www.google.com/maps/place/?q=place_id:ChIJpwALvyZPVVMRyT8iZ7dioVc&hl=en,none,none,none,none,none
1174,N,The Granite Shop,"Russellville, AR",(479) 967-7625,"3010 Bernice Ave, Russellville, AR 72802",https://www.google.com/maps/place/?q=place_id:ChIJ7_c6KLGszYcRDDXNYUKCTvw&hl=en,none,none,none,none,none
1175,N,Orange Superior Kitchen Renovations,"Orange, CA",(657) 701-2224,"2575 N Tustin St, Orange, CA 92865",https://www.google.com/maps/place/?q=place_id:ChIJ77NYzi3X3IAR8baz1H9ziJ8&hl=en,none,none,none,none,none
1176,N,Boutique Kitchen Bathroom Remodeling West Hollywood,"West Hollywood, CA",(323) 457-3298,"8935 CA-2, West Hollywood, CA 90069",https://www.google.com/maps/place/?q=place_id:ChIJry246vW7woAR987IQ31IbmQ&hl=en,none,none,none,none,none
1177,N,Budget kitchen cabinets,"Mt Vernon, NY",(917) 600-2665,"134 Gramatan Ave, Mt Vernon, NY 10550",https://www.google.com/maps/place/?q=place_id:ChIJ7dxKqhSNwokR3OzsMYpWUy0&hl=en,none,none,none,none,none
1178,N,Lilia's Kitchen & Tile,"Santa Maria, CA",(805) 349-0026,"111 E Donovan Rd, Santa Maria, CA 93458",https://www.google.com/maps/place/?q=place_id:ChIJHxhoiYNr7IAR7OCMAfha79k&hl=en,none,none,none,none,none
1179,N,H.I.S. Contractors,"Copperas Cove, TX",(254) 547-8227,"216 S Main St, Copperas Cove, TX 76522",https://www.google.com/maps/place/?q=place_id:ChIJ5zGdnjqxWoYR485RM_9RI78&hl=en,none,none,none,none,none
1180,N,"Handyman Remodeling GABRIEL GENERAL CONTRACTOR LIC 1100927 HOME BUILDING DESIGN, RESTORATION bath and kitchen","Hesperia, CA",(760) 900-2370,"14456 Willow St at, Hesperia, CA 92345",https://www.google.com/maps/place/?q=place_id:ChIJz6U7RHxnw4ARnd_VkvNFsaE&hl=en,none,none,none,none,none
1181,N,AAA Bathtub Reglazing,"Moncks Corner, SC",(843) 814-0248,"105 Oak Crest Dr, Moncks Corner, SC 29461",https://www.google.com/maps/place/?q=place_id:ChIJY9IOJ21f_ogRIk8w6O8w7WY&hl=en,none,none,none,none,none
1182,N,Save Wood Kitchen Cabinet Refinishers,"Plainfield, IL",(630) 922-9714,"10059 Bode St, Plainfield, IL 60585",https://www.google.com/maps/place/?q=place_id:ChIJF2_TC872DogR-s5vbtoTKHo&hl=en,none,none,none,none,none
1183,N,Noble Construction - Breckenridge Kitchen and Bath Remodeler,"Breckenridge, CO",(970) 368-2429,"305 S Ridge St, Breckenridge, CO 80424",https://www.google.com/maps/place/?q=place_id:ChIJe7UyuPSdq6sR6s5Ed-KbNnA&hl=en,none,none,none,none,none
1229,N,A&J Kitchen Design LLC,"East Lansdowne, PA",(610) 626-7386,"806 E Baltimore Ave, East Lansdowne, PA 19050",https://www.google.com/maps/place/?q=place_id:ChIJy93X6NDBxokR2edZFOu43F4&hl=en,none,none,none,none,none
1230,N,Sablotny Cabinetry and Design,"Springfield, IL",(217) 370-1496,"3304 Cockrell Ln, Springfield, IL 62711",https://www.google.com/maps/place/?q=place_id:ChIJo7x3c1ZHdYgR5pvcRPjuXSA&hl=en,none,none,none,none,none
1231,N,Quality Renovation LLC,"Smithfield, RI",(401) 480-0110,"2 Farnum Pike, Smithfield, RI 02917",https://www.google.com/maps/place/?q=place_id:ChIJQWMQtcdG5IkRH9AJgIVNEME&hl=en,none,none,none,none,none
1232,N,WQX Kitchen and Bath,"Covington, LA",(985) 302-5083,"70 Park Pl b, Covington, LA 70433",https://www.google.com/maps/place/?q=place_id:ChIJzfq_JKVdJ4YRPxsUc-Ztv1U&hl=en,none,none,none,none,none
1233,N,PWG's One Stop Shop Home Improvement Store,"LaGrange, GA",(678) 997-8144,"1618 Hamilton Rd, LaGrange, GA 30240",https://www.google.com/maps/place/?q=place_id:ChIJLx4vXHBWi4gR0XfpFVUt73M&hl=en,none,none,none,none,none
1234,N,Bath and kitchen remodeling I All New Remodeling,"Jacksonville, FL",(904) 226-7611,"13048 Gran Bay Pkwy, Jacksonville, FL 32258",https://www.google.com/maps/place/?q=place_id:ChIJCQ-lal7N5YgRn8WL5k87b3c&hl=en,none,none,none,none,none
1235,N,Mountain City Cabinets,"Frostburg, MD",(301) 689-5070,"18513 Martin Run Rd SW, Frostburg, MD 21532",https://www.google.com/maps/place/?q=place_id:ChIJnVXVhcyQyokRjqdAff2by1M&hl=en,none,none,none,none,none
1236,N,Premier Bathroom Remodeling,"Gainesville, GA",(678) 203-8350,"8835 Forest Path Dr, Gainesville, GA 30506",https://www.google.com/maps/place/?q=place_id:ChIJKwaUlVOX9YgRgajdaEJiIB4&hl=en,none,none,none,none,none
```
