#!/usr/bin/env python3
"""Cover art pipeline for an omnibus shelf.

Two jobs:

  audit                     what every volume has, and whether the mobile
                            build still fits inside the artifact size limit
  add <volume-id> <image>   optimise a scan into the hero's art dir as
                            <id>.jpg and print the line to paste into its
                            metadata module

Both take --hero <key> (default spider-man); see tools/heroes.py.

Covers used to matter for build size: build_single_file.py inlined every one
into comics-mobile.html as a base64 data URI, because the Claude Artifact had
no sibling files and a CSP that blocked relative image requests. That is over
-- the artifact is retired, both remaining surfaces resolve Art/..., and the
mobile page now ships the paths. So the 16MB ceiling is no longer what
WIDTH/QUALITY defend.

What they still defend is the phone: six shelves of art is downloaded a tile
at a time, and consistency across all six is worth more than sharpness on one.
A genuinely better scan can be dropped in without worrying about a budget.

Needs Pillow:  pip install Pillow
"""
import json, os, sys

HERE    = os.path.dirname(os.path.abspath(__file__))
ROOT    = os.path.dirname(HERE)
# bound per hero by _use(); the module-level defaults keep `import covers`
# working for callers that only want save_cover()
TRACKER = None
ART     = None


def _use(key=None):
    global TRACKER, ART, HERO
    sys.path.insert(0, HERE)
    import heroes
    HERO = heroes.resolve(key)
    TRACKER, ART = HERO["tracker_path"], HERO["art_path"]
    return HERO

WIDTH   = 700          # tiles render ~196px wide; 700 covers 2x displays and the banner
MIN_WIDTH = 500        # below this a cover looks soft on a 2x tile
QUALITY = 82           # ~150KB/cover -- 18 of them stay comfortably inside the budget
BUDGET  = 16 * 1024**2 # artifact hard limit


def omni():
    if TRACKER is None:
        _use()
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
            rows.append((o["id"], "-", "no cover", "", ""))
            continue
        p = os.path.join(ROOT, c)
        if not os.path.exists(p):
            rows.append((o["id"], "!!", "MISSING", "", c))
            continue
        n = os.path.getsize(p)
        total += n
        dim = ""
        try:
            from PIL import Image
            w, h = Image.open(p).size
            dim = "%dx%d" % (w, h)
            if w < MIN_WIDTH:
                dim += " soft"
        except Exception:
            pass
        flag = "  " if n <= 300 * 1024 else "!!"
        rows.append((o["id"], flag, "%.0f KB" % (n / 1024), dim, c))

    print("%-14s %-3s %-10s %-14s %s" % ("VOLUME", "", "SIZE", "PIXELS", "PATH"))
    for r in rows:
        if len(r) == 4:
            r = (r[0], r[1], r[2], "", r[3])
        print("%-14s %-3s %-10s %-14s %s" % r)

    soft = [r[0] for r in rows if len(r) == 5 and "soft" in r[3]]
    if soft:
        print("\n%d cover(s) below %dpx wide -- fine on a standard display, soft on a\n"
              "retina tile and in the detail banner. The Marvel Database has no larger\n"
              "original for these; drop in a better scan with `covers.py add` if you\n"
              "find one: %s" % (len(soft), MIN_WIDTH, ", ".join(soft)))

    have = sum(1 for o in vols if o.get("cover"))
    built = os.path.join(ROOT, "comics-mobile.html")
    now = os.path.getsize(built) if os.path.exists(built) else 0
    print("\n%d/%d volumes have a cover, %.1f MB of art on this shelf" % (
        have, len(vols), total / 1e6))
    # Covers are served by path now, not baked in, so this shelf's art does not
    # move the page size at all. Reported anyway because it is what a phone
    # downloads a tile at a time.
    print("comics-mobile.html is %.1f MB (limit %.0f MB) -- covers are served "
          "from Art/, not inlined" % (now / 1e6, BUDGET / 1024 ** 2))
    if have:
        print("%.0f KB per cover on average; target is %dpx wide / q%d"
              % (total / have / 1e3, WIDTH, QUALITY))
    if now > BUDGET:
        sys.exit("\n!! the built page is over the build size limit")


def save_cover(im, vid, quiet=False):
    """Downscale to WIDTH/QUALITY and write <hero art dir>/<vid>.jpg.

    Returns the repo-relative path to drop into omnibus_meta.py. Shared with
    fetch_covers.py so both routes produce identically sized art.
    """
    from PIL import Image
    if ART is None:
        _use()
    w, h = im.size
    ratio = w / h
    if not (0.60 <= ratio <= 0.75) and not quiet:
        print("!! aspect %.2f is off the 0.67 the tiles expect -- it will be "
              "centre-cropped by object-fit:cover" % ratio)

    im = im.convert("RGB")
    if w > WIDTH:
        im = im.resize((WIDTH, round(h * WIDTH / w)), Image.LANCZOS)

    os.makedirs(ART, exist_ok=True)
    out = os.path.join(ART, vid + ".jpg")
    im.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    return os.path.relpath(out, ROOT).replace(os.sep, "/"), im.size


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

    rel, (iw, ih) = save_cover(Image.open(src), vid)
    out = os.path.join(ROOT, rel)
    im = type("I", (), {"width": iw, "height": ih})
    print("wrote %s  (%dx%d, %.0f KB, was %.0f KB)"
          % (rel, im.width, im.height, os.path.getsize(out) / 1024, os.path.getsize(src) / 1024))
    print("\nadd this to the %s entry in tools/%s.py:\n" % (vid, HERO["meta"]))
    print('  cover="%s",' % rel)
    print("\nthen:  python3 tools/build_omnibus_data.py --hero %s"
          " && python3 tools/build_single_file.py" % HERO["key"])


if __name__ == "__main__":
    # keep `covers.py audit | head` from spewing a BrokenPipeError traceback
    try:
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    sys.path.insert(0, HERE)
    import heroes
    _key, a = heroes.arg(sys.argv[1:])
    _use(_key)
    if a[:1] == ["audit"]:
        audit()
    elif a[:1] == ["add"] and len(a) == 3:
        add(a[1], a[2])
    else:
        sys.exit(__doc__)
