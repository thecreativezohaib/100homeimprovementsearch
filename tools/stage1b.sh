#!/bin/bash
# Maps (3 shards) -> browser/PSI -> extra G8/G3 -> strict G7 -> packets. Re-runnable.
cd /home/user/100homeimprovementsearch/tools
python3 queues.py maps
N=$(date +%s)
python3 -c "
L=open('../data/maps_queue.jsonl').readlines()
for k in range(3): open(f'../data/mq{k}.jsonl','w').write(''.join(L[k::3]))
"
node maps.js ../data/mq0.jsonl ../data/maps_s$N-0.jsonl 2>>../data/maps_r.log &
node maps.js ../data/mq1.jsonl ../data/maps_s$N-1.jsonl 2>>../data/maps_r.log &
node maps.js ../data/mq2.jsonl ../data/maps_s$N-2.jsonl 2>>../data/maps_r.log &
wait
# retry maps rows that errored
python3 queues.py maps && node maps.js ../data/maps_queue.jsonl ../data/maps_s$N-retry.jsonl 2>>../data/maps_r.log
./run_browser.sh 2>> ../data/browser.log
python3 g8extra.py
python3 packets.py
python3 -c "
import json,os
ids=[x['id'] for r in ['R1','R2','R3','R4','R5'] if os.path.exists(f'../data/packets/{r}.json') for x in json.load(open(f'../data/packets/{r}.json'))]
open('../data/wn_ids.txt','w').write(' '.join(ids))"
cat ../data/wn_ids.txt | tr ' ' '\n' | xargs -r -P 6 -n 6 python3 g7verify.py > /dev/null 2>&1
python3 packets.py
