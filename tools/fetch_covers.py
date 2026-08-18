#!/usr/bin/env python3
"""Pull omnibus cover scans from the Marvel Database and wire them in.

Same source as the issue contents (see "Where the contents came from" in
CLAUDE.md) -- the wiki stores a cover image per volume page, which the
MediaWiki API hands back via prop=pageimages.

    python3 tools/fetch_covers.py            # every volume still missing a cover
    python3 tools/fetch_covers.py asm-o4     # just these
    python3 tools/fetch_covers.py --all      # refetch, overwriting existing

Downloads, downscales through covers.save_cover (so art from here is the same
size as art added by hand), and writes the cover= line into omnibus_meta.py.
It does NOT regenerate -- finish with:

    python3 tools/build_omnibus_data.py && python3 tools/build_single_file.py
"""
import json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
META = os.path.join(HERE, "omnibus_meta.py")
API  = "https://marvel.fandom.com/api.php"
UA   = "COMICS-tracker/1.0 (personal reading tracker; +https://github.com/nightowl952/COMICS)"

# The volumes in ORDER carry their wiki page title as the ORDER key. The
# PLACEHOLDERS do not (they have no contents pulled yet), so their pages are
# named here -- resolved by search and eyeballed once.
PLACEHOLDER_PAGES = {
    "vs-venom-o1":  "Spider-Man vs. Venom Omnibus Vol 1 1",
    "venom-o1":     "Venomnibus Vol 1 1",
    "venom-o2":     "Venomnibus Vol 1 2",
    "jms-o1":       "Amazing Spider-Man by J. Michael Straczynski Omnibus Vol 1 1",
    "ult-o1":       "Ultimate Spider-Man Omnibus Vol 1 1",
    "ult-death-o1": "Ultimate Comics Spider-Man: Death of Spider-Man Omnibus Vol 1 1",
}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=60).read()


def pages_for(ids):
    sys.path.insert(0, HERE)
    from omnibus_meta import ORDER
    out = {m["id"]: page for page, m in ORDER}
    out.update(PLACEHOLDER_PAGES)
    missing = [i for i in ids if i not in out]
    if missing:
        sys.exit("no wiki page known for %s -- add it to PLACEHOLDER_PAGES" % missing)
    return {i: out[i] for i in ids}


def image_url(page):
    q = urllib.parse.urlencode({"action": "query", "titles": page,
                                "prop": "pageimages", "piprop": "original",
                                "format": "json"})
    d = json.loads(get(API + "?" + q))
    for p in d.get("query", {}).get("pages", {}).values():
        if "original" in p:
            return p["original"]["source"]
        if "missing" in p:
            return None
    return None


def set_cover(vid, rel):
    """Insert (or update) cover="..." on this volume's entry in omnibus_meta.py."""
    s = open(META, encoding="utf-8").read()
    m = re.search(r'id="%s"' % re.escape(vid), s)
    if not m:
        sys.exit("no entry for %s in omnibus_meta.py" % vid)
    # the entry runs to the closing ")," of its dict
    end = s.index("),\n", m.end())
    block = s[m.start():end]
    if 'cover="' in block:
        block2 = re.sub(r'cover="[^"]*"', 'cover="%s"' % rel, block)
    else:
        # hang it off the spine= line so related fields stay together
        sm = re.search(r'( *)spine="[^"]*",\n', block)
        if not sm:
            sys.exit("no spine= line on %s to anchor cover= to" % vid)
        block2 = block[:sm.end()] + '%scover="%s",\n' % (sm.group(1), rel) + block[sm.end():]
    open(META, "w", encoding="utf-8").write(s[:m.start()] + block2 + s[end:])


def main(argv):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("needs Pillow:  pip install Pillow")
    sys.path.insert(0, HERE)
    import covers
    import io

    force = "--all" in argv
    want = [a for a in argv if not a.startswith("-")]
    vols = covers.omni()
    ids = [o["id"] for o in vols]
    have = {o["id"] for o in vols if o.get("cover")}

    if want:
        bad = [w for w in want if w not in ids]
        if bad:
            sys.exit("unknown volume id %s\nknown: %s" % (bad, ", ".join(ids)))
        todo = want if force else [w for w in want if w not in have]
    else:
        todo = ids if force else [i for i in ids if i not in have]

    if not todo:
        print("every volume already has a cover -- pass --all to refetch")
        return

    pages = pages_for(todo)
    ok, failed = [], []
    for i, vid in enumerate(todo, 1):
        page = pages[vid]
        print("[%d/%d] %-14s %s" % (i, len(todo), vid, page))
        try:
            url = image_url(page)
            if not url:
                print("        no cover image on that page"); failed.append(vid); continue
            raw = get(url)
            rel, size = covers.save_cover(Image.open(io.BytesIO(raw)), vid, quiet=True)
            set_cover(vid, rel)
            print("        -> %s  %dx%d  %.0f KB (from %.0f KB)"
                  % (rel, size[0], size[1],
                     os.path.getsize(os.path.join(ROOT, rel)) / 1024, len(raw) / 1024))
            ok.append(vid)
        except Exception as e:
            print("        FAILED: %s" % e); failed.append(vid)
        time.sleep(1)          # the wiki is fine with this pace; don't hammer it

    print("\n%d fetched, %d failed" % (len(ok), len(failed)))
    if failed:
        print("failed: %s" % ", ".join(failed))
    print("\nnow run: python3 tools/build_omnibus_data.py && python3 tools/build_single_file.py")


if __name__ == "__main__":
    main(sys.argv[1:])
