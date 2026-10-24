# Round 2: Gemini task 4 (33 new businesses from the last Maps discovery round)

## What to do
Same as the task 3 parts: a NEW Gemini chat, **Deep Research**, upload this file, send "Do the task in this file.",
click **Start research**, and send me the report with the others. If it ends with `LAST_ROW_DONE` before row
3033, reply "Continue with the businesses after LAST_ROW_DONE, same rules, same columns".

## The task (Gemini: follow this exactly)
```
You are doing a research task on 33 small kitchen and bathroom remodeling businesses in the United States. Each one
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

## Businesses (33, in order)
```csv
row,task,business_name,town,phone,address,google_maps,known_facebook,known_instagram,known_email,known_owner,dead_website
3001,N,Meyer Remodeling LLC,"Hayward, WI",(715) 530-4551,"W Park Rd, Hayward, WI 54843",https://www.google.com/maps/place/?q=place_id:ChIJ77_DMHQmm6ARy0HnRCS1njo&hl=en,http://www.facebook.com/meyerremodelingllc,none,none,none,none
3002,N,Zack The Tub Guy,"Lapeer, MI",(810) 895-1142,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJt_TgpM2vZq8RXSU0F0cbdhQ&hl=en,https://www.facebook.com/ZackTheTubGuy,none,none,none,none
3003,N,Holmseth Construction,"Waseca, MN",(507) 722-9142,"805 8th Ave NW, Waseca, MN 56093",https://www.google.com/maps/place/?q=place_id:ChIJJcWGMMoH9IcRLJoYMQ1my9g&hl=en,http://www.facebook.com/holmsethconstruction,none,none,none,none
3004,N,Mississippi Wood,"Pontotoc, MS",(662) 308-1894,"13 W Reynolds St, Pontotoc, MS 38863",https://www.google.com/maps/place/?q=place_id:ChIJL6eyEfe7gIgRQl4D4XPrpVM&hl=en,https://www.facebook.com/p/Mississippi-Wood-61559275435527/,none,none,none,none
3005,N,Robinson Tile and Stone,"Semmes, AL",(251) 447-1838,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJY1Rkuqyvm4gRDJB4yX0lKCs&hl=en,https://www.facebook.com/RTNScustom,none,none,none,none
3006,N,Flooring & Tile Designs LLC,"Dundee, FL",(863) 399-2157,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJaQqvcNvmraARNbBwCbuCFkg&hl=en,none,none,none,none,none
3007,N,Brute Force Remodeling LLC,"Philadelphia, PA",(267) 582-5601,"238 E Durham St apt a, Philadelphia, PA 19150",https://www.google.com/maps/place/?q=place_id:ChIJU42kJQm5xokRW3LBSkd8fuU&hl=en,none,none,none,none,none
3008,N,"Tom Mowrey Home Werks, LLC","Northumberland, PA",(570) 809-2769,"370 King St, Northumberland, PA 17857",https://www.google.com/maps/place/?q=place_id:ChIJU4o7g5Rrz4kRNl_9AtPjQNA&hl=en,none,none,none,none,none
3009,N,NashTile llc,"Ashland City, TN",(615) 947-7952,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_7umkDQ50wYRdGpHzitn6uQ&hl=en,none,none,none,none,none
3010,N,Bowyers Kitchen Center,"East Liverpool, OH",(330) 385-2808,"15446 E Liverpool Rd, East Liverpool, OH 43920",https://www.google.com/maps/place/?q=place_id:ChIJCR56FeoQNIgRW8kKyQ7u2kc&hl=en,none,none,none,none,none
3011,N,Locust Granite & Tile,"Locust, NC",(704) 888-4531,"401 Lion Club Dr, Locust, NC 28097",https://www.google.com/maps/place/?q=place_id:ChIJmQ6VR3trVIgRYsCnpmXUob8&hl=en,none,none,none,none,none
3012,N,Bashore Custom Counters,"Lapeer, MI",(810) 664-0301,"1277 Roods Lake Rd #8366, Lapeer, MI 48446",https://www.google.com/maps/place/?q=place_id:ChIJ-zlLcDlnJIgRY7RKgyuT6Yo&hl=en,none,none,none,none,none
3013,N,Wall2Wall Remodeling,"Hartville, OH",(330) 388-8485,"1043 Cayuga Trail SW, Hartville, OH 44632",https://www.google.com/maps/place/?q=place_id:ChIJbReGWO7usaERAlGhqrCraH0&hl=en,none,none,none,none,none
3014,N,Mccurry Cabinets Inc.,"Jackson, GA",(678) 618-6032,"North, 1518 GA-42, Jackson, GA 30233",https://www.google.com/maps/place/?q=place_id:ChIJ92J54rdB9IgR-dAWxLPf2vE&hl=en,none,none,none,none,none
3015,N,Wachswoods Inc,"Oak Grove, MO",(816) 690-3631,"200 S Broadway Ste B, Oak Grove, MO 64075",https://www.google.com/maps/place/?q=place_id:ChIJcQYvfZMTwYcRm5v_DlKi4KA&hl=en,none,none,none,none,none
3016,N,CreekSide Remodeling LLC,"Milton, PA",(570) 284-7625,"515 State Rd, Milton, PA 17847",https://www.google.com/maps/place/?q=place_id:ChIJsVxwKDtlz4kRD16ohltboPA&hl=en,none,none,none,none,none
3017,N,Shattuck Remodeling & Home Repair,"North Syracuse, NY",(315) 391-8252,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzZnBUYXz2YkRZaO3LVf4AfE&hl=en,none,none,none,none,none
3018,N,Afh properties LLC,"Mocksville, NC",(336) 331-2774,"2212 NC-801, Mocksville, NC 27028",https://www.google.com/maps/place/?q=place_id:ChIJpVMntCG_U4gRZyH4GW2uAIY&hl=en,none,none,none,none,none
3019,N,AllState 1 Day Baths,"Fruitland, MD",(443) 233-0232,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTw3YpQqD_kQRJympW5TvV4g&hl=en,none,none,none,none,none
3020,N,Charlotte Cabinets Inc,"Charlotte, MI",(517) 543-1522,"629 W Seminary St, Charlotte, MI 48813",https://www.google.com/maps/place/?q=place_id:ChIJTXJM4ySvIogRBkMHuF5QRcs&hl=en,none,none,none,none,none
3021,N,ORLANDO'S GRANITE LLC,"Ranson, WV",(301) 305-3701,"Oak Lee Dr, Ranson, WV 25438",https://www.google.com/maps/place/?q=place_id:ChIJ_8ACkPZRomcRa5puSq_xXis&hl=en,none,none,none,none,none
3022,N,McHugh Partners LLC -- Custom Tile Contracting -- Vinyl Flooring,"Summit Hill, PA",(570) 225-6684,"112 E Fell St, Summit Hill, PA 18250",https://www.google.com/maps/place/?q=place_id:ChIJuy29oX2xxYkRv-mVvQgdIcY&hl=en,none,none,none,none,none
3023,N,Pippen Construction LLC,"Dayton, OH",(937) 856-6284,"3124 Shroyer Rd, Dayton, OH 45429",https://www.google.com/maps/place/?q=place_id:ChIJbWj-znOFQIgR9s1DBlzsUz0&hl=en,none,none,none,none,none
3024,N,JGL Remodeling LLC,"Warrenton, MO",(636) 297-5463,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJew2Qs8fQ3ocRC1IHB4akC7c&hl=en,none,none,none,none,none
3025,N,Alberts Custom Woodworks Inc,"Grand Forks, ND",(701) 772-0845,"1725 Dyke Ave, Grand Forks, ND 58203",https://www.google.com/maps/place/?q=place_id:ChIJJ8vUdjSBxlIRwjITfNIeq5s&hl=en,none,none,none,none,none
3026,N,Creative Cabinet Works,"Starke, FL",(904) 964-5711,"140 S Thompson St, Starke, FL 32091",https://www.google.com/maps/place/?q=place_id:ChIJG53-Vur95YgRgU1t3gku69Y&hl=en,none,none,none,none,none
3027,N,Best View Cabinets Installation LLC,"Flagler Beach, FL",(386) 283-7392,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJW2iQPO28oKkRCUwy5IREGtY&hl=en,none,none,none,none,none
3028,N,Greer & Phillips LLC,"Syracuse, NY",(315) 552-7252,"7343 Thompson Rd, Syracuse, NY 13212",https://www.google.com/maps/place/?q=place_id:ChIJlZStmOLt2YkRPiY9nj1Df8g&hl=en,none,none,none,none,none
3029,N,Dave's Cabinets,"Rockwood, TN",(865) 354-1644,"639 N Gateway Ave, Rockwood, TN 37854",https://www.google.com/maps/place/?q=place_id:ChIJE2neb0XhXYgRbdB9gODZ7FI&hl=en,none,none,none,none,none
3030,N,Ziegler Kitchens & Baths,"Okeechobee, FL",(863) 261-4444,"106 NW 36th St, Okeechobee, FL 34972",https://www.google.com/maps/place/?q=place_id:ChIJl6GW50gh3IgR-SUkyrTkR1o&hl=en,none,none,none,none,none
3031,N,Maas Tile Designs,"Shawano, WI",(715) 851-6151,"944 S Waukechon St, Shawano, WI 54166",https://www.google.com/maps/place/?q=place_id:ChIJZeE0K7YRAogR6i6rgZfx95A&hl=en,none,none,none,none,none
3032,N,The Little Remodeling Company LLC.,"Spring Valley, MN",(507) 202-0861,"100 N Section Ave, Spring Valley, MN 55975",https://www.google.com/maps/place/?q=place_id:ChIJxZLdqa0G-ocRgI3LvsvpD2s&hl=en,none,none,none,none,none
3033,N,4th Street Kitchen Studio,"Peru, IL",(815) 200-2546,"2000 4th St, Peru, IL 61354",https://www.google.com/maps/place/?q=place_id:ChIJnWKGTf1gCYgRO46nnGUsq0w&hl=en,none,none,none,none,none
```
