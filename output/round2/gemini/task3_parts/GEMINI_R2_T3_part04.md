# Round 2: Gemini task 3, part 04 of 22 (50 businesses: 50 F)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 197, reply in that chat "Continue with the businesses
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
1716,F,"J. Miller Cabinet Company, Inc.","Columbia City, IN",(260) 691-2032,"5874 N 350 E, Columbia City, IN 46725",https://www.google.com/maps/place/?q=place_id:ChIJSTgDaml3FogRHzVzEhydZ_w&hl=en,https://www.facebook.com/jmillercabinet,none,none,"Steve Marchand, Sherral Marschand",http://jmillercabinetco.centurylinksite.net/
1722,F,Bath Remodel Pro Inc.,"Watervliet, NY",(518) 838-0798,"7 Maple Ave, Watervliet, NY 12189",https://www.google.com/maps/place/?q=place_id:ChIJO4G1wEwO3okRtkSXNGE1qWk&hl=en,https://www.facebook.com/Yourremodelpro,none,none,Allen Passonno,none
1731,F,"CHIC Services, LLC","Cicero, IL",(312) 690-1292,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTxTkVnI1DogRNeDqbbrRj5A&hl=en,https://www.facebook.com/CHICModernDesign,none,none,none,http://chicmoderndesign.com/
1735,F,Navisa Custom Countertops LLC,"DeSoto, TX",(214) 586-4875,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ07_k1nhNHCsRUyfFf_HRGuI&hl=en,https://www.facebook.com/navisacustomcountertopsllc,none,none,none,none
1740,F,J&M floor and Bathroom Construction,"Palmetto Bay, FL",(786) 608-0337,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbxLHaDTF2YgRZG6U8L1I5uA&hl=en,https://www.facebook.com/100067487492434,none,none,none,none
1749,F,Perque Cabinets and Counter tops,"Houma, LA",(985) 360-3450,"6189 W Main St, Houma, LA 70360",https://www.google.com/maps/place/?q=place_id:ChIJ1Qz1e3UQIYYR1uU00WNlqaU&hl=en,https://www.facebook.com/pages/Perque-Cabinets/176680883015944,none,none,"Brian John Perque, Joshua Perque",none
1752,F,Battin Kitchen Designs,"Cochranton, PA",(814) 573-2780,"156 N Franklin St, Cochranton, PA 16314",https://www.google.com/maps/place/?q=place_id:ChIJjX65iFP-MogRcqQ_LYCHrBI&hl=en,https://www.facebook.com/BattinKitchenDesigns,none,none,Jill Battin,http://www.battinkitchendesigns.com
1756,F,Cabinets By Springfield,"Miami, OK",(918) 540-0505,"300 E BJ Tunnell Blvd, Miami, OK 74354",https://www.google.com/maps/place/?q=place_id:ChIJSTVawZcXyIcRe7wbiTRlSKk&hl=en,https://www.facebook.com/CabinetsBySpringfieldMiamiOK,none,none,David Springfield,none
1766,F,MHDS Renovations,"Indiana, PA",(724) 427-5075,"494 Stannard Ave, Indiana, PA 15701",https://www.google.com/maps/place/?q=place_id:ChIJlxGgDP1by4kRLT7iOVCn7FY&hl=en,https://www.facebook.com/mattsHDS,none,none,Matt Inscho,http://www.mhdsreno.com/
1768,F,Spinks Stone Shop Granite and More,"Arkadelphia, AR",(870) 210-6199,"119 Malvern Rd, Arkadelphia, AR 71923",https://www.google.com/maps/place/?q=place_id:ChIJjWGsh3XfMoYRUlH3zwMl2-4&hl=en,https://www.facebook.com/100066821821575,none,none,none,none
1771,F,Bates Home Improvement,"Ardmore, OK",(580) 264-0264,"16 S Washington St, Ardmore, OK 73401",https://www.google.com/maps/place/?q=place_id:ChIJ8SeBpcMvTYYRjlM7E5APoL8&hl=en,https://www.facebook.com/100063620170938,none,none,Greg Bates,none
1773,F,M G BATHTUB REPAIR,"Victorville, CA",(760) 900-6743,"12653 Field Way, Victorville, CA 92395",https://www.google.com/maps/place/?q=place_id:ChIJpS60CuyBt4cRLkTc1NKirIo&hl=en,https://www.facebook.com/p/Bathtub-Repair-100067851643972,none,none,none,none
1781,F,Quad State Upgrades,"Joplin, MO",(417) 439-1352,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTaSEQ_YLKosRvUQDRYcGbG0&hl=en,https://www.facebook.com/61591578598075,none,none,none,none
1785,F,Shaffer Construction,"Salisbury, MD",(443) 859-5317,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbTjH5Wr9uIkRKO4mNrSDVq8&hl=en,https://www.facebook.com/shafferconstructiondelmarva,none,none,none,none
1812,F,Alex Massa llc,"Haddon Heights, NJ",(856) 685-9758,"916 W Kings Hwy, Haddon Heights, NJ 08035",https://www.google.com/maps/place/?q=place_id:ChIJtdEyKpnOxokR5BqNssN3StI&hl=en,https://www.facebook.com/AlexanderMassaLLC,none,none,Alexander Massa,none
1814,F,Braun Home Improvements,"New Kensington, PA",(412) 519-6446,"218 Dombroski Ave, New Kensington, PA 15068",https://www.google.com/maps/place/?q=place_id:ChIJiYVNYIuVNIgRFuzWvzpQiH0&hl=en,https://www.facebook.com/braunhomeimprovements/,none,none,William Braun,none
1892,F,M&M Cabinets & Countertops,"Butte, MT",(406) 219-8010,"3928 Wynne Ave Unit 3 & 4, Butte, MT 59701",https://www.google.com/maps/place/?q=place_id:ChIJjZEINO4HW1MRwnbvNYUG-eE&hl=en,https://www.facebook.com/m2countertops/,none,none,none,none
1895,F,Affordable Cabinets LLC,"South Daytona, FL",(386) 299-1064,"1079 Sheri Blvd, South Daytona, FL 32119",https://www.google.com/maps/place/?q=place_id:ChIJEx42qq7Z5ogRF2P_9pp82aw&hl=en,https://www.facebook.com/100057539525282,none,none,Ed,http://affordablecabinetsllc.com
1918,F,Frias Remodeling LLC,"Palm Springs, FL",(561) 460-7815,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXYbmHEEF6YsR13aPznCwFhA&hl=en,https://www.facebook.com/frias.remodeling.llc/,none,none,none,none
1928,F,Royal-T Construction inc.,"Erda, UT",(801) 808-3882,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJseXFObVQ1KsR4axTDH7JXSM&hl=en,https://www.facebook.com/royaltconstructionutah/,none,none,Stephanie Chamberlain and Micah Chamberlain,none
1930,F,Casa Genessa Home Renovations LLC,"Warr Acres, OK",(405) 652-8764,"5601 NW 72nd St Suite #260B, Warr Acres, OK 73132",https://www.google.com/maps/place/?q=place_id:ChIJA5ROg6gFsocR5_Jxz3Nq1pY&hl=en,https://www.facebook.com/profile.php?id=61592534485317,none,none,none,none
1987,F,"Mohawk Renovations, LLC","Aurora, IL",(630) 800-8819,"2261 Feltes Ln, Aurora, IL 60502",https://www.google.com/maps/place/?q=place_id:ChIJ4eA6I677DogRGAewyOELHcA&hl=en,https://www.facebook.com/Mohawkrenovation,none,none,none,none
2009,F,Brooksberry Kitchens and Baths,"St. Louis, MO",(314) 872-7720,"751 Old Frontenac Square, St. Louis, MO 63131",https://www.google.com/maps/place/?q=place_id:ChIJ7bhI79DM2IcRnS5VY3KoSFc&hl=en,https://www.facebook.com/pages/brooksBerry-Kitchens-and-Baths/529437973802477,none,none,none,none
2012,F,Precision Woodworks llc,"Suffolk, VA",(757) 642-1686,"1614 Pitchkettle Rd, Suffolk, VA 23434",https://www.google.com/maps/place/?q=place_id:ChIJBd_W3TMPsIkRMaMgogLQzUM&hl=en,https://www.facebook.com/stephenjames48,none,none,Stephen James,none
2105,F,Paul Allen Construction,"Weatherford, TX",(817) 658-9803,"1839 E Lake Dr, Weatherford, TX 76087",https://www.google.com/maps/place/?q=place_id:ChIJJThHNyQHToYRSekPvP7HwAg&hl=en,https://www.facebook.com/100057402731294,none,none,Paul Allen,none
2189,F,A Best Granite,"Lumberton, TX",(409) 751-0825,"4805 US-69, Lumberton, TX 77657",https://www.google.com/maps/place/?q=place_id:ChIJ3bKS8nIxOYYRosoUdppRKy4&hl=en,https://www.facebook.com/pages/category/business-center/a-best-granite-in-beaumont-1796898877203019,none,none,none,http://abestgraniteinbeaumont.com
2195,F,C.Q. Construction,"Jackson, MI",(517) 962-8610,"2716 Page Ave, Jackson, MI 49203",https://www.google.com/maps/place/?q=place_id:ChIJm8UXe5ElPYgR_QRRgjY-AzE&hl=en,https://www.facebook.com/CQConstructionn,none,none,none,none
2199,F,Brenham Area Marble; LLC,"Brenham, TX",(979) 836-1249,"2579 FM389, Brenham, TX 77833",https://www.google.com/maps/place/?q=place_id:ChIJ41-G2pkDRIYRpdrsLy8oAEU&hl=en,https://www.facebook.com/brenhamareamarble,none,none,none,https://www.brenhamareamarble.com/
2219,F,Top Tier Bathworks,"Pleasant Hill, IA",(515) 717-1215,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJM0uSu5aV7ocRDcb5tvpAJ2U&hl=en,https://www.facebook.com/JRRenovations17,none,none,none,none
2292,F,J May Custom Carpentry,"Hobbs, NM",(575) 602-3240,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJL2tPVyJGOIAR57CpYSysBPo&hl=en,https://www.facebook.com/jmaycustomcarpentry/,none,none,none,none
2297,F,Hyde Studio,"Shawnee, OK",(405) 551-5386,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbXlIP8NbgYURrZ_raFncdiE&hl=en,https://www.facebook.com/61589386452664/,none,none,none,none
2325,F,Tnt Bathtub Repair of Ga LLC,"Bethlehem, GA",(770) 886-2255,"583 J B Owens Rd, Bethlehem, GA 30620",https://www.google.com/maps/place/?q=place_id:ChIJSfXF6rfc9YgRnxlIqYHNjR8&hl=en,https://www.facebook.com/61581868357506/,none,none,Tony Ray,http://www.tntbathtubrepair.com
2332,F,Morgan Tile Creations LLC,"Pea Ridge, AR",(479) 405-9637,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJA-mgNMmfzwYRdTcG09vMEhM&hl=en,https://www.facebook.com/100089037422447/,none,none,Dylan,none
2334,F,"Heritage Construction, LLC","Hardeeville, SC",(843) 683-2894,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpxJiFuPMvAEReaAqNcUCaFo&hl=en,https://www.facebook.com/61589745449309/,none,none,none,none
2336,F,Kitchen Bath Designers,"Camp Verde, AZ",(877) 207-0220,"2833 S Old Church Rd, Camp Verde, AZ 86322",https://www.google.com/maps/place/?q=place_id:ChIJZWTQ4BBVLIcRzL1KOeqj5aE&hl=en,https://www.facebook.com/61563571475293/,none,none,Alexis,http://kitchen-bath-designers.com
2342,F,"Creative Flooring & Remodeling, LLC","Baraboo, WI",(608) 393-7455,"456 Lynn St, Baraboo, WI 53913",https://www.google.com/maps/place/?q=place_id:ChIJzxWdrj9qB4gR4DmNmFydsNI&hl=en,https://www.facebook.com/creativeflooringandremodeling/,none,none,Travis,none
2355,F,JBee Designs,"Macomb, IL",(309) 333-0637,"17 East Side Square, Macomb, IL 61455",https://www.google.com/maps/place/?q=place_id:ChIJVbxHWQf34IcRlJBZx6KHIAA&hl=en,https://www.facebook.com/jbeedesignsco/,none,none,"Jena Bredeman, CKBD",none
2357,F,"Davies Custom Design, LLC","Plaquemine, LA",(225) 685-7423,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxapsVu-s1KUR9EWaBNS2d6o&hl=en,https://www.facebook.com/DaviesTCD/,none,none,none,none
2375,F,Jr Blair Remodeling,"Massillon, OH",(330) 324-2271,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHZDM59hgSkURiOdy7SVGQ4A&hl=en,https://www.facebook.com/100089528122197/,none,none,Kelli Blair,none
2384,F,Refinement Remodeling & Design,"Goose Creek, SC",(203) 260-1733,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJixDcqqY5cyoRBd_YUZV3q8k&hl=en,https://www.facebook.com/Refinementpaintingservices,none,none,none,none
2387,F,B & B Cabinet & Trim,"Lufkin, TX",(936) 632-5743,"2864 FM325, Lufkin, TX 75901",https://www.google.com/maps/place/?q=place_id:ChIJN38z0L88OIYRo2ptWz-1WzY&hl=en,https://www.facebook.com/pages/B-B-Cabinet-Trim/117650698296505,none,none,none,none
2394,F,Grouted Tile And Flooring,"Williston, ND",(228) 229-4846,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJhc_75SbfD28RHytAgzz7EjA&hl=en,https://www.facebook.com/p/Travis-Hesler-III-61581480573516/,none,none,Travis Hesler III,none
522,F,JMC Luxury Countertops LLC,"Burlington, NC",(336) 437-3953,"106 W Hanover Rd, Graham, NC 27253",https://www.google.com/maps/place/?q=place_id:ChIJF0o8g5ErU4gRVeXY-STmRtc&hl=en,https://www.facebook.com/JMCluxurycountertops,none,none,Luis,none
321,F,Hopkins Renovation & Design,"Atlanta, GA",(404) 563-9716,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJo6QFhIAf9YgR9gFj9By10_E&hl=en,https://www.facebook.com/hopkins.renovadesign,none,none,Tasha Hopkins,none
121,F,Renovations F&W,"Kissimmee, FL",(321) 290-2884,"2802 E Irlo Bronson Memorial Hwy, Kissimmee, FL 34744",https://www.google.com/maps/place/?q=place_id:ChIJ419031OKJKER3EaZQ5pf1zs&hl=en,https://www.facebook.com/renovations.fw,none,none,Francisco F. Solorzano Sr.,http://www.renovationsfw.com
326,F,Continental Wood and Stone Company,"Defiance, OH",(419) 789-9765,"919 Grove St, Defiance, OH 43512",https://www.google.com/maps/place/?q=place_id:ChIJRd0cVpHRPYgRHy6row9OrAE&hl=en,https://www.facebook.com/pages/Continental-Wood-and-Stone/318654535010316,none,none,Nathan Bowers,http://www.woodandstonecompany.mynetworksolutions.com/
331,F,Aesthetics Cabinetry LLC,"DeLand, FL",(386) 320-2806,"1510 Old Daytona Cir, DeLand, FL 32724",https://www.google.com/maps/place/?q=place_id:ChIJxVlofXEd54gROjGwg0wJJA0&hl=en,https://www.facebook.com/61561537658265,none,none,Dwayne Dayes,none
403,F,RD&CS,"Clarksville, IN",(651) 802-8519,"8098 Hynes Ave S, Cottage Grove, MN 55016",https://www.google.com/maps/place/?q=place_id:ChIJvZQ3T9zb94cRh_QOEYoizAw&hl=en,https://www.facebook.com/ReyesDCS,none,none,none,none
340,F,Los Álvarez y Reyes Floor Service,"Balch Springs, TX",(972) 876-5474,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ79FxlQg-GqkRHLJqP5SDV1Q&hl=en,https://www.facebook.com/los.alvarez.reyes,none,none,none,none
197,F,Sierra Home Remodel LLC,"La Porte, IN",(219) 455-9017,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJH7GqSKVnyykRQm15NZ4Qc-E&hl=en,https://www.facebook.com/61553933757431,none,none,Carlos Garfias,https://www.sierrahomeremodelin.com/
```
