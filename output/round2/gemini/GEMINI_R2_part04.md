# Round 2 Gemini file, part 4 of 6 (rows 301 to 400)

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
301,All City Renovations,"4890 E 49th St, Cuyahoga Heights, OH 44125, United States",+12163188327,https://www.google.com/maps/place/?q=place_id:ChIJubbMM2-Y8y4RwGIguoj0hYA&hl=en,none
302,EK Tile and Floor Masters,"649 Old Hwy 8, St Paul, MN 55112, United States",+16127884609,https://www.google.com/maps/place/?q=place_id:ChIJ0QeLwmgvs1IR8LJQ-QdqP0k&hl=en,none
303,Crincoli Kitchens,"160 Spring St, Elizabeth, NJ 07201, United States",+19083529312,https://www.google.com/maps/place/?q=place_id:ChIJUxbw0FlNwokRj14E-RQJKBU&hl=en,none
304,Wolfson Construction,"204 W Cedar Ave, Oaklyn, NJ 08107, United States",+18569523700,https://www.google.com/maps/place/?q=place_id:ChIJ6WG2w9zPxokRkx8Ou8aGDf4&hl=en,none
305,All About Kitchen and Bathroom remodel,,+17323767878,https://www.google.com/maps/place/?q=place_id:ChIJt_V8lH61w4kRRJG9bPgfH8Y&hl=en,none
306,Morris Finishing Company LLC,"549 E Main St, Dublin, VA 24084, United States",+15406740079,https://www.google.com/maps/place/?q=place_id:ChIJeambtNbkTYgRSlJ7CU3rEOE&hl=en,none
307,First Class Concept Design & Remodel,,+13522879262,https://www.google.com/maps/place/?q=place_id:ChIJeRASRSmss6wRfa3ZInzkDok&hl=en,none
308,Kitchen Remodel Denver,,+17207261820,https://www.google.com/maps/place/?q=place_id:ChIJIX98McV4bIcR7LGjEUCsgZQ&hl=en,none
309,B&M Contractors,,+14698263636,https://www.google.com/maps/place/?q=place_id:ChIJZzmkEjAlTIYRBiXnpEKeGsw&hl=en,none
310,Home and Space Contracting,,+18562301419,https://www.google.com/maps/place/?q=place_id:ChIJy7uIRmWvZUARdyZcyzASaPo&hl=en,none
311,Renew Space Remodeling,"2489 Industrial Pkwy W, Hayward, CA 94545, United States",+13412343035,https://www.google.com/maps/place/?q=place_id:ChIJC0xSqJeXj4ARsQNAqJJUVBo&hl=en,none
312,Morenos Custom Cabinets,"17919 Baldwin St #102, Madera, CA 93638, United States",+15594162084,https://www.google.com/maps/place/?q=place_id:ChIJO-mJqZcJlIAR-r36MrwWq6I&hl=en,none
313,We Do Home Repair & Renovation,,+13238002331,https://www.google.com/maps/place/?q=place_id:ChIJLci4hv3FwoARqU6IvPNr4Ss&hl=en,none
314,Independent flooring& Stone,"1147 Don Carlos Ct, San Jacinto, CA 92582, United States",+19514734152,https://www.google.com/maps/place/?q=place_id:ChIJR_io6Jxo24ARYxcVXKr-r3c&hl=en,none
315,Carrara Kitchen Countertops,"729 Farm Rd Ste H, Marlborough, MA 01752, United States",+15085795857,https://www.google.com/maps/place/?q=place_id:ChIJL8mIqzjzAWMRtR03Xa9GQNA&hl=en,none
316,Builders Direct,"757 W Broad St, Hazleton, PA 18201, United States",+15705011133,https://www.google.com/maps/place/?q=place_id:ChIJ-c9sD3SkxYkR5sbrh7GsFrY&hl=en,none
317,Masters Kitchen and Flooring,"2420 Vince Rd, Nicholasville, KY 40356, United States",+18598130727,https://www.google.com/maps/place/?q=place_id:ChIJMwLeaZFfQogR8BO23Z6F1VM&hl=en,none
318,Absolute Home Solutions LLC,"Mauldin, SC 29662, United States",+18647042678,https://www.google.com/maps/place/?q=place_id:ChIJ1Zk-oNklWIgRB45U02jzN6o&hl=en,none
319,JGM Construction & Remodeling LLC,"3826 Bay Club Cir Unit 204, Kissimmee, FL 34741, United States",+14077472700,https://www.google.com/maps/place/?q=place_id:ChIJ4_SVPZuD3YgRYzRr_SRXZ6w&hl=en,none
320,Aqua Remodeling LLC,,+17542485034,https://www.google.com/maps/place/?q=place_id:ChIJC5ddamZuL20ROTRb6sy1rZ8&hl=en,none
321,Hopkins Renovation & Design,,+14045639716,https://www.google.com/maps/place/?q=place_id:ChIJo6QFhIAf9YgR9gFj9By10_E&hl=en,none
322,"Better Edge Tile & Remodeling, LLC","8371 Norwood Ln N, Maple Grove, MN 55369, United States",+16129783569,https://www.google.com/maps/place/?q=place_id:ChIJOyTuFjw6s1IR2sLgGdQgy0M&hl=en,none
323,Mass Remodeling,"Pratt St, Mansfield, MA 02048, United States",+17742197880,https://www.google.com/maps/place/?q=place_id:ChIJIcFeh19j5IkROxDQhWt7z1A&hl=en,none
324,da silva tile installation & Design Inc,"143 Pleasant St, Rockland, MA 02370, United States",+17815885390,https://www.google.com/maps/place/?q=place_id:ChIJwzjFKI9y5IkRdDXFSSd4exs&hl=en,none
325,Arnold Improvements LLC,"8 Faith Dr, Vernon, CT 06066, United States",+18608726226,https://www.google.com/maps/place/?q=place_id:ChIJxan55Qr35okRncfsf59apYI&hl=en,none
326,Continental Wood and Stone Company,"919 Grove St, Defiance, OH 43512, United States",+14197899765,https://www.google.com/maps/place/?q=place_id:ChIJRd0cVpHRPYgRHy6row9OrAE&hl=en,none
327,Tile Decor LLC,"21 King St, Haledon, NJ 07508, United States",+19294240737,https://www.google.com/maps/place/?q=place_id:ChIJS8eNGfX9wokR_kW6m2QC0RE&hl=en,none
328,DREAM KITCHEN SOLUTION,,+18184545063,https://www.google.com/maps/place/?q=place_id:ChIJBzkFedjqtKURIWvbKAbC7CQ&hl=en,none
329,Titan Repair LLC,"2515 Poly Dr, Billings, MT 59102, United States",+14066900987,https://www.google.com/maps/place/?q=place_id:ChIJny8Poox8SFMRrIi_Vw3LB5Y&hl=en,none
330,Mancebo Home Renovations LLC,,+19542263522,https://www.google.com/maps/place/?q=place_id:ChIJGWQMZWGwFwAR5nl4o2ZkUpA&hl=en,none
331,Aesthetics Cabinetry LLC,"1510 Old Daytona Cir, DeLand, FL 32724, United States",+13863202806,https://www.google.com/maps/place/?q=place_id:ChIJxVlofXEd54gROjGwg0wJJA0&hl=en,none
332,San Marcos Tile & Flooring,,+15128319190,https://www.google.com/maps/place/?q=place_id:ChIJrY9Y3zipXIYRdd7nsRUgqSg&hl=en,none
333,JP Contractors | Tulsa Kitchen & Bathroom Remodeling,"10061 E 52nd St, Tulsa, OK 74146, United States",+19186009162,https://www.google.com/maps/place/?q=place_id:ChIJby_FQhuNtocRI1DYhCzV47w&hl=en,none
334,Bath Remodeling Home Contractor G&S Construction,"2041 Gladstone St, Glendora, CA 91740, United States",+16265362959,https://www.google.com/maps/place/?q=place_id:ChIJTyei5Esvw4ARJxWl6-N8Yn4&hl=en,none
335,Exquisite Designs Kitchen and Bath INC.,"13060 SE County Hwy 484, Belleview, FL 34420, United States",+13522034812,https://www.google.com/maps/place/?q=place_id:ChIJhzbp4kfQ54gRZ1-DXfcUnaU&hl=en,none
336,CSContractingINC.,,+17039966238,https://www.google.com/maps/place/?q=place_id:ChIJyUWzwoIEr6cRXUNh2b_vKdA&hl=en,none
337,Carl's Renovations,,+13212316733,https://www.google.com/maps/place/?q=place_id:ChIJc7s63qxk54gRITxNezJZDlo&hl=en,none
338,Ruschke Builders,,+19892250801,https://www.google.com/maps/place/?q=place_id:ChIJD_wfs_HVI4gRlyD-_844owc&hl=en,none
339,A&O Wood Design LLC,"216 Mitchell St, Clovis, NM 88101, United States",+15757495657,https://www.google.com/maps/place/?q=place_id:ChIJPz3jW_DfAocRiwU3rt5I8Bo&hl=en,none
340,Los Álvarez y Reyes Floor Service,,+19728765474,https://www.google.com/maps/place/?q=place_id:ChIJ79FxlQg-GqkRHLJqP5SDV1Q&hl=en,none
341,Matt's Home Solutions LLC (Matthew Pyles),"120 Reid Cir, Paducah, KY 42003, United States",+12703492054,https://www.google.com/maps/place/?q=place_id:ChIJ4zDp3EYSXYMRLraRtlqwBz0&hl=en,none
342,Latino Carpentry & Finish,"12101 NW 98th Ave Unit 4, Hialeah Gardens, FL 33018, United States",+17866636894,https://www.google.com/maps/place/?q=place_id:ChIJ54OPxE-72YgRDBk78rNOgtQ&hl=en,none
343,Pro Carpentry,"8521 Mosley Rd Unit 5, Houston, TX 77075, United States",+17138758313,https://www.google.com/maps/place/?q=place_id:ChIJRV5yzxCRQIYRtUbVSmSY1Uo&hl=en,none
344,Sans Construction and Design: Remodeling,,+19492356540,https://www.google.com/maps/place/?q=place_id:ChIJr45CNAzp3IARvg2ap8j6U70&hl=en,none
345,V&M Granite and Remodeling LLC,"2741 US-175 Frontage Rd, Seagoville, TX 75159, United States",+12149741515,https://www.google.com/maps/place/?q=place_id:ChIJu0L7IQm7ToYRYF9Wp0pDqhs&hl=en,none
346,M&R Tile & Remodel,"103 S 13th St, Santa Paula, CA 93060, United States",+18056602094,https://www.google.com/maps/place/?q=place_id:ChIJ08d9WIW16YARM3L3PtV2Ksg&hl=en,none
347,CK Tile and Home Repair LLC,"6530 57th Ave N, Minneapolis, MN 55428, United States",+19523567295,https://www.google.com/maps/place/?q=place_id:ChIJpfecVL83s1IRjPur556CnvQ&hl=en,none
348,Flavor Point Kitchen Remodeling,"2034 Ravoli Dr, Oxnard, CA 93035, United States",+18054579990,https://www.google.com/maps/place/?q=place_id:ChIJ9bgP2ENP6IARKwG1BcBPi-E&hl=en,none
349,JH Remodeling & Painting,,+15756404607,https://www.google.com/maps/place/?q=place_id:ChIJKyzDtHg93oYR49LwSOpIIiA&hl=en,none
350,Reackom Remodeling,"89 Orchard, Irvine, CA 92618, United States",+19496125060,https://www.google.com/maps/place/?q=place_id:ChIJjdQRHorxBYcREZ6TOZD71rU&hl=en,none
351,Patton Family Remodeling llc,"308 10th St, Crystal City, MO 63019, United States",+13146205172,https://www.google.com/maps/place/?q=place_id:ChIJn7LNRoHv2IcRlOTNNyU-weU&hl=en,none
352,Legacy Countertops & More,"1925 Gause Blvd W, Slidell, LA 70460, United States",+19852018588,https://www.google.com/maps/place/?q=place_id:ChIJa-4dE3HlnYgRwEE_LCwA5Do&hl=en,none
353,Gravitas Services,"200 Edsel Dr, Richmond Hill, GA 31324, United States",+19127304038,https://www.google.com/maps/place/?q=place_id:ChIJA79n_BUP-4gRO9ldCuuZp94&hl=en,none
354,Victor Smith's Construction,,+19524124147,https://www.google.com/maps/place/?q=place_id:ChIJBw-FOQ9o7qMRnlNfDRC5jxE&hl=en,none
355,Creative Tile and Remodeling LLC,,+18163372374,https://www.google.com/maps/place/?q=place_id:ChIJQVGpdo75wIcRTnwma3-AUk8&hl=en,none
356,DMP Remodels,,+17084151719,https://www.google.com/maps/place/?q=place_id:ChIJxbx5VKWOgaoRcAZF2fVGpuI&hl=en,none
357,Ronghi Construction LLC,"500 E Marshall Rd, McDonald, OH 44437, United States",+13305539185,https://www.google.com/maps/place/?q=place_id:ChIJrfiL9vznM4gRGFU5SN3ztug&hl=en,none
358,Giovannis Design and Install Group,,+19082444259,https://www.google.com/maps/place/?q=place_id:ChIJo5nbmJKtw4kRqAAelBvgOv0&hl=en,none
359,Bitsbrij,"7237 Marcy St Ste 4, Norfolk, VA 23505, United States",+17573240688,https://www.google.com/maps/place/?q=place_id:ChIJPcYZSIqZuokRkaFUa5yUPa4&hl=en,none
360,Kitchen Cabinet Refacing Specialists,,+19544941130,https://www.google.com/maps/place/?q=place_id:ChIJVVVVVWkA2YgR8Vh3HznvG2g&hl=en,none
361,Texas Stone Countertops & Services LLC,"7824 FM917, Alvarado, TX 76009, United States",+16829702981,https://www.google.com/maps/place/?q=place_id:ChIJ4z5T3mtvToYRFdoDsulpnwg&hl=en,none
362,Grace Remodeling & Construction,,+15124971529,https://www.google.com/maps/place/?q=place_id:ChIJ6blXZxXJRIYR_dkU3RB5q-A&hl=en,none
363,HomePride Bath of Grand Junction,,+19703874248,https://www.google.com/maps/place/?q=place_id:ChIJ8YQ-_HAdR4cRoCKcu6rYftg&hl=en,none
364,DJS Home Improvement - Miranda Property Service,,+19784917315,https://www.google.com/maps/place/?q=place_id:ChIJoX3pQm3pxqARrdd6d1wmcTM&hl=en,none
365,EG Custom Countertops LLC,"1187 East Ave, Cedartown, GA 30125, United States",+16789017995,https://www.google.com/maps/place/?q=place_id:ChIJLVdjco7BiogRDmYLqttY7LU&hl=en,none
366,Springbok Remodeling,"Blue Ridge, Comfort, TX 78013, United States",+18304460095,https://www.google.com/maps/place/?q=place_id:ChIJs4WIHex-LW4RA2Sc_8DmGq8&hl=en,none
367,Daily Life Kitchen Remodeling,"22162 Barbacoa Dr, Santa Clarita, CA 91350, United States",+16616698376,https://www.google.com/maps/place/?q=place_id:ChIJs4vfu9OHwoAR2me2_T7Q7lA&hl=en,none
368,"Christians Remodeling, LLC","Avondale Ct, Jeffersonville, IN 47130, United States",+15024340521,https://www.google.com/maps/place/?q=place_id:ChIJz32sMM2qY4YRvI47jhUC_E0&hl=en,none
369,Knighton Custom Kitchen and Bath LLC,,+13522199773,https://www.google.com/maps/place/?q=place_id:ChIJP8mmr_3SAC8RuEsCjCdhne8&hl=en,none
370,"Natural Wonders Marble & Granite, Inc.","2713 OK-37, Tuttle, OK 73089, United States",+14053819796,https://www.google.com/maps/place/?q=place_id:ChIJAykoPGt1socRGxWUWH3PIG4&hl=en,none
371,"RS Construction Solutions-kitchen,bathroom remodeler/excavation","3871 Saranac Dr, Sharpsville, PA 16150, United States",+17244563396,https://www.google.com/maps/place/?q=place_id:ChIJccZaGbfQEqIR-QkEnIpAc60&hl=en,none
372,Daxa Cabinetry LLC,,+13529887800,https://www.google.com/maps/place/?q=place_id:ChIJaX0_3zIcKiQR_zpdxFJBp-A&hl=en,https://linktr.ee/daxacabinetry https://linktr.ee/daxacabinetry
373,Just Bathrooms Remodeling Inc,"763 Marshall Way N, Layton, UT 84041, United States",+18018829718,https://www.google.com/maps/place/?q=place_id:ChIJH2l-PgIDU4cRcdWemRzrBtA&hl=en,http://www.facebook.com/jbremodelings/ http://www.facebook.com/jbremodelings/
374,Best Kitchen,"34-15 Broadway, Fair Lawn, NJ 07410, United States",+12017736412,https://www.google.com/maps/place/?q=place_id:ChIJOe0pRp_7wokRN1CorN4zJZc&hl=en,https://instagram.com/bestkitchen_nj?igshid=OGQ5ZDc2ODk2ZA== https://instagram.com/bestkitchen_nj?igshid=OGQ5ZDc2ODk2ZA==
375,Elite Home Renovations,,,https://www.google.com/maps/place/?q=place_id:ChIJKf0M0raRf4gRo0sqMsvakIo&hl=en,https://www.facebook.com/Elite-Home-Renovations-103118754840854/ https://www.facebook.com/Elite-Home-Renovations-103118754840854/
376,Elevation Renovation,,+18015109993,https://www.google.com/maps/place/?q=place_id:ChIJC2V5cPS73KsR9D6EJxcR3iU&hl=en,https://www.instagram.com/elevation.renovation/ https://www.instagram.com/elevation.renovation/
377,The Expert Touch,"1021 NJ-37 Unit D, Toms River, NJ 08755, United States",+17328206720,https://www.google.com/maps/place/?q=place_id:ChIJk-_1sBt2wYkRxBE8cFc8Z0A&hl=en,https://www.facebook.com/people/The-Expert-Touch/100057405493125/ https://www.facebook.com/people/The-Expert-Touch/100057405493125/
378,Mr. Odd Job,,+13344751000,https://www.google.com/maps/place/?q=place_id:ChIJjYvuQX1IUIcRX6Xc1SbHqWA&hl=en,http://www.facebook.com/mroddjobllc http://www.facebook.com/mroddjobllc
379,"Greeson Cabinets Custom Cabinetry, LLC","5961 State Hwy 49, Burlington, NC 27215, United States",+13363808458,https://www.google.com/maps/place/?q=place_id:ChIJI4QJY_ktU4gRpINrTnXYyGs&hl=en,https://www.facebook.com/greesoncabinetsinc?mibextid=LQQJ4d https://www.facebook.com/greesoncabinetsinc?mibextid=LQQJ4d
380,Kitchen Cabinet and Countertop Factory,"423 Bergen Blvd, Palisades Park, NJ 07650, United States",+12019064062,https://www.google.com/maps/place/?q=place_id:ChIJ52Ktfqn3wokRqVSQaNU4aDw&hl=en,https://www.instagram.com/kitchen.cabinet.factory/ https://www.instagram.com/kitchen.cabinet.factory/
381,Celebrity Appliance Contractors LLC,,+19734028484,https://www.google.com/maps/place/?q=place_id:ChIJQRLkc318noERzfW0YcuOOpk&hl=en,https://www.instagram.com/celebrityappliances/ https://www.instagram.com/celebrityappliances/
382,By One Bathroom Renovations,"940 Carter Rd, Winter Garden, FL 34787, United States",+14075055625,https://www.google.com/maps/place/?q=place_id:ChIJWTvafkkrX2kRWBAUcyf6yLw&hl=en,https://www.instagram.com/byonebathrooms/ https://www.instagram.com/byonebathrooms/
383,PTC Remodeling & Construction,,+14695125805,https://www.google.com/maps/place/?q=place_id:ChIJ3YoHc2Kfa0sRo0OEyd-DFjg&hl=en,http://linktr.ee/ptcllc http://linktr.ee/ptcllc
384,Tile Jawn Bathroom Remodeling,"1151 Callowhill St, Phoenixville, PA 19460, United States",+14843028265,https://www.google.com/maps/place/?q=place_id:ChIJV8FyA5lUxWQRYrE-SFxb1L8&hl=en,http://www.instagram.com/tilejawn http://www.instagram.com/tilejawn
385,Pick a color remodeling,,+19547707651,https://www.google.com/maps/place/?q=place_id:ChIJY9k3Py8J2YgRJ45ciMk585U&hl=en,http://www.instagram.com/remodelingwithcolor http://www.instagram.com/remodelingwithcolor
386,Adriani Brothers Full Service Remodeling/Kitchen & Bath Showroom,"40845 Merchants Ln Unit 240-10B, Leonardtown, MD 20650, United States",+12403094200,https://www.google.com/maps/place/?q=place_id:ChIJM5cTxgppt4kRxJcXhsBbfDk&hl=en,http://www.facebook.com/adrianibrothersconstruction http://www.facebook.com/adrianibrothersconstruction
387,Lakeside Stone,"34470 US-280, Childersburg, AL 35044, United States",+12563780606,https://www.google.com/maps/place/?q=place_id:ChIJXSzfzjpaiYgRTzS9tO-q66Y&hl=en,https://www.facebook.com/LakesideStoneGranite https://www.facebook.com/LakesideStoneGranite
388,Elite Remodeling And Construction Llc,,+19413341837,https://www.google.com/maps/place/?q=place_id:ChIJ_YaLYS5zdUwR7gwOaOoZmgo&hl=en,none
389,Skeya's Flooring and Home Improvements,"1006 Airport Rd, Hot Springs, AR 71913, United States",,https://www.google.com/maps/place/?q=place_id:ChIJH6wiT77VzIcRfH4qm07X_KA&hl=en,none
390,Creative Surfaces & Design LLC.,"2257 W 875 S, Syracuse, UT 84075, United States",+18015404281,https://www.google.com/maps/place/?q=place_id:ChIJ7T9nkPsbU4cR97TlbwL8E2w&hl=en,none
391,Texas Pro Design & Remodeling LLC,,+14698550765,https://www.google.com/maps/place/?q=place_id:ChIJb6odj3CJToYRbEcp1WxwOGs&hl=en,none
392,Precision Craft Woodworks LLC,"7723 Colquitt Rd, Terrell, TX 75160, United States",+19728721708,https://www.google.com/maps/place/?q=place_id:ChIJyZc64alTSYYR1wBu9DR_LRg&hl=en,none
393,THE THREE BROTHERS GENERAL REMODELING,"2609 S Front St, Angleton, TX 77515, United States",+18326569041,https://www.google.com/maps/place/?q=place_id:ChIJ-5suwqJdQIYRVTnp_swBAt8&hl=en,none
394,Greacen Home Repair and Remodeling,,+13157065591,https://www.google.com/maps/place/?q=place_id:ChIJ5yDiQbmAZ6wRDyjH4yk7ni8&hl=en,none
395,AL Renovation | Bathroom & Kitchen Remodelers,,+13602418034,https://www.google.com/maps/place/?q=place_id:ChIJU_MRHqIZeY4RFcu9RXJMm34&hl=en,none
396,Kitchen Remodel,,+12533322361,https://www.google.com/maps/place/?q=place_id:ChIJfWA_8Pb0DSgRr5ZpA9sQ71w&hl=en,none
397,A1 Tiled Customs & Remodeling,,+15093672193,https://www.google.com/maps/place/?q=place_id:ChIJA5TOa5DjEogRqlMDC0jneVg&hl=en,none
398,Platt Painting and Renovations LLC.,,+19194187601,https://www.google.com/maps/place/?q=place_id:ChIJCcbaLJnErIkR3QJJVg01Hok&hl=en,none
399,The Bath and Kitchen Connection,"11976 Dorsett Rd, Maryland Heights, MO 63043, United States",+13145282270,https://www.google.com/maps/place/?q=place_id:ChIJCY8Xmjkz34cRGij2MmvkgEQ&hl=en,none
400,DLA SERVICES REPAIR AND REMODELING,,+12482705066,https://www.google.com/maps/place/?q=place_id:ChIJVd7Bh56WqkcRzzXrpWImL2U&hl=en,none
```
