#!/usr/bin/env python3
"""Rebuild the CSV block of a Gemini Deep Research PDF export (pdftotext -raw output).
The code box wraps long space-free tokens anywhere and other text at spaces, and ends each record with U+200B.
Usage: parse_gemini_pdf.py <raw.txt> <out.csv>"""
import csv, sys
L = [l.lstrip('\x0c') for l in open(sys.argv[1]).read().split('\n')]
s = next(i for i, l in enumerate(L) if l.startswith('row,business_name'))
e = next(i for i, l in enumerate(L) if l.startswith('NOTHING_FOUND'))
out = ''
for l in (l for l in L[s:e] if l.strip()):
    out += l
    # a line without spaces that fills the box is a broken token; anything else was wrapped at a space
    if not l.endswith('​') and not (' ' not in l and len(l) >= 40):
        out += ' '
rows = list(csv.reader(r.strip() for r in out.split('​') if r.strip()))
with open(sys.argv[2], 'w', newline='') as f:
    csv.writer(f).writerows(rows)
print(len(rows) - 1, 'records;', sum(len(r) != len(rows[0]) for r in rows), 'with a wrong column count')
