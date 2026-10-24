# Round 2: Gemini task 3, part 21 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 368, reply in that chat "Continue with the businesses
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
323,N,Mass Remodeling,"Foxborough, MA",(774) 219-7880,"Pratt St, Mansfield, MA 02048",https://www.google.com/maps/place/?q=place_id:ChIJIcFeh19j5IkROxDQhWt7z1A&hl=en,none,none,none,none,none
366,N,Springbok Remodeling,"Alpine, TX",(830) 446-0095,"Blue Ridge, Comfort, TX 78013",https://www.google.com/maps/place/?q=place_id:ChIJs4WIHex-LW4RA2Sc_8DmGq8&hl=en,none,none,none,none,none
400,N,DLA SERVICES REPAIR AND REMODELING,"Romulus, MI",(248) 270-5066,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVd7Bh56WqkcRzzXrpWImL2U&hl=en,none,none,none,none,none
437,N,Cornerstone Remodeling,"Cypress, CA",(800) 998-8983,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJDc-LTIHB4AcRTOMpoGcs8ZE&hl=en,none,none,none,none,none
467,N,Pablo's Remodeling & Painting LLC,"Beaumont, TX",(409) 223-8970,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ10FYAFE1S68RikIajuSr_eY&hl=en,none,none,none,none,none
545,N,Almonte Home improvement Contractor,"Whitehall, OH",(614) 933-1995,"6107 McNaughten Ctr, Columbus, OH 43232",https://www.google.com/maps/place/?q=place_id:ChIJPWeQAZVjOIgRTOs2cTttYQg&hl=en,none,none,none,none,none
555,N,Priority Home Works,"Newport News, VA",,"607 Industrial Park Dr Ste FF, Newport News, VA 23608",https://www.google.com/maps/place/?q=place_id:ChIJY7rekiN9sIkRoAcm5W1lkSc&hl=en,none,none,none,none,none
10,N,Big Sky Bathroom & Kitchen,"Laurel, MT",(406) 964-5116,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7zh40fjfXEURPv023DT0hPw&hl=en,none,none,none,none,none
30,N,Montco Handyman,"Norristown, PA",(484) 534-7851,"1529 Pine St, Norristown, PA 19401",https://www.google.com/maps/place/?q=place_id:ChIJnf84z969xokRR9-phgkdaJI&hl=en,none,none,none,none,none
59,N,BAB Construction LLC,"Aurora, CO",(720) 687-7651,"12870 E Idaho Dr, Aurora, CO 80012",https://www.google.com/maps/place/?q=place_id:ChIJaccjaOB9bIcR4XlSnalF97Y&hl=en,none,none,none,none,none
82,N,ILIRIA REMODELING,"Tinley Park, IL",(708) 673-1671,"Courtyards of 78th Avenue Shopping Center, W 159th St, Tinley Park, IL 60477",https://www.google.com/maps/place/?q=place_id:ChIJTTGPgThExgYRWbCiMugmsiU&hl=en,none,none,none,none,none
127,N,NB Bath & Remodeling,"Washington, IL",(309) 370-6017,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvbKaHchTCogREEO8y518aEI&hl=en,none,none,none,none,none
162,N,CTG TILE & HANDYMAN,"Villa Rica, GA",(404) 904-2834,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJExARAF7FoacRMbGEZxA7ydg&hl=en,none,none,none,none,none
207,N,Zaprala Romano Remodeling,"Gloucester City, NJ",(856) 981-7569,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv1NYTBvSxokRsh-IRDcNwlg&hl=en,none,none,none,none,none
213,N,Capitol Countertops,"Pearl, MS",(601) 664-2008,"129 Paul Truitt Ln, Pearl, MS 39208",https://www.google.com/maps/place/?q=place_id:ChIJNcQd6DgsKIYRiApHX66nMU4&hl=en,none,none,none,none,none
246,N,Creative Construction Services Inc,"Santa Maria, CA",(805) 694-6525,"240 S Broadway, Orcutt, CA 93455",https://www.google.com/maps/place/?q=place_id:ChIJA8Dj5Ftt7IARemzvFOtrw9s&hl=en,none,none,none,none,none
351,N,Patton Family Remodeling llc,"Festus, MO",(314) 620-5172,"308 10th St, Crystal City, MO 63019",https://www.google.com/maps/place/?q=place_id:ChIJn7LNRoHv2IcRlOTNNyU-weU&hl=en,none,none,none,none,none
468,N,Red Remodeling LLC,"Topeka, KS",(785) 506-5731,"2065 SW Lane St, Topeka, KS 66604",https://www.google.com/maps/place/?q=place_id:ChIJv_7hU-LyXK8RV_nIoA28a0g&hl=en,none,none,none,none,none
524,N,CT Remodeling,"Ellington, CT",(860) 200-7135,"27 Folkstone Rd Apt C, Broad Brook, CT 06016",https://www.google.com/maps/place/?q=place_id:ChIJF479TdOMOCsR-h-9mTsvh9o&hl=en,none,none,none,none,none
568,N,Marble & Granite Guys,"Smithfield, NC",(919) 441-3219,"3295 US-70 BUS, Smithfield, NC 27577",https://www.google.com/maps/place/?q=place_id:ChIJsVUqMGQRrIkR6cBm2myuCjk&hl=en,none,none,none,none,none
6,N,Maverick Remodeling,"University Park, TX",(214) 736-4210,"5730 Anita St, Dallas, TX 75206",https://www.google.com/maps/place/?q=place_id:ChIJV6tLG2mfToYReOUQO8ofojA&hl=en,none,none,none,none,none
11,N,Innerstone Marble & Granite LLC,"Brookings, OR",(541) 469-3906,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ09bM_zeg2lQRPQLLpUYopFo&hl=en,none,none,none,none,none
16,N,Elizabeth Kitchen & Granite LLC,"Elizabeth, NJ",(908) 662-9512,"719 Livingston St, Elizabeth, NJ 07201",https://www.google.com/maps/place/?q=place_id:ChIJe0AJP3lNwokRwXb3AJOuG6g&hl=en,none,none,none,none,none
51,N,T. C. Rich,"North Augusta, SC",(706) 231-1589,"1450 Georgia Ave Ste 6564, North Augusta, SC 29861",https://www.google.com/maps/place/?q=place_id:ChIJEYiutsXN-YgRiqNrYwfSfjo&hl=en,none,none,none,none,none
108,N,J&C Tile & Marble Renovation LLC,"West New York, NJ",(201) 667-9311,"6619 Bergenline Ave, West New York, NJ 07093",https://www.google.com/maps/place/?q=place_id:ChIJwymjcnFZwokR70BVycWm64M&hl=en,none,none,none,none,none
120,N,Jireh Remodeling,"Sanford, NC",(919) 895-0275,"322 Oakwood Ave, Sanford, NC 27330",https://www.google.com/maps/place/?q=place_id:ChIJ0RQb7WGnrIkRHUQedRjCpjk&hl=en,none,none,none,none,none
133,N,Hoosier Custom Cabinet Designs,"Mount Dora, FL",(352) 385-0000,"880 Bay Rd Unit B4, Mt Dora, FL 32757",https://www.google.com/maps/place/?q=place_id:ChIJ8WAtJLKi54gR5g8Me7W9EZo&hl=en,none,none,none,none,none
150,N,Prime Atlanta Renovations,"Duluth, GA",(770) 823-6474,"3843 Howell Springs Dr, Duluth, GA 30096",https://www.google.com/maps/place/?q=place_id:ChIJNSCkKIaj9YgRnP5U40jOP0I&hl=en,none,none,none,none,none
163,N,S&A Excellence Bathroom Remodeling,"Laguna Woods, CA",(657) 236-3301,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJkaUSsPdCOmYRPINKFxtDyn4&hl=en,none,none,none,none,none
202,N,A.C.E Carpentry,"Bridgewater, VA",(540) 699-3098,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXWc4RC-_tIkRmdthhelSsNk&hl=en,none,none,none,none,none
261,N,Dna remodels llc,"Titusville, FL",(321) 557-0469,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqQJDZwMVjQYRtAvKmbFOoZI&hl=en,none,none,none,none,none
309,N,B&M Contractors,"The Colony, TX",(469) 826-3636,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZzmkEjAlTIYRBiXnpEKeGsw&hl=en,none,none,none,none,none
358,N,Giovannis Design and Install Group,"Kenilworth, NJ",(908) 244-4259,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJo5nbmJKtw4kRqAAelBvgOv0&hl=en,none,none,none,none,none
459,N,Luxury Remodeling LLC,"Falls Church, VA",(571) 505-9854,"2922 Willston Pl, Falls Church, VA 22044",https://www.google.com/maps/place/?q=place_id:ChIJ-aBZwh21t4kRdB9BPtH93ck&hl=en,none,none,none,none,none
561,N,E &O LLC,"Olathe, KS",(913) 444-0232,"13505 S Mur-Len Rd Ste 105 #145, Olathe, KS 66062",https://www.google.com/maps/place/?q=place_id:ChIJfyNBCnK_wIcRYuR0wKQ8TzE&hl=en,none,none,none,none,none
36,N,Dynasty Home Improvement LLC,"Montville, CT",(860) 710-4602,"7A Windham Ave, Colchester, CT 06415",https://www.google.com/maps/place/?q=place_id:ChIJD2cHR6pp5okRI-_s7du6UpA&hl=en,none,none,none,none,none
54,N,Stone Koat Kreations LLC Epoxy Countertops & Floors,"Zachary, LA",(225) 453-2353,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXaHPeA-bJoYRaXooXaGqSOw&hl=en,none,none,none,none,none
74,N,Better Looks Home Renovations,"Coconut Creek, FL",(561) 662-9099,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJm5IOaH_S1CkRq2JTb1DjLX0&hl=en,none,none,none,none,none
157,N,All Pro Basements,"Dardenne Prairie, MO",(636) 281-6045,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJRSGSYiDQ3ocRPxeMtycNUpE&hl=en,none,none,none,none,none
172,N,"Simko Tile & Bath, LLC","Macon, GA",(912) 266-1433,"911 Matthews Dr, Macon, GA 31210",https://www.google.com/maps/place/?q=place_id:ChIJCxzx1GYn5YgRgkTe5GpM7qE&hl=en,none,none,none,none,none
206,N,A1 Granite & Quartz Inc.,"Wallington, NJ",(973) 815-1170,"34 Midland Ave #1723, Wallington, NJ 07057",https://www.google.com/maps/place/?q=place_id:ChIJT6QRpjz5wokROhFlw8o_iFw&hl=en,none,none,none,none,none
237,N,Carlson Property Solutions LLC,"Johnstown, CO",,"3751 Summerwood Way, Johnstown, CO 80534",https://www.google.com/maps/place/?q=place_id:ChIJ_____09JaYcRmP2WFvFdPIw&hl=en,none,none,none,none,none
240,N,Centex Bath,"Round Rock, TX",(512) 592-1203,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJMb1U5afTRIYRN5dBWSKynuQ&hl=en,none,none,none,none,none
251,N,Do All Glaze and Remodel,"Flat Rock, MI",(734) 934-0010,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJtz2Ho4Y_O4gRmwBdnQyRVeI&hl=en,none,none,none,none,none
256,N,"Essential Home Renovation, Llc","Council Bluffs, IA",(402) 301-7142,"Council Bluffs, IA 51502",https://www.google.com/maps/place/?q=place_id:ChIJ3XUc9miFk4cRj1Csrs_th8Y&hl=en,none,none,none,none,none
264,N,Northshore Custom Tile and Flooring Inc.,"Covington, LA",(985) 317-9847,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxwO_XoxdJ4YRdWvbEMmNmo8&hl=en,none,none,none,none,none
268,N,LCR Home Solutions LLC,"Lochbuie, CO",(720) 350-1984,"579 Jewel St, Lochbuie, CO 80603",https://www.google.com/maps/place/?q=place_id:ChIJxch48Z-3gYERtOwPsQyA72A&hl=en,none,none,none,none,none
317,N,Masters Kitchen and Flooring,"Nicholasville, KY",(859) 813-0727,"2420 Vince Rd, Nicholasville, KY 40356",https://www.google.com/maps/place/?q=place_id:ChIJMwLeaZFfQogR8BO23Z6F1VM&hl=en,none,none,none,none,none
329,N,Titan Repair LLC,"Billings, MT",(406) 690-0987,"2515 Poly Dr, Billings, MT 59102",https://www.google.com/maps/place/?q=place_id:ChIJny8Poox8SFMRrIi_Vw3LB5Y&hl=en,none,none,none,none,none
368,N,"Christians Remodeling, LLC","Jeffersonville, IN",(502) 434-0521,"Avondale Ct, Jeffersonville, IN 47130",https://www.google.com/maps/place/?q=place_id:ChIJz32sMM2qY4YRvI47jhUC_E0&hl=en,none,none,none,none,none
```
