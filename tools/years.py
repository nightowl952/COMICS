#!/usr/bin/env python3
"""Harvest each linked issue's publication date from marvel.com's open catalog.

The shelf knew *which* issue every row was and *where* to read it, but never
when it came out -- so a chapter of 1968 comics and a chapter of 1994 comics
looked identical on the page. That year is the whole point of reading a shelf
historically, and it turns out to be one field away: the same bifrost catalog
`link_issues.py` already matches against carries `published_date` per issue.

    {"data": {"published_date": "1962-05-01", ...}}

So this probes only the ids we already link (tools/marvel_ids.json), not the
140,000-id space `catalog.py sweep` walks -- about 6,100 requests, a few
minutes, and resumable. It writes tools/marvel_years.json:

    {"<marvel comic id>": "YYYY-MM-DD"}

keyed by marvel's id rather than by shelf issue id, because the id store is
shared across every hero and the same comic has to key the same way on all of
them. `build_omnibus_data.py` joins the two into the per-page YEARS map.

    python3 tools/years.py            # everything linked but not yet dated
    python3 tools/years.py --all      # re-probe, overwriting
    python3 tools/years.py status
"""
import json, os, sys, threading
from concurrent.futures import ThreadPoolExecutor

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
IDS = os.path.join(HERE, "marvel_ids.json")
OUT = os.path.join(HERE, "marvel_years.json")
DEAD = os.path.join(HERE, "marvel_years_dead.json")

API = "https://bifrost.marvel.com/catalog/comics/%s"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")
WORKERS = 24


def load(p, d):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def save(p, obj):
    tmp = p + ".tmp"
    json.dump(obj, open(tmp, "w", encoding="utf-8"),
              indent=0, sort_keys=True, ensure_ascii=False)
    os.replace(tmp, p)


_local = threading.local()


def session():
    s = getattr(_local, "s", None)
    if s is None:
        s = _local.s = requests.Session()
        s.headers.update({"User-Agent": UA, "Accept": "application/json"})
    return s


def probe(cid):
    """-> (cid, 'YYYY-MM-DD') or (cid, None). A date of 0000-00-00 is Marvel's
    own 'unknown', which is a real answer and not a failed request."""
    for _ in range(3):
        try:
            r = session().get(API % cid, timeout=20)
            if r.status_code == 404:
                return cid, None
            if r.status_code != 200:
                continue
            d = (r.json() or {}).get("data") or {}
            pd = d.get("published_date") or ""
            if pd.startswith("0000"):
                # fall back to the print date the digital record carries --
                # a handful of older issues have one where the top-level
                # published_date is zeroed.
                pd = ((d.get("digital_comic") or {}).get("print_format_date")
                      or "")
            return cid, (pd or None)
        except Exception:
            continue
    return cid, None


def main():
    args = sys.argv[1:]
    ids = load(IDS, {})
    years = load(OUT, {})
    dead = set(load(DEAD, []))

    # marvel_ids.json values are "<comic id>/<slug>"; the id is what we probe.
    want = sorted({v.split("/", 1)[0] for v in ids.values() if "/" in v},
                  key=lambda x: int(x) if x.isdigit() else 0)

    if "status" in args:
        have = sum(1 for c in want if c in years)
        print("%d linked issues, %d dated (%.0f%%), %d with no date on "
              "marvel.com, %d not yet probed"
              % (len(want), have, 100.0 * have / max(1, len(want)),
                 len([c for c in want if c in dead]),
                 len([c for c in want if c not in years and c not in dead])))
        return

    todo = want if "--all" in args else [
        c for c in want if c not in years and c not in dead]
    if not todo:
        print("nothing to do -- every linked issue already has a date")
        return
    print("probing %d of %d linked issues" % (len(todo), len(want)))

    got = 0
    with ThreadPoolExecutor(WORKERS) as ex:
        for n, (cid, pd) in enumerate(ex.map(probe, todo), 1):
            if pd:
                years[cid] = pd
                got += 1
            else:
                dead.add(cid)
            if n % 500 == 0:
                print("  %d/%d  (%d dated)" % (n, len(todo), got))
                save(OUT, years)
                save(DEAD, sorted(dead))

    save(OUT, years)
    save(DEAD, sorted(dead))
    print("done: %d dated, %d with no usable date. %d in the store."
          % (got, len(todo) - got, len(years)))


if __name__ == "__main__":
    main()
