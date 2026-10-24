# Round 2: Gemini task 2, part 09 of 17 (100 businesses, rows 1884 to 1983)

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row 1983: reply in that chat "Continue with
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
1884,C,Yoel Fl remodeling kitchen,"Miami, FL",(305) 842-0083,"17030 NW 12th Ave, Miami, FL 33169",https://www.google.com/maps/place/?q=place_id:ChIJs3P-9Suv2YgRipUfGHCIyEg&hl=en,none,none,none,none
1885,C,Macomb Kitchen & Bath,"Fraser, MI",(586) 943-3687,"33109 Groesbeck Hwy, Fraser, MI 48026",https://www.google.com/maps/place/?q=place_id:ChIJ35kO4frYJIgR5WhvIHbSQhs&hl=en,none,none,none,none
1886,C,Big Bear Cabinetry,"Big Bear, CA",(909) 436-8345,"627 W Valley Blvd, Big Bear, CA 92314",https://www.google.com/maps/place/?q=place_id:ChIJc1YFHTi0xIARn23_RUzAw5w&hl=en,none,none,none,none
1887,C,David's Custom Cabinets,"Franklin, VA",(757) 562-6672,"330 East St, Franklin, VA 23851",https://www.google.com/maps/place/?q=place_id:ChIJUVlK1XQksIkRrQE8V38zRkA&hl=en,none,none,none,none
1888,C,Arias Remodeling,"Sweetwater, FL",(305) 889-9695,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJF5Gt3CF3U4kRSzLQVzkcIck&hl=en,none,none,none,none
1889,C,"South Mountain Kitchen and Bath, LLC","Rio Communities, NM",(505) 977-6158,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJafQ2eMANIocR6ncmgKo-Gco&hl=en,none,none,none,none
1890,C,Designer Choice Kitchen and Bath,"Bonita Springs, FL",(239) 878-7722,"28101 Race Track Rd #707, Bonita Springs, FL 34135",https://www.google.com/maps/place/?q=place_id:ChIJPU63UEoZ24gRkuuDfs102eM&hl=en,none,none,none,none
1891,C,JR LEAL BROTHERS INC.,"Bellflower, CA",(562) 925-3300,"15510 Lakewood Blvd, Bellflower, CA 90706",https://www.google.com/maps/place/?q=place_id:ChIJYzrJWDHNwoARXGRrHFUlYfA&hl=en,none,none,none,none
1892,C,M&M Cabinets & Countertops,"Butte, MT",(406) 219-8010,"3928 Wynne Ave Unit 3 & 4, Butte, MT 59701",https://www.google.com/maps/place/?q=place_id:ChIJjZEINO4HW1MRwnbvNYUG-eE&hl=en,none,none,none,none
1893,C,Beaufort Midway Cabinetry & Design,"Port Royal, SC",(843) 812-4654,"1002 15th St, Port Royal, SC 29935",https://www.google.com/maps/place/?q=place_id:ChIJUY8Yps4M_IgR_HYjigFegJs&hl=en,none,none,none,none
1894,C,Springfield Kitchen and Bathroom Remodeling Company,"Springfield, MO",(417) 353-0990,"851 S Glenstone Ave, Springfield, MO 65802",https://www.google.com/maps/place/?q=place_id:ChIJIQI9oHJjz4cR4fx_G1DuDUA&hl=en,none,none,none,none
1895,C,Affordable Cabinets LLC,"South Daytona, FL",(386) 299-1064,"1079 Sheri Blvd, South Daytona, FL 32119",https://www.google.com/maps/place/?q=place_id:ChIJEx42qq7Z5ogRF2P_9pp82aw&hl=en,none,none,none,none
1896,C,Illinois Remodeling Consultants,"Morton, IL",(309) 304-3040,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ7_yBzJlXCogR9Up1QDPEBWI&hl=en,none,none,none,none
1897,C,For the love of cabinets,"West Plains, MO",(417) 224-2659,"1400 S Vly Rd, West Plains, MO 65775",https://www.google.com/maps/place/?q=place_id:ChIJya1n5sZX0IcRPIsmmaxjxCE&hl=en,none,none,none,none
1898,C,ONYX Kitchen & Bath,"Dearborn, MI",(313) 575-4696,"1330 N Telegraph Rd, Dearborn, MI 48128",https://www.google.com/maps/place/?q=place_id:ChIJcUL2wD5LO4gR1T60ZSD9nVU&hl=en,none,none,none,none
1899,C,Magnolia Kitchen & Bath Remodeling Costa Mesa.,"Costa Mesa, CA",(714) 489-5911,"263 Briggs Ave, Costa Mesa, CA 92626",https://www.google.com/maps/place/?q=place_id:ChIJiTLxCrfX3IAR3ckhnRHn1mo&hl=en,none,none,none,none
1900,C,1-2-3 Shower & Bath LLC,"Greenwood, AR",(479) 336-7890,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJW7rcUEt7NosRjdNPz8YGG30&hl=en,none,none,none,none
1901,C,Restore yours llc,"Springfield, FL",(706) 566-3531,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJKVPK-DfyS6sRojJVIlbzLJg&hl=en,none,none,none,none
1902,C,Moseley Cabinets,"Copperas Cove, TX",(321) 591-1265,"954 Moseley Rd, Copperas Cove, TX 76522",https://www.google.com/maps/place/?q=place_id:ChIJTcbm4hSwWoYRHnI45DnfCTQ&hl=en,none,none,none,none
1903,C,Innovative Kitchen & Bath Inc.,"Killingly, CT",(860) 397-6300,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJez_TqDLCqioR5SMOWwJWyug&hl=en,none,none,none,none
1904,C,Dempsey Contracting,"La Vista, NE",(402) 340-9924,"6906 Pine Dr, La Vista, NE 68128",https://www.google.com/maps/place/?q=place_id:ChIJ9zFMcLqLk4cRfhAc_oZp-J8&hl=en,none,none,none,none
1905,C,M&J Demolition & Remodeling LLC,"Deer Park, TX",(832) 691-1171,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ13w9NV5RoWsRRkHycDl3x40&hl=en,none,none,none,none
1906,C,Restoration NuVue,"Cottonwood Heights, UT",(801) 560-6008,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJQTwTmxF9UocRp4Kvx3goRa8&hl=en,none,none,none,none
1907,C,Kraft Kitchens,"Nevada City, CA",(530) 263-0602,"220 Main St Ste 7, Nevada City, CA 95959",https://www.google.com/maps/place/?q=place_id:ChIJX-omPH17m4ARvnFwWE1BF9A&hl=en,none,none,none,none
1908,C,MK Dream Home LLC,"Sunland Park, NM",(915) 422-1600,"317 First St, Sunland Park, NM 88063",https://www.google.com/maps/place/?q=place_id:ChIJ0xjxD9v53YYRcDkStCT0WAs&hl=en,none,none,none,none
1909,C,Independence Renovations LLC.,"Pottstown, PA",(484) 925-4872,"2315 N Charlotte St, Pottstown, PA 19464",https://www.google.com/maps/place/?q=place_id:ChIJFcdjXD2FxokRARFDmxZGs9A&hl=en,none,none,none,none
1910,C,S Tiles Custom Tile & Stone,"Council Bluffs, IA",(402) 813-3233,"631 Simms Ave, Council Bluffs, IA 51503",https://www.google.com/maps/place/?q=place_id:ChIJf1aWE_KFk4cRCWFllEjHlsI&hl=en,none,none,none,none
1911,C,LifeStyle Granite & Cabinetry,"Spanish Fort, AL",(251) 367-7777,"5395 Battleship Pkwy, Spanish Fort, AL 36527",https://www.google.com/maps/place/?q=place_id:ChIJT00cA2FDmogREnzf8bQiAnA&hl=en,none,none,none,none
1912,C,Abel Woodworking & Remodeling,"Greensburg, KY",(270) 645-2324,"109 N 2nd St, Greensburg, KY 42743",https://www.google.com/maps/place/?q=place_id:ChIJu5B7gjp5aIgR7m8taUfCO7w&hl=en,none,none,none,none
1913,C,Remodeling and Home Improvement LLC,"Collierville, TN",(901) 428-0377,"348 New Byhalia Rd Suite 9A, Collierville, TN 38017",https://www.google.com/maps/place/?q=place_id:ChIJMT4Lw3Gff4gRCH1TY3qPGbE&hl=en,none,none,none,none
1914,C,RP Creative Carpentry,"Loves Park, IL",(847) 346-6459,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJFcH_mL6huG4RLss6U4O5WwE&hl=en,none,none,none,none
1915,C,Avon Building and Renovations LLC,"West Simsbury, CT",(860) 985-4789,"19 Wildwood Rd, West Simsbury, CT 06092",https://www.google.com/maps/place/?q=place_id:ChIJEw48u5up54kR-NKy5MOGnVI&hl=en,none,none,none,none
1916,C,Espinoza Remodeling Services,"Yuba City, CA",(530) 978-3920,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXY587cV-cWoRR0AUFKGYb2E&hl=en,none,none,none,none
1917,C,Correia Tile NJ,"Long Branch, NJ",(848) 332-0657,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJkX8OgqphsoMRnHGQaAfOBhw&hl=en,none,none,none,none
1918,C,Frias Remodeling LLC,"Palm Springs, FL",(561) 460-7815,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJXYbmHEEF6YsR13aPznCwFhA&hl=en,none,none,none,none
1919,C,Iron Peak Remodeling,"Jerome, ID",(208) 404-9822,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ_e3YPz9UjYoRwUN0nQHSIzQ&hl=en,none,none,none,none
1920,C,Garrison Tile & Renovation,"Burley, ID",(801) 637-5401,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ-0aWTbw3q1QRdy7di7xnAiM&hl=en,none,none,none,none
1921,C,Liam Paul Kitchen & Bath LLC,"Jefferson Hills, PA",(412) 694-2995,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJZyjm2duorgQRgu-DB5-7FjY&hl=en,none,none,none,none
1922,C,P & F Custom Tileworks Inc,"Monroe, MI",(734) 341-3764,"432 Bogey Ct, Monroe, MI 48162",https://www.google.com/maps/place/?q=place_id:ChIJ7xH_36RlO4gRPXisIkcqbP0&hl=en,none,none,none,none
1923,C,Countertop Concepts,"Polson, MT",(406) 270-4998,"1 7th Ave W, Polson, MT 59860",https://www.google.com/maps/place/?q=place_id:ChIJ63I07ONzZ1MRUlXX3qdmEzo&hl=en,none,none,none,none
1924,C,Heritage Cabinets Inc,"King City, CA",(831) 386-0805,"300 E San Antonio Dr, King City, CA 93930",https://www.google.com/maps/place/?q=place_id:ChIJE85aWdTwkoARk241zS3HNsk&hl=en,none,none,none,none
1925,C,Top Notch Renovations,"Madison, WI",(608) 291-6461,"995 Applegate Rd Ste B2, Madison, WI 53713",https://www.google.com/maps/place/?q=place_id:ChIJpas-MUutB4gRLw6pdBwJ1Tw&hl=en,none,none,none,none
1926,C,GF flooring & tile corp,"Cicero, IL",(832) 994-2252,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJUQQWOu-s0C4RtLZuPE58YYs&hl=en,none,none,none,none
1927,C,"Total Home Repair, LLC.","Temple, TX",(254) 931-5803,"305 W Ave M, Temple, TX 76504",https://www.google.com/maps/place/?q=place_id:ChIJ9XSrB51sRYYRrnAlO3Rdx2U&hl=en,none,none,none,none
1928,C,Royal-T Construction inc.,"Erda, UT",(801) 808-3882,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJseXFObVQ1KsR4axTDH7JXSM&hl=en,none,none,none,none
1929,C,Cabinet & Design Gallery,"Salisbury, MD",(410) 422-4385,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJycZAD-IDuYkRMCMOPYUTv8k&hl=en,none,none,none,none
1930,C,Casa Genessa Home Renovations LLC,"Warr Acres, OK",(405) 652-8764,"5601 NW 72nd St Suite #260B, Warr Acres, OK 73132",https://www.google.com/maps/place/?q=place_id:ChIJA5ROg6gFsocR5_Jxz3Nq1pY&hl=en,none,none,none,none
1931,C,JS CREW REMODELING,"Kemp, TX",(903) 471-2672,"19386 FM148, Kemp, TX 75143",https://www.google.com/maps/place/?q=place_id:ChIJJ4Xdrn8xSYYRS2Yx5IW0LEw&hl=en,none,none,none,none
1932,C,Carrillo Tile & Remodeling,"Palmhurst, TX",(956) 442-6475,"605 Nora Ln, Palmhurst, TX 78573",https://www.google.com/maps/place/?q=place_id:ChIJ906SCimpZYYRv0u1juzYm6M&hl=en,none,none,none,none
1933,C,HSP Bathroom Remodel,"Lakewood, WA",(253) 364-4034,"14405 Union Ave SW A, Lakewood, WA 98498",https://www.google.com/maps/place/?q=place_id:ChIJKQbYYk0HkVQR8HhZ4OV5hwY&hl=en,none,none,none,none
1934,C,"Bath Rescue, Inc.","Newtown, PA",(215) 968-6020,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJOd8SXo1UwYkRX4wlX-lu09Q&hl=en,none,none,none,none
1935,C,Anointed Action Services,"Richton Park, IL",(313) 583-9035,"Richton Park, IL 60471",https://www.google.com/maps/place/?q=place_id:ChIJeY3_C8kRDogRZTdpLQKZR1M&hl=en,none,none,none,none
1936,C,WhiteStone Construction & Cabinetry,"Bakersfield, CA",(661) 384-1418,"217 Mount Vernon Ave #20, Bakersfield, CA 93307",https://www.google.com/maps/place/?q=place_id:ChIJI7q1sEDp4kQRCZfgGc3afnQ&hl=en,none,none,none,none
1937,C,Pereira Remodeling Group,"Greenacres, FL",(561) 639-2167,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJJ6HLXZop2YgR5dOGh_hxufk&hl=en,none,none,none,none
1938,C,Remodco Remodeling & Tub Repair,"Phenix City, AL",(334) 614-8192,"338 Mimosa Rd, Phenix City, AL 36870",https://www.google.com/maps/place/?q=place_id:ChIJn9rMCrhHjYgR1pFAKOiz_-k&hl=en,none,none,none,none
1939,C,Faux to Finish LLC Cabinet Painting,"Mt Holly, NC",(980) 322-7282,"243 Cedar Ln, Mt Holly, NC 28120",https://www.google.com/maps/place/?q=place_id:ChIJU86IZHXmAW0RTwfYjVBnbFs&hl=en,none,none,none,none
1940,C,L & L Tile & Floor Coverings,"Demopolis, AL",(334) 289-9627,"1734 US-43, Demopolis, AL 36732",https://www.google.com/maps/place/?q=place_id:ChIJVUxni_SXhYgRsydCRVeHEHo&hl=en,none,none,none,none
1941,C,Texas Pride Home Services,"Schertz, TX",(830) 370-4433,"3616 Gamble, Schertz, TX 78154",https://www.google.com/maps/place/?q=place_id:ChIJX0lLUlqSXIYRj_sEerJeeDA&hl=en,none,none,none,none
1942,C,RG Brothers Custom Cabinet,"Toccoa, GA",(770) 870-9325,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ8bS1p4aUXGcRlTGWoEI1HjQ&hl=en,none,none,none,none
1943,C,Bastian Pro Remodeling LLC,"Raymore, MO",(816) 215-1227,"402 Palomino Cir, Raymore, MO 64083",https://www.google.com/maps/place/?q=place_id:ChIJaaieefrZwIcRKBauE4cyZ9M&hl=en,none,none,none,none
1944,C,QC Cabinetry Plus,"Davenport, IA",(563) 370-6335,"5101 Tremont Ave Unit B, Davenport, IA 52807",https://www.google.com/maps/place/?q=place_id:ChIJVVWVdag14ocR4iWkitF1ITQ&hl=en,none,none,none,none
1945,C,Joslin's Cabinet Co.,"Columbus, IN",(812) 379-1392,"4050 Middle Rd, Columbus, IN 47203",https://www.google.com/maps/place/?q=place_id:ChIJibQELHmga4gRKr9_8_k1PAk&hl=en,none,none,none,none
1946,C,Wall to Wall Home Improvement LLC,"Coventry, CT",(860) 759-8956,"540 Bunker Hill Rd, Coventry, CT 06238",https://www.google.com/maps/place/?q=place_id:ChIJ7yvml4lh5okR-AhpPo0sfWk&hl=en,none,none,none,none
1947,C,Azalea Tile and Remodeling,"Oakland, TN",(901) 634-2269,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJF2XRw99N7C8RycQltMOc3dA&hl=en,none,none,none,none
1948,C,WAC Resurfacing,"Massillon, OH",(330) 833-2722,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJvWEWkXonN4gRymrnwnQyLRg&hl=en,none,none,none,none
1949,C,Bright Interiors Studio - Kitchen Cabinets,"Elk Grove Village, IL",(847) 262-5989,"1675 Tonne Rd, Elk Grove Village, IL 60007",https://www.google.com/maps/place/?q=place_id:ChIJg23XquexD4gR2wDnwbs5UZ0&hl=en,none,none,none,none
1950,C,Speedy Kitchens LLC,"Litchfield Park, AZ",(602) 618-6363,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJrT2MFmaFVYkRk-ERvKjwKkA&hl=en,none,none,none,none
1951,C,Aim High Kitchen & Cabinets,"St. Augustine, FL",(904) 304-2488,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJLcbzalgn5IgR7Ur5j1SZX3c&hl=en,none,none,none,none
1952,C,Kingdom Karpentry,"Darby, PA",(484) 372-0602,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJY119kFXBxokRMyn_HcCikKI&hl=en,none,none,none,none
1953,C,A Cabinet Above Kitchen Remodelers,"Bargersville, IN",(317) 771-1103,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJN4Gx3jKpMaMRfjzSEN_0PWs&hl=en,none,none,none,none
1954,C,Cabinet Specialties LLC,"Plainville, CT",(860) 747-4114,"38 Neal Ct, Plainville, CT 06062",https://www.google.com/maps/place/?q=place_id:ChIJMTvSD--w54kRsWXVFWKRKN8&hl=en,none,none,none,none
1955,C,Alfa Home Solutions | Bathroom renovation | Kitchen remodeling | Carpentry | Flooring installation | Painting,"Ocoee, FL",(689) 356-6801,"1711 Amazing Way Ste 213, Ocoee, FL 34761",https://www.google.com/maps/place/?q=place_id:ChIJl4S0w66D54gR3ra4wmQZU48&hl=en,none,none,none,none
1956,C,Timeless Renovations,"Christiansburg, VA",(540) 404-8586,"150 Corning Dr, Christiansburg, VA 24073",https://www.google.com/maps/place/?q=place_id:ChIJs0VVHDrKbm4RQYNw5XyaDhI&hl=en,none,none,none,none
1957,C,Abernethy Enterprises Construction Group,"Orange City, FL",(858) 667-0142,"1195 13th St, Orange City, FL 32763",https://www.google.com/maps/place/?q=place_id:ChIJLxoMjyUb54gR9k943v9KYeY&hl=en,none,none,none,none
1958,C,Custom Cabinet Doors Inc,"Pilot Point, TX",(940) 686-2808,"924 N Industrial Blvd, Pilot Point, TX 76258",https://www.google.com/maps/place/?q=place_id:ChIJfxiIeupPTIYRI9STclO8Yww&hl=en,none,none,none,none
1959,C,Performance Kitchen & Bathroom Remodel Tulsa,"Verdigris, OK",(918) 400-0660,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJB4R7a5M6dkQRUbqCMXMguEY&hl=en,none,none,none,none
1960,C,"Rose Rock Remodeling, LLC","Noble, OK",(580) 278-8069,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJwZqxRK1Re2kR2MKOtc1XeSI&hl=en,none,none,none,none
1961,C,K&E Home Upgrades Remodeling Contractor,"Mt Carmel, TN",(423) 765-3376,"138 Inca Dr, Mt Carmel, TN 37645",https://www.google.com/maps/place/?q=place_id:ChIJg_eCNOrxWogRnIES3Q58YrE&hl=en,none,none,none,none
1962,C,RMZ Renovations LLC,"Selma, NC",(984) 274-5232,"154 Halton Ln, Selma, NC 27576",https://www.google.com/maps/place/?q=place_id:ChIJk1Ls0fATrIkRhGeTx_Ko53o&hl=en,none,none,none,none
1963,C,DC Remodeling and Home Repair LLC,"Monmouth, OR",(971) 718-3764,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJBSwFldxuEiERTw4pkRhLXKQ&hl=en,none,none,none,none
1964,C,Heredia's Custom Cabinets,"Santa Paula, CA",(805) 524-7727,"957 Faulkner Rd #212, Santa Paula, CA 93060",https://www.google.com/maps/place/?q=place_id:ChIJAxynfAO16YARtM8c4oiS9us&hl=en,none,none,none,none
1965,C,R&R Handyman & Renovation's LLC,"Henderson, NC",(252) 767-0586,"500 J P Taylor Rd lot 36, Henderson, NC 27537",https://www.google.com/maps/place/?q=place_id:ChIJL7aJR-27rYkRLpIuM4dgzcY&hl=en,none,none,none,none
1966,C,Northern Countertops & Cabinets,"Ukiah, CA",(707) 467-3969,"195 Clara Ave Entrance on, Mason St, Ukiah, CA 95482",https://www.google.com/maps/place/?q=place_id:ChIJVWq2mSt7gYARpa4Uxx0jEls&hl=en,none,none,none,none
1967,C,Navarro Construction Solutions,"Dade City, FL",(352) 807-2790,"15045 Pinellas Ave, Dade City, FL 33523",https://www.google.com/maps/place/?q=place_id:ChIJK3uufUaCXgUR23hwYJ2Ikng&hl=en,none,none,none,none
1968,C,Deb's Cabinet Shop,"Brookland, AR",(870) 935-0193,"303 S Holman St, Brookland, AR 72417",https://www.google.com/maps/place/?q=place_id:ChIJz1lL4GnV1YcRs6oz6LcYYB8&hl=en,none,none,none,none
1969,C,Cottrell Renovation LLC,"Mooresville, IN",(317) 287-4171,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJ66_RV9Hjx6MRs_VaozX3m9s&hl=en,none,none,none,none
1970,C,Top Home Kitchen Remodeling,"Rolling Hills Estates, CA",(424) 478-8010,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJia_c4v_pgSYRF6hU4F48Kvw&hl=en,none,none,none,none
1971,C,Laurel river renovations,"Corbin, KY",(606) 404-1752,"185 E Lewis St, Corbin, KY 40701",https://www.google.com/maps/place/?q=place_id:ChIJN_9yTqjFXIgRb87zcz3iDjw&hl=en,none,none,none,none
1972,C,SPIR Homes,"New Smyrna Beach, FL",(386) 290-4838,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJuypQycqLXa8RSKwBIuaAumw&hl=en,none,none,none,none
1973,C,AK Contracting,"Pontiac, IL",(779) 804-6017,service-area business,https://www.google.com/maps/place/?q=place_id:ChIJqZWAaN94_GgR7faEyy9_TQI&hl=en,none,none,none,none
1974,C,Classic Spaces LLC,"Georgetown, KY",(859) 492-0070,"401 Outlet Center Dr #280, Georgetown, KY 40324",https://www.google.com/maps/place/?q=place_id:ChIJU9i4XDQ_QogR0Y7JZ0uS1WI&hl=en,none,none,none,none
1975,C,H&T Custom Interiors,"Graham, TX",(940) 456-3734,"1033 4th St, Graham, TX 76450",https://www.google.com/maps/place/?q=place_id:ChIJx7eqm3zJU4YRiMj-mu5nmQY&hl=en,none,none,none,none
1976,C,"Birmingham Remodeling and Construction, LLC","Stillwater, OK",(405) 612-9708,"4018 Yorkshire Dr, Stillwater, OK 74074",https://www.google.com/maps/place/?q=place_id:ChIJ45u6W46gsYcRlyHpYufw0_k&hl=en,none,none,none,none
1977,C,Modern Kitchen Makeovers,"Santa Fe Springs, CA",(562) 554-6566,"13063 Rosecrans Ave c, Santa Fe Springs, CA 90670",https://www.google.com/maps/place/?q=place_id:ChIJMQm5p44t3YARScvw67vYh_c&hl=en,none,none,none,none
1978,C,G&L Heilman Remodeling,"Taneytown, MD",(410) 218-9116,"4272 Francis Scott Key Hwy, Taneytown, MD 21787",https://www.google.com/maps/place/?q=place_id:ChIJZ1BSj9ZNyIkR_pdpxfXTSwQ&hl=en,none,none,none,none
1979,C,Fenn construction LLC,"Azle, TX",(817) 495-8897,"252 Mountain View Dr, Azle, TX 76020",https://www.google.com/maps/place/?q=place_id:ChIJe5__qmUvsYYRlkWxLiOqdE8&hl=en,none,none,none,none
1980,C,URESTI Fine Woodworks,"Donna, TX",(956) 884-1924,"807 N Hutto Rd, Donna, TX 78537",https://www.google.com/maps/place/?q=place_id:ChIJOa8Fj_J1ZYYR91FKldGNTC8&hl=en,none,none,none,none
1981,C,Baker Tile,"Sanger, CA",(559) 770-5732,"21343 E Weldon Ave, Sanger, CA 93657",https://www.google.com/maps/place/?q=place_id:ChIJKyBt1OYBlYARxhegQGWiKsU&hl=en,none,none,none,none
1982,C,Keystone Home Improvement LLC,"Washougal, WA",(360) 904-7374,"4031 Addy St, Washougal, WA 98671",https://www.google.com/maps/place/?q=place_id:ChIJvQ6krb-9lVQRHLgN6iSHOEM&hl=en,none,none,none,none
1983,C,Fusion Refinishing,"West Wareham, MA",(508) 807-3477,"47 Crest Dr, West Wareham, MA 02576",https://www.google.com/maps/place/?q=place_id:ChIJIQmxH5KjBEMRZAEq3SLBSwU&hl=en,none,none,none,none
```
