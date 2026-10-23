# Round 2 Gemini file, part 1 of 6 (rows 1 to 100)

Paste the prompt into a NEW Gemini chat, then paste the table under it (or attach this file).

## Prompt
```
Use Google Search and Google Maps. For EVERY business in the attached table (kitchen and bathroom remodelers in the US that have no website), find:
- facebook_url: the business's own Facebook page (match it by name AND phone number or town; if unsure write UNKNOWN)
- instagram_url: the business's own Instagram profile (same matching rule)
- email: an email address the business itself publishes, on its Facebook page (Intro / About / contact info), Instagram bio, Google Business Profile, Yelp, BBB, Nextdoor, Houzz, Angi, Thumbtack, a chamber of commerce or licence listing, or a post. NEVER guess or build an address from a name.
- email_source_url and email_source_quote: the exact page where you saw the email and a short quote (20 words or fewer) that contains it
- owner_name: the owner's name if a page names them (Facebook intro, reviews that name the owner, licence record)
- facebook_followers, facebook_latest_post_date, instagram_followers, instagram_latest_post_date (copy what is shown; relative dates like "3w" exactly)
- photo_posts: roughly how many project photo posts the Facebook and Instagram accounts show (a number, or UNKNOWN)

Rules:
- Never guess. Unknown means UNKNOWN. Plain URLs only (no [text](url), no google.com redirect links).
- Do ALL rows. Do not stop to ask me. If a reply runs out of room, continue in the next reply until every row is done.
- Best: put all rows into ONE table and use "Export to Sheets" so I can download a CSV.

Output: CSV only, no commentary, with exactly this header (keep the row number from the table on every line):
row,facebook_url,instagram_url,email,email_source_url,email_source_quote,owner_name,facebook_followers,facebook_latest_post_date,instagram_followers,instagram_latest_post_date,photo_posts
Put text containing a comma in double quotes.
```

