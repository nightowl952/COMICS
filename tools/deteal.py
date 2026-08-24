#!/usr/bin/env python3
"""Take the cool colour cast out of a poster's background.

Written for the Ghost Rider poster, whose background is a teal-green smoke
field behind an orange figure -- the user asked for that field to read black,
which the pitch-black plate under it already does.

    python3 tools/deteal.py ghost-rider "Art/covers/Ghost Rider.jpg"
    python3 tools/deteal.py ghost-rider "Art/covers/Ghost Rider.jpg" --dark 0.7

It writes Art/Heroes/<hero id>.jpg through covers.save_cover, exactly as
`fetch_hero_art.py adopt` does, so the result is sized like every other image
on the site.  **The source in Art/covers/ is left untouched** -- that folder is
the archive of originals -- which means `adopt` on the same file will put the
teal straight back.  Re-run this instead.

How it works, and why not the obvious way:

The first attempt classified a pixel by HUE, blanking anything in a teal band.
That fails badly where the smoke meets the flame: hue is unstable at low
saturation and wraps, so the band edge speckles, and a steep darkening curve
turns the speckle into a hard-edged black blob.  Rendered, it looks like a
tear in the picture.

What works is a continuous test with no branches in it.  The subject is warm
(fire, red chains, a brown jacket: R dominates) and the background is cool
(G and B meet or beat R), so

    w = clip((max(G,B) - R + 18) / 20)

is 0 on anything warm, 1 on anything cool, and slides smoothly between -- no
hue, no threshold, no wraparound.  Those pixels are then pulled to a neutral
grey at their own MIN channel, which is a true desaturation: it kills a teal
(G,B > R) and an olive (G > R > B) alike, where capping G and B at R leaves the
olive behind as a yellow tint.

Darkening is gated on brightness (`gate`) and that gate is load-bearing.  The
white-hot core of the flame is near-neutral, so `w` catches it too -- dimming it
punches grey holes through the fire.  Only genuinely dark pixels are dimmed.

Needs Pillow and numpy.
"""
import argparse, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

LO, HI  = -18.0, 2.0     # max(G,B)-R ramp: warm subject -> cool background
GATE    = (160.0, 60.0)  # dim only pixels whose brightest channel is below this
DARK    = 0.22           # what a fully cool, fully dark pixel is scaled to


def deteal(im, dark=DARK):
    import numpy as np
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    mn = np.minimum(np.minimum(r, g), b)
    mx = np.maximum(np.maximum(r, g), b)
    w    = np.clip((np.maximum(g, b) - r - LO) / (HI - LO), 0, 1)
    gate = np.clip((GATE[0] - mx) / GATE[1], 0, 1)
    grey = np.stack([mn * (1 - w * gate * (1 - dark))] * 3, 2)
    out  = a * (1 - w[:, :, None]) + grey * w[:, :, None]
    from PIL import Image
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("hero_id")
    p.add_argument("image")
    p.add_argument("--dark", type=float, default=DARK,
                   help="scale a fully cool dark pixel to this (default %.2f; "
                        "1.0 desaturates without dimming)" % DARK)
    p.add_argument("--out", help="write the full-size result here instead of "
                                 "normalising into Art/Heroes/")
    a = p.parse_args()
    try:
        from PIL import Image
        import numpy  # noqa: F401
    except ImportError:
        sys.exit("needs Pillow and numpy:  pip install Pillow numpy")
    if not os.path.exists(a.image):
        sys.exit("no such image: %s" % a.image)

    sys.path.insert(0, HERE)
    import fetch_hero_art, covers
    if a.hero_id not in fetch_hero_art.PICKS:
        sys.exit("unknown hero id %r\nknown: %s"
                 % (a.hero_id, ", ".join(fetch_hero_art.PICKS)))

    im = deteal(Image.open(a.image), a.dark)
    if a.out:
        im.save(a.out, quality=93)
        print("wrote %s  (%dx%d)" % (a.out, *im.size))
        return
    covers.ART = fetch_hero_art.ART
    rel, size = covers.save_cover(im, a.hero_id)
    print("wrote %s  (%dx%d, %.0f KB)"
          % (rel, size[0], size[1], os.path.getsize(os.path.join(ROOT, rel)) / 1024))
    print("Art/covers/ still holds the untouched original -- `adopt` on it "
          "would undo this.")


if __name__ == "__main__":
    main()
