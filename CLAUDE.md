# C.O.M.I.C.S. — Caleb’s Online Marvel Intractable Comic Shelf

A small constellation of single-file web apps for tracking curated, chronological
comic reads. Built in Claude sessions; this file exists so a fresh Claude Code
session can pick it up cold.

The project was called **Cerebro** until Aug 2026. The name survives in three
places on purpose: the in-world X-Men summaries (Beast installing Cerebro is
plot, not branding), and `OLD_RECORD_KEY` in `index.html`, which still reads
pre-rename homescreen records. Everything else is C.O.M.I.C.S.

**GitHub is the source of truth**: <https://github.com/nightowl952/COMICS>.
Iterate through the repo, not through loose local copies — see "Working on
this" at the bottom.

`index.html` is the homescreen — a streaming-style poster wall of "subjects"
(heroes). Each subject that has a curated reading list gets its own self-contained
tracker file, which the homescreen links into.

## Files

- `index.html` — the C.O.M.I.C.S. homescreen. Poster grid, Continue Reading panel,
  per-subject dossier modal, filters.
- `comics-mobile.html` — **generated, do not hand-edit.** All three pages
  composed into one hash-routed file for publishing as a Claude Artifact
  (artifacts are one file per URL). Rebuild with
  `python3 tools/build_single_file.py` after changing any source page.
- `xmen-reading-tracker.html` — the X-Men Messiah Saga protocol. A single curated
  chronological read, grouped into acts → chapters → issues.
- `spiderman-reading-tracker.html` — the Spider-Man omnibus shelf. A different
  shape: a shelf of omnibus volumes, each opening into its own reading list.

No build step, no package.json, no dependencies, no server. Open either file
directly in a browser.

Every file is individually self-contained (data, styles, logic, artwork) on
purpose. Keep it that way — portability is the point. The only thing that crosses
a file boundary is the small storage record described under "Homescreen" below.

## Two tracker shapes

There are two ways a hero's tracker can be organised. Pick per hero:

- **Curated chronology** (X-Men) — one researched reading order through a single
  saga. Acts → chapters → issues, all on one page.
- **Omnibus shelf** (Spider-Man) — a poster shelf of omnibus volumes, each
  reproducing exactly what the printed book collects, in print order. Two views
  in one file, hash-routed (`#/omni/<id>`).

The omnibus shape is what to copy when the goal is "read the collections as
published" rather than "read this story in the right order".

## Adding a hero

1. Curate the reading list and build `<hero>-reading-tracker.html`, modelled on
   whichever of the two shapes fits.
2. In `index.html`, flip that hero's `HEROES` entry: set `file` to the new
   filename and `total` to its issue count. That alone makes the poster live.
3. In the new tracker, add a `.topnav` back link and a `publishIndex()` call at
   the end of `refresh()` (copy both from the X-Men file, changing the storage
   key to `comics-hero-<id>`).

Steps 1 and 2 are independent — a hero can sit on the shelf as "Curating"
indefinitely with no tracker file, and nothing breaks.

## Homescreen (`index.html`)

The `HEROES` array is the whole configuration. Each entry:
`{id, name, art, tex, emblem, era, file, total, desc, light?}`.
- `file: null` → poster renders dimmed with a "Curating" badge, and clicking it
  opens the dossier modal instead of navigating.
- `file: "…"` → poster gets a gold "Ready" badge, a progress bar, and clicking it
  navigates straight to the tracker. The small "i" button opens the dossier.

### Artwork

All CSS and inline SVG — no image files, so the page stays portable. Three
layers per poster: an `.a-*` colour ramp, a `.tex-*` pattern (web / claw marks /
impact burst / crosshatch / starfield / moonlight / radar rings), and an `EMBLEMS`
inline SVG. `.wide` variants of each ramp re-aim the gradient for the short, wide
modal banner, which would otherwise bottom out to black in its first 40px.

Two non-obvious constraints, both already bitten once:
- `emblemSVG()` mints a **fresh gradient id per call**. Reusing one id makes every
  later copy of an emblem inherit the first one's fill.
