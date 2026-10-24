# Round 2: Gemini task 3, part 13 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1541, reply in that chat "Continue with the businesses
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
1472,N,Randy's Cabinets & Woodwork,"Soddy-Daisy, TN",(423) 332-3846,"233 Industrial Park Dr E, Soddy-Daisy, TN 37379",https://www.google.com/maps/place/?q=place_id:ChIJI8mQ5G2MYIgReJLVh6oyQ0Q&hl=en,none,none,none,none,none
1473,N,Wyoming Windows & Cabinets,"Lander, WY",(307) 332-2372,"3011 US-287, Lander, WY 82520",https://www.google.com/maps/place/?q=place_id:ChIJAQBQ87b_WIcRVJ3Y92pSBSA&hl=en,none,none,none,none,none
1474,N,FACT : Flooring And Cabinet Tradecenter,"Florence, SC",(843) 283-8001,"254 N Flea Market Rd, Florence, SC 29506",https://www.google.com/maps/place/?q=place_id:ChIJ3d8nv1BcVYgRZucekrGyhbI&hl=en,none,none,none,none,none
1475,N,Kitchen Cabinet & Granite,"Kennewick, WA",(509) 783-9500,"7903 W Grandridge Blvd Ste J, Kennewick, WA 99336",https://www.google.com/maps/place/?q=place_id:ChIJ3aHZ9PF5mFQRA6lVj_7Ym9c&hl=en,none,none,none,none,none
1476,N,"Housers Cabinet Shop, Inc.","Lincolnton, NC",(704) 735-5755,"3325 NC-27, Lincolnton, NC 28092",https://www.google.com/maps/place/?q=place_id:ChIJv2mMWsnRVogRGcQTwK_raGw&hl=en,none,none,none,none,none
1477,N,Tile Unlimited,"Shelbyville, TN",(931) 685-4303,"109 Noblitt St, Shelbyville, TN 37160",https://www.google.com/maps/place/?q=place_id:ChIJg50fBWDCY4gR7u6eAY44Xew&hl=en,none,none,none,none,none
1478,N,Natural Stone and Granite,"White Settlement, TX",(817) 244-1600,"and D, 230 S Grants Ln Ste C2, White Settlement, TX 76108",https://www.google.com/maps/place/?q=place_id:ChIJh6JTO0wMToYRT-OKcQOJvyI&hl=en,none,none,none,none,none
1479,N,Herrera Custom Cabinets,"McGregor, TX",(254) 709-5497,"379 Val Verde Rd, McGregor, TX 76657",https://www.google.com/maps/place/?q=place_id:ChIJXR14vBGJT4YRCGcC9ClEsWA&hl=en,none,none,none,none,none
1480,N,Rochon - New York / Master Kitchen Designer,"Greenvale, NY",(516) 626-0480,"50 Glen Cove Rd, Greenvale, NY 11548",https://www.google.com/maps/place/?q=place_id:ChIJbYOfELtiwokRwR-OayHHg-E&hl=en,none,none,none,none,none
1481,N,Venture Kitchen & Bath Showroom Roofing and Design Center,"Plymouth, MI",(734) 656-7179,"44191 Plymouth Oaks Blvd #1300, Plymouth, MI 48170",https://www.google.com/maps/place/?q=place_id:ChIJ-W4S_ietJIgRLTkBQL1hISw&hl=en,none,none,none,none,none
1482,N,Soggy Bottoms Bathtub Refinishing,"Jonesboro, AR",(870) 926-2729,"153 CR-769, Jonesboro, AR 72405",https://www.google.com/maps/place/?q=place_id:ChIJ10VJXEuA1ocRgpHnsWkklaA&hl=en,none,none,none,none,none
1483,N,"A-AFFORDABLE REMODELING - Remodeling Service, House Remodeling, Siding Repair, Bathroom Remodel","Daphne, AL",(850) 346-0357,"25895a Friendship Rd Ste e, Daphne, AL 36526",https://www.google.com/maps/place/?q=place_id:ChIJzTZYmYpDmogRLsVaFFZC9oE&hl=en,none,none,none,none,none
1504,N,Essential Kitchen & Bath,"Alpharetta, GA",(678) 366-0996,"356 S Main St, Alpharetta, GA 30009",https://www.google.com/maps/place/?q=place_id:ChIJVVVVVUEQ9YgRkIwHRloGvAg&hl=en,none,none,none,none,none
1505,N,Rohall Contracting LLC,"Youngstown, OH",(412) 298-1315,"7622 Huntington Dr, Youngstown, OH 44512",https://www.google.com/maps/place/?q=place_id:ChIJEzCKFPhPiQQRB3Rrli0Se-o&hl=en,none,none,none,none,none
1506,N,Beating The Best Home Improvement,"Speedway, IN",(317) 908-9122,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJtxJ5HG3LfykRRZhYLAbvyA4&hl=en,none,none,none,none,none
1507,N,Colonial Kitchens Custom Cabinets,"Yorktown, VA",(757) 898-1332,"7621 George Washington Memorial Hwy #2, Yorktown, VA 23692",https://www.google.com/maps/place/?q=place_id:ChIJj-t8scZ_sIkRi7CnfUUQW7M&hl=en,none,none,none,none,none
1508,N,AZ tile and granite LLC DBA J&K Construction Builders LLC,"Tolleson, AZ",(623) 277-8440,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0Q_lD_E_K4cRpgfHnu0g92M&hl=en,none,none,none,none,none
1509,N,Trophy Tile and Bathroom Renovations,"Dahlonega, GA",(678) 923-9568,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpzFpO20lsygR0oa3U3auQB4&hl=en,none,none,none,none,none
1510,N,One Day Bathtub Refinishers,"National City, CA",(619) 820-5435,"1857 S Lanoitan Ave, National City, CA 91950",https://www.google.com/maps/place/?q=place_id:ChIJAQAAADxS2YARqUvf5eLEAcE&hl=en,none,none,none,none,none
1511,N,GMG HOME SOLUTIONS LLC,"Clayton, NC",(919) 813-9223,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQalZlphpZa8RSyPUzHbHPLo&hl=en,none,none,none,none,none
1512,N,C&J Custom Surfaces,"Ravenna, OH",(330) 256-5445,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ140vmXW-ig4RIAUuqnD9Jhw&hl=en,none,none,none,none,none
1513,N,Mayou Tile & Bath,"Clinton, MA",(978) 333-2447,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP1ZqOwzx44kRjGoEbcfHpn4&hl=en,none,none,none,none,none
1514,N,Home Remodeling Texas,"Leon Valley, TX",(210) 504-7096,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJu4A03gNpXIYRfGc5faZP4TU&hl=en,none,none,none,none,none
1515,N,Nu-Look Kitchens,"Dubuque, IA",(563) 582-4680,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ795HzbAt44cRRZ1NdIbHFvo&hl=en,none,none,none,none,none
1516,N,Custom Designers of Milwaukee,"Milwaukee, WI",(414) 281-0155,"5652 South 13th Street, Milwaukee, WI 53221",https://www.google.com/maps/place/?q=place_id:ChIJtdJK47UWBYgRG0JP1lhN8ts&hl=en,none,none,none,none,none
1517,N,The Cabinet Maker LLC,"Georgetown, SC",(843) 855-5746,"312 Lee St, Georgetown, SC 29440",https://www.google.com/maps/place/?q=place_id:ChIJT40MgYUrAIkRV0_byfJL1wY&hl=en,none,none,none,none,none
1518,N,Blue Jay Builders,"Westminster, CO",(720) 577-8509,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHRPJaW-YSS4RbH1WM6hdoek&hl=en,none,none,none,none,none
1519,N,"Jaken Remodeling, LLC","Dayton, MN",(612) 390-4436,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJh6Hyhew7s1IRj_tSYTzjPrM&hl=en,none,none,none,none,none
1520,N,Kitchen Cabinets Houston,"Magnolia, TX",(832) 497-8417,"32624 Wright Rd, Magnolia, TX 77355",https://www.google.com/maps/place/?q=place_id:ChIJoTBZGErNQIYRlUAcL_xiTSk&hl=en,none,none,none,none,none
1521,N,Stephen North Points North Remodeling & Restoration,"Plymouth, MA",(781) 975-3413,"7 Water St #7, Plymouth, MA 02360",https://www.google.com/maps/place/?q=place_id:ChIJzf27kz675IkRTko8GMNlTyQ&hl=en,none,none,none,none,none
1522,N,IV Remodeling,"Liberty Hill, TX",(512) 820-4758,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJBd2a2ncsW4YR0bCl_iLpg04&hl=en,none,none,none,none,none
1523,N,"Luis General Construction, LLC","Union City, NJ",(201) 969-6027,"539 41st Street, Union City, NJ 07087",https://www.google.com/maps/place/?q=place_id:ChIJyZ-_3IZXwokR1scXcpIurts&hl=en,none,none,none,none,none
1524,N,"Tom's Tile Store & More, Inc.","Sharon, MA",(781) 806-5841,"1 Merchant St L1, Sharon, MA 02067",https://www.google.com/maps/place/?q=place_id:ChIJv2MxtRZ95IkRCIoRopSzevc&hl=en,none,none,none,none,none
1525,N,Monterey Peninsula Tile Inc,"Salinas, CA",(831) 595-3835,"1577 Cottonwood Dr, Salinas, CA 93905",https://www.google.com/maps/place/?q=place_id:ChIJ04lVDZEHkoARA56FKGjDmf8&hl=en,none,none,none,none,none
1526,N,New era kitchen design,"Bloomington, CA",(909) 260-4992,"1564 W Carter St, Bloomington, CA 92316",https://www.google.com/maps/place/?q=place_id:ChIJA0eqJqlNw4ARXUWkIy_NxL8&hl=en,none,none,none,none,none
1527,N,HD Constructions LLC,"Manchester, NH",(603) 722-4507,"71 Billings St, Manchester, NH 03103",https://www.google.com/maps/place/?q=place_id:ChIJvRJeqNfkaUkRP_X-EPoglZ4&hl=en,none,none,none,none,none
1528,N,Robert Repairs LLC,"Alcoa, TN",(865) 276-7363,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTaICDqqZ4mMRTvqQB85RgrU&hl=en,none,none,none,none,none
1529,N,Michimani and sons,"New Haven, CT",(203) 491-9134,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXyG1gzNwim4RxrGJHXsw6QE&hl=en,none,none,none,none,none
1530,N,CPR REMODELING LLC,"Minneapolis, MN",(612) 860-5858,"959 118th Ln NE, Minneapolis, MN 55434",https://www.google.com/maps/place/?q=place_id:ChIJb_ZKaHgjs1IRxT44wtZEGbM&hl=en,none,none,none,none,none
1531,N,Skilled Home Improvement LLC,"Johnstown, CO",(720) 789-9534,"3618 SE Frontage Rd #204, Johnstown, CO 80534",https://www.google.com/maps/place/?q=place_id:ChIJw_7KbV6ij2URRCX9ZaaQwnw&hl=en,none,none,none,none,none
1532,N,Keller Construction,"South St. Paul, MN",(651) 775-4014,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOQI49S-jwoIRY0zdonfcRR0&hl=en,none,none,none,none,none
1533,N,Home Remodeler Inc,"Roseville, CA",(916) 730-6777,"333 Sawtell Rd, Roseville, CA 95678",https://www.google.com/maps/place/?q=place_id:ChIJaxShn64hm4ARFOnCo_7eiwQ&hl=en,none,none,none,none,none
1534,N,River Stone Works,"Lake Havasu City, AZ",(928) 453-5656,"585 N Lake Havasu Ave, Lake Havasu City, AZ 86403",https://www.google.com/maps/place/?q=place_id:ChIJEXXctu3t0YARWF2sXLzkbe8&hl=en,none,none,none,none,none
1535,N,New Idea Kitchen & Bath,"Columbia, MD",(410) 777-5105,"8895 McGaw Rd Suite D, Columbia, MD 21045",https://www.google.com/maps/place/?q=place_id:ChIJyQsd2DPht4kRjbfi-TCJnv0&hl=en,none,none,none,none,none
1536,N,Franco Renovation Company LLC,"Robstown, TX",(361) 227-6445,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ4QYoZIxKJwgRQTC2bO_F_ko&hl=en,none,none,none,none,none
1537,N,Kitchen Remodel And Design Fremont,"Portola Valley, CA",(510) 422-4421,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHxR_x6vBj4ARrhYraA0Y9tY&hl=en,none,none,none,none,none
1538,N,Lawrence Christopher's Kitchen & Bath,"Fairview Park, OH",(216) 322-1717,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZ4DCZGztMIgR1tK7YG1WG-k&hl=en,none,none,none,none,none
1539,N,Hunter & Son Custom Cabinets,"Lebanon, TN",(615) 351-7570,"102 Newby St, Lebanon, TN 37087",https://www.google.com/maps/place/?q=place_id:ChIJ58lKk_gfZIgRG9BDziigaEw&hl=en,none,none,none,none,none
1540,N,Gebben’s Remodeling LLC,"Morganton, NC",(828) 244-4095,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJab10mE7NjSQRnYzPgwEttY0&hl=en,none,none,none,none,none
1541,N,J AND J REMODELING & BACKHOE,"Belton, TX",(254) 563-3643,"5750 Sparta Rd, Belton, TX 76513",https://www.google.com/maps/place/?q=place_id:ChIJT9gPlmlBRYYRD7SEj9olR08&hl=en,none,none,none,none,none
```
