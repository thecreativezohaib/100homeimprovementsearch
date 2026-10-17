#!/bin/bash
# Round-5 pipeline: site checks -> DNS/render -> Maps -> social -> browser + PSI -> packets. Re-runnable.
cd /home/user/100homeimprovementsearch/tools
python3 sitecheck.py ../data/site_queue_r5.jsonl ../data/site.jsonl 24 2>> ../data/site.log
python3 dns.py
python3 queues.py render
RENDER=1 python3 sitecheck.py ../data/render_queue.jsonl ../data/site_render.jsonl 8 2>> ../data/site_render.log
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
python3 q_r5.py social && python3 social.py ../data/social_r5_ids.txt ../data/social.jsonl 16
python3 q_r5.py browser && python3 q_r5.py psi
for k in 0 1 2 3; do node browser.js ../data/bqr5_$k.jsonl ../data/browser_r5$N-$k.jsonl 2>> ../data/browser.log & done
for k in 0 1 2 3 4 5; do python3 psi.py ../data/psir5_in$k.jsonl ../data/psi_q$k.jsonl > /dev/null 2>&1 & done
wait
echo STAGE_R5_DONE
