# Homepage kit: 100 kitchen and bath remodellers

Everything needed to build one homepage per business from a single master template. Each page has its own copy, built
from that firm's real site, Google Business Profile, reviews and photos.

## Start here
| File | What it is | Give it to |
|---|---|---|
| `ALL_100_content.json` (3 MB) | All 100 businesses: key facts, Google profile, socials, original photos, and the finished homepage copy in the template structure | the page builder (best single file) |
| `ALL_100_content.md` | The same copy as readable text, one section per business, with conversion notes and the list of missing facts | you, for reading and review |
| `ALL_100.json` (40 MB) | Everything in one file: the content plus every crawled page's text, headings, meta tags, every image URL with alt text and size, outbound and social links, JSON-LD, full Google profile and reviews, verified research | Claude, when it needs raw detail |
| `data/<id>.json` | The same full record, one file per business | Claude, one business at a time |
| `content/<id>.json` | The homepage copy for one business | the page builder, one business at a time |
| `CONTENT_BRIEF.md` | The rules the copy was written to: section order, lengths, SEO, writing rules | the template designer |
| `content_schema_example.json` | The exact JSON shape of every `content/<id>.json` | the template designer |
| `index.json` | One summary row per business (name, site, city, phone, owner, rating, counts, defects) | quick lookups |

## Template sections (same order on every page)
seo, hero, intro, services, why_choose_us, about, process, gallery, testimonials, service_area, faq, final_cta, footer,
schema_jsonld. Three more keys are for you, not the page: `conversion_notes` (the firm's measured site defects, what the
new page fixes, the conversion angle and a one-line outreach hook), `facts_used` (every claim with its source URL) and
`missing` (useful facts not found, so left out rather than invented).

## How the copy was made
- Every site was crawled with a real browser (up to 16 to 20 pages each; a plain Python fallback for one plain-HTTP
  site), plus the Google Business Profile capture and the verified research from the prospect list.
- Each homepage was written from that data only. One primary keyword per page (main service + main city) placed in
  the title tag, H1, first paragraph, one H2 and the hero alt text. Title tags 50 to 60 characters, meta descriptions
  140 to 160.
- Name, address and phone follow the Google Business Profile exactly. Where the firm's own site shows a different phone
  or address, the page uses Google's and the mismatch is flagged in `conversion_notes`.
- Testimonials are real reviews quoted exactly, first name and last initial (first name alone where Google shows only
  that). Images come only from the firm's own site; writers viewed the photos before writing alt text and left out
  stock, logo, AI-looking and sideways images. Schema carries no aggregateRating.
- `tools/validate_content.py` checks all 100 files: required keys, lengths, banned filler and em dashes, testimonials
  verbatim against captured reviews and site text, images from known URLs, and no paragraph shared between two firms.
  Result: checked 100, with issues 0, duplicated paragraphs across firms 0.

## Known exceptions
- Completely Kitchens: 2 testimonials (Google shows only two positive reviews; the site prints none). One review had its
  em dashes changed to spaced hyphens, noted in `facts_used`.
- Pereira Construction (pcsouthflorida.com): one-page site, so 5 gallery photos and 3 services.
- Callen Construction: every captured review is about windows and doors.
- Several firms have no street address on Google; their footers name the city only.

