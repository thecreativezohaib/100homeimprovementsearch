#!/usr/bin/env python3
"""Discovery round 14 town list: the 60 most populous Census places per region (Vintage 2023 sub-county estimates, 4,000 to 100,000 people;
incorporated places, plus New England towns) that no earlier round searched. Writes REGIONS14 into this file's
companion run_discover14.sh. Usage: regions14.py <sub-est2023.csv>"""
import csv, glob, re, sys
REG = {"R1": "CT MA ME NH NJ NY PA RI VT", "R2": "AL DE FL GA KY MD MS NC SC TN VA WV DC", "R3": "IA IL IN MI MN MO ND NE OH SD WI KS",
       "R4": "AR CO LA NM OK TX UT WY", "R5": "AK AZ CA HI ID MT NV OR WA"}
AB = {"Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA", "Colorado": "CO", "Connecticut": "CT",
      "Delaware": "DE", "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL",
      "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
      "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO", "Montana": "MT",
      "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
      "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA",
      "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
      "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"}
NE = set("CT MA ME NH RI VT".split())
SUF = re.compile(r"\s+(city and borough|consolidated government \(balance\)|metropolitan government \(balance\)|unified government \(balance\)|"
                 r"urban county|city|town|village|borough|township|municipality|CDP|plantation)$", re.I)
seen = set()
for f in glob.glob("/home/user/100homeimprovementsearch/tools/regions*.py"):
    if f.endswith("regions14.py"):
        continue
    ns = {}
    exec(open(f).read(), ns)
    for k, v in ns.items():
        if k.startswith("REGIONS") and isinstance(v, dict):
            for lst in v.values():
                seen |= {t.lower() for t in lst if isinstance(t, str)}
cands = {r: {} for r in REG}
for row in csv.DictReader(open(sys.argv[1], encoding="latin-1")):
    st = AB.get(row["STNAME"])
    if not st or "(balance)" in row["NAME"] or "(pt.)" in row["NAME"]:
        continue
    if not (row["SUMLEV"] == "162" or (row["SUMLEV"] == "061" and st in NE)):
        continue
    name = re.sub(r".*\((.*)\)$", r"\1", SUF.sub("", row["NAME"]).strip())  # "El Paso de Robles (Paso Robles)" -> "Paso Robles"
    if "'" in name:  # keeps the shell quoting in run_discover14.sh simple
        continue
    town = f"{name}, {st}"
    if town.lower() in seen:
        continue
    reg = next(r for r, s in REG.items() if st in s.split())
    pop = int(row["POPESTIMATE2023"] or 0)
    if 4000 <= pop <= 100000 and " metro" not in name:  # big cities were searched by metro and neighbourhood in rounds 1 to 4
        cands[reg][town] = max(pop, cands[reg].get(town, 0))
REGIONS14 = {r: [t for t, _ in sorted(c.items(), key=lambda x: -x[1])[:60]] for r, c in cands.items()}
if __name__ == "__main__":
    with open("/home/user/100homeimprovementsearch/tools/run_discover14.sh", "w") as f:
        f.write("#!/bin/bash\ncd /home/user/100homeimprovementsearch/tools\n")
        for r, lst in REGIONS14.items():
            jobs = " ".join(f"'{q}|{t}'" for t in lst for q in ("kitchen remodeler", "bathroom remodeler"))
            f.write(f"node discover.js {r} ../data/discover14_{r}.jsonl {jobs} 2> ../data/discover14_{r}.log &\n")
        f.write("wait\necho DISCOVER14_DONE\n")
    for r, lst in REGIONS14.items():
        print(r, len(lst), lst[:6], lst[-2:])
