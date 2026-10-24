# Round 2: Gemini task 2, part 13 of 17 (100 businesses, rows 2284 to 2383)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 2383: reply in that chat "Continue with
   the businesses after LAST_ROW_DONE, same rules, same columns" and keep that report too.

## The task (Gemini: follow this exactly)
```
You are doing a long research task on 100 small kitchen and bathroom remodeling businesses in the United
States. Each one has a Google Business Profile but no working website. For each one I need: a contact email that the
business itself has published, and its Facebook page and/or Instagram profile. Work through the table at the end of
this file from top to bottom, in that order, and do NOT skip any.

The "task" column:
- C and D: new businesses. Do all the checks below for every one.

CHECKS FOR EACH BUSINESS (do every step; do not stop at the first result):
1. Facebook: search Google for "<business_name>" <town> facebook, and for the phone number in quotes
   (for example "(352) 988-7800" and "352-988-7800"). Open the page and confirm it is the same business (same name
   AND same phone, town or owner). If known_facebook is given, open it. Read the Intro, About, Page transparency and
   contact info, and the captions of its latest posts and photos. Small contractors often write their email in a
   post caption, a photo caption, a flyer or a business card photo. Note followers and the newest post date.
2. Instagram: search "<business_name>" instagram and the handle from the Facebook page. Read the bio, the contact
   button and the latest captions. Note followers and the newest post date.
3. Email: search Google for the phone number together with "@gmail.com", "@yahoo.com", "@aol.com", "@outlook.com",
   "@hotmail.com" and "email". Then check the Google Business Profile, BBB, Yelp, Houzz, Angi, HomeAdvisor,
   Thumbtack, Nextdoor, Porch, BuildZoom, Manta, Alignable, Birdeye, MapQuest, Chamber of Commerce listings, the state
   contractor licence lookup, the state business registry, local newspaper articles, and supplier "find an
   installer" pages.
4. Website check: search "<business_name>" <town> and the phone number. If the business has its own website that
   loads and shows the business, put it in website_found and write website_status = live. If a site exists but is
   down, parked, "launching soon", expired or a "domain not connected" page, put it in website_found and write
   website_status = dead. A Facebook, Instagram, Linktree, Yelp or directory page is NOT a website. If none: NONE.

RULES
- Never guess or build an email from a name pattern. Only copy an email you actually saw on a page, with that page's
  URL (email_source_url) and a quote of 20 words or fewer from that page that contains it (email_source_quote).
  People-search and email-finder sites (ContactOut, RocketReach, ZoomInfo, Whitepages and similar) do NOT count.
- Accept a Facebook page, Instagram profile or email only if it clearly belongs to THIS business (same name and the
  same phone, town or owner). If unsure, leave it out and say why in notes.
- Plain full URLs only: no [text](url) links, no google.com redirect links, no shortened links.
- sources_checked: every source you actually opened for that business, separated by semicolons.
- Keep each business's row number from the table.
- Do not stop to ask me anything and do not write long prose. Spend your effort on the research. A short summary at
  the top is enough.
- If you run out of room before the last business, finish the one you are on, output everything so far, and end
  with the line LAST_ROW_DONE: <row number>.

OUTPUT
End the report with ONE CSV block (in a ```csv code block) with exactly this header:
row,business_name,facebook_url,instagram_url,email,email_source_url,email_source_quote,website_found,website_status,owner_name,facebook_followers,facebook_latest_post_date,instagram_followers,instagram_latest_post_date,photo_posts,sources_checked,notes
- One line for every business where you found at least one of: a Facebook page, an Instagram profile, an email or
  a website. Unknown fields are UNKNOWN. Put any text containing a comma in double quotes.
- After the CSV block, one line: NOTHING_FOUND: followed by the row numbers you researched and found nothing for,
  separated by commas.
