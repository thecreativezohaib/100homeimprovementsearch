"""Shared helpers: relative Google timestamps -> conservative date windows."""
import re
from datetime import date, timedelta

RUN_DATE = date(2026, 10, 14)
D90 = RUN_DATE - timedelta(days=90)   # 2026-07-16
D60 = RUN_DATE - timedelta(days=60)   # 2026-08-15
M9 = RUN_DATE - timedelta(days=273)   # 2026-01-14

NUM = {"a": 1, "an": 1, "one": 1}


def rel_window(s, retrieved=RUN_DATE):
    """Map a Google relative timestamp to (earliest, latest) possible dates.

    Conservative on BOTH common rounding conventions (floor, and moment.js-style rounding):
    'N weeks ago' -> up to N*7+6 days; 'a month ago' -> up to 59 days; 'N months ago' -> up to (N+1)*30-1 days.
    Returns None for unparseable strings and for 'Edited ...' stamps (edit date is not a posting date).
    """
    if not s:
        return None
    s = s.strip().lower()
    if s.startswith("edited"):
        return None
    m = re.match(r"(a|an|one|\d+)\s+(minute|hour|day|week|month|year)s?\s+ago", s)
    if not m:
        return None
    n = NUM.get(m.group(1)) or int(m.group(1))
    unit = m.group(2)
    if unit in ("minute", "hour"):
        lo, hi = 0, 1
    elif unit == "day":
        lo, hi = n, n
    elif unit == "week":
        lo, hi = n * 7, n * 7 + 6
    elif unit == "month":
        lo, hi = max(26, n * 30 - 15), (n + 1) * 30 - 1
    else:
        lo, hi = n * 365 - 183, (n + 1) * 365
    return retrieved - timedelta(days=hi), retrieved - timedelta(days=lo)


def within(s, cutoff):
    w = rel_window(s)
    return bool(w) and w[0] >= cutoff
