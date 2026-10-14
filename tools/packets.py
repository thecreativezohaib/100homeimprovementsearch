#!/usr/bin/env python3
"""Build per-region agent packets: candidates alive after every automated gate except the parts that need
human-style reading (G4 second signal, G5 confirmation, G6 decision maker, niche confirmation).
Usage: packets.py [--include-done]"""
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from decide import load, niche, g3, g4, g5, g7, g8, g9, jl, D  # noqa: E402


def main():
    data = load()
    L, site, maps, br, psi, dns, manual, pre = data
    done = set(manual) if "--include-done" not in sys.argv else set()
    if os.path.exists(f"{D}/dispatched.txt") and "--include-done" not in sys.argv:
        done |= {l.strip() for l in open(f"{D}/dispatched.txt") if l.strip()}
    # competitor pool: same search location, incumbent-agency sites (G3 fail) that load with viewport+HTTPS
    pool = defaultdict(list)
    for cid, c in L.items():
        s = site.get(cid)
        if not s or s.get("g2") != "PASS":
            continue
        if g3(c, s)[0] == "FAIL" and s.get("viewport_meta") and s.get("final_scheme") == "https":
            for loc in c["locations_seen"]:
                pool[loc].append({"name": c["name"], "url": s["final_url"], "gbp_address": (maps.get(cid) or {}).get("address")})
    packets = defaultdict(list)
    for cid, c in L.items():
        if cid in done:
            continue
        s, m, b, p = site.get(cid), maps.get(cid), br.get(cid), psi.get(cid)
        if c.get("dup_of"):
            continue
        if not s or s.get("g2") != "PASS" or not m or not m.get("title"):
            continue
        if niche(c, s, None)[0] == "FAIL":
            continue
        st3, e3 = g3(c, s)
        bench = st3 != "PASS"
        if bench and not e3.get("g3_vendor"):
            continue
        st4, e4 = g4(c, s, m, None)
        if not e4.get("g4_signals") or st4 == "FAIL":
            continue
        if g5(c, s, None)[0] == "FAIL" or g7(c, s, None)[0] != "PASS":
            continue
        if g8(c, s, b, p)[0] != "PASS" or g9(c, s, b)[0] != "PASS":
            continue
        e8 = g8(c, s, b, p)[1]
        packets[c["region"]].append({
            "id": cid, "name": c["name"], "region": c["region"], "website": s["final_url"],
            "bench_vendor_route": bench, "incumbent_vendor": e3.get("g3_vendor") if bench else None,
            "platform": s.get("platform"), "pages_fetched": s.get("pages_fetched"),
            "auto_signals": e4.get("g4_signals"), "need_signal_types": max(0, 2 - len({x['type'] for x in e4.get('g4_signals')})),
            "gbp_url": m.get("gbp_url"), "gbp_title": m.get("title"), "gbp_address": m.get("address"),
            "gbp_rating": m.get("rating_label"), "gbp_phone": m.get("phone"),
            "gbp_reviews_visible": [{k: r.get(k) for k in ("reviewer", "when", "stars", "text", "owner")} for r in m.get("reviews") or []],
            "emails_found": s.get("emails"), "dm_snippets": s.get("dm_snippets"),
            "facebook_links": s.get("facebook_links"), "instagram_links": s.get("instagram_links"),
            "franchise_mentions": s.get("franchise_hits"), "niche_word_counts": s.get("niche_counts"),
            "g8_defects_measured": [d[0] + ": " + d[1][:160] for d in e8.get("g8_defects", [])],
            "competitor_pool": [x for loc in c["locations_seen"] for x in pool.get(loc, []) if x["name"] != c["name"]][:6],
            "locations_seen": c["locations_seen"],
        })
    os.makedirs(f"{D}/packets", exist_ok=True)
    tot = 0
    for r, lst in sorted(packets.items()):
        with open(f"{D}/packets/{r}.json", "w") as f:
            json.dump(lst, f, indent=1)
        tot += len(lst)
        print(r, len(lst), "bench:", sum(1 for x in lst if x["bench_vendor_route"]))
    print("total", tot)


if __name__ == "__main__":
    main()
