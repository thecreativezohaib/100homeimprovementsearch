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
python3 -c "
import sys; sys.path.insert(0,'.')
from decide import *
import subprocess
data=load(); ids=[]
for x in jl(D+'/bq_queue.jsonl'):
    s=data[1].get(x['id'])
    if s and 'g7verify' not in s: ids.append(x['id'])
open('../data/g7_todo.txt','w').write(' '.join(ids))
"
python3 g7verify.py $(cat ../data/g7_todo.txt) > /dev/null 2>&1
python3 packets.py
