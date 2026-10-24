# Round 2: Gemini task 3, part 19 of 22 (50 businesses: 50 N)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 2259, reply in that chat "Continue with the businesses
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
2167,N,"C H Home Improvements, Inc.","Ankeny, IA",(515) 865-8929,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJuyQNEmL-RG8RopSubgQAENI&hl=en,none,none,none,none,none
2168,N,Hcs Kitchen And Bath,"Memphis, TN",(901) 384-8755,"7560 A E Beaty Dr, Memphis, TN 38133",https://www.google.com/maps/place/?q=place_id:ChIJVVVltYOdf4gRW0xZ9YPCudI&hl=en,none,none,none,none,none
2169,N,Cbuildinteriors,"Kingston, NY",(845) 594-7773,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJy4s13YzVdo0RIdEnJ1m0qWs&hl=en,none,none,none,none,none
2170,N,Home Remodelers in Dallas,"Plano, TX",(469) 210-1139,"5830 Granite Pkwy #100-346, Plano, TX 75024",https://www.google.com/maps/place/?q=place_id:ChIJe4DZ0R_v_IkRz4tlHbE8GYs&hl=en,none,none,none,none,none
2171,N,Calancea home building,"Ypsilanti, MI",(734) 260-6489,"10382 Martz Rd, Ypsilanti, MI 48197",https://www.google.com/maps/place/?q=place_id:ChIJO7etQFFZO4gRUKh2yFxgesE&hl=en,none,none,none,none,none
2172,N,Chicago Builders & Remodeling Team,"Addison, IL",(331) 215-8779,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJE-3NIOCtD4gRgjR0I_NUbGI&hl=en,none,none,none,none,none
2173,N,Exotic Stones,"Carriere, MS",(601) 798-4334,"6985 US-11, Carriere, MS 39426",https://www.google.com/maps/place/?q=place_id:ChIJcerf1ie8nYgR-D6E-yONwXM&hl=en,none,none,none,none,none
2174,N,"All Builders Millworks, Llc","Ruston, LA",(318) 381-2586,"758 Burgessville Rd, Ruston, LA 71270",https://www.google.com/maps/place/?q=place_id:ChIJNVdMaJbbMYYRC6TAR9nVB7k&hl=en,none,none,none,none,none
2175,N,"H&A Remodeler | Home, Deck & Kitchen Remodeling Eagle","Eagle, ID",(208) 603-5471,"79 E Aikens Rd, Eagle, ID 83616",https://www.google.com/maps/place/?q=place_id:ChIJe4XM0Iurr1QRKhu3mMzPXMU&hl=en,none,none,none,none,none
2176,N,R&R Tile Services LLC,"Union Gap, WA",(509) 406-5828,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZbUn-1ElsSARFxj2VV_jb-4&hl=en,none,none,none,none,none
2177,N,Hilton Head Home Solutions,"Hilton Head Island, SC",(843) 227-4087,"18 Executive Park Rd #3, Hilton Head Island, SC 29928",https://www.google.com/maps/place/?q=place_id:ChIJ8WU2zzx5_IgRR6X27DaD6V0&hl=en,none,none,none,none,none
2178,N,Our Tops LLC,"Barberton, OH",(330) 396-1974,"846 Coventry Rd, Barberton, OH 44203",https://www.google.com/maps/place/?q=place_id:ChIJywakG5jVMIgRIHhY-qm4gbY&hl=en,none,none,none,none,none
2179,N,Rodabough Construction,"Layton, UT",(801) 499-2288,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv6mmgod15YsRzJJZNI0FhGM&hl=en,none,none,none,none,none
2180,N,Handyman Can Utah,"Cedar City, UT",(385) 219-7186,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0wUzgIthtYARGrfbwKnXlI4&hl=en,none,none,none,none,none
2181,N,Hobbs Property Improvement LLC,"Bath, NY",(607) 684-1346,"13 Hillview Dr, Bath, NY 14810",https://www.google.com/maps/place/?q=place_id:ChIJ63MfQHmv0YkR8gJMyrU9txc&hl=en,none,none,none,none,none
2182,N,"Elite Tile and Remodeling, LLC","Petersburg, VA",(804) 888-4501,"17917 Sandy Ford Rd, Petersburg, VA 23803",https://www.google.com/maps/place/?q=place_id:ChIJDyzjrRqhsYkRPPh-IBmFiV0&hl=en,none,none,none,none,none
2183,N,Watson Construction,"Greenville, MS",(662) 703-1991,"700 Sewanee St, Greenville, MS 38701",https://www.google.com/maps/place/?q=place_id:ChIJo85lEXXtK4YR9Di2pGa29FE&hl=en,none,none,none,none,none
2227,N,Custom Tile Installations,"Chino Valley, AZ",(928) 460-2073,"1355 Taft Ave, Chino Valley, AZ 86323",https://www.google.com/maps/place/?q=place_id:ChIJs2O7Jwc3LYcRWzRqgmOz8ZI&hl=en,none,none,none,none,none
2228,N,Cabinets Plus,"Bemidji, MN",(218) 444-1937,"51243 US-71, Bemidji, MN 56601",https://www.google.com/maps/place/?q=place_id:ChIJe4fiyLgruFIRH2dmYFft-VQ&hl=en,none,none,none,none,none
2229,N,Montgomery Carpentry & Construction,"Clayton, OH",(937) 216-5413,"5928 W Wenger Rd, Clayton, OH 45315",https://www.google.com/maps/place/?q=place_id:ChIJ34qwfOuBP4gR5cGw8rprhaI&hl=en,none,none,none,none,none
2230,N,Aiken Tub and Tile Repair and Refinishing,"Aiken, SC",(803) 262-3262,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJSRRb75xL-IgRoLVrLli_hPs&hl=en,none,none,none,none,none
2231,N,Elegant Kitchens and Home Design,"Staten Island, NY",(718) 967-7700,"20 S Bridge St Ste B, Staten Island, NY 10309",https://www.google.com/maps/place/?q=place_id:ChIJqYGrqKu1w4kRNoHfGS5AHuc&hl=en,none,none,none,none,none
2232,N,Collins Cabinets,"Russellville, AR",(479) 880-1906,"285 Crow Mountain Rd, Russellville, AR 72802",https://www.google.com/maps/place/?q=place_id:ChIJQQBEYNWszYcRs8-n1rqu8LI&hl=en,none,none,none,none,none
2233,N,Kitchen and Bath Solutions,"Charlottesville, VA",(434) 466-5232,"1208 E Market St, Charlottesville, VA 22902",https://www.google.com/maps/place/?q=place_id:ChIJr57gmSaJs4kRa0uowZxCm30&hl=en,none,none,none,none,none
2234,N,Kitchen and Bath Design Center,"Lake Hopatcong, NJ",(973) 810-5300,"820-, 766 NJ-15, Lake Hopatcong, NJ 07849",https://www.google.com/maps/place/?q=place_id:ChIJnwXB3VNzw4kRpjbWliDjUHo&hl=en,none,none,none,none,none
2235,N,Reliable Remodelers,"St Marys, PA",(814) 389-6866,"134 Robin Rd, St Marys, PA 15857",https://www.google.com/maps/place/?q=place_id:ChIJLQ22DSWtzYkRP6SZOCKMJFo&hl=en,none,none,none,none,none
2236,N,Mercier's Woodworks,"Ocean Springs, MS",(228) 872-2060,"6521 Sunplex Dr, Ocean Springs, MS 39564",https://www.google.com/maps/place/?q=place_id:ChIJBw-yHan2m4gRNwwUuXZfHWA&hl=en,none,none,none,none,none
2237,N,Jaime's Custom Cabinets,"City of Atwater, CA",(209) 819-6013,"3514 Atwater Blvd C, City of Atwater, CA 95301",https://www.google.com/maps/place/?q=place_id:ChIJc2j4wrtrkYARzq923spm3NE&hl=en,none,none,none,none,none
2238,N,Kitchen Brothers,"Riverside, OH",(937) 999-7517,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgc0ezN2FQIgRjlJ0ALd6s28&hl=en,none,none,none,none,none
2239,N,JC Tile & Home Remodeling llc,"Newton, NC",(704) 201-0015,"504 S Main Ave, Newton, NC 28658",https://www.google.com/maps/place/?q=place_id:ChIJndzsB4Q1UYgRYGYfKydWdWA&hl=en,none,none,none,none,none
2240,N,Heffner Flooring & Tile LLC,"Greenbrier, AR",(501) 589-5107,"608 AR-25, Greenbrier, AR 72058",https://www.google.com/maps/place/?q=place_id:ChIJ40HhFCb__2UR4Gj7B401se0&hl=en,none,none,none,none,none
2241,N,Precision Remodeling of IL inc.,"Centralia, IL",(779) 279-9412,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJtdt0i_IpDIgR14oQXEzFeGA&hl=en,none,none,none,none,none
2242,N,"Kitchens By Design, Inc.","Sterling, MA",(978) 422-6008,"57 Old Princeton Rd W, Sterling, MA 01564",https://www.google.com/maps/place/?q=place_id:ChIJJTPIS8j544kR-cp2gc69LaY&hl=en,none,none,none,none,none
2243,N,Jason Morris Tile Installer,"Fort Madison, IA",(319) 316-8119,"3178 180th St, Fort Madison, IA 52627",https://www.google.com/maps/place/?q=place_id:ChIJP8ptTMbX5ocR6DpQI2LuMnc&hl=en,none,none,none,none,none
2244,N,Urban Kitchen and Bath LLC,"Germantown, MD",(240) 370-7656,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzSmpGhMttokRjzaHuNZmcyQ&hl=en,none,none,none,none,none
2245,N,Kitchen Designs,"Kingsport, TN",(423) 378-5181,"830 W Center St, Kingsport, TN 37660",https://www.google.com/maps/place/?q=place_id:ChIJKX6Cr1ftWogR8UNf1jhdwd4&hl=en,none,none,none,none,none
2246,N,S&S Home Supplies Inc.,"Daly City, CA",(415) 330-9288,"419 Allan St, Daly City, CA 94014",https://www.google.com/maps/place/?q=place_id:ChIJZ1EriNB-j4ARbK5tpQZir5I&hl=en,none,none,none,none,none
2247,N,Dericko Remodeling,"Grandview, MO",(816) 342-5742,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJaXi5JwjdwIcRVXjeWN5hDX8&hl=en,none,none,none,none,none
2248,N,Cedar Rose Woodworks,"Cañon City, CO",(719) 269-9171,"1210 Park Ave, Cañon City, CO 81212",https://www.google.com/maps/place/?q=place_id:ChIJX4SOZnuPFIcRCxSPjlHCXGg&hl=en,none,none,none,none,none
2249,N,A+ Construction And Remodeling Service,"Zion, IL",(847) 244-4444,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJI_mM28jyD4gREpV0YMPaohE&hl=en,none,none,none,none,none
2250,N,Cincinnati Bathroom Remodeling Pros,"Cincinnati, OH",(513) 547-6539,"147 E McMicken Ave #2, Cincinnati, OH 45202",https://www.google.com/maps/place/?q=place_id:ChIJNTcXmfyzQYgRd2h2r2bayb4&hl=en,none,none,none,none,none
2251,N,HERRERA REMODELING LLC,"Indianapolis, IN",(463) 426-0149,"225 N Holmes Ave, Indianapolis, IN 46222",https://www.google.com/maps/place/?q=place_id:ChIJwRbGfwdXa4gR8beYwhRmxus&hl=en,none,none,none,none,none
2252,N,Strand Home Services LLC,"Marshall, MN",(507) 720-4864,"902 Birch St, Marshall, MN 56258",https://www.google.com/maps/place/?q=place_id:ChIJaWvzsYdZiocRlfE-IkKIVq0&hl=en,none,none,none,none,none
2253,N,Pinpoint Kitchen & Bath Showroom,"Williston Park, NY",(516) 833-5151,"348 Hillside Ave., Williston Park, NY 11596",https://www.google.com/maps/place/?q=place_id:ChIJVehBh_2HwokR5d2v8nJ5DKg&hl=en,none,none,none,none,none
2254,N,Modern Design Center,"Cherry Hill Township, NJ",(856) 288-1300,"912 Haddonfield Rd B, Cherry Hill Township, NJ 08002",https://www.google.com/maps/place/?q=place_id:ChIJFUVZWDvjb0AR6_uVFxOXBio&hl=en,none,none,none,none,none
2255,N,Fort Wayne Bathroom Remodeling Pros,"Fort Wayne, IN",(260) 295-8727,"5420 Lake Ave, Fort Wayne, IN 46815",https://www.google.com/maps/place/?q=place_id:ChIJ___j23v7FYgReedwqE8Vrpk&hl=en,none,none,none,none,none
2256,N,BP REMODELING AND CONSTRUCTION,"Rosenberg, TX",(832) 509-6933,"5108 Alderney Ct #5686, Rosenberg, TX 77471",https://www.google.com/maps/place/?q=place_id:ChIJDxi2mDMcQYYRF9OwYZU7CxI&hl=en,none,none,none,none,none
2257,N,Gervais Kitchen Cabinets,"Methuen, MA",(508) 982-5852,"1 Ferndale Ave, Methuen, MA 01844",https://www.google.com/maps/place/?q=place_id:ChIJj_owhdSp44kRtPIZi9G4Dlc&hl=en,none,none,none,none,none
2258,N,CDUBBS REMODELING,"Big Spring, TX",(432) 213-4095,"1503 Lexington Ave, Big Spring, TX 79720",https://www.google.com/maps/place/?q=place_id:ChIJEfzp0H4j-YYR6h3cuUY5rWE&hl=en,none,none,none,none,none
2259,N,Gold Remodeling Wildomar.,"Wildomar, CA",(925) 940-1124,"20616 Sydney Ct, Wildomar, CA 92595",https://www.google.com/maps/place/?q=place_id:ChIJTY3ChTib3IARFdDdRjGb9o0&hl=en,none,none,none,none,none
```
