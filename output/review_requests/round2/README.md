# Review dates, round 2 (771 firms)

These firms pass every other check: website, no web vendor, independence, photos, a measured defect and paid-spend
proof. What they lack is proof of activity since 2026-07-16. A recent Google review is one of the two kinds of
activity that G4 needs.

- **Batches 01 to 03 (rows 1 to 58), priority A:** each already has a dated post on its own LinkedIn, YouTube or
  Pinterest account. A recent review gives it the second kind, so these are the most likely to pass.
- **Batches 03 to 31, priority B:** no activity found yet. A recent review gives them one kind, and I then search
  for the second (job posts, permits, social accounts).

Please do batches 01 to 03 first. Send results whenever you have some; you don't have to finish all 31 batches.

## Prompt for Gemini (once per batch)
Use the same prompt as round 1 (`../GEMINI_PROMPT.md`), and paste the contents of one `batchNN.txt` file at the
bottom. The output columns stay the same:

```
row,business_name,maps_url,checked_on,newest_review_when,newest_review_edited,newest_reviewer,newest_review_first_words,second_review_when,second_reviewer,owner_reply_when,rating,review_count,status_note
```

What matters most to me:
- `newest_review_when`: the exact date (YYYY-MM-DD) if Gemini can see it, otherwise the text as shown ("3 weeks ago").
- `newest_review_first_words`: the first 10 to 15 words, copied exactly.
- `status_note`: `closed` if Google shows the business as closed.

The row numbers continue across batches (1 to 771) and match `targets.csv`.

## Sending it back
Upload the CSV files or a zip here, as you did last time. Last time, signed-in checks of 4 firms were enough. After
I load the results, I'll tell you which few to check.
