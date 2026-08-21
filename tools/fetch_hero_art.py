#!/usr/bin/env python3
"""Pull the homescreen poster art from the Marvel Database.

The homescreen used to draw each subject as a CSS ramp + texture + inline SVG
emblem. It now shows a real comic cover per subject; this is what fetches them.

Same source and the same downscale pipeline as the shelf covers
(tools/fetch_covers.py -> covers.save_cover), so poster art and omnibus art are
sized identically. The difference is where it lands and how it is wired:

  * files go to Art/Heroes/<hero id>.jpg
  * nothing is generated from them -- the `cover` field in HEROES in index.html
    is hand-written, so a new pick means editing PICKS here and that entry there

    python3 tools/fetch_hero_art.py            # everything missing
    python3 tools/fetch_hero_art.py --all      # refetch, overwriting
    python3 tools/fetch_hero_art.py hulk xmen  # just these

The pick is a curation call, not something a tool can make: one cover that says
"this is the subject" at poster size, era-appropriate to the reading list where
a famous cover exists in that era. Reasoning per hero is in the table below.

Since Aug 2026 none of the live poster art comes from here. All seven subjects
carry art the user supplied by hand (the painted pieces in Art/covers/), which
is better than the wiki's scans for this job: no logo, no barcode and no trade
dress competing with the poster plate. So PICKS below is the fallback route,
not a description of what is on the wall -- every hero is listed in SUPPLIED
and this tool refuses to overwrite them without --replace.
"""
import json, os, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ART  = os.path.join(ROOT, "Art", "Heroes")
API  = "https://marvel.fandom.com/api.php"
UA   = ("COMICS-tracker/1.0 (personal reading tracker; "
        "+https://github.com/nightowl952/COMICS)")

# hero id -> (Marvel Database file title, why this one)
PICKS = {
    "spider-man":     ("Amazing Spider-Man Vol 1 300",
                       "McFarlane, 1988 -- the black suit torn off, Venom's first "
                       "cover. Squarely inside the shelf's 1962-2011 span."),
    "wolverine":      ("Wolverine Vol 1 1",
                       "Miller, 1982 -- the brown-costume limited series that gave "
                       "him a solo book. Collected in Wolverine Omnibus Vol. 2."),
    "hulk":           ("Immortal Hulk Vol 1 1",
                       "Alex Ross, 2018 -- Banner's own grave. Incredible Hulk #340 "
                       "is the more famous cover and was the first pick, but it is "
                       "three quarters Wolverine, who is the poster next to it."),
    "xmen":           ("X-Men Messiah Complex Vol 1 1",
                       "Finch, 2007 -- the one-shot that opens the saga this "
                       "tracker reads."),
    "fantastic-four": ("Fantastic Four Vol 1 51",
                       "Kirby, 1966 -- 'This Man... This Monster!', the Thing alone "
                       "in the rain. Fantastic Four Omnibus Vol. 2."),
    "moon-knight":    ("Moon Knight Vol 7 1",
                       "Shalvey, 2014 -- the white suit. The page sets light:true "
                       "for this subject and the cover is near-white to match."),
    "daredevil":      ("Daredevil Vol 1 227",
                       "Mazzucchelli, 1986 -- the opening chapter of Born Again, "
                       "which the pending reading list is built around."),
}


# Subjects whose live poster art was supplied by hand rather than fetched here.
# --all skips these; --replace overrides, which discards the user's scan.
SUPPLIED = set(PICKS)


def get(url):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read()


def image_url(title):
    """Marvel Database file title -> the stored original's URL.

    Issue pages do not answer prop=pageimages the way the omnibus pages do, so
    this asks the File: page for its imageinfo instead.
    """
    q = urllib.parse.urlencode({"action": "query", "titles": "File:%s.jpg" % title,
                                "prop": "imageinfo", "iiprop": "url|size",
                                "format": "json"})
    d = json.loads(get(API + "?" + q))
    for p in d.get("query", {}).get("pages", {}).values():
        ii = p.get("imageinfo")
        if ii:
            return ii[0]["url"], ii[0]["width"], ii[0]["height"]
    return None, 0, 0


def main(argv):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("needs Pillow:  pip install Pillow")
    sys.path.insert(0, HERE)
    import covers, io
    covers.ART = ART               # save_cover writes here instead of a shelf dir

    force   = "--all" in argv
    replace = "--replace" in argv
    want = [a for a in argv if not a.startswith("-")]
    bad = [w for w in want if w not in PICKS]
    if bad:
        sys.exit("unknown hero id %s\nknown: %s" % (bad, ", ".join(PICKS)))
    todo = want or list(PICKS)
    if not force:
        todo = [h for h in todo
                if not os.path.exists(os.path.join(ART, h + ".jpg"))]
    if not replace:
        held = [h for h in todo if h in SUPPLIED]
        if held:
            print("hand-supplied art, left alone: %s" % ", ".join(held))
            print("  (pass --replace to overwrite it with the wiki's pick)")
        todo = [h for h in todo if h not in SUPPLIED]
    if not todo:
        print("nothing to fetch -- pass --all to refetch, --replace to "
              "overwrite hand-supplied art")
        return

    ok, failed = [], []
    for i, hid in enumerate(todo, 1):
        title, _why = PICKS[hid]
        print("[%d/%d] %-15s %s" % (i, len(todo), hid, title))
        try:
            url, w, h = image_url(title)
            if not url:
                failed.append((hid, "no such file on the wiki"))
                continue
            im = Image.open(io.BytesIO(get(url)))
            rel, size = covers.save_cover(im, hid)
            print("        %s  %dx%d -> %dx%d, %.0f KB"
                  % (rel, w, h, size[0], size[1],
                     os.path.getsize(os.path.join(ROOT, rel)) / 1024))
            ok.append((hid, rel))
        except Exception as e:
            failed.append((hid, str(e)))

    print("\n%d fetched, %d failed" % (len(ok), len(failed)))
    for hid, why in failed:
        print("  !! %-15s %s" % (hid, why))
    if ok:
        print("\nwire them into HEROES in index.html as:")
        for hid, rel in ok:
            print('  cover:"%s",' % rel)
        print("\nthen screenshot the dossier banner and retune `pos` -- the "
              "banner is a 2.8:1\nslot cut out of a 2:3 page, so the crop is "
              "per-cover.")


if __name__ == "__main__":
    main(sys.argv[1:])
