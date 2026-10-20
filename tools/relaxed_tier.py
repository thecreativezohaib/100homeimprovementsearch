#!/usr/bin/env python3
"""Relaxed tier, approved by the user on 2026-10-20 to reach 100 from already-researched firms.
Loosenings (each row lists the ones it relies on; every other gate is unchanged):
  G4     one dated activity signal in 2026-07-16..2026-10-14 instead of two different signal types
  NICHE  kitchen and bath lead the advertised service list even though the page title is generic remodelling
  G6     owner named with role on the firm's own site, but no published email: contact by phone or contact form
  G5     independence taken from the named owner on the firm's own site plus no franchise / parent wording in the
         automated scan (the agent G5 check was not run because the agent stopped at an earlier gate)
Inputs: data/relaxed_evidence.jsonl (owner and email re-fetched verbatim), data/service_order.jsonl, data/g7visual.jsonl,
manual agent lines, the ledger, Maps and site records. Writes output/prospects100_relaxed.csv and output/prospects100_all.csv."""
import csv, json, sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, evaluate, jl, D, O  # noqa: E402

KB_TITLE = {"aptitudedesignandbuild.com", "bigbuildconstruction.net", "customkitchensinc.net", "mountaineerkitchensandbaths.com",
            "specialtykitchensandbaths.com", "affordableremodelingsolutions.com", "cervantescabinets.com", "woodsman.biz",
            "whitebirchdesignllc.com", "halcokb.com", "modernkitchen.net", "completelykitchens.com", "getwreedone.com",
            "okckitchenandbath.com", "yournewbaths.com"}
# owner quotes recorded earlier where the re-fetch found the name without a role word nearby
FILL = {
 "cervantescabinets.com": ("Joel Cervantes", "https://cervantescabinets.com/about", "OWNER/CRAFTSMAN JOEL CERVANTES Cabinetry has been my lifelong passion"),
 "woodsman.biz": ("Brad Mangold", "https://www.woodsman.biz/esop", "Meet the Executive Team Brad Mangold President Ira Cloud Vice President"),
 "north2southflo.com": ("Colby Matheny", "https://www.north2southflo.com/", "becomes part of the North2South family Colby Matheny Owner- Operator"),
 "discoverelite.com": ("Eric Lamascus", "https://discoverelite.com/about", "Eric Lamascus, CEO"),
 "yournewbaths.com": ("Brandon Moore", "https://www.yournewbaths.com/", "Brandon Moore, founder and owner"),
 "bennettcontracting.com": ("Andrew Gutman", "https://bennettcontracting.com/about-bennett/", "Specialty Trades Office Team Andrew Gutman President & Co-Owner"),
 "stebnitzbuilders.com": ("Chris Stebnitz", "https://www.stebnitzbuilders.com/about/our-team/", "Chris Stebnitz Owner"),
}
EMAIL_FILL = {"getwreedone.com": "team@getwreedone.com", "okckitchenandbath.com": "team@okckitchenandbath.com"}


def main():
    d = load(); L, site, maps, man = d[0], d[1], d[2], d[6]
    vis = {x["id"]: x for x in jl(f"{D}/g7visual.jsonl")}
    so = {x["id"]: x for x in jl(f"{D}/service_order.jsonl")}
    evid = {x["id"]: x for x in jl(f"{D}/relaxed_evidence.jsonl")}
    rows = []
    for cid, e in evid.items():
        if not (vis.get(cid) or {}).get("ok"):
            continue
        c, s, m, mn = L[cid], site[cid], maps.get(cid) or {}, man.get(cid) or {}
        ev = evaluate(c, d)["ev"]
        sig = ev.get("g4_signals") or []
        types = {x["type"] for x in sig}
        name, ourl, oq = e["owner"], e["owner_url"], e["owner_quote"]
        if cid in FILL:
            name, ourl, oq = FILL[cid]
        email = e["email"] or EMAIL_FILL.get(cid)
        loosened = []
        if len(types) < 2:
            loosened.append("G4: one dated activity signal type in the window (two required)")
        if cid not in KB_TITLE:
            loosened.append("NICHE: kitchen and bath lead the service list; page title is generic remodelling")
        if not email:
            loosened.append("G6: owner named but no email published on the site; contact by phone or contact form")
        if not (mn.get("g5_independent") or mn.get("g5")):
            loosened.append("G5: independence from the owner named on the firm's own site and no franchise or parent wording (agent G5 check not run)")
        if cid in so and so[cid].get("ok"):
            nurl, nq = so[cid]["url"], so[cid]["quote"]
        else:
            nurl, nq = s["final_url"], (s.get("title") or "")[:140]
        sigtxt = [f"{x['type']} | {x['date']} | {x.get('url')} | {x['quote'][:140]}" for x in sig[:2]]
        defects = ev.get("g8_defects") or []
        rows.append({
            "tier": "relaxed", "prospect_id": cid, "business_name": m.get("title") or c["name"], "region": c.get("region"),
            "website": s["final_url"], "phone": (m.get("phone") or "").replace("phone:tel:", ""), "gbp_url": m.get("gbp_url"),
            "gbp_address": (m.get("address") or "").replace("", "").strip(),
            "loosened": " ; ".join(loosened),
            "niche_evidence_url": nurl, "niche_evidence_quote": nq,
            "decision_maker": name, "decision_maker_url": ourl, "decision_maker_quote": oq,
            "email": email or "", "email_url": e.get("email_url") or "", "email_method": e.get("email_how") or ("site check" if email else ""),
            "G3_platform": s.get("platform"),
            "G4_signal_1": sigtxt[0] if sigtxt else "", "G4_signal_2": sigtxt[1] if len(sigtxt) > 1 else "",
            "G7_visual_review": vis[cid]["note"],
            "G8_defect": defects[0][0] if defects else "", "G8_measurement": defects[0][1][:200] if defects else "",
            "retrieved": "2026-10-20"})
    rows.sort(key=lambda r: (r["loosened"].count(";"), r["business_name"]))
    cols = list(rows[0].keys())
    with open(f"{O}/prospects100_relaxed.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    strict = list(csv.DictReader(open(f"{O}/prospects100.csv")))
    allcols = ["tier", "prospect_id", "business_name", "region", "website", "phone", "gbp_url", "loosened", "decision_maker", "email", "G8_defect"]
    with open(f"{O}/prospects100_all.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=allcols); w.writeheader()
        for r in strict:
            w.writerow({"tier": "strict", "prospect_id": r["prospect_id"], "business_name": r["business_name"], "region": r["region"],
                        "website": r["website"], "phone": r.get("phone"), "gbp_url": r.get("gbp_url"), "loosened": "",
                        "decision_maker": r.get("decision_maker"), "email": r.get("email"), "G8_defect": r.get("G8_defect")})
        for r in rows:
            w.writerow({k: r.get(k) for k in allcols})
    print("relaxed", len(rows), "strict", len(strict), "total", len(rows) + len(strict))
    from collections import Counter
    cnt = Counter()
    for r in rows:
        for x in r["loosened"].split(" ; "):
            if x: cnt[x.split(":")[0]] += 1
    print(dict(cnt))


if __name__ == "__main__":
    main()
