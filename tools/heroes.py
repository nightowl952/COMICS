#!/usr/bin/env python3
"""The hero registry -- one entry per subject that has an omnibus-shelf tracker.

Everything hero-specific that the tools need lives here, so build_omnibus_data,
covers and fetch_covers can all be pointed at a different shelf with --hero
instead of being edited. Adding a hero means adding an entry here and a metadata
module beside it; see "Adding an omnibus hero" in CLAUDE.md.

`meta` names a module in tools/ that defines ORDER, PLACEHOLDERS and SHELF (and
optionally PLACEHOLDER_PAGES and SERIES_EXTRA) -- the hand-written half of that
hero's shelf. `ids` names the harvested marvel.com id store that becomes the
tracker's MARVEL map.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

HEROES = {
    "spider-man": dict(
        name    = "Spider-Man",
        tracker = "spiderman-reading-tracker.html",
        art     = os.path.join("Art", "Spider-Man"),
        meta    = "omnibus_meta",
        raw     = "omnibus_contents_raw.json",
        ids     = "marvel_ids.json",
        # the panel key + id prefix build_single_file.py scopes this page under
        panel   = "spidey",
        pfx     = "sm",
        route   = "/spider-man",
    ),
}

DEFAULT = "spider-man"


def resolve(key=None):
    """Return one hero's config with every path made absolute."""
    key = key or DEFAULT
    if key not in HEROES:
        sys.exit("unknown hero %r\nknown: %s" % (key, ", ".join(sorted(HEROES))))
    h = dict(HEROES[key], key=key)
    h["tracker_path"] = os.path.join(ROOT, h["tracker"])
    h["art_path"]     = os.path.join(ROOT, h["art"])
    h["raw_path"]     = os.path.join(HERE, h["raw"])
    h["ids_path"]     = os.path.join(HERE, h["ids"])
    return h


def meta_module(h):
    sys.path.insert(0, HERE)
    return __import__(h["meta"])


def arg(argv):
    """Pull --hero <key> (or --hero=<key>) out of argv; returns (key, rest)."""
    rest, key = [], None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--hero" and i + 1 < len(argv):
            key = argv[i + 1]; i += 2; continue
        if a.startswith("--hero="):
            key = a.split("=", 1)[1]; i += 1; continue
        rest.append(a); i += 1
    return key, rest


if __name__ == "__main__":
    for k in sorted(HEROES):
        h = resolve(k)
        print("%-12s %-34s %s" % (k, h["tracker"], h["art"]))
