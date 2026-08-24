#!/usr/bin/env python3
"""Knock a flat studio background out of a poster and put a dark ground behind it.

Written for the Venom poster, which is an Alex Ross figure floating on a flat
pale-cyan field with Marvel's logo box in one corner and the artist's signature
in the other. All three fight the wall: the poster plate is a near-black band,
and a near-white page above it reads as a sticker rather than as art.

The interesting parts, because a naive version of each goes wrong:

* **The figure is found, not the background.** A colour-distance mask alone eats
  the white eye patches, the teeth and the chest spider, which are the same
  value as the field. So the mask is flood-filled inward from the border and
  then the FIGURE is taken as the largest connected component of its
  complement. Anything else -- the logo box, the signature, stray specks -- is
  an island in the background and is swallowed for free, with no rectangle to
  hand-place and nothing to re-tune if the art moves.

* **A hard swap leaves a bright halo.** Every antialiased edge pixel is a mix of
  figure and field, so against a dark ground the figure keeps a pale outline.
  `--bite` erodes the figure by a pixel or two before compositing, which spends
  a hair of the silhouette to buy a clean edge, and the mask is then blurred by
  `--feather` so the seam is not a staircase.

* **A flat fill reads as a cutout.** The default ground is a vertical ramp with
  a soft pool of light behind the figure's head -- an alley, not a void. `--flat`
  turns that off. Keep it darker than the subject's plate, or the band at the
  foot of the poster stops reading as the picture continuing.

    python3 tools/knockout.py venom "Art/covers/Venom.jpg"
    python3 tools/knockout.py venom "Art/covers/Venom.jpg" --flat --top 10,12,20

Writes through covers.save_cover, so the result is sized exactly like every
other poster on the wall. Needs Pillow, numpy and scipy.
"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import covers                                     # noqa: E402  (path first)
import fetch_hero_art                             # noqa: E402

# Cool, dim, and darker than any plate on the wall. The pair is (top, bottom).
TOP    = (13, 18, 32)
BOTTOM = (6, 8, 14)
GLOW   = (34, 44, 74)     # the pool of light the figure stands in front of


def rgb(s):
    p = [int(x) for x in s.split(",")]
    if len(p) != 3:
        sys.exit("expected r,g,b -- got %r" % s)
    return tuple(p)


def ground(w, h, top, bottom, glow, cx, cy, flat):
    """The replacement background: a vertical ramp, plus an optional soft pool
    of light centred on the figure so the plate does not read as a void."""
    ramp = np.linspace(0, 1, h)[:, None, None]
    g = np.array(top)[None, None, :] * (1 - ramp) + np.array(bottom)[None, None, :] * ramp
    g = np.repeat(g, w, axis=1)
    if not flat:
        yy, xx = np.mgrid[0:h, 0:w]
        r = np.sqrt(((xx - cx) / (w * .70)) ** 2 + ((yy - cy) / (h * .55)) ** 2)
        halo = np.clip(1 - r, 0, 1) ** 2
        g = g + (np.array(glow)[None, None, :] - g) * halo[:, :, None] * .85
    return g


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    hero_id, src = argv[0], argv[1]
    opt = argv[2:]

    def flag(name, default=None, cast=str):
        if name in opt:
            return cast(opt[opt.index(name) + 1])
        return default

    tol     = int(flag("--tol", 70))       # colour distance counted as background
    bite    = int(flag("--bite", 2))       # px of figure given up to kill the halo
    feather = float(flag("--feather", 1.2))
    flat    = "--flat" in opt
    top     = rgb(flag("--top", "%d,%d,%d" % TOP))
    bottom  = rgb(flag("--bottom", "%d,%d,%d" % BOTTOM))
    glow    = rgb(flag("--glow", "%d,%d,%d" % GLOW))
    out     = flag("--out")

    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    h, w, _ = a.shape

    # The field colour is the MODE of the border, not the median of the four
    # corners: on this poster the figure runs off the bottom edge, so two of the
    # corners are Venom and the median of the four is a colour that appears
    # nowhere -- which reported the figure as 97% of the frame.
    border = np.concatenate([a[0, :], a[-1, :], a[:, 0], a[:, -1]])
    q = (border // 8).astype(np.int32)
    key = q[:, 0] * 4096 + q[:, 1] * 64 + q[:, 2]
    vals, counts = np.unique(key, return_counts=True)
    field = np.median(border[key == vals[int(np.argmax(counts))]], axis=0)
    near = np.abs(a - field[None, None, :]).sum(2) < tol

    # Background = the part of `near` reachable from the border. Flood inward by
    # labelling and keeping every component that touches an edge, which is the
    # same thing without a recursive fill.
    lab, n = ndimage.label(near)
    edge = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
    edge.discard(0)
    if not edge:
        sys.exit("no background found at the border -- is --tol too tight?")
    bg = np.isin(lab, list(edge))

    # The figure is the biggest island in what is left. Everything else -- the
    # logo box, the signature -- is background by definition.
    lab2, n2 = ndimage.label(~bg)
    if n2 == 0:
        sys.exit("nothing left after the background -- is --tol too loose?")
    sizes = ndimage.sum(np.ones_like(lab2), lab2, range(1, n2 + 1))
    fig = lab2 == (int(np.argmax(sizes)) + 1)
    kept = fig.sum()

    if bite:
        fig = ndimage.binary_erosion(fig, iterations=bite)

    m = Image.fromarray((fig * 255).astype(np.uint8))
    if feather:
        m = m.filter(ImageFilter.GaussianBlur(feather))
    alpha = np.asarray(m).astype(np.float32)[:, :, None] / 255.0

    ys, xs = np.nonzero(fig)
    cx, cy = (xs.mean(), ys.mean()) if len(xs) else (w / 2, h / 2)
    g = ground(w, h, top, bottom, glow, cx, cy * .72, flat)

    res = a * alpha + g * (1 - alpha)
    res = Image.fromarray(np.clip(res, 0, 255).astype(np.uint8))

    print("field %s  figure %.1f%% of frame  islands removed %d"
          % (tuple(int(x) for x in field), 100.0 * kept / (w * h), n2 - 1))
    if out:
        res.save(out, quality=94)
        print("wrote", out, res.size)
    else:
        # Same 700px/q82 pipeline every poster on the wall goes through, aimed
        # at Art/Heroes/ rather than at a shelf's art directory.
        covers.ART = fetch_hero_art.ART
        rel, size = covers.save_cover(res, hero_id)
        print("wrote %s  (%dx%d)" % (rel, size[0], size[1]))


if __name__ == "__main__":
    main(sys.argv[1:])
