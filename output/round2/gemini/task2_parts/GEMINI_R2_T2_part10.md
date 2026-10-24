# Round 2: Gemini task 2, part 10 of 17 (100 businesses, rows 1984 to 2083)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 2083: reply in that chat "Continue with
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
1984,C,Trusty Hammers of NWI,"Lake Station, IN",(219) 240-5208,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJo1C7nYyaOI4RNtxV_aDyYTQ&hl=en,none,none,none,none
1985,C,D&S Interiors,"Roanoke, IN",(260) 410-3937,"14518 US-24, Roanoke, IN 46783",https://www.google.com/maps/place/?q=place_id:ChIJByCW4MPdFYgR-DZY0Wx3qkY&hl=en,none,none,none,none
1986,C,Nordic Design Custom Homes,"Troy, MO",(636) 462-0803,"1036 Huntington Dr, Troy, MO 63379",https://www.google.com/maps/place/?q=place_id:ChIJmRAPvq293ocRctF7JQVEJQ0&hl=en,none,none,none,none
1987,C,"Mohawk Renovations, LLC","Aurora, IL",(630) 800-8819,"2261 Feltes Ln, Aurora, IL 60502",https://www.google.com/maps/place/?q=place_id:ChIJ4eA6I677DogRGAewyOELHcA&hl=en,none,none,none,none
1988,C,Devian Designs,"Dacono, CO",(720) 352-3093,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6RFA01JzbIcRjrjhKR83otY&hl=en,none,none,none,none
1989,C,Kitchen & Bath Direct,"Oakdale, CA",(209) 847-1111,"1266 E F St, Oakdale, CA 95361",https://www.google.com/maps/place/?q=place_id:ChIJV7rnZ2L5kIAR_2IszTdBj44&hl=en,none,none,none,none
1990,C,Apodaca Kitchen & Bathroom Remodeling,"San Elizario, TX",(915) 275-8093,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJWVZd9UWzNWURwTmYhc35tgQ&hl=en,none,none,none,none
1991,C,San Clemente Bathroom Remodeling Pros,"San Clemente, CA",(949) 996-9724,"120 Calle Iglesia, San Clemente, CA 92672",https://www.google.com/maps/place/?q=place_id:ChIJOT-Mivnz3IAREkKwNav3VOE&hl=en,none,none,none,none
1992,C,SD construction,"Los Altos Hills, CA",(650) 445-9529,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJWWy3itf0l28Rk9LLlNP0XqA&hl=en,none,none,none,none
1993,C,RenovaNest Remodeling and Painting LLC,"Zion, IL",(224) 480-5743,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZVLfJdtTTi0RGEfGBS6IiHA&hl=en,none,none,none,none
1994,C,CAP Design Build,"East Greenwich, RI",(401) 241-4111,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJwwMY14FN5IkRHDJxns57P9E&hl=en,none,none,none,none
1995,C,Beussink Brothers Woodworks,"Jackson, MO",(573) 243-4642,"2129 Old Toll Rd, Jackson, MO 63755",https://www.google.com/maps/place/?q=place_id:ChIJ43C0xleLd4gRole2MEGYNXY&hl=en,none,none,none,none
1996,C,My Old House Construction,"Selma, NC",(919) 300-1977,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_1HEhfRtrIkROytXlIf0fEA&hl=en,none,none,none,none
1997,C,Made New Construction LLC,"Rathdrum, ID",(208) 964-6682,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ07PXFD5nngQR6CztSqdI4v4&hl=en,none,none,none,none
1998,C,Refresh and Remodel,"Glenview, IL",(847) 910-8477,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdZ06CgMHm0YRBZLguAeYAgk&hl=en,none,none,none,none
1999,C,Klassen Remodeling,"Elm Grove, WI",(262) 894-7311,"1385 Crescent Dr, Elm Grove, WI 53122",https://www.google.com/maps/place/?q=place_id:ChIJq6ratjYEBYgRRORffXN0jYI&hl=en,none,none,none,none
2000,C,Tarheel Tile Inc,"Gibsonville, NC",(336) 449-6774,"106 E Railroad Ave, Gibsonville, NC 27249",https://www.google.com/maps/place/?q=place_id:ChIJmwfCPhUmU4gRXlL7MuQf4m4&hl=en,none,none,none,none
2001,C,Calhoun Millworks,"Calhoun, GA",(706) 625-2288,"995 W Line St, Calhoun, GA 30701",https://www.google.com/maps/place/?q=place_id:ChIJ7bMMXjoHYIgRSguXed730rY&hl=en,none,none,none,none
2002,C,Jerez Bathroom Solutions,"Miami Gardens, FL",(786) 208-5424,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP4F4Dq61sCARJ6F2Z4IHFtA&hl=en,none,none,none,none
2003,C,Loupe Woodcraft,"Houma, LA",(985) 855-2772,"5306 LA-311, Houma, LA 70360",https://www.google.com/maps/place/?q=place_id:ChIJsWUb718FIYYRkrdC9t4yVwg&hl=en,none,none,none,none
2004,C,Gray Construction and Remodeling,"Washington, PA",(724) 705-3950,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJcYjv6f2rNYgRPlp4s6PETKY&hl=en,none,none,none,none
2005,C,Concord Kitchen Remodeling,"Concord, CA",(925) 397-7594,"140 Mason Cir, Concord, CA 94520",https://www.google.com/maps/place/?q=place_id:ChIJX8QQdwBnhYARnpqo4ycalwI&hl=en,none,none,none,none
2006,C,House Splendid,"Emmaus, PA",(610) 965-3030,"345 Chestnut St, Emmaus, PA 18049",https://www.google.com/maps/place/?q=place_id:ChIJ27_6PNs6xIkRAXIdcFrntZg&hl=en,none,none,none,none
2007,C,R L Design.,"Sterling, CO",(970) 522-0280,"232 S Front St, Sterling, CO 80751",https://www.google.com/maps/place/?q=place_id:ChIJXzdHsBLzcYcRN2rrXXRfMLM&hl=en,none,none,none,none
2008,C,Forino Kitchen Cabinets Inc,"Park Ridge, NJ",(201) 573-0990,"33 S Maple Ave, Park Ridge, NJ 07656",https://www.google.com/maps/place/?q=place_id:ChIJuzX0WvrlwokRVGcEF_t8laQ&hl=en,none,none,none,none
2009,C,Brooksberry Kitchens and Baths,"St. Louis, MO",(314) 872-7720,"751 Old Frontenac Square, St. Louis, MO 63131",https://www.google.com/maps/place/?q=place_id:ChIJ7bhI79DM2IcRnS5VY3KoSFc&hl=en,none,none,none,none
2010,C,Rock Tops Tile And stone,"Fallon, NV",(775) 423-7625,"172 Industrial Way, Fallon, NV 89406",https://www.google.com/maps/place/?q=place_id:ChIJD1GiSuSGmIAR47pcRaRYUkA&hl=en,none,none,none,none
2011,C,Nu Look Kitchens,"Lindenhurst, IL",(847) 265-3000,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJx0WVdYqED4gRZTQS-POUjLE&hl=en,none,none,none,none
2012,C,Precision Woodworks llc,"Suffolk, VA",(757) 642-1686,"1614 Pitchkettle Rd, Suffolk, VA 23434",https://www.google.com/maps/place/?q=place_id:ChIJBd_W3TMPsIkRMaMgogLQzUM&hl=en,none,none,none,none
2013,C,On Point Home Remodeling,"Decatur, IL",(217) 369-7986,"3512 Ravina Park Rd, Decatur, IL 62526",https://www.google.com/maps/place/?q=place_id:ChIJGYOZB6GxdIgRGBUOF5Jx9Nc&hl=en,none,none,none,none
2014,C,JP TileWorks,"Sheboygan, WI",(414) 430-0269,"403 Lincoln Ave, Sheboygan, WI 53081",https://www.google.com/maps/place/?q=place_id:ChIJcerfKb-nBIgR7JfPKsl3aa8&hl=en,none,none,none,none
2015,C,Mc Gowan Cabinet Co,"Forest Lake, MN",(651) 464-2209,"23804 Northlake Blvd, Forest Lake, MN 55025",https://www.google.com/maps/place/?q=place_id:ChIJueGh9tPnslIR3GHrUwW7HwQ&hl=en,none,none,none,none
2016,C,"Kitchen Beautiful, LLC","Broadview Heights, OH",(216) 299-6354,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJB4qQx9jdMIgRMvGhDNZ2bSg&hl=en,none,none,none,none
2017,C,cali cabinet renovation,"Bakersfield, CA",(408) 813-8270,"3432 Gilmore Ave, Bakersfield, CA 93308",https://www.google.com/maps/place/?q=place_id:ChIJ9Yv3lapp6oAR0g6xjzeu2Zk&hl=en,none,none,none,none
2018,C,"Turlock Cabinet Shop, Inc.","Turlock, CA",(209) 632-1311,"1475 West Ave S, Turlock, CA 95380",https://www.google.com/maps/place/?q=place_id:ChIJnwIp2tEHkYARHX4fEKhpyk4&hl=en,none,none,none,none
2019,C,l,"Glendale, CA",(323) 599-1456,"1200 S Brand Blvd Ste 416, Glendale, CA 91204",https://www.google.com/maps/place/?q=place_id:ChIJ22fIXA3BwoARvNTRvLHC8JU&hl=en,none,none,none,none
2020,C,Kitchens and Bath by Design,"LaGrange, GA",(706) 443-5139,"1379 Lafayette Pkwy, LaGrange, GA 30241",https://www.google.com/maps/place/?q=place_id:ChIJ_ZLE61xUi4gROapTYaUHXpc&hl=en,none,none,none,none
2021,C,Woodbridge Kitchen & Bath LLC,"Woodbridge, CT",(203) 393-6803,"24 Sunbrook Rd, Woodbridge, CT 06525",https://www.google.com/maps/place/?q=place_id:ChIJF1pPvMTf54kRg1X_uU6eM9A&hl=en,none,none,none,none
2022,C,Northern Nevada Cabinets,"Fernley, NV",(775) 575-6611,"45 E Front St, Fernley, NV 89408",https://www.google.com/maps/place/?q=place_id:ChIJRaSGTl7dmIARHmhruJ-24uU&hl=en,none,none,none,none
2023,C,AB Kitchen Bathroom Remodeling Monrovia,"Monrovia, CA",(626) 210-0196,"133 E Maple Ave, Monrovia, CA 91016",https://www.google.com/maps/place/?q=place_id:ChIJd3ewB0PZwoARle9Cv1NzyDI&hl=en,none,none,none,none
2024,C,Polar Kitchen Bathroom Remodeling Agoura Hills,"Agoura Hills, CA",(818) 208-0758,"30406 Passageway Pl, Agoura Hills, CA 91301",https://www.google.com/maps/place/?q=place_id:ChIJEWW8wcadwoARMKhVExKEqII&hl=en,none,none,none,none
2025,C,Ocean State Kitchen & Bath Inc,"Warwick, RI",(401) 921-4885,"63 Alhambra Rd, Warwick, RI 02886",https://www.google.com/maps/place/?q=place_id:ChIJC6hnooJO5IkRqpHujpawpKg&hl=en,none,none,none,none
2026,C,Signature Kitchens,"Memphis, TN",(901) 450-3233,"3870 New Getwell Rd, Memphis, TN 38118",https://www.google.com/maps/place/?q=place_id:ChIJEYYlyByGf4gR1R536MhDhe8&hl=en,none,none,none,none
2027,C,Majestic Marble,"Farmington, NM",(505) 326-2447,"2801 La Plata Hwy C, Farmington, NM 87401",https://www.google.com/maps/place/?q=place_id:ChIJu5ikMi-QO4cRyD7fAYn96Zc&hl=en,none,none,none,none
2028,C,Cabinet Works,"Richmond, KY",(859) 625-9070,"620 Big Hill Ave #6, Richmond, KY 40475",https://www.google.com/maps/place/?q=place_id:ChIJ7-2KuIn9QogRhuMHHFVvav0&hl=en,none,none,none,none
2029,C,Dynamic Designs Custom Countertops Inc.,"Marion, IN",(765) 573-4982,"3818 S Lincoln Blvd, Marion, IN 46953",https://www.google.com/maps/place/?q=place_id:ChIJHWYVM6b_FIgRZ-7Y_rmiu5o&hl=en,none,none,none,none
2030,C,Homeplus Kitchen and Bath Company,"Lawndale, CA",(310) 503-8446,"15317 Hawthorne Blvd, Lawndale, CA 90260",https://www.google.com/maps/place/?q=place_id:ChIJK03311S1woARTdsyf5fpQAc&hl=en,none,none,none,none
2031,C,Creative Cabinets & Floors,"Somersworth, NH",(603) 923-3687,"28 Green St, Somersworth, NH 03878",https://www.google.com/maps/place/?q=place_id:ChIJ3cBVdSKZ4okRwHaJYkkjX44&hl=en,none,none,none,none
2032,C,Top-Notch Tile & Renovations,"Clinton, IA",(563) 249-6815,"652 8th Ave S, Clinton, IA 52732",https://www.google.com/maps/place/?q=place_id:ChIJi05IRSFl4ocRl9en9V2HIQg&hl=en,none,none,none,none
2033,C,Veteran Renovation,"Glasgow, KY",(270) 579-2807,"100 Beverly Hills Dr, Glasgow, KY 42141",https://www.google.com/maps/place/?q=place_id:ChIJs6zGLeUXZogRObvSm6OW3hY&hl=en,none,none,none,none
2034,C,timberline cabinetry,"Sweet Home, OR",(541) 401-1087,"4645 US-20, Sweet Home, OR 97386",https://www.google.com/maps/place/?q=place_id:ChIJERnkqX2IwFQR8uVs1NP-N7k&hl=en,none,none,none,none
2035,C,The Granite Connection,"Lander, WY",(307) 349-9706,"8117 WY-789, Lander, WY 82520",https://www.google.com/maps/place/?q=place_id:ChIJkbiSO1cBWYcRlgOm5NKE8OI&hl=en,none,none,none,none
2036,C,Mehl's Custom Woodworking,"New Richmond, WI",(715) 246-7383,"1766 Co Rd T, New Richmond, WI 54017",https://www.google.com/maps/place/?q=place_id:ChIJ18aU5YNXrVIRDZCc3kTjHiQ&hl=en,none,none,none,none
2037,C,NAHUM's Kitchens and Bath LLC,"Beaumont, TX",(409) 791-6706,"3599 S Martin Luther King Jr Pkwy Unit 100, Beaumont, TX 77705",https://www.google.com/maps/place/?q=place_id:ChIJs7KzjpvLPoYRMqc22WqIWS8&hl=en,none,none,none,none
2038,C,Sharp kitchen Bath Renovation Arcadia,"Arcadia, CA",(626) 231-0431,"139 E Huntington Dr, Arcadia, CA 91006",https://www.google.com/maps/place/?q=place_id:ChIJ1SbVpufbwoARVcEutJYH9aQ&hl=en,none,none,none,none
2039,C,"American Remodeling, Kitchen & Bathroom Company","Suwanee, GA",(770) 568-1702,"7778 McGinnis Ferry Rd, Suwanee, GA 30024",https://www.google.com/maps/place/?q=place_id:ChIJq6rbzkyY9YgRLisS5CoRf9s&hl=en,none,none,none,none
2040,C,Pacific Tile & Granite,"Ridgecrest, CA",(760) 446-9000,"531 W Inyokern Rd, Ridgecrest, CA 93555",https://www.google.com/maps/place/?q=place_id:ChIJ-5pJBKQTwYARBYIyfB-JFmI&hl=en,none,none,none,none
2041,C,Stellar kitchen Bath Renovation El Cajon,"El Cajon, CA",(619) 353-0126,"500 Fesler St, El Cajon, CA 92020",https://www.google.com/maps/place/?q=place_id:ChIJW86seThY2YARS4EJM16K-78&hl=en,none,none,none,none
2042,C,Noah's Ark Carpentry,"Ottawa, IL",(815) 252-4663,"804 Chapel St, Ottawa, IL 61350",https://www.google.com/maps/place/?q=place_id:ChIJAXPes31UCYgRmmEbnFfX3ro&hl=en,none,none,none,none
2043,C,Cowlitz Cabinets LLC,"Kelso, WA",(760) 987-4690,"115 Corduroy Rd, Kelso, WA 98626",https://www.google.com/maps/place/?q=place_id:ChIJ46dLSyMRMiYR6hQmpwxgJ7o&hl=en,none,none,none,none
2044,C,"D&D Remodel Masters - Kitchen Makeover, Bathroom Remodeling Company","South Charleston, WV",(304) 833-9292,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJuV804w7TSIgRSRnftkfDQ-4&hl=en,none,none,none,none
2045,C,Grand Cabinet & Stone,"Lafayette, LA",(337) 804-2888,"4947 Johnston St, Lafayette, LA 70503",https://www.google.com/maps/place/?q=place_id:ChIJl6eMLZCfJIYRgf7BQ0FXenU&hl=en,none,none,none,none
2046,C,David's Custom Cabinets,"Decatur, TX",(940) 536-4520,"155 Quail Chase Ln, Decatur, TX 76234",https://www.google.com/maps/place/?q=place_id:ChIJTSBUXYSVTYYRnkcwWKtQh-s&hl=en,none,none,none,none
2047,C,All Aspects Tile and Carpentry.,"Shelburne, VT",(802) 355-7148,"4901 Dorset St, Shelburne, VT 05482",https://www.google.com/maps/place/?q=place_id:ChIJxSiZm-x-ykwRpd0nfAiwnnI&hl=en,none,none,none,none
2048,C,Splash Bathroom Remodeling Stockton,"Stockton, CA",(209) 713-5112,"2973 Sleepy Hollow Dr, Stockton, CA 95209",https://www.google.com/maps/place/?q=place_id:ChIJedL4n9gLkIARL-OWrRIhw7c&hl=en,none,none,none,none
2049,C,"D & S Building, Inc","Margate, FL",(954) 605-7920,"1435 NW 68th Terrace, Margate, FL 33063",https://www.google.com/maps/place/?q=place_id:ChIJXSlObekE2YgRM2L_KP7DfM8&hl=en,none,none,none,none
2050,C,Kitchen Works,"Freeport, NY",(800) 698-4900,"679 S Ocean Ave, Freeport, NY 11520",https://www.google.com/maps/place/?q=place_id:ChIJt8bypsB7wokRUBgPROQ_kyc&hl=en,none,none,none,none
2051,C,Bath Planet of Rockford,"Loves Park, IL",(815) 205-0049,"7111 N Alpine Rd, Loves Park, IL 61111",https://www.google.com/maps/place/?q=place_id:ChIJLYx8bBK8CIgR7fJSwGbsPFA&hl=en,none,none,none,none
2052,C,Southern Marble,"Albemarle, NC",(704) 982-4142,"2033 W Main St, Albemarle, NC 28001",https://www.google.com/maps/place/?q=place_id:ChIJw6yPkc1kVIgRJGMg_k_A1pA&hl=en,none,none,none,none
2053,C,Milwaukee Bathroom Remodeling Experts,"Milwaukee, WI",(414) 340-5628,"2739 S Greeley St, Milwaukee, WI 53207",https://www.google.com/maps/place/?q=place_id:ChIJq6ommGYXBYgRGLXJ4sEyjpA&hl=en,none,none,none,none
2054,C,Woodworkers Plus,"Rainbow City, AL",(256) 442-0733,"135 Hames St, Rainbow City, AL 35906",https://www.google.com/maps/place/?q=place_id:ChIJ0bUg3gk7iogRIK0TdZTMrMM&hl=en,none,none,none,none
2055,C,Jesup Cabinet,"Jesup, GA",(912) 427-0586,"2340 US-84, Jesup, GA 31545",https://www.google.com/maps/place/?q=place_id:ChIJu1v7A1fH-ogRiAT2q5kYr0M&hl=en,none,none,none,none
2056,C,Rocky Mountain Cabinet,"Salida, CO",(719) 539-4235,"500 W 7th St, Salida, CO 81201",https://www.google.com/maps/place/?q=place_id:ChIJQ6RnSNsXFYcRnZA6WFVShh4&hl=en,none,none,none,none
2057,C,Ideal Kitchen & Bath,"Croton-On-Hudson, NY",(914) 271-8188,"138 Grand St, Croton-On-Hudson, NY 10520",https://www.google.com/maps/place/?q=place_id:ChIJyzoASgHHwokRmOvBu6srYJk&hl=en,none,none,none,none
2058,C,Vero Beach Bathroom Remodeling Experts,"Vero Beach, FL",(772) 273-4264,"1848 Wilbur Ave, Vero Beach, FL 32960",https://www.google.com/maps/place/?q=place_id:ChIJS8Ogzx1f3ogRj1ULx4M7lnw&hl=en,none,none,none,none
2059,C,Elegant Kitchens,"American Fork, UT",(801) 550-3999,"1349 S 500 E, American Fork, UT 84003",https://www.google.com/maps/place/?q=place_id:ChIJtfBmX1SDTYcR3akf3fDGTlI&hl=en,none,none,none,none
2060,C,"Nicholas & Co Tile and Masonry Supply, LLC","Hailey, ID",(208) 788-5684,"1551 Colibri Ln C, Hailey, ID 83333",https://www.google.com/maps/place/?q=place_id:ChIJicGM0FHUq1QRY338IOMv5ro&hl=en,none,none,none,none
2061,C,Superior CustomCabinets,"Goldsboro, NC",(919) 330-8020,"170 Scott St, Goldsboro, NC 27534",https://www.google.com/maps/place/?q=place_id:ChIJkx8GiaiqrokR3ySMhAA8fjU&hl=en,none,none,none,none
2062,C,Irvine Bathroom Remodeling Pros,"Irvine, CA",(949) 628-6394,"910 Roosevelt, Irvine, CA 92620",https://www.google.com/maps/place/?q=place_id:ChIJryWexprd3IARXIbKZTFBh2Y&hl=en,none,none,none,none
2063,C,All Quality LLC,"Matthews, NC",(704) 302-6283,"Williams Rd, Matthews, NC 28105",https://www.google.com/maps/place/?q=place_id:ChIJq6hZhqkmVIgR7Smopupa_Fo&hl=en,none,none,none,none
2064,C,Redo Kitchen & Bath Remodeling Boca Raton,"Boca Raton, FL",(954) 614-7292,"3581 N Federal Hwy, Boca Raton, FL 33431",https://www.google.com/maps/place/?q=place_id:ChIJNUE8UXXh2IgR1QA5IMO6RQY&hl=en,none,none,none,none
2065,C,Royal Renovation & Design,"Stamford, CT",(914) 255-2314,"76 Progress Dr #264, Stamford, CT 06902",https://www.google.com/maps/place/?q=place_id:ChIJzf1Na6ZZwokRpjrefJt5RpI&hl=en,none,none,none,none
2066,C,Palmetto Renovation & Design LLC,"Gaffney, SC",(864) 450-9596,"301 N Limestone St, Gaffney, SC 29340",https://www.google.com/maps/place/?q=place_id:ChIJaUT4xuYFV4gRtS4jXh3cNvc&hl=en,none,none,none,none
2067,C,VIP Bathroom Remodeling & Restoration,"Lauderdale-By-The-Sea, FL",(726) 900-9564,"12 Hibiscus Ave, Lauderdale-By-The-Sea, FL 33308",https://www.google.com/maps/place/?q=place_id:ChIJT6gekdCx2YgRnxv4Aom-2gY&hl=en,none,none,none,none
2068,C,Kitchen Cabinets Of NJ LLC,"Moonachie, NJ",(973) 977-5809,"141 Moonachie Rd, Moonachie, NJ 07074",https://www.google.com/maps/place/?q=place_id:ChIJGSSAc_n5wokR2Z3-jzrwrK8&hl=en,none,none,none,none
2069,C,Musk Construction Bathroom Remodeling | Union City,"Union City, CA",(510) 470-7816,"33401 Western Ave Ste 1, Union City, CA 94587",https://www.google.com/maps/place/?q=place_id:ChIJ-cJ0sLnhNIgRpyQOaDEvDhI&hl=en,none,none,none,none
2070,C,Essence Kitchen & Bath,"Brandon, FL",(813) 330-1055,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ9_dlsU9S_AgR28PFqcg5Q1w&hl=en,none,none,none,none
2071,C,KFK Renovations,"Westport, MA",(508) 642-0435,"135A Cadmans Neck Rd, Westport, MA 02790",https://www.google.com/maps/place/?q=place_id:ChIJ_7Q31Lf45IkRFABdAg7qnFs&hl=en,none,none,none,none
2072,C,The Golden Touch,"Huntington, WV",(304) 412-9077,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ83UbVxfbXgYRFaw6p39be4g&hl=en,none,none,none,none
2073,C,InsideOut Design & Renovations LLC,"Dalton, GA",(706) 934-4516,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJc5NAEPQkHSERYQci9sC0FlU&hl=en,none,none,none,none
2074,C,Osuna Renovation Services,"Wolfforth, TX",(806) 786-5095,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJidaSTCwiPyQRPv-7u5xhV0Y&hl=en,none,none,none,none
2075,C,Charlie the Kitchen Magician,"Litchfield, CT",(203) 414-7492,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJF-Tbjm-Z54kRejnAd25AFt8&hl=en,none,none,none,none
2076,C,Alvarez Brothers Construction & Remodeling LLC,"Robbins, IL",(773) 418-4172,"3804 W 137th St, Robbins, IL 60472",https://www.google.com/maps/place/?q=place_id:ChIJ6YVIJBA9DogRKOw4vaJF4HM&hl=en,none,none,none,none
2077,C,Rommy's Kitchens & Closets by Design,"Chula Vista, CA",(619) 575-7707,"2260 Main St Ste 7, Chula Vista, CA 91911",https://www.google.com/maps/place/?q=place_id:ChIJdZ9dU8dN2YAR8x_0XKwVUBQ&hl=en,none,none,none,none
2078,C,"H&A Remodeler | Home, Deck & Kitchen Remodeling Boise","Boise, ID",(208) 213-2694,"11044 W Peconic Ct, Boise, ID 83709",https://www.google.com/maps/place/?q=place_id:ChIJcxpo3ulXrlQR59E27eCb6Kg&hl=en,none,none,none,none
2079,C,R & D Kitchen Interiors,"Warren, MI",(586) 759-3550,"31739 Mound Rd, Warren, MI 48092",https://www.google.com/maps/place/?q=place_id:ChIJhS_o4lrQJIgRoyDzy6VW7ew&hl=en,none,none,none,none
2080,C,Alan's Bathtub Refinishing,"Canton, OH",(330) 492-4125,"4600 Roosevelt Ave NE, Canton, OH 44705",https://www.google.com/maps/place/?q=place_id:ChIJ2RhNUNjRNogRt9Gfk1KtzC8&hl=en,none,none,none,none
2081,C,P&T Design Drafting And Renovations,"Grove City, PA",(724) 854-1083,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJe-5yOcwHM4gRtmw0XurkGxM&hl=en,none,none,none,none
2082,C,Custom Cabinet & Mill Work,"Redding, CA",(530) 246-7450,"1610 Tahoe Ct, Redding, CA 96003",https://www.google.com/maps/place/?q=place_id:ChIJDc4QPF2N0lQRd4VLVx4c9iY&hl=en,none,none,none,none
2083,C,Residential & Commercial Service LLC,"White Oak, PA",(724) 861-7273,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0UOg-N3nNIgR6CiVnZxHg9U&hl=en,none,none,none,none
```
