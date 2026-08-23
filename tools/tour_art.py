#!/usr/bin/env python3
"""Fetch the individual issue covers a guided tour points at.

A tour says "look at what Trimpe does with a figure here" and then has to show
it. The omnibus jackets already on disk cannot do that job -- there are 17 of
them for 665 issues, and the one a tour wants is almost always an issue cover,
not a collection's.

The source is the same open catalog everything else here feeds from:
`bifrost.marvel.com/catalog/comics/<id>` carries `image_url` and
`image_extension`, which together are Marvel's own scan. So a tour figure is
resolved exactly the way a deep link is -- shelf issue id -> marvel id ->
asset -- and nothing is hand-sourced.

    python3 tools/tour_art.py hulk hulk-1 hulk-181 hulk-340
    python3 tools/tour_art.py hulk --list          # what is already fetched

Writes Art/Tours/<hero>/<shelf issue id>.jpg through covers.save_cover, so the
art is the same 700px/q82 as every jacket on the site.
"""
import io, json, os, sys

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IDS = os.path.join(HERE, "marvel_ids.json")

API = "https://bifrost.marvel.com/catalog/comics/%s"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")


def out_dir(hero):
    return os.path.join(ROOT, "Art", "Tours", hero)


def fetch(hero, iid):
    from PIL import Image
    ids = json.load(open(IDS, encoding="utf-8"))
    if iid not in ids:
        return iid, "not linked -- no marvel id for this issue"
    cid = ids[iid].split("/", 1)[0]
    r = requests.get(API % cid, headers={"User-Agent": UA}, timeout=25)
    if r.status_code != 200:
        return iid, "catalog HTTP %d" % r.status_code
    d = (r.json() or {}).get("data") or {}
    url, ext = d.get("image_url"), d.get("image_extension") or "jpg"
    if not url:
        return iid, "no image on the catalog record"
    # /detail/ is the largest rendition marvel serves for these.
    img = requests.get("%s/clean.%s" % (url, ext),
                       headers={"User-Agent": UA}, timeout=40)
    if img.status_code != 200:
        img = requests.get("%s.%s" % (url, ext),
                           headers={"User-Agent": UA}, timeout=40)
    if img.status_code != 200:
        return iid, "image HTTP %d" % img.status_code

    im = Image.open(io.BytesIO(img.content)).convert("RGB")
    w, h = im.size
    if w > 700:
        im = im.resize((700, round(h * 700 / w)), Image.LANCZOS)
    os.makedirs(out_dir(hero), exist_ok=True)
    p = os.path.join(out_dir(hero), iid + ".jpg")
    im.save(p, "JPEG", quality=82, optimize=True, progressive=True)
    return iid, "%s  (%dx%d from %dx%d, %.0f KB)  %s" % (
        d.get("title", ""), im.size[0], im.size[1], w, h,
        os.path.getsize(p) / 1024.0,
        os.path.relpath(p, ROOT).replace(os.sep, "/"))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    hero, args = sys.argv[1], sys.argv[2:]
    if args[0] == "--list":
        d = out_dir(hero)
        if not os.path.isdir(d):
            print("nothing fetched for %s yet" % hero)
            return
        for f in sorted(os.listdir(d)):
            print("  %-22s %6.0f KB" % (f, os.path.getsize(os.path.join(d, f)) / 1024.0))
        return
    for iid in args:
        print("%-16s %s" % fetch(hero, iid))


if __name__ == "__main__":
    main()
