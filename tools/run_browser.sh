#!/bin/bash
cd /home/user/100homeimprovementsearch/tools
python3 q_browser.py
N=$(date +%s)
python3 -c "
L=[l for l in open('../data/bq_queue.jsonl')]
for k in range(3): open(f'../data/bq{k}.jsonl','w').write(''.join(L[k::3]))
"
node browser.js ../data/bq0.jsonl ../data/browser_$N-0.jsonl &
node browser.js ../data/bq1.jsonl ../data/browser_$N-1.jsonl &
node browser.js ../data/bq2.jsonl ../data/browser_$N-2.jsonl &
python3 psi.py ../data/psi_queue.jsonl ../data/psi.jsonl &
wait
