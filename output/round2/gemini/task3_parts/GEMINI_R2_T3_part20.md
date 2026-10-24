# Round 2: Gemini task 3, part 20 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 259, reply in that chat "Continue with the businesses
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
2260,N,"H&A Remodeler | Home, Deck & Kitchen Remodeling Quail Ridge","Boise, ID",(208) 508-1526,"3835 N Woody Ln, Boise, ID 83703",https://www.google.com/maps/place/?q=place_id:ChIJO-77_Qr_rlQRo4VqF2LMA3I&hl=en,none,none,none,none,none
2261,N,MT-Bath.INC,"Morton Grove, IL",(224) 715-2854,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJoexOsYetZUMRcduzxXGwzkk&hl=en,none,none,none,none,none
2262,N,Bulldog Renovations and Solutions LLC,"Pittsford, NY",(585) 416-8720,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ367EH6Zk0KER6sFpNdzkJig&hl=en,none,none,none,none,none
2263,N,Vanderhoof Custom Cabinets,"Verona, NY",(315) 336-3015,"5317 Old Oneida Rd, Verona, NY 13478",https://www.google.com/maps/place/?q=place_id:ChIJqfcYPa9y2YkR2dqzIh0vlK8&hl=en,none,none,none,none,none
2264,N,Silver Pine Kitchen Remodeler La Mirada,"La Mirada, CA",(562) 574-2954,"15290 Rosecrans Ave, La Mirada, CA 90638",https://www.google.com/maps/place/?q=place_id:ChIJJeYljeAr3YARehYU0Gm-w40&hl=en,none,none,none,none,none
2265,N,King Custom Cabinets,"Yuba City, CA",(530) 845-2614,"367 Burns Dr #3, Yuba City, CA 95991",https://www.google.com/maps/place/?q=place_id:ChIJZerDpttSm4ARfpUDGFr3kR4&hl=en,none,none,none,none,none
2266,N,RPD Construction LLC - Home Improvement Contractor,"Norwich, CT",(860) 884-5921,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgath3bbFyKYRt56K2K5k0G4&hl=en,none,none,none,none,none
2267,N,Fast Pro Kitchen,"Chelsea, MA",(781) 885-5776,"22B Willow St, Chelsea, MA 02150",https://www.google.com/maps/place/?q=place_id:ChIJKQSuPuNx44kRqX-BQoCUMAI&hl=en,none,none,none,none,none
2268,N,C&C Quality Home Improvement - Home Renovation Companies Port Chester NY,"Port Chester, NY",(914) 580-4336,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMVBS916XwokRrjwXqIofCIc&hl=en,none,none,none,none,none
2269,N,Pelaez Renovations LLC,"Leland, NC",(910) 612-0324,"2417 Palisade Ct, Leland, NC 28451",https://www.google.com/maps/place/?q=place_id:ChIJu7P-XeYZqokRHHC35h_ODw4&hl=en,none,none,none,none,none
2270,N,Superior Home Remodeling,"Morrisville, PA",(609) 310-9260,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJS9IIbYNeb4QRM1ue2tOuUDk&hl=en,none,none,none,none,none
2271,N,Reliable Home Remodeling & Repair,"Gun Barrel City, TX",(430) 207-0365,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDawuIKF2-ggRu8RKSdqyQZA&hl=en,none,none,none,none,none
2272,N,Kitchen World Inc.,"Ponte Vedra Beach, FL",(844) 579-0905,"244 Pablo Rd, Ponte Vedra Beach, FL 32082",https://www.google.com/maps/place/?q=place_id:ChIJuYN8cjc35IgRQi7qdabbqe8&hl=en,none,none,none,none,none
2273,N,Tennessee Craftsmen,"Franklin, TN",(615) 294-2544,"114 Blue Grass Dr, Franklin, TN 37064",https://www.google.com/maps/place/?q=place_id:ChIJm1Ux11J_ZIgRsP8vdHToSwo&hl=en,none,none,none,none,none
2274,N,Higley Cabinets LLC.,"Heyburn, ID",(208) 679-4630,"2800 Nevada St, Heyburn, ID 83336",https://www.google.com/maps/place/?q=place_id:ChIJPXf46-I2q1QR0IQKuTnNMRw&hl=en,none,none,none,none,none
2275,N,Donovan Design & Build Inc,"South Bend, IN",(574) 291-9222,"19641 Lucinda St, South Bend, IN 46614",https://www.google.com/maps/place/?q=place_id:ChIJTwzD7gvMFogRt_nLNO_K3z0&hl=en,none,none,none,none,none
2276,N,Aguilar Remodeling,"South Houston, TX",(832) 933-2852,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHfMGC9x19wURJMkb_caQiRo&hl=en,none,none,none,none,none
2277,N,SOUTHERN RUSTIC,"Pineville, LA",(318) 277-0808,"1203 Pearce Rd, Pineville, LA 71360",https://www.google.com/maps/place/?q=place_id:ChIJNdxv2Z5LJYYRne2o25bhsbg&hl=en,none,none,none,none,none
2278,N,Olymp construction,"Bellevue, WA",(425) 410-0023,"15248 SE 39th St, Bellevue, WA 98006",https://www.google.com/maps/place/?q=place_id:ChIJ_Vh5bVswUY0Rysv1X63mHB8&hl=en,none,none,none,none,none
2279,N,AD Golden Renovation LLC,"Harrisburg, NC",(704) 421-5480,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJUwyhBAAZVIgRe5Qmu9zJ5M0&hl=en,none,none,none,none,none
2280,N,Signature cabinet company,"Brainerd, MN",(218) 513-9025,"17043 Commercial Park Rd, Brainerd, MN 56401",https://www.google.com/maps/place/?q=place_id:ChIJPczGKvq5tlIRBOpli-mwZEc&hl=en,none,none,none,none,none
2281,N,Spence Construction LLC,"Runnemede, NJ",(856) 292-5327,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJj_5ry__F5yURATf09hyKyc4&hl=en,none,none,none,none,none
2282,N,Bazh Re-construction,"Mansfield, TX",(817) 841-2047,"211 Hillcrest St, Mansfield, TX 76063",https://www.google.com/maps/place/?q=place_id:ChIJ0X3FRRRhToYRV5K_aB_69Tk&hl=en,none,none,none,none,none
2283,N,California Granite & Natural Stone Inc,"Guadalupe, CA",(805) 343-7783,"190 Guadalupe St, Guadalupe, CA 93434",https://www.google.com/maps/place/?q=place_id:ChIJYaVpzCxC7IARGs3HPr7uA_w&hl=en,none,none,none,none,none
106,N,Myers Construction Services,"Zanesville, OH",(740) 607-4184,"6145 Rollins Dr, Nashport, OH 43830",https://www.google.com/maps/place/?q=place_id:ChIJbUHxvHHzN4gRXc9diTx7kAQ&hl=en,none,none,none,none,none
114,N,Tubs & Tops,"Longview, TX",(903) 235-2422,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJf3R5RKM-NoYRzEoqRfyvYyY&hl=en,none,none,none,none,none
131,N,Welch Renovations,"Phenix City, AL",(706) 577-0115,"1511 Melanie Ln, Phenix City, AL 36867",https://www.google.com/maps/place/?q=place_id:ChIJ1Qmz2i7NjIgR5emMlPRCfsQ&hl=en,none,none,none,none,none
146,N,Stone by AJ,"Maumelle, AR",(501) 794-8382,"9211 Maumelle Blvd, North Little Rock, AR 72113",https://www.google.com/maps/place/?q=place_id:ChIJZae0Yomj0ocRwyOfOnW4rHc&hl=en,none,none,none,none,none
170,N,Nu-Shine Kitchen and Bathroom Refinishing,"Brooksville, FL",(727) 319-8332,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJJXN6YxP7wogRQR7VJWunwnU&hl=en,none,none,none,none,none
176,N,Operation Renovation LLC,"Massillon, OH",(330) 879-8124,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJfXr4dg8mN4gRYtXVWv93sks&hl=en,none,none,none,none,none
177,N,Good Choice Works LLC,"Ramsey, MN",(763) 219-2150,"5631 164th Ln NW, Ramsey, MN 55303",https://www.google.com/maps/place/?q=place_id:ChIJzSX9U6kVs1IRfbT_sG1WOTE&hl=en,none,none,none,none,none
295,N,Reliable Remodels,"Unalaska, AK",(907) 632-1029,"9701 Elmore Rd, Anchorage, AK 99507",https://www.google.com/maps/place/?q=place_id:ChIJp8xwoo6XyFYRjqsW56zIlqU&hl=en,none,none,none,none,none
306,N,Morris Finishing Company LLC,"Wytheville, VA",(540) 674-0079,"549 E Main St, Dublin, VA 24084",https://www.google.com/maps/place/?q=place_id:ChIJeambtNbkTYgRSlJ7CU3rEOE&hl=en,none,none,none,none,none
316,N,Builders Direct,"Hazleton, PA",(570) 501-1133,"757 W Broad St, Hazleton, PA 18201",https://www.google.com/maps/place/?q=place_id:ChIJ-c9sD3SkxYkR5sbrh7GsFrY&hl=en,none,none,none,none,none
325,N,Arnold Improvements LLC,"Ellington, CT",(860) 872-6226,"8 Faith Dr, Vernon, CT 06066",https://www.google.com/maps/place/?q=place_id:ChIJxan55Qr35okRncfsf59apYI&hl=en,none,none,none,none,none
355,N,Creative Tile and Remodeling LLC,"Gladstone, MO",(816) 337-2374,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQVGpdo75wIcRTnwma3-AUk8&hl=en,none,none,none,none,none
434,N,Complete Home Remodeling LLC,"Springfield, MO",(417) 761-0675,"227 E Sunshine St Suite 105, Springfield, MO 65807",https://www.google.com/maps/place/?q=place_id:ChIJ8T9mNOdjz4cR33V_FRqHyag&hl=en,none,none,none,none,none
453,N,Tile co,"Lebanon, OH",(937) 407-5833,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJS5834oyoC0QRVcvn5n2AfXk&hl=en,none,none,none,none,none
497,N,SnR Remodeling Services LLC,"Kennesaw, GA",(770) 880-8981,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJN7NUUIOJx64RtqJaZKJ5xkk&hl=en,none,none,none,none,none
507,N,Stone Creations and Cabinetry,"Revere, MA",(617) 390-2110,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0f_udiFx44kRHzdKdTSAQV0&hl=en,none,none,none,none,none
558,N,Clancy's Custom Cabinets & More,"Seguin, TX",(210) 870-8735,"171 Indian Trail, Seguin, TX 78155",https://www.google.com/maps/place/?q=place_id:ChIJo7lcJrXHXIYRoqZGgMINYT8&hl=en,none,none,none,none,none
564,N,D'ANGELS HOME REMODELING,"Streamwood, IL",(847) 807-5014,"5 S Victoria Ln, Streamwood, IL 60107",https://www.google.com/maps/place/?q=place_id:ChIJpxgszCmoD4gR1zdErTL2xSk&hl=en,none,none,none,none,none
12,N,"Fit & Finish HPS,LLC","Jupiter, FL",(561) 888-3381,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ1dgYmjOaNUsRDng7_2Flf2M&hl=en,none,none,none,none,none
47,N,ERC Renovation LLC,"Braselton, GA",(866) 254-0162,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJs51CkSuKn68RmlyNmUECS9c&hl=en,none,none,none,none,none
141,N,Ramos Home Renovations,"Balch Springs, TX",(972) 891-4259,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJR2SaX6eXqwQR-3rZaw067aU&hl=en,none,none,none,none,none
145,N,Atlas Tile Co,"Vineyard, UT",(714) 350-5904,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ5912k1l0BE4Ri50GptGo3W4&hl=en,none,none,none,none,none
171,N,Matrix Bathroom Systems,"Portage, MI",(269) 575-0079,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJX4EPvDF1F4gR815t4_WbdHg&hl=en,none,none,none,none,none
203,N,Emerald Remodeling llc.,"Buena Vista, VA",(571) 518-8026,"7367 Cluster House Way, Gainesville, VA 20155",https://www.google.com/maps/place/?q=place_id:ChIJHz0t9g1ntokRfyNu9c79XSE&hl=en,none,none,none,none,none
247,N,Mr MrHandyDandy Bathroom Renovations,"Hampton, GA",,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbdEpAW_19IgR5avZ8xL_uuA&hl=en,none,none,none,none,none
259,N,Lk Kitchen,"Dunellen, NJ",(929) 374-9031,"118 N Washington Ave, Dunellen, NJ 08812",https://www.google.com/maps/place/?q=place_id:ChIJS4ndqOe5w4kRNaRjXkt-yTs&hl=en,none,none,none,none,none
```
