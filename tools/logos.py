#!/usr/bin/env python3
"""The subject logos that sit in the homescreen poster plate.

One file per subject, Art/Logos/<hero id>.png, pointed at by `logo` in that
hero's HEROES entry. Same shape as Art/Heroes/<hero id>.jpg and the shelf
covers -- named by id, not by whatever the source file was called.

    python3 tools/logos.py add spider-man ~/Desktop/Spiderman-Logo-1994.png
    python3 tools/logos.py audit

`add` does the two things that matter and are easy to get wrong by hand:

  * **crops to the artwork.** Logo PNGs arrive with wildly different amounts of
    transparent margin baked in -- two of the seven were 320x320 files holding
    a 288x109 logo. Left alone, that margin is real layout: the plate sizes the
    <img>, so a logo with 40% padding renders 40% smaller than one without and
    the wall looks arbitrary. Cropping to the alpha bounding box makes every
    subject's logo fill the same box.
  * **keeps the alpha.** PNG stays PNG, and a palette image is promoted to
    RGBA first -- `P` mode with a `transparency` index survives a resize badly.

There is no fetch route here, unlike fetch_hero_art.py. A printed logo is not
on the Marvel Database as a clean transparent asset, so these are supplied by
hand and this only normalises them.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ART  = os.path.join(ROOT, "Art", "Logos")

WIDTH   = 500          # plate renders it ~170px wide; 500 covers a 3x display
MIN_TIGHT = 220        # below this the source was too small to look clean

HERO_IDS = ["spider-man", "wolverine", "hulk", "xmen",
            "fantastic-four", "moon-knight", "daredevil"]


def save_logo(im, hid):
    """Crop to the artwork, downscale to WIDTH, write Art/Logos/<hid>.png."""
    from PIL import Image
    im = im.convert("RGBA")
    bb = im.getchannel("A").getbbox()
    if bb is None:
        raise SystemExit("%s is fully transparent" % hid)
    im = im.crop(bb)
    tight = im.size
    if im.width > WIDTH:
        im = im.resize((WIDTH, max(1, round(im.height * WIDTH / im.width))),
                       Image.LANCZOS)
    os.makedirs(ART, exist_ok=True)
    out = os.path.join(ART, hid + ".png")
    im.save(out, "PNG", optimize=True)
    return os.path.relpath(out, ROOT).replace(os.sep, "/"), tight, im.size


def add(hid, src):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("needs Pillow:  pip install Pillow")
    if hid not in HERO_IDS:
        sys.exit("unknown hero id %r\nknown: %s" % (hid, ", ".join(HERO_IDS)))
    rel, tight, size = save_logo(Image.open(src), hid)
    print("%-15s %s" % (hid, os.path.basename(src)))
    print("   cropped to %dx%d, saved %dx%d -> %s (%.0f KB)"
          % (tight[0], tight[1], size[0], size[1], rel,
             os.path.getsize(os.path.join(ROOT, rel)) / 1024))
    if min(tight) and tight[0] < MIN_TIGHT:
        print("   !! source artwork is only %dpx wide -- soft on a 2x tile"
              % tight[0])
    print('\n   logo:"%s",' % rel)


def audit():
    try:
        from PIL import Image
    except ImportError:
        sys.exit("needs Pillow:  pip install Pillow")
    total = 0
    for hid in HERO_IDS:
        p = os.path.join(ART, hid + ".png")
        if not os.path.exists(p):
            print("%-15s -   no logo" % hid)
            continue
        im = Image.open(p)
        n = os.path.getsize(p)
        total += n
        has_a = im.mode in ("RGBA", "LA") or "transparency" in im.info
        print("%-15s %-11s %-6s %6.0f KB%s"
              % (hid, "%dx%d" % im.size, im.mode, n / 1024,
                 "" if has_a else "   !! NO ALPHA -- will render as a box"))
    print("\n%d/%d subjects have a logo, %.0f KB in total"
          % (sum(os.path.exists(os.path.join(ART, h + ".png"))
                 for h in HERO_IDS), len(HERO_IDS), total / 1e3))


def main(argv):
    if not argv or argv[0] not in ("add", "audit"):
        sys.exit(__doc__)
    if argv[0] == "audit":
        return audit()
    if len(argv) != 3:
        sys.exit("usage: logos.py add <hero-id> <image>")
    add(argv[1], argv[2])


if __name__ == "__main__":
    main(sys.argv[1:])
