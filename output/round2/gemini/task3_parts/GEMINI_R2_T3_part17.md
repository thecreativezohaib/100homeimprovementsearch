# Round 2: Gemini task 3, part 17 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 2082, reply in that chat "Continue with the businesses
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
2033,N,Veteran Renovation,"Glasgow, KY",(270) 579-2807,"100 Beverly Hills Dr, Glasgow, KY 42141",https://www.google.com/maps/place/?q=place_id:ChIJs6zGLeUXZogRObvSm6OW3hY&hl=en,none,none,none,none,none
2034,N,timberline cabinetry,"Sweet Home, OR",(541) 401-1087,"4645 US-20, Sweet Home, OR 97386",https://www.google.com/maps/place/?q=place_id:ChIJERnkqX2IwFQR8uVs1NP-N7k&hl=en,none,none,none,none,none
2035,N,The Granite Connection,"Lander, WY",(307) 349-9706,"8117 WY-789, Lander, WY 82520",https://www.google.com/maps/place/?q=place_id:ChIJkbiSO1cBWYcRlgOm5NKE8OI&hl=en,none,none,none,none,none
2036,N,Mehl's Custom Woodworking,"New Richmond, WI",(715) 246-7383,"1766 Co Rd T, New Richmond, WI 54017",https://www.google.com/maps/place/?q=place_id:ChIJ18aU5YNXrVIRDZCc3kTjHiQ&hl=en,none,none,none,none,none
2037,N,NAHUM's Kitchens and Bath LLC,"Beaumont, TX",(409) 791-6706,"3599 S Martin Luther King Jr Pkwy Unit 100, Beaumont, TX 77705",https://www.google.com/maps/place/?q=place_id:ChIJs7KzjpvLPoYRMqc22WqIWS8&hl=en,none,none,none,none,none
2038,N,Sharp kitchen Bath Renovation Arcadia,"Arcadia, CA",(626) 231-0431,"139 E Huntington Dr, Arcadia, CA 91006",https://www.google.com/maps/place/?q=place_id:ChIJ1SbVpufbwoARVcEutJYH9aQ&hl=en,none,none,none,none,none
2039,N,"American Remodeling, Kitchen & Bathroom Company","Suwanee, GA",(770) 568-1702,"7778 McGinnis Ferry Rd, Suwanee, GA 30024",https://www.google.com/maps/place/?q=place_id:ChIJq6rbzkyY9YgRLisS5CoRf9s&hl=en,none,none,none,none,none
2040,N,Pacific Tile & Granite,"Ridgecrest, CA",(760) 446-9000,"531 W Inyokern Rd, Ridgecrest, CA 93555",https://www.google.com/maps/place/?q=place_id:ChIJ-5pJBKQTwYARBYIyfB-JFmI&hl=en,none,none,none,none,none
2041,N,Stellar kitchen Bath Renovation El Cajon,"El Cajon, CA",(619) 353-0126,"500 Fesler St, El Cajon, CA 92020",https://www.google.com/maps/place/?q=place_id:ChIJW86seThY2YARS4EJM16K-78&hl=en,none,none,none,none,none
2042,N,Noah's Ark Carpentry,"Ottawa, IL",(815) 252-4663,"804 Chapel St, Ottawa, IL 61350",https://www.google.com/maps/place/?q=place_id:ChIJAXPes31UCYgRmmEbnFfX3ro&hl=en,none,none,none,none,none
2043,N,Cowlitz Cabinets LLC,"Kelso, WA",(760) 987-4690,"115 Corduroy Rd, Kelso, WA 98626",https://www.google.com/maps/place/?q=place_id:ChIJ46dLSyMRMiYR6hQmpwxgJ7o&hl=en,none,none,none,none,none
2044,N,"D&D Remodel Masters - Kitchen Makeover, Bathroom Remodeling Company","South Charleston, WV",(304) 833-9292,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJuV804w7TSIgRSRnftkfDQ-4&hl=en,none,none,none,none,none
2045,N,Grand Cabinet & Stone,"Lafayette, LA",(337) 804-2888,"4947 Johnston St, Lafayette, LA 70503",https://www.google.com/maps/place/?q=place_id:ChIJl6eMLZCfJIYRgf7BQ0FXenU&hl=en,none,none,none,none,none
2046,N,David's Custom Cabinets,"Decatur, TX",(940) 536-4520,"155 Quail Chase Ln, Decatur, TX 76234",https://www.google.com/maps/place/?q=place_id:ChIJTSBUXYSVTYYRnkcwWKtQh-s&hl=en,none,none,none,none,none
2047,N,All Aspects Tile and Carpentry.,"Shelburne, VT",(802) 355-7148,"4901 Dorset St, Shelburne, VT 05482",https://www.google.com/maps/place/?q=place_id:ChIJxSiZm-x-ykwRpd0nfAiwnnI&hl=en,none,none,none,none,none
2048,N,Splash Bathroom Remodeling Stockton,"Stockton, CA",(209) 713-5112,"2973 Sleepy Hollow Dr, Stockton, CA 95209",https://www.google.com/maps/place/?q=place_id:ChIJedL4n9gLkIARL-OWrRIhw7c&hl=en,none,none,none,none,none
2049,N,"D & S Building, Inc","Margate, FL",(954) 605-7920,"1435 NW 68th Terrace, Margate, FL 33063",https://www.google.com/maps/place/?q=place_id:ChIJXSlObekE2YgRM2L_KP7DfM8&hl=en,none,none,none,none,none
2050,N,Kitchen Works,"Freeport, NY",(800) 698-4900,"679 S Ocean Ave, Freeport, NY 11520",https://www.google.com/maps/place/?q=place_id:ChIJt8bypsB7wokRUBgPROQ_kyc&hl=en,none,none,none,none,none
2051,N,Bath Planet of Rockford,"Loves Park, IL",(815) 205-0049,"7111 N Alpine Rd, Loves Park, IL 61111",https://www.google.com/maps/place/?q=place_id:ChIJLYx8bBK8CIgR7fJSwGbsPFA&hl=en,none,none,none,none,none
2052,N,Southern Marble,"Albemarle, NC",(704) 982-4142,"2033 W Main St, Albemarle, NC 28001",https://www.google.com/maps/place/?q=place_id:ChIJw6yPkc1kVIgRJGMg_k_A1pA&hl=en,none,none,none,none,none
2053,N,Milwaukee Bathroom Remodeling Experts,"Milwaukee, WI",(414) 340-5628,"2739 S Greeley St, Milwaukee, WI 53207",https://www.google.com/maps/place/?q=place_id:ChIJq6ommGYXBYgRGLXJ4sEyjpA&hl=en,none,none,none,none,none
2054,N,Woodworkers Plus,"Rainbow City, AL",(256) 442-0733,"135 Hames St, Rainbow City, AL 35906",https://www.google.com/maps/place/?q=place_id:ChIJ0bUg3gk7iogRIK0TdZTMrMM&hl=en,none,none,none,none,none
2055,N,Jesup Cabinet,"Jesup, GA",(912) 427-0586,"2340 US-84, Jesup, GA 31545",https://www.google.com/maps/place/?q=place_id:ChIJu1v7A1fH-ogRiAT2q5kYr0M&hl=en,none,none,none,none,none
2056,N,Rocky Mountain Cabinet,"Salida, CO",(719) 539-4235,"500 W 7th St, Salida, CO 81201",https://www.google.com/maps/place/?q=place_id:ChIJQ6RnSNsXFYcRnZA6WFVShh4&hl=en,none,none,none,none,none
2057,N,Ideal Kitchen & Bath,"Croton-On-Hudson, NY",(914) 271-8188,"138 Grand St, Croton-On-Hudson, NY 10520",https://www.google.com/maps/place/?q=place_id:ChIJyzoASgHHwokRmOvBu6srYJk&hl=en,none,none,none,none,none
2058,N,Vero Beach Bathroom Remodeling Experts,"Vero Beach, FL",(772) 273-4264,"1848 Wilbur Ave, Vero Beach, FL 32960",https://www.google.com/maps/place/?q=place_id:ChIJS8Ogzx1f3ogRj1ULx4M7lnw&hl=en,none,none,none,none,none
2059,N,Elegant Kitchens,"American Fork, UT",(801) 550-3999,"1349 S 500 E, American Fork, UT 84003",https://www.google.com/maps/place/?q=place_id:ChIJtfBmX1SDTYcR3akf3fDGTlI&hl=en,none,none,none,none,none
2060,N,"Nicholas & Co Tile and Masonry Supply, LLC","Hailey, ID",(208) 788-5684,"1551 Colibri Ln C, Hailey, ID 83333",https://www.google.com/maps/place/?q=place_id:ChIJicGM0FHUq1QRY338IOMv5ro&hl=en,none,none,none,none,none
2061,N,Superior CustomCabinets,"Goldsboro, NC",(919) 330-8020,"170 Scott St, Goldsboro, NC 27534",https://www.google.com/maps/place/?q=place_id:ChIJkx8GiaiqrokR3ySMhAA8fjU&hl=en,none,none,none,none,none
2062,N,Irvine Bathroom Remodeling Pros,"Irvine, CA",(949) 628-6394,"910 Roosevelt, Irvine, CA 92620",https://www.google.com/maps/place/?q=place_id:ChIJryWexprd3IARXIbKZTFBh2Y&hl=en,none,none,none,none,none
2063,N,All Quality LLC,"Matthews, NC",(704) 302-6283,"Williams Rd, Matthews, NC 28105",https://www.google.com/maps/place/?q=place_id:ChIJq6hZhqkmVIgR7Smopupa_Fo&hl=en,none,none,none,none,none
2064,N,Redo Kitchen & Bath Remodeling Boca Raton,"Boca Raton, FL",(954) 614-7292,"3581 N Federal Hwy, Boca Raton, FL 33431",https://www.google.com/maps/place/?q=place_id:ChIJNUE8UXXh2IgR1QA5IMO6RQY&hl=en,none,none,none,none,none
2065,N,Royal Renovation & Design,"Stamford, CT",(914) 255-2314,"76 Progress Dr #264, Stamford, CT 06902",https://www.google.com/maps/place/?q=place_id:ChIJzf1Na6ZZwokRpjrefJt5RpI&hl=en,none,none,none,none,none
2066,N,Palmetto Renovation & Design LLC,"Gaffney, SC",(864) 450-9596,"301 N Limestone St, Gaffney, SC 29340",https://www.google.com/maps/place/?q=place_id:ChIJaUT4xuYFV4gRtS4jXh3cNvc&hl=en,none,none,none,none,none
2067,N,VIP Bathroom Remodeling & Restoration,"Lauderdale-By-The-Sea, FL",(726) 900-9564,"12 Hibiscus Ave, Lauderdale-By-The-Sea, FL 33308",https://www.google.com/maps/place/?q=place_id:ChIJT6gekdCx2YgRnxv4Aom-2gY&hl=en,none,none,none,none,none
2068,N,Kitchen Cabinets Of NJ LLC,"Moonachie, NJ",(973) 977-5809,"141 Moonachie Rd, Moonachie, NJ 07074",https://www.google.com/maps/place/?q=place_id:ChIJGSSAc_n5wokR2Z3-jzrwrK8&hl=en,none,none,none,none,none
2069,N,Musk Construction Bathroom Remodeling | Union City,"Union City, CA",(510) 470-7816,"33401 Western Ave Ste 1, Union City, CA 94587",https://www.google.com/maps/place/?q=place_id:ChIJ-cJ0sLnhNIgRpyQOaDEvDhI&hl=en,none,none,none,none,none
2070,N,Essence Kitchen & Bath,"Brandon, FL",(813) 330-1055,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ9_dlsU9S_AgR28PFqcg5Q1w&hl=en,none,none,none,none,none
2071,N,KFK Renovations,"Westport, MA",(508) 642-0435,"135A Cadmans Neck Rd, Westport, MA 02790",https://www.google.com/maps/place/?q=place_id:ChIJ_7Q31Lf45IkRFABdAg7qnFs&hl=en,none,none,none,none,none
2072,N,The Golden Touch,"Huntington, WV",(304) 412-9077,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ83UbVxfbXgYRFaw6p39be4g&hl=en,none,none,none,none,none
2073,N,InsideOut Design & Renovations LLC,"Dalton, GA",(706) 934-4516,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJc5NAEPQkHSERYQci9sC0FlU&hl=en,none,none,none,none,none
2074,N,Osuna Renovation Services,"Wolfforth, TX",(806) 786-5095,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJidaSTCwiPyQRPv-7u5xhV0Y&hl=en,none,none,none,none,none
2075,N,Charlie the Kitchen Magician,"Litchfield, CT",(203) 414-7492,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJF-Tbjm-Z54kRejnAd25AFt8&hl=en,none,none,none,none,none
2076,N,Alvarez Brothers Construction & Remodeling LLC,"Robbins, IL",(773) 418-4172,"3804 W 137th St, Robbins, IL 60472",https://www.google.com/maps/place/?q=place_id:ChIJ6YVIJBA9DogRKOw4vaJF4HM&hl=en,none,none,none,none,none
2077,N,Rommy's Kitchens & Closets by Design,"Chula Vista, CA",(619) 575-7707,"2260 Main St Ste 7, Chula Vista, CA 91911",https://www.google.com/maps/place/?q=place_id:ChIJdZ9dU8dN2YAR8x_0XKwVUBQ&hl=en,none,none,none,none,none
2078,N,"H&A Remodeler | Home, Deck & Kitchen Remodeling Boise","Boise, ID",(208) 213-2694,"11044 W Peconic Ct, Boise, ID 83709",https://www.google.com/maps/place/?q=place_id:ChIJcxpo3ulXrlQR59E27eCb6Kg&hl=en,none,none,none,none,none
2079,N,R & D Kitchen Interiors,"Warren, MI",(586) 759-3550,"31739 Mound Rd, Warren, MI 48092",https://www.google.com/maps/place/?q=place_id:ChIJhS_o4lrQJIgRoyDzy6VW7ew&hl=en,none,none,none,none,none
2080,N,Alan's Bathtub Refinishing,"Canton, OH",(330) 492-4125,"4600 Roosevelt Ave NE, Canton, OH 44705",https://www.google.com/maps/place/?q=place_id:ChIJ2RhNUNjRNogRt9Gfk1KtzC8&hl=en,none,none,none,none,none
2081,N,P&T Design Drafting And Renovations,"Grove City, PA",(724) 854-1083,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJe-5yOcwHM4gRtmw0XurkGxM&hl=en,none,none,none,none,none
2082,N,Custom Cabinet & Mill Work,"Redding, CA",(530) 246-7450,"1610 Tahoe Ct, Redding, CA 96003",https://www.google.com/maps/place/?q=place_id:ChIJDc4QPF2N0lQRd4VLVx4c9iY&hl=en,none,none,none,none,none
```