```

## Businesses (100, in order)
```csv
row,task,business_name,town,phone,address,google_maps,known_facebook,known_instagram,known_email,dead_website
2284,C,Steinberger Tile and Remodeling,"Cisco, TX",(214) 431-2019,"501 W 17th St, Cisco, TX 76437",https://www.google.com/maps/place/?q=place_id:ChIJR_dHZHVs7qwRGxrNDnxXDwY&hl=en,none,none,none,none
2285,C,K-Lind Tile Inc,"Cape Girardeau, MO",(573) 335-5121,"487 Mockingbird Ln, Cape Girardeau, MO 63701",https://www.google.com/maps/place/?q=place_id:ChIJS1VX6-cgeIgRIRfhZH6B_CE&hl=en,none,none,none,none
2286,C,Old Mill Cabinets & Carpentry,"Jackson, MI",(517) 796-4936,"2344 Brooklyn Rd, Jackson, MI 49203",https://www.google.com/maps/place/?q=place_id:ChIJYyjIA0okPYgRH43kWXQmjX8&hl=en,none,none,none,none
2287,C,Eliu Remodeling LLC,"Cincinnati, OH",(283) 227-7655,"10407 Gloria Ave, Cincinnati, OH 45231",https://www.google.com/maps/place/?q=place_id:ChIJ85fDHy1LQIgRJY8pzmmsmAM&hl=en,none,none,none,none
2288,C,Hurley's Creative Tile Co,"Duncan, OK",(580) 252-0218,"4705 Ponderosa Rd, Duncan, OK 73533",https://www.google.com/maps/place/?q=place_id:ChIJ3Xi8d-BcrYcR9xLF_7ZGg-Y&hl=en,none,none,none,none
2289,C,Southern Idaho Cabinets,"Buhl, ID",(208) 543-6495,"4195 N 1380 E, Buhl, ID 83316",https://www.google.com/maps/place/?q=place_id:ChIJqbbZH5-UrFQRaPCQBRkFlMw&hl=en,none,none,none,none
2290,C,Neptoon Tile Company,"Mount Sterling, KY",(859) 414-0962,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJY0q_gqS9Q4gRgRUNWQ7NqVk&hl=en,none,none,none,none
2291,C,Jv construction & remodeling LLC,"Kenner, LA",(504) 559-3408,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJL_fdj_FBu4YRICjVEbNmiEs&hl=en,none,none,none,none
2292,C,J May Custom Carpentry,"Hobbs, NM",(575) 602-3240,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJL2tPVyJGOIAR57CpYSysBPo&hl=en,none,none,none,none
2293,C,Best Home Remodeling MN,"St Paul, MN",(612) 324-8003,"1981 Yorkshire Ct, St Paul, MN 55116",https://www.google.com/maps/place/?q=place_id:ChIJPytgLVgp9ocR_VeItbfS16o&hl=en,none,none,none,none
2294,C,Oak Lane Remodeling,"Heath, OH",(740) 403-9449,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ79l4LNovI4URsaQSp7supRI&hl=en,none,none,none,none
2295,C,Aquidneck Kitchen & Bath,"Middletown, RI",(401) 619-2624,"510 E Main Rd #6, Middletown, RI 02842",https://www.google.com/maps/place/?q=place_id:ChIJ2c7uojOp5YkR9ws_7S2Ng_E&hl=en,none,none,none,none
2296,C,Nextek Kitchen's And Baths,"Lauderdale Lakes, FL",(305) 600-9421,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJE65S1vwH2YgR3_ELZUnHrnk&hl=en,none,none,none,none
2297,C,Hyde Studio,"Shawnee, OK",(405) 551-5386,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbXlIP8NbgYURrZ_raFncdiE&hl=en,none,none,none,none
2298,C,All American Coatings,"Twin Falls, ID",(208) 735-4173,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ3TfUpFNzKmURJblmRGTYnxE&hl=en,none,none,none,none
2299,C,Elite Remodeling & Renovations,"Duluth, GA",(404) 649-1165,"1826 Ridge Brook Trail, Duluth, GA 30096",https://www.google.com/maps/place/?q=place_id:ChIJL6UD5n6j9YgRj8nW1PqCAKU&hl=en,none,none,none,none
2300,C,Bespoke Bathrooms Boise,"Kuna, ID",(208) 695-0222,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJiwHP3dSyX40Rbl3Yx0E6R3w&hl=en,none,none,none,none
2301,C,Upper Left Construction,"Wenatchee, WA",(509) 670-2392,"125 N Wilson St, Wenatchee, WA 98801",https://www.google.com/maps/place/?q=place_id:ChIJVVUxf7zMm1QRK1Hgf3g_rOU&hl=en,none,none,none,none
2302,C,FRANCISCO PROFESSIONAL REMODELING LLC,"Corinth, MS",(662) 603-2759,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJb_deoNTuqAER1o4Asu8eQg0&hl=en,none,none,none,none
2303,C,"Select Custom Cabinetry, Inc","Auburn, GA",(678) 777-6150,"1384 Duncan Ln, Auburn, GA 30011",https://www.google.com/maps/place/?q=place_id:ChIJAz93UzjC9YgRF3CXT3chH14&hl=en,none,none,none,none
2304,C,JLB Handyman,"Fayetteville, NC",(910) 813-3809,"4413 Atlantic Ave, Fayetteville, NC 28306",https://www.google.com/maps/place/?q=place_id:ChIJteiVRj5uXAERSR4lyjcZ83Q&hl=en,none,none,none,none
2305,C,KGA Renovations And Design LLC,"Dearborn, MI",(313) 614-5968,"412 Greenfield Rd, Dearborn, MI 48121",https://www.google.com/maps/place/?q=place_id:ChIJrSQGr5Im4GIRn7cNbwUiOd8&hl=en,none,none,none,none
2306,C,Hometown Solutions - Rochester West,"Geneseo, NY",(585) 604-0352,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJj8k7AD0JaS4RjC-dzA3Ve8U&hl=en,none,none,none,none
2307,C,Florida Cabinet Solutions Co.,"Homestead, FL",(786) 253-4556,"20951 SW 336th St, Homestead, FL 33034",https://www.google.com/maps/place/?q=place_id:ChIJC8o-Zi-72YgRUcTrtEWGXUk&hl=en,none,none,none,none
2308,C,The Shower & Floor Co of GA LLC,"Albany, GA",(229) 903-7097,"2200 Little John Ln, Albany, GA 31707",https://www.google.com/maps/place/?q=place_id:ChIJ95oYqVIGBmYR5pA67CWTc-c&hl=en,none,none,none,none
2309,C,New Shine Co.,"Moline, IL",(309) 764-2064,"4521 11th Street A, Moline, IL 61265",https://www.google.com/maps/place/?q=place_id:ChIJzV_MkI4x4ocRQrJ4Ix_Mv-k&hl=en,none,none,none,none
2310,C,Kitchen Bath Plus,"High Point, NC",(866) 656-0175,"2210 Geddie Pl, High Point, NC 27260",https://www.google.com/maps/place/?q=place_id:ChIJB-5-U_gOU4gRGIijNJcGGFk&hl=en,none,none,none,none
2311,C,KGF Home Improvement,"Romulus, MI",(734) 502-4805,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJP3Njd6WpYSkRbtiDFfzPd88&hl=en,none,none,none,none
2312,C,Evolution marble & granite,"Milford, MA",(774) 477-9559,"34 Jefferson St ap 4, Milford, MA 01757",https://www.google.com/maps/place/?q=place_id:ChIJfT5OWalz5IkRYoi52DrhFi8&hl=en,none,none,none,none
2313,C,Countertop Creations LLc,"Fort Lupton, CO",(720) 202-1564,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJe2lTQtF5bIcRYVJLPP8zA-0&hl=en,none,none,none,none
2314,C,Trinity Remodeling,"Fort Worth, TX",(817) 448-7700,"Llano Ave, Fort Worth, TX 76116",https://www.google.com/maps/place/?q=place_id:ChIJG1UGsDMNToYR35CI-85ILoM&hl=en,none,none,none,none
2315,C,PARADISE BATHROOM REMODELS L.L.C.,"Vero Beach, FL",(772) 212-6871,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJG3uElvNDpAARn8_6THWkVxI&hl=en,none,none,none,none
2316,C,PJP REMODELING LLC,"Sayreville, NJ",(609) 977-5153,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxb_nAWd8TYMRKihp-r8Hn4g&hl=en,none,none,none,none
2317,C,Pelmbroke pines Remodeling Kitchen and Bathroom Expert,"Pembroke Pines, FL",(754) 223-8957,"8329 Pines Blvd, Pembroke Pines, FL 33024",https://www.google.com/maps/place/?q=place_id:ChIJrZVeDrCp2YgR_-LCBaZuNUM&hl=en,none,none,none,none
2318,C,H & H Construction and Remodeling,"Hingham, MA",(857) 499-0482,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJmekzaM9j44kRWw92IgG2IRo&hl=en,none,none,none,none
2319,C,Five Star Bath Solutions of Southern Tennessee,"Columbia, TN",(931) 288-5517,"1511 Bailey St, Columbia, TN 38401",https://www.google.com/maps/place/?q=place_id:ChIJXySfUAZzY4gRgWYvt0Ooa8g&hl=en,none,none,none,none
2320,C,Marbella Tile Co.,"Meadville, PA",(814) 673-4522,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbQWTvQpA808RqP7L687xEBY&hl=en,none,none,none,none
2321,C,H & R Renovations,"Pearland, TX",(832) 560-9559,"17119 Harkey Rd, Pearland, TX 77584",https://www.google.com/maps/place/?q=place_id:ChIJs7W3wCGSQIYRv2zdBIGE16Y&hl=en,none,none,none,none
2322,C,Custom Cabinet Co,"Green Bay, WI",(920) 434-1525,"2344 O Connor Rd, Green Bay, WI 54313",https://www.google.com/maps/place/?q=place_id:ChIJb8GKjCPxAogRcgbvrxslE8g&hl=en,none,none,none,none
2323,C,Crawford Cabinets By Kelly,"Blackshear, GA",(912) 286-7943,"3375 Gene Ln, Blackshear, GA 31516",https://www.google.com/maps/place/?q=place_id:ChIJ1wNi0bb_74gRoGR2x13cSGs&hl=en,none,none,none,none
2324,C,Jackson Woodworks,"Polson, MT",(406) 600-4443,"34598 Courville Trail, Polson, MT 59860",https://www.google.com/maps/place/?q=place_id:ChIJCVSyEWp3Z1MRcFM7qTSiw00&hl=en,none,none,none,none
2325,C,Tnt Bathtub Repair of Ga LLC,"Bethlehem, GA",(770) 886-2255,"583 J B Owens Rd, Bethlehem, GA 30620",https://www.google.com/maps/place/?q=place_id:ChIJSfXF6rfc9YgRnxlIqYHNjR8&hl=en,none,none,none,none
2326,C,Kitchen Renovators,"Mooresville, IN",(612) 735-0078,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_QQsxHso9ocRrOZKuPF4aCU&hl=en,none,none,none,none
2327,C,Rocky Bar Tile & Home Remodeling,"Mountain Home, ID",(208) 871-9971,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJO60h2lwtrFQRlVav7-1gvKA&hl=en,none,none,none,none
2328,C,JJ Construction & Renovations,"Kingsport, TN",(423) 388-5251,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv4lZezqmwYgRy6gKEu4AoC0&hl=en,none,none,none,none
2329,C,Zook Custom Kitchens,"Mendon, MA",(508) 280-6127,"21 Milford St, Mendon, MA 01756",https://www.google.com/maps/place/?q=place_id:ChIJY_vC8D9t5IkRDc3XI7Dfvyk&hl=en,none,none,none,none
2330,C,LJ Construction,"Tremont, IL",(309) 241-2839,"409 W Washington St, Tremont, IL 61568",https://www.google.com/maps/place/?q=place_id:ChIJQ3nWPVz7CogRlWeTS_CAlu8&hl=en,none,none,none,none
2331,C,L.S. Remodels LLC,"Mentor, OH",(216) 225-6957,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJG5LNgDyvMYgRHjqU-3hHCt0&hl=en,none,none,none,none
2332,C,Morgan Tile Creations LLC,"Pea Ridge, AR",(479) 405-9637,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJA-mgNMmfzwYRdTcG09vMEhM&hl=en,none,none,none,none
2333,C,Wilbourn & Son Cabinets,"Grenada, MS",(662) 417-7440,"271-273 Rosemond Rd, Grenada, MS 38901",https://www.google.com/maps/place/?q=place_id:ChIJpapex3jNgYgRc0e6h-q65Sk&hl=en,none,none,none,none
2334,C,"Heritage Construction, LLC","Hardeeville, SC",(843) 683-2894,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJpxJiFuPMvAEReaAqNcUCaFo&hl=en,none,none,none,none
2335,C,SafeNest Home Solutions LLC,"Timnath, CO",(970) 699-0679,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7WRxrQJXeYARIy7qj8zX48s&hl=en,none,none,none,none
2336,C,Kitchen Bath Designers,"Camp Verde, AZ",(877) 207-0220,"2833 S Old Church Rd, Camp Verde, AZ 86322",https://www.google.com/maps/place/?q=place_id:ChIJZWTQ4BBVLIcRzL1KOeqj5aE&hl=en,none,none,none,none
2337,C,Kitchen Remodeling Expert New Jersey,"Jersey City, NJ",(551) 271-3001,"152 Danforth Ave, Jersey City, NJ 07305",https://www.google.com/maps/place/?q=place_id:ChIJ-7XNpFBRwokRma7UWnjnEv4&hl=en,none,none,none,none
2338,C,Kanda Kitchen & Bathroom Remodeling,"Eagle Mountain, UT",(385) 429-3366,"4252 Kilkenny Way, Eagle Mountain, UT 84005",https://www.google.com/maps/place/?q=place_id:ChIJzU3bRTSCW6IR-NZt_-6f_vs&hl=en,none,none,none,none
2339,C,Instyle Kitchens and Bathrooms,"Marlborough, MA",(774) 203-3643,"200 E Main St Unit D, Marlborough, MA 01752",https://www.google.com/maps/place/?q=place_id:ChIJaUeRUGFh5IkR8-GhVCEc3dI&hl=en,none,none,none,none
2340,C,CNC Custom Cabinets,"Frankfort, KY",(502) 226-0666,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ6yJgqgJ1QogRq1_U_gEIxXA&hl=en,none,none,none,none
2341,C,Modifier,"Coral Springs, FL",(954) 425-2235,"4915 NW 105th Dr, Coral Springs, FL 33076",https://www.google.com/maps/place/?q=place_id:ChIJ8UMgXXgb2YgR4O5AYgOA4BA&hl=en,none,none,none,none
2342,C,"Creative Flooring & Remodeling, LLC","Baraboo, WI",(608) 393-7455,"456 Lynn St, Baraboo, WI 53913",https://www.google.com/maps/place/?q=place_id:ChIJzxWdrj9qB4gR4DmNmFydsNI&hl=en,none,none,none,none
2343,C,Westchester Woodworking,"Colchester, CT",(860) 537-3700,"228 Old Hartford Rd, Colchester, CT 06415",https://www.google.com/maps/place/?q=place_id:ChIJG-oS1T1C5okRUXYgeclFjdo&hl=en,none,none,none,none
2344,C,Prime Kitchen Cabinetry,"Powder Springs, GA",(404) 452-5974,"Bramlett Way, Powder Springs, GA 30127",https://www.google.com/maps/place/?q=place_id:ChIJXa7mWQgl9YgRCHrTwSkbJgg&hl=en,none,none,none,none
2345,C,Kustom Homes LLC,"Monroe, NC",(704) 441-2658,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJH5cwH9cxVIgRGN9F4T7RsWg&hl=en,none,none,none,none
2346,C,Kingdom Construction & Renovations LLC,"Cameron, TX",(361) 389-8749,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZ0B1yNInl0UReBzA60fas4E&hl=en,none,none,none,none
2347,C,Craftsman's Corner,"Butte, MT",(406) 723-5120,"223 E Park St, Butte, MT 59701",https://www.google.com/maps/place/?q=place_id:ChIJBwLS_LIJW1MRFC9VLTtdphQ&hl=en,none,none,none,none
2348,C,G&C Specialty Contractors,"La Grande, OR",(971) 732-3473,"701 Jackson Ave, La Grande, OR 97850",https://www.google.com/maps/place/?q=place_id:ChIJv9LfTrR3o1QRCZt-XtRaVEA&hl=en,none,none,none,none
2349,C,L H Carpentry,"Nacogdoches, TX",(936) 556-3053,"3057 Co Rd 723, Nacogdoches, TX 75964",https://www.google.com/maps/place/?q=place_id:ChIJAVJPSxv1N4YRyb2cB_hbu-0&hl=en,none,none,none,none
2350,C,Newport Beach Bathroom Remodeling Pros,"Newport Beach, CA",(949) 541-8327,"369 San Miguel Dr, Newport Beach, CA 92660",https://www.google.com/maps/place/?q=place_id:ChIJ342LKfjh3IAR_5g4g4EQUjA&hl=en,none,none,none,none
2351,C,Danz Remodeling LLC,"Hailey, ID",(208) 720-1654,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJcRUUdcprNkIRqOY_CZyveb4&hl=en,none,none,none,none
2352,C,J.r. pluming Jasper Alabama,"Jasper, AL",(205) 544-9423,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-YgpTZOSbEkRKI3PhV_ADQ8&hl=en,none,none,none,none
2353,C,H&A Home Remodeling of Hidden Springs,"Garden City, ID",(208) 471-9849,"5843 W Hidden Springs Dr, Garden City, ID 83714",https://www.google.com/maps/place/?q=place_id:ChIJtfyXStIBr1QRpFFmArD2mSc&hl=en,none,none,none,none
2354,C,Smith Custom Cabinets,"Columbus, IN",(812) 374-2523,"1196 Nelson Ridge Rd, Columbus, IN 47201",https://www.google.com/maps/place/?q=place_id:ChIJX0nHqimda4gRigKcPGD6yks&hl=en,none,none,none,none
2355,C,JBee Designs,"Macomb, IL",(309) 333-0637,"17 East Side Square, Macomb, IL 61455",https://www.google.com/maps/place/?q=place_id:ChIJVbxHWQf34IcRlJBZx6KHIAA&hl=en,none,none,none,none
2356,C,Bridge Custom Cabinets & Trim,"Canton, MS",(601) 954-5085,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJx0FeVZ7XKYYR1djMqQDb0Bw&hl=en,none,none,none,none
2357,C,"Davies Custom Design, LLC","Plaquemine, LA",(225) 685-7423,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJxapsVu-s1KUR9EWaBNS2d6o&hl=en,none,none,none,none
2358,C,Custom Wood Works Creative Kitchens,"Brockton, PA",(570) 668-4970,"221 Lewis St, Brockton, PA 17925",https://www.google.com/maps/place/?q=place_id:ChIJ676A2AvAxYkReg87ETDcFss&hl=en,none,none,none,none
2359,C,Jupiter Remodeling,"Jupiter, FL",(561) 283-5541,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJW1ghog0_bIsR0GPCPhAHjHE&hl=en,none,none,none,none
2360,C,Waco Texas Handyman and Remodeling Services LLC,"Waco, TX",(254) 313-8305,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJRy1XxvBWywwRM2MSjpJqRvY&hl=en,none,none,none,none
2361,C,High Quality Renovations,"Raymondville, TX",(830) 202-9128,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJkXxhKpwTXIYREP4ZqNieHV0&hl=en,none,none,none,none
2362,C,"PMCO LLC | Affordable Kitchen & Bathroom Remodeling, Reliable Flooring Contractor","Evans, CO",(970) 387-2617,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVVUQMvugbocRHdqFp8Gdb9o&hl=en,none,none,none,none
2363,C,Home Improvements of Arizona Cabinet Refacing,"Litchfield Park, AZ",(480) 249-2703,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJC49GtqM4K4cR3PTseCERGU8&hl=en,none,none,none,none
2364,C,Installer Pro Inc,"Suffern, NY",(845) 300-3944,"193 Doxbury Ln, Suffern, NY 10901",https://www.google.com/maps/place/?q=place_id:ChIJNajj9VrhwokRXsHTICWLBao&hl=en,none,none,none,none
2365,C,Superior Granite & Marble,"Madera, CA",(559) 395-4390,"24180 Ave 18, Madera, CA 93638",https://www.google.com/maps/place/?q=place_id:ChIJf6EvBi0JlIARNA1xWW3U1uM&hl=en,none,none,none,none
2366,C,BluePeak Bath Remodeling,"Cudahy, CA",(833) 567-6043,"4539 Santa Ana St, Cudahy, CA 90201",https://www.google.com/maps/place/?q=place_id:ChIJFwzP5WPPwoARp88-AAOph4Q&hl=en,none,none,none,none
2367,C,Gaithersburg Interior and Remodeling INC,"Gaithersburg, MD",(240) 679-5424,"102 Booth St, Gaithersburg, MD 20878",https://www.google.com/maps/place/?q=place_id:ChIJSUvmK-EttokR2-tqFnXjw94&hl=en,none,none,none,none
2368,C,Koehler Wood Works,"Mineral Wells, TX",(940) 325-0832,"2649 S US Hwy 281, Mineral Wells, TX 76067",https://www.google.com/maps/place/?q=place_id:ChIJ2WtIbRf1UYYRsgzFz_75pe0&hl=en,none,none,none,none
2369,C,Capitol Construction & Remodeling,"Saugus, MA",(978) 876-5488,"366 Central St #1, Saugus, MA 01906",https://www.google.com/maps/place/?q=place_id:ChIJ1a4I7fxz44kRa54KEv3GvFs&hl=en,none,none,none,none
2370,C,Higher Standard Renovations LLC,"Lenexa, KS",(913) 271-2071,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZ7HwM4ChUwkRuXgm8ggb0Tk&hl=en,none,none,none,none
2371,C,The Best Luxury Home Services,"Miramar, FL",(786) 752-2648,"6628 Emerald Lake Dr, Miramar, FL 33023",https://www.google.com/maps/place/?q=place_id:ChIJ90zgCTmv2YgRJOmWsBViLjc&hl=en,none,none,none,none
2372,C,Couch Potato Construction & Solutions LLC,"Aurora, OH",(440) 749-5986,"558 Crackel Rd, Aurora, OH 44202",https://www.google.com/maps/place/?q=place_id:ChIJvU1lsucXMYgRbNMXEgdFfew&hl=en,none,none,none,none
2373,C,Upward Build,"Lewisburg, TN",(602) 300-1602,"1728 Verona Caney Rd, Lewisburg, TN 37091",https://www.google.com/maps/place/?q=place_id:ChIJWUsVbBOjY4gRq0jA8MGY7Qg&hl=en,none,none,none,none
2374,C,Haise Remodeling LLC,"Lawrenceburg, KY",(502) 649-6750,"1898 Graefenburg Rd, Lawrenceburg, KY 40342",https://www.google.com/maps/place/?q=place_id:ChIJg_9_mV3ZaYgRHj4VI4Xl8LE&hl=en,none,none,none,none
2375,C,Jr Blair Remodeling,"Massillon, OH",(330) 324-2271,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJHZDM59hgSkURiOdy7SVGQ4A&hl=en,none,none,none,none
2376,C,Household Repairs and Remodel,"Sanger, TX",(940) 399-2326,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ2S9OVt8A868Rmk4rKa5eh98&hl=en,none,none,none,none
2377,C,M&M Cabinets,"Kensett, AR",(501) 827-2572,"1124 W Wilbur Mills Ave, Kensett, AR 72082",https://www.google.com/maps/place/?q=place_id:ChIJ3dx00Hio04cRXW5KAh20jM8&hl=en,none,none,none,none
2378,C,Chelan Custom Cabinetry,"Chelan, WA",(509) 387-9099,"40 E Shop Ave, Chelan, WA 98816",https://www.google.com/maps/place/?q=place_id:ChIJs4I639Cbm1QRf87ax66Se1g&hl=en,none,none,none,none
2379,C,"Fountain Construction & Cabinetry, LLC","Bay Minette, AL",(251) 402-4704,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ8RfX-S9pmogRsrzaWsZc4Uw&hl=en,none,none,none,none
2380,C,Classic Woodworks,"Humboldt, TN",(731) 784-3114,"3603 E Mitchell St, Humboldt, TN 38343",https://www.google.com/maps/place/?q=place_id:ChIJa3IBM5yufogRmXi-7P2hnrI&hl=en,none,none,none,none
2381,C,Stahl Construction,"Hopkinton, MA",(508) 561-4699,"6 Marshall Ave, Hopkinton, MA 01748",https://www.google.com/maps/place/?q=place_id:ChIJAQA8cSJ05IkRaDJUHaQ9uK4&hl=en,none,none,none,none
2382,C,Deon Design Kitchen & Bath,"Little Ferry, NJ",(201) 561-3017,"204 Main St, Little Ferry, NJ 07643",https://www.google.com/maps/place/?q=place_id:ChIJ5bnkBK_5wokR0dev1CLbd_o&hl=en,none,none,none,none
2383,C,Colombara's Cabinet & Mill,"Woodland, CA",(530) 662-2665,"421 4th St, Woodland, CA 95695",https://www.google.com/maps/place/?q=place_id:ChIJD9TkZ-HQhIARAeAAomlaKG0&hl=en,none,none,none,none
```
