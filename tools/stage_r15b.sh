#!/bin/bash
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
python3 queues.py maps && node maps.js ../data/maps_queue.jsonl ../data/maps_s$N-retry.jsonl 2>>../data/maps_r.log
echo R6B_DONE
