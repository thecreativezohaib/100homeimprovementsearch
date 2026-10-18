# Remodel 100: Gemini file I (59 new firms from discovery round 10)

Upload this file to a NEW Gemini chat and paste the prompt below. Same format as files A to H.

## Prompt

```
Use Google Maps and Google Search. For EVERY company in the attached table, find:
- the date of its NEWEST Google review (open maps_url, sort reviews by Newest) and the first 8 words of that review
- the date of the latest post on the Facebook page in the facebook column, and on the Instagram account in the instagram column (if the column says "none", write UNKNOWN; never use any other account)
- any job ad for the company that shows a posting date (its careers page, Indeed, ZipRecruiter, LinkedIn Jobs): the URL and the date

Rules:
- Never guess. Unknown means UNKNOWN. Dates as YYYY-MM-DD; if only a relative date is shown (like "3 weeks ago" or "10w"), copy it exactly.
- Plain URLs only. No links, no [text](url), no google.com/search wrappers.
- Write "closed" in status if Google shows the business closed, otherwise ok.
- Do ALL rows in this file. Do not stop to ask me. If a reply runs out of room, keep going in the next reply without waiting for me, until every row is done.
- Best: put all rows into ONE table and use "Export to Sheets", so I can download it as a CSV.

Output: CSV only, no commentary, with exactly this header:
row,checked_on,status,newest_review_date,newest_review_first_words,facebook_url,facebook_latest_post_date,instagram_url,instagram_latest_post_date,job_posting_url,job_posting_date
checked_on is today's date. Put text containing a comma in double quotes.
```

