#!/usr/bin/env python3
"""Single outreach file for the 100 live homepage concepts: output/OUTREACH_100.xlsx (one row per business with every
contact channel and the email drafts), plus OUTREACH_100.csv with the same columns.
Inputs: data/outreach_base.json (tools/outreach_base.py) and data/outreach_drafts_*.json (the drafts).
Usage: build_outreach.py"""
import csv, glob, json
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

R = "/home/user/100homeimprovementsearch"
COLS = [("n", "#", 5), ("business_name", "Business", 26), ("owner", "Owner / contact", 20), ("owner_role", "Role", 16),
        ("old_site", "Current website", 30), ("new_concept", "New homepage concept", 40),
        ("google_phone", "Phone (Google profile)", 16), ("other_phones", "Other phones on their site", 22),
        ("whatsapp", "WhatsApp", 26), ("email", "Best email", 30), ("other_emails", "Other emails", 26),
        ("email_source", "Email found on", 30), ("contact_form_url", "Contact form", 30), ("facebook", "Facebook", 34),
        ("instagram", "Instagram", 34), ("other_socials", "Other profiles (Houzz, LinkedIn, YouTube...)", 40),
        ("address", "Address", 30), ("google_rating", "Google rating", 12), ("google_profile", "Google profile", 30),
        ("key_issue", "Main issue on current site", 50), ("subject", "Email subject", 34), ("email_body", "Email (day 1)", 70),
        ("follow_up_1", "Follow-up 1 (day 4)", 55), ("follow_up_2", "Follow-up 2 (day 11)", 50),
        ("short_dm", "Short message (Facebook / Instagram / SMS / WhatsApp)", 50), ("personalization_notes", "Why this angle", 40)]


def main():
    base = {r["n"]: r for r in json.load(open(f"{R}/data/outreach_base.json"))}
    drafts = {}
    for f in sorted(glob.glob(f"{R}/data/outreach_drafts_*.json")):
        for d in json.load(open(f)):
            drafts[int(d["n"])] = d
    rows = []
    for n in sorted(base):
        b, d = base[n], drafts.get(n, {})
        s = b["socials"]
        best = b["verified_email"] or (b["emails"][0] if b["emails"] else "")
        cd = (b["conversion_notes"] or {}).get("current_site_defects") or []
        rows.append({
            "n": n, "business_name": b["business_name"], "owner": b["owner"] or "", "owner_role": b["owner_role"] or "",
            "old_site": b["old_site"], "new_concept": b["new_concept"], "google_phone": b["google_phone"] or "",
            "other_phones": ", ".join(p for p in b["all_phones"] if p != b["google_phone"]),
            "whatsapp": ", ".join(b["whatsapp_links_on_site"]) or "Not listed on their site (try the phone number on WhatsApp)",
            "email": best, "other_emails": ", ".join(e for e in b["emails"] if e != best),
            "email_source": b["email_source"] or "", "contact_form_url": b["contact_form_url"] or (b["old_site"] if not best else ""),
            "facebook": "\n".join(s.get("facebook", [])), "instagram": "\n".join(s.get("instagram", [])),
            "other_socials": "\n".join(u for k, v in s.items() if k not in ("facebook", "instagram") for u in v),
            "address": b["address"] or "", "google_rating": b["google_rating"], "google_profile": b["google_profile"] or "",
            "key_issue": "; ".join(b["measured_defects"]) or (cd[0] if cd else ""),
            **{k: d.get(k, "") for k in ("subject", "email_body", "follow_up_1", "follow_up_2", "short_dm", "personalization_notes")}})

    wb = Workbook(); ws = wb.active; ws.title = "Outreach"
    ws.append([c[1] for c in COLS])
    for r in rows:
        ws.append([r[c[0]] for c in COLS])
    head = PatternFill("solid", fgColor="2B2420")
    for i, (_, _, w) in enumerate(COLS, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
        c = ws.cell(1, i); c.font = Font(bold=True, color="FFFFFF"); c.fill = head; c.alignment = Alignment(wrap_text=True, vertical="top")
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "C2"; ws.auto_filter.ref = ws.dimensions

    g = wb.create_sheet("How to use")
    for line in [
        "How to use this file",
        "1. One row per business. 'New homepage concept' is the free preview you built; 'Current website' is their live site.",
        "2. Replace [Your Name], [Your Company], [Your Phone / WhatsApp] and [Your Business Address] in every email before sending.",
        "   US law (CAN-SPAM) requires a real postal address and a working opt-out in commercial email; the drafts already include the opt-out line.",
        "3. Send the day-1 email, then follow-up 1 after 3 days and follow-up 2 after 7 more days, only if there is no reply. Stop as soon as anyone says no.",
        "4. No email? Use the contact form link, then the short message on Facebook or Instagram.",
        "5. WhatsApp: none of these businesses links WhatsApp on its own site. The short message can be sent by SMS or WhatsApp to the Google phone,",
        "   but most US business lines are not on WhatsApp, so a phone call or SMS is the safer second channel.",
        "6. Send in small batches (10 to 20 a day) from a warmed-up mailbox to protect deliverability; personalised plain-text emails work best.",
        "7. Emails marked 'Email found on: careers page' reach staff, not the owner; consider the contact form or a call first for those.",
    ]:
        g.append([line])
    g.column_dimensions["A"].width = 140
    g["A1"].font = Font(bold=True, size=14)
    wb.save(f"{R}/output/OUTREACH_100.xlsx")

    with open(f"{R}/output/OUTREACH_100.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow([c[1] for c in COLS])
        for r in rows:
            w.writerow([r[c[0]] for c in COLS])
    print("rows", len(rows), "with drafts", sum(1 for r in rows if r["email_body"]))


if __name__ == "__main__":
    main()
