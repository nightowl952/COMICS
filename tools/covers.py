#!/usr/bin/env python3
"""Cover art pipeline for the Spider-Man omnibus shelf.

Two jobs:

  audit                     what every volume has, and whether the mobile
                            build still fits inside the artifact size limit
  add <volume-id> <image>   optimise a scan into Art/Spider-Man/<id>.jpg and
                            print the one line to paste into omnibus_meta.py

Covers matter for size, not just looks: tools/build_single_file.py inlines
every cover into comics-mobile.html as a base64 data URI (the artifact runs
under a CSP that blocks relative image requests), and base64 costs ~33% on
top of the file. A folder of full-resolution scans blows the 16MB artifact
budget long before all 18 volumes are covered -- hence WIDTH/QUALITY below.

Needs Pillow:  pip install Pillow
"""
import json, os, re, sys

HERE    = os.path.dirname(os.path.abspath(__file__))
ROOT    = os.path.dirname(HERE)
TRACKER = os.path.join(ROOT, "spiderman-reading-tracker.html")
ART     = os.path.join(ROOT, "Art", "Spider-Man")

WIDTH   = 700          # tiles render ~196px wide; 700 covers 2x displays and the banner
QUALITY = 82           # ~150KB/cover -- 18 of them stay comfortably inside the budget
BUDGET  = 16 * 1024**2 # artifact hard limit
TARGET  = 12 * 1024**2 # leave headroom; warn past this


def omni():
    h = open(TRACKER, encoding="utf-8").read()
    s = h.index("const OMNI = [")
    e = h.index("\n];", s)
    return json.loads(h[s + len("const OMNI = "):e + 2])


def audit():
    vols = omni()
    total = 0
    rows = []
    for o in vols:
        c = o.get("cover")
        if not c:
            rows.append((o["id"], "-", "no cover", ""))
            continue
        p = os.path.join(ROOT, c)
        if not os.path.exists(p):
            rows.append((o["id"], "!!", "MISSING FILE", c))
            continue
        n = os.path.getsize(p)
        total += n
        flag = "  " if n <= 300 * 1024 else "!!"
        rows.append((o["id"], flag, "%.0f KB" % (n / 1024), c))

    print("%-14s %-3s %-13s %s" % ("VOLUME", "", "SIZE", "PATH"))
    for r in rows:
        print("%-14s %-3s %-13s %s" % r)

    have = sum(1 for o in vols if o.get("cover"))
    built = os.path.join(ROOT, "comics-mobile.html")
    now = os.path.getsize(built) if os.path.exists(built) else 0
    # the built page already carries the inlined covers -- strip them back out
    # so `base` is the page without any art, and projections do not double-count
    base = now - sum(len(m) for m in re.findall(r"data:image/[^\"]+", 
                     open(built, encoding="utf-8").read())) if now else 0
    est = base + int(total * 1.37)
    print("\n%d/%d volumes have a cover, %.1f MB of art" % (have, len(vols), total / 1e6))
    print("comics-mobile.html is %.1f MB now; page without art is %.1f MB"
          % (now / 1e6, base / 1e6))
    print("with these covers inlined: ~%.1f MB (limit %.0f MB)" % (est / 1e6, BUDGET / 1e6))

    if have:
        per = total / have
        full = base + int(per * len(vols) * 1.37)
        print("at this average, all %d covers -> ~%.1f MB" % (len(vols), full / 1e6))
        if full > TARGET:
            print("\n!! projected build is too big. Re-run `covers.py add` on the\n"
                  "   volumes flagged !! above to shrink them to %dpx/q%d." % (WIDTH, QUALITY))
    if est > BUDGET:
        sys.exit("\n!! already over the artifact limit -- shrink covers before publishing")


def add(vid, src):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("needs Pillow:  pip install Pillow")

    ids = [o["id"] for o in omni()]
    if vid not in ids:
        sys.exit("unknown volume id %r\nknown: %s" % (vid, ", ".join(ids)))
    if not os.path.exists(src):
        sys.exit("no such image: %s" % src)

    im = Image.open(src)
    w, h = im.size
    ratio = w / h
    if not (0.60 <= ratio <= 0.75):
        print("!! aspect %.2f is off the 0.67 the tiles expect -- it will be "
              "centre-cropped by object-fit:cover" % ratio)

    im = im.convert("RGB")
    if w > WIDTH:
        im = im.resize((WIDTH, round(h * WIDTH / w)), Image.LANCZOS)

    os.makedirs(ART, exist_ok=True)
    out = os.path.join(ART, vid + ".jpg")
    im.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)

    rel = os.path.relpath(out, ROOT).replace(os.sep, "/")
    print("wrote %s  (%dx%d, %.0f KB, was %.0f KB)"
          % (rel, im.width, im.height, os.path.getsize(out) / 1024, os.path.getsize(src) / 1024))
    print("\nadd this to the %s entry in tools/omnibus_meta.py:\n" % vid)
    print('  cover="%s",' % rel)
    print("\nthen:  python3 tools/build_omnibus_data.py && python3 tools/build_single_file.py")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["audit"]:
        audit()
    elif a[:1] == ["add"] and len(a) == 3:
        add(a[1], a[2])
    else:
        sys.exit(__doc__)
