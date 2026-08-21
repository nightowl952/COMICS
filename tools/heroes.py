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
    ),
    "hulk": dict(
        name    = "Hulk",
        tracker = "hulk-reading-tracker.html",
        art     = os.path.join("Art", "Hulk"),
        meta    = "hulk_meta",
        raw     = "hulk_contents_raw.json",
        # deliberately the same store as Spider-Man: the id map is keyed by
        # issue id, several series appear on both shelves, and a shared store
        # means an overlap resolves without being harvested twice.
        ids     = "marvel_ids.json",
    ),
    "wolverine": dict(
        name    = "Wolverine",
        tracker = "wolverine-reading-tracker.html",
        art     = os.path.join("Art", "Wolverine"),
        meta    = "wolverine_meta",
        raw     = "wolverine_contents_raw.json",
        # the same shared store again -- this shelf collects Incredible Hulk,
        # Marvel Comics Presents, Fantastic Four and Uncanny X-Men issues the
        # other three shelves already reach for.
        ids     = "marvel_ids.json",
    ),
    "moon-knight": dict(
        name    = "Moon Knight",
        tracker = "moonknight-reading-tracker.html",
        art     = os.path.join("Art", "Moon-Knight"),
        meta    = "moonknight_meta",
        raw     = "moonknight_contents_raw.json",
        # the same shared store again -- this shelf collects Amazing
        # Spider-Man, Web of Spider-Man, Marvel Team-Up, Marvel Two-In-One and
        # Marvel Comics Presents issues the other four shelves already reach
        # for, so an overlap resolves without being harvested twice.
        ids     = "marvel_ids.json",
    ),
    "daredevil": dict(
        name    = "Daredevil",
        tracker = "daredevil-reading-tracker.html",
        art     = os.path.join("Art", "Daredevil"),
        meta    = "daredevil_meta",
        raw     = "daredevil_contents_raw.json",
        # the same shared store again -- this shelf collects Amazing
        # Spider-Man, Spectacular Spider-Man, Marvel Comics Presents, Fantastic
        # Four, Iron Man and Avengers issues the other five shelves already
        # reach for, so an overlap resolves without being harvested twice.
        ids     = "marvel_ids.json",
    ),
    "fantastic-four": dict(
        name    = "Fantastic Four",
        tracker = "fantasticfour-reading-tracker.html",
        art     = os.path.join("Art", "Fantastic-Four"),
        meta    = "ff_meta",
        raw     = "ff_contents_raw.json",
        # the same shared store again -- the FF shelf collects Marvel Team-Up,
        # Strange Tales and Fantastic Four issues the other two shelves already
        # reach for, so an overlap resolves without being harvested twice.
        ids     = "marvel_ids.json",
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
