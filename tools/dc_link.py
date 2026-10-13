#!/usr/bin/env python3
"""Link every DC shelf issue to its DC Universe Infinite book.

The DC half of link_issues.py, and much smaller, because the DCUI catalog is
better shaped than marvel.com's: a series record carries its years in the
title ("Green Lantern (1960-1986)") and a book record carries its series uuid
and its issue number, so a match is two lookups rather than a slug parse.

    python3 tools/dc_link.py --hero green-lantern          # report only
    python3 tools/dc_link.py --hero green-lantern --write  # -> dc_ids.json

How a shelf series finds its DCUI series:
  1. The meta module pins a display name WITH the year the series started --
     "Green Lantern (1960)". That year is load-bearing: there are six DCUI
     series called Green Lantern, and it is the only thing that picks one.
  2. Candidates are DCUI series whose folded title equals the folded name.
     The one whose first-print year is nearest the pinned year wins, and it
     has to be within two years or nothing is chosen.
  3. An annual with no series of its own ("Green Lantern Annual (2011)")
     falls back to the parent series and matches books typed ANNUAL.
  4. DC_SERIES_ALIAS in the meta module pins a wiki series straight to a DCUI
     series uuid, for the naming disagreements no fold can derive. The run
     names every series it could not place, so that table cannot grow
     silently.

Writes tools/dc_ids.json  {"<shelf issue id>": "<book uuid>/<book slug>"}
  and tools/dc_years.json {"<book uuid>": "YYYY-MM-DD"}
The uuid-first shape is deliberate: it is the same "<id>/<slug>" shape the
Marvel store uses, so build_omnibus_data.py splices both with the same code.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import heroes, dc_catalog                     # noqa: E402
import build_omnibus_data as B               # noqa: E402

IDS = os.path.join(HERE, "dc_ids.json")
YEARS = os.path.join(HERE, "dc_years.json")


def fold(s):
    s = s.lower().replace("&", " and ")
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"^the\s+", "", s.strip())
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def series_year(title, first):
    m = re.search(r"\((\d{4})", title)
    return int(m.group(1)) if m else int(first[:4]) if first[:4].isdigit() else None


def numkey(n):
    n = str(n).strip().lstrip("#")
    if re.fullmatch(r"\d+\.0+", n):
        n = n.split(".")[0]
    if re.fullmatch(r"0*\d+", n):
        n = str(int(n))
    return n


# Words a title can gain or lose between the wiki and DCUI without becoming a
# different comic: "World's Finest Comics" is DCUI's "World's Finest", the
# wiki's "Larfleeze Christmas Special" is DCUI's "Larfleeze Christmas".
SOFT = {"special", "comics", "one", "shot"}


def near(a, b):
    a, b = a.split(), b.split()
    if len(a) > len(b):
        a, b = b, a
    return len(a) >= 2 and b[:len(a)] == a and set(b[len(a):]) <= SOFT


def place(name, year, ser):
    """DCUI series uuid for a display name and start year, or None."""
    want = fold(name)
    for test in (lambda t: fold(t) == want, lambda t: near(fold(t), want)):
        cands = [(u, series_year(t, a)) for u, (t, a, b, c) in ser.items()
                 if test(t)]
        cands = [(u, y) for u, y in cands if y is not None]
        if not cands:
            continue
        if year is None:
            if len(cands) == 1:
                return cands[0][0]
            continue
        u, y = min(cands, key=lambda c: abs(c[1] - year))
        if abs(y - year) <= 2:
            return u
    return None


def slugify(s):
    s = re.sub(r"\(.*?\)", " ", s.lower()).replace("'", "")
    return "-".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def split_slug(slug):
    """'green-lantern-2011-23' -> ('green-lantern-2011', '23')."""
    stem, _, tail = slug.rpartition("-")
    return stem, tail


def main():
    key, argv = heroes.arg(sys.argv[1:])
    h = heroes.resolve(key)
    mod = heroes.meta_module(h)
    write = "--write" in argv
    B.RAW = h["raw_path"]
    arr = B.build_all(mod)
    table = dict(B.SERIES)
    table.update(getattr(mod, "SERIES_EXTRA", {}) or {})
    by_code = {}
    for base, (code, disp) in table.items():
        by_code.setdefault(code, disp)
    alias = getattr(mod, "DC_SERIES_ALIAS", {}) or {}
    issue_alias = getattr(mod, "DC_ISSUE_ALIAS", {}) or {}

    ser = dc_catalog.load(dc_catalog.SER, {})
    if not ser:
        sys.exit("no DCUI series banked -- run: python3 tools/dc_catalog.py series")

    issues = {}
    for o in arr:
        for c in o["chapters"]:
            for i in c["issues"]:
                issues[i["id"]] = i

    codes = sorted({iid.rsplit("-", 1)[0] for iid in issues},
                   key=lambda c: -len(c))
    placed, annual, unplaced = {}, {}, []
    for code in codes:
        disp = by_code.get(code, code)
        if code in alias:
            placed[code] = alias[code]
            continue
        m = re.match(r"^(.*?)\s*\((\d{4})\)\s*$", disp)
        name, year = (m.group(1), int(m.group(2))) if m else (disp, None)
        u = place(name, year, ser)
        if u is None and re.search(r"\bannual\b", name, re.I):
            parent = re.sub(r"\s*\bannual\b", "", name, flags=re.I)
            u = place(parent, year, ser)
            if u:
                annual[code] = True
        if u:
            placed[code] = u
        else:
            unplaced.append((code, disp))

    need = sorted(set(placed.values()) - set(dc_catalog.load(dc_catalog.PULLED, [])))
    if need:
        print("pulling %d series from DCUI..." % len(need))
        dc_catalog.pull_books(need, quiet=True)
    cat = dc_catalog.load(dc_catalog.CAT, {})
    # DCUI's issue_number field cannot be trusted -- Green Lantern (2011) #0 is
    # filed as "1", and that series also carries its annuals and its Futures
    # End one-shot inline as plain ISSUEs. The SLUG is reliable
    # ("green-lantern-2011-0", "green-lantern-annual-2012-1"), so matching is
    # done on it: a series' own issues share one stem, which is the most
    # common stem among its ISSUE books.
    books, stems = {}, {}
    for bu, (slug, su, num, typ, date, w, p, img) in cat.items():
        if typ.upper() != "ISSUE":
            continue
        stem, tail = split_slug(slug)
        books.setdefault(su, []).append((bu, slug, stem, tail, date))
    for su, bs in books.items():
        count = {}
        for b in bs:
            count[b[2]] = count.get(b[2], 0) + 1
        stems[su] = max(count, key=count.get)
    every = [b for bs in books.values() for b in bs]

    store = dc_catalog.load(IDS, {})
    years = dc_catalog.load(YEARS, {})
    found, missing = {}, []
    for iid, i in sorted(issues.items()):
        if iid in issue_alias:
            bu = issue_alias[iid]
            if bu not in cat:
                d = dc_catalog.search({"q": "", "per_page": 1, "document_types": ["book"],
                                       "filters": {"book": {"uuid": bu}}})
                for r in d["records"]["book"]:
                    cat[bu] = [r["slug"], r.get("series_uuid"),
                               str(r.get("issue_number") or ""), "ISSUE",
                               (r.get("first_print_release") or "")[:10],
                               r.get("authors__display_name") or [],
                               r.get("pencillers__display_name") or [],
                               r.get("base_asset_url") or ""]
            if bu not in cat:
                sys.exit("DC_ISSUE_ALIAS[%r] = %s is not on DCUI" % (iid, bu))
            found[iid] = (bu, cat[bu][0], cat[bu][4])
            continue
        code, num = iid.rsplit("-", 1)
        want = numkey(num)
        su = placed.get(code)
        hit = []
        if su and annual.get(code):
            hit = [b for b in books.get(su, []) if "annual" in b[2] and b[3] == want]
        elif su:
            # The stem is not even constant within one series --
            # "green-lantern-2005-2011-1" sits beside "green-lantern-2007-21".
            # Accept the series' commonest stem, or any stem that ends in a
            # year and is not a variant (annual, "feat", special, Futures End).
            pool = [b for b in books.get(su, []) if b[3] == want and (
                    b[2] == stems[su] or (re.search(r"-\d{4}$", b[2]) and
                    not re.search(r"annual|feat|special|futures-end|secret", b[2])))]
            hit = [b for b in pool if b[2] == stems[su]] or pool
            if len(hit) > 1:
                # DCUI carries a few issues twice; any copy reads the same
                # comic, so take the earliest-dated deterministically
                hit = sorted(hit, key=lambda b: (b[4] or "9999", b[0]))[:1]
        if not hit:
            # A one-shot DCUI files inside its parent ("Green Lantern: Futures
            # End" is a book in Green Lantern (2011-2016)) or under a series of
            # its own whose title differs: look for its slug anywhere banked.
            disp = by_code.get(code, code)
            ym = re.search(r"\((\d{4})\)\s*$", disp)
            pat = re.compile(r"^%s(?:-(\d{4}))?$" % re.escape(slugify(disp)))
            hit = []
            for b in every:
                m = pat.match(b[2])
                # a year in the stem has to be this series' year (see the
                # era guard below for what happens without this)
                if m and b[3] == want and (not (m.group(1) and ym) or
                                           abs(int(m.group(1)) - int(ym.group(1))) <= 1):
                    hit.append(b)
        if not hit:
            # Last resort, one search request: DCUI files many one-shots
            # under an umbrella series ("Untold Tales of Blackest Night" is a
            # book in Blackest Night; Green Lantern Secret Files 2005 is in
            # "DC Secret Files"). Accept only a book whose slug starts with
            # this series' own name and ends in this issue's number.
            disp = by_code.get(code, code)
            name = re.sub(r"\s*\(\d{4}\)\s*$", "", disp)
            ym = re.search(r"\((\d{4})\)\s*$", disp)
            year = int(ym.group(1)) if ym else None
            sl = slugify(name)

            def same_comic(stem, date):
                # THE ERA GUARD, and it is not optional: without it this
                # search linked Green Lantern (1960) #94-122 to Green Lantern
                # (1990) #94-122 and The Flash (1959) #226-246 to The Flash
                # (1987) -- same names, same numbers, different comics. A
                # stem that names a year must name this series' year; one
                # that does not must at least not be dated before the series
                # began.
                if year is None:
                    return True
                sy = re.search(r"-(\d{4})(?:-\d{4})?$", stem)
                if sy:
                    return abs(int(sy.group(1)) - year) <= 1
                return not date or int(date[:4]) >= year - 1
            d = dc_catalog.search({"q": "%s %s" % (name, want), "per_page": 10,
                                   "document_types": ["book"]})
            for r in d["records"]["book"]:
                if (r.get("issue_type") or "").upper() != "ISSUE":
                    continue
                stem, tail = split_slug(r["slug"])
                date = (r.get("first_print_release") or "")[:10]
                if stem.startswith(sl) and tail == want and same_comic(stem, date):
                    hit.append((r["uuid"], r["slug"], stem, tail,
                                (r.get("first_print_release") or "")[:10]))
                    cat[r["uuid"]] = [r["slug"], r.get("series_uuid"),
                                      str(r.get("issue_number") or ""), "ISSUE",
                                      (r.get("first_print_release") or "")[:10],
                                      r.get("authors__display_name") or [],
                                      r.get("pencillers__display_name") or [],
                                      r.get("base_asset_url") or ""]
            if len(hit) > 1:
                hit = sorted(hit, key=lambda b: (b[4] or "9999", b[0]))[:1]
        if len(hit) == 1:
            found[iid] = (hit[0][0], hit[0][1], hit[0][4])
        elif not su and not hit:
            missing.append((iid, "series not placed"))
        else:
            where = ser[su][0] if su else "the catalog"
            missing.append((iid, "%d candidates in %s" % (len(hit), where)
                            if hit else "no #%s in %s" % (want, where)))

    print("[%s] %d unique issues | %d linked | %d not linked"
          % (h["key"], len(issues), len(found), len(missing)))
    print("series placed: %d of %d" % (len(placed), len(codes)))
    for code, disp in unplaced:
        print("  !! no DCUI series for %-8s %s" % (code, disp))
    for code, su in sorted(placed.items()):
        print("    %-8s -> %s%s" % (code, ser[su][0], "  [annuals]" if annual.get(code) else ""))
    for iid, why in missing:
        print("  -- %-12s %s" % (iid, why))

    if write:
        dc_catalog.save(dc_catalog.CAT, cat)   # keeps books the search found
        for iid, (bu, slug, date) in found.items():
            store[iid] = "%s/%s" % (bu, slug)
            if date:
                years[bu] = date
        for iid, _ in missing:
            store.pop(iid, None)
        json.dump(dict(sorted(store.items())), open(IDS, "w", encoding="utf-8"),
                  indent=0, ensure_ascii=False)
        json.dump(dict(sorted(years.items())), open(YEARS, "w", encoding="utf-8"),
                  indent=0, ensure_ascii=False)
        print("wrote %s (%d) and %s (%d)" % (os.path.basename(IDS), len(store),
                                             os.path.basename(YEARS), len(years)))


if __name__ == "__main__":
    main()
