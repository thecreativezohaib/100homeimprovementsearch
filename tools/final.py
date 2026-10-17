#!/usr/bin/env python3
"""Write deliverables from all evidence: output/prospects100.csv, priority30.csv, rejected.csv,
contact-only.csv, bench-vendor.csv, evidence.csv, logs/R1..R5.csv, funnel.json."""
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from decide import (load, evaluate, first_fail, ORDER, jl, D, O, TODAY, D60, within, phone_check)  # noqa: E402

BANNED = re.compile(r"\b(likely|appears to|probably|presumably|seems|suggests)\b", re.I)


def j(x):
    return json.dumps(x, ensure_ascii=False) if not isinstance(x, str) else x


def sig_str(x):
    src = f" | source: {x['source']}" if x.get("source") else ""
    return f"{x.get('type')} | {x.get('date')} | {x.get('url')} | {x.get('quote')}{src}"


def rating(m):
    lab = (m or {}).get("rating_label") or ""
    mm = re.match(r"\s*([0-9.]+)\s*\(([\d,]+)\)", lab.replace("\n", ""))
    return (float(mm.group(1)), int(mm.group(2).replace(",", ""))) if mm else (None, None)


def owner_reply(m):
    for r in (m or {}).get("reviews") or []:
        o = r.get("owner") or ""
        mm = re.match(r"Response from the owner\s+(.+?ago)", o)
        if mm and within(mm.group(1), D60):
            return {"value": f"owner replied '{mm.group(1)}' to {r.get('reviewer')}'s review", "url": m.get("gbp_url"),
                    "quote": o.split("\n")[0][:120], "date": mm.group(1)}
    return None


def score(c, s, m, man):
    sc = (man or {}).get("score") or {}
    comp = {}

    def val(k):
        v = sc.get(k)
        if v in (None, "", "UNKNOWN"):
            return "UNKNOWN"
        if isinstance(v, str) and v.upper().startswith("NONE"):
            return "NONE FOUND"
        return v
    trig = val("trigger")
    if isinstance(trig, dict):
        # a trigger scores only when its date is evidenced on/after 2026-01-14 (9-month window)
        trig = {**trig, "meets": bool(re.match(r"\d{4}-\d{2}-\d{2}", str(trig.get("date")))) and str(trig.get("date"))[:10] >= "2026-01-14"}
    comp["trigger"] = (5, trig)
    orp = owner_reply(m)
    comp["owner_reply_60d"] = (5, orp if orp else ("NONE FOUND (3 visible GBP reviews checked)" if m and m.get("title") else "UNKNOWN"))
    comp["job_posting_live"] = (4, val("job_posting_live"))
    comp["competitor_modern_15mi"] = (3, val("competitor"))
    comp["owner_account_post_60d"] = (3, val("owner_account_post_60d"))
    r, n = rating(m)
    if r is None:
        comp["rating_4_5_20_200"] = (3, "UNKNOWN")
    else:
        ok = r >= 4.5 and 20 <= n <= 200
        comp["rating_4_5_20_200"] = (3, {"value": f"{r} stars, {n} Google reviews", "url": m.get("gbp_url"),
                                         "quote": f"GBP header '{r} ({n})' retrieved {m.get('retrieved','')[:10]}", "meets": ok})
    comp["high_ticket"] = (2, val("high_ticket"))
    total, unknown = 0, 0
    for k, (pts, v) in comp.items():
        if v == "UNKNOWN":
            unknown += 1
        elif isinstance(v, dict) and v.get("meets", True):
            total += pts
    return total, unknown, comp


