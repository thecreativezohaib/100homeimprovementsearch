#!/usr/bin/env python3
"""Master ledger: dedupe all regional discovery rows on normalised root domain AND
normalised business name (union-find), so a company found in several regions or
under several queries is one record. Writes data/ledger.jsonl and output/ledger.csv."""
import csv
import glob
import json
import re
import sys
from urllib.parse import urlparse, parse_qs, unquote

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from sitecheck import root_domain  # noqa: E402

D = "/home/user/100homeimprovementsearch/data"
O = "/home/user/100homeimprovementsearch/output"


def norm_name(n):
    n = (n or "").lower().replace("&", " and ")
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(r"\b(llc|inc|co|corp|corporation|company|ltd|the|of|pllc|lp)\b", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def real_site(w):
    if not w:
        return None
    if "google.com/aclk" in w or "googleadservices" in w:
        q = parse_qs(urlparse(w).query)
        a = q.get("adurl", [""])[0]
        return unquote(a) if a else None
    return w


def main():
    rows = []
    for f in sorted(glob.glob(f"{D}/discover*_R*.jsonl")):
        for l in open(f):
            rows.append(json.loads(l))
    parent = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    for i, r in enumerate(rows):
        r["_i"] = i
        site = real_site(r.get("website"))
        r["site"] = site
        r["dom"] = root_domain(site) if site else None
        r["nkey"] = norm_name(r["name"])
        m = re.search(r"!19s(ChIJ[^?&!]+)", r.get("maps_url") or "")
        r["place_id"] = m.group(1) if m else None
        if r["dom"]:
            union(f"row:{i}", f"dom:{r['dom']}")
        if r["place_id"]:
            union(f"row:{i}", f"pid:{r['place_id']}")
    # name merge only where it does not join two different websites
    byname = {}
    for r in rows:
        byname.setdefault(r["nkey"], []).append(r)
    for nk, rs in byname.items():
        for r in rs[1:]:
            a, b = find(f"row:{rs[0]['_i']}"), find(f"row:{r['_i']}")
            da = {x["dom"] for x in rows if x["dom"] and find(f"row:{x['_i']}") == a}
            db = {x["dom"] for x in rows if x["dom"] and find(f"row:{x['_i']}") == b}
            if not da or not db or da & db:
                union(a, b)
    groups = {}
    for r in rows:
        groups.setdefault(find(f"row:{r['_i']}"), []).append(r)
    ledger = []
    for g in groups.values():
        g.sort(key=lambda r: (r["site"] is None, r["discovered"]))
        h = g[0]
        doms = sorted({r["dom"] for r in g if r["dom"]})
        cid = doms[0] if doms else "name:" + h["nkey"].replace(" ", "-")
        ledger.append({
            "id": cid, "name": h["name"], "norm_name": h["nkey"], "website": h["site"], "root_domains": doms,
            "place_id": h["place_id"], "maps_url": h["maps_url"], "phone_maps": h["phone"], "category": h["category"],
            "rating_list": h["rating"], "region": h["region"], "regions_seen": sorted({r["region"] for r in g}),
            "locations_seen": sorted({r["location"] for r in g}), "queries": sorted({r["query"] for r in g}),
            "dup_rows": len(g), "names_seen": sorted({r["name"] for r in g}), "card_text": h["card_text"],
            "discovered": h["discovered"][:10]})
    ledger.sort(key=lambda x: x["id"])
    with open(f"{D}/ledger.jsonl", "w") as f:
        for x in ledger:
            f.write(json.dumps(x) + "\n")
    with open(f"{O}/ledger.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ledger_id", "name", "normalised_name", "root_domains", "website", "place_id", "region",
                    "regions_seen", "locations_seen", "duplicate_rows_merged", "names_seen"])
        for x in ledger:
            w.writerow([x["id"], x["name"], x["norm_name"], ";".join(x["root_domains"]), x["website"], x["place_id"],
                        x["region"], ";".join(x["regions_seen"]), ";".join(x["locations_seen"]), x["dup_rows"],
                        " | ".join(x["names_seen"])])
    print(f"raw rows {len(rows)} -> unique {len(ledger)}; with website {sum(1 for x in ledger if x['website'])}; "
          f"multi-region {sum(1 for x in ledger if len(x['regions_seen']) > 1)}", file=sys.stderr)


if __name__ == "__main__":
    main()