## The 100 businesses
| Business | Website | Google city | Tier | Primary keyword |
|---|---|---|---|---|
| MJ Kitchen & Bath | https://mj-kitchens.com/ | Plymouth, MI | strict | kitchen remodeling Plymouth |
| Majestic Home Solutions LLC | https://www.majestichomesolutions.com/ | Sterling Heights, MI | strict | remodeling contractor Sterling Heights |
| AC Remodeling Inc. | https://acremodeling.com/ | Gaithersburg, MD | strict | design-build remodeling Gaithersburg MD |
| JDI Construction | https://www.jdiconstruction.co/ | Vancouver, WA | strict | kitchen remodeling Vancouver WA |
| 3 Day Cabinet Pros and More | https://3daycabinetprosandmore.com/ | Machesney Park, IL | strict | kitchen remodeling Machesney Park IL |
| All Exclusive Construction Inc | https://www.allexclusivepro.com/ | Westlake Village, CA | strict | bathroom remodeling Westlake Village |
| Ann Arbor Remodeling | https://annarborremodelingllc.com/ | Ann Arbor, MI | strict | design-build remodeling Ann Arbor |
| Assembly Squad Remodeling Chicago | https://www.assemblyserviceil.com/ | Chicago, IL | strict | condo remodeling Chicago |
| Craft Home Remodeling | https://crafthomeremodel.com/ | San Diego, CA | strict | bathroom remodeling San Diego |
| Forward Design Build Remodel | https://planforward.net/ | Ann Arbor, MI | strict | kitchen remodeling Ann Arbor |
| Hamlett Renovations | https://www.hamlettrenovations.com/ | Wayne, NJ | strict | kitchen remodeling Wayne NJ |
| McDonald Remodeling | https://www.mcdonaldremodeling.com/ | Inver Grove Heights, MN | strict | kitchen remodeler Inver Grove Heights |
| ALL Renovation & Design LLC | https://allrd.com/ | Manheim, PA | strict | kitchen remodeling Lancaster PA |
| Boss Design Center Bath and Kitchen Remodeling | https://bossdesigncenter.com/ | Bethesda, MD | strict | kitchen remodeling Bethesda |
| Degnan Design-Build-Remodel | https://degnandesignbuildremodel.com/ | Windsor, WI | strict | kitchen remodeling Madison WI |
| KBF Design Gallery | https://www.kbfdesigngallery.com/ | Maitland, FL | strict | kitchen remodeling Maitland |
| Nip Tuck Remodeling | https://niptuckremodel.com/ | Bellevue, WA | strict | kitchen remodeling Bellevue |
| Semper Fi Custom Remodeling of Asheville | https://sfcustomremodeling.com/ | Black Mountain, NC | strict | kitchen remodeling Asheville NC |
| Sweeney Design Remodel | https://sweeneydesign.com/ | Madison, WI | strict | design-build remodeling Madison WI |
| Wade Design & Construction Inc. | https://wadedesigninc.com/ | Mequon, WI | strict | kitchen and bath remodeling Mequon |
| Wood Contracting Chicago | https://www.woodcontractingchicago.com/ |  | strict | bathroom remodeling Chicago |
| Anani Remodeling | https://www.ananiremodeling.com/ | Roseville, CA | strict | kitchen remodeling Roseville |
| Better Remodels | https://betterremodels.com/ | Orange, CA | strict | kitchen remodeling Orange County |
| Five Fold Solutions | https://www.fivefoldkc.com/ | Overland Park, KS | strict | bathroom remodeling Overland Park |
| Keselman Construction Group Inc | https://keselmangroup.com/ | Solon, OH | strict | kitchen remodeling Cleveland |
| Kitchen Barn, Inc | https://www.kitchenbarn.net/ | Poway, CA | strict | kitchen remodeling Poway |
| ARIID Build & Remodel | https://ariidbuild.com/ | Kirkland, WA | strict | design-build remodeling Kirkland WA |
| Gayler Design Build | https://gaylerdesignbuild.com/ | Danville, CA | strict | kitchen remodeling Danville CA |
| Kellow Construction | https://www.kellowconstruction.com/ | Santa Barbara, CA | strict | kitchen remodeling Santa Barbara |
| RIKB Design Build | https://rikb.com/ | Warwick, RI | strict | kitchen and bath remodeling Warwick |
| A+ Custom builders | https://www.buildwithaplus.com/ | Seekonk, MA | strict | bathroom remodeling Seekonk MA |
| AZ New Bath | https://aznewbath.com/ |  | strict | bathroom remodeling Peoria AZ |
| Bayshore Remodels | https://www.bayshoreremodels.com/ | Largo, FL | strict | kitchen remodeling Largo FL |
| C&S Remodeling | https://www.cs-enterprises.net/ | San Antonio, TX | strict | bathroom remodeling San Antonio |
| Craftsman Design and Renovation | https://www.craftsmandesign.com/ | Portland, OR | strict | kitchen remodeling Portland |
| ELITE Remodels | https://remodelsbyelite.com/ | Santa Barbara, CA | strict | kitchen remodeling Santa Barbara |
| ELM Construction LLC | https://www.elmbuilds.com/ | Homewood, AL | strict | kitchen remodeling Homewood |
| Elite Kitchen & Bath / Express Contracting | https://www.elitekb.com/ | Manhasset, NY | strict | luxury kitchen remodeling Manhasset |
| Golden Era Remodel | https://www.goldeneraremodel.com/ |  | strict | bathroom remodeling Dallas-Fort Worth |
| Goldsmith Remodel and Design | https://www.goldsmithremodelanddesign.com/ |  | strict | kitchen remodeling Rochester MN |
| H&H Signature Renovations | https://hhsrenovations.com/bathroom-remodeling/lake-worth-beach/ | Lake Worth Beach, FL | strict | bathroom remodeling Lake Worth Beach |
| HDR Remodeling | https://hdrremodeling.com/ | Emeryville, CA | strict | kitchen remodeling Berkeley |
| Haven Reno KC | https://www.havenrenokc.com/ | Lee's Summit, MO | strict | bathroom remodeling Lee's Summit |
| JBJ Building & Remodeling Inc | https://jbjbuildersincmi.com/ | Comstock Park, MI | strict | bathroom remodeling Grand Rapids |
| Premier Design-Build-Remodel | https://premierkitchenandbath.com/showroom/scottsdale/ | Scottsdale, AZ | strict | kitchen remodeling Scottsdale AZ |
| Red Fox Remodeling | https://www.redfoxremodeling.com/ | Minneapolis, MN | strict | kitchen remodeling Minneapolis |
| Remont Remodeling | https://remontremodel.com/ | Redmond, WA | strict | bathroom remodeling Redmond WA |
| Renovating KC Design + Remodel | https://www.renokc.com/ | Lenexa, KS | strict | kitchen remodeling Kansas City |
| Straight Line Design and Remodeling LLC | https://www.straightlinedr.com/ |  | strict | kitchen remodeling Lake Oswego |
| The Bath Remodeling Center | https://thebathremodelingcenter.com/ | Cary, NC | strict | bathroom remodeling Cary NC |
| Thrive Home Construction | https://thrivehomeconstruction.com/ | Sacramento, CA | strict | bathroom remodeling Sacramento |
| Transitions Kitchens, Baths and Remodeling | https://transitionskbr.com/ | Norwell, MA | strict | kitchen remodeling Norwell MA |
| Wise Design & Remodel LLC | https://www.wisedesignremodel.com/ | St Paul, MN | strict | kitchen remodeling St. Paul |
| Wright's Renovations | https://wrights-renovations.com/ |  | strict | design-build remodeling Ann Arbor |
| Your Dream Remodeling | https://yourdreamremodeling.com/ | Houston, TX | strict | bathroom remodeling Houston |
| Alpha General Construction | https://alphagenco.com/ |  | strict | bathroom remodeling Midland TX |
| Creative Cabinets and Fine Finishes, LLC | https://ccfauxfinishes.com/ | Marietta, GA | strict | kitchen remodeling Marietta |
| Kitchen Concepts NW LLC | https://kitchenconceptsinoregon.com/ | Gresham, OR | strict | kitchen remodeling Gresham OR |
| Newberry Home Improvement | https://www.newberryhome.com/ | Wilmington, NC | strict | cabinet refacing Wilmington NC |
| Pacific Remodeling- Bathroom and Kitchen Remodeling Puyallup WA | https://pacificremodelingllc.com/ |  | strict | bathroom remodeling Puyallup WA |
| Renovations and Dependable Building | https://www.renodb.com/ |  | strict | bathroom remodeling Blacksburg VA |
| S&W Kitchens | https://sandwkitchens.com/showrooms/sarasota/ | Sarasota, FL | strict | kitchen and bath remodeling Sarasota FL |
| Guthrie Kitchen And Bath Plus | https://guthriekitchenandbath.com/ | Pleasant View, TN | strict | kitchen remodeling Pleasant View TN |
| Kitchen Places | http://kitchenplacesventura.com/ | Ventura, CA | strict | kitchen remodeling Ventura |
| Aptitude Design & Build | https://www.aptitudedesignandbuild.com/ | St Charles, MO | relaxed | kitchen remodeling St. Charles |
| Big Build Construction | https://bigbuildconstruction.net/ | Kent, WA | relaxed | bathroom remodeling Kent WA |
| Completely Kitchens | https://www.completelykitchens.com/ | Ames, IA | relaxed | kitchen remodeling Ames |
| Custom Kitchens Inc | https://customkitchensinc.net/ | Richmond, VA | relaxed | kitchen remodeling Richmond VA |
| Modern Kitchen | https://modernkitchen.net/ | Elkhart, IN | relaxed | kitchen remodeling Elkhart |
| Mountaineer Kitchens & Baths | https://www.mountaineerkitchensandbaths.com/ | Martinsburg, WV | relaxed | kitchen remodeling Martinsburg WV |
| OKC Kitchen & Bath | https://okckitchenandbath.com/ |  | relaxed | kitchen remodeling Oklahoma City |
| Specialty Kitchens and Baths, LLC | https://www.specialtykitchensandbaths.com/ |  | relaxed | bathroom remodeling Warren MI |
| Wreedone | https://getwreedone.com/ |  | relaxed | kitchen remodeling Denton TX |
| Your New Baths | https://www.yournewbaths.com/offer/ |  | relaxed | bathroom remodeling Boardman OH |
| Affordable Remodeling Solutions | https://affordableremodelingsolutions.com/ | Raleigh, NC | relaxed | kitchen remodeling Raleigh NC |
| Callen Construction, Inc. | https://www.callenconstruction.com/ | Delafield, WI | relaxed | kitchen remodeling Delafield WI |
| JC Custom Cabinets Kitchen And Bath Remodeling Temecula | https://cervantescabinets.com/ |  | relaxed | kitchen remodeling Temecula |
| Schock Construction and Design | https://schockinc.com/ | Issaquah, WA | relaxed | kitchen remodeling Issaquah |
| Stebnitz Builders Inc | https://www.stebnitzbuilders.com/ | Elkhorn, WI | relaxed | kitchen remodeling Elkhorn |
| USA Home Remodeling | https://usahomeremodeling.com/ | Irvine, CA | relaxed | kitchen remodeling Irvine |
| White Birch Design, LLC | https://whitebirchdesignllc.com/ | Lakeville, MN | relaxed | kitchen remodeling Lakeville |
| Woodsman Kitchens & Floors | https://www.woodsman.biz/ | Jacksonville, FL | relaxed | kitchen remodeling Jacksonville |
| Bennett Contracting, LLC | https://bennettcontracting.com/ | Albany, NY | relaxed | kitchen remodeling Albany NY |
| Elevate Remodeling | https://www.elevate-remodeling.com/ | Columbus, OH | relaxed | kitchen remodeling Columbus Ohio |
| Elite Construction Services Inc | https://www.discoverelite.com/ | Santa Cruz, CA | relaxed | kitchen remodeling Santa Cruz |
| Halco Kitchen & Bath | https://www.halcokb.com/ | Malden, MA | relaxed | kitchen remodeling Malden MA |
| Integral Renovations | https://integralrenovations.co/ | Buford, GA | relaxed | bathroom remodeling Buford GA |
| Laplante Cabinetry | https://www.laplantecabinetry.com/ | Gray, ME | relaxed | custom kitchen cabinetry Gray ME |
| North2South Renovations- Bathroom Remodeling | Kitchen Remodeling | https://north2southflo.com/ | Delray Beach, FL | relaxed | bathroom remodeling Delray Beach FL |
| Palmhouse Design & Build | https://palmhousedesign.com/ | Jupiter, FL | relaxed | kitchen remodeling Jupiter FL |
| Rohrer For Construction | https://rohrerforconstruction.com/ |  | relaxed | kitchen and bath remodeling Lake County IL |
| Stevens Kitchens | https://www.stevenskitchens.com/ | Oviedo, FL | relaxed | kitchen remodeling Oviedo FL |
| Treasure Valley Redesign & Remodel | https://www.tvremodel.com/ | Caldwell, ID | relaxed | kitchen remodeling Caldwell |
| APlus Interior Design & Remodeling | https://www.aplushomeimprovements.com/ | Anaheim, CA | relaxed | kitchen remodeling Anaheim |
| GMH CONSTRUCTION | https://gmh-remodeling.com/services/ | Waukesha, WI | relaxed | kitchen remodeling Waukesha |
| Upscale Remodeling | https://upscaleremodeling.com/ | Freeville, NY | relaxed | kitchen remodeling Ithaca NY |
| VanderBeken Remodel | https://vanderbekenremodel.com/ | Marysville, WA | relaxed | kitchen remodeling Marysville WA |
| Clar Construction | https://clarconstruction.com/ | Montpelier, VT | relaxed | kitchen remodeling Montpelier VT |
| Pereira Construction of South FL, Inc. | https://www.pereiraconstructionsouthfl.com/ |  | relaxed | bathroom remodeling Lake Worth |
| Sicora Design / Build | https://sicora.com/ | Minneapolis, MN | relaxed | kitchen remodeling Minneapolis |
