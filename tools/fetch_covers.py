#!/usr/bin/env python3
"""Fetch and optimise the omnibus cover art for the Spider-Man shelf.

Source of truth is the Marvel Database wiki's own cover image for each
collected-edition page -- the same wiki the contents come from, queried through
`prop=pageimages`. A handful of volumes have a hand-picked local scan instead
(LOCAL below); those win over the wiki.

Writes two derivatives per volume, both committed:

  Art/Spider-Man/covers/<id>.jpg        long edge 1200px -- the master. Use this one.
  Art/Spider-Man/covers/small/<id>.jpg  long edge 480px  -- for embedding as a
                                        base64 data: URI, which is the only way a
                                        cover survives into a published artifact
                                        (their CSP blocks every external request).

Art/Spider-Man/covers/covers.json is the manifest: one record per volume with its
shelf id, title, creators, era, both file paths and pixel sizes, and the wiki page
the art came from. Nothing in the app reads it -- it is there so a layout tool can
populate a shelf without re-deriving any of this.

Five volumes (stern-o1, larsen-o1, clone-o2, ult-o1, ult-death-o1) only exist on
the wiki at ~325x500, so their master is that size rather than 1200px; mcf-o1 and
utsm-o1 are also under it.

Rerunning is cheap: the full-size downloads are cached under tools/.cover-cache/
(gitignored), so a second run only re-encodes.

    pip install Pillow
    python3 tools/fetch_covers.py            # all volumes
    python3 tools/fetch_covers.py venom-o1   # just these ids
"""
import json, os, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Art", "Spider-Man", "covers")
CACHE = os.path.join(ROOT, "tools", ".cover-cache")
UA = "COMICS-tracker/1.0 (https://github.com/nightowl952/COMICS)"

# shelf id -> Marvel Database page whose cover image to use.
# Two are deliberately not the page you would guess:
#   mcf-o2  the wiki files this book under its "Complete Collection" cover.
#   ult-death-o1  the book is catalogued as Ultimate Comics Spider-Man.
WIKI = {
 "asm-o1":       "Amazing Spider-Man Omnibus Vol 1 1",
 "asm-o2":       "Amazing Spider-Man Omnibus Vol 1 2",
 "asm-o3":       "Amazing Spider-Man Omnibus Vol 1 3",
 "asm-o4":       "Amazing Spider-Man Omnibus Vol 1 4",
 "utsm-o1":      "Untold Tales of Spider-Man Omnibus Vol 1 1",
 "stern-o1":     "Spider-Man by Roger Stern Omnibus Vol 1 1",
 "mcf-o1":       "Amazing Spider-Man by David Michelinie and Todd McFarlane Omnibus Vol 1 1",
 "larsen-o1":    "Spider-Man by David Michelinie and Erik Larsen Omnibus Vol 1 1",
 "vs-venom-o1":  "Spider-Man vs. Venom Omnibus Vol 1 1",
 "venom-o1":     "Venomnibus Vol 1 1",
 "venom-o2":     "Venomnibus Vol 1 2",
 "mcf-o2":       "Spider-Man by Todd McFarlane Omnibus Vol 1 1",
 "clone-o1":     "Spider-Man: Clone Saga Omnibus Vol 1 1",
 "clone-o2":     "Spider-Man: Clone Saga Omnibus Vol 1 2",
 "ben-o1":       "Spider-Man: Ben Reilly Omnibus Vol 1 1",
 "jms-o1":       "Amazing Spider-Man by J. Michael Straczynski Omnibus Vol 1 1",
 "ult-o1":       "Ultimate Spider-Man Omnibus Vol 1 1",
 "ult-death-o1": "Ultimate Comics Spider-Man: Death of Spider-Man Omnibus Vol 1 1",
}

# Hand-picked scans already in the repo. These are the raw cover paintings
# without the omnibus trade dress; delete an entry to fall back to the wiki
# cover, which carries the book's logo bar like the other fifteen.
LOCAL = {
 "asm-o1": "Art/Spider-Man/The Amazing Spider-Man Vol1.png",
 "asm-o2": "Art/Spider-Man/The Amazing Spider-Man Vol2.jpg",
 "asm-o3": "Art/Spider-Man/The Amazing Spider-Man Vol3.jpg",
}

