# Round 2: Gemini task 2, part 08 of 17 (100 businesses, rows 1784 to 1883)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 1883: reply in that chat "Continue with
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
1784,C,Imperial Home Remodeling - Tile&Bathroom Remodel,"Citrus Heights, CA",(689) 202-9161,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJVX_IN4OmuCIRvqJyrmR6pMY&hl=en,none,none,none,none
1785,C,Shaffer Construction,"Salisbury, MD",(443) 859-5317,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbTjH5Wr9uIkRKO4mNrSDVq8&hl=en,none,none,none,none
1786,C,HSP Kitchen Remodel,"Lakewood, WA",(253) 364-7373,"14413 Union Ave SW A, Lakewood, WA 98498",https://www.google.com/maps/place/?q=place_id:ChIJxSURNjIHkVQRsfzHsxrvYmo&hl=en,none,none,none,none
1787,C,Total Upgrade & Remodeling,"Bloomingdale, IL",(630) 205-6254,"One Tiffany Pointe Ste 300, Bloomingdale, IL 60108",https://www.google.com/maps/place/?q=place_id:ChIJd72Y3fetD4gRNmMQclNl7oo&hl=en,none,none,none,none
1788,C,Porcelain Refinishing Company,"Redlands, CA",(909) 735-5151,"30631 3rd Ave, Redlands, CA 92374",https://www.google.com/maps/place/?q=place_id:ChIJAQDQAxZW24ARetNMUgmPTl4&hl=en,none,none,none,none
1789,C,Signature Cabinets LLC,"Florence, AL",(256) 764-1141,"3105 Northington Ct, Florence, AL 35630",https://www.google.com/maps/place/?q=place_id:ChIJTTNcU643fYgRhdtAWYsaGIQ&hl=en,none,none,none,none
1790,C,HO Remodel kitchen & bath,"Pomona, CA",(909) 344-6841,"568 N Towne Ave, Pomona, CA 91767",https://www.google.com/maps/place/?q=place_id:ChIJo9L-Tgotw4ARI2CA6YuVHLg&hl=en,none,none,none,none
1791,C,Guntersville Granite,"Albertville, AL",(256) 400-8389,"503 Glover St, Albertville, AL 35950",https://www.google.com/maps/place/?q=place_id:ChIJf2Z1TYUDiogRTyBLQQwFE6M&hl=en,none,none,none,none
1792,C,Top Shop,"Mountain Home, AR",(870) 492-4455,"118 Basswood Ln, Mountain Home, AR 72653",https://www.google.com/maps/place/?q=place_id:ChIJhxk2YyLb0YcRNCjAEwVP5Oo&hl=en,none,none,none,none
1793,C,MENDOZA CONSTRUCTION LIFE LLC,"Metairie, LA",(985) 778-9150,"116 Marguerite Rd, Metairie, LA 70003",https://www.google.com/maps/place/?q=place_id:ChIJ0xmN6iuxIIYRwi9xigS2dGY&hl=en,none,none,none,none
1794,C,iKitchen Inc,"Quincy, MA",(617) 481-7608,"271 Quincy Ave, Quincy, MA 02169",https://www.google.com/maps/place/?q=place_id:ChIJwXvDKRFj44kRlc0rijj1Ue4&hl=en,none,none,none,none
1795,C,MAAK construction LLC,"Hartsville, SC",(843) 858-8140,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ86Ga-zMFVKcRofyPHO6mDfs&hl=en,none,none,none,none
1796,C,HSP Bathroom Remodel Co.,"Federal Way, WA",(253) 321-1414,"1761 S 305th Pl Unit B, Federal Way, WA 98003",https://www.google.com/maps/place/?q=place_id:ChIJs-W2G6pXkFQR5iDVQVTaeUg&hl=en,none,none,none,none
1797,C,"Pmf Installers, Llc","Villa Rica, GA",(770) 480-6587,"430 Northstar Dr, Villa Rica, GA 30180",https://www.google.com/maps/place/?q=place_id:ChIJ2Y2tsjEu9YgRwdNj4x39QlI&hl=en,none,none,none,none
1798,C,Malone Construction of New Albany Ms.LLC,"New Albany, MS",(662) 316-4768,"1028 Co Rd 88, New Albany, MS 38652",https://www.google.com/maps/place/?q=place_id:ChIJm_1udtehgIgRSM2M-A0vRpU&hl=en,none,none,none,none
1799,C,UpHome Renovation,"McAllen, TX",(800) 470-3101,"7001 N 10th St Ste G3, McAllen, TX 78504",https://www.google.com/maps/place/?q=place_id:ChIJf9Cvwi13ZYYR3cXUCfZVN3k&hl=en,none,none,none,none
1800,C,Work Prime RP LLC - Home Remodel and Renovation,"Burlington, NJ",(856) 220-8261,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ2VGS9Fyt-a8RVk2WZoP1FUg&hl=en,none,none,none,none
1801,C,JMD General Construction LLC,"Monroe, OH",(513) 571-0713,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ17JaFLWCF6MRTf1ijaFmSI0&hl=en,none,none,none,none
1802,C,Renew Bath and Remodel,"Hudson, TX",(972) 654-6240,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZWO8EG4PToYRoeBHpnwVcW0&hl=en,none,none,none,none
1803,C,PRO-ANT,"Noble, OK",(405) 205-9635,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ75L5AMdCsocRh9ba0ZzlSuE&hl=en,none,none,none,none
1804,C,Arriaga’s Remodeling,"Sealy, TX",(832) 884-0222,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJt-EEQTxFQYYR6Ci7Nm49VNk&hl=en,none,none,none,none
1805,C,Smart kitchen Bath Renovation Culver City,"Culver City, CA",(424) 203-5528,"10822 Jefferson Blvd, Culver City, CA 90230",https://www.google.com/maps/place/?q=place_id:ChIJ9aQ5Ofi5woARlOK5oKnBKRY&hl=en,none,none,none,none
1806,C,Interiors That Work,"Longwood, FL",(407) 790-7873,"111 N Longwood St #101, Longwood, FL 32750",https://www.google.com/maps/place/?q=place_id:ChIJfdR5p3Ry54gRmQNAwfA8wI4&hl=en,none,none,none,none
1807,C,"Construct Kitchen and Bath, LLC","Newcastle, WA",(206) 498-3426,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJl17c7X4cvkwRsJB_liEtGWA&hl=en,none,none,none,none
1808,C,Quality Home Builders Norwalk,"Norwalk, CA",(562) 340-7073,"14405 Best Ave, Norwalk, CA 90650",https://www.google.com/maps/place/?q=place_id:ChIJT87wzMYs3YARICLpj2-Fits&hl=en,none,none,none,none
1809,C,Innovative Home Transformations,"Southbridge Town, MA",(774) 317-0599,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJsyo4bmSj5okRALy6eWQekXA&hl=en,none,none,none,none
1810,C,Boyd Home Renovation,"Fayetteville, GA",(770) 626-1560,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJfTe1Vd1FXEkROW4aUs-WUF0&hl=en,none,none,none,none
1811,C,Me&A Elite Remodeling,"Dothan, AL",(850) 661-6255,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0aCOCFi8kCkRZPb0ld_6lNI&hl=en,none,none,none,none
1812,C,Alex Massa llc,"Haddon Heights, NJ",(856) 685-9758,"916 W Kings Hwy, Haddon Heights, NJ 08035",https://www.google.com/maps/place/?q=place_id:ChIJtdEyKpnOxokR5BqNssN3StI&hl=en,none,none,none,none
1813,C,US Ceramics Tile Contractor,"West Haven, UT",(385) 289-5130,"1039 W Wilson Ln, West Haven, UT 84401",https://www.google.com/maps/place/?q=place_id:ChIJwd1P83YOrgMRMnKgDQ9hF6s&hl=en,none,none,none,none
1814,C,Braun Home Improvements,"New Kensington, PA",(412) 519-6446,"218 Dombroski Ave, New Kensington, PA 15068",https://www.google.com/maps/place/?q=place_id:ChIJiYVNYIuVNIgRFuzWvzpQiH0&hl=en,none,none,none,none
1815,C,Ricardo Remodeling,"Garfield, NJ",(973) 851-7225,"15 Orchard St, Garfield, NJ 07026",https://www.google.com/maps/place/?q=place_id:ChIJIWHFDiWsmGYRnGcNFsFSKEM&hl=en,none,none,none,none
1816,C,Kelly's Kitchen and Bath,"O'Fallon, MO",(636) 697-0380,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJYylCmJe_LGYRKB_2vEUF56A&hl=en,none,none,none,none
1817,C,D and D Woodcrafters LLC,"Two Rivers, WI",(920) 973-4204,"2004 14th St, Two Rivers, WI 54241",https://www.google.com/maps/place/?q=place_id:ChIJzQEI1oE0A4gRR1LR9NAy200&hl=en,none,none,none,none
1818,C,Metro Kitchen Cabinets And Windows,"Union Beach, NJ",(732) 566-4400,"1105 Union Ave, Union Beach, NJ 07735",https://www.google.com/maps/place/?q=place_id:ChIJH2vGK2E0wokRdkbNj7C9fKY&hl=en,none,none,none,none
1819,C,NT NEW TIME REMODELING LLC,"Anna, TX",(682) 326-1999,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJdwut9wvi1qUR1H1Bl1SccJE&hl=en,none,none,none,none
1820,C,Barry's Cultured Marble,"Benicia, CA",(707) 745-3444,"866 Teal Dr, Benicia, CA 94510",https://www.google.com/maps/place/?q=place_id:ChIJGwbRjfNuhYARcwTrQ7ReRYs&hl=en,none,none,none,none
1821,C,Noon Til 9 Flooring,"Maysville, KY",(606) 564-0044,"911 Fleming Rd, Maysville, KY 41056",https://www.google.com/maps/place/?q=place_id:ChIJO9whaw1QQYgROOyI-fWwdG4&hl=en,none,none,none,none
1822,C,Amigo's Remodeling L.L.C.,"Hammond, IN",(219) 670-9271,"2640 162nd Pl, Hammond, IN 46323",https://www.google.com/maps/place/?q=place_id:ChIJ-30kRWPfEYgRxhIt43gQW5E&hl=en,none,none,none,none
1823,C,Tabinets,"Lakeville, MA",(774) 419-2171,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJM7Y-DGFr-4kR_377epzhJ60&hl=en,none,none,none,none
1824,C,Mario's Home Pro Services,"Green Cove Springs, FL",(904) 806-0802,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJy7b-CZ69iGURWcQ-Xmub1Y4&hl=en,none,none,none,none
1825,C,Arizone Refinishing LLC,"Casa Grande, AZ",(602) 831-9003,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ50aXTpa22W8Rn2xMIXaLnso&hl=en,none,none,none,none
1826,C,Nick's Home Repair & Remodeling,"Peachtree City, GA",(470) 399-0300,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJp9zjqQKkOWsRlEEs_WElUxw&hl=en,none,none,none,none
1827,C,Gibbs Home Remodeling,"Wichita Falls, TX",(940) 782-2486,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ1xKnjqw8U4YRslVc4IDhON0&hl=en,none,none,none,none
1828,C,Industry Cabinets,"Beaumont, CA",(951) 663-2424,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ0b20vWXZZwwRqn_2lf3SFes&hl=en,none,none,none,none
1829,C,Santos Shower Remodeling,"Goldsboro, NC",(919) 432-7415,"808 Scott St, Goldsboro, NC 27534",https://www.google.com/maps/place/?q=place_id:ChIJFYW5Fa-rrokRNeKL_rfw_wI&hl=en,none,none,none,none
1830,C,"Kitchens and Baths by Design, LLC","Pearl, MS",(769) 233-1511,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJbRmUx4bMzUURWDQjxRJV0LQ&hl=en,none,none,none,none
1831,C,Paradise Kitchens and Floors LLC,"Frostburg, MD",(301) 687-1001,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJzTIrhCqXyokRIX6pVVTM4XA&hl=en,none,none,none,none
1832,C,Custom Surface Solutions Inc.,"League City, TX",(281) 338-1445,"190B2, Gulf Fwy, League City, TX 77573",https://www.google.com/maps/place/?q=place_id:ChIJAQAAANCCQIYRn25aY4hObzY&hl=en,none,none,none,none
1833,C,Stoneworks,"Pocatello, ID",(208) 237-0696,"12499 W Reservation Rd, Pocatello, ID 83202",https://www.google.com/maps/place/?q=place_id:ChIJt0oficpGVVMRuZ7dGJEfOew&hl=en,none,none,none,none
1834,C,S and M Home Improvements,"Troy, OH",(937) 418-9954,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJt2mHYyI5n6ERWzinROuUZSo&hl=en,none,none,none,none
1835,C,Amaya Design & Remodeling,"Odessa, TX",(432) 215-5540,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZaWMR3CzsQYRaS7fsH81zow&hl=en,none,none,none,none
1836,C,mprodesign,"Wheeling, IL",(773) 657-0141,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJO-Y6kaTNlkMRimRRPVR9xE8&hl=en,none,none,none,none
1837,C,LM KITCHEN DESIGN,"Miami Springs, FL",(786) 674-1905,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJv4t4ImWgRwMRhjU9Wkr3XwU&hl=en,none,none,none,none
1838,C,Cabinet Factory,"Duncan, OK",(580) 255-2111,"1000 McCurdy Rd, Duncan, OK 73533",https://www.google.com/maps/place/?q=place_id:ChIJ29hsdLNCrYcR6ToJ7R6cRz0&hl=en,none,none,none,none
1839,C,Rene's Painting & Remodeling Services,"Melrose Park, IL",(708) 600-5964,"705 N 17th Ave, Melrose Park, IL 60160",https://www.google.com/maps/place/?q=place_id:ChIJw-LbgkSRJ0MRzn_aXz_9G30&hl=en,none,none,none,none
1840,C,K&S Remodeling and Custom Cabinetry,"White Bear Lake, MN",(612) 518-3804,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJTfeQynzXslIRi3DAZu5blcg&hl=en,none,none,none,none
1841,C,cml home renovation LLC,"Morrow, GA",(470) 315-5132,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7zgEpmdkMC4RFEZEjcB-RY8&hl=en,none,none,none,none
1842,C,Fidelis Remodeling Group,"McCordsville, IN",(317) 910-4718,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJaSaIDyW1FIgRsy1NOSJMhjo&hl=en,none,none,none,none
1843,C,Designs Plus Kitchen & Bath,"Brookfield, CT",(203) 740-7744,"246 Federal Rd STE C11, Brookfield, CT 06804",https://www.google.com/maps/place/?q=place_id:ChIJKXlPRuH554kRzPOL2BJFICk&hl=en,none,none,none,none
1844,C,HSP Kitchen Remodel,"Bremerton, WA",(360) 997-2338,"828 Broadway Ave Unit A, Bremerton, WA 98337",https://www.google.com/maps/place/?q=place_id:ChIJRTAUZRI3kFQRLTOjM5ef5c8&hl=en,none,none,none,none
1845,C,Moses Custom Cabinetry LLC,"Burley, ID",(208) 650-0279,"389 S 250 E, Burley, ID 83318",https://www.google.com/maps/place/?q=place_id:ChIJT5h_daM1q1QRUdZqp5VTs4U&hl=en,none,none,none,none
1846,C,Construction J&C LLC,"Cottonwood Heights, UT",(561) 695-6571,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJW1M4I68z3QURlp_BrknXUCo&hl=en,none,none,none,none
1847,C,Blanchard Home Improvements,"Lafayette, LA",(337) 255-2482,"619 Bonin Rd, Lafayette, LA 70508",https://www.google.com/maps/place/?q=place_id:ChIJ9SXGDz-dJIYRsy0YCk0I-ps&hl=en,none,none,none,none
1848,C,Fischer Tile & Floor Covering,"Brenham, TX",(979) 836-5616,"2221 S Market St, Brenham, TX 77833",https://www.google.com/maps/place/?q=place_id:ChIJs3nr6UmoRoYR_T8XB8pB44M&hl=en,none,none,none,none
1849,C,Ronnie's Resolutions,"Chickasha, OK",(405) 200-3138,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJgbn-9Vo3TCYR7mhzSefpCAs&hl=en,none,none,none,none
1850,C,Rogue Valley Marble & Granite LLC,"Grants Pass, OR",(541) 474-4319,"2375 Foothill Blvd A, Grants Pass, OR 97526",https://www.google.com/maps/place/?q=place_id:ChIJmUUAuXl5xVQR2Z53Xzxywxw&hl=en,none,none,none,none
1851,C,Casa crafted remodeling LLC,"Humble, TX",(832) 960-0260,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJEfmHJlRzHGURV2tP1T0vzmQ&hl=en,none,none,none,none
1852,C,Cetile California,"Hemet, CA",(951) 399-1076,"245 Hanoverian Dr, Hemet, CA 92545",https://www.google.com/maps/place/?q=place_id:ChIJge7bUz1EzQsRnnoZ97v3jWI&hl=en,none,none,none,none
1853,C,Sierra Construction & Design LLC,"Reno, NV",(775) 771-5165,"5655 Riggins Ct #13, Reno, NV 89502",https://www.google.com/maps/place/?q=place_id:ChIJR2ftNusPHQURNZJww3qz0XM&hl=en,none,none,none,none
1854,C,Wolverine Maintenance LLC,"Allen Park, MI",(734) 368-8034,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJi8wRFyxDrGMR2GWDoGodMA4&hl=en,none,none,none,none
1855,C,Lightshine Design,"Massillon, OH",(330) 232-3249,"2137 Wales Ave NW Unit 1, Massillon, OH 44646",https://www.google.com/maps/place/?q=place_id:ChIJGxxMxijXNogRfG0m4DfWYQ8&hl=en,none,none,none,none
1856,C,Awe Home Services LLC,"Watertown, WI",(920) 206-2751,"419 Humboldt St, Watertown, WI 53094",https://www.google.com/maps/place/?q=place_id:ChIJHUqa7F0rBIgRU0NP7OUzHlQ&hl=en,none,none,none,none
1857,C,AC Designer Cabinets,"West Park, FL",(954) 274-5766,"5927 SW 21st St, West Park, FL 33023",https://www.google.com/maps/place/?q=place_id:ChIJp08JlsWv2YgRJCVhZW_f8JI&hl=en,none,none,none,none
1858,C,Highlands Cabinet Inc,"Sebring, FL",(863) 385-4396,"739 Glenwood Ave, Sebring, FL 33870",https://www.google.com/maps/place/?q=place_id:ChIJO5edjzlX3IgRfm24BTlgYDM&hl=en,none,none,none,none
1859,C,Vito Remodeling And Refinishing Inc,"Forest Park, IL",(708) 369-9263,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJrxftda4ZkyQRGMBi36gYyUU&hl=en,none,none,none,none
1860,C,Versatile Renovations,"Fernandina Beach, FL",(678) 320-7202,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZ2iS9Zer5YgReBGnVHn2j6Q&hl=en,none,none,none,none
1861,C,Designer Kitchen & Bath Div.,"Madison, AL",(256) 858-1970,"106 Castle Dr, Madison, AL 35758",https://www.google.com/maps/place/?q=place_id:ChIJNZJDLeZpYogRqsud-3G139E&hl=en,none,none,none,none
1862,C,United Kitchen & Bath,"Kenner, LA",(504) 780-8400,"2304 Marietta St, Kenner, LA 70062",https://www.google.com/maps/place/?q=place_id:ChIJ78IcAjO3IIYR42xroOpzZ_g&hl=en,none,none,none,none
1863,C,Precious Custom Cabinets / Pacific Custom Millwork Inc.,"South Gate, CA",(323) 476-7777,"10600 Dolores Ave, South Gate, CA 90280",https://www.google.com/maps/place/?q=place_id:ChIJE6PDQO_LwoAR7Pt8c4QlKug&hl=en,none,none,none,none
1864,C,B&B Home Improvement & Design,"Hallandale Beach, FL",(305) 940-9881,"800 Silks Run, Hallandale Beach, FL 33009",https://www.google.com/maps/place/?q=place_id:ChIJBeq_u4es2YgRlu6PCDtEDSA&hl=en,none,none,none,none
1865,C,Kitchen & Bath Cabinets,"El Paso, TX",(915) 852-0499,"13682 Nayarit Dr, El Paso, TX 79928",https://www.google.com/maps/place/?q=place_id:ChIJY9W_SxtB54YRTUBC7Q5TpOk&hl=en,none,none,none,none
1866,C,Vogue Kitchen and Bath,"Dana Point, CA",(949) 493-9998,"34085 CA-1 #205, Dana Point, CA 92629",https://www.google.com/maps/place/?q=place_id:ChIJI8egbhDw3IARDvRQ3sQFCmE&hl=en,none,none,none,none
1867,C,RW Tile,"Scottsboro, AL",(256) 305-3331,"784 Co Rd 30, Scottsboro, AL 35768",https://www.google.com/maps/place/?q=place_id:ChIJ4wJ1ksnxYYgRrtpFBeDdPCg&hl=en,none,none,none,none
1868,C,Advanced Cabinetry Inc,"Prineville, OR",(541) 447-7024,"2853 SW High Desert Dr, Prineville, OR 97754",https://www.google.com/maps/place/?q=place_id:ChIJ-2gfi-wtuVQRnx63G_0zRZI&hl=en,none,none,none,none
1869,C,JP Custom Cabinets and Construction,"Krum, TX",(940) 580-8123,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJnddUr3Od2iERK3jFETUe3Jo&hl=en,none,none,none,none
1870,C,Greenwood Kitchen Cabinet & Countertop,"Williston Park, NY",(516) 294-1918,"368 Hillside Ave., Williston Park, NY 11596",https://www.google.com/maps/place/?q=place_id:ChIJgyLhZAeIwokR7LXq6rZ_kkQ&hl=en,none,none,none,none
1871,C,A+ countertops & home remodeling,"Charlotte, NC",(704) 773-8670,"6024 McDaniel Ln, Charlotte, NC 28213",https://www.google.com/maps/place/?q=place_id:ChIJV609E68fVIgRqi70F8e9wDo&hl=en,none,none,none,none
1872,C,American Kitchen Bathroom Renovation Los Angeles,"Los Angeles, CA",(310) 691-8856,"8616 S La Tijera Blvd, Los Angeles, CA 90045",https://www.google.com/maps/place/?q=place_id:ChIJzbedr9OwwoARyurafC3O5cA&hl=en,none,none,none,none
1873,C,Elite Custom Cabinets & Trim LLC,"Sulphur, LA",(337) 502-2296,"144 S Post Oak Rd, Sulphur, LA 70663",https://www.google.com/maps/place/?q=place_id:ChIJD1Wh53SNO4YRCAYdo_6s784&hl=en,none,none,none,none
1874,C,Phoenix Home Remodeling,"Fairview Heights, IL",(618) 207-3090,"10890 Lincoln Trail, Fairview Heights, IL 62208",https://www.google.com/maps/place/?q=place_id:ChIJI_8ZsQzEm2MRIzU9wLdQAg8&hl=en,none,none,none,none
1875,C,Yazmin Tiles,"Tavernier, FL",(305) 484-2030,"Next to ACE Hardware, 91880 Overseas Hwy, Tavernier, FL 33070",https://www.google.com/maps/place/?q=place_id:ChIJBz3vwutA14gRiOaiSFmihD4&hl=en,none,none,none,none
1876,C,Gentile Homes & Renovations,"Boiling Spring Lakes, NC",(518) 935-3793,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJT1W4PnOV_GkRQ5XmoVoHiPc&hl=en,none,none,none,none
1877,C,B & C Cabinets & Millwork,"Carson City, NV",(775) 322-0000,"5241 Metric Way, Carson City, NV 89706",https://www.google.com/maps/place/?q=place_id:ChIJg9xW0aoLmYARfeAwiVjPYeA&hl=en,none,none,none,none
1878,C,Unique Tile,"Turlock, CA",(209) 676-0575,"320 S Broadway, Turlock, CA 95380",https://www.google.com/maps/place/?q=place_id:ChIJ70Oh2jUGkYARBs3UK_qUs9Y&hl=en,none,none,none,none
1879,C,Florida Kitchen Design and Bath LLC,"Boynton Beach, FL",(561) 769-0380,"1257 Vía Panzani, Boynton Beach, FL 33426",https://www.google.com/maps/place/?q=place_id:ChIJVc7veXbKpIcREQ24g7C59Gc&hl=en,none,none,none,none
1880,C,Hanson's Home Improvements,"Janesville, WI",(608) 921-8353,"1312 Blaine Ave, Janesville, WI 53545",https://www.google.com/maps/place/?q=place_id:ChIJC7j0ww8aBogRF6zy-kdL7eU&hl=en,none,none,none,none
1881,C,"Sumter Reglazing,LLC","Sumter, SC",(803) 847-1008,"2804 Cains Mill Rd, Sumter, SC 29154",https://www.google.com/maps/place/?q=place_id:ChIJZWy669Nr_4gRdzzZKJ1HgZ8&hl=en,none,none,none,none
1882,C,Antonio Cabinetry,"Sleepy Hollow, NY",(914) 631-2353,"334 N Broadway, Sleepy Hollow, NY 10591",https://www.google.com/maps/place/?q=place_id:ChIJIQTmV6HqwokRx-7v0ebGMcs&hl=en,none,none,none,none
1883,C,"DC Cabinets, LLC","Dickson, TN",(615) 829-0476,"1401 US-70, Dickson, TN 37055",https://www.google.com/maps/place/?q=place_id:ChIJYeZY8p67ZIgRk9pQyP9dXGE&hl=en,none,none,none,none
```
