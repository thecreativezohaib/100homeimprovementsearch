#!/usr/bin/env python3
"""Relaxed tier (user-approved 2026-10-20): re-fetch verbatim owner and email evidence from each firm's own site.
For each (id, expected owner name) it fetches the home page and common about / team / contact paths, plus the
rendered page text already captured (data/rt*_out*.jsonl), and records the first snippet (at most 20 words) where
the name appears next to an ownership role, with its URL; also the first mailto or visible email on the site.
Writes data/relaxed_evidence.jsonl. Usage: relaxed_evidence.py"""
import json, re, sys, glob
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, D  # noqa: E402
from sitecheck import HDRS  # noqa: E402
OWN = {
 "aptitudedesignandbuild.com": "Matt Mierek", "bigbuildconstruction.net": "Oleg Nikityuk", "customkitchensinc.net": "Richard Hendrick",
 "mountaineerkitchensandbaths.com": "Ben DeOms", "specialtykitchensandbaths.com": "Howard Emmer", "affordableremodelingsolutions.com": "Jonathan Doering",
 "cervantescabinets.com": "Joel Cervantes", "woodsman.biz": "Brad Mangold", "whitebirchdesignllc.com": "Steve McDonald", "halcokb.com": "Tyler Procopio",
 "modernkitchen.net": "Mark Jones", "bennettcontracting.com": "Andrew Gutman", "usahomeremodeling.com": "Isaac Rozolyo", "callenconstruction.com": "Michael Wood",
 "schockinc.com": "Steve Schock", "rohrerforconstruction.com": "Adolph Rohrer", "elevate-remodeling.com": "Michael Freed", "palmhousedesign.com": "Oscar Barrig",
 "north2southflo.com": "Colby Matheny", "gmh-remodeling.com": "Greg Perkins", "upscaleremodeling.com": "Steve Nash", "pcsouthflorida.com": "Robert Pereira",
 "clarconstruction.com": "Dan Clar", "stebnitzbuilders.com": "Chris Stebnitz", "tvremodel.com": "Michael Kuhn", "stevenskitchens.com": "Steve Tedesco",
 "completelykitchens.com": "Becky Jones", "discoverelite.com": "Eric Lamascus", "getwreedone.com": "Wil Reed", "okckitchenandbath.com": "Ryan Johnson",
 "aplushomeimprovements.com": "Alex Tabrizi", "vanderbekenremodel.com": "Ron VanderBeken", "laplantecabinetry.com": "Ryan Laplante",
 "yournewbaths.com": "Brandon Moore", "sicora.com": "Ron Sonnek", "integralrenovations.co": "Taylor Scalera", "southfloridahomeremodelingllc.com": "David Lang"}
ROLE = re.compile(r"Co-?Owner|Owner|Co-?Founder|Founder|President|CEO|Principal|Proprietor", re.I)
PATHS = ["", "about", "about-us", "about/our-team", "our-team", "team", "meet-the-team", "our-story", "who-we-are", "contact", "contact-us", "company"]
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def texts(cid, base):
    out = []
    for f in glob.glob(f"{D}/rt*_out*.jsonl"):
        for l in open(f):
            r = json.loads(l)
            if r["id"] == cid:
                out += [(p["url"], p.get("text") or "", p.get("mailto") or []) for p in r.get("pages", [])]
    for p in PATHS:
        u = base.rstrip("/") + ("/" + p if p else "/")
        try:
            r = requests.get(u, headers=HDRS, timeout=15)
            if r.status_code != 200:
                continue
            s = BeautifulSoup(r.text, "lxml")
            mt = [a["href"] for a in s.select('a[href^="mailto:"]')]
            for t in s(["script", "style", "noscript"]):
                t.decompose()
            out.append((u, s.get_text(" "), mt))
        except Exception:
            pass
    return out


def one(cid, name, base):
    rec = {"id": cid, "owner": name, "owner_url": None, "owner_quote": None, "email": None, "email_url": None, "email_how": None}
    for u, t, mt in texts(cid, base):
        t = re.sub(r"\s+", " ", t)
        if not rec["owner_quote"]:
            for m in re.finditer(re.escape(name), t):
                win = t[max(0, m.start() - 60):m.end() + 60]
                if ROLE.search(win):
                    w = t[max(0, m.start() - 50):m.end() + 70].split()
                    rec["owner_url"], rec["owner_quote"] = u, " ".join(w[:20]); break
        if not rec["email"]:
            for h in mt:
                e = h[7:].split("?")[0].strip()
                if "@" in e and "example" not in e and "mysite" not in e:
                    rec.update(email=e, email_url=u, email_how="mailto"); break
        if not rec["email"]:
            for e in EMAIL.findall(t):
                if not e.lower().endswith((".png", ".jpg", ".webp", ".svg")) and "example" not in e and "mysite" not in e and "sentry" not in e:
                    rec.update(email=e, email_url=u, email_how="visible text"); break
    return rec


if __name__ == "__main__":
    site = load()[1]
    with open(f"{D}/relaxed_evidence.jsonl", "w") as f, ThreadPoolExecutor(12) as ex:
        for rec in ex.map(lambda kv: one(kv[0], kv[1], site[kv[0]]["final_url"]), OWN.items()):
            f.write(json.dumps(rec) + "\n")
            print(rec["id"], "|", rec["owner_quote"], "|", rec["email"])