SIZES = [("", 1200, 84), ("small", 480, 72)]


def api(params):
    args = ["curl", "-s", "-m", "40", "-A", UA, "-G", "https://marvel.fandom.com/api.php"]
    for k, v in params.items():
        args += ["--data-urlencode", "%s=%s" % (k, v)]
    return json.loads(subprocess.run(args, capture_output=True, text=True).stdout)


def wiki_cover(page):
    """Original-size URL of the page's lead image, or None."""
    d = api({"action": "query", "titles": page, "prop": "pageimages",
             "piprop": "original", "format": "json"})
    for p in d.get("query", {}).get("pages", {}).values():
        o = p.get("original")
        if o:
            return o["source"].split("/revision/")[0]
    return None


def source_file(cid):
    """Full-size original for one volume, downloading it if need be."""
    if cid in LOCAL:
        return os.path.join(ROOT, LOCAL[cid])
    os.makedirs(CACHE, exist_ok=True)
    cached = os.path.join(CACHE, cid + ".img")
    if os.path.exists(cached) and os.path.getsize(cached) > 2000:
        return cached
    url = wiki_cover(WIKI[cid])
    if not url:
        print("  !! no wiki cover for %s (%s)" % (cid, WIKI[cid]))
        return None
    subprocess.run(["curl", "-s", "-m", "120", "-A", UA, "-o", cached, url], check=True)
    return cached


def encode(cid, src):
    im = Image.open(src)
    if im.mode != "RGB":
        im = im.convert("RGB")
    for sub, edge, q in SIZES:
        d = os.path.join(OUT, sub) if sub else OUT
        os.makedirs(d, exist_ok=True)
        c = im.copy()
        c.thumbnail((edge, edge), Image.LANCZOS)
        path = os.path.join(d, cid + ".jpg")
        c.save(path, "JPEG", quality=q, optimize=True, progressive=True)
        yield c.size, os.path.getsize(path)


def manifest():
    """One record per volume, in shelf order, joining the shelf metadata that
    already lives in the tracker to the files this script just wrote."""
    import re
    html = open(os.path.join(ROOT, "spiderman-reading-tracker.html"), encoding="utf-8").read()
    omni = json.loads(re.search(r"const OMNI = (\[.*?\n\]);\n", html, re.S).group(1))
    out = []
    for i, o in enumerate(omni, 1):
        rec = {
            "id": o["id"],
            "shelfPosition": i,
            "title": o["title"],
            "vol": o["vol"],
            "creators": o["creators"],
            "era": o["era"],
            "released": o["released"],
            "issues": sum(len(c["issues"]) for c in o["chapters"]),
            "chapters": len(o["chapters"]),
            "contentsPending": bool(o.get("placeholder")),
            "note": o["note"],
            "source": ("local scan: " + LOCAL[o["id"]]) if o["id"] in LOCAL
                      else "Marvel Database: " + WIKI[o["id"]],
        }
        for sub, key in (("", "cover"), ("small", "small")):
            rel = "/".join(x for x in ("Art/Spider-Man/covers", sub, o["id"] + ".jpg") if x)
            path = os.path.join(ROOT, rel)
            if os.path.exists(path):
                w, h = Image.open(path).size
                rec[key] = {"path": rel, "w": w, "h": h}
        out.append(rec)
    dest = os.path.join(OUT, "covers.json")
    json.dump(out, open(dest, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("wrote %s (%d volumes)" % (dest, len(out)))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(WIKI)
    total = 0
    for cid in ids:
        src = source_file(cid)
        if not src:
            continue
        line = "%-14s" % cid
        for (w, h), n in encode(cid, src):
            line += "  %4dx%-4d %6.1fkB" % (w, h, n / 1024)
            total += n
        print(line + ("   [local]" if cid in LOCAL else ""))
    print("total %.1f kB across %d volumes" % (total / 1024, len(ids)))
    manifest()
