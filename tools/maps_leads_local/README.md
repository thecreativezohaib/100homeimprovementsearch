# Google Maps lead finder (runs on your laptop)

Finds kitchen and bath businesses on Google Maps with **no website**, rated **4.5+ from 15+ reviews**, with a review
in the **last 6 months** and **10+ photos**, and saves their details, newest reviews and full-size photos.

## Setup (once)
1. Install Python 3.10+ (python.org). On Windows tick "Add Python to PATH".
2. Open a terminal in this folder and run:
   ```
   pip install playwright
   python -m playwright install chromium
   ```

## Run
Test first (10 searches, 30 businesses each):
```
python maps_leads.py --limit-searches 10 --max-per-search 30
```
Full run (every category in every town):
```
python maps_leads.py
```
- A Chrome window opens and works by itself; leave it alone. The terminal shows every business live: `PASS` or
  `fail` with the reason.
- If Google asks you to prove you are human, solve it in the window and press Enter in the terminal.
- Stop any time with Ctrl+C; running it again continues where it stopped.
- Change the criteria at the top of `maps_leads.py`, the searches in `categories.txt`, the places in `towns.txt`.

## Overnight
1. Install Google Drive for desktop (google.com/drive/download) and sign in. Your Drive appears as a drive letter
   (Windows, usually `G:\My Drive`) or under Finder > Google Drive (Mac).
2. Create a folder `maps_leads` in it.
3. Stop the laptop from sleeping (Windows: Settings > System > Power > Sleep: Never, and plug it in).
4. Run:
   ```
   python maps_leads.py --unattended --drive-folder "G:/My Drive/maps_leads"
   ```
   (Mac: `--drive-folder "$HOME/Library/CloudStorage/GoogleDrive-<your email>/My Drive/maps_leads"`)
5. After the first upload (every 1,000 businesses, and at the end) a file `maps_out_latest.zip` appears in that Drive
   folder. Right-click > Share > "Anyone with the link" > Copy link, and send me the link once: it always opens the
   newest results.

If Google asks for a human check during the night, the script simply waits (20, 40, 60 minutes) and tries again; it
does not try to get around it. If it keeps happening, lower the pace by raising the numbers in `pause()`.

## Emails
Google listings rarely show an email. For every business that passes, the script adds a line to
`maps_out/email_todo.csv` with any email it found on the Google listing and the business's Facebook / Instagram links.
Only those businesses need an email search (with a screenshot of the email on their own page).

## Send the results
Zip the `maps_out` folder (it holds `leads_all.csv` and `qualified/` with a folder per business) and share it.
