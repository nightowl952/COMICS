#!/usr/bin/env python3
"""Marvel catalog harvester -- the reliable way to link an issue.

marvel.com runs an open JSON catalog at bifrost.marvel.com. It needs no key,
it answers in ~1KB instead of a 250KB HTML page, and each record carries the
canonical issue URL, the series it belongs to, the issue number, and whether
the issue is on Marvel Unlimited. That makes a complete sweep of the id space
cheap, which is what this does -- once swept, linking an issue is a local
lookup instead of a web search.

    python3 tools/catalog.py sweep              # everything not yet probed
    python3 tools/catalog.py sweep 1:20000      # just this range
    python3 tools/catalog.py status             # how much is banked
    python3 tools/catalog.py find "Books of Doom"

Writes tools/marvel_catalog.json:
    {"<comic id>": [slug, series_id, issue_number, in_mu, is_variant]}
and tools/marvel_series.json: {"<series id>": "Title (1962 - 1999)"}.
Both are resumable -- a rerun skips ids already probed, dead ones included.
"""
import json, os, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
CAT = os.path.join(HERE, "marvel_catalog.json")
SER = os.path.join(HERE, "marvel_series.json")
DONE = os.path.join(HERE, "marvel_catalog_probed.json")

API = "https://bifrost.marvel.com/catalog/comics/%d"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")
MAX_ID = 140000
WORKERS = 32


def load(p, d):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def save(p, obj):
    tmp = p + ".tmp"
    json.dump(obj, open(tmp, "w", encoding="utf-8"), separators=(",", ":"))
    os.replace(tmp, p)


# probed ids are stored as sorted [start, end] inclusive ranges -- 140k ints
# would be a 1MB file of noise, and the sweep is contiguous anyway.
def to_ranges(ids):
    out = []
    for i in sorted(ids):
        if out and i == out[-1][1] + 1:
            out[-1][1] = i
        else:
            out.append([i, i])
    return out


def from_ranges(rs):
    s = set()
    for a, b in rs:
        s.update(range(a, b + 1))
    return s


# One requests.Session per worker thread. Without keep-alive every id pays a
# fresh TLS handshake, which is most of the cost of a sweep -- reusing the
# connection is worth roughly 3x.
_local = threading.local()


def session():
    s = getattr(_local, "s", None)
    if s is None:
        s = _local.s = requests.Session()
        s.headers.update({"User-Agent": UA,
                          "Referer": "https://www.marvel.com/"})
    return s


def fetch(cid):
    """-> (cid, record or None). None means the id is dead."""
    r = session().get(API % cid, timeout=25)
    if r.status_code == 404:
        return cid, None
    if r.status_code in (403, 429):
        raise IOError("blocked %d" % r.status_code)
    d = (r.json().get("data") or {}) if r.ok else {}
    if not d or d.get("error") or not d.get("url"):
        return cid, None
    url = d["url"]
    if "/comics/issue/" not in url:
        return cid, None
    slug = url.rsplit("/", 1)[-1]
    ser = d.get("series") or {}
    dig = d.get("digital_comic") or {}
    return cid, [slug, ser.get("id"), d.get("issue_number"),
                 1 if dig.get("in_mu") else 0,
                 1 if d.get("is_variant") else 0, ser.get("title") or ""]


def cmd_sweep(args):
    lo, hi = 1, MAX_ID
    if args and ":" in args[0]:
        lo, hi = (int(x) for x in args[0].split(":"))
    cat, ser = load(CAT, {}), load(SER, {})
    probed = from_ranges(load(DONE, []))
    todo = [i for i in range(lo, hi + 1) if i not in probed]
    print("sweeping %d-%d: %d ids to probe (%d already banked)"
          % (lo, hi, len(todo), len(cat)), flush=True)
    t0, live = time.time(), 0
    for n in range(0, len(todo), 500):
        chunk = todo[n:n + 500]
        blocked = False
        with ThreadPoolExecutor(WORKERS) as ex:
            for res in ex.map(lambda c: _safe(c), chunk):
                if res == "BLOCK":
                    blocked = True
                    continue
                cid, rec = res
                probed.add(cid)
                if rec:
                    live += 1
                    cat[str(cid)] = rec[:5]
                    if rec[1]:
                        ser[str(rec[1])] = rec[5]
        if blocked:                       # backed off inside _safe already
            print("   (some ids were blocked and will be retried on rerun)",
                  flush=True)
        save(CAT, cat); save(SER, ser); save(DONE, to_ranges(probed))
        el = time.time() - t0
        print("   %d/%d probed | %d issues banked | %.0f ids/s"
              % (n + len(chunk), len(todo), len(cat),
                 (n + len(chunk)) / max(el, 1)), flush=True)
    print("done: %d issues in the catalog, %d series" % (len(cat), len(ser)))


def _safe(cid):
    for attempt in range(4):
        try:
            return fetch(cid)
        except Exception:                 # blocked, timed out, or bad JSON
            _local.s = None               # drop a poisoned connection
            time.sleep(2 ** attempt)
    return "BLOCK"


def cmd_status(args):
    cat, ser = load(CAT, {}), load(SER, {})
    probed = load(DONE, [])
    n = sum(b - a + 1 for a, b in probed)
    mu = sum(1 for v in cat.values() if v[3])
    var = sum(1 for v in cat.values() if v[4])
    print("%d ids probed of %d (%.0f%%)" % (n, MAX_ID, 100.0 * n / MAX_ID))
    print("%d issues banked (%d variants), %d on Marvel Unlimited"
          % (len(cat), var, mu))
    print("%d series" % len(ser))
    gaps = []
    prev = 0
    for a, b in probed:
        if a > prev + 1:
            gaps.append((prev + 1, a - 1))
        prev = b
    if prev < MAX_ID:
        gaps.append((prev + 1, MAX_ID))
    if gaps:
        print("unprobed: " + ", ".join("%d-%d" % g for g in gaps[:12]))


def cmd_find(args):
    cat, ser = load(CAT, {}), load(SER, {})
    q = " ".join(args).lower().replace(" ", "_")
    hits = [(int(k), v) for k, v in cat.items() if q in v[0]]
    for cid, v in sorted(hits)[:60]:
        print("%7d  %-52s #%-6s %s" % (cid, v[0], v[2],
                                       "MU" if v[3] else ""))
    print("%d hit(s)" % len(hits))


CMDS = {"sweep": cmd_sweep, "status": cmd_status, "find": cmd_find}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        sys.exit(__doc__)
    CMDS[sys.argv[1]](sys.argv[2:])
