#!/bin/bash
# incremental: browser/PSI on candidates whose Maps data exists -> extra G8/G3 -> packets -> strict G7 on packets
cd /home/user/100homeimprovementsearch/tools
./run_browser.sh 2>> ../data/browser.log
python3 g8extra.py
python3 packets.py
python3 -c "
import json,os
ids=[x['id'] for r in ['R1','R2','R3','R4','R5'] if os.path.exists(f'../data/packets/{r}.json') for x in json.load(open(f'../data/packets/{r}.json'))]
open('../data/wn_ids.txt','w').write(' '.join(ids))"
cat ../data/wn_ids.txt | tr ' ' '\n' | xargs -r -P 6 -n 6 python3 g7verify.py > /dev/null 2>&1
python3 packets.py