def main():
    data = load()
    L, site, maps, br, psi, dns, manual, pre = data
    os.makedirs(f"{O}/logs", exist_ok=True)
    rows, rejected, contact_only, bench, evid, logs = [], [], [], [], [], defaultdict(list)
    funnel = Counter()
    for cid, c in L.items():
        s, m, man = site.get(cid), maps.get(cid), manual.get(cid)
        base = {"prospect_id": cid, "business_name": c["name"], "region": c["region"], "website": c.get("website"),
                "google_maps_category": c.get("category"), "discovered_in": "; ".join(c["locations_seen"][:3])}
        funnel["discovered"] += 1
        if c.get("dup_of"):
            logs[c["region"]].append({**base, "status": "DUPLICATE", "gate": "", "detail": f"same final website as {c['dup_of']}"})
            funnel["duplicate_merged"] += 1
            continue
        if cid in pre:
            g, why = pre[cid]["gate"], pre[cid]["reason"]
            rejected.append({**base, "failed_gate": g, "evidence": why, "other_known_failures": ""})
            logs[c["region"]].append({**base, "status": "REJECTED", "gate": g, "detail": why})
            funnel[f"reject_{g}"] += 1
            continue
        funnel["screened"] += 1
        r = evaluate(c, data)
        ev = r["ev"]
        if r.get("niche") == "FAIL" or (man and man.get("niche_ok") is False):
            why = (man or {}).get("niche_evidence") or ev.get("niche")
            rejected.append({**base, "failed_gate": "NICHE", "evidence": j(why), "other_known_failures": ""})
            logs[c["region"]].append({**base, "status": "REJECTED", "gate": "NICHE", "detail": j(why)})
            funnel["reject_NICHE"] += 1
            continue
        gates = r["gates"]
        g, st = first_fail(r)
        if g == "G3":
            # bench routing: fails ONLY G3, would otherwise pass, has a measured G8 defect, vendor named
            rest = [x for x in ORDER if x not in ("G1", "G2", "G3")]
            if ev.get("g3_vendor") and all(gates.get(x) == "PASS" for x in rest) and (man or {}).get("stopped_at") is None and man:
                bench.append({**base, "incumbent_vendor": ev.get("g3_vendor"), "vendor_evidence": ev.get("g3"),
                              "g8_defect": j(ev.get("g8_defects")), "decision_maker": j(ev.get("g6_dm")),
                              "email": j(ev.get("g6_email")), "g4_signals": j(ev.get("g4_signals")),
                              "g9_signals": j(ev.get("g9_signals"))})
                logs[c["region"]].append({**base, "status": "BENCH_VENDOR", "gate": "G3", "detail": ev.get("g3")})
                funnel["bench_vendor"] += 1
                continue
        if g == "G6" and st == "CONTACT_ONLY":
            rest = ["G7", "G8", "G9"]
            if all(gates.get(x) == "PASS" for x in rest):
                contact_only.append({**base, "decision_maker": j(ev.get("g6_dm")), "contact_form_url": (man or {}).get("contact_form_url"),
                                     "phone": (man or {}).get("phone") or (m or {}).get("phone"), "socials": j((man or {}).get("socials")),
                                     "g8_defect": j(ev.get("g8_defects")), "g9_signals": j(ev.get("g9_signals"))})
                logs[c["region"]].append({**base, "status": "CONTACT_ONLY", "gate": "G6", "detail": "no published email"})
                funnel["contact_only"] += 1
                continue
        if g is not None:
            detail = ev.get(g.lower()) or ev.get(g.lower() + "_reason") or st
            if isinstance(detail, str):
                detail = detail.replace("route1 route1", "route1")
            if st and st.startswith("PENDING"):
                detail = f"[not completed] {detail}"
            others = [f"{x}:{gates.get(x)}" for x in ORDER if ORDER.index(x) > ORDER.index(g) and gates.get(x) == "FAIL"]
            rejected.append({**base, "failed_gate": g, "evidence": j(detail),
                             "other_known_failures": "; ".join(others)})
            logs[c["region"]].append({**base, "status": "REJECTED", "gate": g, "detail": j(detail)})
            funnel[f"reject_{g}"] += 1
            continue
        # all gates passed
        total, unknown, comp = score(c, s, m, man)
        if unknown > 2:
            rejected.append({**base, "failed_gate": "SCORING_UNKNOWNS", "evidence": f"{unknown} UNKNOWN scoring fields",
                             "other_known_failures": ""})
            logs[c["region"]].append({**base, "status": "REJECTED", "gate": "SCORING_UNKNOWNS", "detail": str(unknown)})
            funnel["reject_SCORING_UNKNOWNS"] += 1
            continue
        funnel["passed"] += 1
        dm, em = ev["g6_dm"], ev["g6_email"]
        sigs = ev["g4_signals"]
        d8 = ev["g8_defects"][0]
        row = {"score_total": total, **base,
               "final_url": ev["g2_final_url"], "phone": (m or {}).get("phone", "").replace("phone:tel:", ""),
               "gbp_url": (m or {}).get("gbp_url"), "gbp_address": (m or {}).get("address"),
               "decision_maker": dm.get("name"), "decision_maker_role": dm.get("role"), "decision_maker_source": dm.get("url"),
               "decision_maker_quote": dm.get("quote"), "email": em.get("email"), "email_source_url": em.get("url") or em.get("page"),
               "email_raw_string": em.get("raw"), "email_method": em.get("method") or em.get("how"),
               "G1_not_contacted": ev["g1"],
               "G2_final_url": ev["g2_final_url"], "G2_http_status": ev["g2_http_status"], "G2_fetch_date": ev["g2_fetch_date"],
               "G2_route": ev["g2_route"],
               "G3_platform": "; ".join(ev["g3_platform"]), "G3_check": ev["g3_check"],
               "G4_signal_1": sig_str(sigs[0]), "G4_signal_2": sig_str(sigs[1]), "G4_phone_check": ev["g4_phone"]["detail"],
               "G5_independent": j(ev.get("g5")),
               "G6_decision_maker": f"{dm.get('name')} ({dm.get('role')})", "G6_email": em.get("email"),
               "G7_original_images_800px": len(ev.get("g7_urls") or []), "G7_image_urls": " ".join(ev.get("g7_urls") or []),
               "G7_dims": " ".join(ev.get("g7_dims") or []), "G7_method": ev.get("g7_method") or ev.get("g7"),
               "G8_defect": d8[0], "G8_measurement": d8[1], "G8_tested_url": d8[2], "G8_test_date": d8[3],
               "G8_all_defects": " || ".join(f"{d[0]}: {d[1][:160]}" for d in ev["g8_defects"][1:]),
               "G8_psi": j(ev.get("g8_psi")),
               "G9_signal": ev["g9_signals"][0]["signal"], "G9_evidence": ev["g9_signals"][0]["evidence"][:300],
               "G9_all_signals": "; ".join(x["signal"] for x in ev["g9_signals"]),
               "unknown_scoring_fields": unknown}
        for k, (pts, v) in comp.items():
            pts_got = pts if (isinstance(v, dict) and v.get("meets", True)) else 0
            row[f"score_{k}_pts"] = pts_got
            row[f"score_{k}_evidence"] = j(v)
        row["assessment_OPINION"] = (man or {}).get("assessment", "")
        rows.append(row)
        # evidence rows
        for f_, v_, u_, q_ in [
            ("G2 final URL", f"HTTP {ev['g2_http_status']} {ev['g2_final_url']}", ev["g2_final_url"], ev["g2_route"]),
            ("G3 platform", "; ".join(ev["g3_platform"]), ev["g2_final_url"], ev["g3_check"]),
            ("G4 signal 1", sigs[0]["date"], sigs[0].get("url"), sigs[0].get("quote")),
            ("G4 signal 2", sigs[1]["date"], sigs[1].get("url"), sigs[1].get("quote")),
            ("G4 phone", (m or {}).get("phone"), (m or {}).get("gbp_url"), ev["g4_phone"]["detail"]),
            ("G5 independent", "independent", (man or {}).get("g5_evidence", {}).get("url") if isinstance((man or {}).get("g5_evidence"), dict) else "",
             j((man or {}).get("g5_evidence"))),
            ("G6 decision maker", f"{dm.get('name')} ({dm.get('role')})", dm.get("url"), dm.get("quote")),
            ("G6 email", em.get("email"), em.get("url") or em.get("page"), f"raw: {em.get('raw')} ({em.get('method') or em.get('how')})"),
            ("G7 images", f"{len(ev.get('g7_urls') or [])} images >=800px", ev["g2_final_url"], ev.get("g7_method")),
            ("G8 defect", d8[0], d8[2], d8[1]),
            ("G8 PSI", j((ev.get("g8_psi") or {}).get("result")), (ev.get("g8_psi") or {}).get("tested_url"),
             "PSI API v5 mobile performance: " + j((ev.get("g8_psi") or {}).get("attempts"))),
            ("G9 paid signal", ev["g9_signals"][0]["signal"], ev["g2_final_url"], ev["g9_signals"][0]["evidence"][:300]),
        ]:
            note, rdate = "", TODAY
            sig = {"G4 signal 1": sigs[0], "G4 signal 2": sigs[1]}.get(f_)
            if sig and sig.get("source"):
                note = sig["source"]
                rdate = re.search(r"checked_on (\d{4}-\d{2}-\d{2})", note).group(1)
            if f_ == "G8 defect" and d8[3]:
                rdate = str(d8[3])[:10]
            if f_ == "G8 PSI" and (psi.get(cid) or {}).get("psi_date"):
                rdate = psi[cid]["psi_date"][:10]
            evid.append({"prospect": c["name"], "prospect_id": cid, "field": f_, "value": v_, "source_url": u_,
                         "quote_or_method": q_, "retrieval_date": rdate, "source_note": note})
        logs[c["region"]].append({**base, "status": "PASSED", "gate": "", "detail": f"score {total}"})
    rows.sort(key=lambda x: (-x["score_total"], x["business_name"]))
    for i, r in enumerate(rows, 1):
        r["rank"] = i

    def wcsv(path, lst, first=None):
        keys = []
        for x in lst:
            for k in x:
                if k not in keys:
                    keys.append(k)
        if first:
            keys = first + [k for k in keys if k not in first]
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys or ["none"])
            w.writeheader()
            for x in lst:
                w.writerow(x)
    wcsv(f"{O}/prospects100.csv", rows, ["rank", "score_total", "prospect_id", "business_name"])
    tmpl = {}
    for x in jl(f"{D}/template/*.jsonl"):
        tmpl.setdefault(x["id"], {}).update(x)
    p30 = []
    for r in rows[:30]:
        t = tmpl.get(r["prospect_id"], {})
        p30.append({"rank": r["rank"], "score_total": r["score_total"], "prospect_id": r["prospect_id"],
                    "business_name": r["business_name"], "region": r["region"], "website": r["final_url"],
                    "decision_maker": f"{r['decision_maker']} ({r['decision_maker_role']})", "email": r["email"],
                    "trigger_event": r.get("score_trigger_evidence"), "g8_defect": f"{r['G8_defect']}: {r['G8_measurement']}",
                    **{k: (j(t.get(k)) if t else "NOT YET CAPTURED") for k in
                       ("hero_headline_source", "services_3", "gallery_urls_8", "before_after_pairs", "reviews_3",
                        "service_area", "phone", "cta_wording", "years_in_business", "licences_awards", "outreach_angle")}})
    wcsv(f"{O}/priority30.csv", p30)
    wcsv(f"{O}/rejected.csv", rejected)
    wcsv(f"{O}/contact-only.csv", contact_only)
    wcsv(f"{O}/bench-vendor.csv", bench)
    wcsv(f"{O}/evidence.csv", evid)
    for reg, lst in logs.items():
        wcsv(f"{O}/logs/{reg}.csv", lst)
    funnel["rejected_total"] = len(rejected)
    json.dump(dict(funnel), open(f"{O}/funnel.json", "w"), indent=1)
    json.dump([{k: r[k] for k in ("rank", "score_total", "prospect_id", "business_name", "region")} for r in rows],
              open(f"{D}/ranked.json", "w"), indent=1)
    # banned-word audit over factual fields
    bad = []
    for r in rows:
        for k, v in r.items():
            if k != "assessment_OPINION" and isinstance(v, str) and BANNED.search(v):
                bad.append((r["business_name"], k, BANNED.search(v).group(0)))
    print(json.dumps(dict(funnel), indent=1))
    print("banned-word hits in factual fields:", bad[:20])
    longq = []
    for r in rows:
        for k, v in r.items():
            if "quote" in k.lower() and isinstance(v, str) and len(v.split()) > 20:
                longq.append((r["business_name"], k, len(v.split())))
            if k.endswith("_evidence") and isinstance(v, str) and v.startswith("{"):
                try:
                    q = json.loads(v).get("quote")
                    if q and len(q.split()) > 20:
                        longq.append((r["business_name"], k, len(q.split())))
                except Exception:
                    pass
    print("quotes over 20 words:", longq)


if __name__ == "__main__":
    main()
