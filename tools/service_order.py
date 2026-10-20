#!/usr/bin/env python3
"""Relaxed NICHE check (user-approved 2026-10-20): kitchen and bath must be the first two service lines a firm advertises,
even when its page title is generic home remodelling. Reads rendered home-page text (render_text.js output), finds the
first occurrence of each service keyword, and reports the order plus a verbatim quote (at most 20 words) around the
first service mention. Every result is reviewed by the coordinator. Usage: service_order.py <rt_out*.jsonl ...>"""
import json, re, sys
SERV = {"kitchen": r"kitchen", "bath": r"bath(room)?s?\b|shower", "basement": r"basement", "addition": r"addition",
        "whole home": r"whole[- ]?(home|house)", "deck": r"\bdecks?\b|patio|outdoor living", "roof": r"roof", "siding": r"siding",
        "exterior": r"exterior", "window": r"windows?\b|doors?\b", "custom home": r"custom home|new (home|construction)",
        "flooring": r"flooring", "painting": r"painting", "adu": r"\bADUs?\b", "commercial": r"commercial", "garage": r"garage"}


def order(text):
    t = re.sub(r"\s+", " ", text)
    # skip the first 300 characters (logo, phone, menu chrome) only when the text is long
    first = {}
    for k, rx in SERV.items():
        m = re.search(rx, t, re.I)
        if m:
            first[k] = m.start()
    return sorted(first, key=first.get), t, first


if __name__ == "__main__":
    for path in sys.argv[1:]:
        for l in open(path):
            r = json.loads(l)
            if not r.get("pages"):
                print(json.dumps({"id": r["id"], "error": r.get("error", "no pages")})); continue
            home = r["pages"][0]
            o, t, first = order(home["text"] or "")
            ok = o[:2] in (["kitchen", "bath"], ["bath", "kitchen"])
            a = min(first.get("kitchen", 10**9), first.get("bath", 10**9))
            w = t[max(0, a - 60):a + 160].split()
            print(json.dumps({"id": r["id"], "ok": ok, "order": o[:5], "url": home["url"], "quote": " ".join(w[:20])}))
