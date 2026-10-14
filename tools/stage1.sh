#!/bin/bash
# Incremental automated screening pass. Safe to re-run.
set -x
cd /home/user/100homeimprovementsearch/tools
python3 ledger.py && python3 prep.py
python3 sitecheck.py ../data/site_queue.jsonl ../data/site.jsonl 24 2>> ../data/site.log
python3 dns.py
python3 queues.py render
RENDER=1 python3 sitecheck.py ../data/render_queue.jsonl ../data/site_render.jsonl 8 2>> ../data/site_render.log
