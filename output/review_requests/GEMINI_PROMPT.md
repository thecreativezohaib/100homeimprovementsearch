# Google review dates: what I need and how to get it

## Why only 109 firms
G4 needs two different kinds of activity since 2026-07-16. Google reviews count as one kind, however many there are.
So fuller review data can only rescue firms that already have one non-review signal (a dated post on their own
site) and fail nothing else. There are 109 of those:

- 8 that the regional agents already searched and failed only G4.
- 101 that also need a PSI score below 60 for G8. I will run PSI myself in the session that has the API key.

Firms whose only signal is already a Google review cannot be helped by more reviews, so they are not on this list.

Files in this folder:
- `targets.csv`: all 109, with the Maps link for each.
- `batch1.txt` to `batch5.txt`: the same list in groups of 25 (batch 5 has 9), ready to paste.

## What I need for each business
| Column | What to put |
|---|---|
| `row` | The row number from the batch file. |
| `business_name` | As shown on Google Maps. |
| `maps_url` | The Google Maps link the data came from. |
| `checked_on` | The date you looked, YYYY-MM-DD. |
| `newest_review_when` | The date text exactly as Google shows it for the newest review ("3 weeks ago", "2 months ago"). |
| `newest_review_edited` | `yes` if the date line says "Edited", otherwise `no`. |
| `newest_reviewer` | The reviewer name exactly as shown. |
| `newest_review_first_words` | The first 10 to 15 words of that review, copied exactly. |
| `second_review_when`, `second_reviewer` | The same for the next newest review that is not edited (only needed if the newest one is edited). |
| `owner_reply_when` | The date text of the owner's reply to the newest review, or `none`. |
| `rating`, `review_count` | For example `4.8` and `34`. |
| `status_note` | `ok`, `closed` if Google says permanently or temporarily closed, or `not found`. |

If something isn't shown, write `UNKNOWN`. Don't estimate a date.

## Prompt to paste into Gemini (once per batch)
```
Use Google Maps to look up each business below. For each one, open its Google Maps reviews, sort them by
"Newest", and report the newest review. Do not guess or estimate anything. If you cannot see a value, write
UNKNOWN. If you cannot find the business, write "not found" in status_note.

Return ONLY a CSV with this exact header and one line per business, in the same order as the list:
row,business_name,maps_url,checked_on,newest_review_when,newest_review_edited,newest_reviewer,newest_review_first_words,second_review_when,second_reviewer,owner_reply_when,rating,review_count,status_note

Rules:
- newest_review_when: the date text exactly as Google shows it (for example "3 weeks ago").
- newest_review_edited: "yes" if the date line says "Edited", otherwise "no".
- If the newest review is edited, fill second_review_when and second_reviewer with the next newest review that is not edited.
- newest_review_first_words: copy the first 10 to 15 words of the review exactly, in double quotes.
- checked_on: today's date as YYYY-MM-DD.
- maps_url: copy the link I gave you for that business.

Businesses (row. name | address | phone | Google Maps link):
<PASTE THE CONTENTS OF ONE batchN.txt FILE HERE>
```

## Checking Gemini's output (please do this)
Gemini can return dates it didn't actually read. Before you send me the results, pick 5 rows from each batch.
Open their Maps links while signed in to Google, sort reviews by Newest, and check that the newest review date
and the reviewer name match. If any row doesn't match, redo that batch by hand. Tell me which rows you checked
so I can record them as verified. Rows you didn't check will be marked as Gemini-sourced in `evidence.csv`.

## The fully manual alternative (about an hour, most reliable)
Signed in to Google in Chrome, open each link in `targets.csv`, click Reviews, then Sort, then Newest, and fill
in the same columns in a copy of `targets.csv`. It takes about 30 seconds per business.

## Sending it back
Paste the CSV into the chat, or save it as `output/review_requests/results_batchN.csv` and commit it. Don't
include any API keys or passwords.
