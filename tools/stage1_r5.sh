#!/bin/bash
# Round-5 automated screening: site checks for new ledger ids only, then DNS and render retries.
cd /home/user/100homeimprovementsearch/tools
python3 sitecheck.py ../data/site_queue_r5.jsonl ../data/site.jsonl 24 2>> ../data/site.log
python3 dns.py
python3 queues.py render
RENDER=1 python3 sitecheck.py ../data/render_queue.jsonl ../data/site_render.jsonl 8 2>> ../data/site_render.log
