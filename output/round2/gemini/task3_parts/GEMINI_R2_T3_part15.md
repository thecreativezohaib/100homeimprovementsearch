# Round 2: Gemini task 3, part 15 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1882, reply in that chat "Continue with the businesses
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
1833,N,Stoneworks,"Pocatello, ID",(208) 237-0696,"12499 W Reservation Rd, Pocatello, ID 83202",https://www.google.com/maps/place/?q=place_id:ChIJt0oficpGVVMRuZ7dGJEfOew&hl=en,none,none,none,none,none
1834,N,S and M Home Improvements,"Troy, OH",(937) 418-9954,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJt2mHYyI5n6ERWzinROuUZSo&hl=en,none,none,none,none,none
1835,N,Amaya Design & Remodeling,"Odessa, TX",(432) 215-5540,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZaWMR3CzsQYRaS7fsH81zow&hl=en,none,none,none,none,none
1836,N,mprodesign,"Wheeling, IL",(773) 657-0141,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJO-Y6kaTNlkMRimRRPVR9xE8&hl=en,none,none,none,none,none
1837,N,LM KITCHEN DESIGN,"Miami Springs, FL",(786) 674-1905,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv4t4ImWgRwMRhjU9Wkr3XwU&hl=en,none,none,none,none,none
1838,N,Cabinet Factory,"Duncan, OK",(580) 255-2111,"1000 McCurdy Rd, Duncan, OK 73533",https://www.google.com/maps/place/?q=place_id:ChIJ29hsdLNCrYcR6ToJ7R6cRz0&hl=en,none,none,none,none,none
1839,N,Rene's Painting & Remodeling Services,"Melrose Park, IL",(708) 600-5964,"705 N 17th Ave, Melrose Park, IL 60160",https://www.google.com/maps/place/?q=place_id:ChIJw-LbgkSRJ0MRzn_aXz_9G30&hl=en,none,none,none,none,none
1840,N,K&S Remodeling and Custom Cabinetry,"White Bear Lake, MN",(612) 518-3804,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTfeQynzXslIRi3DAZu5blcg&hl=en,none,none,none,none,none
1841,N,cml home renovation LLC,"Morrow, GA",(470) 315-5132,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7zgEpmdkMC4RFEZEjcB-RY8&hl=en,none,none,none,none,none
1842,N,Fidelis Remodeling Group,"McCordsville, IN",(317) 910-4718,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJaSaIDyW1FIgRsy1NOSJMhjo&hl=en,none,none,none,none,none
1843,N,Designs Plus Kitchen & Bath,"Brookfield, CT",(203) 740-7744,"246 Federal Rd STE C11, Brookfield, CT 06804",https://www.google.com/maps/place/?q=place_id:ChIJKXlPRuH554kRzPOL2BJFICk&hl=en,none,none,none,none,none
1844,N,HSP Kitchen Remodel,"Bremerton, WA",(360) 997-2338,"828 Broadway Ave Unit A, Bremerton, WA 98337",https://www.google.com/maps/place/?q=place_id:ChIJRTAUZRI3kFQRLTOjM5ef5c8&hl=en,none,none,none,none,none
1845,N,Moses Custom Cabinetry LLC,"Burley, ID",(208) 650-0279,"389 S 250 E, Burley, ID 83318",https://www.google.com/maps/place/?q=place_id:ChIJT5h_daM1q1QRUdZqp5VTs4U&hl=en,none,none,none,none,none
1846,N,Construction J&C LLC,"Cottonwood Heights, UT",(561) 695-6571,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJW1M4I68z3QURlp_BrknXUCo&hl=en,none,none,none,none,none
1847,N,Blanchard Home Improvements,"Lafayette, LA",(337) 255-2482,"619 Bonin Rd, Lafayette, LA 70508",https://www.google.com/maps/place/?q=place_id:ChIJ9SXGDz-dJIYRsy0YCk0I-ps&hl=en,none,none,none,none,none
1848,N,Fischer Tile & Floor Covering,"Brenham, TX",(979) 836-5616,"2221 S Market St, Brenham, TX 77833",https://www.google.com/maps/place/?q=place_id:ChIJs3nr6UmoRoYR_T8XB8pB44M&hl=en,none,none,none,none,none
1849,N,Ronnie's Resolutions,"Chickasha, OK",(405) 200-3138,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgbn-9Vo3TCYR7mhzSefpCAs&hl=en,none,none,none,none,none
1850,N,Rogue Valley Marble & Granite LLC,"Grants Pass, OR",(541) 474-4319,"2375 Foothill Blvd A, Grants Pass, OR 97526",https://www.google.com/maps/place/?q=place_id:ChIJmUUAuXl5xVQR2Z53Xzxywxw&hl=en,none,none,none,none,none
1851,N,Casa crafted remodeling LLC,"Humble, TX",(832) 960-0260,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJEfmHJlRzHGURV2tP1T0vzmQ&hl=en,none,none,none,none,none
1852,N,Cetile California,"Hemet, CA",(951) 399-1076,"245 Hanoverian Dr, Hemet, CA 92545",https://www.google.com/maps/place/?q=place_id:ChIJge7bUz1EzQsRnnoZ97v3jWI&hl=en,none,none,none,none,none
1853,N,Sierra Construction & Design LLC,"Reno, NV",(775) 771-5165,"5655 Riggins Ct #13, Reno, NV 89502",https://www.google.com/maps/place/?q=place_id:ChIJR2ftNusPHQURNZJww3qz0XM&hl=en,none,none,none,none,none
1854,N,Wolverine Maintenance LLC,"Allen Park, MI",(734) 368-8034,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJi8wRFyxDrGMR2GWDoGodMA4&hl=en,none,none,none,none,none
1855,N,Lightshine Design,"Massillon, OH",(330) 232-3249,"2137 Wales Ave NW Unit 1, Massillon, OH 44646",https://www.google.com/maps/place/?q=place_id:ChIJGxxMxijXNogRfG0m4DfWYQ8&hl=en,none,none,none,none,none
1856,N,Awe Home Services LLC,"Watertown, WI",(920) 206-2751,"419 Humboldt St, Watertown, WI 53094",https://www.google.com/maps/place/?q=place_id:ChIJHUqa7F0rBIgRU0NP7OUzHlQ&hl=en,none,none,none,none,none
1857,N,AC Designer Cabinets,"West Park, FL",(954) 274-5766,"5927 SW 21st St, West Park, FL 33023",https://www.google.com/maps/place/?q=place_id:ChIJp08JlsWv2YgRJCVhZW_f8JI&hl=en,none,none,none,none,none
1858,N,Highlands Cabinet Inc,"Sebring, FL",(863) 385-4396,"739 Glenwood Ave, Sebring, FL 33870",https://www.google.com/maps/place/?q=place_id:ChIJO5edjzlX3IgRfm24BTlgYDM&hl=en,none,none,none,none,none
1859,N,Vito Remodeling And Refinishing Inc,"Forest Park, IL",(708) 369-9263,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJrxftda4ZkyQRGMBi36gYyUU&hl=en,none,none,none,none,none
1860,N,Versatile Renovations,"Fernandina Beach, FL",(678) 320-7202,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZ2iS9Zer5YgReBGnVHn2j6Q&hl=en,none,none,none,none,none
1861,N,Designer Kitchen & Bath Div.,"Madison, AL",(256) 858-1970,"106 Castle Dr, Madison, AL 35758",https://www.google.com/maps/place/?q=place_id:ChIJNZJDLeZpYogRqsud-3G139E&hl=en,none,none,none,none,none
1862,N,United Kitchen & Bath,"Kenner, LA",(504) 780-8400,"2304 Marietta St, Kenner, LA 70062",https://www.google.com/maps/place/?q=place_id:ChIJ78IcAjO3IIYR42xroOpzZ_g&hl=en,none,none,none,none,none
1863,N,Precious Custom Cabinets / Pacific Custom Millwork Inc.,"South Gate, CA",(323) 476-7777,"10600 Dolores Ave, South Gate, CA 90280",https://www.google.com/maps/place/?q=place_id:ChIJE6PDQO_LwoAR7Pt8c4QlKug&hl=en,none,none,none,none,none
1864,N,B&B Home Improvement & Design,"Hallandale Beach, FL",(305) 940-9881,"800 Silks Run, Hallandale Beach, FL 33009",https://www.google.com/maps/place/?q=place_id:ChIJBeq_u4es2YgRlu6PCDtEDSA&hl=en,none,none,none,none,none
1865,N,Kitchen & Bath Cabinets,"El Paso, TX",(915) 852-0499,"13682 Nayarit Dr, El Paso, TX 79928",https://www.google.com/maps/place/?q=place_id:ChIJY9W_SxtB54YRTUBC7Q5TpOk&hl=en,none,none,none,none,none
1866,N,Vogue Kitchen and Bath,"Dana Point, CA",(949) 493-9998,"34085 CA-1 #205, Dana Point, CA 92629",https://www.google.com/maps/place/?q=place_id:ChIJI8egbhDw3IARDvRQ3sQFCmE&hl=en,none,none,none,none,none
1867,N,RW Tile,"Scottsboro, AL",(256) 305-3331,"784 Co Rd 30, Scottsboro, AL 35768",https://www.google.com/maps/place/?q=place_id:ChIJ4wJ1ksnxYYgRrtpFBeDdPCg&hl=en,none,none,none,none,none
1868,N,Advanced Cabinetry Inc,"Prineville, OR",(541) 447-7024,"2853 SW High Desert Dr, Prineville, OR 97754",https://www.google.com/maps/place/?q=place_id:ChIJ-2gfi-wtuVQRnx63G_0zRZI&hl=en,none,none,none,none,none
1869,N,JP Custom Cabinets and Construction,"Krum, TX",(940) 580-8123,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJnddUr3Od2iERK3jFETUe3Jo&hl=en,none,none,none,none,none
1870,N,Greenwood Kitchen Cabinet & Countertop,"Williston Park, NY",(516) 294-1918,"368 Hillside Ave., Williston Park, NY 11596",https://www.google.com/maps/place/?q=place_id:ChIJgyLhZAeIwokR7LXq6rZ_kkQ&hl=en,none,none,none,none,none
1871,N,A+ countertops & home remodeling,"Charlotte, NC",(704) 773-8670,"6024 McDaniel Ln, Charlotte, NC 28213",https://www.google.com/maps/place/?q=place_id:ChIJV609E68fVIgRqi70F8e9wDo&hl=en,none,none,none,none,none
1872,N,American Kitchen Bathroom Renovation Los Angeles,"Los Angeles, CA",(310) 691-8856,"8616 S La Tijera Blvd, Los Angeles, CA 90045",https://www.google.com/maps/place/?q=place_id:ChIJzbedr9OwwoARyurafC3O5cA&hl=en,none,none,none,none,none
1873,N,Elite Custom Cabinets & Trim LLC,"Sulphur, LA",(337) 502-2296,"144 S Post Oak Rd, Sulphur, LA 70663",https://www.google.com/maps/place/?q=place_id:ChIJD1Wh53SNO4YRCAYdo_6s784&hl=en,none,none,none,none,none
1874,N,Phoenix Home Remodeling,"Fairview Heights, IL",(618) 207-3090,"10890 Lincoln Trail, Fairview Heights, IL 62208",https://www.google.com/maps/place/?q=place_id:ChIJI_8ZsQzEm2MRIzU9wLdQAg8&hl=en,none,none,none,none,none
1875,N,Yazmin Tiles,"Tavernier, FL",(305) 484-2030,"Next to ACE Hardware, 91880 Overseas Hwy, Tavernier, FL 33070",https://www.google.com/maps/place/?q=place_id:ChIJBz3vwutA14gRiOaiSFmihD4&hl=en,none,none,none,none,none
1876,N,Gentile Homes & Renovations,"Boiling Spring Lakes, NC",(518) 935-3793,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJT1W4PnOV_GkRQ5XmoVoHiPc&hl=en,none,none,none,none,none
1877,N,B & C Cabinets & Millwork,"Carson City, NV",(775) 322-0000,"5241 Metric Way, Carson City, NV 89706",https://www.google.com/maps/place/?q=place_id:ChIJg9xW0aoLmYARfeAwiVjPYeA&hl=en,none,none,none,none,none
1878,N,Unique Tile,"Turlock, CA",(209) 676-0575,"320 S Broadway, Turlock, CA 95380",https://www.google.com/maps/place/?q=place_id:ChIJ70Oh2jUGkYARBs3UK_qUs9Y&hl=en,none,none,none,none,none
1879,N,Florida Kitchen Design and Bath LLC,"Boynton Beach, FL",(561) 769-0380,"1257 Vía Panzani, Boynton Beach, FL 33426",https://www.google.com/maps/place/?q=place_id:ChIJVc7veXbKpIcREQ24g7C59Gc&hl=en,none,none,none,none,none
1880,N,Hanson's Home Improvements,"Janesville, WI",(608) 921-8353,"1312 Blaine Ave, Janesville, WI 53545",https://www.google.com/maps/place/?q=place_id:ChIJC7j0ww8aBogRF6zy-kdL7eU&hl=en,none,none,none,none,none
1881,N,"Sumter Reglazing,LLC","Sumter, SC",(803) 847-1008,"2804 Cains Mill Rd, Sumter, SC 29154",https://www.google.com/maps/place/?q=place_id:ChIJZWy669Nr_4gRdzzZKJ1HgZ8&hl=en,none,none,none,none,none
1882,N,Antonio Cabinetry,"Sleepy Hollow, NY",(914) 631-2353,"334 N Broadway, Sleepy Hollow, NY 10591",https://www.google.com/maps/place/?q=place_id:ChIJIQTmV6HqwokRx-7v0ebGMcs&hl=en,none,none,none,none,none
```
