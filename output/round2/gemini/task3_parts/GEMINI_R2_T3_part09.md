# Round 2: Gemini task 3, part 09 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1286, reply in that chat "Continue with the businesses
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
1237,N,Elegant Granite & Cabinets,"Gonzales, LA",(985) 318-2009,"311 S Burnside Ave, Gonzales, LA 70737",https://www.google.com/maps/place/?q=place_id:ChIJzdGYBXy1JoYR_JqC4ZyLM98&hl=en,none,none,none,none,none
1238,N,Options In Granite,"Collegeville, PA",(484) 902-8713,"134 2nd Ave, Collegeville, PA 19426",https://www.google.com/maps/place/?q=place_id:ChIJz_nMQLmQxokRsB5jdDRTNVA&hl=en,none,none,none,none,none
1239,N,Futura Custom Kitchen,"Warren, MI",(586) 576-7524,"2929 John B Ave, Warren, MI 48091",https://www.google.com/maps/place/?q=place_id:ChIJBb8RWqXRJIgRNwvjRB608Hc&hl=en,none,none,none,none,none
1240,N,Florida Cabinets Of Stuart,"Stuart, FL",(772) 324-8277,"257 SE Monterey Rd, Stuart, FL 34994",https://www.google.com/maps/place/?q=place_id:ChIJX9oiPBfd3ogRy-0XAqykrqU&hl=en,none,none,none,none,none
1241,N,Davis Interior Surfaces,"Tahlequah, OK",(918) 456-3500,"13813 US-62, Tahlequah, OK 74464",https://www.google.com/maps/place/?q=place_id:ChIJGcvGm_3_yYcR92Ord4iIe3Q&hl=en,none,none,none,none,none
1242,N,Cabinet Mania,"Munster, IN",(800) 531-8720,"822 Ridge Rd, Munster, IN 46321",https://www.google.com/maps/place/?q=place_id:ChIJX7QjumXgEYgRXyUjozqXuUA&hl=en,none,none,none,none,none
1243,N,Modern Cabinet & Construction,"Altoona, PA",(814) 942-1000,"110 Frankstown Rd, Altoona, PA 16602",https://www.google.com/maps/place/?q=place_id:ChIJm00VJGyRy4kRAsjj95Ypqtw&hl=en,none,none,none,none,none
1244,N,Conrads Cabinets & Doors,"Longview, TX",(903) 234-8348,"812 McKesson Dr, Longview, TX 75604",https://www.google.com/maps/place/?q=place_id:ChIJERroB5hHNoYRN76rOmrmnZo&hl=en,none,none,none,none,none
1245,N,Dynamic Cabinetry & Design,"Hewlett, NY",(516) 792-5855,"1195 Railroad Ave, Hewlett, NY 11557",https://www.google.com/maps/place/?q=place_id:ChIJQzRyncBlwokRgbH3v9c9M_E&hl=en,none,none,none,none,none
1246,N,Todd's Cabinets,"Mapleton, UT",(801) 489-0590,"50 S 1600 W, Mapleton, UT 84664",https://www.google.com/maps/place/?q=place_id:ChIJd6uuJku8TYcRtuJot_gkjo0&hl=en,none,none,none,none,none
1247,N,William Olsen Designs,"Phoenix, OR",(541) 326-1652,"216 Houston Rd, Phoenix, OR 97535",https://www.google.com/maps/place/?q=place_id:ChIJS83TeXp3z1QR_9eD07R6wss&hl=en,none,none,none,none,none
1248,N,Tri-Tex Cabinets - work,"Pilot Point, TX",(940) 686-2617,"900 US-377, Pilot Point, TX 76258",https://www.google.com/maps/place/?q=place_id:ChIJmxKkxcFPTIYRp5ItyYaJ9Po&hl=en,none,none,none,none,none
1249,N,RDB Bathroom Remodel,"Huron, SD",(206) 456-3329,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMUcIp44xJ4gRcY8C8pZAwro&hl=en,none,none,none,none,none
1250,N,Cabinets Kitchens,"Covington, GA",(770) 787-7211,"7187 Washington St SW, Covington, GA 30014",https://www.google.com/maps/place/?q=place_id:ChIJTY_D9EQ09IgR-ieanX9BXHM&hl=en,none,none,none,none,none
1251,N,Brandom Manufacturing of Texas,"Hillsboro, TX",(254) 580-1200,"404 Hawkins St, Hillsboro, TX 76645",https://www.google.com/maps/place/?q=place_id:ChIJpyUHYFioT4YRsHO-X6ouT0s&hl=en,none,none,none,none,none
1252,N,Home Remodel Boutique,"Edison, NJ",(732) 543-2022,"400 US-1, Edison, NJ 08817",https://www.google.com/maps/place/?q=place_id:ChIJ230SWHbJw4kRKfxLsFNVEnY&hl=en,none,none,none,none,none
1253,N,Tom's Cabinetry,"New Baltimore, MI",(586) 749-5700,"53377 Gratiot Ave, New Baltimore, MI 48051",https://www.google.com/maps/place/?q=place_id:ChIJq5IkWjMZJYgRXasN6zTubE4&hl=en,none,none,none,none,none
1254,N,"Meeder Design & Remodeling, Inc","Oak Brook, IL",(630) 709-3800,"1301 W 22nd St, Oak Brook, IL 60523",https://www.google.com/maps/place/?q=place_id:ChIJof3x3axMDogR9SFYWhaZroc&hl=en,none,none,none,none,none
1255,N,Q&P Woodcraft,"Seminole, TX",(432) 201-0182,"606 SE 4th St, Seminole, TX 79360",https://www.google.com/maps/place/?q=place_id:ChIJbS50Z-5n_IYR4_bD9wRLadA&hl=en,none,none,none,none,none
1256,N,Bath Planet of SW Florida,"Fort Myers, FL",(239) 427-0541,"11350 Metro Pkwy #104, Fort Myers, FL 33966",https://www.google.com/maps/place/?q=place_id:ChIJcywn-04V24gRjLH1lMAUrMo&hl=en,none,none,none,none,none
1257,N,"Easy Bath Solutions, LLC","Hatboro, PA",(267) 456-7300,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ1VdbvnKvxokRj4FhZrmn7xI&hl=en,none,none,none,none,none
1258,N,Acosta & Sons Inc,"Oakdale, CA",(209) 322-3181,"736 Wakefield Ct, Oakdale, CA 95361",https://www.google.com/maps/place/?q=place_id:ChIJvzsoHIoCkYARix_5qdJqIA4&hl=en,none,none,none,none,none
1259,N,Frederickson Flooring and Bath Renovations,"Miamisburg, OH",(937) 245-2579,"26 N Main St, Miamisburg, OH 45342",https://www.google.com/maps/place/?q=place_id:ChIJJ5KEd_pjQIgRUS87RKsW2OA&hl=en,none,none,none,none,none
1260,N,"Gulf Coast Cabinetry, LLC","Ponchatoula, LA",(985) 956-7097,"18228 S I-12 Service Rd, Ponchatoula, LA 70454",https://www.google.com/maps/place/?q=place_id:ChIJ9cZUcEchJ4YREU2kvqIdl3g&hl=en,none,none,none,none,none
1261,N,Danny's Top Shop,"Festus, MO",(636) 931-6606,"793 American Legion Dr, Festus, MO 63028",https://www.google.com/maps/place/?q=place_id:ChIJeyfhYOru2IcR7NvUvk-a3aU&hl=en,none,none,none,none,none
1262,N,Ric's Kitchen & Bath Showroom,"Castro Valley, CA",(510) 733-5543,"3664 Castro Valley Blvd, Castro Valley, CA 94546",https://www.google.com/maps/place/?q=place_id:ChIJU73eMTCSj4ARciFdKe_3Nlk&hl=en,none,none,none,none,none
1263,N,Luxe Haus Kitchen & Bath Remodeling,"Fort Worth, TX",(939) 633-2833,"640 Taylor St Suite 1200, Fort Worth, TX 76102",https://www.google.com/maps/place/?q=place_id:ChIJ969TWCFxToYRzQ0RD1RPt-c&hl=en,none,none,none,none,none
1264,N,Nordhouse Remodeling & Renovation,"Normandy Park, WA",(916) 275-0039,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJjxllcOqujAcR-C_4EwwRNoQ&hl=en,none,none,none,none,none
1265,N,"Alpha Stone, LLC","Swannanoa, NC",(828) 777-1965,"2576 US-70, Swannanoa, NC 28778",https://www.google.com/maps/place/?q=place_id:ChIJ1RcyxhaMWYgRkNGLXZVPkjY&hl=en,none,none,none,none,none
1266,N,Gordy's Custom Cabinets,"East Bethel, MN",(763) 434-7071,"1861 Viking Blvd NE, East Bethel, MN 55011",https://www.google.com/maps/place/?q=place_id:ChIJ6WqoA1IZs1IRbAWPibeAX0w&hl=en,none,none,none,none,none
1267,N,KM Construction & Remodeling,"Lock Haven, PA",(570) 660-9303,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJsaO36zrt-UYRWnzaUQHMQjY&hl=en,none,none,none,none,none
1268,N,Brothers Flooring,"Pocahontas, AR",(870) 892-2525,"1805 Old County Rd, Pocahontas, AR 72455",https://www.google.com/maps/place/?q=place_id:ChIJoVC5EKfA1ocRptqMOAbIYlc&hl=en,none,none,none,none,none
1269,N,Her Renovations llc,"East Cleveland, OH",(216) 815-2626,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhyx-lyC5YqcRY8y3ie1xK8g&hl=en,none,none,none,none,none
1270,N,Kitchen & Bath Inspirations,"Clinton, IA",(563) 241-1918,"1845 Manufacturing Dr # C, Clinton, IA 52732",https://www.google.com/maps/place/?q=place_id:ChIJ-6K4U69m4ocRa75dT5KnHyA&hl=en,none,none,none,none,none
1271,N,Remodeling Expo,"Downers Grove, IL",(630) 724-9000,"412 75th St, Downers Grove, IL 60516",https://www.google.com/maps/place/?q=place_id:ChIJkSJDy_NPDogRZpU_6pkqUGg&hl=en,none,none,none,none,none
1272,N,Qualified Home Solutions LLC,"Barnesville, GA",(678) 572-4459,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ98ChK_mP9IgRAAUERCzitvY&hl=en,none,none,none,none,none
1273,N,MGB remodeling LLC,"Independence, KY",(859) 446-3934,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvXLCBI_HQYgRpU5HQ10nFmg&hl=en,none,none,none,none,none
1274,N,Heart of the Home Design-Build,"Winchester, VA",(540) 877-0429,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJrxjopsPutYkRgpDHeVs1oXA&hl=en,none,none,none,none,none
1275,N,A&S Home Remodeling LLC,"Kissimmee, FL",(954) 701-2546,"4751 Luminous Loop, Kissimmee, FL 34746",https://www.google.com/maps/place/?q=place_id:ChIJV9DPvHep2YgRaGsz1fW0C1Y&hl=en,none,none,none,none,none
1276,N,Orchard Home Designs,"Hickory Creek, TX",(469) 247-7758,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMfHTKfa4R4gRTBHeYvOTAN0&hl=en,none,none,none,none,none
1277,N,Kujos Custom LLC,"Sealy, TX",(832) 788-0019,"1789 Lezak Rd, Sealy, TX 77474",https://www.google.com/maps/place/?q=place_id:ChIJcxoBz8g4QYYRqI3YC_ms0dE&hl=en,none,none,none,none,none
1278,N,The Ramsay Group INC,"Naples, FL",(239) 778-5570,"3437 Westview Dr, Naples, FL 34104",https://www.google.com/maps/place/?q=place_id:ChIJBWKnRGbj2ogRt0d6owwWJXg&hl=en,none,none,none,none,none
1279,N,Tussey Mountain Custom Kitchen,"Meadville, PA",(814) 337-6733,"1061 Park Ave, Meadville, PA 16335",https://www.google.com/maps/place/?q=place_id:ChIJi68ZYA1XMogR-NP4jofaH7o&hl=en,none,none,none,none,none
1280,N,Wentzell Cabinet Shop Inc,"Birmingham, AL",(205) 836-5999,"2804 Woodwork Way, Birmingham, AL 35210",https://www.google.com/maps/place/?q=place_id:ChIJazC6VIwNiYgRry5Qs9l48wo&hl=en,none,none,none,none,none
1281,N,Martinez Complete Remodeling Services LLC,"DeBary, FL",(315) 992-3667,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJha7ler2OVYERblbd9kfENvg&hl=en,none,none,none,none,none
1282,N,Corner Cabinet,"Neosho, MO",(417) 451-2363,"12628 State Hwy 86, Neosho, MO 64850",https://www.google.com/maps/place/?q=place_id:ChIJo0TaAA1gyIcRIfL6j7svuzA&hl=en,none,none,none,none,none
1283,N,GP RemodelingServices,"Kyle, TX",(512) 756-3469,"181 Maroon Ln, Kyle, TX 78640",https://www.google.com/maps/place/?q=place_id:ChIJ6z2da-JTW4YRx6c9fvopoYw&hl=en,none,none,none,none,none
1284,N,Petrey's Cabinet Shop,"Science Hill, KY",(606) 423-2002,"923 Stringtown Rd, Science Hill, KY 42553",https://www.google.com/maps/place/?q=place_id:ChIJlcCpQrC0QogRtJk7qTwRby0&hl=en,none,none,none,none,none
1285,N,Resurrection Contracting LLC,"Flowery Branch, GA",(470) 266-7320,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJPS9PfIopd0IR0H8__pNfiYk&hl=en,none,none,none,none,none
1286,N,"Arnold's Custom Renovations, LLC","Chesapeake, VA",(757) 227-8910,"1140 Sharon Dr, Chesapeake, VA 23320",https://www.google.com/maps/place/?q=place_id:ChIJ7wxgAi-9uokRNB3xBChSAmY&hl=en,none,none,none,none,none
```
