#!/usr/bin/env python3
"""The above-the-fold banner art, one per page that has one.

Every page's banner is `Art/Banners/<key>.jpg`, where the key is `index` for the
homescreen and the subject's `HEROES` id for a tracker. Nothing generates these
-- they are hand-picked wide art -- so this tool only normalises what you drop
in, the way tools/logos.py does for the printed logos.

    python3 tools/banners.py add index      ~/Desktop/comics-home.png
    python3 tools/banners.py add spider-man ~/Desktop/spidey.jpg
    python3 tools/banners.py add-folder     ~/Desktop
    python3 tools/banners.py audit

`add-folder` matches every image in a folder against the eight keys by name,
which is the cheap path when the files are already named after their subject.
It prints what it matched and what it could not, and never guesses twice for
one key -- an ambiguous name is reported, not resolved.

Sizing: 1800px wide at q82. Wider than a cover because this is displayed at up
to the full viewport width, and the .hb box is about 3.4:1 -- a portrait image
still works but object-fit:cover will take a band out of the middle of it.

A missing banner is not a broken page. `hbFallback()` in each tracker walks
Art/Banners/<id>.jpg -> Art/Heroes/<id>.jpg -> the .hb-fallback ramp, so a
subject with no banner falls back to its poster scan; the homescreen, which has
no poster of its own, falls back to the ramp.

Needs Pillow:  pip install Pillow
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT  = os.path.join(ROOT, "Art", "Banners")

WIDTH   = 1800
QUALITY = 82

# key -> the words a filename can carry to mean it. Order matters only for the
# report; matching requires exactly one key to hit.
KEYS = {
    "index":          ["index", "home", "comics", "homescreen", "main"],
    "spider-man":     ["spider-man", "spiderman", "spidey", "spider"],
    "wolverine":      ["wolverine", "logan"],
    # NB: not "banner" for the Hulk. Every file here is a banner, so the word
    # is in half the filenames and matched Bruce Banner on all of them.
    "hulk":           ["hulk"],
    "xmen":           ["x-men", "xmen", "x men"],
    "fantastic-four": ["fantastic-four", "fantasticfour", "fantastic four", "fantastic", "ff"],
    "moon-knight":    ["moon-knight", "moonknight", "moon knight", "moon"],
    "daredevil":      ["daredevil", "dare devil", "matt murdock"],
}
EXT = (".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp")


def save(src, key):
    from PIL import Image
    im = Image.open(src)
    w, h = im.size
    im = im.convert("RGB")
    if w > WIDTH:
        im = im.resize((WIDTH, round(h * WIDTH / w)), Image.LANCZOS)
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, key + ".jpg")
    im.save(dst, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    note = ""
    if w / h < 1.6:
        note = "  (portrait-ish at %.2f:1 -- the banner is ~3.4:1, so expect a band out of the middle)" % (w / h)
    print("%-15s <- %s   %dx%d -> %dx%d, %dKB%s" %
          (key, os.path.basename(src), w, h, im.size[0], im.size[1],
           os.path.getsize(dst) // 1024, note))


def match(name):
    """Which keys a filename names. Matching is on whole words, so "ff" does not
    hit "stuff" and "moon" does not hit "moonrise"; a name that hits two keys is
    reported rather than resolved."""
    stem = re.sub(r"[^a-z0-9]+", "-", os.path.splitext(name)[0].lower())
    hits = []
    for k, words in KEYS.items():
        for w in words:
            w = re.sub(r"[^a-z0-9]+", "-", w)
            if re.search(r"(^|-)" + re.escape(w) + r"($|-)", stem):
                hits.append(k); break
    return hits


def add_folder(folder):
    folder = os.path.expanduser(folder)
    files = sorted(f for f in os.listdir(folder) if f.lower().endswith(EXT))
    if not files:
        print("no images in " + folder)
        return
    taken, unclear = {}, []
    for f in files:
        hits = match(f)
        if len(hits) == 1:
            taken.setdefault(hits[0], []).append(f)
        else:
            unclear.append((f, hits))
    for key, names in sorted(taken.items()):
        if len(names) > 1:
            unclear.append((", ".join(names), [key]))
            continue
        save(os.path.join(folder, names[0]), key)
    for name, hits in unclear:
        print("?? %-40s %s -- name it after one subject, or use `add <key> <file>`"
              % (name, ("matches " + "/".join(hits)) if hits else "matches nothing"))
    missing = [k for k in KEYS if not os.path.exists(os.path.join(OUT, k + ".jpg"))]
    if missing:
        print("still missing: " + ", ".join(missing))


def audit():
    for key in KEYS:
        p = os.path.join(OUT, key + ".jpg")
        if not os.path.exists(p):
            print("%-15s --" % key)
            continue
        try:
            from PIL import Image
            w, h = Image.open(p).size
            dim = "%dx%d" % (w, h)
            flag = "  soft" if w < 1200 else ""
        except Exception:
            dim, flag = "?", ""
        print("%-15s %-11s %5dKB%s" % (key, dim, os.path.getsize(p) // 1024, flag))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["add"] and len(a) == 3:
        assert a[1] in KEYS, "key must be one of: " + ", ".join(KEYS)
        save(os.path.expanduser(a[2]), a[1])
    elif a[:1] == ["add-folder"] and len(a) == 2:
        add_folder(a[1])
    elif a[:1] == ["audit"]:
        audit()
    else:
        print(__doc__)
