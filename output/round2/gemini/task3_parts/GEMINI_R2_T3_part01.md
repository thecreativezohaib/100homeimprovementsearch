# Round 2: Gemini task 3, part 01 of 22 (50 businesses: 39 E, 11 F)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row 1009, reply in that chat "Continue with the businesses
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
69,E,McMichael Home Repair,"St. Peters, MO",(314) 568-5888,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJw8zFTsEr34cRhVzNQGrwRuk&hl=en,none,none,Seth@McMichaelHomeRepair.com (seen at https://www.markate.com/business/mcmichaelhomerepair),SethMcMichael,http://mcmichaelhomerepair.com
438,E,Custom By Alvarez,"Lake Wales, FL",(863) 439-3889,"18720 US-27, Lake Wales, FL 33853",https://www.google.com/maps/place/?q=place_id:ChIJGZvXgLQK3YgRNDwxq3VwTSs&hl=en,none,none,cbatops@aol.com (seen at https://www.yoursun.com/polk/newsarchives/cabinetmaker-relocates-to-downtown-lake-wales/article_f173772a-f1f6-5edf-8d15-755453450af4.html),Chris Alvarez and Mary Alvarez,none
214,E,Floyd Remodeling/Custom Kitchen/Bath,"Thomasville, NC",(336) 491-0256,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ12Ql4DmZU4gRJNDqpfijFcg&hl=en,none,none,stevereno2005@yahoo.com (seen at https://www.onbizmap.com/company-details/lexington-nc/floyd-remodeling/2921),Steve and David,none
42,E,VL Granite & Marble LLC,"Sheridan, CO",(303) 591-7523,"1865 W Union Ave Ste J, Sheridan, CO 80110",https://www.google.com/maps/place/?q=place_id:ChIJW-H0U6-Ba4cR6WfSqeIULMo&hl=en,none,none,VLGRANITEANDMARBLE9@GMAIL.COM (seen at https://www.facebook.com/groups/974662322726856/posts/3256591437867255/),Victor Lopez,http://vlgranite.com
1215,E,DC Kitchen & Bath,"Westbury, NY",(516) 280-7988,"896 Old Country Rd, Westbury, NY 11590",https://www.google.com/maps/place/?q=place_id:ChIJmVhyF0qHwokRc3zcruhDbbk&hl=en,none,none,dckitchenb@gmail.com (seen at https://www.cosentino.com/en-gb/store/westbury/dc-kitchen-bath/),none,none
1405,E,CRUSH IT Renovations LLC,"South Pasadena, FL",(727) 490-9451,"email. crushitrenovate@gmail.com, 7882 Sailboat Key Blvd S, South Pasadena, FL 33707",https://www.google.com/maps/place/?q=place_id:ChIJIcX5Ijj9wogR1SFH2eMXMmU&hl=en,none,none,crushitrenovate@gmail.com (seen at https://www.google.com/maps/place/?q=place_id:ChIJIcX5Ijj9wogR1SFH2eMXMmU&hl=en),none,none
1592,E,Top Notch Granite solid countertops,"Florence, MS",(601) 540-0755,"93 Jackson Cir, Florence, MS 39073",https://www.google.com/maps/place/?q=place_id:ChIJkcakxDHTKYYRwD7rUGWdBsM&hl=en,none,none,federick.oberto@gmail.com (seen at https://www.msbuildersbuyersguide.com/listing.php?listing_id=660002309&company_name=Top+Notch+Granite),Federick Oberto,none
1594,E,Ogden Woodworking,"Goleta, CA",(805) 680-5867,"375 Pine Ave #13, Goleta, CA 93117",https://www.google.com/maps/place/?q=place_id:ChIJ56ix-nhA6YARgr-rdfNSR8U&hl=en,none,none,sbpoolleague@cox.net (seen at https://www.santabarbarayp.com/biz/31104/ogden-woodworking),none,http://ogdenwoodworking.com
1611,E,JCS TILE & MARBLE,"Port Townsend, WA",(360) 643-3344,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJI_p0UbdccQkRaNtKt5PYLPA&hl=en,none,none,5477rocket@gmail.com (seen at https://blaketileandstone.com/local-tile-setters/),Marcia Adrienne Herrmann,http://jcstilemarble.com
1619,E,Designed By Julie LLC,"Midland, MI",(989) 835-1200,"608 S Saginaw Rd, Midland, MI 48640",https://www.google.com/maps/place/?q=place_id:ChIJwR5h76PVI4gR6L8d8Rc5ZmM&hl=en,none,none,info@designedbyjulie.biz (seen at https://www.manta.com/c/mt48x19/designed-by-julie),"Julie Ratcliffe, Mark Ratcliffe",http://www.designedbyjulie.biz
1640,E,DNA CONSTRUCTION 1 LLC,"Harrison, NJ",(551) 580-5040,"59 Washington St, Harrison, NJ 07029",https://www.google.com/maps/place/?q=place_id:ChIJQ4PjuKVVwokRnEnrqPolf6g&hl=en,none,none,dpservices0607@gmail.com (seen at https://njlca.org/find-a-contractor/),Diego Porres,none
1645,E,Argento Marble & Granite Inc,"Carbondale, CO",(970) 963-7070,"1101 Dolores Way, Carbondale, CO 81623",https://www.google.com/maps/place/?q=place_id:ChIJMVj1ZOqrQYcRAT8ewRtWmL8&hl=en,none,none,office@argentomarble.com (seen at https://talents.vaia.com/companies/tahoe-daily-tribune/carbondale/office-assistant-project-estimator-argento-marble-llc-103128806/),none,http://argentostone.com/
1667,E,Wills Builders,"Warren, PA",(814) 723-4190,"1513 Pennsylvania Ave W # C, Warren, PA 16365",https://www.google.com/maps/place/?q=place_id:ChIJ2d1zV6ZFzYkRH8g05tVK7k4&hl=en,none,none,willsbuilders@westpa.net (seen at http://yankeebushproductions.com/directory/listing/superior-plus-energy-services),Jack A. Wills,http://www.willsbuildersnwpa.com
1699,E,Elevated Services LLC,"Ruidoso, NM",(575) 937-3752,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ66PU6uOT-KMROivkoNxEays&hl=en,none,none,elevatedtile575@gmail.com (seen at https://www.facebook.com/groups/237708150747979/posts/1862685341583577/),none,none
1705,E,"Swing Cabinets, LLC","Shelbyville, TN",(931) 684-3576,"331 Pinkston Rd, Shelbyville, TN 37160",https://www.google.com/maps/place/?q=place_id:ChIJ8fa121_pY4gRWb8ZnmjO4Zs&hl=en,none,none,wright9544@yahoo.com (seen at https://www.tn.gov/agriculture/businesses/business-development/forest-products/directory-of-tn-forest-industries-rd.html),"Ezralee Swing, Carol Wright",none
1723,E,"KirkBath, Kirk Kitchen","Albany, OR",(541) 758-0776,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJK_I1CZJAwFQRblNfWzIqJTA&hl=en,none,none,KirkBath@KirkBath.com (seen at https://sites.google.com/site/njbhouse/services/contractor),"Emma Kirk, Joel Kirk",http://www.kirkbuild.biz/
1737,E,Roberts Stone Products,"Shelbyville, KY",(502) 844-2107,"1073 Brooks Industrial Rd, Shelbyville, KY 40065",https://www.google.com/maps/place/?q=place_id:ChIJDYOWPxDAaYgRHTNA7RN2tx0&hl=en,none,none,info@robertsstoneproducts.com (seen at https://www.manta.com/c/mmsy021/robert-stone-products),Orville J. (Jay) Roberts,http://www.robertsstoneproducts.com/
1741,E,VAV Construction Corp- Remodeling- Contractor,"Calumet City, IL",(872) 238-9920,"1215 Hirsch Ave, Calumet City, IL 60409",https://www.google.com/maps/place/?q=place_id:ChIJ99l6UBCzhqURnhMf-gQRhrk&hl=en,none,none,vavconstructioncorp@gmail.com (seen at https://www.doraziorealestate.com/affiliates),Alex Villa,none
1754,E,R&S Home Remodelers,"Manchester, NH",(603) 361-1138,"500 Harvey Rd #201, Manchester, NH 03103",https://www.google.com/maps/place/?q=place_id:ChIJ93gaeW9F4okRYzRikkeWWCc&hl=en,none,none,grogers10104@gmail.com (seen at https://www.nhcompanyregistry.com/companies/r-s-home-remodelers-llc/),Gerome Rogers Sr.,https://rshomeremodelers.com/
1755,E,Chesapeake Perma Glaze South Inc.,"Bel Air, MD",(410) 688-4740,"1202 Glastonbury Way, Bel Air, MD 21014",https://www.google.com/maps/place/?q=place_id:ChIJq7KuvEbcx4kRlJVM9Fqklcg&hl=en,none,none,john@cpgsouth.com (seen at https://www.manta.com/c/mtcc4fv/chesapeake-perma-glaze-south-inc),John Raccioppi,http://www.cpgsouth.com/
1816,E,Kelly's Kitchen and Bath,"O'Fallon, MO",(636) 697-0380,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJYylCmJe_LGYRKB_2vEUF56A&hl=en,none,none,kelly@kellyskandb.com (seen at https://www.facebook.com/KelleyHomeServices/posts/the-best-bathrooms-arent-just-beautiful-theyre-built-to-lastfrom-the-materials-b/1537742144806033/),none,none
1905,E,M&J Demolition & Remodeling LLC,"Deer Park, TX",(832) 691-1171,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ13w9NV5RoWsRRkHycDl3x40&hl=en,none,none,en071591@gmail.com (seen at https://usdirectory.com/M-J-Demolition-Remodeling-Llc-Pasadena),none,none
1941,E,Texas Pride Home Services,"Schertz, TX",(830) 370-4433,"3616 Gamble, Schertz, TX 78154",https://www.google.com/maps/place/?q=place_id:ChIJX0lLUlqSXIYRj_sEerJeeDA&hl=en,none,none,texaspridehomeservices@gmail.com (seen at https://satx.localhorizon.com/detail-page/texas-pride-home-services),Joseph (Joe),none
1995,E,Beussink Brothers Woodworks,"Jackson, MO",(573) 243-4642,"2129 Old Toll Rd, Jackson, MO 63755",https://www.google.com/maps/place/?q=place_id:ChIJ43C0xleLd4gRole2MEGYNXY&hl=en,none,none,swissarmy@element74.com (seen at https://jacksonmochamber.org/members/beussink-brothers-woodworks/),Steve Beussink & Greg Beussink,none
2300,E,Bespoke Bathrooms Boise,"Kuna, ID",(208) 695-0222,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJiwHP3dSyX40Rbl3Yx0E6R3w&hl=en,none,none,info@bespokebathroomsboise.com (seen at https://container.parishesonline.com/bulletins/05/1198/20231001B.pdf),Russell Evans,http://bespokeboise.com
2301,E,Upper Left Construction,"Wenatchee, WA",(509) 670-2392,"125 N Wilson St, Wenatchee, WA 98801",https://www.google.com/maps/place/?q=place_id:ChIJVVUxf7zMm1QRK1Hgf3g_rOU&hl=en,none,none,jsnyder86@yahoo.com (seen at https://data.wa.gov/api/views/72ja-e4r2/rows.rdf?accessType=DOWNLOAD),Joshua James Snyder; Tristen Ryles,http://www.upperleftconstruction.com
2324,E,Jackson Woodworks,"Polson, MT",(406) 600-4443,"34598 Courville Trail, Polson, MT 59860",https://www.google.com/maps/place/?q=place_id:ChIJCVSyEWp3Z1MRcFM7qTSiw00&hl=en,none,none,bozemanwood@gmail.com (seen at https://leaderadvertiser.com/news/2018/jun/28/local-carpenter-jackson-crafts-cabinetry-for-13/),Bob Jackson,http://jacksonwoodworksmt.com
2328,E,JJ Construction & Renovations,"Kingsport, TN",(423) 388-5251,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv4lZezqmwYgRy6gKEu4AoC0&hl=en,none,none,jj_construction_reno@yahoo.com (seen at https://www.brownbook.net/business/12259895/jj-construction-renovations),none,http://jjconstruction.co
2349,E,L H Carpentry,"Nacogdoches, TX",(936) 556-3053,"3057 Co Rd 723, Nacogdoches, TX 75964",https://www.google.com/maps/place/?q=place_id:ChIJAVJPSxv1N4YRyb2cB_hbu-0&hl=en,none,none,1hcarpentry6@gmail.com (seen at https://findnactx.com/detail-page/l-h-carpentry),Lonnie Hoffman,none
2386,E,Sam's Cabinets Inc.,"Salisbury, NC",(704) 754-0096,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6YeCUvqLU4gRmP_mxP46FYI&hl=en,none,none,ssplus8@carolina.rr.com (seen at https://www.chamberofcommerce.com/business-directory/north-carolina/salisbury/cabinet-maker/1339207575-sam-s-cabinets-inc),Sam / Gail Spain-Marsh,none
347,E,CK Tile and Home Repair LLC,"Crystal, MN",(952) 356-7295,"6530 57th Ave N, Minneapolis, MN 55428",https://www.google.com/maps/place/?q=place_id:ChIJpfecVL83s1IRjPur556CnvQ&hl=en,none,none,ciros115@gmail.com (seen at https://www.archspm.org/pastoral-familiar/),Ciro Sanchez Jr.,none
175,E,Antonio's Tile,"Ypsilanti, MI",(734) 623-3274,"2770 Eastlawn Ave, Ypsilanti, MI 48197",https://www.google.com/maps/place/?q=place_id:ChIJS-bSy4ypPIgRUmh71lU0ers&hl=en,none,none,antonialmurdoc@gmail.com (seen at https://ezlocal.com/mi/ypsilanti/tile-contractors/097839535),Antonio Murdock,none
61,E,Custombilt Counter Tops,"Waycross, GA",(912) 283-5704,"1822 Albany Ave, Waycross, GA 31503",https://www.google.com/maps/place/?q=place_id:ChIJbTowhqn674gRhZrLYxQMw8g&hl=en,none,none,custombiltcountertops@gmail.com (seen at https://brokersnapshot.com/Company/custombilt-products-inc),none,none
173,E,CNG Construction Inc,"Kenmore, NY",,"33 Traymore St, Buffalo, NY 14216",https://www.google.com/maps/place/?q=place_id:ChIJL5TKmiFt04kR3TYix_lbNLY&hl=en,none,none,cngconstructioninc@gmail.com (seen at https://www.roserocket.com/trucking-company/cng-construction-inc-usdot-2886450),Craig Gardo,none
534,E,ARM Home Care,"Mendham, NJ",(973) 348-9915,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ75loAqejw4kRQnUDsQrtplk&hl=en,none,none,tom@armhomecare.com (seen at https://importer.tradeford.com/arms),Thomas Tahl,https://www.armhomecare.com
539,E,Granite Mastercraft,"Shelby, NC",(336) 410-2260,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJUQZOI3zEZSoRpTahP1j42Mw&hl=en,none,none,granitemaster@emailsl.com (seen at https://sites.bubblelife.com/community/granite_master_craft),Victor K. Chamorro,http://www.granitemastercraft.com
111,E,Quality Kitchens & Baths,"Humboldt, TN",(731) 431-9944,"7657 Hwy 45 S, Martin, TN 38237",https://www.google.com/maps/place/?q=place_id:ChIJ0QZqHuZgeYgRwpmHgtxuLOc&hl=en,none,none,qualitykitchensandbaths@hotmail.com (seen at https://delta.creativecirclecdn.com/richardson/files/20260212-110938-1d1-02.12.26%20WEB%20DE%20KMC.pdf),Michael Guthrie,none
103,E,Turnmire Eco Construction,"Connell, WA",(509) 220-4367,"3478-B Moore Rd, Kettle Falls, WA 99141",https://www.google.com/maps/place/?q=place_id:ChIJNbYkumoinlQR0LcW-M1Ocsk&hl=en,none,none,LiamTurnmire@gmail.com (seen at https://kyrs.org/underwriting/turnmire-logo/),Liam Turnmire (William P Turnmire),none
407,E,Hawksview Services,"Cheshire, CT",(203) 809-1133,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJO8NLpW7H54kREKrhFXuxPoM&hl=en,none,none,info@hawksviewservices.com (seen at https://www.manta.com/c/mtbtpsp/hawksview-services-llc),Brian Frappier,http://hawksviewservices.com
254,F,Hangliter Residential llc (OH),"Dublin, OH",(614) 290-6430,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJEYHUpi71CygRbevsU7v3lX0&hl=en,https://www.facebook.com/100089274582347,https://www.instagram.com/hangliterresidential,none,Kenneth W Hangliter,http://hangliterres.com
577,F,La. Custom's Inc.,"Patterson, LA",(985) 290-5737,"30133 Philip Smith Rd, Lacombe, LA 70445",https://www.google.com/maps/place/?q=place_id:ChIJ_SL3LhrxnYgRfaUbZ1QVSew&hl=en,https://www.facebook.com/lacustoms/,none,none,none,http://lacustoms.us
282,F,Paragon Remodeling,"Tuskegee, AL",(334) 521-6162,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJw4nAI9U184gR40CzemrmQWY&hl=en,https://www.facebook.com/remodelingbyparagon,none,none,none,http://remodelingbyparagon.com
491,F,ECC TILE SERVICES,"Lemon Grove, CA",(619) 327-8258,"3242 A Kempf St, Lemon Grove, CA 91945",https://www.google.com/maps/place/?q=place_id:ChIJgfZuH2BR2YARn_6OMZ7SDEI&hl=en,none,https://www.instagram.com/ecc_tile,none,Eduardo,http://ecctileservices.com/
504,F,Surface Pro STL Kitchen and Bathtub Refinishing,"Webster Groves, MO",(636) 359-6844,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ15n74C2n3ocR2QZjUwYJREk&hl=en,https://www.facebook.com/surfaceprostl,none,none,none,http://surfaceprostl.com
1001,F,Xclusive Kitchens and Baths Corp,"Miami Shores, FL",(305) 912-8094,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJayyx51ux2YgRCOlmB6OTVWI&hl=en,http://www.facebook.com/xclusivekitchensandbaths,none,none,none,none
1003,F,The Kitchen Connection LLC.,"Farmington, MO",(573) 701-5101,"Home Office Please Call First To Setup An Appointment, 720 Grey Fox, Farmington, MO 63640",https://www.google.com/maps/place/?q=place_id:ChIJmX01BhpF2IcRGX5FV25qFn8&hl=en,https://www.facebook.com/TheKitchenConnectionLLC,none,none,Jeramie D Soderlund,none
1005,F,Bath Designs by Ceramics Niagara Inc.,"Niagara Falls, NY",(905) 708-2539,"7832 Mulhern St, Niagara Falls, ON L2H 1B7, Canada",https://www.google.com/maps/place/?q=place_id:ChIJx5tmu5ZF04kRsapkudnqA-M&hl=en,https://www.facebook.com/bathsdesignsbyceramicsniagara,none,none,Sergio Fierimonte,none
1006,F,Casa Tile & Design,"Chappaqua, NY",(914) 374-3347,"1 King St, Chappaqua, NY 10514",https://www.google.com/maps/place/?q=place_id:ChIJR2oD1G26wokR7IZF7QVyCfY&hl=en,https://m.facebook.com/CasaTile,none,none,none,https://www.casatileanddesign.com/
1008,F,Preaux Cabinets & Quartz,"Covington, LA",(985) 276-3145,"2027 Philip Dr, Covington, LA 70433",https://www.google.com/maps/place/?q=place_id:ChIJL1F4ttkqZSwRbj9znIB4vM4&hl=en,https://www.facebook.com/profile.php?id=61593496591734,none,none,none,none
1009,F,Lakeway Countertops & Cabinets,"Morristown, TN",(423) 587-8655,"1135 W Morris Blvd, Morristown, TN 37813",https://www.google.com/maps/place/?q=place_id:ChIJ_____wKXW4gR2Hvo-4AaHE8&hl=en,https://www.facebook.com/profile.php?id=61551998780346,none,none,none,none
```
