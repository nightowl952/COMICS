#!/usr/bin/env python3
"""Write a hero's guided tour into its tracker as the TOUR object.

Same shape as build_omnibus_data.py and for the same reason: the page is a
build product, the editable source is a module. Tour prose is long enough that
hand-editing it inside an HTML file would be miserable and would make every
change an unreviewable diff.

    python3 tools/build_tours.py --hero hulk
    python3 tools/build_tours.py --hero hulk --check     # exit 1 if stale
    python3 tools/build_tours.py --all

A hero with no module in tools/tours/ is skipped, not an error -- the tracker
keeps its empty TOUR and hides the button, which is the intended state for a
subject whose history has not been researched yet.
"""
import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MARK = "const TOUR = "

sys.path.insert(0, HERE)
import heroes                                                    # noqa: E402

# The X-Men page is deliberately outside heroes.py (no wiki page exists for a
# book that was never printed), but it is still a shelf with a tour, so it is
# named here rather than being silently unreachable.
EXTRA = {"xmen": {"key": "xmen", "tracker": "xmen-reading-tracker.html",
                  "art_dir": "Art/X-Men"}}


def registry():
    r = {k: dict(v, key=k) for k, v in heroes.HEROES.items()}
    r.update(EXTRA)
    return r


def module_for(key):
    try:
        return importlib.import_module("tours." + key.replace("-", "_"))
    except ImportError:
        return None


def check_refs(key, tour, tracker_html):
    """Every shelf chip must name a real volume, and every figure a real file.

    Both failures are silent in the browser -- a chip for a missing id renders
    as nothing, and a missing image hides its own figure via the onerror hook.
    Silent is the problem: a tour that quietly drops half its pictures still
    looks finished.
    """
    i = tracker_html.index("const OMNI = [")
    body = tracker_html[i + len("const OMNI = "):tracker_html.index("\n];", i) + 2]
    ids = set(re.findall(r'"?id"?\s*:\s*"([\w-]+)"', body.split('"chapters"')[0])
              ) | set(re.findall(r'\bid:\s*"([\w-]+)"', body))
    # cheap and exact: pull every top-level volume id the shelf actually renders
    vol_ids = set(re.findall(r'[{,]\s*"?id"?\s*:\s*"([\w-]+)"', body))

    bad_vols, bad_figs = set(), set()

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ("shelf", "vols"):
                    for vid in v:
                        if vid not in vol_ids:
                            bad_vols.add(vid)
                elif k == "fig":
                    for s in v.get("src", []):
                        if not os.path.exists(os.path.join(ROOT, s)):
                            bad_figs.add(s)
                    walk(v)
                else:
                    walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(tour)
    if bad_vols:
        sys.exit("[%s] tour points at volume(s) not on the shelf: %s"
                 % (key, ", ".join(sorted(bad_vols))))
    if bad_figs:
        sys.exit("[%s] tour figure(s) missing from disk: %s"
                 % (key, "\n    ".join(sorted(bad_figs))))
    _ = ids


def render(tour):
    return MARK + json.dumps(tour, indent=1, ensure_ascii=False, sort_keys=False) + ";"


def splice(html, tour):
    s = html.index(MARK)
    e = html.index("};", s) + 2
    return html[:s] + render(tour) + html[e:]


def count(tour):
    v = tour.get("volumes") or {}
    words = len(re.findall(r"[A-Za-z']+", json.dumps(tour, ensure_ascii=False)))
    return len(v), words


def one(h, check):
    key = h["key"]
    mod = module_for(key)
    if mod is None:
        print("[%-15s] no tours/%s.py -- skipped" % (key, key.replace("-", "_")))
        return 0
    tracker = os.path.join(ROOT, h["tracker"])
    html = open(tracker, encoding="utf-8").read()
    if MARK not in html:
        sys.exit("[%s] %s has no TOUR marker -- install the panel first" % (key, h["tracker"]))

    tour = mod.TOUR
    check_refs(key, tour, html)
    new = splice(html, tour)
    nv, words = count(tour)
    covered = len(tour.get("volumes") or {})
    total = len(re.findall(r'[{,]\s*"?id"?\s*:\s*"[\w-]+"',
                           html[html.index("const OMNI = ["):html.index("\n];", html.index("const OMNI = ["))]
                           .split('"chapters"')[0]))
    print("[%-15s] %d volume tours, ~%d words%s"
          % (key, nv, words, "" if not tour.get("overview") else ", plus the character tour"))
    _ = covered, total

    if check:
        ok = new == html
        print("            %s" % ("in sync" if ok else "OUT OF SYNC -- run without --check"))
        return 0 if ok else 1
    if new == html:
        print("            %s already up to date" % h["tracker"])
    else:
        open(tracker, "w", encoding="utf-8").write(new)
        print("            wrote %s" % h["tracker"])
    return 0


def main():
    argv = sys.argv[1:]
    check = "--check" in argv
    reg = registry()
    if "--all" in argv:
        keys = sorted(reg)
    else:
        try:
            keys = [argv[argv.index("--hero") + 1]]
        except (ValueError, IndexError):
            sys.exit(__doc__ + "\nknown heroes: " + ", ".join(sorted(reg)))
    rc = 0
    for k in keys:
        if k not in reg:
            sys.exit("unknown hero %r -- known: %s" % (k, ", ".join(sorted(reg))))
        rc |= one(reg[k], check)
    sys.exit(rc)


if __name__ == "__main__":
    main()
