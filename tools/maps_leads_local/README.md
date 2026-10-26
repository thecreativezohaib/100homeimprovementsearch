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

## Send the results
Zip the `maps_out` folder (it holds `leads_all.csv` and `qualified/` with a folder per business) and share it.
