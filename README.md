# C.O.M.I.C.S.

**C**aleb's **O**nline **M**arvel **I**ntractable **C**omic **S**helf — a set of
single-file web apps for tracking curated, chronological Marvel reads.

No build step for the pages, no dependencies, no server. Every page is
self-contained — data, styles, logic and artwork all inline — so any one of them
works opened straight off disk.

## What's here

| File | What it is |
|---|---|
| `index.html` | The homescreen. Poster wall of subjects, Continue Reading, per-subject dossiers. |
| `xmen-reading-tracker.html` | X-Men: the Messiah Saga. 174 issues, 27 arcs, 6 acts, in researched chronological order. |
| `spiderman-reading-tracker.html` | Spider-Man: an 18-volume omnibus shelf, each volume opening into what the printed book actually collects. |
| `comics-mobile.html` | Generated. All three pages composed into one hash-routed file for publishing. **Do not hand-edit.** |
| `tools/` | The generators and the marvel.com ID harvester. |
| `CLAUDE.md` | The full working notes — architecture, data provenance, every constraint already learned the hard way. Read this before changing anything. |

## Running it

Open `index.html` in a browser. That's it.

For anything involving navigation or saved progress, serve it over HTTP instead —
some preview tools render `file://` pages as `data:` URLs, where `localStorage`
throws and relative links don't resolve:

```bash
python3 -m http.server
```

## Changing a page

```bash
python3 tools/build_single_file.py
```

Run that after editing any of the three source pages, and commit the regenerated
`comics-mobile.html` alongside them — the published copies don't run a build.

## Progress

Progress is stored per-browser in `localStorage`, never in the HTML. Copying a
file to another machine does not carry your progress with it; each published
surface (Pages, the Claude artifact, a local copy) keeps its own. Use the
Back up / restore JSON buttons to move between them.

Automatic cross-device sync is not built yet — see the sync notes in
`CLAUDE.md`.
