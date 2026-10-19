#!/bin/bash
cd /home/user/100homeimprovementsearch/tools
N=$(date +%s)
SITE_QUEUE=site_queue_r16.jsonl python3 q_r5.py social && python3 social.py ../data/social_r5_ids.txt ../data/social.jsonl 16
SITE_QUEUE=site_queue_r16.jsonl python3 q_r5.py browser && SITE_QUEUE=site_queue_r16.jsonl python3 q_r5.py psi
for k in 0 1 2 3; do node browser.js ../data/bqr5_$k.jsonl ../data/browser_r16$N-$k.jsonl 2>> ../data/browser.log & done
for k in 0 1 2 3 4 5; do python3 psi.py ../data/psir5_in$k.jsonl ../data/psi_q$k.jsonl > /dev/null 2>&1 & done
wait
echo STAGE_R6_DONE