## Businesses
```csv
row,business_name,address,phone,maps_url,known_social_links
1,Two Guys from Jersey FL,"1209 S Swinton Ave, Delray Beach, FL 33444, United States",+19452287304,https://www.google.com/maps/place/?q=place_id:ChIJx6jEO6rh2IgRx-uaOqXBjjk&hl=en,none
2,Category 1 Kitchen Remodeling LLC,,+17708715222,https://www.google.com/maps/place/?q=place_id:ChIJzwx2FFmR9YgRJTK0TIZMH0Y&hl=en,none
3,Prime Living Oklahoma City,"5606 N Rockwell Ave, Bethany, OK 73008, United States",+14054009644,https://www.google.com/maps/place/?q=place_id:ChIJiybMKXEPsocRqkC8U7do27E&hl=en,none
4,G Remodeling Services Llc,,+16822482703,https://www.google.com/maps/place/?q=place_id:ChIJX8ojzveJToYR2ddcxdh6pEs&hl=en,none
5,DFW BATH & SHOWER EXPERTS LLC,,+19725050032,https://www.google.com/maps/place/?q=place_id:ChIJffyRdR73Sy0RKnZSMkJlKZg&hl=en,none
6,Maverick Remodeling,"5730 Anita St, Dallas, TX 75206, United States",+12147364210,https://www.google.com/maps/place/?q=place_id:ChIJV6tLG2mfToYReOUQO8ofojA&hl=en,none
7,Tile of the Mountain LLC,,+18014724580,https://www.google.com/maps/place/?q=place_id:ChIJsxAvhhlqtAMRaZ-rw-ddFBM&hl=en,none
8,Farhad Designs Remodeling,"San Clemente, CA 92673, United States",+19494489009,https://www.google.com/maps/place/?q=place_id:ChIJ_df0iWLx3IARtg27bu7WMBY&hl=en,none
9,Red Beard Renovations,,+19075215596,https://www.google.com/maps/place/?q=place_id:ChIJqYMc_r_fyFYRpQuhX7TRfeQ&hl=en,none
10,Big Sky Bathroom & Kitchen,,+14069645116,https://www.google.com/maps/place/?q=place_id:ChIJ7zh40fjfXEURPv023DT0hPw&hl=en,none
11,Innerstone Marble & Granite LLC,,+15414693906,https://www.google.com/maps/place/?q=place_id:ChIJ09bM_zeg2lQRPQLLpUYopFo&hl=en,none
12,"Fit & Finish HPS,LLC",,+15618883381,https://www.google.com/maps/place/?q=place_id:ChIJ1dgYmjOaNUsRDng7_2Flf2M&hl=en,none
13,Keegan Consultants LLC,"4273 Lebanon Church Rd, Athens, GA 30607, United States",+17062969515,https://www.google.com/maps/place/?q=place_id:ChIJcf1l740N9ogR8XYoobnIluA&hl=en,none
14,"Integrity Home Remodeling, LLC",,+18123061988,https://www.google.com/maps/place/?q=place_id:ChIJ9zHH2702EK4RVgsYUbSet1c&hl=en,none
15,Jota Handyman Remodeling LLC,,+13125866495,https://www.google.com/maps/place/?q=place_id:ChIJtwjg8zJ6riIRmnl_ANJAtfk&hl=en,none
16,Elizabeth Kitchen & Granite LLC,"719 Livingston St, Elizabeth, NJ 07201, United States",+19086629512,https://www.google.com/maps/place/?q=place_id:ChIJe0AJP3lNwokRwXb3AJOuG6g&hl=en,none
17,"New Creation Kitchen, Bath and Flooring","800 Valley Plaza Ste 1, Johnson City, NY 13790, United States",+16072380366,https://www.google.com/maps/place/?q=place_id:ChIJJ-uP-2Hv2okR3mLeBfuCbUg&hl=en,none
18,Superior Tile,"12 Bittersweet Ln, Clifton Park, NY 12065, United States",+15185963276,https://www.google.com/maps/place/?q=place_id:ChIJSfjVW63MmUcRD3Gw5gKj-ko&hl=en,none
19,Floor 2 Ceiling tile & stone,"213 Neal St, West Point, GA 31833, United States",+14049148262,https://www.google.com/maps/place/?q=place_id:ChIJ8UgUqAQr9YgRnJ28Rxs41fI&hl=en,none
20,Team Worx Remodeling,"4595 Helena Moriah Rd, Rougemont, NC 27572, United States",+19193845147,https://www.google.com/maps/place/?q=place_id:ChIJq6omVH0QrYkR5SIJ8NyZowU&hl=en,https://www.youtube.com/watch?v=1I5n7K0jt5E
21,Best Flooring LLC,,+18433247301,https://www.google.com/maps/place/?q=place_id:ChIJm4knWM-J44kRz-ysjnUhrBc&hl=en,none
22,Murphy Kitchen and Bath Construction,"7 Rinehart Ln, Pottersville, NJ 07979, United States",+19085209722,https://www.google.com/maps/place/?q=place_id:ChIJ0yhsclGRw4kRrWXbP3UgAMM&hl=en,https://www.instagram.com/murphykitchenandbath?igsh=MXE3cXFjeXM4NGxoeg==&utm_source=qr https://www.instagram.com/murphykitchenandbath?igsh=MXE3cXFjeXM4NGxoeg==&utm_source=qr
23,Sami's Countertops LLC,"3988 Gulfway Dr, Port Arthur, TX 77642, United States",+14095480373,https://www.google.com/maps/place/?q=place_id:ChIJAz40Xly7PoYR1qwQwFw3-FA&hl=en,none
24,A Cut Above WoodWorks,,+12548134374,https://www.google.com/maps/place/?q=place_id:ChIJff4Ix1C-nGQRYd0HtfCNc54&hl=en,none
25,"T & R Contracting, LLC","314 Plantation Drive, Cinnaminson, NJ 08077, United States",+18566736548,https://www.google.com/maps/place/?q=place_id:ChIJkWMGtyjMxokR8gdbCkkAcVc&hl=en,none
26,"Blessed Remodeling Home Improvements, LLC",,+16318361186,https://www.google.com/maps/place/?q=place_id:ChIJn5boVEfJ2UkRTDjQO8qbGmw&hl=en,none
27,MCJ Kitchen And Bath,"466 Pompton Ave, Cedar Grove, NJ 07009, United States",+15512579059,https://www.google.com/maps/place/?q=place_id:ChIJ3aj-Cz4Bw4kRiexgfPmLm44&hl=en,none
28,Modern Wave Bathrooms,"1050 Forselles Way, Hayward, CA 94544, United States",+13412223443,https://www.google.com/maps/place/?q=place_id:ChIJj2LOiX6Vj4ARhNG3DjqPGPg&hl=en,none
29,Signature Bath Solutions,"4447 Alice Way, Union City, CA 94587, United States",+13412342966,https://www.google.com/maps/place/?q=place_id:ChIJeznhMDuVj4ARqnP0yzIbWg4&hl=en,none
30,Montco Handyman,"1529 Pine St, Norristown, PA 19401, United States",+14845347851,https://www.google.com/maps/place/?q=place_id:ChIJnf84z969xokRR9-phgkdaJI&hl=en,none
31,Nexgen Flooring LLC.,"501 Wilson St, Statesville, NC 28677, United States",+17049576985,https://www.google.com/maps/place/?q=place_id:ChIJHWg9PTmpVogRQ0aLNZTHxAs&hl=en,none
32,123 Construction & Remodeling,,+18139665454,https://www.google.com/maps/place/?q=place_id:ChIJe8bOd56e4W4RK0HfvPmWvng&hl=en,none
33,Creative Additions Plus,,+16126855314,https://www.google.com/maps/place/?q=place_id:ChIJDQG1UPsXs1IRSHeiAQnvpsQ&hl=en,none
34,Prestige Painters & Remodeling,"3649 W 138th St, Cleveland, OH 44111, United States",+12165131610,https://www.google.com/maps/place/?q=place_id:ChIJzaf2HeDtMIgRk5vMF0TClRk&hl=en,none
35,New Era Builders INC.,,+15087822098,https://www.google.com/maps/place/?q=place_id:ChIJzcPOh1F35IkRP2F-9syc9Gw&hl=en,none
36,Dynasty Home Improvement LLC,"7A Windham Ave, Colchester, CT 06415, United States",+18607104602,https://www.google.com/maps/place/?q=place_id:ChIJD2cHR6pp5okRI-_s7du6UpA&hl=en,none
37,Stone Rosario,"4941 173rd St, Country Club Hills, IL 60478, United States",+17082502144,https://www.google.com/maps/place/?q=place_id:ChIJ695DLSUXDogRnVNzmT4qDRU&hl=en,none
38,"Jobak Home Improvement, LLC",,+12486060150,https://www.google.com/maps/place/?q=place_id:ChIJv6eI7U0bEw8R7Xnk6disLBk&hl=en,none
39,Pro Crafters,"393 Acorn Ave, Telford, PA 18969, United States",+12672451587,https://www.google.com/maps/place/?q=place_id:ChIJt5fgOIqhxokRt6Vx-drH4MQ&hl=en,none
40,New Life Home Improvements,"5006 Elm Ave, Fort Pierce, FL 34982, United States",+17863030559,https://www.google.com/maps/place/?q=place_id:ChIJy15awGLv3ogRlBEcBt65Rrc&hl=en,none
41,Granite Kingdom LLC,"2730 Mountain Industrial Blvd #101, Tucker, GA 30084, United States",+16785519555,https://www.google.com/maps/place/?q=place_id:ChIJ16EpPv6h9YgRLEWvrwYduyM&hl=en,none
42,VL Granite & Marble LLC,"1865 W Union Ave Ste J, Sheridan, CO 80110, United States",+13035917523,https://www.google.com/maps/place/?q=place_id:ChIJW-H0U6-Ba4cR6WfSqeIULMo&hl=en,none
43,C&B Flooring Llc & Granite kitchen cabinets,"5833 Jacksboro Hwy, Fort Worth, TX 76114, United States",+18176249595,https://www.google.com/maps/place/?q=place_id:ChIJy1RGR-90ToYRRiMurS_oYgw&hl=en,https://www.facebook.com/profile.php?id=61582195393551 https://www.facebook.com/profile.php?id=61582195393551
44,A French Handyman,"180 Glenn Ct, West Lafayette, IN 47906, United States",+17652366669,https://www.google.com/maps/place/?q=place_id:ChIJdRauMxExdYgRSmKTERh5Yc0&hl=en,none
45,Aguirre's Tile Services,"University Dr, Forney, TX 75126, United States",+12144072403,https://www.google.com/maps/place/?q=place_id:ChIJs6htyuysToYR9zeJVGiovUQ&hl=en,none
46,M+ Kitchen & Bathroom Remodeling,"5800 Hannum Ave #121, Culver City, CA 90230, United States",+14244784229,https://www.google.com/maps/place/?q=place_id:ChIJd64XS3m3woARD5TwO7oaLKc&hl=en,none
47,ERC Renovation LLC,,+18662540162,https://www.google.com/maps/place/?q=place_id:ChIJs51CkSuKn68RmlyNmUECS9c&hl=en,none
48,"Shoreline Marble & Tile, Inc.","3207 63rd St, Kenosha, WI 53142, United States",+12623080510,https://www.google.com/maps/place/?q=place_id:ChIJlar3MHZeBYgReJALoqVnCj0&hl=en,none
49,Martinez Stone Inc,"3007 NW Stallings Dr, Nacogdoches, TX 75964, United States",+19363295997,https://www.google.com/maps/place/?q=place_id:ChIJl73oUICLN4YReRPTliD6AP4&hl=en,none
50,FJ Remodeling,,,https://www.google.com/maps/place/?q=place_id:ChIJ67Far3obMKgR_InMD0D5ewg&hl=en,none
51,T. C. Rich,"1450 Georgia Ave Ste 6564, North Augusta, SC 29861, United States",+17062311589,https://www.google.com/maps/place/?q=place_id:ChIJEYiutsXN-YgRiqNrYwfSfjo&hl=en,none
52,3J GRANITE LLC,"726 Roanoke St, Salem, VA 24153, United States",+15405560927,https://www.google.com/maps/place/?q=place_id:ChIJO6bFbOQJTYgRHLX3G2fNFyA&hl=en,none
53,The Tile Pro's,,+13369957102,https://www.google.com/maps/place/?q=place_id:ChIJFYYNGXWxU4gR3DGr792aPYw&hl=en,none
54,Stone Koat Kreations LLC Epoxy Countertops & Floors,,+12254532353,https://www.google.com/maps/place/?q=place_id:ChIJXaHPeA-bJoYRaXooXaGqSOw&hl=en,none
55,Timeless Marble & Granite LLC,"14587 S 790 W, Bluffdale, UT 84065, United States",+18013499990,https://www.google.com/maps/place/?q=place_id:ChIJRSRf7oSBUocRtzPyg8OIEWE&hl=en,none
56,Designer Kitchen and Bath,"5238 Imogene St, Houston, TX 77096, United States",+17137247306,https://www.google.com/maps/place/?q=place_id:ChIJbxF9ShebXhQRTSm-Qlsaap8&hl=en,none
57,CasaCrew Remodeling,"505 Wild Pecan Lp, Mustang Ridge, TX 78610, United States",+15124134287,https://www.google.com/maps/place/?q=place_id:ChIJZ4CLmehqByERSFfuGJ4vGhE&hl=en,none
58,S&A Excellence Kitchen Remodeling,,+19498506793,https://www.google.com/maps/place/?q=place_id:ChIJh7STnCL7XasR2Dsv_NSYRRc&hl=en,none
59,BAB Construction LLC,"12870 E Idaho Dr, Aurora, CO 80012, United States",+17206877651,https://www.google.com/maps/place/?q=place_id:ChIJaccjaOB9bIcR4XlSnalF97Y&hl=en,none
60,"Simmons Home Remodeling Las Cruces | Kitchen and Bath | Drywall and Paint | Stucco, Fencing, Many Other Services",,+15756492981,https://www.google.com/maps/place/?q=place_id:ChIJZ5OlLx8W7YERwXCnCee5K3o&hl=en,none
61,Custombilt Counter Tops,"1822 Albany Ave, Waycross, GA 31503, United States",+19122835704,https://www.google.com/maps/place/?q=place_id:ChIJbTowhqn674gRhZrLYxQMw8g&hl=en,none
62,Raccoon Stone & Tile Works,"2347 GA-247CONN, Byron, GA 31008, United States",+14789562222,https://www.google.com/maps/place/?q=place_id:ChIJ-ZisyzXm84gRug4KD2uOJak&hl=en,none
63,New Style Tiles,,+17086980090,https://www.google.com/maps/place/?q=place_id:ChIJE_Pezpw9DogRpCnedN8M5w0&hl=en,none
64,Flooring and Granite By Silva,"600 S Denton Tap Rd #135, Coppell, TX 75019, United States",+12147832981,https://www.google.com/maps/place/?q=place_id:ChIJQ0qo2EImTIYRGVZAVj4mnNA&hl=en,none
65,The Grout Savior,"35 Washington Ave, Dumont, NJ 07628, United States",+12015981555,https://www.google.com/maps/place/?q=place_id:ChIJW1xdZDfwwokRhi_ParzPAaA&hl=en,none
66,Super Builders,,+17432412342,https://www.google.com/maps/place/?q=place_id:ChIJZ64eYHJRtAERxY_PSV5hvbc&hl=en,none
67,The Final Touch Design,,+18505886142,https://www.google.com/maps/place/?q=place_id:ChIJU6qvBv6Mk4gR9HaqXAKjlqI&hl=en,none
68,Zion Remodeling and Restoration,,+16303597020,https://www.google.com/maps/place/?q=place_id:ChIJKZGouLf_DogRQhYLRAz-UIQ&hl=en,none
69,McMichael Home Repair,,+13145685888,https://www.google.com/maps/place/?q=place_id:ChIJw8zFTsEr34cRhVzNQGrwRuk&hl=en,none
70,Grey Finishes,"9605 S 53rd Ave, Oak Lawn, IL 60453, United States",+18722169168,https://www.google.com/maps/place/?q=place_id:ChIJLz_IEvUnVwIRTlXbgVb0lSw&hl=en,none
71,Graphene Stone Home Repairs LLC,"4577 W 13th Ln, Hialeah, FL 33012, United States",,https://www.google.com/maps/place/?q=place_id:ChIJdRIkNHC72YgRJ1kQ0vX3vxk&hl=en,none
72,Elegant Stone Cabinet LLC,"7535 Old Shell Rd, Mobile, AL 36608, United States",+12513781855,https://www.google.com/maps/place/?q=place_id:ChIJhe599nOym4gRd3LyPY4Z9Hc&hl=en,none
73,"MAGIC HANDS HOME SERVICES,Corp.","304 SE 10th Ave Ste D, Pompano Beach, FL 33060, United States",+19547939808,https://www.google.com/maps/place/?q=place_id:ChIJg3O59zsD2YgRWm6U4HhxU6o&hl=en,none
74,Better Looks Home Renovations,,+15616629099,https://www.google.com/maps/place/?q=place_id:ChIJm5IOaH_S1CkRq2JTb1DjLX0&hl=en,none
75,True Custom Countertops,"100 N Edward Gary St Ste C, San Marcos, TX 78666, United States",+15128772734,https://www.google.com/maps/place/?q=place_id:ChIJJUEUFVCpXIYRMbuPq_NbhH8&hl=en,none
76,"White's Quality Homes and Remodeling, LLC",,+15738802488,https://www.google.com/maps/place/?q=place_id:ChIJpWJLneNF2IcRyEKTzsKcdZo&hl=en,none
77,Home Design & Luxury,"610 W Waters Ave B, Tampa, FL 33604, United States",+17867527604,https://www.google.com/maps/place/?q=place_id:ChIJwVUvtaPHwogR27xPDLSw0Kk&hl=en,none
78,Southerly Home Improvements,,+13024706740,https://www.google.com/maps/place/?q=place_id:ChIJ0-Px7GQ2dwkR1vhaJnF_i_k&hl=en,none
79,marcos custom designs,,+17325279166,https://www.google.com/maps/place/?q=place_id:ChIJ91jCskOhx28R3jw8jiaiYEU&hl=en,none
80,Windsor Kitchen & Bath - Kitchen Cabinets - Edison,"800 US-1, Edison, NJ 08817, United States",+17329855958,https://www.google.com/maps/place/?q=place_id:ChIJL39mnWrIw4kRnrdH_iEDb9E&hl=en,none
81,Roots & Risers Home Remodeling,,+15704811004,https://www.google.com/maps/place/?q=place_id:ChIJOYeUjHrCxYkRpmd0g0xWM3Q&hl=en,none
82,ILIRIA REMODELING,"Courtyards of 78th Avenue Shopping Center, W 159th St, Tinley Park, IL 60477, United States",+17086731671,https://www.google.com/maps/place/?q=place_id:ChIJTTGPgThExgYRWbCiMugmsiU&hl=en,none
83,Simply Rachael’s Creations LLC,"19262 Ogden St NW, Elk River, MN 55330, United States",+17633002920,https://www.google.com/maps/place/?q=place_id:ChIJcRGviT1vs1IRGOASY_DXoL8&hl=en,none
84,Jerusalem Construction Co,,,https://www.google.com/maps/place/?q=place_id:ChIJb63pa0jrMIgRxJyOCGlc2xE&hl=en,none
85,H & S Remodeling and Painting l.l.c.,,+16147951733,https://www.google.com/maps/place/?q=place_id:ChIJr5cZb17FOIgRJsFv7ab6LrU&hl=en,none
86,WOODEYE LLC,"278 E High St, Stayton, OR 97383, United States",+14583568185,https://www.google.com/maps/place/?q=place_id:ChIJZ-lXVzf1v1QR3eG-YiRVN8Y&hl=en,https://www.instagram.com/woodeye_woodworking?igsh=dXk3bzlibTdtaDJ1&utm_source=qr https://www.instagram.com/woodeye_woodworking?igsh=dXk3bzlibTdtaDJ1&utm_source=qr
87,B&H Kitchen Remodeling,,+15136590568,https://www.google.com/maps/place/?q=place_id:ChIJGRT4wATMVWQRf4VFVe9IVqk&hl=en,https://www.facebook.com/BHKITCHENREMODELING https://www.facebook.com/BHKITCHENREMODELING
88,S&M customs (home solutions),"1287 Nelson Dr, Brighton, TN 38011, United States",+19013154970,https://www.google.com/maps/place/?q=place_id:ChIJBwD-34QTf4gRKWmwl1UBNao&hl=en,http://facebook.com/SandMCustoms http://facebook.com/SandMCustoms
89,"Kapal Cabinets, Granite & Quartz","2025 N Minnesota Ave, Brownsville, TX 78521, United States",+19564610692,https://www.google.com/maps/place/?q=place_id:ChIJ0XA-rTC_b4YRDbH-L5b092s&hl=en,https://linktr.ee/kapal_industries https://linktr.ee/kapal_industries
90,Blankenberg flooring & more llc,,+18638779740,https://www.google.com/maps/place/?q=place_id:ChIJ5zvPJWtP4KQRAjIS6iLA7FA&hl=en,https://www.facebook.com/BlankenbergFlooringmorellc?mibextid=LQQJ4d https://www.facebook.com/BlankenbergFlooringmorellc?mibextid=LQQJ4d
91,Thomas TileWorks LLC,,+18653049792,https://www.google.com/maps/place/?q=place_id:ChIJCeDzU0NB1k0RQakSUWEc8so&hl=en,https://www.facebook.com/profile.php?id=61582438320918 https://www.facebook.com/profile.php?id=61582438320918
92,JMA Home Repair and Remodel LLC,,+13863349034,https://www.google.com/maps/place/?q=place_id:ChIJlTmuWvvOI6sRScz0QqhN36w&hl=en,http://facebook.com/JMAHomeRepairandRemodelLLC http://facebook.com/JMAHomeRepairandRemodelLLC
93,EM Woodwork & Tile - Bathroom Remodeling - Traverse City,,+12319205211,https://www.google.com/maps/place/?q=place_id:ChIJHTavdO65H4gRN2JN3pwTBzA&hl=en,https://www.facebook.com/emwoodworkandtile https://www.facebook.com/emwoodworkandtile
94,Modern Kitchen & Bath,"9079 County Rd 375, St Joseph, MO 64505, United States",+18166469246,https://www.google.com/maps/place/?q=place_id:ChIJKWTXdh4dwIcRWxMCBvY8ZK0&hl=en,https://www.facebook.com/modernrenovations4u https://www.facebook.com/modernrenovations4u
95,Danish Remodeling LLC,,+14702551899,https://www.google.com/maps/place/?q=place_id:ChIJP14dfs5P9YgRWQzZbziSFqg&hl=en,http://instagram.com/danishremodeling http://instagram.com/danishremodeling
96,Swartz Customs Remodeling,"16 Mirage Way, Miramar Beach, FL 32550, United States",+16789833652,https://www.google.com/maps/place/?q=place_id:ChIJtwVx3I_S5GcRFs-H1qcS7_E&hl=en,https://www.facebook.com/Swartzcustoms/ https://www.facebook.com/Swartzcustoms/
97,Dean's Custom Cabinets,"961 N Central City Rd, Joplin, MO 64801, United States",+14177824109,https://www.google.com/maps/place/?q=place_id:ChIJn_To8L9wyIcRhHb-Xab2uxo&hl=en,https://www.facebook.com/Deans-Custom-Cabinets-111935522154913/ https://www.facebook.com/Deans-Custom-Cabinets-111935522154913/
98,Fix Plus,"121 W Washington St, Minneola, FL 34715, United States",+13522424330,https://www.google.com/maps/place/?q=place_id:ChIJ3eg570SO54gRRkdCF036GFU&hl=en,none
99,RGV Remodeling & Construction Llc,"315 N Shary Rd Suit 1034, Mission, TX 78572, United States",+19563213279,https://www.google.com/maps/place/?q=place_id:ChIJ3RLpDZKnZYYRxfgzU2T0gt8&hl=en,none
100,"Logo Renovations, LLC","509 N Kansas Ave, Columbus, KS 66725, United States",+16204290740,https://www.google.com/maps/place/?q=place_id:ChIJSUcEi06id2MRm_7v6uPkfcU&hl=en,none
```
