#!/usr/bin/env python3
"""DC catalog harvester -- the DC half of what catalog.py does for Marvel.

DC Universe Infinite's site search is an open Swiftype index behind a proxy on
www.dcuniverseinfinite.com. The proxy wants an `X-Consumer-Key`, and the site
hands that key to every anonymous visitor from /api/5/consumer/www -- it is the
public "www" consumer, the same one the DCUI web app fetches on boot. This tool
fetches it the same way at runtime and never writes it to disk.

Two record types matter:

    comicseries  uuid, title ("Green Lantern (1960-1986)"), first/last release
    book         uuid, slug, series_uuid, issue_number, issue_type, first
                 print release, writers, pencillers, cover asset

A book's DCUI reader URL is /comics/book/<slug>/<uuid>, which is what a Read
button on a DC shelf opens -- the Marvel Unlimited link's equivalent.

    python3 tools/dc_catalog.py series             # sweep every series (~21 requests)
    python3 tools/dc_catalog.py books <uuid> ...   # pull one series' books
    python3 tools/dc_catalog.py status
    python3 tools/dc_catalog.py find "green lantern"

Writes tools/dc_series.json  {"<series uuid>": [title, first, last, count]}
   and tools/dc_catalog.json {"<book uuid>": [slug, series_uuid, number, type,
                              date, writers, pencillers, cover]}
Books are pulled per series rather than swept whole: the index caps paging, a
series is at most a few pages, and a shelf only ever needs a few dozen series.
dc_link.py pulls whatever series it is missing on its own.
"""
import json, os, sys, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
SER = os.path.join(HERE, "dc_series.json")
CAT = os.path.join(HERE, "dc_catalog.json")
PULLED = os.path.join(HERE, "dc_series_pulled.json")

SITE = "https://www.dcuniverseinfinite.com"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124 Safari/537.36"}
_KEY = None


def load(p, d):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def save(p, obj):
    tmp = p + ".tmp"
    json.dump(obj, open(tmp, "w", encoding="utf-8"), ensure_ascii=False,
              separators=(",", ":"), sort_keys=True)
    os.replace(tmp, p)


def key():
    global _KEY
    if _KEY is None:
        r = urllib.request.Request(SITE + "/api/5/consumer/www", headers=UA)
        _KEY = json.load(urllib.request.urlopen(r, timeout=30))["consumer_secret"]
    return _KEY


def search(body, tries=4):
    data = json.dumps(body).encode()
    for n in range(tries):
        try:
            r = urllib.request.Request(
                SITE + "/api/search_proxy/1/search", data=data,
                headers={**UA, "X-Consumer-Key": key(),
                         "content-type": "application/json"})
            return json.load(urllib.request.urlopen(r, timeout=30))
        except urllib.error.HTTPError as e:
            if e.code < 500 and e.code != 429:
                raise
        except urllib.error.URLError:
            pass
        time.sleep(2 ** n)
    raise SystemExit("DCUI search kept failing: %r" % body)


def day(s):
    return (s or "")[:10]


def sweep_series():
    ser = load(SER, {})
    page, pages = 1, 1
    while page <= pages:
        d = search({"q": "", "per_page": 100, "page": page,
                    "document_types": ["comicseries"]})
        pages = d["info"]["comicseries"]["num_pages"]
        for r in d["records"]["comicseries"]:
            ser[r["uuid"]] = [r["title"], day(r.get("first_print_release")
                              or r.get("first_released")),
                              day(r.get("last_released")), r.get("issue_count")]
        print("  page %d/%d  %d series" % (page, pages, len(ser)))
        page += 1
    save(SER, ser)
    print("%d series in %s" % (len(ser), os.path.basename(SER)))


def pull_books(uuids, quiet=False):
    cat, done = load(CAT, {}), set(load(PULLED, []))
    for su in uuids:
        page, pages, n = 1, 1, 0
        while page <= pages:
            d = search({"q": "", "per_page": 100, "page": page,
                        "document_types": ["book"],
                        "filters": {"book": {"series_uuid": su}}})
            pages = d["info"]["book"]["num_pages"]
            for r in d["records"]["book"]:
                cat[r["uuid"]] = [r["slug"], r.get("series_uuid"),
                                  str(r.get("issue_number") or ""),
                                  r.get("issue_type") or "",
                                  day(r.get("first_print_release")
                                      or r.get("first_released")),
                                  r.get("authors__display_name") or [],
                                  r.get("pencillers__display_name") or [],
                                  r.get("base_asset_url") or ""]
                n += 1
            page += 1
        done.add(su)
        if not quiet:
            print("  %s  %d books" % (su, n))
    save(CAT, cat)
    save(PULLED, sorted(done))
    return cat


def status():
    ser, cat, done = load(SER, {}), load(CAT, {}), load(PULLED, [])
    print("%d series swept, %d pulled, %d books banked" % (len(ser), len(done), len(cat)))


def find(q):
    ser = load(SER, {})
    q = q.lower()
    for u, (t, a, b, c) in sorted(ser.items(), key=lambda x: x[1][1]):
        if q in t.lower():
            print("%s  %-50s %s..%s  %s issues" % (u, t, a, b, c))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "status":
        status()
    elif a[0] == "series":
        sweep_series()
    elif a[0] == "books":
        pull_books(a[1:])
    elif a[0] == "find":
        find(" ".join(a[1:]))
    else:
        sys.exit(__doc__)
