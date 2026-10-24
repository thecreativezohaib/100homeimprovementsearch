# Round 2: Gemini task 3, part 16 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 2032, reply in that chat "Continue with the businesses
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
1883,N,"DC Cabinets, LLC","Dickson, TN",(615) 829-0476,"1401 US-70, Dickson, TN 37055",https://www.google.com/maps/place/?q=place_id:ChIJYeZY8p67ZIgRk9pQyP9dXGE&hl=en,none,none,none,none,none
1952,N,Kingdom Karpentry,"Darby, PA",(484) 372-0602,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJY119kFXBxokRMyn_HcCikKI&hl=en,none,none,none,none,none
1953,N,A Cabinet Above Kitchen Remodelers,"Bargersville, IN",(317) 771-1103,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJN4Gx3jKpMaMRfjzSEN_0PWs&hl=en,none,none,none,none,none
1954,N,Cabinet Specialties LLC,"Plainville, CT",(860) 747-4114,"38 Neal Ct, Plainville, CT 06062",https://www.google.com/maps/place/?q=place_id:ChIJMTvSD--w54kRsWXVFWKRKN8&hl=en,none,none,none,none,none
1955,N,Alfa Home Solutions | Bathroom renovation | Kitchen remodeling | Carpentry | Flooring installation | Painting,"Ocoee, FL",(689) 356-6801,"1711 Amazing Way Ste 213, Ocoee, FL 34761",https://www.google.com/maps/place/?q=place_id:ChIJl4S0w66D54gR3ra4wmQZU48&hl=en,none,none,none,none,none
1956,N,Timeless Renovations,"Christiansburg, VA",(540) 404-8586,"150 Corning Dr, Christiansburg, VA 24073",https://www.google.com/maps/place/?q=place_id:ChIJs0VVHDrKbm4RQYNw5XyaDhI&hl=en,none,none,none,none,none
1957,N,Abernethy Enterprises Construction Group,"Orange City, FL",(858) 667-0142,"1195 13th St, Orange City, FL 32763",https://www.google.com/maps/place/?q=place_id:ChIJLxoMjyUb54gR9k943v9KYeY&hl=en,none,none,none,none,none
1958,N,Custom Cabinet Doors Inc,"Pilot Point, TX",(940) 686-2808,"924 N Industrial Blvd, Pilot Point, TX 76258",https://www.google.com/maps/place/?q=place_id:ChIJfxiIeupPTIYRI9STclO8Yww&hl=en,none,none,none,none,none
1959,N,Performance Kitchen & Bathroom Remodel Tulsa,"Verdigris, OK",(918) 400-0660,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJB4R7a5M6dkQRUbqCMXMguEY&hl=en,none,none,none,none,none
1960,N,"Rose Rock Remodeling, LLC","Noble, OK",(580) 278-8069,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJwZqxRK1Re2kR2MKOtc1XeSI&hl=en,none,none,none,none,none
1961,N,K&E Home Upgrades Remodeling Contractor,"Mt Carmel, TN",(423) 765-3376,"138 Inca Dr, Mt Carmel, TN 37645",https://www.google.com/maps/place/?q=place_id:ChIJg_eCNOrxWogRnIES3Q58YrE&hl=en,none,none,none,none,none
1962,N,RMZ Renovations LLC,"Selma, NC",(984) 274-5232,"154 Halton Ln, Selma, NC 27576",https://www.google.com/maps/place/?q=place_id:ChIJk1Ls0fATrIkRhGeTx_Ko53o&hl=en,none,none,none,none,none
1963,N,DC Remodeling and Home Repair LLC,"Monmouth, OR",(971) 718-3764,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJBSwFldxuEiERTw4pkRhLXKQ&hl=en,none,none,none,none,none
1964,N,Heredia's Custom Cabinets,"Santa Paula, CA",(805) 524-7727,"957 Faulkner Rd #212, Santa Paula, CA 93060",https://www.google.com/maps/place/?q=place_id:ChIJAxynfAO16YARtM8c4oiS9us&hl=en,none,none,none,none,none
1965,N,R&R Handyman & Renovation's LLC,"Henderson, NC",(252) 767-0586,"500 J P Taylor Rd lot 36, Henderson, NC 27537",https://www.google.com/maps/place/?q=place_id:ChIJL7aJR-27rYkRLpIuM4dgzcY&hl=en,none,none,none,none,none
1966,N,Northern Countertops & Cabinets,"Ukiah, CA",(707) 467-3969,"195 Clara Ave Entrance on, Mason St, Ukiah, CA 95482",https://www.google.com/maps/place/?q=place_id:ChIJVWq2mSt7gYARpa4Uxx0jEls&hl=en,none,none,none,none,none
1967,N,Navarro Construction Solutions,"Dade City, FL",(352) 807-2790,"15045 Pinellas Ave, Dade City, FL 33523",https://www.google.com/maps/place/?q=place_id:ChIJK3uufUaCXgUR23hwYJ2Ikng&hl=en,none,none,none,none,none
1968,N,Deb's Cabinet Shop,"Brookland, AR",(870) 935-0193,"303 S Holman St, Brookland, AR 72417",https://www.google.com/maps/place/?q=place_id:ChIJz1lL4GnV1YcRs6oz6LcYYB8&hl=en,none,none,none,none,none
1969,N,Cottrell Renovation LLC,"Mooresville, IN",(317) 287-4171,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ66_RV9Hjx6MRs_VaozX3m9s&hl=en,none,none,none,none,none
1970,N,Top Home Kitchen Remodeling,"Rolling Hills Estates, CA",(424) 478-8010,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJia_c4v_pgSYRF6hU4F48Kvw&hl=en,none,none,none,none,none
1971,N,Laurel river renovations,"Corbin, KY",(606) 404-1752,"185 E Lewis St, Corbin, KY 40701",https://www.google.com/maps/place/?q=place_id:ChIJN_9yTqjFXIgRb87zcz3iDjw&hl=en,none,none,none,none,none
1972,N,SPIR Homes,"New Smyrna Beach, FL",(386) 290-4838,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJuypQycqLXa8RSKwBIuaAumw&hl=en,none,none,none,none,none
1973,N,AK Contracting,"Pontiac, IL",(779) 804-6017,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqZWAaN94_GgR7faEyy9_TQI&hl=en,none,none,none,none,none
1974,N,Classic Spaces LLC,"Georgetown, KY",(859) 492-0070,"401 Outlet Center Dr #280, Georgetown, KY 40324",https://www.google.com/maps/place/?q=place_id:ChIJU9i4XDQ_QogR0Y7JZ0uS1WI&hl=en,none,none,none,none,none
1975,N,H&T Custom Interiors,"Graham, TX",(940) 456-3734,"1033 4th St, Graham, TX 76450",https://www.google.com/maps/place/?q=place_id:ChIJx7eqm3zJU4YRiMj-mu5nmQY&hl=en,none,none,none,none,none
1976,N,"Birmingham Remodeling and Construction, LLC","Stillwater, OK",(405) 612-9708,"4018 Yorkshire Dr, Stillwater, OK 74074",https://www.google.com/maps/place/?q=place_id:ChIJ45u6W46gsYcRlyHpYufw0_k&hl=en,none,none,none,none,none
1977,N,Modern Kitchen Makeovers,"Santa Fe Springs, CA",(562) 554-6566,"13063 Rosecrans Ave c, Santa Fe Springs, CA 90670",https://www.google.com/maps/place/?q=place_id:ChIJMQm5p44t3YARScvw67vYh_c&hl=en,none,none,none,none,none
1978,N,G&L Heilman Remodeling,"Taneytown, MD",(410) 218-9116,"4272 Francis Scott Key Hwy, Taneytown, MD 21787",https://www.google.com/maps/place/?q=place_id:ChIJZ1BSj9ZNyIkR_pdpxfXTSwQ&hl=en,none,none,none,none,none
1979,N,Fenn construction LLC,"Azle, TX",(817) 495-8897,"252 Mountain View Dr, Azle, TX 76020",https://www.google.com/maps/place/?q=place_id:ChIJe5__qmUvsYYRlkWxLiOqdE8&hl=en,none,none,none,none,none
1980,N,URESTI Fine Woodworks,"Donna, TX",(956) 884-1924,"807 N Hutto Rd, Donna, TX 78537",https://www.google.com/maps/place/?q=place_id:ChIJOa8Fj_J1ZYYR91FKldGNTC8&hl=en,none,none,none,none,none
1981,N,Baker Tile,"Sanger, CA",(559) 770-5732,"21343 E Weldon Ave, Sanger, CA 93657",https://www.google.com/maps/place/?q=place_id:ChIJKyBt1OYBlYARxhegQGWiKsU&hl=en,none,none,none,none,none
1982,N,Keystone Home Improvement LLC,"Washougal, WA",(360) 904-7374,"4031 Addy St, Washougal, WA 98671",https://www.google.com/maps/place/?q=place_id:ChIJvQ6krb-9lVQRHLgN6iSHOEM&hl=en,none,none,none,none,none
1983,N,Fusion Refinishing,"West Wareham, MA",(508) 807-3477,"47 Crest Dr, West Wareham, MA 02576",https://www.google.com/maps/place/?q=place_id:ChIJIQmxH5KjBEMRZAEq3SLBSwU&hl=en,none,none,none,none,none
2015,N,Mc Gowan Cabinet Co,"Forest Lake, MN",(651) 464-2209,"23804 Northlake Blvd, Forest Lake, MN 55025",https://www.google.com/maps/place/?q=place_id:ChIJueGh9tPnslIR3GHrUwW7HwQ&hl=en,none,none,none,none,none
2016,N,"Kitchen Beautiful, LLC","Broadview Heights, OH",(216) 299-6354,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJB4qQx9jdMIgRMvGhDNZ2bSg&hl=en,none,none,none,none,none
2017,N,cali cabinet renovation,"Bakersfield, CA",(408) 813-8270,"3432 Gilmore Ave, Bakersfield, CA 93308",https://www.google.com/maps/place/?q=place_id:ChIJ9Yv3lapp6oAR0g6xjzeu2Zk&hl=en,none,none,none,none,none
2019,N,l,"Glendale, CA",(323) 599-1456,"1200 S Brand Blvd Ste 416, Glendale, CA 91204",https://www.google.com/maps/place/?q=place_id:ChIJ22fIXA3BwoARvNTRvLHC8JU&hl=en,none,none,none,none,none
2020,N,Kitchens and Bath by Design,"LaGrange, GA",(706) 443-5139,"1379 Lafayette Pkwy, LaGrange, GA 30241",https://www.google.com/maps/place/?q=place_id:ChIJ_ZLE61xUi4gROapTYaUHXpc&hl=en,none,none,none,none,none
2021,N,Woodbridge Kitchen & Bath LLC,"Woodbridge, CT",(203) 393-6803,"24 Sunbrook Rd, Woodbridge, CT 06525",https://www.google.com/maps/place/?q=place_id:ChIJF1pPvMTf54kRg1X_uU6eM9A&hl=en,none,none,none,none,none
2022,N,Northern Nevada Cabinets,"Fernley, NV",(775) 575-6611,"45 E Front St, Fernley, NV 89408",https://www.google.com/maps/place/?q=place_id:ChIJRaSGTl7dmIARHmhruJ-24uU&hl=en,none,none,none,none,none
2023,N,AB Kitchen Bathroom Remodeling Monrovia,"Monrovia, CA",(626) 210-0196,"133 E Maple Ave, Monrovia, CA 91016",https://www.google.com/maps/place/?q=place_id:ChIJd3ewB0PZwoARle9Cv1NzyDI&hl=en,none,none,none,none,none
2024,N,Polar Kitchen Bathroom Remodeling Agoura Hills,"Agoura Hills, CA",(818) 208-0758,"30406 Passageway Pl, Agoura Hills, CA 91301",https://www.google.com/maps/place/?q=place_id:ChIJEWW8wcadwoARMKhVExKEqII&hl=en,none,none,none,none,none
2025,N,Ocean State Kitchen & Bath Inc,"Warwick, RI",(401) 921-4885,"63 Alhambra Rd, Warwick, RI 02886",https://www.google.com/maps/place/?q=place_id:ChIJC6hnooJO5IkRqpHujpawpKg&hl=en,none,none,none,none,none
2026,N,Signature Kitchens,"Memphis, TN",(901) 450-3233,"3870 New Getwell Rd, Memphis, TN 38118",https://www.google.com/maps/place/?q=place_id:ChIJEYYlyByGf4gR1R536MhDhe8&hl=en,none,none,none,none,none
2027,N,Majestic Marble,"Farmington, NM",(505) 326-2447,"2801 La Plata Hwy C, Farmington, NM 87401",https://www.google.com/maps/place/?q=place_id:ChIJu5ikMi-QO4cRyD7fAYn96Zc&hl=en,none,none,none,none,none
2028,N,Cabinet Works,"Richmond, KY",(859) 625-9070,"620 Big Hill Ave #6, Richmond, KY 40475",https://www.google.com/maps/place/?q=place_id:ChIJ7-2KuIn9QogRhuMHHFVvav0&hl=en,none,none,none,none,none
2029,N,Dynamic Designs Custom Countertops Inc.,"Marion, IN",(765) 573-4982,"3818 S Lincoln Blvd, Marion, IN 46953",https://www.google.com/maps/place/?q=place_id:ChIJHWYVM6b_FIgRZ-7Y_rmiu5o&hl=en,none,none,none,none,none
2030,N,Homeplus Kitchen and Bath Company,"Lawndale, CA",(310) 503-8446,"15317 Hawthorne Blvd, Lawndale, CA 90260",https://www.google.com/maps/place/?q=place_id:ChIJK03311S1woARTdsyf5fpQAc&hl=en,none,none,none,none,none
2031,N,Creative Cabinets & Floors,"Somersworth, NH",(603) 923-3687,"28 Green St, Somersworth, NH 03878",https://www.google.com/maps/place/?q=place_id:ChIJ3cBVdSKZ4okRwHaJYkkjX44&hl=en,none,none,none,none,none
2032,N,Top-Notch Tile & Renovations,"Clinton, IA",(563) 249-6815,"652 8th Ave S, Clinton, IA 52732",https://www.google.com/maps/place/?q=place_id:ChIJi05IRSFl4ocRl9en9V2HIQg&hl=en,none,none,none,none,none
```