## Companies
```csv
row,business_name,address,website,maps_url,facebook,instagram
1301,Kitchen by kn remodeling,"19709 Ventura Blvd, Woodland Hills, CA 91364, United States",https://kitchenbyknremodeling.com/,https://www.google.com/maps/place/?q=place_id:ChIJvVIVeyAy0wURSjWbY7JHoas&hl=en,https://www.facebook.com/kitchenbyknremodeling https://www.facebook.com/remodelingyourhouses,https://www.instagram.com/kitchenbyknremodeling https://www.instagram.com/knremodelinginc
1302,Savvy Kitchens,"820 Manhattan Ave Ste 103, Manhattan Beach, CA 90266, United States",http://www.savvykitchens.com/,https://www.google.com/maps/place/?q=place_id:ChIJMbypTpOzwoARgrZcwsyQa4E&hl=en,http://facebook.com/savvykitchensmanhattanbeach http://www.facebook.com/2008/fbml,http://instagram.com/savvykitchens
1303,Twin Lakes Kitchen and Bath,"1210 Commerce Dr, Mountain Home, AR 72653, United States",https://twinlakeskitchenandbath.com/,https://www.google.com/maps/place/?q=place_id:ChIJs2DYP8Hb0YcR66zgDcOpX_4&hl=en,https://www.facebook.com/TwinLakesKitchenandBath https://www.facebook.com/TwinLakesWoodworkingandRemodeling,none
1304,Pristine Kitchens & Baths Corp.,"50 Pelham Dr, Coatesville, PA 19320, United States",https://pristinekitchensandbaths.com/,https://www.google.com/maps/place/?q=place_id:ChIJIxSpWqEnxIkRXJM0oEfNiNU&hl=en,https://www.facebook.com/PristineKitchensAndBaths,none
1305,CC Home Remodeling & Real Estate,,https://www.remodelwithcc.com/,https://www.google.com/maps/place/?q=place_id:ChIJNSZSw8oJig0Rv9JTk8gMNLw&hl=en,https://www.facebook.com/counterculturesohio,https://www.instagram.com/remodelwithcc
1306,HMK Construction,,https://hmkconstruction.com/,https://www.google.com/maps/place/?q=place_id:ChIJISrZYj1gXKwRExWuAHt_zkM&hl=en,https://www.facebook.com/HMKConstructionLLC,none
1307,Remodeling & Reconstruction Pros,"1345 Johns Rd, New Franklin, OH 44216, United States",https://www.rrprosohio.com/,https://www.google.com/maps/place/?q=place_id:ChIJfTisVDzQOigR40Gcd0qRRTw&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/profile.php,https://www.instagram.com/rrprosohio
1308,Surface Tech LLC,"492 W Tracker Rd, Nixa, MO 65714, United States",https://surfacetechllc.com/,https://www.google.com/maps/place/?q=place_id:ChIJE4CQwXZvz4cRGb7aKg40ll8&hl=en,https://www.facebook.com/surftech2017,https://www.instagram.com/surface_tech_llc
1309,Tier One Remodeling Inc.,"487 Erie St, Lancaster, NY 14086, United States",https://www.t1remodeling.com/,https://www.google.com/maps/place/?q=place_id:ChIJJe7RTbbRroQRMgUnorXINqk&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/Tier1remodeling,http://instagram.com/mariahmagazinedesign http://instagram.com/tieroneremodeling
1310,VECTOR ARTS Inc.,"3060 Giant Hwy, San Pablo, CA 94806, United States",https://vectorarts.org/,https://www.google.com/maps/place/?q=place_id:ChIJkVxR5LqChYARbbMt0--BFTo&hl=en,none,none
1311,"Gold Champion Interiors, LLC","219 East Dr, East Alton, IL 62024, United States",https://goldchampioninteriors.com/,https://www.google.com/maps/place/?q=place_id:ChIJw9EMesBb34cRf5RdOOD3zQ0&hl=en,https://www.facebook.com/GoldchampionInteriors https://www.facebook.com/settings,https://www.instagram.com/goldchampioninteriors
1312,Lewis Custom Woodwork LLC,"786 N 1250 W, Centerville, UT 84014, United States",https://www.lewiscustomwoodwork.com/,https://www.google.com/maps/place/?q=place_id:ChIJR8q3mfj4UocRq04tXqJkmkk&hl=en,http://www.facebook.com/2008/fbml,http://instagram.com/lewiscustomwoodwork https://www.instagram.com/lewiscustomwoodwork
1313,Kitchens Plus Upstate,,https://kitchensplusupstate.com/,https://www.google.com/maps/place/?q=place_id:ChIJDdNIU9fCYS0RRkstUQo25v0&hl=en,https://www.facebook.com/kitchensplussc,https://www.instagram.com/kitchensplusupstate
1314,"Timber & Stone Renovations, Inc.","159 Jesse King Rd, Advance, NC 27006, United States",https://tandsrenovations.com/,https://www.google.com/maps/place/?q=place_id:ChIJFdoHcDFXrIkR-JTyF5h3c8E&hl=en,https://www.facebook.com/timberandstonerenovations,https://www.instagram.com/tands_renovations
1315,Absolute Building and Energy,,https://www.goabsolute.co/,https://www.google.com/maps/place/?q=place_id:ChIJaXsuWm06lgER3-BiAV6gCkA&hl=en,https://www.facebook.com/wix,https://www.instagram.com/wix
1316,"Elite Renovations, LLC","11355 Inverness Ln, Maryland Heights, MO 63043, United States",https://eliterenovations.pro/,https://www.google.com/maps/place/?q=place_id:ChIJe0jJ5Ycx34cRYc4F4NReg0U&hl=en,none,none
1317,Hofmann Kitchens,"1811 Springfield Ave Ste 2L, New Providence, NJ 07974, United States",https://www.hofmanndb.com/,https://www.google.com/maps/place/?q=place_id:ChIJjZJfi3mlw4kRTYZv_MDvLeg&hl=en,https://www.facebook.com/people/Hofmann-Design-Build/100027162986974 https://www.facebook.com/profile.php,https://www.instagram.com/hofmanndesignbuild
1318,DeShong Design + Remodeling,,https://deshongdesignremodeling.com/,https://www.google.com/maps/place/?q=place_id:ChIJwf7kjnx-qWcRWsBQ4zJpEFM&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/deshongdesignremodeling,https://instagram.com/pwb_pgh https://www.instagram.com/deshongdesignremodeling
1319,Elizabeth Hall Designs,,https://elizabethhalldesigns.com/,https://www.google.com/maps/place/?q=place_id:ChIJ396_yrf3m4gR2erWxesl50I&hl=en,https://www.facebook.com/WordPresscom https://www.facebook.com/elizabethhalldesigns,https://www.instagram.com/ehdinteriordzign
1320,Faust Design Build,"99 Dutchess Terrace, Beacon, NY 12508, United States",https://faustdesignbuild.com/,https://www.google.com/maps/place/?q=place_id:ChIJq7Rvy04x3YkRwzHESAvRMtw&hl=en,http://www.facebook.com/2008/fbml http://www.facebook.com/faustdesignbuild,http://www.instagram.com/faustdesignbuild
1321,Total Home Remodeling,"14101 Norby Rd Unit B, Grandview, MO 64030, United States",https://totalhomekc.com/,https://www.google.com/maps/place/?q=place_id:ChIJMW8vBgTtwIcReWNLbX8l0mw&hl=en,none,none
1322,Beautiful Kitchens LLC,"861 N Greengate Rd, Greensburg, PA 15601, United States",https://beautifulkitchensllc.com/,https://www.google.com/maps/place/?q=place_id:ChIJ5c76NLzaNIgRJkEG1uFGK6o&hl=en,https://www.facebook.com/BeautifulKitchensLLC,none
1323,Nsight Kitchen & Bath Design,"2901 General De Gaulle Dr #102, New Orleans, LA 70131, United States",http://nsightdesignsnola.com/,https://www.google.com/maps/place/?q=place_id:ChIJk3-fHPOhIIYRAeHF2eCcx9s&hl=en,none,none
1324,Kitchen & Bath Center,"3518 Homer M Adams Pkwy, Alton, IL 62002, United States",http://www.kboutlet.com/,https://www.google.com/maps/place/?q=place_id:ChIJHSwodG1b34cRaH7-H5ivu34&hl=en,none,none
1325,Wooden Specialties,"110 Turn Row, Lafayette, LA 70508, United States",https://www.woodenspecialties.net/,https://www.google.com/maps/place/?q=place_id:ChIJd16tfEedJIYRPphhGqo76KQ&hl=en,https://www.facebook.com/woodenspecialties,none
1326,Kza Nova Home Remodeling Inc,,https://kazanovahomeremodelinginc.com/,https://www.google.com/maps/place/?q=place_id:ChIJ6a7o1tW7EE4RmPlHFb-Ijdo&hl=en,https://www.facebook.com/kzaNovaHomeRemodeling,none
1327,Design de Cuisine 805,"5860 Traffic Way, Atascadero, CA 93422, United States",https://www.designdecuisine805.com/,https://www.google.com/maps/place/?q=place_id:ChIJ8eulOW_D7IARSJI-EonRlv4&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/kitchenandbathdesign805,https://www.instagram.com/knobs_and_pulls
1328,Reliable Quality Construction Inc.,"245 W Roosevelt Rd Bldg 6, Unit 41, West Chicago, IL 60185, United States",https://reliablequalityconstruction.com/,https://www.google.com/maps/place/?q=place_id:ChIJZ2QhIff_DogRKivuO112gT0&hl=en,https://www.facebook.com/ReliableQualityConstruction,https://www.instagram.com/rq.construction
1329,Green Planet Remodeling,"9595 Wilshire Blvd Ste 900-724, Beverly Hills, CA 90212, United States",https://greenplanetremodeling.com/,https://www.google.com/maps/place/?q=place_id:ChIJLQnQode7woARhMjSdXpmhpw&hl=en,none,https://www.instagram.com/greenremodeling1
1330,Robinwood Kitchens,"560 Springfield Ave, Berkeley Heights, NJ 07922, United States",https://www.robinwoodkitchens.com/,https://www.google.com/maps/place/?q=place_id:ChIJEQStpt26w4kRTgjfBa9Lb3Y&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/RobinwoodKitchens,http://instagram.com/rw_kitchens
1331,"Schulz Design Build, Portland Home Builder",,https://www.schulzdesignbuild.com/,https://www.google.com/maps/place/?q=place_id:ChIJda2-aktzlVQR-jHImEpyubg&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/schulzdesignllc,https://www.instagram.com/schulzdesignbuild
1332,Fox Remodeling & Construction,"2306 Carolyn Dr, Taylor, TX 76574, United States",https://foxremodels.com/,https://www.google.com/maps/place/?q=place_id:ChIJ0bjA_0nnRIYR5w3FfFhgQ_s&hl=en,none,none
1333,Belle Design Collective,"26116 Lake Wilderness Country Club Dr SE, Maple Valley, WA 98038, United States",https://belledesigncollective.com/,https://www.google.com/maps/place/?q=place_id:ChIJAQCwAxBgkFQRar-tp6p9fRk&hl=en,https://www.facebook.com/belledesignbuild,https://www.instagram.com/belle_design_collective
1334,"Beck Renovate and Remodel, LLC",,https://www.beckrenovateandremodel.com/,https://www.google.com/maps/place/?q=place_id:ChIJGRh32lmKNIgRpXdM0s6TtP8&hl=en,https://www.facebook.com/beckrenovateandremodel,https://www.instagram.com/beckrenovateandremodel
1335,"EmpireHD, Inc.","99 Tulip Ave Ste 203, Floral Park, NY 11001, United States",https://empirehd.com/,https://www.google.com/maps/place/?q=place_id:ChIJ9zMh875RrIkRMJKODq7-30k&hl=en,none,none
1336,Modern Interiors,,https://moderninteriors.co/,https://www.google.com/maps/place/?q=place_id:ChIJNyKwDt2MUgwRWkf0R8eNy1E&hl=en,https://www.facebook.com/settings,none
1337,Old World Remodeling,"418 Depot St, Whitesboro, TX 76273, United States",https://oldworldremodeling.com/,https://www.google.com/maps/place/?q=place_id:ChIJnb1NS4kMToYRvkCH_k7gNws&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/OldWorldRemodeling,none
1338,T&H Home Improvements,,https://www.thhomeimprovements.com/,https://www.google.com/maps/place/?q=place_id:ChIJfwB9PnwLTYgRxWzl-Xp47rQ&hl=en,https://www.facebook.com/thhomeimprovementsllc,none
1339,Persia renovation LLC,"Persia renovation llc, 15875 Boones Ferry Rd Ste 2096, Lake Grove, OR 97035, United States",https://www.persiarenovation.com/,https://www.google.com/maps/place/?q=place_id:ChIJlYrNOIXyDygRg-AN1LoO-No&hl=en,none,https://www.instagram.com/persiarenovationllc
1340,Sandifer Design Build,"1639 Beach Blvd, Jacksonville Beach, FL 32250, United States",https://www.sandiferdesignbuild.com/,https://www.google.com/maps/place/?q=place_id:ChIJ04w4CWe35YgRxepieYVxow0&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/SandiferCustomHomes,https://www.instagram.com/p https://www.instagram.com/sandiferdesignbuild
1341,Deon Design Custom Builders.,"204 Main St, Little Ferry, NJ 07643, United States",https://www.deonbuilders.com/,https://www.google.com/maps/place/?q=place_id:ChIJU2NKoqv3wokRYp7CMv9KLEg&hl=en,https://www.facebook.com/DeonDesignCustomBuilders,https://www.instagram.com/deondesign
1342,RNHI General Contracting LLC,,https://rnhigeneralcontracting.com/,https://www.google.com/maps/place/?q=place_id:ChIJQaD-W0PYrwsR4B_FYiIuwtk&hl=en,https://www.facebook.com/rnhomeimprovementandrepair,none
1343,Dream Concepts Contracting LLC,"81-A NJ-183, Stanhope, NJ 07874, United States",https://www.dreamconceptscontracting.com/,https://www.google.com/maps/place/?q=place_id:ChIJf0LES9l3w4kR4sG36eqJnuQ&hl=en,https://www.facebook.com/dreamconceptscontracting,none
1344,General contractor Seven Wonders Construction,"428 Lincoln Blvd, Middlesex, NJ 08846, United States",https://www.sevenwondersconstruction.com/,https://www.google.com/maps/place/?q=place_id:ChIJM-XfWfi5w4kR2IFaRgIw_Qw&hl=en,https://www.facebook.com/sevenwondersconstruction,https://www.instagram.com/sevenwondersconstruction
1345,Pierce Design + Build,"5728 S 1475 E Ste 100, South Ogden, UT 84403, United States",https://piercedesignbuild.co/,https://www.google.com/maps/place/?q=place_id:ChIJH0VFFqoIU4cR48T7TwqrAO0&hl=en,https://www.facebook.com/piercedesignbuild,https://www.instagram.com/piercedesignbuild
1346,Eulenfeld Interiors & Construction,"604 E Lake Dr, Taylor, TX 76574, United States",https://eulenfeldinc.com/,https://www.google.com/maps/place/?q=place_id:ChIJw3f5KS7nRIYR_cXXH37l6Fs&hl=en,none,none
1347,Anderson & Hammack Construction Company,"301 Tower Ave, Superior, WI 54880, United States",https://andersonhammack.com/,https://www.google.com/maps/place/?q=place_id:ChIJBSdhzARSrlIRLQyGlJgfkQ0&hl=en,https://www.facebook.com/andersonhammack https://www.facebook.com/presalliancemn,none
1348,Simler Solutions LLC | General Contractor & Handyman,,https://www.simlersolutions.com/,https://www.google.com/maps/place/?q=place_id:ChIJ486sZAFedU4RtmF6dxAiBA4&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/profile.php,https://www.instagram.com/simlersolutions
1349,Strong Builders LLC,"6314 Calhoun Memorial Hwy Ste A, Easley, SC 29640, United States",https://www.strongbuildersllc.net/,https://www.google.com/maps/place/?q=place_id:ChIJc6sCgtpHWIgRyJNg2i0Fad4&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/strongbuildersllc,none
1350,Dependable Home Improvements,"596 Broadway, Massapequa, NY 11758, United States",https://www.dhihomeimprovements.com/,https://www.google.com/maps/place/?q=place_id:ChIJPZHsJFTV6YkRnVJL74gwtj4&hl=en,none,https://www.instagram.com/dhicontracting
1351,"Griffin Finish Works, LLC",,https://www.griffinfinishworks.com/,https://www.google.com/maps/place/?q=place_id:ChIJ11cwP_ayj6AR5gVpujbIeEU&hl=en,http://www.facebook.com/griffinfinishworks,none
1352,J Pro Remodel,,https://jproremodel.com/,https://www.google.com/maps/place/?q=place_id:ChIJD7jHgvIjYGYRby0W7V2AkpA&hl=en,none,none
1353,Florez MIllwork,"300 Race Ave Bldg 6, Waynesboro, VA 22980, United States",https://florezmillwork.com/,https://www.google.com/maps/place/?q=place_id:ChIJveUnUztjs4kRRsPM_uorf48&hl=en,none,none
1354,Vito Home Remodeling,,https://www.vitohomeremodeling.com/,https://www.google.com/maps/place/?q=place_id:ChIJU5sf6WgIt6QRH6V4l_HT0EM&hl=en,none,https://www.instagram.com/vitohomeremodeling
1355,C B Smith Construction Inc,"5148 Meadow Valley Cir, Roanoke, VA 24018, United States",https://www.cbsmithconstruction.com/,https://www.google.com/maps/place/?q=place_id:ChIJ_____68STYgRhXesJk4a28k&hl=en,https://www.facebook.com/maverickroofingva,https://www.instagram.com/maverickroofingva
1356,Stine Home & Yard Natchitoches,"5690 LA-1, Natchitoches, LA 71457, United States",https://www.stinehome.com/,https://www.google.com/maps/place/?q=place_id:ChIJbV_S5_GHMIYRh5s56tSs8Gk&hl=en,http://www.facebook.com/stinehomestore,https://www.instagram.com/stinehome
1357,Creekview Homes and Contracting,,https://www.creekviewhomeswi.com/,https://www.google.com/maps/place/?q=place_id:ChIJz0PLDjih9w8RaTmGF6NYYo8&hl=en,none,none
1358,Precision Interiors & Construction,,https://precisionic.com/,https://www.google.com/maps/place/?q=place_id:ChIJ9WwF51HHRYYRpAzfzvnMuKg&hl=en,http://www.facebook.com/2008/fbml https://www.facebook.com/precisionic,https://www.instagram.com/precision_ic
1359,Jenkins Homes Inc,"1751 Grand Ave, Cañon City, CO 81212, United States",https://www.jenkinshomes.net/,https://www.google.com/maps/place/?q=place_id:ChIJzVBBg-F-E4cR4WkdZg7czHc&hl=en,http://www.facebook.com/2008/fbml,none
```
