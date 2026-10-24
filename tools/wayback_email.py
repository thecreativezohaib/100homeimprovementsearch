#!/usr/bin/env python3
"""Emails published on a firm's own (now dead) website, read from Wayback Machine snapshots.
For each domain: list archived HTML pages (CDX), prefer contact/about/home, fetch up to 8 snapshots, collect emails
with the snapshot URL and the surrounding text as the quote.
Usage: wayback_email.py <in.json [{row, domain}]> <out.json>"""
import json, re, sys, time, urllib.parse, urllib.request
EM = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
BAD = re.compile(r'\.(png|jpe?g|gif|webp|svg)$|sentry|wixpress|example\.|domain\.com|godaddy|yourdomain|@2x', re.I)


def get(u, t=40):
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=t).read().decode('utf-8', 'ignore')
        except Exception:
            time.sleep(3 * (i + 1))
    return ''


out = []
for x in json.load(open(sys.argv[1])):
    d = x['domain']
    cdx = get('https://web.archive.org/cdx/search/cdx?' + urllib.parse.urlencode({'url': d + '/*', 'output': 'json', 'filter': ['statuscode:200', 'mimetype:text/html'], 'collapse': 'urlkey', 'limit': 400}, doseq=True))
    try:
        caps = json.loads(cdx)[1:] if cdx else []
    except ValueError:
        caps = []
    caps.sort(key=lambda c: (0 if re.search(r'contact', c[2], re.I) else 1 if re.search(r'about', c[2], re.I) else 2 if c[2].rstrip('/').count('/') <= 2 else 3, -int(c[1])))
    found = {}
    for c in caps[:8]:
        snap = f'https://web.archive.org/web/{c[1]}/{c[2]}'
        t = re.sub(r'<[^>]+>', ' ', get(snap).replace('mailto:', ' '))
        t = re.sub(r'\s+', ' ', t)
        for m in EM.finditer(t):
            e = m.group(0).rstrip('.')
            if not BAD.search(e) and e.lower() not in found:
                found[e.lower()] = {'email': e, 'snapshot': snap, 'quote': t[max(0, m.start() - 80):m.end() + 40].strip()}
        if found:
            break
    out.append({**x, 'snapshots': len(caps), 'emails': list(found.values())})
    print(x['row'], d, len(caps), [f['email'] for f in found.values()], flush=True)
json.dump(out, open(sys.argv[2], 'w'), indent=1)
