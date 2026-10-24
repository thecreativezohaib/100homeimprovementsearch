# Round 2: Gemini task 3, part 06 of 22 (50 businesses: 50 F)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 183, reply in that chat "Continue with the businesses
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
95,F,Danish Remodeling LLC,"Cartersville, GA",(470) 255-1899,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP14dfs5P9YgRWQzZbziSFqg&hl=en,none,https://www.instagram.com/danishremodeling,none,none,none
186,F,Niemeyer Elite Construction,"Hitchcock, TX",(832) 390-8811,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZQdwqdPv_wMR05-hdrM6Cq4&hl=en,https://www.facebook.com/profile.php?id=100085039082849,none,none,Josh Boltz,none
382,F,By One Bathroom Renovations,"Ocoee, FL",(407) 505-5625,"940 Carter Rd, Winter Garden, FL 34787",https://www.google.com/maps/place/?q=place_id:ChIJWTvafkkrX2kRWBAUcyf6yLw&hl=en,https://www.facebook.com/61559079570597/,https://www.instagram.com/byonebathrooms/,none,Tyler,none
278,F,Ridgeline Renovations,"Sahuarita, AZ",(520) 332-3123,"18775 S Sonoita Hwy, Vail, AZ 85641",https://www.google.com/maps/place/?q=place_id:ChIJm4Bc69JaOqURCQgugZaRSQM&hl=en,https://www.facebook.com/CodysHomeImprovements,none,none,Cody,none
485,F,GM Construction Inc.,"Richton Park, IL",(630) 542-1983,"221 Arrowhead St, Park Forest, IL 60466",https://www.google.com/maps/place/?q=place_id:ChIJpdt4d6tjDogRiF4OuLtIeo0&hl=en,https://www.facebook.com/morenogmc,none,none,none,none
187,F,JBZ Custom Cabinets & Trim,"Willis, TX",(832) 803-5686,"12016 Hairston Dr, Willis, TX 77318",https://www.google.com/maps/place/?q=place_id:ChIJJ-uIRnYXR4YRSshg2HJMPRo&hl=en,https://www.facebook.com/jbzcustom,none,none,none,none
188,F,The Tile Guys LLC,"Southington, CT",(959) 212-9138,"131 Farmstead Rd, Southington, CT 06489",https://www.google.com/maps/place/?q=place_id:ChIJy357RSG354kRqGaILrgraxM&hl=en,https://www.facebook.com/profile.php?id=61564071747010,none,none,Thomas Weber,none
478,F,RS Builders Unlimited - Kitchen Bath Builders,"Severna Park, MD",(202) 492-4557,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ89oRd3r8t4kRo8ch4SuiUcY&hl=en,none,https://www.instagram.com/kitchenbathdesigners,none,none,none
182,F,Devlin Remodeling LLC,"Edgewood, KY",(859) 380-0370,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJlf1PclQ-DKMR0SgmTvKjGPI&hl=en,https://www.facebook.com/devlinremodeling,none,none,Keith Devlin,none
570,F,VM TEAM - HOME REMODELING,"Liberty Hill, TX",,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6XhTkpah2iEROub3lBW5tCY&hl=en,https://www.facebook.com/homeremodelcompany,none,none,none,none
270,F,Dove Remodeling,"Medford, OR",(541) 951-3683,"2275 Kings Hwy, Medford, OR 97501",https://www.google.com/maps/place/?q=place_id:ChIJQVX5UV93z1QRjPjbsE9820s&hl=en,http://www.facebook.com/doveremodelingccb122274,none,none,Steven Earl Westcott,none
387,F,Lakeside Stone,"Sylacauga, AL",(256) 378-0606,"34470 US-280, Childersburg, AL 35044",https://www.google.com/maps/place/?q=place_id:ChIJXSzfzjpaiYgRTzS9tO-q66Y&hl=en,https://www.facebook.com/LakesideStoneGranite,none,none,Tim Green; Amanda Green,none
583,F,Minarikz remodeling/contracting llc,"Owosso, MI",(517) 206-2196,"6547 E Cutler Rd, Bath Township, MI 48808",https://www.google.com/maps/place/?q=place_id:ChIJx94e1i3lIogRVIYv4FVvyLg&hl=en,none,https://www.instagram.com/worklikeagentleman/,none,none,none
536,F,Beckett Custom Finishes,"Rapid City, SD",(605) 391-0014,"859 N Valley Dr, Rapid City, SD 57703",https://www.google.com/maps/place/?q=place_id:ChIJv3vUlgxpfYcRvxysfHWogSI&hl=en,https://www.facebook.com/BeckettCustomFinishes,none,none,none,none
92,F,JMA Home Repair and Remodel LLC,"Palm Coast, FL",(386) 334-9034,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJlTmuWvvOI6sRScz0QqhN36w&hl=en,https://www.facebook.com/JMAHomeRepairandRemodelLLC,none,none,Matt,none
184,F,ELEVATE REMODELING CONSTRUCCION LLC,"Kearny, NJ",(862) 220-7325,"Clifton Ave #293, Newark, NJ 07104",https://www.google.com/maps/place/?q=place_id:ChIJ8R0Yxi1VwokR7VmDU3UHLvw&hl=en,none,https://www.instagram.com/elevateremodelingco,none,none,none
272,F,Hord Home Improvements LLC,"Edgewood, KY",(919) 902-3749,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJy_WtfsfHQYgR8KklazTxeEs&hl=en,https://www.facebook.com/Hord-Home-Improvements-109547397566279/,none,none,Brandon Hord,none
483,F,Master Tile Bathrooms Remodeling,"Leominster, MA",(857) 237-8043,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJI6Pg7TWjFKcRCJYqPTy_G5c&hl=en,none,https://www.instagram.com/master_tile_/,none,none,none
492,F,Astoria Granite Works,"Warrenton, OR",(503) 325-0761,"423 Gateway Ave, Astoria, OR 97103",https://www.google.com/maps/place/?q=place_id:ChIJAxFU2Mdkk1QRhAMY8N50PsQ&hl=en,https://www.facebook.com/Astoriagranite,none,none,Chris Schauermann; Sharon Louise Schauermann,none
578,F,Dovetail Custom Cabinets,"Grove, OK",(918) 801-8372,"61959 E 349 Rd, Grove, OK 74344",https://www.google.com/maps/place/?q=place_id:ChIJn05ZuGLLyYcRPEdt0DoAB8o&hl=en,https://www.facebook.com/share/1HxACLuD4a/,none,none,none,none
579,F,J-Dub Remodeling LLC,"Marianna, FL",(850) 614-0729,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ835KIv-v_gEREFA394geU0M&hl=en,https://www.facebook.com/people/J-Dub-Remodeling-LLC/100084852790020/,none,none,JustinRobson,none
97,F,Dean's Custom Cabinets,"Joplin, MO",(417) 782-4109,"961 N Central City Rd, Joplin, MO 64801",https://www.google.com/maps/place/?q=place_id:ChIJn_To8L9wyIcRhHb-Xab2uxo&hl=en,https://www.facebook.com/Deans-Custom-Cabinets-111935522154913/,none,none,none,none
490,F,Leon Remodeling LLC,"Rexburg, ID",(928) 243-4073,"1439 N 1100 E, Shelley, ID 83274",https://www.google.com/maps/place/?q=place_id:ChIJx5vq4dEbVVMR8dwq6cgmSMM&hl=en,https://www.facebook.com/leonremod/,none,none,none,none
475,F,Janke Custom Tile,"Bay City, MI",(989) 475-5452,"3390 Dobson Dr, Bay City, MI 48706",https://www.google.com/maps/place/?q=place_id:ChIJzdVt7JDhI4gRgrQV2gYey7k&hl=en,https://www.facebook.com/Jankecustoms,none,none,Kevin Janke,none
487,F,Custom Works Renovations,"Presque Isle, ME",(207) 554-6360,"495 Main St, Presque Isle, ME 04769",https://www.google.com/maps/place/?q=place_id:ChIJr59LlTC7vEwRcNDX-j9sS1Y&hl=en,https://www.facebook.com/share/19qDcwwicf/,none,none,none,none
178,F,C.A HOMES REMODELING LLC,"Freeport, TX",(979) 997-5138,"151 Cora Ln, Oyster Creek, TX 77541",https://www.google.com/maps/place/?q=place_id:ChIJgy-TsoZPtqkRu696jjZm2Vk&hl=en,https://www.facebook.com/CAHomesRemodelingLLC,none,none,none,none
375,F,Elite Home Renovations,"Holly Springs, MS",,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJKf0M0raRf4gRo0sqMsvakIo&hl=en,https://www.facebook.com/Elite-Home-Renovations-103118754840854/,none,none,none,none
180,F,Charlie’s Kitchen and Bath,"Romulus, MI",(313) 300-4499,"25315 Kean St Suite 6, Dearborn, MI 48124",https://www.google.com/maps/place/?q=place_id:ChIJ6dld4vBLO4gRMQf3Yw7xQ78&hl=en,none,https://www.instagram.com/charlies_kitchen_and_bath,none,none,none
379,F,"Greeson Cabinets Custom Cabinetry, LLC","Burlington, NC",(336) 380-8458,"5961 State Hwy 49, Burlington, NC 27215",https://www.google.com/maps/place/?q=place_id:ChIJI4QJY_ktU4gRpINrTnXYyGs&hl=en,https://www.facebook.com/greesoncabinetsinc,none,none,David Greeson; Shaun Greeson,none
484,F,A PLUS REMODELING LLC,"Rahway, NJ",(347) 889-9297,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ5bMbhAcw9C0R9ahkQlcRC9o&hl=en,none,https://www.instagram.com/a.plusremodeling,none,none,none
86,F,WOODEYE LLC,"Aumsville, OR",(458) 356-8185,"278 E High St, Stayton, OR 97383",https://www.google.com/maps/place/?q=place_id:ChIJZ-lXVzf1v1QR3eG-YiRVN8Y&hl=en,none,https://www.instagram.com/woodeye_woodworking,none,none,none
181,F,Splash Tile,"Freeport, FL",(850) 499-5251,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ9XsGUdgh2g4RX-Dz3wrP3U0&hl=en,http://www.facebook.com/splashllc,none,none,Briana Lynn Maurchie,none
189,F,KD Builders,"Zebulon, NC",(252) 578-3268,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJU5OdtohO02wRn5tshU-mV5k&hl=en,https://www.facebook.com/profile.php?id=100083679876282,none,none,none,none
263,F,IDF GRANITE,"Garden City, GA",(912) 238-5000,"4801A Ogeechee Rd, Garden City, GA 31405",https://www.google.com/maps/place/?q=place_id:ChIJjfKyb6EK-4gRlQ0DJ_XHXB4&hl=en,https://www.facebook.com/pages/idf-granite/152027814732,none,none,Luke; Dwayne,none
405,F,Jimmy Deans Tile Installers LLC.,"Freeport, FL",(850) 399-0303,"Not a Store, 3391 County Hwy 83A front, Freeport, FL 32439",https://www.google.com/maps/place/?q=place_id:ChIJk5ttLFDnk4gR91fN1fVMnHQ&hl=en,https://www.facebook.com/100063529904971,none,none,none,none
494,F,KR & Sons Remodeling LLC,"Irving, TX",(469) 222-0709,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJPTFDa5LybqQRkeC-IVGbCzo&hl=en,none,https://www.instagram.com/krsonsremodeling,none,none,none
576,F,Windsor Construction of MN,"Victoria, MN",(952) 270-0876,"1391 Creekside Dr, Waconia, MN 55387",https://www.google.com/maps/place/?q=place_id:ChIJiTeLp-UzpG0RYAWUND7KwyA&hl=en,https://www.facebook.com/windsorconstructionmn/,none,none,Shon E. Hissam,none
584,F,A&R Flooring and Remodeling LLC,"Moore, OK",(405) 889-3214,"Oklahoma City, OK 73139",https://www.google.com/maps/place/?q=place_id:ChIJCaIVw4Yhn6wRk6Xu3fxyz3c&hl=en,https://www.facebook.com/profile.php?id=100051374928837,none,none,Luis Ramirez,none
75,F,True Custom Countertops,"San Marcos, TX",(512) 877-2734,"100 N Edward Gary St Ste C, San Marcos, TX 78666",https://www.google.com/maps/place/?q=place_id:ChIJJUEUFVCpXIYRMbuPq_NbhH8&hl=en,https://www.facebook.com/truecustomco,none,none,Denny Rivas; Luis Rivas,none
88,F,S&M customs (home solutions),"Munford, TN",(901) 315-4970,"1287 Nelson Dr, Brighton, TN 38011",https://www.google.com/maps/place/?q=place_id:ChIJBwD-34QTf4gRKWmwl1UBNao&hl=en,https://www.facebook.com/SandMCustoms,none,none,Matt Page; Heather Page,none
276,F,Simplified Construction,"Old Forge, PA",(570) 955-6258,"153 Sussex St, Old Forge, PA 18518",https://www.google.com/maps/place/?q=place_id:ChIJOw34WOY4X4UR8BvxVscNTRk&hl=en,https://www.facebook.com/profile.php?id=61569885021803,none,none,none,none
378,F,Mr. Odd Job,"Enterprise, AL",(334) 475-1000,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJjYvuQX1IUIcRX6Xc1SbHqWA&hl=en,http://www.facebook.com/mroddjobllc,none,none,none,none
380,F,Kitchen Cabinet and Countertop Factory,"Leonia, NJ",(201) 906-4062,"423 Bergen Blvd, Palisades Park, NJ 07650",https://www.google.com/maps/place/?q=place_id:ChIJ52Ktfqn3wokRqVSQaNU4aDw&hl=en,none,https://www.instagram.com/kitchen.cabinet.factory/,none,William,none
384,F,Tile Jawn Bathroom Remodeling,"Phoenixville, PA",(484) 302-8265,"1151 Callowhill St, Phoenixville, PA 19460",https://www.google.com/maps/place/?q=place_id:ChIJV8FyA5lUxWQRYrE-SFxb1L8&hl=en,none,https://www.instagram.com/tilejawn,none,Ashley Singer; Marlon Cedeno,none
509,F,Two Phoenix Remodeling,"Sweetwater, TN",(423) 594-6000,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHb4NgK2hYIgRSeayvibAbpA&hl=en,https://www.facebook.com/twophoenixremodeling,none,none,Edsel Parnell,none
87,F,B&H Kitchen Remodeling,"Oxford, OH",(513) 659-0568,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJGRT4wATMVWQRf4VFVe9IVqk&hl=en,https://www.facebook.com/BHKITCHENREMODELING,none,none,Joel Hecker,none
271,F,"Cutting Edge Remodeling, Llc","Otsego, MN",(612) 978-8465,"8136 Padgett Ave NE, Otsego, MN 55330",https://www.google.com/maps/place/?q=place_id:ChIJgcmQVENps1IRzZWIxa4zT3c&hl=en,https://www.facebook.com/profile.php?id=100054286340960,none,none,Dima (Dmitriy) Sharik,none
488,F,WGB Construction LLC,"Monroe, NC",(980) 499-9445,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP0wRtdXITS4R_zRoc72lkzg&hl=en,none,https://www.instagram.com/wgbceramictile,none,none,none
179,F,Empire Cabinets,"Denham Springs, LA",(225) 955-0299,"9445 Prince Charles St, Denham Springs, LA 70726",https://www.google.com/maps/place/?q=place_id:ChIJfQgKuJa_JoYR5mXzt8qpR1Y&hl=en,http://facebook.com/empirecabinetshop,none,none,none,none
183,F,Pure Remodelers LLC,"Marysville, WA",(425) 518-0969,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJs7BOI_B3KmMRPV1zZgnq16s&hl=en,https://www.facebook.com/pureremodelers,none,none,none,none
```
