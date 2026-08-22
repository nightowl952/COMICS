# C.O.M.I.C.S.

**C**aleb's **O**nline **M**arvel **I**ntractable **C**omic **S**helf — a set of
single-file web apps for tracking curated, chronological Marvel reads.

No build step for the pages, no dependencies, no server. Every page is
self-contained — data, styles, logic and artwork all inline — so any one of them
works opened straight off disk.

## What's here

| File | What it is |
|---|---|
| `index.html` | The homescreen. Banner, Keep Reading rail, poster wall of subjects, per-subject dossiers. |
| `xmen-reading-tracker.html` | X-Men: the Messiah Saga. 174 issues, 27 arcs, shelved as four omnibuses Marvel never printed. |
| `spiderman-reading-tracker.html` | Spider-Man: a 16-volume omnibus shelf, each volume opening into what the printed book actually collects. |
| `hulk-reading-tracker.html` | Hulk: 17 mainline Bruce Banner omnibuses, same shape. |
| `fantasticfour-reading-tracker.html` | Fantastic Four: 18 omnibuses, plus the Thing's solo book and Doctor Doom's. |
| `wolverine-reading-tracker.html` | Wolverine: 14 omnibuses of Logan's own books, including Uncanny X-Force. |
| `moonknight-reading-tracker.html` | Moon Knight: all 7 omnibuses Marvel has printed, same shape. |
| `daredevil-reading-tracker.html` | Daredevil: 17 omnibuses of Matt Murdock's own books. |
| `tools/` | The generators and the marvel.com ID harvester. |
| `CLAUDE.md` | The full working notes — architecture, data provenance, every constraint already learned the hard way. Read this before changing anything. |

## The shape of a page

Dark blue-black, laid out like a streaming service: a wide banner at the top,
then a **Keep Reading** rail of one wide tile per volume you have open, then the
shelf. Click a tile to land back where you were. There are no completion
percentages anywhere — the tiles carry a position, not a score.

Banner art lives in `Art/Banners/` and is dropped in by hand:

```bash
python3 tools/banners.py add-folder ~/Desktop   # match a folder by filename
python3 tools/banners.py add spider-man ~/Desktop/spidey.jpg
python3 tools/banners.py audit
```

A missing banner is not a broken page — each subject falls back to its poster
scan, and the homescreen to all seven of them in a row.

## Where it lives

- **Live:** <https://nightowl952.github.io/COMICS/>

Every page is responsive and reads fine on a phone straight from there. There
used to be two other surfaces and both are retired: a Claude Artifact, and
`comics-mobile.html`, a generated single-file build of the whole site that
existed to fit the Artifact's one-file-per-URL rule. Both went in August 2026.

A local copy keeps its own reading progress, separate from the live site — see
"Progress" below.

## Running it

Open `index.html` in a browser. That's it.

For anything involving navigation or saved progress, serve it over HTTP instead —
some preview tools render `file://` pages as `data:` URLs, where `localStorage`
throws and relative links don't resolve:

```bash
python3 -m http.server
```

## Changing a page

Edit it and commit — there is no build step, and GitHub Pages doesn't run one.

The exception is a shelf's data: the `OMNI` and `MARVEL` blocks in an omnibus
tracker are generated, so change `tools/<hero>_meta.py` and regenerate rather
than hand-editing the page:

```bash
python3 tools/build_omnibus_data.py --hero <key>
```

## Progress

Progress is stored per-browser in `localStorage`, never in the HTML. Copying a
file to another machine does not carry your progress with it; the live site and
a local copy each keep their own. Use the Back up / restore JSON buttons to move
between them.

Automatic cross-device sync is not built yet — see the sync notes in
`CLAUDE.md`.
