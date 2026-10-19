#!/usr/bin/env python3
"""Next discovery round: the 60 most populous Census places per region (Vintage 2023 sub-county estimates,
4,000 to 100,000 people; incorporated places plus New England towns) that no earlier run_discover*.sh searched.
Writes tools/run_discover<N>.sh and tools/regions<N>.txt. Usage: regions_next.py <N> <sub-est2023.csv>"""
import csv, glob, re, sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
T = "/home/user/100homeimprovementsearch/tools"
n, src = sys.argv[1], sys.argv[2]
exec(open(f"{T}/regions14.py").read().split("seen = set()")[0])  # REG, AB, NE, SUF from round 14
seen = set()
for f in glob.glob(f"{T}/run_discover*.sh"):
    seen |= {m.lower() for m in re.findall(r"\|([^'|]+, [A-Z]{2})'", open(f).read())}
cands = {r: {} for r in REG}
for row in csv.DictReader(open(src, encoding="latin-1")):
    st = AB.get(row["STNAME"])
    if not st or "(balance)" in row["NAME"] or "(pt.)" in row["NAME"]:
        continue
    if not (row["SUMLEV"] == "162" or (row["SUMLEV"] == "061" and st in NE)):
        continue
    name = re.sub(r".*\((.*)\)$", r"\1", SUF.sub("", row["NAME"]).strip())
    if "'" in name or " metro" in name:
        continue
    town, pop = f"{name}, {st}", int(row["POPESTIMATE2023"] or 0)
    if town.lower() in seen or not 4000 <= pop <= 100000:
        continue
    reg = next(r for r, s in REG.items() if st in s.split())
    cands[reg][town] = max(pop, cands[reg].get(town, 0))
regions = {r: [t for t, _ in sorted(c.items(), key=lambda x: -x[1])[:60]] for r, c in cands.items()}
with open(f"{T}/run_discover{n}.sh", "w") as f:
    f.write("#!/bin/bash\ncd /home/user/100homeimprovementsearch/tools\n")
    for r, lst in regions.items():
        jobs = " ".join(f"'{q}|{t}'" for t in lst for q in ("kitchen remodeler", "bathroom remodeler"))
        f.write(f"node discover.js {r} ../data/discover{n}_{r}.jsonl {jobs} 2> ../data/discover{n}_{r}.log &\n")
    f.write(f"wait\necho DISCOVER{n}_DONE\n")
open(f"{T}/regions{n}.txt", "w").write("".join(f"{r}\t{t}\n" for r, lst in regions.items() for t in lst))
for r, lst in regions.items():
    print(r, len(lst), lst[:4], "remaining pool", len(cands[r]))