- `.art` / `.tex` / `.gloss` / `.vig` are **not** scoped under `.poster`. The same
  markup is reused by the Continue thumbnail and the modal banner; scoping them
  collapsed both to zero height.

Moon Knight sets `light:true`, which swaps the gold emblem ramp for an ink one —
gold on a near-white poster is invisible.

### How the homescreen knows your progress

Trackers publish a summary record on every `refresh()`:

    comics-hero-<id> → {total, read, skip, next:{t, arc, ch}}

The homescreen reads those records; it never carries a copy of any tracker's data.
If no record exists yet (that tracker has never been opened since this feature
landed), it falls back to reading the tracker's own progress key directly — see
`LEGACY` in `index.html` — and failing that, to the hardcoded `total`.

Because the record is only a cache of the tracker's own state, deleting it is
always safe.

## The Spider-Man tracker (omnibus shelf)

18 omnibus volumes on the shelf: **12 with contents** (459 issue slots, 456 unique
issues) and **6 placeholders** that render as a tile but carry no issue list.

The shelf is a curated selection, not "every omnibus" — see "Scope call" below.
Display order is `SHELF` in `tools/omnibus_meta.py`; it is a reading order, not
publication order.

### Placeholder volumes

A placeholder is an entry with `placeholder:true` and `chapters:[]`. Note the
badge wording predates scraped covers: a placeholder can now carry a real cover
and full edition metadata and still be a placeholder, because what is pending is
its *issue list*, not its art. Rename the badge if that gets confusing. It uses the
`.o-placeholder` ramp, shows a "Cover pending" badge and "not added yet" in place
of the progress figures, and its detail page shows an empty-state note instead of
a chapter list.

Three code paths know about them, and all three are load-bearing:
- `showOmni()` guards `o.chapters[0]` — without the guard, opening a placeholder
  throws and the page dies. **This is the one that bites.**
- `buildOmni()` returns early and hides `#viewOmni .controls` (Mark whole omnibus
  read / Expand all are meaningless with no chapters).
- `buildShelf()` branches on `o.placeholder` before the `released==="Announced"`
  check.

`omniStats()`, `upNext()`, `refresh()` and `flat` already tolerate zero issues —
no changes were needed there.

To promote a placeholder to a real volume: add its wiki page to
`omnibus_contents_raw.json`, move its entry from `PLACEHOLDERS` to `ORDER` in
`tools/omnibus_meta.py` (dropping `placeholder`/`chapters` and giving it a real
`art`/`tex`/`released`), and regenerate.

### Where the contents came from

**Not** hand-typed, and not from a collecting blog. Each volume's issue list is
pulled from the Marvel Database wiki's structured `ReprintOf<N>` fields via its
MediaWiki API:

```bash
curl -s -A "$UA" -G "https://marvel.fandom.com/api.php" \
  --data-urlencode "action=parse" --data-urlencode "page=Amazing Spider-Man Omnibus Vol 1 1" \
  --data-urlencode "prop=wikitext" --data-urlencode "format=json"
```

Those fields are one row per *story*, in printed order — so the generator dedupes
globally (keeping first occurrence) and the surviving order **is** the book's
reading order. Prose "Collects…" blurbs from retail sites disagree with each
other and with the books; the ReprintOf fields did not. Prefer them.

Enumerate candidate pages with `list=allpages&apprefix=...`, filtering for
`Omnibus` in the title.

### Chaptering — two strategies, chosen automatically

The generator computes runs of consecutive same-series issues and looks at the
average run length:

- **avg ≥ 3.5 → chapter per series run** (9 of the 12 volumes with contents). E.g.
  "Amazing Spider-Man #1–38", "Amazing Spider-Man Annual #1–2".
- **avg < 3.5 → interleaved crossover** (Clone Saga Vol. 1–2, Ben Reilly Vol. 1).
  These books print Web → Amazing → Spider-Man →
  Spectacular month by month, so a per-series chapter would be one issue long.
  They chunk into blocks of 6 labelled "Part N" with the span as the subtitle.

