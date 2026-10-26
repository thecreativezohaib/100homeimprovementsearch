# Photo check brief (round 3)

Another AI (Antigravity) collected photos for small kitchen and bath remodeling businesses from their Facebook,
Instagram and Google pages. Earlier runs of it often grabbed photos of unrelated people, news, stock images or other
companies with a similar name, so every photo must be checked by eye before a homepage uses it.

Folders are under /tmp/claude-0/-home-user-100homeimprovementsearch/f4353c7d-d573-58ad-81e2-652b0f6f72ae/scratchpad/r3dl/n1/<folder>/:
- sheet.jpg: all images numbered by file name (look at this first; open single images in images/ when unsure)
- photos.csv: file, source_page, what_it_shows (Antigravity's claims, not trusted)
- info.json: business_name, phone, facebook_url, instagram_url, email, email_seen_on, reviews, notes

For each image decide:
- keep: a real photo of remodeling work that plausibly belongs to this business (kitchens, baths, showers, tile,
  cabinets, counters, floors, before/after, their crew at work, their truck or shop, their own sign), or their own logo.
- reject: unrelated content (people's portraits, food, events, memes, news, sports), stock or catalogue images,
  manufacturer or real-estate listing photos (MLS watermarks), photos branded with ANOTHER company's name or phone,
  pure text flyers, screenshots of web pages, duplicates, tiny or broken images.
Also reject the whole set if the photos clearly belong to a different business than business_name (other company
names on logos, signs, trucks or watermarks), and say so.
Check source_page: photos whose source page is not the business's own Facebook, Instagram or Google page (another
company's site, Yelp of another business, a group post by someone else) are rejected unless the image itself shows
this business's own name.

Write your verdicts as one JSON object to the output file you were given:
{"<folder>": {"keep": ["images/fb_01.jpg", ...], "logo": "images/logo.jpg" or null,
              "reject": {"images/fb_05.jpg": "reason", ...},
              "kitchen_bath_photos": <count of kept photos showing kitchen, bath, shower, tile, cabinet or counter work>,
              "identity": "ok" or "doubt: <why>", "note": "<anything important>"}}
Do nothing else and change no files except your output file. Reply with one line per folder: kept, rejected,
kitchen_bath_photos, identity.
