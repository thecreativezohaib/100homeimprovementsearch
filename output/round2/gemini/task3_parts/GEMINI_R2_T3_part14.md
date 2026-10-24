# Round 2: Gemini task 3, part 14 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1832, reply in that chat "Continue with the businesses
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
1542,N,Lakeside Renovations LLC,"South Milwaukee, WI",(414) 578-6916,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6QAxC1jZHEgRimzlvdlxgQ4&hl=en,none,none,none,none,none
1543,N,"Stetzel Builders, Inc.","Eureka, CA",(707) 499-7427,"Eureka, CA 95502",https://www.google.com/maps/place/?q=place_id:ChIJgz9zkar_01QRmUECSANWtEU&hl=en,none,none,none,none,none
1544,N,"The Tub Wizard, Inc.","Pittsburgh, PA",(412) 343-6006,"394 Anawanda Ave, Pittsburgh, PA 15228",https://www.google.com/maps/place/?q=place_id:ChIJ3SqJvmf3NIgRLTqY4gyfBDc&hl=en,none,none,none,none,none
1545,N,Infinity Construction WDM,"Clive, IA",(515) 630-6994,"15920 Hickman Rd Unit 300, Clive, IA 50325",https://www.google.com/maps/place/?q=place_id:ChIJzysG8xwj7IcR-IihX0XM0cc&hl=en,none,none,none,none,none
1546,N,Jersey Fresh | Tub & Tile Refinishing,"Cranford, NJ",(732) 318-9793,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJn6sSytazw4kRtZfM6F2RMcI&hl=en,none,none,none,none,none
1547,N,Valley Kitchen and Bath Design Centers,"Chowchilla, CA",(209) 445-6580,"307 W Robertson Blvd, Chowchilla, CA 93610",https://www.google.com/maps/place/?q=place_id:ChIJUVr86kxDkYARt0oZBVvaCrg&hl=en,none,none,none,none,none
1548,N,"Thomas construction and remodeling, LLC","Snyder, TX",(325) 242-5613,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJSaopV9PDlEwRlyyDxNRTfXg&hl=en,none,none,none,none,none
1549,N,Golden Profit Cabinets,"Walnut, CA",(909) 869-8633,"875 Fairway Dr, Walnut, CA 91789",https://www.google.com/maps/place/?q=place_id:ChIJVVVVVSU1w4ARRn93yuMy_g4&hl=en,none,none,none,none,none
1550,N,Top of the Mark Refinishing,"Granbury, TX",(817) 219-0946,"2701 Creek Dr, Granbury, TX 76048",https://www.google.com/maps/place/?q=place_id:ChIJH3zKFy4hToYRwwfjFTvOVz4&hl=en,none,none,none,none,none
1551,N,Cabinet King,"Needles, CA",(928) 546-4271,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJy9XoxXyH3SIRgzDOyDxXl8U&hl=en,none,none,none,none,none
1552,N,Wiley's Services,"Owensboro, KY",(270) 316-6114,"1233 Castlewood Pl, Owensboro, KY 42303",https://www.google.com/maps/place/?q=place_id:ChIJf6uXf_K6b4gReZqY5rcnpHU&hl=en,none,none,none,none,none
1553,N,JC James Remodeling,"Point Pleasant, NJ",(732) 840-4456,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7UoUVnqEwYkRRthC_a-TnvM&hl=en,none,none,none,none,none
1554,N,"Magnum Remodeling, LLC","Dickinson, TX",(281) 960-0486,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdx6Jc_p9P4YR8gxVdGogG44&hl=en,none,none,none,none,none
1555,N,Broadway Custom Home Design,"Massapequa, NY",(516) 636-5260,"934 N Broadway, Massapequa, NY 11758",https://www.google.com/maps/place/?q=place_id:ChIJoZgvAprV6YkRb-c39iLpDAc&hl=en,none,none,none,none,none
1556,N,Platte Valley Refinishing LLC,"Columbus, NE",(402) 910-8221,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJKY56e2HrkIcRPR5tyPzhcLc&hl=en,none,none,none,none,none
1557,N,DUARTE'S CUSTOM CABINETS LLC.,"Kennedale, TX",(817) 818-0572,"847 Trent St Ste A, Kennedale, TX 76060",https://www.google.com/maps/place/?q=place_id:ChIJX4DlzBFlToYRFOU6vHrViw8&hl=en,none,none,none,none,none
1558,N,Bathroom Renovations Grand Prairie,"Grand Prairie, TX",(682) 337-4830,"5103 Magna Carta Blvd, Grand Prairie, TX 75052",https://www.google.com/maps/place/?q=place_id:ChIJtXtJAGKbskwRLKvWJMK3lic&hl=en,none,none,none,none,none
1559,N,Kropf Craft LLC,"Wickenburg, AZ",(928) 684-3014,"3500 N Sabin Brown Rd, Wickenburg, AZ 85390",https://www.google.com/maps/place/?q=place_id:ChIJo4WT_VtP04AR8k3Yu6SjIiI&hl=en,none,none,none,none,none
1560,N,George Wilson GWR&C Remodeling & Construction,"Sand Springs, OK",(918) 671-5733,"3206 Rawson Rd, Sand Springs, OK 74063",https://www.google.com/maps/place/?q=place_id:ChIJNyVxvVoGBSAR1QJP1F3WuG0&hl=en,none,none,none,none,none
1561,N,Prestige Bathroom Remodeling,"Rome, GA",(706) 374-9605,"3 Westridge Pl, Rome, GA 30165",https://www.google.com/maps/place/?q=place_id:ChIJUV2o0NmiiogRO-LZqqdyLQA&hl=en,none,none,none,none,none
1562,N,Ideal Kitchen & Bath,"Naples, FL",(239) 289-5000,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJwf9ULxUe24gRoHzeFde6x9s&hl=en,none,none,none,none,none
1563,N,"OnPar Home Improvements LLC | Kitchen & Bathroom , Residential Remodeling Service in Kingman, AZ","Kingman, AZ",(928) 716-6347,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJs11H7v_bzYARThWq-yJeVFY&hl=en,none,none,none,none,none
1564,N,North Star Custom Cabinets Inc,"Posen, IL",(708) 597-2099,"14825 McKinley Ave, Posen, IL 60469",https://www.google.com/maps/place/?q=place_id:ChIJq71SrjwjDogRelp2DjBTJoY&hl=en,none,none,none,none,none
1565,N,Kitchen and Floor Decor,"Woburn, MA",(617) 659-1449,"275 Salem St Ste 3, Woburn, MA 01801",https://www.google.com/maps/place/?q=place_id:ChIJkZmzez1144kRb700Ou22Z2M&hl=en,none,none,none,none,none
1566,N,Warrenton Custom Cabinets Llc,"Warrenton, VA",(540) 349-3227,"7347 Comfort Inn Dr, Warrenton, VA 20187",https://www.google.com/maps/place/?q=place_id:ChIJfcOx0uh8tokRt4nnBrNV-DQ&hl=en,none,none,none,none,none
1567,N,HTH Cabinets,"Odessa, TX",(432) 331-7583,"2932 N Torrance Ave, Odessa, TX 79764",https://www.google.com/maps/place/?q=place_id:ChIJCZNwIMi3-4YRBWLIBYIz0pw&hl=en,none,none,none,none,none
1568,N,Perfection Kitchen Bath Studio,"Boynton Beach, FL",(561) 770-4933,"3100 S Congress Ave Ste 2, Boynton Beach, FL 33426",https://www.google.com/maps/place/?q=place_id:ChIJ-0QoYB_f2IgRMtViYJNT35k&hl=en,none,none,none,none,none
1569,N,All Star Home Supply,"Taylor, MI",(313) 896-8747,"8914 Telegraph Rd, Taylor, MI 48180",https://www.google.com/maps/place/?q=place_id:ChIJIU1CpyxJO4gR8tRoVJl7qOE&hl=en,none,none,none,none,none
1570,N,Benavides Cabinet Shop,"Waxahachie, TX",(972) 935-9696,"1813 Howard Rd, Waxahachie, TX 75165",https://www.google.com/maps/place/?q=place_id:ChIJeUl15kjvToYRbe_5FQlxLjE&hl=en,none,none,none,none,none
1571,N,Mathews Fine Cabinetry,"Lufkin, TX",(936) 824-2469,"6094 US-69, Lufkin, TX 75901",https://www.google.com/maps/place/?q=place_id:ChIJ45rIV_U7OIYRCK4DVrCYXfY&hl=en,none,none,none,none,none
1572,N,Brandenberger Cabinets,"Easley, SC",(864) 650-3908,"4019 SC-86, Easley, SC 29642",https://www.google.com/maps/place/?q=place_id:ChIJ3xUxqbw4WIgR61Np7eRlcjI&hl=en,none,none,none,none,none
1573,N,Perma-Tex Resurfacing Inc,"Fraser, MI",(313) 640-8700,"34092 James J Pompo Dr, Fraser, MI 48026",https://www.google.com/maps/place/?q=place_id:ChIJmU5gPJLVJIgRuchnzfFexzk&hl=en,none,none,none,none,none
1574,N,H Garcia's Custom Cabinets LLC,"Fort Worth, TX",(817) 287-1159,"4230 Rendon Rd, Fort Worth, TX 76140",https://www.google.com/maps/place/?q=place_id:ChIJLQZ7A0llToYRDbmEFeCCTGg&hl=en,none,none,none,none,none
1575,N,Nixon Cabinet Co,"Athens, AL",(256) 232-5722,"17048 Blackburn Rd, Athens, AL 35611",https://www.google.com/maps/place/?q=place_id:ChIJ26eyJ12NYogRAI-hwPjgmZs&hl=en,none,none,none,none,none
1576,N,Granite Rocks,"East Chicago, IN",(219) 427-9855,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJfVmZuSLfEYgRJvtJeWeMO1Q&hl=en,none,none,none,none,none
1577,N,Construction 360 Services - kitchen & bath remodeling,"Cocoa, FL",(786) 501-0034,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ4akIC-NuRw0RAQ4BIA1Dreg&hl=en,none,none,none,none,none
1578,N,Zane's Handyman Services,"Ogden, UT",(385) 423-5352,"774 N Quincy Ave, Ogden, UT 84404",https://www.google.com/maps/place/?q=place_id:ChIJJ6U9V7MNU4cRKtdXWeTkX1Q&hl=en,none,none,none,none,none
1579,N,Enhanced Refacing/Remodeling Inc,"Freeport, IL",(833) 873-3223,"1791 S West Ave Ste A, Freeport, IL 61032",https://www.google.com/maps/place/?q=place_id:ChIJdZ6Z_gBrCIgRqQ1Q2CrDjms&hl=en,none,none,none,none,none
1580,N,Shoals Creek Home Improvements,"Florence, AL",(256) 702-3845,"457 Sky Park Rd, Florence, AL 35634",https://www.google.com/maps/place/?q=place_id:ChIJhz9Skjc3mq4R87fVIFSl8b8&hl=en,none,none,none,none,none
1581,N,Transformative Interiors LLC,"Berea, KY",(859) 539-9995,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJJeco14NkOmQRwZ3uAM5gatA&hl=en,none,none,none,none,none
1582,N,Ensign Tile,"Bountiful, UT",(801) 598-7432,"2924 S 175 E #5733, Bountiful, UT 84010",https://www.google.com/maps/place/?q=place_id:ChIJjR0sZcn3UocRtKNz5ivIl6g&hl=en,none,none,none,none,none
1583,N,Sauk Valley Granite,"Dixon, IL",(815) 677-6893,"650 Palmyra Rd, Dixon, IL 61021",https://www.google.com/maps/place/?q=place_id:ChIJD5cQ8DKsCYgRGjh9yMWFBUg&hl=en,none,none,none,none,none
1825,N,Arizone Refinishing LLC,"Casa Grande, AZ",(602) 831-9003,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ50aXTpa22W8Rn2xMIXaLnso&hl=en,none,none,none,none,none
1826,N,Nick's Home Repair & Remodeling,"Peachtree City, GA",(470) 399-0300,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJp9zjqQKkOWsRlEEs_WElUxw&hl=en,none,none,none,none,none
1827,N,Gibbs Home Remodeling,"Wichita Falls, TX",(940) 782-2486,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ1xKnjqw8U4YRslVc4IDhON0&hl=en,none,none,none,none,none
1828,N,Industry Cabinets,"Beaumont, CA",(951) 663-2424,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0b20vWXZZwwRqn_2lf3SFes&hl=en,none,none,none,none,none
1829,N,Santos Shower Remodeling,"Goldsboro, NC",(919) 432-7415,"808 Scott St, Goldsboro, NC 27534",https://www.google.com/maps/place/?q=place_id:ChIJFYW5Fa-rrokRNeKL_rfw_wI&hl=en,none,none,none,none,none
1830,N,"Kitchens and Baths by Design, LLC","Pearl, MS",(769) 233-1511,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbRmUx4bMzUURWDQjxRJV0LQ&hl=en,none,none,none,none,none
1831,N,Paradise Kitchens and Floors LLC,"Frostburg, MD",(301) 687-1001,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzTIrhCqXyokRIX6pVVTM4XA&hl=en,none,none,none,none,none
1832,N,Custom Surface Solutions Inc.,"League City, TX",(281) 338-1445,"190B2, Gulf Fwy, League City, TX 77573",https://www.google.com/maps/place/?q=place_id:ChIJAQAAANCCQIYRn25aY4hObzY&hl=en,none,none,none,none,none
```
