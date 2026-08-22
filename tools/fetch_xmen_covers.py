#!/usr/bin/env python3
"""Cover art for the X-Men shelf, which no other tool can do.

`fetch_covers.py` maps a volume id to a Marvel Database page by reading the
hero's `ORDER` keys -- the wiki page titles of the printed books. The four X-Men
volumes were never printed, so they have no page and no cover, and the X-Men
page is deliberately not in `heroes.py` at all.

What stands in for it: each volume takes the cover of the issue it is named
after. `PICKS` below holds that choice and why, the same way `PICKS` in
`fetch_hero_art.py` does for the homescreen posters. Art goes through
`covers.save_cover`, so it is sized identically to every other shelf's.

    python3 tools/fetch_xmen_covers.py            # anything still missing
    python3 tools/fetch_xmen_covers.py xm-o2      # just these
    python3 tools/fetch_xmen_covers.py --all      # refetch everything

The `cover:` line is written straight into the OMNI array in
`xmen-reading-tracker.html`, because that array is hand-written -- there is no
meta module to edit and nothing to regenerate afterwards.

Needs Pillow:  pip install Pillow
"""
import io, json, os, re, sys, urllib.parse, urllib.request

HERE    = os.path.dirname(os.path.abspath(__file__))
ROOT    = os.path.dirname(HERE)
TRACKER = os.path.join(ROOT, "xmen-reading-tracker.html")
ART     = os.path.join(ROOT, "Art", "X-Men")
API     = "https://marvel.fandom.com/api.php"
UA      = "COMICS-tracker/1.0 (personal reading tracker; +https://github.com/nightowl952/COMICS)"

# volume id -> (image file on the Marvel Database, why this one)
#
# Two things decided these. The volume is named after an issue in it, so that
# issue's cover is the honest stand-in for a book jacket that does not exist.
# And where the wiki holds both a printed cover and a textless variant, the
# choice is whichever is *larger* -- which is the printed one three times out of
# four. That is the opposite of the homescreen's rule (see "Artwork" in
# CLAUDE.md, where trade dress fights the poster plate) and it is deliberate:
# these tiles are meant to read as real books, and every other shelf on the site
# shows a printed cover with its logo on it.
PICKS = {
    "xm-o1": ("X-Men_Divided_We_Stand_Vol_1_1.jpg",
              "the 2008 two-issue mini the volume is named after; 1280px, and the "
              "textless variant is only 527px"),
    "xm-o2": ("X-Force_Cable_Messiah_War_Vol_1_1.jpg",
              "the crossover's own one-shot -- chapter 1 of the book's centrepiece; "
              "1280px against 400px textless"),
    "xm-o3": ("Dark_Avengers_Uncanny_X-Men_Utopia_Vol_1_1_Bianchi_Variant.jpg",
              "chapter 1 of Utopia. Not the main cover, which the wiki holds only as a "
              "2063px scan of the whole printed page -- white border, copyright line and "
              "all, which reads as a photocopy on a book jacket. Bianchi's variant is "
              "853px of art and nothing else"),
    "xm-o4": ("X-Men_Second_Coming_Vol_1_1_Textless.jpg",
              "the one place the textless variant wins: 900px against 600px for the "
              "printed cover"),
}


def get(url):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read()


def image_url(fname):
    """Full-size URL for a File: page, so we get the stored original."""
    q = urllib.parse.urlencode({"action": "query", "titles": "File:" + fname,
                                "prop": "imageinfo", "iiprop": "url|size",
                                "format": "json"})
    d = json.loads(get(API + "?" + q))
    for p in d.get("query", {}).get("pages", {}).values():
        if "imageinfo" in p:
            i = p["imageinfo"][0]
            return i["url"], i["width"], i["height"]
    return None, 0, 0


def set_cover(vid, rel):
    """Insert (or replace) cover:"..." on this volume's entry in the OMNI array.

    Anchored to spine:"..." on the entry's opening line, which is the one field
    every volume has and the generator's own convention on the other shelves.
    """
    s = open(TRACKER, encoding="utf-8").read()
    pat = re.compile(r'(\{ id:"%s", spine:"[^"]*", )(cover:"[^"]*", )?' % re.escape(vid))
    m = pat.search(s)
    if not m:
        sys.exit("no entry for %s in %s" % (vid, os.path.basename(TRACKER)))
    open(TRACKER, "w", encoding="utf-8").write(
        s[:m.start()] + m.group(1) + 'cover:"%s", ' % rel + s[m.end():])


def have_cover(vid):
    s = open(TRACKER, encoding="utf-8").read()
    return bool(re.search(r'\{ id:"%s", spine:"[^"]*", cover:"' % re.escape(vid), s))


def main(argv):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("needs Pillow:  pip install Pillow")
    sys.path.insert(0, HERE)
    import covers
    covers.ART = ART          # X-Men is not in heroes.py, so bind the dir by hand

    force = "--all" in argv
    want = [a for a in argv if not a.startswith("-")]
    bad = [w for w in want if w not in PICKS]
    if bad:
        sys.exit("unknown volume id %s\nknown: %s" % (bad, ", ".join(PICKS)))
    todo = (want or list(PICKS)) if force else [v for v in (want or PICKS)
                                                if not have_cover(v)]
    if not todo:
        print("every volume already has a cover -- --all to refetch")
        return 0

    for vid in todo:
        fname, why = PICKS[vid]
        url, w, h = image_url(fname)
        if not url:
            print("%-7s !! no such file on the wiki: %s" % (vid, fname))
            continue
        rel, (iw, ih) = covers.save_cover(Image.open(io.BytesIO(get(url))), vid)
        set_cover(vid, rel)
        print("%-7s %-46s %4dx%-5d -> %s  (%dx%d, %.0f KB)\n        %s"
              % (vid, fname, w, h, rel, iw, ih,
                 os.path.getsize(os.path.join(ROOT, rel)) / 1024, why))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
