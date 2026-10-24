# Round 2: Gemini task 2, part 05 of 17 (100 businesses, rows 1484 to 1583)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 1583: reply in that chat "Continue with
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
1484,C,Aqua-Care USA,"Grimes, IA",(877) 497-7777,"3850 SE Beisser Dr, Grimes, IA 50111",https://www.google.com/maps/place/?q=place_id:ChIJTaUp2P8m7IcRsLPRL4sz1z4&hl=en,none,none,none,none
1485,C,Jeff Cretens Custom Cabinetry,"Escanaba, MI",(906) 233-9491,"3631 US 2, US-41, Escanaba, MI 49829",https://www.google.com/maps/place/?q=place_id:ChIJtXk11aGXTU0Re3U7NXWZWKo&hl=en,none,none,none,none
1486,C,O.R.D Inc. Kitchen & Bath Cabinets,"Palm Desert, CA",(760) 565-1431,"74420 CA-111 #4, Palm Desert, CA 92260",https://www.google.com/maps/place/?q=place_id:ChIJCxItMCT82oARY8rUZdYLQ4A&hl=en,none,none,none,none
1487,C,Mantis Construction LLC,"Ivins, UT",(435) 313-0693,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJAd0-Dhf-YI0RF5xiUVHKij8&hl=en,none,none,none,none
1488,C,Ringbauer Construction & Remodeling Inc.,"Homer Glen, IL",(708) 949-8409,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJS8fglUxCDogRLivavHK5VMw&hl=en,none,none,none,none
1489,C,Great White Remodeling LLC,"Lancaster, NY",(716) 335-5222,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJSWQhkkNNZgIRMY-OfaN-F4Q&hl=en,none,none,none,none
1490,C,JHawk Remodeling LLC,"South Lyon, MI",(734) 369-0875,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ4Qvd7FBXI4gR4xrruoeAz-c&hl=en,none,none,none,none
1491,C,Pro Elegant Installations,"Niles, MI",(574) 226-1079,"1831 Terminal Rd, Niles, MI 49120",https://www.google.com/maps/place/?q=place_id:ChIJgbh79DaufQcRhqZpimLSTKM&hl=en,none,none,none,none
1492,C,Hiatt Construction Management LLC.,"Columbia, IL",(636) 692-9578,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ8RXcoX_ELGYRurPFzBItEjY&hl=en,none,none,none,none
1493,C,Eastern Cabinet Co,"Wilson, NC",(252) 237-5245,"3100 Meteor Dr, Wilson, NC 27893",https://www.google.com/maps/place/?q=place_id:ChIJIV5W94kgrIkRd3-XZ6XKQq4&hl=en,none,none,none,none
1494,C,Valley Granite and Cabinets,"Los Banos, CA",(209) 710-8156,"820 E Pacheco Blvd #4326, Los Banos, CA 93635",https://www.google.com/maps/place/?q=place_id:ChIJA4sXa-N-kYARuYq8NcEOTs0&hl=en,none,none,none,none
1495,C,Q and M Designs,"Cartersville, GA",(801) 369-3089,"1160 Mission Rd SW, Cartersville, GA 30120",https://www.google.com/maps/place/?q=place_id:ChIJvdsQqNNN9YgRZWjYTbRrr58&hl=en,none,none,none,none
1496,C,Titanium Construction Service Beverly Hills,"Beverly Hills, CA",(424) 203-5871,"231 S Beverly Dr, Beverly Hills, CA 90212",https://www.google.com/maps/place/?q=place_id:ChIJ7Qrfgvu7woARByZMMt4TPqQ&hl=en,none,none,none,none
1497,C,Connie Moon Design,"Kent, WA",(206) 465-6097,"19435 68th Ave S #103, Kent, WA 98032",https://www.google.com/maps/place/?q=place_id:ChIJRdt1bWZekFQRM0t-diWTdgA&hl=en,none,none,none,none
1498,C,Epoxy seike resin,"Palm Bay, FL",(786) 503-2531,"831 Airoso Rd SE, Palm Bay, FL 32909",https://www.google.com/maps/place/?q=place_id:ChIJKTKft5Fz3ogR1S3M5-wRw3o&hl=en,none,none,none,none
1499,C,Tempo Kitchens,"Davie, FL",(954) 793-0112,"5071 FL-7 #706, Davie, FL 33314",https://www.google.com/maps/place/?q=place_id:ChIJU3pvppWp2YgRFeH19FYYy-k&hl=en,none,none,none,none
1500,C,Countryside Remodeling,"Somerset, KY",(606) 767-3974,"121 Country Ln, Somerset, KY 42503",https://www.google.com/maps/place/?q=place_id:ChIJ8fTxYwdLXYgRfDClsj_EBXI&hl=en,none,none,none,none
1501,C,LUXETILE,"Ivins, UT",(435) 773-8361,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ94EwrRfqGK0RXFWc3pYhXIw&hl=en,none,none,none,none
1502,C,Mulrooney Tub & Shower Repair..,"Meriden, CT",(203) 630-2790,"274 Thorpe Ave, Meriden, CT 06450",https://www.google.com/maps/place/?q=place_id:ChIJbTNoV6DL54kR-DHfG4jd7yw&hl=en,none,none,none,none
1503,C,Masterlux LLC,"New Port Richey, FL",(727) 674-5620,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMSRe4lJjN4ARb2TX0SFedow&hl=en,none,none,none,none
1504,C,Essential Kitchen & Bath,"Alpharetta, GA",(678) 366-0996,"356 S Main St, Alpharetta, GA 30009",https://www.google.com/maps/place/?q=place_id:ChIJVVVVVUEQ9YgRkIwHRloGvAg&hl=en,none,none,none,none
1505,C,Rohall Contracting LLC,"Youngstown, OH",(412) 298-1315,"7622 Huntington Dr, Youngstown, OH 44512",https://www.google.com/maps/place/?q=place_id:ChIJEzCKFPhPiQQRB3Rrli0Se-o&hl=en,none,none,none,none
1506,C,Beating The Best Home Improvement,"Speedway, IN",(317) 908-9122,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJtxJ5HG3LfykRRZhYLAbvyA4&hl=en,none,none,none,none
1507,C,Colonial Kitchens Custom Cabinets,"Yorktown, VA",(757) 898-1332,"7621 George Washington Memorial Hwy #2, Yorktown, VA 23692",https://www.google.com/maps/place/?q=place_id:ChIJj-t8scZ_sIkRi7CnfUUQW7M&hl=en,none,none,none,none
1508,C,AZ tile and granite LLC DBA J&K Construction Builders LLC,"Tolleson, AZ",(623) 277-8440,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0Q_lD_E_K4cRpgfHnu0g92M&hl=en,none,none,none,none
1509,C,Trophy Tile and Bathroom Renovations,"Dahlonega, GA",(678) 923-9568,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpzFpO20lsygR0oa3U3auQB4&hl=en,none,none,none,none
1510,C,One Day Bathtub Refinishers,"National City, CA",(619) 820-5435,"1857 S Lanoitan Ave, National City, CA 91950",https://www.google.com/maps/place/?q=place_id:ChIJAQAAADxS2YARqUvf5eLEAcE&hl=en,none,none,none,none
1511,C,GMG HOME SOLUTIONS LLC,"Clayton, NC",(919) 813-9223,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQalZlphpZa8RSyPUzHbHPLo&hl=en,none,none,none,none
1512,C,C&J Custom Surfaces,"Ravenna, OH",(330) 256-5445,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ140vmXW-ig4RIAUuqnD9Jhw&hl=en,none,none,none,none
1513,C,Mayou Tile & Bath,"Clinton, MA",(978) 333-2447,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP1ZqOwzx44kRjGoEbcfHpn4&hl=en,none,none,none,none
1514,C,Home Remodeling Texas,"Leon Valley, TX",(210) 504-7096,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJu4A03gNpXIYRfGc5faZP4TU&hl=en,none,none,none,none
1515,C,Nu-Look Kitchens,"Dubuque, IA",(563) 582-4680,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ795HzbAt44cRRZ1NdIbHFvo&hl=en,none,none,none,none
1516,C,Custom Designers of Milwaukee,"Milwaukee, WI",(414) 281-0155,"5652 South 13th Street, Milwaukee, WI 53221",https://www.google.com/maps/place/?q=place_id:ChIJtdJK47UWBYgRG0JP1lhN8ts&hl=en,none,none,none,none
1517,C,The Cabinet Maker LLC,"Georgetown, SC",(843) 855-5746,"312 Lee St, Georgetown, SC 29440",https://www.google.com/maps/place/?q=place_id:ChIJT40MgYUrAIkRV0_byfJL1wY&hl=en,none,none,none,none
1518,C,Blue Jay Builders,"Westminster, CO",(720) 577-8509,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHRPJaW-YSS4RbH1WM6hdoek&hl=en,none,none,none,none
1519,C,"Jaken Remodeling, LLC","Dayton, MN",(612) 390-4436,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJh6Hyhew7s1IRj_tSYTzjPrM&hl=en,none,none,none,none
1520,C,Kitchen Cabinets Houston,"Magnolia, TX",(832) 497-8417,"32624 Wright Rd, Magnolia, TX 77355",https://www.google.com/maps/place/?q=place_id:ChIJoTBZGErNQIYRlUAcL_xiTSk&hl=en,none,none,none,none
1521,C,Stephen North Points North Remodeling & Restoration,"Plymouth, MA",(781) 975-3413,"7 Water St #7, Plymouth, MA 02360",https://www.google.com/maps/place/?q=place_id:ChIJzf27kz675IkRTko8GMNlTyQ&hl=en,none,none,none,none
1522,C,IV Remodeling,"Liberty Hill, TX",(512) 820-4758,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJBd2a2ncsW4YR0bCl_iLpg04&hl=en,none,none,none,none
1523,C,"Luis General Construction, LLC","Union City, NJ",(201) 969-6027,"539 41st Street, Union City, NJ 07087",https://www.google.com/maps/place/?q=place_id:ChIJyZ-_3IZXwokR1scXcpIurts&hl=en,none,none,none,none
1524,C,"Tom's Tile Store & More, Inc.","Sharon, MA",(781) 806-5841,"1 Merchant St L1, Sharon, MA 02067",https://www.google.com/maps/place/?q=place_id:ChIJv2MxtRZ95IkRCIoRopSzevc&hl=en,none,none,none,none
1525,C,Monterey Peninsula Tile Inc,"Salinas, CA",(831) 595-3835,"1577 Cottonwood Dr, Salinas, CA 93905",https://www.google.com/maps/place/?q=place_id:ChIJ04lVDZEHkoARA56FKGjDmf8&hl=en,none,none,none,none
1526,C,New era kitchen design,"Bloomington, CA",(909) 260-4992,"1564 W Carter St, Bloomington, CA 92316",https://www.google.com/maps/place/?q=place_id:ChIJA0eqJqlNw4ARXUWkIy_NxL8&hl=en,none,none,none,none
1527,C,HD Constructions LLC,"Manchester, NH",(603) 722-4507,"71 Billings St, Manchester, NH 03103",https://www.google.com/maps/place/?q=place_id:ChIJvRJeqNfkaUkRP_X-EPoglZ4&hl=en,none,none,none,none
1528,C,Robert Repairs LLC,"Alcoa, TN",(865) 276-7363,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTaICDqqZ4mMRTvqQB85RgrU&hl=en,none,none,none,none
1529,C,Michimani and sons,"New Haven, CT",(203) 491-9134,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXyG1gzNwim4RxrGJHXsw6QE&hl=en,none,none,none,none
1530,C,CPR REMODELING LLC,"Minneapolis, MN",(612) 860-5858,"959 118th Ln NE, Minneapolis, MN 55434",https://www.google.com/maps/place/?q=place_id:ChIJb_ZKaHgjs1IRxT44wtZEGbM&hl=en,none,none,none,none
1531,C,Skilled Home Improvement LLC,"Johnstown, CO",(720) 789-9534,"3618 SE Frontage Rd #204, Johnstown, CO 80534",https://www.google.com/maps/place/?q=place_id:ChIJw_7KbV6ij2URRCX9ZaaQwnw&hl=en,none,none,none,none
1532,C,Keller Construction,"South St. Paul, MN",(651) 775-4014,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOQI49S-jwoIRY0zdonfcRR0&hl=en,none,none,none,none
1533,C,Home Remodeler Inc,"Roseville, CA",(916) 730-6777,"333 Sawtell Rd, Roseville, CA 95678",https://www.google.com/maps/place/?q=place_id:ChIJaxShn64hm4ARFOnCo_7eiwQ&hl=en,none,none,none,none
1534,C,River Stone Works,"Lake Havasu City, AZ",(928) 453-5656,"585 N Lake Havasu Ave, Lake Havasu City, AZ 86403",https://www.google.com/maps/place/?q=place_id:ChIJEXXctu3t0YARWF2sXLzkbe8&hl=en,none,none,none,none
1535,C,New Idea Kitchen & Bath,"Columbia, MD",(410) 777-5105,"8895 McGaw Rd Suite D, Columbia, MD 21045",https://www.google.com/maps/place/?q=place_id:ChIJyQsd2DPht4kRjbfi-TCJnv0&hl=en,none,none,none,none
1536,C,Franco Renovation Company LLC,"Robstown, TX",(361) 227-6445,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ4QYoZIxKJwgRQTC2bO_F_ko&hl=en,none,none,none,none
1537,C,Kitchen Remodel And Design Fremont,"Portola Valley, CA",(510) 422-4421,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHxR_x6vBj4ARrhYraA0Y9tY&hl=en,none,none,none,none
1538,C,Lawrence Christopher's Kitchen & Bath,"Fairview Park, OH",(216) 322-1717,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZ4DCZGztMIgR1tK7YG1WG-k&hl=en,none,none,none,none
1539,C,Hunter & Son Custom Cabinets,"Lebanon, TN",(615) 351-7570,"102 Newby St, Lebanon, TN 37087",https://www.google.com/maps/place/?q=place_id:ChIJ58lKk_gfZIgRG9BDziigaEw&hl=en,none,none,none,none
1540,C,Gebben’s Remodeling LLC,"Morganton, NC",(828) 244-4095,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJab10mE7NjSQRnYzPgwEttY0&hl=en,none,none,none,none
1541,C,J AND J REMODELING & BACKHOE,"Belton, TX",(254) 563-3643,"5750 Sparta Rd, Belton, TX 76513",https://www.google.com/maps/place/?q=place_id:ChIJT9gPlmlBRYYRD7SEj9olR08&hl=en,none,none,none,none
1542,C,Lakeside Renovations LLC,"South Milwaukee, WI",(414) 578-6916,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6QAxC1jZHEgRimzlvdlxgQ4&hl=en,none,none,none,none
1543,C,"Stetzel Builders, Inc.","Eureka, CA",(707) 499-7427,"Eureka, CA 95502",https://www.google.com/maps/place/?q=place_id:ChIJgz9zkar_01QRmUECSANWtEU&hl=en,none,none,none,none
1544,C,"The Tub Wizard, Inc.","Pittsburgh, PA",(412) 343-6006,"394 Anawanda Ave, Pittsburgh, PA 15228",https://www.google.com/maps/place/?q=place_id:ChIJ3SqJvmf3NIgRLTqY4gyfBDc&hl=en,none,none,none,none
1545,C,Infinity Construction WDM,"Clive, IA",(515) 630-6994,"15920 Hickman Rd Unit 300, Clive, IA 50325",https://www.google.com/maps/place/?q=place_id:ChIJzysG8xwj7IcR-IihX0XM0cc&hl=en,none,none,none,none
1546,C,Jersey Fresh | Tub & Tile Refinishing,"Cranford, NJ",(732) 318-9793,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJn6sSytazw4kRtZfM6F2RMcI&hl=en,none,none,none,none
1547,C,Valley Kitchen and Bath Design Centers,"Chowchilla, CA",(209) 445-6580,"307 W Robertson Blvd, Chowchilla, CA 93610",https://www.google.com/maps/place/?q=place_id:ChIJUVr86kxDkYARt0oZBVvaCrg&hl=en,none,none,none,none
1548,C,"Thomas construction and remodeling, LLC","Snyder, TX",(325) 242-5613,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJSaopV9PDlEwRlyyDxNRTfXg&hl=en,none,none,none,none
1549,C,Golden Profit Cabinets,"Walnut, CA",(909) 869-8633,"875 Fairway Dr, Walnut, CA 91789",https://www.google.com/maps/place/?q=place_id:ChIJVVVVVSU1w4ARRn93yuMy_g4&hl=en,none,none,none,none
1550,C,Top of the Mark Refinishing,"Granbury, TX",(817) 219-0946,"2701 Creek Dr, Granbury, TX 76048",https://www.google.com/maps/place/?q=place_id:ChIJH3zKFy4hToYRwwfjFTvOVz4&hl=en,none,none,none,none
1551,C,Cabinet King,"Needles, CA",(928) 546-4271,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJy9XoxXyH3SIRgzDOyDxXl8U&hl=en,none,none,none,none
1552,C,Wiley's Services,"Owensboro, KY",(270) 316-6114,"1233 Castlewood Pl, Owensboro, KY 42303",https://www.google.com/maps/place/?q=place_id:ChIJf6uXf_K6b4gReZqY5rcnpHU&hl=en,none,none,none,none
1553,C,JC James Remodeling,"Point Pleasant, NJ",(732) 840-4456,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7UoUVnqEwYkRRthC_a-TnvM&hl=en,none,none,none,none
1554,C,"Magnum Remodeling, LLC","Dickinson, TX",(281) 960-0486,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdx6Jc_p9P4YR8gxVdGogG44&hl=en,none,none,none,none
1555,C,Broadway Custom Home Design,"Massapequa, NY",(516) 636-5260,"934 N Broadway, Massapequa, NY 11758",https://www.google.com/maps/place/?q=place_id:ChIJoZgvAprV6YkRb-c39iLpDAc&hl=en,none,none,none,none
1556,C,Platte Valley Refinishing LLC,"Columbus, NE",(402) 910-8221,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJKY56e2HrkIcRPR5tyPzhcLc&hl=en,none,none,none,none
1557,C,DUARTE'S CUSTOM CABINETS LLC.,"Kennedale, TX",(817) 818-0572,"847 Trent St Ste A, Kennedale, TX 76060",https://www.google.com/maps/place/?q=place_id:ChIJX4DlzBFlToYRFOU6vHrViw8&hl=en,none,none,none,none
1558,C,Bathroom Renovations Grand Prairie,"Grand Prairie, TX",(682) 337-4830,"5103 Magna Carta Blvd, Grand Prairie, TX 75052",https://www.google.com/maps/place/?q=place_id:ChIJtXtJAGKbskwRLKvWJMK3lic&hl=en,none,none,none,none
1559,C,Kropf Craft LLC,"Wickenburg, AZ",(928) 684-3014,"3500 N Sabin Brown Rd, Wickenburg, AZ 85390",https://www.google.com/maps/place/?q=place_id:ChIJo4WT_VtP04AR8k3Yu6SjIiI&hl=en,none,none,none,none
1560,C,George Wilson GWR&C Remodeling & Construction,"Sand Springs, OK",(918) 671-5733,"3206 Rawson Rd, Sand Springs, OK 74063",https://www.google.com/maps/place/?q=place_id:ChIJNyVxvVoGBSAR1QJP1F3WuG0&hl=en,none,none,none,none
1561,C,Prestige Bathroom Remodeling,"Rome, GA",(706) 374-9605,"3 Westridge Pl, Rome, GA 30165",https://www.google.com/maps/place/?q=place_id:ChIJUV2o0NmiiogRO-LZqqdyLQA&hl=en,none,none,none,none
1562,C,Ideal Kitchen & Bath,"Naples, FL",(239) 289-5000,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJwf9ULxUe24gRoHzeFde6x9s&hl=en,none,none,none,none
1563,C,"OnPar Home Improvements LLC | Kitchen & Bathroom , Residential Remodeling Service in Kingman, AZ","Kingman, AZ",(928) 716-6347,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJs11H7v_bzYARThWq-yJeVFY&hl=en,none,none,none,none
1564,C,North Star Custom Cabinets Inc,"Posen, IL",(708) 597-2099,"14825 McKinley Ave, Posen, IL 60469",https://www.google.com/maps/place/?q=place_id:ChIJq71SrjwjDogRelp2DjBTJoY&hl=en,none,none,none,none
1565,C,Kitchen and Floor Decor,"Woburn, MA",(617) 659-1449,"275 Salem St Ste 3, Woburn, MA 01801",https://www.google.com/maps/place/?q=place_id:ChIJkZmzez1144kRb700Ou22Z2M&hl=en,none,none,none,none
1566,C,Warrenton Custom Cabinets Llc,"Warrenton, VA",(540) 349-3227,"7347 Comfort Inn Dr, Warrenton, VA 20187",https://www.google.com/maps/place/?q=place_id:ChIJfcOx0uh8tokRt4nnBrNV-DQ&hl=en,none,none,none,none
1567,C,HTH Cabinets,"Odessa, TX",(432) 331-7583,"2932 N Torrance Ave, Odessa, TX 79764",https://www.google.com/maps/place/?q=place_id:ChIJCZNwIMi3-4YRBWLIBYIz0pw&hl=en,none,none,none,none
1568,C,Perfection Kitchen Bath Studio,"Boynton Beach, FL",(561) 770-4933,"3100 S Congress Ave Ste 2, Boynton Beach, FL 33426",https://www.google.com/maps/place/?q=place_id:ChIJ-0QoYB_f2IgRMtViYJNT35k&hl=en,none,none,none,none
1569,C,All Star Home Supply,"Taylor, MI",(313) 896-8747,"8914 Telegraph Rd, Taylor, MI 48180",https://www.google.com/maps/place/?q=place_id:ChIJIU1CpyxJO4gR8tRoVJl7qOE&hl=en,none,none,none,none
1570,C,Benavides Cabinet Shop,"Waxahachie, TX",(972) 935-9696,"1813 Howard Rd, Waxahachie, TX 75165",https://www.google.com/maps/place/?q=place_id:ChIJeUl15kjvToYRbe_5FQlxLjE&hl=en,none,none,none,none
1571,C,Mathews Fine Cabinetry,"Lufkin, TX",(936) 824-2469,"6094 US-69, Lufkin, TX 75901",https://www.google.com/maps/place/?q=place_id:ChIJ45rIV_U7OIYRCK4DVrCYXfY&hl=en,none,none,none,none
1572,C,Brandenberger Cabinets,"Easley, SC",(864) 650-3908,"4019 SC-86, Easley, SC 29642",https://www.google.com/maps/place/?q=place_id:ChIJ3xUxqbw4WIgR61Np7eRlcjI&hl=en,none,none,none,none
1573,C,Perma-Tex Resurfacing Inc,"Fraser, MI",(313) 640-8700,"34092 James J Pompo Dr, Fraser, MI 48026",https://www.google.com/maps/place/?q=place_id:ChIJmU5gPJLVJIgRuchnzfFexzk&hl=en,none,none,none,none
1574,C,H Garcia's Custom Cabinets LLC,"Fort Worth, TX",(817) 287-1159,"4230 Rendon Rd, Fort Worth, TX 76140",https://www.google.com/maps/place/?q=place_id:ChIJLQZ7A0llToYRDbmEFeCCTGg&hl=en,none,none,none,none
1575,C,Nixon Cabinet Co,"Athens, AL",(256) 232-5722,"17048 Blackburn Rd, Athens, AL 35611",https://www.google.com/maps/place/?q=place_id:ChIJ26eyJ12NYogRAI-hwPjgmZs&hl=en,none,none,none,none
1576,C,Granite Rocks,"East Chicago, IN",(219) 427-9855,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJfVmZuSLfEYgRJvtJeWeMO1Q&hl=en,none,none,none,none
1577,C,Construction 360 Services - kitchen & bath remodeling,"Cocoa, FL",(786) 501-0034,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ4akIC-NuRw0RAQ4BIA1Dreg&hl=en,none,none,none,none
1578,C,Zane's Handyman Services,"Ogden, UT",(385) 423-5352,"774 N Quincy Ave, Ogden, UT 84404",https://www.google.com/maps/place/?q=place_id:ChIJJ6U9V7MNU4cRKtdXWeTkX1Q&hl=en,none,none,none,none
1579,C,Enhanced Refacing/Remodeling Inc,"Freeport, IL",(833) 873-3223,"1791 S West Ave Ste A, Freeport, IL 61032",https://www.google.com/maps/place/?q=place_id:ChIJdZ6Z_gBrCIgRqQ1Q2CrDjms&hl=en,none,none,none,none
1580,C,Shoals Creek Home Improvements,"Florence, AL",(256) 702-3845,"457 Sky Park Rd, Florence, AL 35634",https://www.google.com/maps/place/?q=place_id:ChIJhz9Skjc3mq4R87fVIFSl8b8&hl=en,none,none,none,none
1581,C,Transformative Interiors LLC,"Berea, KY",(859) 539-9995,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJJeco14NkOmQRwZ3uAM5gatA&hl=en,none,none,none,none
1582,C,Ensign Tile,"Bountiful, UT",(801) 598-7432,"2924 S 175 E #5733, Bountiful, UT 84010",https://www.google.com/maps/place/?q=place_id:ChIJjR0sZcn3UocRtKNz5ivIl6g&hl=en,none,none,none,none
1583,C,Sauk Valley Granite,"Dixon, IL",(815) 677-6893,"650 Palmyra Rd, Dixon, IL 61021",https://www.google.com/maps/place/?q=place_id:ChIJD5cQ8DKsCYgRGjh9yMWFBUg&hl=en,none,none,none,none
```