The Part N labels are honest but generic. Real arc names (Power and
Responsibility, The Exile Returns, Maximum Clonage…) would be a genuine
improvement and are the obvious next curation pass.

### Issue ids are shared on purpose

An issue collected in two omnibuses gets the **same** id in both, so marking
ASM #324 read in the Michelinie & Larsen volume also marks it read in the
Michelinie & McFarlane volume. On the current shelf 3 issues overlap this way
(ASM #324, #327, #329); the UI flags them with a gold pill reading "in N
omnibuses". This is deliberate — do not de-duplicate ids per volume.

Consequence: `flat.length` (459, issue *slots*) and `uniqIds.size` (456, distinct
issues) are different numbers. Progress math uses `uniqIds`; the shelf label uses
slots. The overlap count was much higher (46) before the shelf was trimmed —
it scales with how many overlapping volumes are on the shelf.

### Covers and edition metadata

Covers are **scraped once and baked in**, never linked. `Art/covers/<id>.<ext>`
is the source of truth; `build_omnibus_data.py` base64-encodes each one into
`OMNI` as a `data:` URI. Nothing is fetched at page load — the trackers are
offline-only by design, and the Artifact CSP blocks remote images outright, so a
linked cover would render as a hole rather than a picture.

    python3 tools/scrape_covers.py        # the only step needing network
    python3 tools/build_omnibus_data.py   # bakes covers + metadata into OMNI
    python3 tools/build_single_file.py    # rebuilds comics-mobile.html

A volume with no cover file renders the CSS ramp exactly as before — `artHTML()`
draws the image *over* the ramp rather than instead of it, so a missing or
undecodable cover degrades instead of blanking. Saving a cover to
`Art/covers/<id>.jpg` by hand works identically to scraping one.

Each volume also carries an optional `edition` object (format, pages, released,
isbn, price, coverArtist, editor, publisher) rendered as a grid on the detail
view, plus an optional `marvel` collection id that renders a "View collection"
link. Every field is optional; the panel hides itself when empty.

`tools/omnibus_editions.json` is currently **seeded from retail listings**, not
the wiki — the Claude Code web environment cannot reach marvel.fandom.com, so a
first pass was gathered by web search. Each entry carries `printing` and
`source` provenance keys, which are build-time only and never reach the page.
Treat every `isbn`/`pages` value there as provisional: running
`scrape_covers.py` overwrites them from the Marvel Database wiki, keeps the
`marvel` link, and rewrites `source` to name the wiki page it used.

13 of the 18 volumes have a `marvel` collection id. The convention matches the
issue-level links — only the numeric id matters, the slug is decorative.

Budget: each committed kilobyte costs ~1.37 KB in **both**
`spiderman-reading-tracker.html` and `comics-mobile.html`. 18 covers at 45 KB
took the mobile build from 266 KB to 1.35 MB — fine against the 16 MB artifact
limit, but not free. 400px wide is the scraper default and is plenty.

Where the art and metadata come from, and why Marvel's own API is not an option,
is written up in `COVERS-AND-METADATA.md`.

### Marvel deep links

374 of 456 unique issues (82%) resolve to a real marvel.com issue page. The rest
fall back to a `marvel.com/search?query=` URL and render a grey Read button —
same convention as the X-Men tracker.

`MARVEL` still carries all 1118 harvested ids, 744 of which no longer match any
issue on the shelf. That is intentional: unused keys cost nothing, and keeping
them means re-adding a trimmed volume does not require re-running the harvester
against a rate-limited marvel.com.

Unresolved categories: Amazing Spider-Man Annuals (17), Spider-Man Unlimited (10),
Sensational Spider-Man #2–11 (10), Web of Spider-Man Annuals (7), Spectacular
Annuals (7), Venom: Lethal Protector (6), Spider-Man Team-Up (5), Amazing Fantasy
#15–18 (4), Marvel Team-Up #1/#3/#4 (4), and assorted Clone Saga one-shots.

**The harvesting runbook still works, but marvel.com is much more aggressive
about rate limiting than it was.** `-P 20` over ~500 ids succeeded once and then
403'd everything for several minutes; `-P 5` with 2s pauses also tripped it. What
does work is `tools/harvest.py` — small batches, 3 workers, and **403
detection that backs off and retries the same batch** instead of burning through
the range while blocked. Without that, a long run silently returns nothing.

Also note: ID blocks are contiguous per series, so a **scan** beats a walk badly.
One sweep of 6440–6960 returned all 441 Amazing Spider-Man issues with no gaps.
Known block seeds: ASM (1963) ≈ 6482–6900, Spectacular (1976) ≈ 14542–14800,
Web of Spider-Man (1985) ≈ 11973–12100, Spider-Man (1990) ≈ 10767–10870,
Marvel Team-Up (1972) ≈ 19619–19690, Clone Saga minis + Sensational ≈ 61238–61260.
Annuals live in a different, still-unlocated block (Web of Spider-Man Annual #1
is 80439, but 80330–80620 did not contain the ASM annuals).

### Tooling (`tools/`)

- `harvest.py` — the rate-limit-aware marvel.com ID harvester.
  `python3 tools/harvest.py 6440:6960:asm 14500:14820:spectacular` probes those
  id ranges and appends to `tools/marvel_ids.json`. Resumable: already-probed ids
  are skipped, so rerunning after a block costs nothing.
- `omnibus_contents_raw.json` — the raw ReprintOf lists pulled from the Marvel
  Database, one entry per omnibus. Regenerate only if a volume's contents change.
- `omnibus_meta.py` — the hand-written half: `ORDER` (wiki-backed volumes; each
  key must exist in `omnibus_contents_raw.json` or `gen()` KeyErrors),
  `PLACEHOLDERS` (shelf tiles with no contents, each with a `wiki` page title
  for the scraper — a placeholder has no issue list but is still a printed book
  with a cover), and `SHELF` (display order by id). This is where a new omnibus
  gets added. `wiki` is stripped at build time and never reaches the browser.
- `scrape_covers.py` — the one-time cover + edition-metadata scraper (Marvel
  Database wiki, Open Library fallback). Caches every response under
  `tools/scrape_cache/` so a parsing bug costs a `--reparse`, not another pass
  over a rate-limited API. Resumable: already-done volumes are skipped.
- `omnibus_editions.json` — scraped per-volume edition metadata, consumed as the
  `edition` object on each `OMNI` entry.
- `build_omnibus_data.py` — turns the above into the `OMNI` structure (dedupe,
  chaptering strategy, span labels, cover inlining, edition merge) and **writes
  it into `spiderman-reading-tracker.html`** between the `BEGIN/END GENERATED
  OMNI` markers. Run it directly: `python3 tools/build_omnibus_data.py`. It is
  idempotent — regenerating without new covers is a no-op.
- `marvel_ids.json` — id → marvel.com path fragment, consumed as `MARVEL`.
- `build_single_file.py` — composes the three pages into `comics-mobile.html`
  for artifact publishing. See "The mobile build" below.

### Scope call

The shelf was originally built inclusively — all 25 omnibuses covering Amazing
Fantasy #15 through Revelations, companion ongoings and overlapping creator-run
collections included. It has since been **trimmed to an 18-volume curated
shelf**, listed in `SHELF` in `tools/omnibus_meta.py`.

Dropped: Marvel Team-Up Vol. 1–2, Spectacular Vol. 1, Amazing Vol. 5–8, Web of
Spider-Man Vol. 1–2, Michelinie & Bagley Vol. 1–2, DeMatteis & Buscema, and Ben
Reilly Vol. 2. Removing the companion ongoings is what dropped the overlap count
from 46 shared issues to 3.

Added as placeholders (no contents yet): Spider-Man vs. Venom, Venomnibus Vol. 1
and 2, ASM by J. Michael Straczynski, Ultimate Spider-Man, and Death of Ultimate
Spider-Man. These push the shelf past the Clone Saga, so the era label is now
1962–2011 rather than 1962–1997.

**`tools/omnibus_contents_raw.json` was filtered to match** and no longer holds
the raw wiki contents for the 13 dropped volumes. Nothing on the shelf depends on
them, but re-adding a dropped volume means re-pulling its page with the MediaWiki
call under "Where the contents came from". `marvel_ids.json` and the `MARVEL` map
were *not* trimmed, so the deep links come back for free.

## The X-Men tracker

### What it does

Tracks 174 comic issues across 27 story arcs, grouped into 6 acts, in a
researched chronological reading order (not publication order). Per issue you
can: mark read, mark skipped, open it on Marvel, or pull a spoiler summary.

### Architecture

All inside the single `<script>` block, in this order:

1. `SC` — series → cover gradient colors
2. `seq()` — helper that generates runs of consecutive issues
3. `ACTS` — **the master data structure.** Array of 6 acts → `chapters` →
   `issues`. Each chapter has `{id, title, era, tier, note, issues[]}`.
   Each issue has `{id, t (title), s (series), arc, key?}`.
   `tier` 1 = core saga, 2 = main X-line, 3 = optional (hidden by the
   "Hide optional arcs" toggle via `body.hideopt`).
4. `MARVEL` — map of internal issue id → `marvelID/slug` path fragment
5. `ARC_SUMS` — 27 hand-written, pre-loaded spoiler digests keyed by chapter id
6. Storage layer, render, interaction, summaries, refresh

`flat[]` is the flattened `{act, ch, issue}` list driving "Up Next" and all
progress math.

#### Storage (dual-mode)

`IN_CLAUDE` detects whether `window.storage` exists.
- Inside Claude → `window.storage`
- In a normal browser → `localStorage`

The `store` object abstracts both. Keys:
- `xmen-saga-progress-v2` → `{read:[ids], skip:[ids]}`
- `xmen-saga-summaries-v3` → cached generated summaries
- `xmen-anthropic-key` → user's own API key (browser mode only)
- `comics-hero-xmen` → summary record written for the homescreen (derived, not
  a source of truth — see "Homescreen" above)

**Bumping a key version wipes that data.** That's the intended mechanism for
invalidating bad cached summaries — it's been used once already (v2 → v3).

Export/import to JSON exists (`exportProgress` / `importProgress`) because
localStorage is fragile. Progress does NOT live in the HTML file — copying the
file to a new machine does not carry progress.

#### Summaries — two tiers

- **Arc digests**: pre-written in `ARC_SUMS`. Instant, offline, no key. Every
  chapter has one. This is the reliable tier.
- **Per-issue**: live call to `api.anthropic.com` (`claude-sonnet-4-6`) with the
  `web_search_20250305` tool enabled. In-browser it needs the user's own key via
  `x-api-key` + `anthropic-dangerous-direct-browser-access: true`.

`tidy()` sanitizes model output — strips markdown, leading process narration
("I found…", "Let me…"), bullets, trailing source lists, and collapses to at
most two paragraphs. **Don't remove it**; prompt instructions alone did not
reliably suppress that formatting.

`summaryError()` maps error codes (`nokey`, `badkey`, `http`) to useful messages.

### Design

Frutiger Aero / early-2000s: sky-blue gradients, glass panels, glossy orbs,
floating bubbles, italic uppercase display type, X-Men gold accents. CSS
variables at `:root`. Progress bars stack green (read) + grey (skipped).
Respects `prefers-reduced-motion`. Mobile breakpoint at 600px.

### Known gaps / open items

1. **30 of 174 issues lack Marvel deep links.** They fall back to a
   `marvel.com/search?query=` URL and render as a grey "Read" button instead of
   gold. These are one-shots and minis (Messiah War prologue, Lucas Bishop,
   Necrosha one-shots, Hellbound, Blind Science, Second Coming #1–2, New
   Mutants, Sex and Violence, King-Size Cable). The 144 resolved IDs were
   obtained by crawling marvel.com; the one-shots were not in the probed ID
   ranges. Resolving them means finding each numeric Marvel issue ID.
   The full method — verified working — is written up in `MARVEL-IDS.md`.
2. **One disputed reading order.** X-Force #12–13 currently sits before the
   Messiah War crossover (publication order). Some guides argue Messiah War
   should be read first because X-Force returns from the future slightly earlier
   than they left. Flagged in that chapter's `note`.
3. **Per-issue summary quality varies** for obscure issues even with web search.
   Arc digests are the trustworthy layer.

### Reading order sources

Order was researched, not assumed. Primary sources: Crushing Krisis's X-Men
reading order guide (era covering Divided We Stand through Second Coming), which
gives explicit continuity-placement reasoning, and Comic Book Herald's Second
Coming chapter order. Verify against these before reordering anything.

Non-obvious placements that are deliberate, not mistakes:
- X-Men Legacy #208 opens the read (resolves Xavier's head wound), not Uncanny #495
- X-Factor #28 precedes X-Force #1 (Rahne has to leave X-Factor before joining X-Force)
- X-Force #1–6 precede Uncanny #495 (Wolverine/Archangel appearance constraints)
- Cable #6–12 sits after Uncanny #503 (contains present-day scenes that must
  precede X-Force #12)
- Necrosha lands after Nation X despite concurrent release (Magneto participates)

### Conventions

- Preserve existing internal issue ids (`unc-495`, `leg-208`, `xfo-14`,
  `cab-25`, `sc-1`…). **They are the storage keys.** Renaming one silently
  orphans that issue's saved progress.
- Adding issues: append to the right chapter's `issues[]`, and add a `MARVEL`
  entry if a real ID is known.
- Adding a chapter: it also needs an `ARC_SUMS[chapterId]` entry, or the arc
  button falls through to a live web lookup.

## The mobile build (`comics-mobile.html`)

`tools/build_single_file.py` composes the three pages into one. The sources are
never modified — everything below is done at build time.

Routes: `#/` home, `#/xmen`, `#/spider-man`, `#/spider-man/omni/<id>`.

### What the build has to solve

- **83 CSS class names collide** across the three files with *different* values
  (`.wrap` is 960px vs 1120px, `.x-emblem` is blue vs red, `.tex-web` differs).
  Each stylesheet is scoped under its own `#app-<key>` panel. `:root`, the
  reset, `body` and the bubbles are hoisted once. `body.hideopt` is special-cased
  so the X-Men "hide optional arcs" toggle still works.
- **18 DOM ids collide** (`statRead`, `upnext`, `shelf`, …). Every id is
  prefixed per app in both the markup and the JS that looks it up;
  `document.getElementById/querySelector(All)` are rewritten to prefix-aware
  helpers scoped to the panel.
- **Top-level JS names collide wholesale** (`SC`, `MARVEL`, `store`, `refresh`,
  `flat`, `esc`…). Each script is wrapped in an IIFE, so nothing leaks.

### Three artifact-environment constraints, each already handled

1. **No `<meta charset>`** — the Artifact wrapper owns `<head>`, so the page is
   emitted as **pure ASCII** (entities in HTML, `\uXXXX` in JS, `\XXXX ` in CSS).
   Without this, en-dashes and middots render as mojibake. The builder asserts
   zero non-ASCII bytes before writing.
2. **CSP blocks external requests** — the X-Men per-issue summaries call
   `api.anthropic.com` and cannot work. `getKey()` is stubbed to `""` so the
   existing "no key" path fires with a rewritten message pointing at the offline
   arc digests, and the now-useless API-key row is hidden. All 27 arc digests
   still work; they were always offline.
3. **`<a download>` is inert in the viewer** — so the Back up button would
   silently do nothing, which matters because export/import *is* the
   cross-device story. Both trackers' exports are rewired to
   `window.__COMICS_SAVE()`, which uses the `downloads` capability
   (`claude.use("downloads")` → `save({filename,data})`), falls back to the
   clipboard, and uses an ordinary blob link when running locally.
   The artifact must therefore be published with `capabilities: {downloads:true}`.

### Progress does not sync

`localStorage` is per-origin **and per-device**. The artifact, GitHub Pages and
the local `file://` copies each keep their own progress; nothing syncs between
phone and laptop. Export/import JSON is the manual bridge. Real sync would need
a server-side store and is not built.

## Open items — C.O.M.I.C.S.

1. **Five of seven subjects have no reading list yet** (Wolverine, Hulk,
   Fantastic Four, Moon Knight, Daredevil). Their `desc` text in `HEROES`
   sketches the intended shape of each list but nothing is researched or
   verified yet — treat it as a starting brief, not a plan.
2. **`total` for a new hero is a hardcoded fallback.** It is only used before
   that tracker has ever been opened; after that the published record wins. Keep
   them in sync anyway, or a first visit reports the wrong percentage.

## Testing

No test suite. Note that `file://` pages render as `data:` URLs in some preview
tools, where `localStorage` throws and relative links don't resolve — serve the
folder over HTTP (`python3 -m http.server`) to exercise navigation and progress
for real.

Verify changes with:

```bash
# JS syntax
node -e "const fs=require('fs');fs.writeFileSync('/tmp/v.js',
  fs.readFileSync('xmen-reading-tracker.html','utf8').split('<script>')[1].split('</script>')[0])"
node --check /tmp/v.js

# Data integrity (counts, duplicate ids, ARC_SUMS coverage) — see git history
# or re-derive: eval the data section and assert every chapter has a digest.
```

For behavior, `jsdom` with `runScripts:'dangerously'` and no `window.storage`
simulates plain-browser mode accurately — that's how the localStorage fallback
and the no-key summary path were verified.

## Working on this (GitHub is the source of truth)

The canonical copy lives on GitHub. Local clones are disposable; do not treat a
folder on one machine as the real project.

    git pull           # before touching anything
    …edit…
    python3 tools/build_omnibus_data.py   # if covers/contents/editions changed
    python3 tools/build_single_file.py    # if any page changed
    git add -A && git commit && git push

`comics-mobile.html` is generated but **is committed** — GitHub Pages and the
Claude Artifact both serve it, and neither runs a build step. A commit that
changes `index.html`, `xmen-reading-tracker.html` or
`spiderman-reading-tracker.html` without a matching rebuild ships a stale mobile
page. Rebuild in the same commit.

### Three published surfaces, three separate progress stores

| Surface | URL | Progress lives in |
|---|---|---|
| GitHub Pages | `https://nightowl952.github.io/COMICS/` | that origin's `localStorage` |
| Claude Artifact | the artifact link | artifact `window.storage` |
| Local `file://` | the clone | that browser's `localStorage` |

They do not sync — see "Progress does not sync". Export/import JSON is the
bridge. Publishing a new version of either surface does not disturb progress
already saved there, because progress is never in the HTML.

**Cross-device sync is wanted and not built.** Note the asymmetry before
designing it: the artifact runs under a CSP that blocks *all* external requests,
so no artifact-side code can ever reach a sync store. GitHub Pages has no such
restriction. So the two surfaces cannot share one mechanism — the realistic
shape is a store reachable from Pages (a private Gist keyed by a token the user
pastes in, mirroring the existing `xmen-anthropic-key` pattern), with the
artifact staying export/import-only. The artifact `artifact` capability is not
the answer: its live-doc arm only persists DOM inside a marked region, and both
trackers render their issue rows from JS data, which it does not save.

### Updating the artifact

The artifact is **https://claude.ai/code/artifact/a339fcf9-afeb-413c-880c-a4b1aa6b0f81**.

Republish `comics-mobile.html` **to that URL** (pass the existing
URL, don't create a second artifact) with `capabilities: {downloads: true}` —
without that capability the Back up button silently does nothing.
