# Round 2 Gemini file, part 3 of 6 (rows 201 to 300)

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
201,Finish Right Construction LLC,"269 Jeffrey St, Long Branch, NJ 07740, United States",+17326901585,https://www.google.com/maps/place/?q=place_id:ChIJpzNDcB0lwokRMq7pjm4W8BA&hl=en,none
202,A.C.E Carpentry,,+15406993098,https://www.google.com/maps/place/?q=place_id:ChIJXWc4RC-_tIkRmdthhelSsNk&hl=en,none
203,Emerald Remodeling llc.,"7367 Cluster House Way, Gainesville, VA 20155, United States",+15715188026,https://www.google.com/maps/place/?q=place_id:ChIJHz0t9g1ntokRfyNu9c79XSE&hl=en,none
204,Smart Tile Solutions LLC,"1504 Inverness Rd, Lynn Haven, FL 32444, United States",+18502389867,https://www.google.com/maps/place/?q=place_id:ChIJ4XZmjk2Pk4gRApWOMPyJc1s&hl=en,none
205,GEOTOWER CONSTRUCTION LLC,"915 Tuliptree Ct, Mahwah, NJ 07430, United States",+19739316931,https://www.google.com/maps/place/?q=place_id:ChIJd9DrbWvhwokRrmtUhZdHY80&hl=en,none
206,A1 Granite & Quartz Inc.,"34 Midland Ave #1723, Wallington, NJ 07057, United States",+19738151170,https://www.google.com/maps/place/?q=place_id:ChIJT6QRpjz5wokROhFlw8o_iFw&hl=en,none
207,Zaprala Romano Remodeling,,+18569817569,https://www.google.com/maps/place/?q=place_id:ChIJv1NYTBvSxokRsh-IRDcNwlg&hl=en,none
208,Greencastle Construction llc,,+17176431923,https://www.google.com/maps/place/?q=place_id:ChIJ_dBqj_WPyYkR4riTjUghdqs&hl=en,none
209,A+ Bathroom & Kitchen Remodeling,"1441 Huntington Dr #179, South Pasadena, CA 91030, United States",+16262089396,https://www.google.com/maps/place/?q=place_id:ChIJT736moXFwoAR5hvn-uZtfpw&hl=en,none
210,INNOVATION Cabinetry Installs,,+19095454322,https://www.google.com/maps/place/?q=place_id:ChIJy58vzdDSgkgRV23ocMCkXVc&hl=en,none
211,Lee & Sons Remodeling LLC,"4655 N D St, San Bernardino, CA 92407, United States",+19092523592,https://www.google.com/maps/place/?q=place_id:ChIJcXuVqNFTw4ARJtOfe0qEjkY&hl=en,none
212,Filipe Custom Wood Work Inc,"1600 E Edgar Rd, Linden, NJ 07036, United States",+19084860033,https://www.google.com/maps/place/?q=place_id:ChIJP5Ffvc-yw4kR0SL09MDlrkE&hl=en,none
213,Capitol Countertops,"129 Paul Truitt Ln, Pearl, MS 39208, United States",+16016642008,https://www.google.com/maps/place/?q=place_id:ChIJNcQd6DgsKIYRiApHX66nMU4&hl=en,none
214,Floyd Remodeling/Custom Kitchen/Bath,,+13364910256,https://www.google.com/maps/place/?q=place_id:ChIJ12Ql4DmZU4gRJNDqpfijFcg&hl=en,none
215,Styles Kitchen Cabinets,"1939 Del Prado Blvd S # E, Cape Coral, FL 33990, United States",+12398952349,https://www.google.com/maps/place/?q=place_id:ChIJCdHgO4tB24gRolAIvqGEXzY&hl=en,none
216,Express Baths & Glass,"9141 Sauls Rd, Raleigh, NC 27603, United States",+19196614262,https://www.google.com/maps/place/?q=place_id:ChIJI0YjHQ1grIkRTxxd9MAwr3U&hl=en,none
217,Edward Walker Home Improvement,,+15673709583,https://www.google.com/maps/place/?q=place_id:ChIJJSvgft_rOYgRbuLWyC_jgOM&hl=en,none
218,"K & K REMODELING, INC.",,+12484760816,https://www.google.com/maps/place/?q=place_id:ChIJyVbpysmzJIgR_g7X6_tXrfg&hl=en,none
219,Coutino Refinishing Tubs & More,"2005 E Elm St, Griffith, IN 46319, United States",+12199802902,https://www.google.com/maps/place/?q=place_id:ChIJ6cKQ2_7mEYgRGHpuBI-tY9o&hl=en,none
220,Paul the Tileman LLC,,+17738770071,https://www.google.com/maps/place/?q=place_id:ChIJJzDPoCEXDogRHScmRhtwKMk&hl=en,none
221,Iron Rock Design & Build LTD.,"1202 75th St, Downers Grove, IL 60516, United States",+16304708410,https://www.google.com/maps/place/?q=place_id:ChIJPyZktHxFDogRqzqCdLG57zw&hl=en,none
222,JNG Floors And More LLC.,"1454 W US Hwy 30, Valparaiso, IN 46385, United States",+12196699782,https://www.google.com/maps/place/?q=place_id:ChIJE79iTGCREYgRQmcjp8kXoHM&hl=en,none
223,Casa Bella Contractors,"169 5th Ave, Hawthorne, NJ 07506, United States",+12019544275,https://www.google.com/maps/place/?q=place_id:ChIJhcIR4Vj8wokRC8Z6ooNPX9o&hl=en,none
224,LuxeBasin Bathroom Remodeler,"1008 Bell St, Pasadena, CA 91104, United States",+16266693164,https://www.google.com/maps/place/?q=place_id:ChIJM47wVhzDwoARQiNOpTQNvi4&hl=en,none
225,Jar Renovations LLC,,+13054982800,https://www.google.com/maps/place/?q=place_id:ChIJwXVwJlr6NioRlIYAOe2neIA&hl=en,none
226,Hand Remodeling,"1158 Josephine Ave, Prattville, AL 36066, United States",+13344404216,https://www.google.com/maps/place/?q=place_id:ChIJ0XhgEjxTFwARaOqbjYv6q8I&hl=en,none
227,K&B Tub restoration & Home Remodeling,,+17066153958,https://www.google.com/maps/place/?q=place_id:ChIJD40jxx7MjIgRY8Xh8IgS1pA&hl=en,none
228,TMX Improvements and Remodeling,,+12109925995,https://www.google.com/maps/place/?q=place_id:ChIJuwWTNPDzXIYRwxTVZ02rQTE&hl=en,none
229,Tepaco Applications & More,,+13176540832,https://www.google.com/maps/place/?q=place_id:ChIJa2K4aPOtbIgRA5t7Y9nZS2c&hl=en,none
230,Smith Rock Interiors LLC,"3602 Cherry Ave NE, Keizer, OR 97303, United States",+15039317461,https://www.google.com/maps/place/?q=place_id:ChIJxUd5XBr_v1QRNijMwYTShV0&hl=en,none
231,Rocky's Tile and Stone,"3411 E Dawson Rd, Sahuarita, AZ 85629, United States",+15203990934,https://www.google.com/maps/place/?q=place_id:ChIJrQtkPWCD1oYRiM6K_V4hylU&hl=en,none
232,EZR Building,,+12562845513,https://www.google.com/maps/place/?q=place_id:ChIJ-bYh4N2Fvi4RgEGS444pDc4&hl=en,none
233,Glamorous Kitchens & Bath,"147 E Oakwood St, Tarpon Springs, FL 34689, United States",+17279991959,https://www.google.com/maps/place/?q=place_id:ChIJPfimy93zwogREhO39NcMgwU&hl=en,none
234,TGG Stone Granite and Quartz,"23740 Hwy 6, Alvin, TX 77511, United States",+18323361062,https://www.google.com/maps/place/?q=place_id:ChIJlynY5vCPQIYREOhN_k9QDuQ&hl=en,none
235,West Coast Refinishing Tub LLC,"5101 Cyclamen Way, West Jordan, UT 84081, United States",+18012435569,https://www.google.com/maps/place/?q=place_id:ChIJ0WRp4KmJUocRn3UrZqwhJa8&hl=en,none
236,Modern Bath Company LLC,"708 Broadway #106, Tacoma, WA 98402, United States",+14253455194,https://www.google.com/maps/place/?q=place_id:ChIJmemzKBBfkVQR2TN8jY6UBWY&hl=en,none
237,Carlson Property Solutions LLC,"3751 Summerwood Way, Johnstown, CO 80534, United States",,https://www.google.com/maps/place/?q=place_id:ChIJ_____09JaYcRmP2WFvFdPIw&hl=en,none
238,Collin Bryan Construction,"4552 Sunbelt Dr, Addison, TX 75001, United States",+12149275263,https://www.google.com/maps/place/?q=place_id:ChIJX2QC1M2eToYRt3u3fst17RM&hl=en,none
239,Full House Kitchen Remodeling,"2001 Timberloch Pl Ste 409, The Woodlands, TX 77380, United States",+18328107817,https://www.google.com/maps/place/?q=place_id:ChIJVQ6-Y443R4YRtQ7jZtnEBeY&hl=en,none
240,Centex Bath,,+15125921203,https://www.google.com/maps/place/?q=place_id:ChIJMb1U5afTRIYRN5dBWSKynuQ&hl=en,none
241,RockStrong Handyman Services,"360 E 19th St, Merced, CA 95340, United States",+14085093485,https://www.google.com/maps/place/?q=place_id:ChIJh3fVdPJDkYARF2gDVB6I9Qo&hl=en,none
242,PNW Tilewerks,,+19712121230,https://www.google.com/maps/place/?q=place_id:ChIJUeFsUBbAi28RyQe9IQ5ec7Y&hl=en,none
243,Bathroom and Kitchen Remodeling Panorama City,"14650 Roscoe Blvd, Panorama City, CA 91402, United States",+18189606627,https://www.google.com/maps/place/?q=place_id:ChIJg2f6qFaWwoARhQz2P8ezHGA&hl=en,none
244,ToughTop Bathroom Remodeling,"200 W 99th St, Los Angeles, CA 90003, United States",+13234552415,https://www.google.com/maps/place/?q=place_id:ChIJG-ixhPrJwoARp5eSg4-0sLg&hl=en,none
245,JJ Tile and Stone,"76 Maple St, Stoneham, MA 02180, United States",+16174383116,https://www.google.com/maps/place/?q=place_id:ChIJiSzNeb3zsCMRcI5_dBt3VHM&hl=en,none
246,Creative Construction Services Inc,"240 S Broadway, Orcutt, CA 93455, United States",+18056946525,https://www.google.com/maps/place/?q=place_id:ChIJA8Dj5Ftt7IARemzvFOtrw9s&hl=en,none
247,Mr MrHandyDandy Bathroom Renovations,,,https://www.google.com/maps/place/?q=place_id:ChIJbdEpAW_19IgR5avZ8xL_uuA&hl=en,none
248,HomePride Bath,,+17207707944,https://www.google.com/maps/place/?q=place_id:ChIJDVb6lzyBa4cRUmDm_tafwiY&hl=en,none
249,Aser's home remodeling,,+17197226831,https://www.google.com/maps/place/?q=place_id:ChIJicWZnwJFE4cRw4B1EhnKIaM&hl=en,none
250,Cabinet Refresh,"6350 McDonough Dr NW Suite K, Norcross, GA 30093, United States",+16787089585,https://www.google.com/maps/place/?q=place_id:ChIJFdmr7ZOf9YgRwFBd9zkgN3c&hl=en,none
251,Do All Glaze and Remodel,,+17349340010,https://www.google.com/maps/place/?q=place_id:ChIJtz2Ho4Y_O4gRmwBdnQyRVeI&hl=en,none
252,"BSWB, Inc.","860 S Penn Ave, Sellersburg, IN 47172, United States",+18122465619,https://www.google.com/maps/place/?q=place_id:ChIJdzlaLz5waYgRHiDVAouQGGs&hl=en,none
253,Construction Pros,"7401 Metro Blvd Ste 500, Edina, MN 55439, United States",+16123965216,https://www.google.com/maps/place/?q=place_id:ChIJe73SYarV94cRoGyX2F-WN9w&hl=en,none
254,Hangliter Residential llc (OH),,+16142906430,https://www.google.com/maps/place/?q=place_id:ChIJEYHUpi71CygRbevsU7v3lX0&hl=en,https://www.instagram.com/hangliterresidential?igsh=MWZudDZibXA3N2Nq&utm_source=qr https://www.instagram.com/hangliterresidential?igsh=MWZudDZibXA3N2Nq&utm_source=qr
255,S&A Excellence Kitchen Remodeling,,+16572363305,https://www.google.com/maps/place/?q=place_id:ChIJlfg16sb6zUoRb1DfS5oeYNU&hl=en,none
256,"Essential Home Renovation, Llc","Council Bluffs, IA 51502, United States",+14023017142,https://www.google.com/maps/place/?q=place_id:ChIJ3XUc9miFk4cRj1Csrs_th8Y&hl=en,none
257,Miller Remodeling,,+15745961476,https://www.google.com/maps/place/?q=place_id:ChIJMzUkao2NFogRU4JYmJWoe9Y&hl=en,none
258,Granite Designs LLC,"59 Progress Ct, Moscow Mills, MO 63362, United States",+13146995770,https://www.google.com/maps/place/?q=place_id:ChIJGacEloXI3ocRNaW4N8IJ4Bg&hl=en,none
259,Lk Kitchen,"118 N Washington Ave, Dunellen, NJ 08812, United States",+19293749031,https://www.google.com/maps/place/?q=place_id:ChIJS4ndqOe5w4kRNaRjXkt-yTs&hl=en,none
260,on time kitchen cabinets,,+14045521655,https://www.google.com/maps/place/?q=place_id:ChIJAVrMyNmDF2MRJPgfVb3GEVE&hl=en,none
261,Dna remodels llc,,+13215570469,https://www.google.com/maps/place/?q=place_id:ChIJqQJDZwMVjQYRtAvKmbFOoZI&hl=en,none
262,Proficient Remodeling Services,,+12817619296,https://www.google.com/maps/place/?q=place_id:ChIJCUbXzvc8g0ARq9X805JJ76c&hl=en,none
263,IDF GRANITE,"4801A Ogeechee Rd, Garden City, GA 31405, United States",+19122385000,https://www.google.com/maps/place/?q=place_id:ChIJjfKyb6EK-4gRlQ0DJ_XHXB4&hl=en,https://www.facebook.com/share/19ot883vXb/ https://www.facebook.com/share/19ot883vXb/
264,Northshore Custom Tile and Flooring Inc.,,+19853179847,https://www.google.com/maps/place/?q=place_id:ChIJxwO_XoxdJ4YRdWvbEMmNmo8&hl=en,none
265,Top Dawg Remodel LLC,,+12134484035,https://www.google.com/maps/place/?q=place_id:ChIJ44mSRJ4VZwYRyaxw32LtNxc&hl=en,none
266,Pure Form Bathrooms,"29000 Hesperian Blvd, Hayward, CA 94545, United States",+13412343362,https://www.google.com/maps/place/?q=place_id:ChIJq0tm1ZGXj4ARE4IdmphObek&hl=en,none
267,Diamond Bathroom Remodeling,"2160 Connell Ave, Simi Valley, CA 93063, United States",+18205022226,https://www.google.com/maps/place/?q=place_id:ChIJT7mL2_Mp6IARyCYppp9jah4&hl=en,none
268,LCR Home Solutions LLC,"579 Jewel St, Lochbuie, CO 80603, United States",+17203501984,https://www.google.com/maps/place/?q=place_id:ChIJxch48Z-3gYERtOwPsQyA72A&hl=en,none
269,Prestige Custom Stone,"665 Madison St, Crown Point, IN 46307, United States",+12196618335,https://www.google.com/maps/place/?q=place_id:ChIJJdw31zLuEYgRLnYrmxHAqtA&hl=en,none
270,Dove Remodeling,"2275 Kings Hwy, Medford, OR 97501, United States",+15419513683,https://www.google.com/maps/place/?q=place_id:ChIJQVX5UV93z1QRjPjbsE9820s&hl=en,http://www.facebook.com/doveremodelingccb122274 http://www.facebook.com/doveremodelingccb122274
271,"Cutting Edge Remodeling, Llc","8136 Padgett Ave NE, Otsego, MN 55330, United States",+16129788465,https://www.google.com/maps/place/?q=place_id:ChIJgcmQVENps1IRzZWIxa4zT3c&hl=en,https://www.facebook.com/profile.php?id=100054286340960&mibextid=LQQJ4d https://www.facebook.com/profile.php?id=100054286340960&mibextid=LQQJ4d
272,Hord Home Improvements LLC,,+19199023749,https://www.google.com/maps/place/?q=place_id:ChIJy_WtfsfHQYgR8KklazTxeEs&hl=en,https://m.facebook.com/pages/category/Home-Improvement/Hord-Home-Improvements-109547397566279/ https://m.facebook.com/pages/category/Home-Improvement/Hord-Home-Improvements-109547397566279/
273,Phoenician Construction,,+16095016996,https://www.google.com/maps/place/?q=place_id:ChIJRy9Z_lsU6QMR2wyLD29VxzY&hl=en,https://www.facebook.com/Phoenicianconstruction?mibextid=ZbWKwL https://www.facebook.com/Phoenicianconstruction?mibextid=ZbWKwL
274,Queen City Renovation LLC,"10227 Connell Rd, Mint Hill, NC 28227, United States",+17049893052,https://www.google.com/maps/place/?q=place_id:ChIJ-c2S_FgXVIgRumc6GT6zVlU&hl=en,https://www.instagram.com/queencityrenovation?igsh=ZGY0OGc0c3RpcGhr https://www.instagram.com/queencityrenovation?igsh=ZGY0OGc0c3RpcGhr
275,DG Home Improvement LLC PA,,+12674232617,https://www.google.com/maps/place/?q=place_id:ChIJ4fIaWlVhUAQRMzcizUTipHA&hl=en,https://www.facebook.com/dghomeimprovementdg?mibextid=ZbWKwL https://www.facebook.com/dghomeimprovementdg?mibextid=ZbWKwL
276,Simplified Construction,"153 Sussex St, Old Forge, PA 18518, United States",+15709556258,https://www.google.com/maps/place/?q=place_id:ChIJOw34WOY4X4UR8BvxVscNTRk&hl=en,https://www.facebook.com/profile.php?id=61569885021803 https://www.facebook.com/profile.php?id=61569885021803
277,Floor & Remodeling 360 LLC,"725 Northlake Blvd, Altamonte Springs, FL 32701, United States",+14072237301,https://www.google.com/maps/place/?q=place_id:ChIJYZxn5mZn54gReD9VbjzXc-I&hl=en,https://www.facebook.com/profile.php?id=100044948150087 https://www.facebook.com/profile.php?id=100044948150087
278,Ridgeline Renovations,"18775 S Sonoita Hwy, Vail, AZ 85641, United States",+15203323123,https://www.google.com/maps/place/?q=place_id:ChIJm4Bc69JaOqURCQgugZaRSQM&hl=en,https://www.facebook.com/CodysHomeImprovements https://www.facebook.com/CodysHomeImprovements
279,Kinley Remodeling,"1411 Chelsea Ave, Erie, PA 16505, United States",+17243017571,https://www.google.com/maps/place/?q=place_id:ChIJ0VrJYiiDH2URDoefrZi6jjE&hl=en,https://www.facebook.com/profile.php?id=61553011979286&mibextid=ZbWKwL https://www.facebook.com/profile.php?id=61553011979286&mibextid=ZbWKwL
280,Twisted Tile,"201 Gavin Dr, Paragould, AR 72450, United States",+18704507947,https://www.google.com/maps/place/?q=place_id:ChIJeaOiDFfvWwQRJA6BkeUzhIQ&hl=en,https://www.facebook.com/profile.php?id=100057289195028&mibexthttps://www.facebook.com/profile.php?id=100057289195028&mibextid=ZbWKwLid=ZbWKwL https://www.facebook.com/profile.php?id=100057289195028&mibexthttps://www.facebook.com/profile.php?id=100057289195028&mibextid=ZbWKwLid=ZbWKwL
281,Design Surfaces,"660 Cooper St, Monroe, MI 48161, United States",+17346360750,https://www.google.com/maps/place/?q=place_id:ChIJ8f8TGo9vO4gR2cDvb5BEs9Y&hl=en,https://www.facebook.com/designsurfacesmonroe https://www.facebook.com/designsurfacesmonroe
282,Paragon Remodeling,,+13345216162,https://www.google.com/maps/place/?q=place_id:ChIJw4nAI9U184gR40CzemrmQWY&hl=en,http://facebook.com/RemodelingByParagon http://facebook.com/RemodelingByParagon
283,D&H Home Surfaces,,+19032387631,https://www.google.com/maps/place/?q=place_id:ChIJj_G5Zt5FNoYRyFIaqwfRfH4&hl=en,https://www.facebook.com/share/14hn2M17ZV/?mibextid=wwXIfr https://www.facebook.com/share/14hn2M17ZV/?mibextid=wwXIfr
284,Capital Interiors LLC,"2822 Co Rd 523 Unit G 03, Wildwood, FL 34785, United States",+18605766665,https://www.google.com/maps/place/?q=place_id:ChIJYwYxC9CTa0cRT5lZTDoXW84&hl=en,https://www.instagram.com/capital_interiors_llc https://www.instagram.com/capital_interiors_llc
285,M&A Remodeling & Restoration LLC,"1485 GA-34 Ste 2A, Newnan, GA 30265, United States",+16785715441,https://www.google.com/maps/place/?q=place_id:ChIJT0vxUMDr9IgRTPIVrRz-LWc&hl=en,none
286,MG Bathroom Renovations,,+18325569016,https://www.google.com/maps/place/?q=place_id:ChIJ02lkQTSVna4Rbv2fCbigaW0&hl=en,none
287,Siana Remodeling LLC,"28257 Gaylord Rd, Walker, LA 70785, United States",+12252889786,https://www.google.com/maps/place/?q=place_id:ChIJ9fkqFFSjJoYRVTIZAGL4QPQ&hl=en,none
288,Lovell Homes LLC,,+18016789455,https://www.google.com/maps/place/?q=place_id:ChIJfapO-uqu-ogRcVlOWTzN60w&hl=en,none
289,Dikici Design Consultants,"315 S Rogers St #4, Waxahachie, TX 75165, United States",+17607923509,https://www.google.com/maps/place/?q=place_id:ChIJxwKolp3ZTYYRbi15anXmwoo&hl=en,none
290,Green Country Marble,"600 W 158th St, Glenpool, OK 74033, United States",+19183226103,https://www.google.com/maps/place/?q=place_id:ChIJT04XqyWZtocR7BSdFJKMt4w&hl=en,none
291,G's Remodeling and Construction,,+12543348195,https://www.google.com/maps/place/?q=place_id:ChIJx1sWOTsVUYYRVAvjZAkgtWs&hl=en,none
292,Prospector Homes Remodeling (LLC),"2025 E Cortez Dr, Gilbert, AZ 85234, United States",,https://www.google.com/maps/place/?q=place_id:ChIJgyqrK9uuK4cRV9y_GqlOOA8&hl=en,none
293,Warehouse Interiors,"9357 Greenback Ln Unit 3, Orangevale, CA 95662, United States",+19165992473,https://www.google.com/maps/place/?q=place_id:ChIJL-i3MzDhmoAR_R_1A-hj6PQ&hl=en,none
294,BaumStone Customs,"1561 Eldridge Ave, Twin Falls, ID 83301, United States",+12084313427,https://www.google.com/maps/place/?q=place_id:ChIJzX6G6v-9rFQRgg-tbuC21DM&hl=en,none
295,Reliable Remodels,"9701 Elmore Rd, Anchorage, AK 99507, United States",+19076321029,https://www.google.com/maps/place/?q=place_id:ChIJp8xwoo6XyFYRjqsW56zIlqU&hl=en,none
296,My Kitchen Remodel and Design,"3370 Main St, Oakley, CA 94561, United States",+19254440801,https://www.google.com/maps/place/?q=place_id:ChIJYUdyEof_j4AR-FfbcyHau88&hl=en,none
297,Sicos Kitchen and Bath LLC,"5702 Industry Ln B-20, Frederick, MD 21704, United States",+12403571532,https://www.google.com/maps/place/?q=place_id:ChIJEcVdN4DZyYkRhofD-W-1C-M&hl=en,none
298,Korte Tile & Remodel,"108 Deerwood Dr, Hendersonville, TN 37075, United States",+16153305528,https://www.google.com/maps/place/?q=place_id:ChIJy5wZeGFJZIgRyWBIOL3ubAE&hl=en,none
299,Jocelyn Pankey Cabinetry & Design,"104 E 6th St, DeWitt, IA 52742, United States",+13092362235,https://www.google.com/maps/place/?q=place_id:ChIJKfhzaOxT4ocRn13Gj3xeMFw&hl=en,none
300,"Wall To Wall Tiling, LLC","19910 Dellwood Ave, Farmington, MN 55024, United States",+19522126060,https://www.google.com/maps/place/?q=place_id:ChIJbxqoK-w29ocRGChFx-qoPZc&hl=en,none
```
