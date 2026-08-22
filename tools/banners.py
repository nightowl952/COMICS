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

It reports EVERY file in the folder, including ones it cannot open. That is not
tidiness: it used to filter on a fixed extension list and say nothing about the
rest, so a .heic straight off a phone vanished without a word -- which looks
from the outside like the tool ignoring an image that is plainly sitting there.
It also does not recurse; a nested folder is named in the report, not walked.

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
# No extension whitelist. Anything Pillow can open is an image; anything it
# cannot is reported by name rather than dropped. See add_folder().
SKIP = (".ds_store",)


def save(src, key):
    from PIL import Image
    try:
        im = Image.open(src)
    except Exception:
        if src.lower().endswith((".heic", ".heif")):
            raise SystemExit("Cannot read %s -- HEIC needs `pip3 install pillow-heif`, "
                             "or export it as JPEG first." % os.path.basename(src))
        raise
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
    """Which keys a filename names.

    Two passes, because filenames arrive in every shape. `IndexPage.png` is one
    lowercase token once you strip the capitals, so a whole-word test alone
    misses it -- which is exactly how the homescreen banner sat unplaced through
    two rounds of this. So: split camelCase first, try whole words, and only if
    nothing hits fall back to a substring test, restricted to words of four
    characters or more so "ff" cannot match "stuff".

    A name that hits two keys is still reported rather than resolved.
    """
    stem = os.path.splitext(name)[0]
    stem = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", stem)      # IndexPage -> Index-Page
    stem = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")

    def hits(test):
        out = []
        for k, words in KEYS.items():
            for w in words:
                if test(re.sub(r"[^a-z0-9]+", "-", w)):
                    out.append(k); break
        return out

    whole = hits(lambda w: re.search(r"(^|-)" + re.escape(w) + r"($|-)", stem))
    if whole:
        return whole
    return hits(lambda w: len(w) >= 4 and w.replace("-", "") in stem.replace("-", ""))


def add_folder(folder):
    from PIL import Image
    folder = os.path.expanduser(folder)
    entries = sorted(e for e in os.listdir(folder) if not e.startswith("."))
    if not entries:
        print("nothing in " + folder)
        return

    images, notes = [], []
    for e in entries:
        full = os.path.join(folder, e)
        if os.path.isdir(full):
            notes.append((e, "is a folder -- point add-folder at it directly"))
            continue
        if e.lower().endswith(SKIP):
            continue
        try:
            Image.open(full).verify()
        except Exception as err:
            notes.append((e, "HEIC needs `pip3 install pillow-heif`, or export it as JPEG"
                             if e.lower().endswith((".heic", ".heif"))
                             else "not an image Pillow can read (%s)" % type(err).__name__))
            continue
        images.append(e)

    taken = {}
    for f in images:
        hits = match(f)
        if len(hits) == 1:
            taken.setdefault(hits[0], []).append(f)
        else:
            notes.append((f, ("matches " + "/".join(hits)) if hits else "matches no subject"))
    for key, names in sorted(taken.items()):
        if len(names) > 1:
            notes.append((", ".join(names), "all match %s -- pick one" % key))
            continue
        save(os.path.join(folder, names[0]), key)

    for name, why in notes:
        print("?? %-42s %s" % (name[:42], why))
    if notes:
        print("   place any of those by hand: python3 tools/banners.py add <key> <file>")
        print("   keys: " + ", ".join(KEYS))
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
