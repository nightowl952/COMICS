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

## Answering style

Keep replies short and plain. This is a hobby project, not a code review.

- Lead with what happened or what the answer is. No preamble.
- A few sentences beats a section with headings. Skip tables unless the data
  genuinely has columns.
- Don't narrate the steps taken, restate the request, or list what wasn't done.
- Say what broke and what you did about it, then stop.
- Long form is for when it was asked for, or when something genuinely went
  wrong and the detail is the point.

## Files

- `index.html` — the C.O.M.I.C.S. homescreen. Above-the-fold banner, Keep Reading
  rail, poster grid,
  per-subject dossier modal, filters.
- `xmen-reading-tracker.html` — the X-Men Messiah Saga protocol. Same omnibus
  shelf shape as the other six, but the four books on it were **never printed**
  — see "The X-Men tracker". Its `OMNI` array is hand-written in the page, not
  generated: there is no `tools/xmen_meta.py` and no wiki page to pull from.
- `spiderman-reading-tracker.html` — the Spider-Man omnibus shelf. A different
  shape: a shelf of omnibus volumes rendered as CSS-3D hardcover books, each
  opening into its own reading list. Its `OMNI` array is **generated** from
  `tools/omnibus_meta.py` — edit that and regenerate, don't hand-edit the array.
- `hulk-reading-tracker.html` — the Hulk omnibus shelf. Same shape and same
  tooling as the Spider-Man page (`--hero hulk`); 17 mainline Bruce Banner
  volumes. Its `OMNI` array is generated from `tools/hulk_meta.py`.
- `fantasticfour-reading-tracker.html` — the Fantastic Four omnibus shelf. Same
  shape and tooling again (`--hero fantastic-four`); 19 volumes, and the only
  shelf carrying books that are not the title character's own — the Thing's solo
  omnibus and Doctor Doom's. Its `OMNI` array is generated from
  `tools/ff_meta.py`.
- `wolverine-reading-tracker.html` — the Wolverine omnibus shelf. Same shape and
  tooling again (`--hero wolverine`); 14 volumes of Logan's own books. Its
  `OMNI` array is generated from `tools/wolverine_meta.py`.
- `moonknight-reading-tracker.html` — the Moon Knight omnibus shelf. Same shape
  and tooling again (`--hero moon-knight`); 7 volumes, which is *every* Moon
  Knight omnibus in print. Its `OMNI` array is generated from
  `tools/moonknight_meta.py`.
- `daredevil-reading-tracker.html` — the Daredevil omnibus shelf. Same shape
  and tooling again (`--hero daredevil`); 17 volumes covering 1964 to the end
  of Zdarsky's run. Its `OMNI` array is generated from `tools/daredevil_meta.py`.
- `Art/Spider-Man/`, `Art/Hulk/`, `Art/Fantastic-Four/`, `Art/Wolverine/`,
  `Art/Moon-Knight/`, `Art/Daredevil/`, `Art/X-Men/` — cover scans, committed so
  GitHub Pages can serve them. Every page references them by relative path.
  `Art/X-Men/` is the odd one: its four books were never printed, so each file is
  the cover of the issue that volume is named after — see "Cover art for books
  with no covers".
- `Art/Heroes/` — one cover per homescreen subject, seven files named by hero id.
  See "Artwork" below.
- `Art/Banners/` — the wide above-the-fold art, eight files: `index.jpg` for the
  homescreen and `<hero id>.jpg` for each subject's shelf. Hand-picked, never
  fetched; `tools/banners.py` normalises them. A missing one is not a broken
  page — see "The banner" below.
- `Art/covers/` — the original hand-supplied scans the seven `Art/Heroes/`
  files were derived from, at full size. Nothing reads this folder; it is kept
  so a poster can be re-cropped without re-sourcing the art.
- `Art/Logos/` — one printed logo per homescreen subject, `<hero id>.png`,
  cropped to its artwork and alpha-backed. See "The plate" below. The
  source-named originals the user supplied are not kept; git history has them.

No build step, no package.json, no dependencies, no server. Open any of these
files directly in a browser.

Every file is individually self-contained (data, styles, logic, artwork) on
purpose. Keep it that way — portability is the point. The only thing that crosses
a file boundary is the small storage record described under "Homescreen" below.

## One tracker shape, two ways of filling it

**All seven subjects are omnibus shelves** (Aug 2026): a shelf of volumes
rendered as CSS-3D hardcover books, each opening into its own chapter list. Two
views in one file, hash-routed (`#/omni/<id>`). What differs is where a shelf's
data comes from:

- **Wiki-backed** (Spider-Man, Hulk, Fantastic Four, Wolverine, Moon Knight,
  Daredevil) — each volume reproduces exactly what the printed book collects, in
  print order, pulled from the Marvel Database. `OMNI` is **generated** from a
  `tools/<hero>_meta.py`; the whole pipeline behind it is hero-agnostic — see
  "Adding an omnibus hero".
- **Hand-curated** (X-Men) — one researched chronological reading order, cut
  into four books that do not exist. `OMNI` is hand-written in the page, because
  there is no printed edition to pull. See "The X-Men tracker".

The X-Men page was a single flat six-act chronology until Aug 2026. Reshaping it
kept every chapter, note, tier and issue id exactly as it was, which is why
progress logged against the old page still reads correctly on the new one — the
volumes are a regrouping of the same 27 chapters, nothing more.

### A shelf holds books you can actually buy

**Never put an unreleased omnibus on a shelf.** If Marvel has solicited it but
not printed it, it does not go in `ORDER` or `SHELF` — no tile, no issue list,
no contribution to the hero's `total`. A shelf is a reading list, and an
announced book is not something anyone can read.

That is what the `released="Announced"` badge is for and why almost nothing
should use it: a book that ships between one session and the next, not a
standing category. Fantastic Four by Dan Slott Vol. 2 (solicited December 2026)
was on the shelf briefly and came off for exactly this reason.

The cheap way to re-add one when it ships: **leave its entry in the hero's
`<hero>_contents_raw.json`** when you drop it. The raw file is only read for
keys named in `ORDER`, so an unused entry costs nothing, and re-adding the
volume is then a meta-module edit plus a regenerate rather than a fresh wiki
pull.

The omnibus shape is what to copy when the goal is "read the collections as
published" rather than "read this story in the right order".

**The X-Men shelf breaks this rule on purpose, and it is the only one allowed
to.** All four of its volumes are mock-ups of books Marvel has never printed, so
the rule's whole premise — that a tile stands for something a reader can go and
buy — does not apply. What replaces it is saying so: a standing note in bold
directly above the shelf, "0 in print" in the shelf count, and "never printed"
where the other shelves show a release date.

An amber "Never printed" badge on every tile was the fourth signal and **came
off at the user's request** once the volumes had cover art — four identical
warning pills over four convincing book jackets read as nagging rather than as
information, and the tile badge went back to the issue count every other shelf
shows. The three remaining signals are the floor, not a starting point: the note
above the shelf in particular is the one that has to survive any future edit.

None of this is a licence to slip a solicited-but-unshipped book onto a real
shelf — that is still forbidden.

## Adding a hero

1. Curate the reading list and build `<hero>-reading-tracker.html`, modelled on
   whichever of the two shapes fits.
2. In `index.html`, flip that hero's `HEROES` entry: set `file` to the new
   filename and `total` to its issue count. That alone makes the poster live.
3. In the new tracker, add a `.topbar` back link and a `publishIndex()` call at
   the end of `refresh()` (copy both from the X-Men file, changing the storage
   key to `comics-hero-<id>`), and drop a banner in at `Art/Banners/<id>.jpg`.

Steps 1 and 2 are independent — a hero can sit on the shelf as "Curating"
indefinitely with no tracker file, and nothing breaks.

## The three levels, and what sits at the top of each (Aug 2026)

Every page is one of three levels, and they now share the same top:

| Level | Page | Banner shows | Keep Reading shows |
|---|---|---|---|
| 1 | `index.html` | `Art/Banners/index.jpg` + the C.O.M.I.C.S. wordmark | every volume open across all seven subjects |
| 2 | a tracker's shelf view | `Art/Banners/<hero>.jpg` + that subject's printed logo | every volume open on that shelf |
| 3 | a tracker's volume view | that volume's own cover | one tile — the next issue in the volume |

Three things went at once, and all three were the user's call:

- **The HUD bar is gone from every page.** It was the rounded panel carrying the
  page title, the emblem and a row of read / skipped / remaining / cleared
  figures. The title moved into the banner; the figures were not replaced,
  because of the rule below.
- **Completion is not reported anywhere.** No overall percentage, no per-volume
  `done/total`, no per-chapter `N / M` pill, no progress bar on a book tile or a
  chapter header. `.pbar` is deleted from every page. The reading is long enough
  that "8% cleared" is discouraging rather than informative, and the user does
  not read for completion. The one bar left on the site is on a Keep Reading
  tile, and it is a position marker for a single volume, not a score.
  **Do not reintroduce a completion figure** without being asked for one.
- **The Frutiger Aero sky is gone.** See "The dark chrome" below.

What is deliberately *kept* despite touching progress: the shelf's In progress /
Not started / Finished filter chips, the "Finished" badge on a cleared book, and
the read/skipped state on an issue row. Those are states, not scores.

### The banner

One full-bleed image at the top of every page, fading into the page background
at its foot. The fade only works because `--bg` is a **flat** colour — a
gradient body would show a seam where the banner stops. Keep it flat.

`.hb` breaks out of `.wrap` with `width:100vw; margin-left:calc(50% - 50vw)`,
which is exact for a centred max-width box with padding; `body{overflow-x:hidden}`
is what keeps the `100vw` from adding a scrollbar.

**There is no wash over the picture, and putting one back is the wrong instinct.**
The first version darkened the whole frame to buy text contrast and turned all
seven painted plates to mud — the user's word for it was "so dark". `.hb-scrim`
is now only the bottom third: `.94` at 8% up from the foot, clear by 48%, and
`var(--bg)` at 0% because the foot has to *be* the page colour. Everything above
45% of the banner is the untouched image. What buys legibility instead is the
type's own shadow (`.hb-sub` and `.hb-blurb` both carry a double drop-shadow,
and `.hb-logo` a 22px one) — so a brighter plate costs contrast on the copy, not
on the art.

**Where to crop is per-subject, and it is set on the `<img>` inline**, the same
convention as `pos` on a `HEROES` entry, and arrived at the same way — render it
and look. Two of the seven set one: Spider-Man at `72%` (Alex Ross's figure runs
48–90% down the plate, and the default band cut him off at the waist) and
Daredevil at `0%` (the cowl is hard against the top edge). The other five take
the `50% 28%` default.

**X-Men cannot take one, and it is worth knowing why before trying.** That plate
is 2.58:1 against a banner box of about 2.38:1, so `object-fit:cover` fits it by
*height* and crops the width instead — the whole image is already visible top to
bottom at every width, and the `Y` half of `object-position` is inert. When the
bottom of a banner looks cut off, check the aspect before reaching for the crop:
on that one it was the scrim, not the framing.

**The fallback chain matters, because seven of the eight banner files are
supplied by hand and may not be there.** `hbFallback()` in each tracker walks
`Art/Banners/<id>.jpg` → `Art/Heroes/<id>.jpg` (the subject's poster scan, at
the same `pos` crop the dossier banner uses) → the `.hb-fallback` ramp. The
homescreen has no poster of its own, so its fallback is all seven posters in a
row behind the scrim (`#hbTiles`) — they are already downloaded for the wall
below, so it costs no request.

The title treatment over the banner is the subject's printed logo from
`Art/Logos/`, with the name as text if the logo fails. Same
degrade-don't-vanish rule the plate follows.

### Keep Reading

The old single "Up Next" / "Continue Reading" bar named one issue. This names
one per place you have something open, because the reading is not linear.

A **spot** is one omnibus volume with at least one issue left in it — the
streaming metaphor's show. `spotFor()` builds one, `spots()` returns the
touched ones newest-first, and `krCard()` draws the tile. Nothing started
anywhere returns the first volume on the shelf instead, so a fresh browser gets
a "Start Reading" tile rather than an empty band.

**The cover is shown whole, and the tile is still one piece of art.** Those two
pull against each other and the layering is what resolves them, so do not
collapse it back:

- `.kr-face` is the cover at 2:3 against the left edge, width `var(--cw)`, so
  the entire scan is visible. It used to be `object-fit:cover` across the whole
  tile, which cropped a 2:3 scan to about a quarter of itself — the tile read as
  an abstract band and you could not tell one book from another.
- `.kr-blur` is the *same image again*, scaled 124%, blurred and dimmed behind
  everything. That is what keeps it from looking like a thumbnail bolted to a
  panel: the tile carries the cover's own colour edge to edge. Same `src`, so
  it is one request.
- `.kr-card::after` dissolves the two together starting 8px before the cover's
  right edge and solid 58px past it.

**Everything right of the cover is placed off `--cw`, not off a percentage of
the tile.** The tile width is a `clamp()`, so a percentage stop drifts off the
cover's edge at some widths and the gradient starts cutting into the art. One
variable, redeclared in the 600px media query along with the tile height, keeps
the geometry right at both sizes.

**Two things on the tile are approximations, and both are deliberate:**

- **The bar is progress through the volume, not through the issue.** There is no
  such thing as being halfway through one issue in this data — an issue is read,
  skipped or neither. The position line reads "Issue 12 of 43" for the same
  reason: it is an episode number, not a score.
- **The credits are the volume's `creators`, not the issue's.** For most
  omnibuses that is exactly the writer and penciler, because the book is named
  for them. Per-issue credits are not in the shelf data at all; getting them
  means a wiki pull per issue across 3,400 issues. See open item 15.

A tile is an `<a href="#/omni/<id>">`. Inside that volume already, the hash does
not change and no route fires, so the click handler does the jump itself —
`pendingJump` → `jumpToIssue()`, which opens the chapter, scrolls the row into
view and flashes it. Crossing from the homescreen loses `pendingJump` (different
document); the volume view opens the right chapter anyway.

### The dark chrome

The palette is one block of variables at the top of every page's `<style>`,
under a comment naming the two rules that make it work: the page background is
flat `--bg` (see "The banner"), and panels are a low-alpha white wash over it
rather than their own colour, so retinting the site is one variable.

    --bg #0a0e15   --line rgba(255,255,255,.10)   --txt #e9eff7   --dim #9db0c6

What survived from the old look, because it is artwork rather than chrome: the
CSS-3D book tiles and their spines, the `.o-*` cover ramps, the `.tex-*`
textures, the `.a-*` poster ramps, the poster plates and printed logos, and the
gold `--xyellow` accent.

What went: the sky gradient, the four floating `.bubble`s, every glass panel
with a white inner highlight, the glossy orb buttons, and the gradient-clipped
italic headings.

The chrome is duplicated in all eight files on purpose — same portability rule
as the summary engine. Change one, change the others.

## Homescreen (`index.html`)

The `HEROES` array is the whole configuration. Each entry:
`{id, name, art, tex, emblem, cover, pos, plate, logo, logow?, era, file, total, desc, light?}`.
- `file: null` → poster renders dimmed with a "Curating" badge, and clicking it
  opens the dossier modal instead of navigating.
- `file: "…"` → clicking the poster navigates straight to the tracker. The small
  "i" button opens the dossier.

**There is no "Ready" badge** (Aug 2026). It was a gold pill on every live
poster, and once all seven subjects were live it labelled nothing — seven
identical badges is not information. The badge element itself stays, because
"Curating" on a subject with no list *is* worth flagging; only the `.live`
variant went. Re-adding a distinction between live posters means finding
something that actually differs between them.

### Artwork

**Every subject shows a real comic cover** (Aug 2026). One scan per subject in
`Art/Heroes/<id>.jpg`, pointed at by `cover` in that hero's `HEROES` entry, run
through the same `covers.save_cover` 700px/q82 downscale as the omnibus shelf
covers so the whole site's art is sized identically.

**All seven are hand-supplied art, not wiki scans** (Aug 2026). The user
dropped the originals into `Art/covers/` and they replaced the fetched covers
outright. They are painted pieces rather than printed covers, and that turns
out to matter for this particular job: no logo, no barcode strip and no trade
dress fighting the poster plate, so the subject name sits on clean art on all
seven. Keep that property in mind when swapping one — a scan of a printed cover
will put a logo where the plate goes.

`tools/fetch_hero_art.py` is now the **fallback** route, not the live one. Its
`PICKS` table still holds a wiki pick and the reasoning for every subject, and
`SUPPLIED` beside it lists the seven whose art is hand-supplied; `--all` skips
those and says so, and `--replace` is what overwrites them. One entry in `PICKS`
is worth repeating because it is the trap it always was: **Incredible Hulk #340
is the famous Hulk cover and is three quarters Wolverine**, who is the poster
next to it.

The handmade art is still underneath and is still the fallback. Three layers per
poster — an `.a-*` colour ramp, a `.tex-*` pattern (web / claw marks / impact
burst / crosshatch / starfield / moonlight / radar rings), and an `EMBLEMS`
inline SVG — and `artHTML()` now paints the scan **over** the first two rather
than replacing them, so a cover that fails to load degrades to the old poster
instead of to an empty box. (The shelf's own `artHTML(o)` returns the image
*instead of* its ramp; this one deliberately does not.) `.wide` variants of each
ramp re-aim the gradient for the short, wide modal banner, which would otherwise
bottom out to black in its first 40px.

What a cover changes, beyond the picture:
- **the emblem is dropped** on that subject's poster, Continue thumbnail and
  modal banner. A printed cover carries its own logo and figure; the SVG emblem
  on top of it was just clutter. Subjects with no scan still get one, so
  `emblemSVG()` and `EMBLEMS` stay live.
- **the plate darkens** (`.poster.hascover .plate`). Covers put their own logo
  and the barcode strip exactly where the subject name goes, so the plate has to
  read as its own band rather than as a soft fade.
- **the gloss halves** (`.gloss.soft`). Full strength reads as a sheen on a flat
  ramp and as haze over printed art.

The modal banner is a 2.8:1 slot cut out of a 2:3 page, so **where to crop is
per-cover**: optional `pos` on a `HEROES` entry sets `object-position` on the
banner only (the poster is the same aspect as the cover and crops almost
nothing). **All seven now set it** and none of them landed on a guess: every
value below was arrived at by rendering `#mArt` and looking, and four needed a
second pass after the first render clipped something.

| Subject | `pos` | What the band is framed on |
|---|---|---|
| spider-man | 14% | the mask, webline arm across the left |
| wolverine | 13% | the mask — 19% clipped the ear tips |
| hulk | 41% | the roaring head — 45% clipped the hair |
| xmen | 33% | the Jean / Cyclops / Storm face row |
| fantastic-four | 45% | Reed, the Torch, the Thing's fist |
| moon-knight | 7% | the crescent and fist against the moon |
| daredevil | 11% | the head, with the full moon behind it |

Two of those are judgement rather than framing. The FF cover's most striking
band is **Doom's eyes** across the top (`pos:"18%"`), and it was set there
first; 45% is deliberate, because a banner headed by Doom reads as the wrong
subject when the poster below it says Fantastic Four. Moon Knight's 7% drops
the character's face entirely — the crescent held up against the moon is the
stronger 2.8:1 strip, and the poster already shows the whole figure.

Retuning one means looking at it — screenshot `#mArt`, do not reason about it.
The geometry, if it helps you pick a starting value: the visible band is 23.8%
of the image's height and its top edge sits at `0.762 × pos`.

Two non-obvious constraints, both already bitten once:
- `emblemSVG()` mints a **fresh gradient id per call**. Reusing one id makes every
  later copy of an emblem inherit the first one's fill.
- `.art` / `.tex` / `.gloss` / `.vig` are **not** scoped under `.poster`. The same
  markup is reused by the Continue thumbnail and the modal banner; scoping them
  collapsed both to zero height.

Moon Knight sets `light:true`, which swapped the gold emblem ramp for an ink one —
gold on a near-white poster is invisible. With a cover on that poster the emblem
is gone and the flag does nothing visible. **The reason it is kept has changed**:
it used to be that the subject was still the light one on the wall, and the new
cover is a dark blue night piece, so that is no longer true. What is still true
is that the flag governs the `.a-moon` fallback ramp, which is as pale as it
ever was — dropping `cover`, or a scan that fails to load, brings the ink emblem
back and needs it.

### The plate — the subject's colour, and its logo

The plate is the band across the foot of each poster. Until Aug 2026 it was one
shared navy carrying the subject name, the "N / N logged" count and the
progress bar. It now carries **the subject's printed logo on the subject's own
colour, and nothing else** — no name, no count, no bar.

`plate` on a `HEROES` entry is `[mid, foot]` as two **rgb triples** — the stops
the gradient interpolates between, set as `--p1`/`--p2` on the element by
`plateVars()`. They are triples rather than hex so the CSS can vary the alpha
per stop (`rgba(var(--p1),.86)`), which is what lets the band fade into the art
above it instead of starting as a hard edge. An entry with no `plate` falls
back to the old navy, so the field is optional and nothing breaks without it.

| Subject | Plate | Why |
|---|---|---|
| spider-man | blue | the suit's other half; the art above is red |
| wolverine | yellow, run deep | see below |
| hulk | **purple** | the user's call, and the right one — a green plate under green art disappears |
| xmen | green | |
| fantastic-four | uniform blue, nudged toward teal | |
| moon-knight | black | |
| daredevil | red, run deep | see below |

**Wolverine's and Daredevil's plates are noticeably deeper than the other
five**, and that is the one non-obvious thing here. Both logos are the same hue
as the plate the subject asked for — a yellow Wolverine logo on yellow, a red
Daredevil logo on red — so at the brightness the other five use, the logo
vanished into its own background. Deepening the plate keeps the colour identity
and gives the art something to sit on. Expect to do the same for any future
subject whose logo matches its colour.

The logo is `logo` on the entry, one PNG per subject at `Art/Logos/<id>.png`.
Three things about how it is sized and placed:

- **It is cropped to its alpha bounding box** by `tools/logos.py`, not used as
  supplied. Logo PNGs arrive with wildly different transparent margins — two of
  the seven were 320x320 files holding a 288x109 logo — and since the plate
  sizes the `<img>`, that margin is real layout. Uncropped, a logo with 40%
  padding renders 40% smaller than one without and the wall looks arbitrary.
- **A two-line logo is height-limited where a wide one is width-limited.** Moon
  Knight, Fantastic Four and X-Men are the tall ones and rendered visibly small
  against Spider-Man's and Wolverine's until `max-height` went from 46px to
  56px. Changing that number means re-checking all seven, not just the one that
  looked wrong.
- **`logow` trims the ones that number then made too big.** Raising `max-height`
  fixed the tall logos and left the three wide single-line ones (Spider-Man,
  Wolverine, Hulk) reading oversized, so those carry `logow:"84%"` — a per-
  subject width, emitted as `--lw` by `plateStyle()`, defaulting to 100%. The
  two knobs pull against each other: `max-height` sets the tall logos, `logow`
  brings the wide ones back to match.
- **The logo floats, it does not sit on the foot.** `padding-bottom` on the
  plate is 34px against 13px of side padding, which is what lifts it clear of
  the poster edge. That number was the progress bar's space before the bar came
  off; keeping it is deliberate, and dropping it back to 13px drops the logo
  visibly low.

**The name is gone as text but not as data.** It is still the poster's
`aria-label`, and still the `alt` on the logo `<img>` — so a missing or broken
logo file shows the name rather than an empty band. `.pname` also still renders
in full for any subject with no `logo` at all. That is the same
degrade-don't-vanish rule `cover` follows, and it is worth keeping: the poster
is now an image-only button, so without it a failed request leaves a nameless
tile.

**The progress bar came off the plate too** (Aug 2026), so the poster now
carries no progress at all. That is a real loss of information from the wall
and was the user's call: the plate reads as printed trade dress, and a UI
element in it broke that. It was the first of the progress removals; the rest
followed in the same month and `.pbar` is now deleted from every page — see
"The three levels" above.

### How the homescreen knows your progress

Trackers publish a summary record on every `refresh()`:

    comics-hero-<id> → {total, read, skip, next:{t, arc, ch}, spots:[…]}

`spots` is what the homescreen's Keep Reading rail is built from — one entry per
volume that subject has open, capped at 10, each carrying everything a tile
needs and nothing else:

    {o, vol, cover, cred, t, iss, ch, i, n, done, ts}

`ts` is when something in that volume was last marked, so merging every
subject's `spots` and sorting on it gives one cross-subject rail. It comes from
a `touch` map the tracker keeps **inside its own progress record** —
`{read, skip, touch:{<omniId>:<timestamp>}}`. That field is additive: a backup
written before it existed loads fine and simply sorts everything at 0.

`total`, `read`, `skip` and `next` are still written. Nothing on the homescreen
draws a percentage from them any more, but they are the back-compatible half of
the record and the dossier still reports `total` as inventory.

The homescreen reads those records; it never carries a copy of any tracker's data.
If no record exists yet (that tracker has never been opened since this feature
landed), it falls back to reading the tracker's own progress key directly — see
`LEGACY` in `index.html` — and failing that, to the hardcoded `total`.

Because the record is only a cache of the tracker's own state, deleting it is
always safe.

### The settings gear — one API key for the whole site

The gear in the homescreen header opens a small modal holding the **Anthropic
API key**, and that is the only place the key is entered. It is stored under one
name for the whole origin:

    comics-anthropic-key

Every tracker reads that name directly with plain `localStorage` (not through
`store`), which is why the gear lives on the homescreen and not on a subject
page — same origin, one paste, summaries live everywhere.

`xmen-anthropic-key` is the name the X-Men page used when it owned the key box.
Each page's `getKey()` **migrates it forward on first read and then deletes it**,
so an existing key survives the move without the user noticing. Do not remove
that fallback until you are willing to make people re-paste.

The X-Men page's own key row is gone; its Backup row in the same `.setup` block
stayed. Anything that reads a key should call `getKey()` — never
`localStorage.getItem` directly.

## The Spider-Man tracker (omnibus shelf)

16 omnibus volumes on the shelf, **all 16 with contents** — 617 issue slots, 606
unique issues. Spider-Man vs. Venom was the last placeholder and was filled in
Aug 2026, so the shelf now carries no tile without an issue list.

The shelf is a curated selection, not "every omnibus" — see "Scope call" below.
Display order is `SHELF` in `tools/omnibus_meta.py`; it is a reading order, not
publication order.

### Placeholder volumes

**Nothing on this shelf is a placeholder any more** — `PLACEHOLDERS` and
`PLACEHOLDER_PAGES` in `omnibus_meta.py` are both empty since Spider-Man vs.
Venom was filled in. The machinery below is all still live and still correct;
it is written down because the next shelf addition may need it, and because the
`showOmni()` guard is a real crash if it is ever removed.

A placeholder is an entry with `placeholder:true` and `chapters:[]`. It uses the
`.o-placeholder` ramp, shows a "Contents pending" badge and "not added yet" in place
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

Those fields are one row per *story* — so the generator dedupes globally
(keeping first occurrence) and the surviving order is what drives the chapters.
Prose "Collects…" blurbs from retail sites disagree with each other and with the
books; the ReprintOf fields did not. Prefer them.

**They are not always in printed order, though.** The Spider-Man pages happen to
be; the Hulk pages group by series instead, which put Incredible Hulk #102
seventh in Omnibus Vol. 1 when the book prints it last. Read the pulled order
before trusting it, and correct the raw-contents file where a volume's own
chapter order would come out wrong.

Two API details that cost time the first time round:

- **`ReprintOf<N>` is written two ways.** Spider-Man's pages spell the target in
  full (`Amazing Spider-Man Vol 1 1`); the Hulk's use the short form
  (`Incredible Hulk #1`), which does not say *which* volume of a retitled
  series. The rendered page resolves it: fetch `prop=text` instead and read the
  reprint gallery's captions, whose links are canonical page titles
  (`/wiki/Incredible_Hulk_Vol_1_102`), in the same order. Pull both and check
  the counts match — that is the cheap integrity check on the whole list.
- **`list=allpages&apprefix=…` silently truncates.** `aplimit=500` is a page of
  results, not a limit on the answer, and a prefix like "Incredible Hulk" has
  thousands of issue pages before it reaches the omnibus titles — which is how
  the five *Incredible Hulk by Peter David* volumes went missing from a first
  enumeration that looked complete. Follow `continue.apcontinue` until it stops.

The wiki's `list=search` returns nothing useful here (`intitle:` included), so
prefix enumeration is the way in.

### Auditing contents against the solicit

**The `ReprintOf` fields can silently drop an issue, and the rendered gallery is
not an independent check** — on all three cases found so far the issue was
missing from both. The genuinely independent source on the same page is the
**`Solicit` field**, which is Marvel's own retail copy rather than the wiki's
structured data, and which sometimes ends in an explicit range:

    COLLECTING: THE FANTASTIC FOUR (1961) #164-203 & ANNUAL (1963) #11-13, ...

A sweep in Aug 2026 compared every volume's contents against that line across
all four shelves. Two results worth knowing:

- **Only 16 of 64 volumes carry an explicit range.** The other 48 are marketing
  prose with no numbers, so this check cannot cover them. Do not read a clean
  sweep as a clean shelf.
- **Both disagreements were real**: Fantastic Four #171 (`ff-o6`) and Incredible
  Hulk (2000) #75–76 (`rotm-o1`, whose solicit says `#34-76` where the shelf had
  #34–74). Both are fixed by hand in the raw-contents files.

For the 48 volumes with no range, the fallback that works is: find every small
numeric gap **shelf-wide** (not per volume — an issue skipped by one book is
often in the next one), then check the missing issue's **creator credits**
against what the volume is. A creator-run collection is *supposed* to have
holes; a numbered `<Series> Omnibus Vol. N` is not. That test cleared five gaps
as correct and condemned one:

| Gap | Verdict |
|---|---|
| Incredible Hulk #329–330 | correct — Al Milgrom, not Peter David |
| Fantastic Four #219 | correct — Moench/Sienkiewicz, not Byrne |
| Fantastic Four #351 | correct — Kaminski/Bagley fill-in, not a Doom story |
| Spider-Man #17 | correct — Nocenti/Leonardi, neither McFarlane nor Larsen |
| Amazing Spider-Man #242 | correct — a known Stern skip |
| **Wolverine #55** | **wrong** — Hama/Silvestri, same team as #56, in a complete-run volume |

The scripts for both passes are throwaway; the method is the part worth keeping.
One limit to be honest about: neither pass can see an issue dropped from a
volume that has no solicit range *and* leaves no numeric gap.

### Chaptering — two strategies, chosen automatically

The generator computes runs of consecutive same-series issues and looks at the
average run length:

- **avg ≥ 3.5 → chapter per series run** (12 of the 15 Spider-Man volumes with
  contents). E.g. "Amazing Spider-Man #1–38", "Amazing Spider-Man Annual #1–2".
- **avg < 3.5 → interleaved crossover** (Clone Saga Vol. 1–2, Ben Reilly Vol. 1).
  These books print Web → Amazing → Spider-Man →
  Spectacular month by month, so a per-series chapter would be one issue long.
  They chunk into blocks of 6 labelled "Part N" with the span as the subtitle.

The Part N labels are honest but generic. Real arc names (Power and
Responsibility, The Exile Returns, Maximum Clonage…) would be a genuine
improvement and are the obvious next curation pass.

**`chapterby` in a volume's meta entry overrides the heuristic** (`"series"` or
`"parts"`). The average-run-length test asks "is this a month-by-month
crossover?", and an anthology answers the same way for a different reason: five
of the Hulk volumes are collections of tie-in minis and one-shots, which score
under 3.5 but read far better as one chapter per mini ("World War Hulk: X-Men
#1–3") than as "Part 3". The key is a build-time hint — `build_all()` pops it
before serializing, so it never reaches the page.

**A series run is not necessarily contiguous**, so `spanlabel()` splits it into
contiguous blocks and joins them with commas. The Straczynski volume is why:
it collects Amazing Spider-Man (1999) #30–58 *and* #500–514 across the
renumbering, and one span would have read "#30–514" — a claim of 485 issues.
Half a dozen older chapters gained commas the same way (Stern's volume really
does skip ASM #204–223 and #242), which is a correction, not a regression.

### Issue ids are shared on purpose

An issue collected in two omnibuses gets the **same** id in both, so marking
ASM #324 read in the Michelinie & Larsen volume also marks it read in the
Michelinie & McFarlane volume. On the current shelf 11 issues overlap this way;
the UI flags them with a gold pill reading "in N omnibuses". This is deliberate
— do not de-duplicate ids per volume.

| Overlap | Volumes |
|---|---|
| ASM #324, #327, #329 | `mcf-o1` + `larsen-o1` |
| ASM #300, #315–317 | `mcf-o1` + `vs-venom-o1` |
| ASM #332–333, #346–347 | `larsen-o1` + `vs-venom-o1` |

Eight of those eleven arrived with Spider-Man vs. Venom, which is a
Venom-appearance chronology and therefore doubles back across both Michelinie
volumes by design. Note it does **not** overlap ASM #361–363 despite collecting
them — the Larsen volume stops before them.

Consequence: `flat.length` (617, issue *slots*) and `uniqIds.size` (606, distinct
issues) are different numbers. Progress math uses `uniqIds`; the shelf label uses
slots. The overlap count was much higher (46) before the shelf was trimmed —
it scales with how many overlapping volumes are on the shelf.

### The 3D book shelf

Since Aug 2026 each shelf tile is a CSS-3D hardcover, not a flat poster. The
markup `buildShelf()` emits, outermost first:

    .cell        perspective root (1500px). Owns hover z-index.
      .book      the float wrapper -- `bob` keyframes run on hover
        .shade   soft ground shadow
        .omni    the <button>. Tilted `rotateY(21deg)`, `transform-style:preserve-3d`,
                 and carries `--t` (spine thickness) as an inline style
          .spine  Marvel trade dress -- red MARVEL/OMNIBUS band, vertical title,
                  optional credit line, volume number at the foot
          .pages  the paper block along the top edge
          .face   the cover itself -- art layers, badge, plate (no progress bar
                  since Aug 2026 -- see "The three levels")

The spine is the **shared Marvel trade dress** — black field, red
`MARVEL` / `OMNIBUS` band at the top, white title down the spine, `VOL n` at the
foot. It is not per-volume: it reads `o.spine`/`o.title`, `o.creators` and `o.vol`,
which every entry in `omnibus_meta.py` already carries, so a new omnibus (or a new
hero tracker copied from this one) picks the look up for free.

| What | Where it comes from |
|---|---|
| Spine **text** | `o.spine` (short label; falls back to `o.title` if absent) |
| Spine **credit line** | `o.creators`, shown only when the label is ≤ 16 chars and the credits ≤ 30 |
| Spine **volume number** | first digits found in `o.vol` |
| Spine **thickness** | `bookThickness(issueCount)` — `min(82, max(42, 15 + count*1.15))` px |

Thickness is a real omnibus proportion, not a sliver: a printed volume is ~1.5–3in
across a 7.4in cover, so the spine is 20–40% of the tile width. Volumes with no
contents yet sit at the 42px floor and still read as hardcovers.

Three things to know, all cheap to avoid:

- **`SPINE_C` no longer paints anything.** Every spine is the same black trade
  dress now. The table is kept because `build_omnibus_data.py` still checks that
  each `.o-*` ramp has an entry, and because restoring coloured spines is one
  line. A new `.o-*` ramp therefore still needs a `SPINE_C` entry or the build
  fails loudly.
- **`art` still matters on a volume that has a real `cover`.** It no longer picks
  the spine colour, but `artHTML()` falls back to the `.o-*` ramp whenever `cover`
  is missing or fails to load.
- **The spine text is vertical and clipped, not wrapped.** The length gates in
  `buildShelf()` are tuned to the 196px desktop tile; the 600px breakpoint hides
  `.screds` outright because a 142px tile leaves only ~207px of spine, which fits
  the title but not a credit line under it. Lengthening a `spine` label past ~22
  characters means re-checking both breakpoints.

### Cover art

`artHTML(o)` renders a real image when `o.cover` is set and the CSS ramp
otherwise. Note it returns the image *instead of* the ramp, texture, gloss and
spider glyph — a covered volume is just the scan.

Covers are wired in `tools/omnibus_meta.py` (`cover="Art/Spider-Man/<id>.jpg"`),
never by hand-editing the `OMNI` array in the HTML — that array is generated.

All 16 volumes have cover art. It came from the **Marvel Database wiki** — the
same source as the issue contents — via `prop=pageimages`, which hands back the
cover image stored on each volume's page.

**Refetching, or filling in a new volume:**

```bash
python3 tools/fetch_covers.py                # every volume still missing one
python3 tools/fetch_covers.py vs-venom-o1    # just these
python3 tools/fetch_covers.py --all          # refetch everything, overwriting
python3 tools/build_omnibus_data.py
```

**Adding a scan you have locally** (better art than the wiki's, say):

```bash
python3 tools/covers.py add asm-o4 ~/Downloads/scan.png   # optimise + name it
# paste the printed cover="..." line into tools/omnibus_meta.py
python3 tools/build_omnibus_data.py
```

`fetch_covers.py` writes the `cover=` line into `omnibus_meta.py` itself;
`covers.py add` prints it for you to paste. Both route through
`covers.save_cover()`, so art from either is sized identically. Neither
regenerates — that is the follow-up command.

`covers.py audit` prints what every volume has, flags low-res files, and
reports how much art the shelf carries. That weight is not a build budget — the
covers are served by path — it is what a phone downloads a tile at a time.

**Size is no longer a constraint at all, only a habit.** It used to be one
because the retired mobile build inlined every cover as base64 and enforced the
Artifact's 16MB ceiling; both are gone, and GitHub Pages serves files up to
100MB against a 19MB repo.

The `covers.py add` re-encode to 700px wide / JPEG q82 (~150KB) stays, but as a
choice rather than a constraint: six shelves of art at one size is worth more
than one shelf at a sharper one, and every cover is a separate request on a
phone. A genuinely better scan can be dropped in without worrying about any
budget.

Everything is named `Art/Spider-Man/<volume-id>.jpg` — the original
`The Amazing Spider-Man Vol1.png` style names are gone (git history still has
them). `asm-o1` was a 2.4MB PNG; through the pipeline it is 158KB with no
visible difference at tile size.

**Six covers are low-resolution** — `stern-o1`, `mcf-o1`, `larsen-o1`,
`clone-o2`, `ult-o1`, `ult-death-o1`, all around 325x500. That is genuinely all
the Marvel Database has; `imageinfo` confirms the stored originals are that
small, so refetching will not improve them. They look fine on a standard
display and soft on a retina tile or in the detail banner. `covers.py audit`
marks them `soft`. A better scan dropped in via `covers.py add` is the fix.

### Marvel deep links

600 of 606 unique issues (99%) resolve to a real marvel.com issue page, and all
600 are readable on Marvel Unlimited. The 6 that do not are not on marvel.com
at all; they fall back to a `marvel.com/search?query=` URL and render a grey
Read button — same convention as the X-Men tracker.

**`MARVEL` in the tracker is generated** from `tools/marvel_ids.json` by
`build_omnibus_data.py`, same as `OMNI` — do not hand-edit it. It used to be
hand-synced, which is how it silently fell 54 entries behind the store. The
build prints link coverage on every run, so a gap shows up without being
looked for.

**This is the Marvel Unlimited path, and there is nothing else to build.** The
Read button goes to `marvel.com/comics/issue/<id>/<slug>` — the issue's own page,
carrying the description and the Read Now button that opens it in Marvel
Unlimited for a subscriber. "Marvel Unlimited link" and "marvel.com issue link"
mean the same destination here; there is no separate `read.marvel.com` URL
scheme to harvest, and a new hero needs only the same id harvest described
below.

`MARVEL` still carries all 1178 harvested ids, 744 of which no longer match any
issue on the shelf. That is intentional: unused keys cost nothing, and keeping
them means re-adding a trimmed volume does not require re-running the harvester
against a rate-limited marvel.com.

**The Straczynski volume is fully linked as of Aug 2026.** All 47 of its Amazing
Spider-Man (1999) issues (#30–58 and #500–514) resolve. What cracked it was one
web search for the series id (**454**), a `series` pull for a seed, and a `walk`
from **#36 at id 42508** — after several id sweeps had failed. See "Start with a
web search, not with a probe".

The 11 that marvel.com does not have: Spectacular Spider-Man Magazine (2),
Spectacular Spider-Man Annual (2), and one each of Untold Tales of Spider-Man
#-1, Untold Tales: Strange Encounters, Collectors' Preview, Spider-Man Holiday
Special, Amazing Spider-Man Annual '96, a Wizard mini-comic and Ultimate
Spider-Man #½. Magazines, ashcans and half-numbered oddities — see "What is
left, and why".

### Linking issues: sweep the catalog once, then it is a local lookup

**This is the method. Everything under it is history.** marvel.com runs an open
JSON catalog at `bifrost.marvel.com` — no key, no scraping, ~1KB an issue
instead of a 250KB HTML page, and each record carries the canonical issue URL,
the series it belongs to, the issue number, and whether the issue is on Marvel
Unlimited. A full sweep of the id space is therefore cheap, and once swept,
linking an issue is a lookup in a local file rather than a web search.

```bash
python3 tools/catalog.py sweep      # resumable; ~20 min for all 140,000 ids
python3 tools/catalog.py status     # how much is banked
python3 tools/link_issues.py        # report what would link, writes nothing
python3 tools/link_issues.py --write
```

Then regenerate each hero as usual. The sweep is
already committed (`tools/marvel_catalog.json`), so a fresh session only needs
to re-run it to pick up issues published since.

The open endpoints, all unauthenticated (anything under `/v1/` needs a token
and is not worth chasing):

| Path | Gives |
|---|---|
| `/catalog/comics/{id}` | url, series id, issue number, `in_mu`, prev/next siblings |
| `/catalog/series/{id}` | series title, years, issue count |
| `/catalog/{type}/{id}/related/series` | sibling series |

`prev_next_issue` walks a whole run from one seed **at any era** — id 8906
returns Incredible Hulk (1962) #2 as its next issue, where the *HTML* page for
the same issue links no siblings at all. That is the fact that made the old
scraping route look impossible for pre-2008 material.

### How the links used to be missed

The old route was: harvest an id range off the HTML pages, then hand-add an
entry to a `SLUG_PFX` table in `series_harvest.py` so `write` would keep what
was harvested. Two failure modes, and **both were silent**:

- **Nothing swept the range.** Nothing below id 8687 had ever been probed, so
  the whole low regime was invisible. Books of Doom sat at 3006–4033 with all
  six issues live on marvel.com and grey on the shelf.
- **A missing table entry threw the result away.** `write` only promotes a slug
  whose prefix is in `SLUG_PFX`; anything else is counted and dropped. The table
  needed one hand-written line per series, forever.

`link_issues.py` has no such table. It matches two ways and **reports anything
it cannot decide** instead of dropping it:

1. **Learn from what already works.** An issue that *is* linked tells you which
   marvel.com series its id prefix belongs to — `wolv-118` resolving to
   `wolverine_1988_118` means prefix `wolv` is that series, so `wolv-55` is
   issue 55 of it. Exact, no name matching.
2. **Name-match the rest**, after folding both sides hard (number words, `&`
   vs `/` vs `and`, Marvel's trailing `1` on one-shot titles, and the character
   prefix it adds to minis — "Spider-Man: Funeral For An Octopus" for a book the
   shelf calls "Funeral for an Octopus").

Two guards keep that from producing confident nonsense:

- **A reused title is narrowed, never guessed.** There are seven X-Forces and
  four Amazing Fantasys. `tiebreak()` tries, in order: a year the shelf itself
  names, then overlap with the volume's era, then the earliest start year (a
  revival continuing the old numbering beats a later reboot), then an exact
  title match. First rule leaving exactly one candidate wins; if none does, the
  issue is reported as ambiguous.
- **Two shelf series cannot be one marvel.com series.** The shelf keeps the
  wiki's volumes apart (`tta` is Tales to Astonish Vol 1, `tta3` is Vol 3), so a
  name match onto a series a working prefix already owns is a different comic
  that merely shares a title and a number. That single rule is what stops
  "Tales to Astonish (1994) #1" landing on Tales To Astonish (1959) #1.

`ALIAS` at the top of the file is the last resort, for the handful of genuine
naming disagreements (the shelf's "Uncanny X-Men" is marvel.com's "X-Men
(1963 - 2011)"). It is five entries, and the run's own report names anything
that might belong in it — so unlike `SLUG_PFX` it cannot grow silently.

`NUM_ALIAS` beside it is the same thing for an issue *number*, keyed by shelf
issue id, and is held to the same standard. It has one entry: the Marvel
Database files the 1989 Daredevil annual as `#4B` because its cover reprints
the number 4, where marvel.com numbers the run straight through and calls it
`#5`. Reach for it only when no rule can derive the answer — the trailing-zero
case that also turned up on the Daredevil shelf (the wiki's Daredevil (2014)
`#1.50` against the catalog's `1.5`) was a `numkey()` fix instead, because that
one generalises.

`ISSUE_ALIAS` is the last resort below both, and pins a shelf issue id straight
to a catalog id. Every entry so far is a **Marvel Graphic Novel**, and they are
all one shape: the wiki files that line by number (`Marvel Graphic Novel Vol 1
68`), where marvel.com files each volume under its own story title
(`avengers_deathtrap_-_the_vault_1991_1`) as issue #1 of a one-issue series. The
story title is the only thing that could match it, and **the pipeline has
already thrown it away** — a raw-contents entry must end in the issue number or
the `<series>`/`<issue>` split fails, so the subtitle repair strips exactly the
information the matcher would need. No rule can recover that, hence a pin.

Four are pinned (`mgn-49`, `-65`, `-67`, `-68`); only `mgn-50` is genuinely
absent from the catalog. All four had been recorded as "not on marvel.com" for
months, which is the same lesson as the naming pass: **re-test a "not in the
catalog" verdict before believing it.** `catalog.py find "<story title>"` is the
whole check. The pin stores the id only — the slug is read back out of the
catalog — and the run exits loudly if a pinned id is not in it.

### What is left, and why

**3356 of 3412 unique issues across the six shelves resolve (98%).** The 56
that do not were each checked against the catalog: they are not on marvel.com
at all. `tools/unlinked.json` is the written record, refreshed by
`link_issues.py --dump`.

The largest are Epic Illustrated (9 — a magazine, never digitised), Hulk!
Magazine (8 — the same shape), Marc Spector: Moon Knight #52–56 and #58–60,
the 1992–93 Marvel Holiday Specials, Spectacular Spider-Man Magazine,
What The--?! #2 and #10, the 1992 Marvel Holiday Special (which the Daredevil
shelf wants too), and a tail of ashcans, `#-1` and `#½` oddities and
promotional one-shots. Astonishing Tales (1970) is still short — the catalog
holds 21 of its 36 issues, which confirms the older finding that the rest were
pulled rather than merely unfound.

**Nine of those 40 were recovered in a later pass**, all after the user found
`wolverine_1988_102.5` by hand, so treat "not in the catalog" as a claim worth
re-testing rather than a verdict. What the pass added, and why each was missed:

| Shape | Example |
|---|---|
| point issue filed under an invented name | the wiki's "Wolverine Special #102.5" is Wolverine (1988) #102.5 |
| marvel.com carries the shelf's name inside a longer one | "Peter Parker, The Spectacular Spider-Man Annual"; "Iron Fist/Wolverine: The Return Of K'un Lun" |
| the prefix's usual series does not hold this number | Ultimate Spider-Man #½ is its own series |
| a one-shot filed as #0 | Ghost Rider/Wolverine/Punisher: The Dark Design |
| a series named for the one issue it holds | "UNTOLD TALES OF SPIDER-MAN -1" |
| abbreviation | the shelf's FCBD and FF for Free Comic Book Day and Fantastic Four |

**Everything below this line is the superseded route.** `series_harvest.py` and
`harvest.py` still work and their id-space notes are still true, but there is no
longer a reason to reach for them: the catalog answers the same questions in one
local lookup. Keep the notes for the archaeology, not the workflow.

### Harvest by series, not by id range

`tools/series_harvest.py` is the method to reach for first. Three facts make it
much cheaper and more reliable than probing an id range:

- `/comics/series/<id>/<anything>` **resolves on the id alone** — the slug in
  the URL is decoration. So the series-id space can be probed by title the same
  way the issue-id space is.
- A series page lists ~20 of its issues as `/comics/issue/<id>/<slug>`, which is
  exactly the `<id>/<slug>` fragment `MARVEL` stores. No second request, no
  slug to reconstruct.
- An **issue page links to its neighbours in the same series**, so one known
  issue walks out to the whole run at about a request per issue — and unlike a
  blind scan it cannot skip one.

```bash
python3 tools/series_harvest.py probe  2350:2650      # series id -> title
python3 tools/series_harvest.py series 2400 2418      # series -> its issues
python3 tools/series_harvest.py walk   immortal_hulk_2018:77345
python3 tools/series_harvest.py scan   12860:13340    # blind id sweep
python3 tools/series_harvest.py write                 # -> marvel_ids.json
```

**`scan` is the way into the pre-2008 material**, where `walk` is useless
because marvel.com stops linking siblings that far back. It probes an issue-id
range and reads each page's *own* slug back out of it — the live page links
`/comics/issue/<id>/<real-slug>` alongside the `/x` placeholder that was
requested, and a dead id carries no self-link at all, which is how the two are
told apart without trusting the HTTP status. That means it banks slug → id like
every other subcommand, so `write` can consume it; `harvest.py` banks id →
*title*, which `write` cannot. Probed ids (dead ones included) are recorded in
`series_scanned.json`, so a rerun after a 403 storm costs nothing.

The first three append to `tools/series_links.json` and are resumable; `write`
only adds slugs whose prefix is in `SLUG_PFX`, and prints the ones that are not
rather than guessing. That is how Immortal Hulk (51 issues), Incredible Hulk
(2000) (114) and Hulk (2021) (14) were resolved, in minutes rather than hours.

Two things it will not do for you. **Series ids cluster by era but are not
ordered**, so finding an unknown mini means probing a range near a known
sibling — the 2007 World War Hulk tie-ins all sit in 2400–2600, which is how
X-Men, Gamma Corps and World Breaker were found. And **a series page only shows
the tail of a long run** (Hulk (2008) gives #38–57, and the walk stops at #30
because marvel.com does not link further back), so pre-2008 material still needs
the id scan below.

**marvel.com's series names do not always match the wiki's**, and `SLUG_PFX`
takes a callable for exactly that case. The wiki splits the 1999 Hulk ongoing in
two at the retitling — `Hulk Vol 1` #1–11, then `Incredible Hulk Vol 2` #12–112 —
where marvel.com keeps one `hulk_1999` series across the whole run. Punctuation
drifts too: series `world_war_hulk_xmen_2007` holds issues named
`world_war_hulk_x-men_2007_N`, which is why the issue filter groups by slug stem
rather than matching the series slug.

### Start with a web search, not with a probe

**An external web search restricted to `marvel.com` hands back
`/comics/series/<id>/<slug>` and `/comics/issue/<id>/<slug>` URLs verbatim** —
which is the id you were about to spend several hundred requests hunting for.
This is emphatically *not* the same thing as marvel.com's own `/search?query=`,
which is client-rendered and useless (below); it is that a search engine has
already crawled those pages and indexes the canonical URL.

So the cheap order of operations for any series you can name is:

1. Web-search `marvel.com "comics/series" "<title> <year>"` → the series id.
2. `series_harvest.py series <id>` → ~20 issues, and a walk seed.
3. `series_harvest.py walk <slug_prefix>:<seed>` → the rest of the run.

That resolved the Wolverine shelf's last nine series in about a minute each,
*after* a series-id probe across 1800–3400 and exhaustive issue scans of
30000–31500 had all missed them. Uncanny X-Force (2010) turned out to be series
**9976**, issue #1 at id **32573** — the series id an order of magnitude outside
anything previously probed, and the issue id above every range swept. No amount
of striding would have found it in reasonable time.

`probe` and `scan` are what remains for material a search cannot name: an
unknown mini, or pre-2008 runs whose pages are thinly indexed.

Three routes that look promising and are not, so nobody re-walks them:
`www.marvel.com/sitemap.xml` exists and resolves but carries **no**
`/comics/issue/` URLs; `/search?query=…` is client-rendered and returns no
results in the HTML; and `/comics/calendar?date=YYYY-MM-DD` accepts the
parameter but always answers with the current week.

**The id-scanning runbook still works, but marvel.com is much more aggressive
about rate limiting than it was.** `-P 20` over ~500 ids succeeded once and then
403'd everything for several minutes; `-P 5` with 2s pauses also tripped it. What
does work is `tools/harvest.py` — small batches, 3 workers, and **403
detection that backs off and retries the same batch** instead of burning through
the range while blocked. Without that, a long run silently returns nothing.

Also note: ID blocks are contiguous per series, so a **scan** beats a walk badly.
One sweep of 6440–6960 returned all 441 Amazing Spider-Man issues with no gaps.
Known block seeds: ASM (1963) ≈ 6482–6900, Spectacular (1976) ≈ 14542–14800,
Web of Spider-Man (1985) ≈ 11973–12100, Spider-Man (1990) ≈ 10767–10870,
Marvel Team-Up (1972) ≈ 19619–19690, Clone Saga minis + Sensational ≈ 61238–61260,
Ultimate Spider-Man (2000) ≈ 14836–14930, Ultimate Comics Spider-Man #150–160
≈ 37454–37466, Ultimate Fallout ≈ 39962–39967.
Annuals live in a different, still-unlocated block (Web of Spider-Man Annual #1
is 80439, but 80330–80620 did not contain the ASM annuals).

**The id space has three regimes, and knowing which one you are in decides the
search.** Mapping them by striding is much cheaper than scanning blind:

| Ids | Ordering | How to search |
|---|---|---|
| ~1–6400 | chronological by cover date, every series interleaved (~200 ids/month) | date-interpolate; ASM (1999) #526 = 3020 and #539 = 5960 anchor it |
| ~6400–26000 | one contiguous block per series, blocks in no useful order, issues **lexicographic** by number (#1, #10, #100, #11…) | stride 50–60 to find the block, then scan it end to end |
| ~33000+ | chronological again, with digital-backfill batches of older material spliced in | stride 20 near the release date, then scan the neighbourhood |

Striding 40 across 6400–26000 maps the middle regime's blocks in about 500
probes and is worth doing once before any targeted scan — that single pass is
where the Incredible Hulk (1962) block (8906–9285, all 380 issues), Tales to
Astonish (11347–11447) and the Hulk annuals (16867–16882) all came from.

The lexicographic ordering in the middle regime is the surprise: a block that
starts at #10 has not skipped #1–9, they are at the far end. Do not stop a scan
because the numbers look wrong.

### A grey Read button now means one thing

It means the issue is **not on marvel.com**, and `tools/unlinked.json` says so
by name. That was not true before the catalog sweep, when a grey button mostly
meant nobody had looked — see "How the links used to be missed".

So the check when one appears is: `python3 tools/catalog.py find "<title>"`. A
hit means the matcher missed it and the run's own report will say whether it was
ambiguous or rejected; no hit means Marvel does not have it.

### Tooling (`tools/`)

- `catalog.py` — **the id harvester to use.** Sweeps marvel.com's open JSON
  catalog (`bifrost.marvel.com`) into `marvel_catalog.json` / `marvel_series.json`;
  `status` reports coverage, `find` searches it. Resumable — probed ids, dead
  ones included, are recorded in `marvel_catalog_probed.json`. See "Linking
  issues" above.
- `link_issues.py` — matches every shelf issue against that catalog and writes
  `marvel_ids.json`. No table of series prefixes to maintain; reports ambiguity
  instead of guessing. Its three last-resort tables (`ALIAS`, `NUM_ALIAS`,
  `ISSUE_ALIAS`) hold ten entries between them and cannot grow silently,
  because every run reports what it could not match. `--write` to commit,
  `--dump` to refresh `unlinked.json`.
- `marvel_catalog.json`, `marvel_series.json`, `marvel_catalog_probed.json` —
  the swept catalog (61,408 issues, 6,946 series), shared by all heroes.
- `unlinked.json` — the written record of every shelf issue marvel.com does not
  have. Regenerated by `link_issues.py --dump`.
- `harvest.py` — **superseded by `catalog.py`.** The rate-limit-aware marvel.com ID harvester.
  `python3 tools/harvest.py 6440:6960:asm 14500:14820:spectacular` probes those
  id ranges and appends to `tools/marvel_ids.json`. Resumable: already-probed ids
  are skipped, so rerunning after a block costs nothing.
- `omnibus_contents_raw.json`, `hulk_contents_raw.json`, `ff_contents_raw.json`,
  `wolverine_contents_raw.json`, `moonknight_contents_raw.json`,
  `daredevil_contents_raw.json` — the raw
  ReprintOf lists pulled from the Marvel Database, one entry per omnibus, one
  file per hero. Regenerate only if a volume's contents change.
- `heroes.py` — the hero registry. One entry per omnibus-shelf subject, holding
  its tracker filename, art directory, metadata module, panel key and route.
  Every other tool takes `--hero <key>` (default `spider-man`) and reads its
  paths from here. `python3 tools/heroes.py` lists what is registered.
- `omnibus_meta.py` (Spider-Man), `hulk_meta.py` (Hulk), `ff_meta.py` (Fantastic
  Four), `wolverine_meta.py` (Wolverine), `moonknight_meta.py` (Moon Knight),
  `daredevil_meta.py` (Daredevil) — the hand-written half,
  and **the only place shelf metadata should be edited**: `ORDER` (wiki-backed
  volumes; each key must exist in that hero's raw-contents file or `gen()`
  KeyErrors), `PLACEHOLDERS` (shelf tiles with no contents), and `SHELF`
  (display order by id). This is where a new omnibus, a `spine` label, a
  `chapterby` override or a `cover` path gets added.

  One formatting constraint: `fetch_covers.py` anchors the `cover=` line it
  writes to a `spine="…",` that **ends its line**, so keep `spine` last on its
  line — that is why `chapterby` is written before it, not after.
- `build_omnibus_data.py` — turns the two above into the `OMNI` array, and
  `marvel_ids.json` into the `MARVEL` map, **and writes both into
  `spiderman-reading-tracker.html`**. Run it with no arguments to
  regenerate; `--check` verifies the file matches without writing (exit 1 if
  not). It also fails loudly on an unknown field, an id in `SHELF` that nothing
  defines, a volume defined but missing from `SHELF`, and an `.o-*` ramp with no
  `SPINE_C` entry.
- `fetch_hero_art.py` — the homescreen's poster art, and the **fallback** route
  since all seven subjects went to hand-supplied scans. Pulls one cover per
  subject from the Marvel Database into `Art/Heroes/<hero id>.jpg` through
  `covers.save_cover`, so it is sized identically to the shelf art. `PICKS`
  holds which cover and why; `SUPPLIED` lists the subjects it will not
  overwrite without `--replace`. Nothing is generated from it — the `cover`
  field in `HEROES` is hand-written — so a new pick is an edit in both places.
- `banners.py` — the above-the-fold banner art. `add <key> <image>` normalises
  one to 1800px/q82 into `Art/Banners/<key>.jpg`; `add-folder <dir>` matches a
  whole folder against the eight keys by filename and **reports** anything
  ambiguous rather than guessing; `audit` lists what is there. There is no fetch
  route — these are hand-picked wide art, like the logos. Needs Pillow.
- `logos.py` — the homescreen logo pipeline. `add <hero-id> <image>` crops a
  logo to its alpha bounding box, downscales to 500px and writes
  `Art/Logos/<hero-id>.png`; `audit` lists what every subject has and flags any
  file with no alpha channel, which would render as a box. There is no fetch
  route — a printed logo is not on the Marvel Database as a clean transparent
  asset, so these are supplied by hand and the tool only normalises them.
  Needs Pillow.
- `covers.py` — cover art pipeline. `add <volume-id> <image>` optimises a scan
  to 700px/q82 and prints the line to paste into `omnibus_meta.py`; `audit`
  reports every volume's cover and how much art the shelf carries — a download
  weight, not a build budget; there is no build. Needs Pillow
  (`pip install Pillow`).
- `fetch_covers.py` — pulls cover art from the Marvel Database and writes the
  `cover=` line into `omnibus_meta.py`. Wiki page titles come from the `ORDER`
  keys; the placeholders have no such key, so their pages are listed in
  `PLACEHOLDER_PAGES` in the meta module.
- `fetch_xmen_covers.py` — the same job for the X-Men shelf, which
  `fetch_covers.py` cannot do: those four books were never printed, so they have
  no wiki page to map to and X-Men is not in `heroes.py`. A hand-written `PICKS`
  table names the image and the reason for each volume, and the `cover:` line is
  written straight into the `OMNI` array in the HTML — there is no meta module
  and nothing to regenerate. See "Cover art for books with no covers".
- `series_harvest.py` — **superseded by `catalog.py`.** The older HTML harvester: `probe` maps a range of series
  ids to titles, `series` pulls a series page's issue list, `walk` follows an
  issue's sibling links across a whole run, `scan` blind-probes a range of issue
  ids for the pre-2008 material the other three cannot reach, and `write` merges
  the result into `marvel_ids.json` through its `SLUG_PFX` table. See "Harvest by
  series, not by id range" above. Every shelf feeds from the same store.
- `series_links.json`, `series_titles.json`, `series_scanned.json` — what
  `series_harvest.py` has banked: issue slug → marvel id, series id → title, and
  which issue ids `scan` has already probed (dead ones included). Resumable
  caches, so a rerun costs nothing.
- `marvel_ids.json` — id → marvel.com path fragment, **shared by all three heroes**.
  `build_omnibus_data.py` splices it in as `MARVEL`, so a harvest lands by
  regenerating, not by editing the HTML.
**`OMNI` and `MARVEL` in the HTML are generated — do not hand-edit them.** Change
`omnibus_meta.py` (or `marvel_ids.json`) and regenerate. The serialization is pinned to
`json.dumps(arr, indent=0, ensure_ascii=False)` with a fixed key order
(`KEY_ORDER`) precisely so a regen shows a small diff instead of reshuffling
every entry.

A full shelf change is two commands:

```bash
python3 tools/build_omnibus_data.py --hero hulk  # hulk_meta.py -> OMNI in the tracker
python3 tools/build_omnibus_data.py --check --hero hulk   # confirm it round-trips
```

Note that a harvest touches **every** hero, not one: `marvel_ids.json` is
shared, so `link_issues.py --write` means regenerating all six trackers, not
just the shelf you were working on.

All of these take `--hero <key>`; without one they act on Spider-Man.

### Adding an omnibus hero

The tooling is hero-agnostic; what is not automated is curation and the id
harvest. Roughly in order:

1. **Decide the shelf.** Enumerate candidate volumes with
   `list=allpages&apprefix=<Character>` filtered for `Omnibus`, then make the
   judgement call the tools cannot: which books are *this character's* rather
   than ones they merely appear in. That is a question for the user, not a
   default.
2. **Pull contents** for each wiki-backed volume (the `ReprintOf<N>` call under
   "Where the contents came from") into a `<hero>_contents_raw.json`.
3. **Write `tools/<hero>_meta.py`** — `ORDER`, `PLACEHOLDERS`, `SHELF`, and
   `PLACEHOLDER_PAGES`, modelled on `omnibus_meta.py`. `SERIES_EXTRA` is
   optional now: a series no table names gets a derived code and stays on the
   shelf (see "An unmapped series is derived, not dropped"). Add entries only to
   pin a nicer code, or when the build's report says a series collided with one
   another shelf already owns.
4. **Register it** in `tools/heroes.py`.
5. **Build the tracker page.** Copy `spiderman-reading-tracker.html` (or
   `hulk-reading-tracker.html`) and change the title, the glyph, the `SC` series
   → cover-colour map, the `.o-*` ramps with their `SPINE_C` entries, the cover
   textures, and the storage keys (`comics-hero-<id>`, `<hero>-omni-progress-v1`,
   `<hero>-omni-summaries-v1`).
   Empty `OMNI`/`MARVEL` to `const OMNI = [\n];` and `const MARVEL = {\n};` so
   the generator has something to splice into. This is the one genuinely
   hand-made step — it is design, not plumbing.

   Four things are easy to miss, all found the hard way on the Wolverine page:

   - **`SPINE_C` must use single quotes.** `check_spine_colors()` matches
     `'([\w-]+)':\s*\[`, so a double-quoted table parses as *zero* entries and
     the build stops with "no SPINE_C entry for [every ramp]".
   - **The `.x-emblem` orb is CSS, not part of the glyph SVG.** Swapping the
     inline `<svg>` leaves the previous hero's coloured orb behind it — the
     Wolverine page shipped claws on a Hulk-green disc until it was spotted in a
     screenshot. Its `radial-gradient` and the `drop-shadow` on `.x-emblem svg`
     both want the new palette.
   - **The glyph mints a fresh gradient id per call.** Keep the
     `split("GID").join("<pfx>"+(++gid))` mechanism and give it a new prefix;
     reusing one id makes every later copy inherit the first one's fill.
   - **Leave `.o-placeholder` alone** — the build checks it like any other ramp,
     and a shelf that later gains a placeholder volume needs it.

   A fifth, found on the Daredevil page: **a hero's name is not the only string
   to sweep.** Replacing every "Moon Knight" left the shelf-view subtitle
   reading "Werewolf by Night #32 -> the Midnight Mission", because `hudSub`
   is written twice — once in the markup and once in `showShelf()`, which
   overwrites it on every return to the shelf. Grep for the *content* of the
   previous hero's copy, not just its name, and then screenshot the page.
6. **Harvest Marvel ids** — usually nothing to do. The catalog
   (`tools/marvel_catalog.json`) already holds every Marvel issue, so run
   `python3 tools/link_issues.py --write` and read its report. Only re-sweep
   (`python3 tools/catalog.py sweep`) if the hero's books include issues
   published since the last sweep.

   **Run it twice**, with a regenerate in between: `link_issues.py --write`,
   then `build_omnibus_data.py --hero <key>`, then `link_issues.py` again. The
   matcher learns which marvel.com series a prefix owns by reading the links
   that *already work out of the tracker HTML*, so a second pass sees what the
   first one wrote only after a regenerate. On the Daredevil shelf that turned
   17 reported-ambiguous issues into 17 matched, with no code change.
7. **Generate and publish**: `fetch_covers.py --hero <key>`,
   `build_omnibus_data.py --hero <key>` (in that order — fetch writes the
   `cover=` lines the generator reads), then flip the `HEROES` entry in
   `index.html` and set its `total` to the unique-issue count the generator
   printed.
8. **Ship it.** Commit, push, open the PR and merge it to `main` without
   checking in first — see "Shelf work ships itself" under "Working on this".
   The shelf is not done until Pages is serving it.

### Scope call

The shelf was originally built inclusively — all 25 omnibuses covering Amazing
Fantasy #15 through Revelations, companion ongoings and overlapping creator-run
collections included. It has since been **trimmed to an 18-volume curated
shelf**, listed in `SHELF` in `tools/omnibus_meta.py`.

Dropped: Marvel Team-Up Vol. 1–2, Spectacular Vol. 1, Amazing Vol. 5–8, Web of
Spider-Man Vol. 1–2, Michelinie & Bagley Vol. 1–2, DeMatteis & Buscema, and Ben
Reilly Vol. 2. Removing the companion ongoings is what dropped the overlap count
from 46 shared issues to 3.

Added past the Clone Saga, so the era label is 1962–2011 rather than 1962–1997:
ASM by J. Michael Straczynski, Ultimate Spider-Man and Death of Ultimate
Spider-Man, plus Spider-Man vs. Venom. All four carry full contents.

**Spider-Man vs. Venom sits after the McFarlane volume rather than before it**
(Aug 2026). It was placed before `mcf-o2` while it was a contents-less
placeholder; once the contents were pulled its span turned out to be 1984–1994
and to end on Maximum Carnage, which runs straight into the Clone Saga. Reading
it before a 1990–91 volume meant jumping back four years, so it moved one slot
right.

The two Venomnibus volumes were on the shelf briefly as placeholders and were
removed again (Aug 2026) — they are Venom's books, not Spider-Man's. Their cover
scans went with them; git history has both.

**`tools/omnibus_contents_raw.json` was filtered to match** and no longer holds
the raw wiki contents for the 13 dropped volumes. Nothing on the shelf depends on
them, but re-adding a dropped volume means re-pulling its page with the MediaWiki
call under "Where the contents came from". `marvel_ids.json` and the `MARVEL` map
were *not* trimmed, so the deep links come back for free.

### Summaries on a shelf

Every shelf page carries the same summary engine as the X-Men tracker, with a
**Summary** button on every issue row and **Summarize chapter** in each
chapter's tools. Cached per hero in `<hero>-omni-summaries-v1`; chapter digests
are keyed `CH:<chapterId>` in the same store, so "Clear saved summaries" drops
both.

The one real difference: a shelf has **no offline tier**. The X-Men page ships
27 hand-written `ARC_SUMS` digests, but an omnibus shelf is 660 issues, so
everything here is a live lookup and nothing works without a key. That is why
the no-key message points at the homescreen gear rather than offering a
fallback.

## The Hulk tracker (omnibus shelf)

Same code as the Spider-Man page, same tooling, different data: 17 volumes, 665
issue slots, 659 unique issues, all 17 with contents and cover art. No
placeholders. `tools/hulk_meta.py` is the hand-written half; run everything with
`--hero hulk`.

### Scope call — mainline Bruce Banner only

The wiki lists 21 Hulk-family omnibuses. The four **She-Hulk** books (She-Hulk
Omnibus, Savage She-Hulk, Sensational She-Hulk by John Byrne, She-Hulk by Dan
Slott / Peter David / Rainbow Rowell) are a different character and are
deliberately off the shelf. Everything else is on it, including the two
judgement calls, which the user made explicitly:

- **Hulk by Loeb & McGuinness** is the Hulk (2008) ongoing — the Red Hulk
  mystery. It is the mainline Hulk title of its moment even though Banner
  co-stars.
- **Hulk: Maestro by Peter David** is an alternate-future thread rather than
  the main line, but every issue in it is a Hulk book.

`SHELF` order is a reading order, not publication order. Two placements are
deliberate:

- **maestro-o1 sits after pad-o4**, with the Peter David run it grew out of,
  even though half its contents are 2020–2022.
- **pad-o5 sits after rotm-o1**, because its Incredible Hulk (2000) #77–87 picks
  up directly from where Return of the Monster stops, at #76. (It was recorded
  as stopping at #74 until Aug 2026 — the wiki had dropped #75–76; see open
  item 4.)

**There is one real gap in the shelf, and it is Marvel's, not ours.** Incredible
Hulk (1962) #210–327 has never been collected in omnibus, so `inc-o4` ends at
#209 and `pad-o1` opens at #328. The note on `pad-o1` says so on the page.

`inc-o4` is solicited for February 2027 and carries `released="Announced"`, which
is what puts the amber "Announced" badge on its tile — the same path the
Spider-Man shelf already had but never exercised.

### Contents, and where the wiki order is not print order

Pulled the same way as Spider-Man's (the `ReprintOf<N>` MediaWiki call above),
into `tools/hulk_contents_raw.json`. One difference worth knowing: **the Hulk
pages' ReprintOf fields are not always in print order.** They group by series
where the Spider-Man pages did not. Only one volume is actually wrong because of
it — `inc-o1` lists Incredible Hulk #102 seventh, straight after #1–6, when the
book prints it last, after Tales to Astonish #101 (which is the issue it
continues from). `hulk_contents_raw.json` carries the corrected order.

**Incredible Hulk (2000) #75–76 were missing from `rotm-o1` until Aug 2026.**
The wiki's ReprintOf fields and gallery both stopped at #74, but the volume's own
`Solicit` field says `Collecting INCREDIBLE HULK (2000) #34-76`. Restored by
hand. It was invisible for a long time because it fell exactly on a volume
boundary — `pad-o5` starts at #77, so nothing on the shelf looked out of place;
only a shelf-wide gap check catches that shape. See "Auditing contents against
the solicit".

If a volume's contents are ever re-pulled, re-check both fixes — a fresh pull
will reintroduce them.

### Chaptering

Twelve volumes take the automatic per-series chapters. Five carry
`chapterby="series"` because the heuristic would have chunked them into "Part N":
`wwh-o1`, `planet-o1`, `pad-o5`, `maestro-o1` and `cates-o1`. All five are
anthologies of tie-in minis and one-shots rather than month-by-month crossovers,
so one chapter per mini is both shorter and more informative. World War Hulk
lands at 16 chapters that read as the tie-in list it is.

### Marvel deep links

652 of 659 unique issues (99%) resolve to a real marvel.com issue page; the rest
fall back to `marvel.com/search?query=` and a grey Read button, same convention
as the other trackers. Complete: Incredible Hulk (1962) all 380, Tales to
Astonish, Incredible Hulk (2000), Hulk (2021), Immortal Hulk #1–50, the
Incredible Hulk annuals, and the World War Hulk core minis.

**Hulk (2008) is fully linked as of Aug 2026** — all 24 issues on the shelf,
walked from **#1 at id 17623**, which a web search turned up after the series
page and a sibling walk had both dead-ended at #30. See "Start with a web
search, not with a probe".

The 12 that marvel.com does not have: the 1992 and 1993 Marvel Holiday
Specials, an Incredible Hulk ashcan, Incredible Hulk #-1, Incredible Hulk
Annual '97, Hulk: Hercules Unleashed, What If? General Ross, Hulk: Last Call,
Marvel Spotlight: World War Hulk, Incredible Hulk (2009) #600, Immortal Hulk #0
and the 2021 Free Comic Book Day issue.

### Issue ids and the shared id store

Six issue slots overlap between volumes (Hulk: Future Imperfect #1–2 and
Incredible Hulk #460–461 are in both the Peter David volumes and the Maestro
one; World War Hulk Prologue and Giant-Size Hulk #1 are each in two). They share
ids on purpose, exactly as on the Spider-Man shelf.

`heroes.py` points **both** heroes at the same `tools/marvel_ids.json`. That is
deliberate: the store is keyed by issue id, several series (Web of Spider-Man,
Marvel Comics Presents, Fantastic Four) appear on both shelves, and one store
means an overlap resolves without being harvested twice. The cost is that each
tracker carries some ids it does not use, which was already true of Spider-Man's.

## The Fantastic Four tracker (omnibus shelf)

Same code as the Spider-Man and Hulk pages, same tooling, different data: 18
volumes, 686 issue slots, 661 unique issues, all 18 with contents and cover art.
No placeholders, and nothing unreleased. `tools/ff_meta.py` is the hand-written
half; run everything with `--hero fantastic-four`.

### Scope call — the team's own books, plus two the user asked for

The wiki lists rather more Fantastic Four omnibuses than are on the shelf. The
fourteen mainline volumes are the obvious core: Fantastic Four Omnibus Vol. 1–6
(Lee/Kirby through the Pérez era), by John Byrne Vol. 1–2, by Waid & Wieringo,
by Millar & Hitch, by Jonathan Hickman Vol. 1–2, by Matt Fraction, and by Dan
Slott Vol. 1. Both Ultimate Fantastic Four volumes are on too, matching the call
that put Ultimate Spider-Man on the Spider-Man shelf.

**By Dan Slott Vol. 2 is deliberately absent.** It is solicited for December
2026 and has not been printed — see "A shelf holds books you can actually buy".
Its contents stay in `ff_contents_raw.json`, so re-adding it when it ships is an
`ff_meta.py` edit and a regenerate, not a fresh pull.

Two family books are on the shelf because the user asked for them by name, not
because a rule put them there: **the Thing Omnibus** (Ben Grimm's solo series,
a different character by the reasoning that keeps She-Hulk off the Hulk shelf)
and **Doctor Doom: The Book of Doom** (the antagonist's book, not the team's).

Deliberately off: **Marvel Two-In-One** (the Thing's team-up book — the same
call that dropped Marvel Team-Up from the Spider-Man shelf), **Fantastic
Four/Doom 2099** (mostly Doom 2099's own series, unlike Maestro on the Hulk
shelf, which was all Hulk books), **Heroes Reborn** (a mixed Avengers / Captain
America / Iron Man / FF book) and the **Silver Surfer** omnibuses.

`SHELF` is a reading order. One placement is deliberate: **thing-o1 sits
between the two Byrne volumes**, because that is when it was published and what
it reads alongside — Byrne Vol. 1 ends on Thing #1–2. The two cross-era
anthologies (Doom, Ultimate) sit at the end rather than interrupting the main
line.

**There is one real gap in the shelf, and it is Marvel's, not ours.** Fantastic
Four #296–488 has never been collected in omnibus, so byrne-o2 ends at #295 in
1986 and waid-o1 opens at Fantastic Four (1998) #60 in 2002 — sixteen years,
including the whole DeFalco and Simonson runs and the 1996 Heroes Reborn year.
The note on waid-o1 says so on the page. Same shape as the Hulk shelf's
#210–327 gap.

### Contents

Pulled the same way as the other two shelves (the `ReprintOf<N>` MediaWiki call
above), into `tools/ff_contents_raw.json`. Two things went better here than on
the Hulk shelf and one went worse:

- **Every FF page writes the full form** (`Fantastic Four Vol 1 1`), not the
  short form the Hulk pages used, so no gallery cross-reference was needed to
  disambiguate a retitled series.
- **ReprintOf order matched the rendered gallery order on all 19 volumes**, so
  unlike `inc-o1` on the Hulk shelf nothing needed reordering by hand.
- **Three Marvel Graphic Novel entries carry a subtitle after the issue
  number** — `Marvel Graphic Novel Vol 1 27: Emperor Doom` and two others. The
  pipeline splits a title on its last space to get `<series>` and `<issue>`,
  which that form cannot survive, so the raw file drops the subtitles. If those
  volumes are ever re-pulled, re-apply that.

**Fantastic Four #171 was missing until Aug 2026** — the wiki's page for
Fantastic Four Omnibus Vol. 6 lists it in neither the ReprintOf fields nor the
gallery. It is on the shelf now, restored by hand in `ff_contents_raw.json`
after the volume's own `Solicit` field was found to say
`COLLECTING: THE FANTASTIC FOUR (1961) #164-203`, which settles it. See "Auditing
contents against the solicit" — and re-apply the fix if this volume is ever
re-pulled.

### Chaptering

Eighteen volumes take the automatic per-series chapters. Only `slott-o1` carries
`chapterby="series"`: it is an ongoing with one-shots threaded through it
(Wedding Special, 4 Yancy Street, Negative Zone, the Empyre tie-ins), which
scores under the 3.5 average-run-length threshold for the same reason the Hulk
anthologies did, and reads far better as ten named chapters than as five
"Part N" blocks.

`waid-o1` comes out as a single 36-issue chapter, which looks wrong and is not:
the volume is one series throughout, and `spanlabel()` correctly renders the
renumbering as `#60–70, #500–524` rather than claiming 465 issues. The
Straczynski volume on the Spider-Man shelf has exactly the same shape.

### Issue ids and the overlaps

Twenty-five issue slots overlap between volumes — far more than the other two
shelves, and all of it deliberate:

- **Fantastic Four #91–93 are in both Omnibus Vol. 3 and Vol. 4.** That is the
  printed books, not a data error; Vol. 4 reprints the tail of Vol. 3.
- **The Thing Omnibus** shares Thing #1–2 with Byrne Vol. 1, and further Thing
  and Fantastic Four issues with Byrne Vol. 2.
- **The Book of Doom** doubles back across fifteen years of Lee/Kirby, Byrne and
  later material, so most of its overlap is with the mainline volumes.

They share ids on purpose, exactly as on the other two shelves, and the UI flags
them with the gold "in N omnibuses" pill.

### Marvel deep links

643 of 661 unique issues (97%) resolve to a real marvel.com issue page, and the
rest fall back to
`marvel.com/search?query=` and a grey Read button, same convention as the other
two trackers. Complete: Fantastic Four (1961) all 416, Fantastic Four (1998),
FF (2011), FF (2012), Fantastic Four (2012), Fantastic Four (2018), Ultimate
Fantastic Four, the Fantastic Four annuals, Marvel Team-Up, The Thing, and
Super-Villain Team-Up bar one issue that 404s on marvel.com.

The 20 that marvel.com does not have are dominated by **Epic Illustrated (9)**,
a magazine that was never digitised. The rest: What The--?! (2), and one each of
Giant-Size Super-Stars, Marvel Tales #198, Fantastic Four Special Edition,
Fantastic Four (2012) #5AU, Marvel Graphic Novel #49, Astonishing Tales #7, FOOM
#4 and the two Ultimate X-Men/Ultimate FF annuals. **Astonishing Tales (1970)
is confirmed short at source** — the catalog holds 21 of its 36 issues, which
settles the old open question: the rest were pulled, not missed.

**One sweep of ids 12860–13340 returned all 416 issues of Fantastic Four (1961)
with no gaps** — the single most productive harvest on the project so far, and
the reason the `scan` subcommand exists. That block alone covers most of the six
mainline Lee/Kirby-through-Pérez volumes.

Two things this shelf's harvest taught that the earlier ones did not:

- **Middle-regime blocks are exactly issue-count long.** Fantastic Four Annual
  (1963) is 27 issues at 8687–8713, Marvel Team-Up (1972) is 150 at 19575–19724,
  Strange Tales (1951) is 168 at 11016–11183, The Thing (1983) is 36 at
  18717–18752. So one anchor id plus the run length gives the whole range in
  closed form — no striding needed, if the run length is already known.
- **Do not run two `series_harvest.py` commands against the store at once.**
  Neither process re-reads `series_links.json` mid-run, so the one that finishes
  last silently clobbers the other's entries. That cost a re-run of two series
  on the FF shelf, and it happened again on the Wolverine shelf when a long
  background `scan` overlapped a `series` pull. **The symptom is that the second
  command reports issues found and the store then contains none of them** — it
  looks like the command silently failed, not like a race. Check with
  `pgrep -f series_harvest` before starting anything, and if you delegate a
  harvest, make sequential-only the loudest line in the brief.

## The Wolverine tracker (omnibus shelf)

Same code as the other three shelf pages, same tooling, different data: 14
volumes, 637 issue slots, 636 unique issues, all 14 with contents and cover art.
No placeholders, and nothing unreleased. `tools/wolverine_meta.py` is the
hand-written half; run everything with `--hero wolverine`.

### Scope call — Logan's own books

The wiki lists twenty Wolverine-family omnibuses (plus a prose-novel collection
also called Wolverine: Weapon X Omnibus, which is not comics). Fourteen are on
the shelf: Wolverine Omnibus Vol. 1–6 (the mainline chronology, 1974–1997), Not Dead Yet
(which continues it to 2001), then by Mark Millar, by Jason Aaron, Goes to Hell,
Uncanny X-Force by Rick Remender, Death of Wolverine, Return of Wolverine and
Sabretooth War.

**Uncanny X-Force is on the shelf because the user asked for it by name.** It is
a team book, but Wolverine's team, and it is the book people mean when they ask
about the X-Force with Wolverine in it. Note the thing that is *not* here:
**the 2008 Kyle & Yost X-Force has no omnibus.** The only `X-Force Omnibus` the
wiki carries is the 1991 Liefeld run (New Mutants #98 plus X-Force Vol. 1), which
is neither Logan's book nor the 2008 one, and is off the shelf for the same
reason Marvel Team-Up is off the Spider-Man shelf.

Deliberately off, every one of these the user's call:

- **Weapon X: The Return** — Wolverine appears in 9 of its 53 issues; the rest is
  the Weapon X programme's ensemble series. The same reasoning that keeps
  She-Hulk off the Hulk shelf.
- **Wolverine & the X-Men by Jason Aaron** — an X-Men team book, unlike Uncanny
  X-Force, which is Logan's own strike team.
- **All-New Wolverine** and **X-23** — Laura Kinney is a different character.

Off by the "a shelf holds books you can actually buy" rule: **Wolverine: Old Man
Logan Omnibus** (solicited December 2026) and **Wolverine: The Return of Weapon X
Omnibus** (solicited June 2027). Both keep their entries in
`wolverine_contents_raw.json`, so re-adding either when it ships is a
`wolverine_meta.py` edit and a regenerate rather than a fresh wiki pull. Millar's
volume already collects the original Old Man Logan story, so only the 2016–2018
ongoing is actually missing.

`SHELF` is a reading order, which here runs close to publication order. Two
placements are deliberate: **millar-o1 sits before aaron-o1** even though Old Man
Logan (2008) overlaps Aaron's start, because Millar's book is one creator's
complete run and reads as a unit; and **hell-o1 sits before xforce-o1** because
Wolverine's own title is the spine of that moment.

**There is one real gap in the shelf, and it is Marvel's, not ours.** Wolverine
(1988) #159–189 has not been collected in omnibus, so `ndy-o1` ends at #158 in
2001 and `millar-o1` opens at Wolverine (2003) #20 in 2004. The Return of Weapon X
Omnibus closes it in June 2027. One issue escapes the gap: **#175**, the
anniversary issue, is in the Jason Aaron volume, so the shelf's actual holes are
#159–174 and #176–189. The note on `ndy-o1` says so on the page. Same shape as
the Hulk shelf's #210–327 gap and the FF shelf's #296–488 one.

**Wolverine #55 was missing until Aug 2026**, exactly like Fantastic Four #171 —
the wiki's page for Wolverine Omnibus Vol. 3 lists it in neither the ReprintOf
fields nor the gallery, though #54 and #56 are both there. It is restored by
hand in `wolverine_contents_raw.json` now, so the chapter reads `#51–59`. What
settled it was the creator credits: #55 is Larry Hama and Marc Silvestri, the
same team as #56 which the volume does hold, and `wolv-o3` is a complete-run
volume rather than a creator selection. Re-apply the fix if this volume is ever
re-pulled.

### Contents, and three data hazards this shelf hit

Pulled the same way as the other three shelves (the `ReprintOf<N>` MediaWiki call
above), into `tools/wolverine_contents_raw.json`. **ReprintOf order matched the
rendered gallery order on all 16 volumes**, so unlike `inc-o1` on the Hulk shelf
nothing needed reordering by hand.

Note that Wolverine Omnibus Vol. 1 genuinely **opens on Weapon X**, not on his
first appearance — Marvel Comics Presents #72–84 comes first and the book then
goes back to Incredible Hulk #180. Both sources agree, and it is not the
group-by-series hazard: Marvel Comics Presents appears in two separate runs in
that volume (#72–84, then #1–10), which a grouped list would never do.

Three entry shapes had to be repaired, and all three break the same thing — the
pipeline splits an issue title on its **last space** to get `<series>` and
`<issue>`, so anything else silently drops out of the shelf:

- **A doubled internal space.** `Havok and Wolverine - Meltdown Vol 1  1` in
  Vol. 2. Every entry is whitespace-collapsed now.
- **Subtitles after the issue number.** `Marvel Graphic Novel Vol 1 65: Wolverine:
  Bloodlust` and two others, exactly as on the FF shelf. Truncated at the first
  colon after the issue number.
- **Short-form entries.** `Uncanny X-Force #5.1` and `#19.1` instead of
  `Uncanny X-Force Vol 1 5.1` — the Hulk shelf's short-form problem again, but
  here only for two point-issues, and resolvable from the 35 long-form siblings
  in the same volume.

If any volume is ever re-pulled, re-apply all three.

One entry is deliberately non-ASCII: `Wolverine Vol 2 ½`. That is the printed
issue number, and the Spider-Man shelf already carries `Ultimate Spider-Man Vol 1
½`. The pure-ASCII rule that used to constrain this was the retired mobile
build's, not a raw-contents one, and it is gone with it.

### Chaptering

Eleven volumes take the automatic per-series chapters. Three carry
`chapterby="series"` because the average-run-length heuristic would have chunked
them into "Part N": `wolv-o5` (3.4), `wolv-o6` (3.1) and `return-o1` (3.05). All
three are ongoing runs with a long tail of one-shots and minis after them rather
than month-by-month crossovers — the same reason five Hulk volumes carry the
override. `return-o1` is the clearest case: as one chapter per mini it reads as
the Hunt for Wolverine tie-in list it actually is.

Two volumes come out as one long non-contiguous span, and both are correct:
`millar-o1` renders Wolverine (2003) `#20–32, #66–72` and `hell-o1` renders
Wolverine (2010) `#1–20, #300–304` across the renumbering. `spanlabel()` is doing
its job — the Straczynski volume on the Spider-Man shelf has the same shape.

### Issue ids and the one overlap

Exactly one issue slot overlaps between volumes: **Wolverine: Road to Hell #1**,
the prologue that both Goes to Hell and Uncanny X-Force collect. It shares its id
across both on purpose, as on every other shelf, and the UI flags it with the
gold "in 2 omnibuses" pill. That is why the shelf reports 636 slots and 635
unique issues.

### Marvel deep links

627 of 636 unique issues (99%) resolve to a real marvel.com issue page; the rest
fall back to `marvel.com/search?query=` and a grey Read button, same convention
as the other trackers. Complete or near-complete: Wolverine (1988) all 189
issues, Marvel Comics Presents all 175, Wolverine (2003), Wolverine (2010),
Wolverine: Weapon X, Uncanny X-Force, Wolverines, Wolverine (2013)/(2014)/(2020),
X-Men: Schism and Wolverine: Infinity Watch.

The 15 that marvel.com does not have: Iron Fist: Wolverine (4), Marvel Graphic
Novel #50/#65/#67, Wolverine #½ and #-1, and one each of Marvel Comic #335, Best
of Marvel Comics, Spider-Man/Punisher/Sabretooth: Designer Genes, the 1992
Marvel Holiday Special, Ghost Rider/Wolverine/Punisher: The Dark Design and a
Wolverine Special.

Two harvests did most of the early work and are worth knowing about:

- **The two big pre-2008 blocks fell to one `scan` each**, because a
  middle-regime block is exactly issue-count long. Wolverine (1988) is 189
  issues at **14036–14224** and Marvel Comics Presents (1988) is 175 at
  **10010–10184**; both were derived in closed form from four already-known ids
  plus the lexicographic ordering, then confirmed by a single sweep with no
  gaps.
- **Everything modern fell to a web search**, after probing and scanning had
  both failed — see "Start with a web search, not with a probe". Nine series ids
  came back in a couple of minutes: Uncanny X-Force **9976**, Wolverines (2015)
  **19794**, Wolverine (2013) **17615**, Wolverine (2014) **18517**, Wolverine
  (2020) **28051**, Death of Wolverine (2014) **19073**, Return of Wolverine
  (2018) **25582**, X-Men: Schism **13880**, Wolverine: Infinity Watch
  **26369**. That took the shelf from 56% to 74% in one pass.

The long tail that used to sit here — 59 series at one or two issues apiece —
was closed by the catalog sweep, not by 59 web searches.

One thing the harvest fixed on the way past: `hulk08-30` had pointed at Hulk
(2008) **#30.1** rather than #30. A `scan` self-identifies a page's own slug, so
it corrected the entry. Worth remembering that a harvest can *change* an
existing link, not only add one — and that a point-issue is the likely reason.

### An unmapped series is derived, not dropped

`gen()` merges `SERIES` with the hero module's own `SERIES_EXTRA`. A series in
neither used to print `!! UNMAPPED` and be **thrown away**, which silently
shortened the shelf — the Wolverine build came out 597 slots instead of 636 that
way, and a from-scratch Avengers shelf would have lost 98% of its issues.

It no longer drops anything. `autocode()` derives a stable id prefix from the
series title and the build lists what it derived:

- one or two words are kept whole (`New Avengers Vol 1` -> `newavengers`),
  three or more become an acronym (`Civil War: The Confession Vol 1` -> `cwtc`),
  and a later volume gets its number appended (`Avengers Vol 3` -> `avengers3`);
- **a code another hero's table already uses is reused verbatim.** The id store
  is shared and keyed by code, so the same comic has to key the same way on
  every shelf. That used to be a rule a human had to remember when repeating an
  entry (the eight at the foot of `wolverine_meta.py`); now it is automatic.

Derivation is deterministic, so a rebuild always produces the same ids and saved
progress keeps working. Pin a code in `SERIES_EXTRA` if you want a shorter or
more conventional one — but do it **before** anyone reads with it, because an
issue id is a saved-progress key.

**One case still needs a person, and the run names it.** When two wiki keys mean
one marvel.com series — the Avengers pages say `X-Men Vol 1` where the FF and
Wolverine modules say `Uncanny X-Men Vol 1` — the two get different codes, and
`link_issues.py` refuses the second with "that series already belongs to another
shelf series" rather than linking both. The fix is one `SERIES_EXTRA` line
giving the new key the existing code.

### What a brand-new hero actually gets

Measured against four real Avengers omnibuses (Vol 1-2, New Avengers Vol 1,
Hickman Vol 1 — 156 unique issues, no `SERIES_EXTRA` written at all):

| | |
|---|---|
| dropped at build | **0** (was 154 of 156) |
| linked automatically | **153 (98%)** |
| ambiguous | 0 |
| flagged for a human | 1 (the `X-Men Vol 1` key above) |
| genuinely not on marvel.com | 2 (an AAFES giveaway, an FCBD issue) |

So the id harvest is no longer a step. What is left for a new hero is the part
that was always judgement: which books belong on the shelf, and hand-designing
the tracker page.

## The Moon Knight tracker (omnibus shelf)

Same code as the other four shelf pages, same tooling, different data: 7
volumes, 260 issue slots, 260 unique issues, all 7 with contents and cover art.
No placeholders, and nothing unreleased. `tools/moonknight_meta.py` is the
hand-written half; run everything with `--hero moon-knight`.

It is the smallest shelf and the only one that is *complete*: the Marvel
Database lists exactly seven Moon Knight omnibuses and all seven are on it.

### Scope call — there wasn't one

Every other shelf needed a judgement call the tools could not make. This one
did not, and that is worth stating rather than leaving implicit:

- **No family character to rule out.** Nothing here is the Moon Knight
  equivalent of She-Hulk or Laura Kinney — no spin-off character has an
  omnibus.
- **No team book to argue about.** Nothing like Marvel Team-Up, Marvel
  Two-In-One or Uncanny X-Force.
- **Nothing unreleased.** The most recent volume shipped October 2024, so the
  "a shelf holds books you can actually buy" rule excludes nothing.

`SHELF` order is a reading order that here is also publication order, so
nothing is resequenced either.

**Two gaps in the shelf are Marvel's, not ours**, and unusually they are in the
middle rather than at the end:

- **Moon Knight (2011) #1–12**, Bendis and Maleev, between the Huston volume
  and From The Dead.
- **Moon Knight (2016) #1–14 and #188–200**, Lemire and then Bemis, between
  From The Dead and the MacKay volume.

Neither has an omnibus. The notes on `ftd-o1` and `mackay-o1` say so on the
page. Note that Lemire's run is the one the old Moon Knight `desc` on the
homescreen was built around when this subject was still going to be a curated
chronology — as an omnibus shelf it cannot be here at all.

### Contents

Pulled the same way as the other four shelves (the `ReprintOf<N>` MediaWiki
call above), into `tools/moonknight_contents_raw.json`. This is the cleanest
pull on the project so far, and the three hazards the other shelves hit did not
appear:

- **ReprintOf order matched the rendered gallery order on all 7 volumes**, so
  nothing needed reordering by hand the way `inc-o1` did.
- **Every page writes the full form** (`Moon Knight Vol 1 1`), so no gallery
  cross-reference was needed to disambiguate — and there are *nine* volumes of
  a series called "Moon Knight" for it to have gone wrong on.
- **No doubled spaces, no subtitles after the issue number, no short-form
  entries.** Nothing had to be repaired, so unlike `ff-o6`, `wolv-o3` and
  `rotm-o1` there is no hand fix to re-apply if a volume is re-pulled.

**The audit found nothing to fix either.** Only one of the seven volumes has an
explicit `COLLECTING` range in its solicit (MacKay's, and it matches the shelf
exactly), so the fallback shelf-wide gap check did the rest. Four gaps, all
correct: Amazing Spider-Man #221–352 and Marvel Age #10–28 and Marvel Fanfare
#31–37 are ordinary guest-appearance spacing, and **Hulk! Magazine #16 and
#19** carry no Moon Knight story at all — the backup serial skipped them, which
the wiki's own character lists confirm.

### Chaptering

Six volumes take the automatic per-series chapters. Only `mk-o2` carries
`chapterby="series"`: it is the tail of the original run (#21–38), the 1985
Fist of Khonshu revival, and then eleven one-shot guest appearances, which
scores 3.27 on the average-run-length test for the same reason the Hulk
anthologies do — and reads far better as one chapter per book than as "Part N".

`mackay-o1` comes out as eight chapters where four of them are all called
"Moon Knight (2021)", which looks wrong and is not: the two annuals and the
Devil's Reign tie-in are printed *inside* the run, so the ongoing genuinely
appears as four separate blocks in print order.

### Issue ids — no overlaps at all

260 issue slots and 260 unique issues: the only shelf where those two numbers
are equal. No volume reprints another's issues, so nothing carries the gold
"in N omnibuses" pill. That is a property of these seven books, not something
to preserve — a future volume that doubles back would share ids as usual.

### Marvel deep links

243 of 260 unique issues (93%) resolve to a real marvel.com issue page; the
rest fall back to `marvel.com/search?query=` and a grey Read button, same
convention as the other four trackers. Complete: Moon Knight (1980) all 38,
Moon Knight (1985), (1999), (2006), (2014) and (2021), Vengeance of the Moon
Knight, Shadowland: Moon Knight, and all three annuals.

**The id harvest was not a step** — the catalog already held everything, so
this was one `link_issues.py --write`. It matched 227 issues with 0 ambiguous
on the first run, which is the "what a brand-new hero actually gets" number
holding up on a real shelf.

One `ALIAS` entry was needed, and the run's own report is what named it:
**Power Man and Iron Fist** is marvel.com's **Power Man (1974 - 1986)** — the
book was retitled at #50 but the catalog keeps one series under the original
name, and the two later series that *do* carry the retitled name stop well
short of #87.

The 17 that marvel.com does not have, all verified against a fully-swept
catalog: **Hulk! Magazine #11–20** (8 issues — a magazine, never digitised,
the same shape as Epic Illustrated on the FF shelf), **Marc Spector: Moon
Knight #52–56 and #58–60** (the catalog holds 52 of that series' 60 issues and
not those), and **Big Shots Spotlight #1**, a 2011 promotional one-shot.

## The Daredevil tracker (omnibus shelf)

Same code as the other five shelf pages, same tooling, different data: 17
volumes, 590 issue slots, 590 unique issues, all 17 with contents and cover art.
No placeholders. `tools/daredevil_meta.py` is the hand-written half; run
everything with `--hero daredevil`.

### Scope call — Matt Murdock's own books

The wiki lists twenty Daredevil-family omnibuses. Seventeen are on the shelf:
Daredevil Omnibus Vol. 1–3, by Miller & Janson, the Frank Miller Omnibus
Companion, by Nocenti & Romita Jr. Vol. 1–2, by Bendis Vol. 1–2, by Brubaker
Vol. 1–2, Shadowland, by Waid Vol. 1–2, by Soule, and by Zdarsky Vol. 1–2.

Three are off, and two of those were the user's call rather than a rule:

- **Elektra by Frank Miller Omnibus** — Elektra's book, not Matt's. The same
  reasoning that keeps She-Hulk off the Hulk shelf and Laura Kinney off
  Wolverine's. It is Elektra: Assassin, Elektra Lives Again, Bizarre Adventures
  #28 and What If #35; Matt is barely in any of it. Note that this is the one
  Miller-adjacent book the Companion does *not* already collect.
- **Devil's Reign Omnibus** — a line-wide event, with X-Men, Winter Soldier,
  Spider-Woman, Superior Four and Villains for Hire tie-ins. Off for the same
  reason Heroes Reborn is off the FF shelf. Nothing is lost by it: its Daredevil
  half (Devil's Reign #1–6, Omega, Woman Without Fear #1–3) is printed inside
  the Zdarsky Vol. 2 omnibus, which is on the shelf.
- **Daredevil Omnibus Vol. 4** is off by the "a shelf holds books you can
  actually buy" rule — it ships **September 2026**, which is next month. Its
  entry stays in `daredevil_contents_raw.json`, so adding it then is an edit to
  `ORDER`/`SHELF` in `daredevil_meta.py` plus a regenerate, not a fresh pull.
  Adding it also means rewording the gap note on `miller-o1`, and bumping the
  Daredevil `total` on the homescreen from 590.

`SHELF` is a reading order, which on this shelf runs with publication order.
The one placement worth stating is that it needed no resequencing: the Miller
Companion collects material dated 1979–1993 but belongs immediately after the
Miller run it comments on, and publication order already puts it there.

**Three gaps in the shelf are Marvel's, not ours**, and unusually the largest
is in the middle rather than at an end:

- **Daredevil #120–157**, closing in September when Vol. 4 ships. The only
  temporary one.
- **Daredevil #192–218 and #220–225** — the Denny O'Neil run between Miller
  and Nocenti. The Companion holds #219 and #226–233, so the hole is either
  side of those.
- **Daredevil #292–380 and Vol. 2 #1–15** — nine years, covering Chichester,
  Kelly and Kesel and then the whole Marvel Knights relaunch by Kevin Smith and
  David Mack. None of it has an omnibus, and it is why `bendis-o1` opens at
  Vol. 2 #16 rather than #1. The notes on `miller-o1`, `nocenti-o1` and
  `bendis-o1` say so on the page.

### Contents

Pulled the same way as the other five shelves (the `ReprintOf<N>` MediaWiki
call above), into `tools/daredevil_contents_raw.json`. Nearly as clean a pull
as Moon Knight's:

- **The ReprintOf order needed no correction on any volume**, unlike `inc-o1`
  on the Hulk shelf. It was checked against the rendered page's own issue
  links; where the two disagreed it was the page carrying an extra link, never
  the fields being grouped by series.
- **Every page writes the full form** (`Daredevil Vol 1 1`), so no gallery
  cross-reference was needed to disambiguate — and there are seven volumes of a
  series called "Daredevil" for it to have gone wrong on.
- **One entry needed the subtitle repair**: `Marvel Graphic Novel Vol 1 24:
  Daredevil: Love and War`, the same shape as three on the FF shelf and three
  on Wolverine's. Truncated at the first colon after the issue number. Re-apply
  it if `millerc-o1` is ever re-pulled.

**The audit found nothing to fix.** Not one of the seventeen volumes carries an
explicit `COLLECTING` range in its solicit — the worst coverage of any shelf,
so that check could not say anything at all here — and the fallback shelf-wide
gap check did the whole job. Five gaps, all correct:

| Gap | Verdict |
|---|---|
| Daredevil #162 | correct — a Ditko fill-in, not Miller & Janson |
| Daredevil Vol. 2 #20–25 | correct — Bob Gale, in a "by Bendis" volume |
| Daredevil Vol. 2 #51–55 | correct — David Mack's Echo, same reason |
| Daredevil Annual #2–3 | correct — 1971 and 1972 all-reprint annuals |
| Marvel Comics Presents #117–122, #131–149 | correct — an anthology; only the Daredevil backups are collected |

One near-miss worth recording: **Daredevil Annual #5 looks like a sixth gap and
is not.** The wiki has no #5 page — it is a redirect to `#4B`, which is what it
calls the 1989 annual whose cover reprints the number 4. Chasing that is also
what turned up the link for it (see below).

A second: the rendered page for `nocenti-o2` links **Marvel Fanfare #45**,
which the ReprintOf fields do not. That is the *cover image credit* ("Reprint
of an image from Marvel Fanfare #45"), not a collected issue — and it is why a
naive "every issue link on the page" cross-check reports a spurious extra on
several volumes.

### Chaptering

Thirteen volumes take the automatic per-series chapters. Four carry
`chapterby="series"` because the average-run-length heuristic would have chunked
them into "Part N": `millerc-o1`, `nocenti-o2`, `shadow-o1` and `zdarsky-o2`.
All four are the anthology shape rather than a month-by-month crossover —
`shadow-o1` is the clearest, landing at 14 chapters that read as the Shadowland
tie-in list it actually is.

`millerc-o1` is worth a look for a different reason: its second chapter renders
as `Daredevil (1964) #219, #226–233`, which is `spanlabel()` correctly refusing
to claim fifteen issues for a non-contiguous run.

### Issue ids — no overlaps at all

590 issue slots and 590 unique issues, the second shelf after Moon Knight where
those two numbers are equal, so nothing carries the gold "in N omnibuses" pill.
That is a consequence of the scope calls rather than of the books: **Devil's
Reign would have overlapped Zdarsky Vol. 2 by ten issues**, and Daredevil
Omnibus Vol. 4 shares #158 with the Miller & Janson volume. Both come back as
overlaps if either book is ever added.

### Marvel deep links

**587 of 590 unique issues (99%) resolve** — the joint-best coverage of any
shelf. The rest fall back to `marvel.com/search?query=` and a grey Read button,
same convention as the other trackers. Complete: all 219 on-shelf issues of
Daredevil (1964), and Daredevil (1998), (2011), (2014), (2015), (2019) and (2022),
every Shadowland and Devil's Reign tie-in, The Man Without Fear, Reborn, and
Woman Without Fear.

**The id harvest was not a step** — the catalog already held everything, so
this was `link_issues.py --write` twice. The second pass is the interesting
part, and worth knowing about because it is not obvious:

**Daredevil (2014) #2–18 came back ambiguous on the first run and resolved on
the second with no code change.** marvel.com has both Daredevil (2011 - 2014)
and Daredevil (2014 - 2015); the volume's era (2013–2015) overlaps each by
exactly two years, so `tiebreak()` genuinely could not choose and reported
rather than guessed. What broke it was writing the run's other results first:
once `dd3` owned the 2011 series, the "two shelf series cannot be one
marvel.com series" rule left one candidate. So **run `--write`, regenerate the
trackers, then run again** — the matcher reads its "what already works" input
out of the tracker HTML, not out of `marvel_ids.json`, so a second pass with no
regenerate in between learns nothing.

Two issues were recovered by the re-test CLAUDE.md asks for rather than
accepted as missing, and both changed the tool rather than the id store:

- **Daredevil (2014) #1.50** is the catalog's `daredevil_2014_1.5`. `numkey()`
  folded `5.0` to `5` but left `1.50` alone, so an exact string compare missed
  a link that was sitting right there. It now normalises any decimal.
- **Daredevil Annual #4B** is marvel.com's Daredevil Annual (1967) **#5** —
  confirmed by its January 1989 publication date and by elimination (the wiki's
  #4 and #6 both take marvel.com's #4 and #6). No rule can derive that, so it
  is the one entry in the new `NUM_ALIAS` table.

The 3 that marvel.com does not have: the 1992 Marvel Holiday Special (already
missing for the Wolverine shelf), Big Shots Spotlight #1 (already missing for
Moon Knight's) and What If Karen Page Had Lived? #1.


## The X-Men tracker (a shelf of books that don't exist)

### What it does

Tracks 174 comic issues across 27 story arcs in a researched chronological
reading order (not publication order), shelved as **four omnibuses Marvel has
never printed**. Per issue you can: mark read, mark skipped, open it on Marvel,
or pull a spoiler summary.

### The four volumes

Marvel has collected almost none of this era and no part of it in omnibus, so
these are mock-ups. The cut points are the only new curation — everything inside
them is the reading order the page already had.

| Vol | Book | Chapters | Issues | Covers |
|---|---|---|---|---|
| 1 | X-Men: Divided We Stand Omnibus | `c-leg1` → `c-unc2` | 38 | the fallout of Messiah Complex, X-Force forming, the move to San Francisco |
| 2 | X-Men: Messiah War Omnibus | `c-cab2` → `c-cab3` | 49 | the road into the middle chapter, the crossover itself, and its aftermath |
| 3 | X-Men: Utopia Omnibus | `c-leg4` → `c-leg5` | 42 | Osborn, the founding of Utopia, Nation X |
| 4 | X-Men: Second Coming Omnibus | `c-nec` → `c-sc` | 45 | Necrosha, Cable and Hope's homecoming, the finale |

**The volume boundaries do not follow the old act boundaries**, and that was
deliberate. Splitting on the six acts gave 66 / 21 / 64 / 23 — two books too fat
to bind and two too thin to call omnibuses. Cutting mid-Act-II and mid-Act-V
instead gives four books of real omnibus size, and each still has one clean
identity. The acts are gone as a structure; their titles survive in the volume
names.

The trilogy framing is why there are four books rather than three: Messiah
Complex itself is *not* on this shelf. The read opens with X-Men Legacy #208,
which resolves Xavier's head wound from Complex's last pages — so the shelf is
the trilogy's second and third chapters plus everything between and around them.

### Architecture

All inside the single `<script>` block, in this order:

1. `SC` — series → cover gradient colors
2. `seq()` — helper that generates runs of consecutive issues
3. `OMNI` — **the master data structure.** Array of 4 volumes → `chapters` →
   `issues`. A volume has `{id, spine, title, vol, creators, era, art, tex,
   note, chapters[]}` — the same shape the generated shelves use, minus
   `released` and `cover`, neither of which means anything for an unprinted
   book. Each chapter has `{id, title, era, tier, note, issues[]}`; each issue
   `{id, t (title), s (series), arc, key?}`.
   `tier` 1 = core saga, 2 = main X-line, 3 = optional (hidden by the
   "Hide optional arcs" toggle via `body.hideopt`, which lives in the volume
   view's controls).
4. `MARVEL` — map of internal issue id → `marvelID/slug` path fragment
5. `ARC_SUMS` — 27 hand-written, pre-loaded spoiler digests keyed by chapter id
6. Storage layer, shelf render, volume render, interaction, summaries, refresh

`flat[]` is the flattened `{o, ch, issue}` list driving Keep Reading and all
progress math. No issue is collected twice here, so slots and unique ids are the
same 174 and there is no `dupCount` / "in N omnibuses" pill as on the real
shelves.

**This page is not in the build pipeline and must not be added to it.**
`build_omnibus_data.py`, `heroes.py` and `fetch_covers.py` all key off a wiki
page title, and there is no wiki page for a book that was never printed. Edit
`OMNI` in the HTML directly — it is the only shelf where that is the right move.

Three things the shelf conversion kept that no other shelf has, all worth not
losing: the per-chapter placement `note` (rendered above the issue rows), the
`tier` system and its toggle, and `ARC_SUMS` as an offline first tier in
`doArcSummary`.

#### Storage (dual-mode)

`IN_CLAUDE` detects whether `window.storage` exists.
- Inside Claude → `window.storage`
- In a normal browser → `localStorage`

The `store` object abstracts both. Keys:
- `xmen-saga-progress-v2` → `{read:[ids], skip:[ids]}`
- `xmen-saga-summaries-v3` → cached generated summaries
- `comics-anthropic-key` → the user's own API key, **shared with every other
  tracker** and set from the homescreen gear (browser mode only). Migrated
  from the page-local `xmen-anthropic-key` on first read
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
- **Per-issue**: live call to `api.anthropic.com` (`claude-opus-5`,
  `output_config.effort: "low"`) with the `web_search_20260209` tool enabled.
  In-browser it needs the user's own key via `x-api-key` +
  `anthropic-dangerous-direct-browser-access: true`; the key comes from the
  homescreen gear. Inside Claude the key check is skipped entirely.

The same engine — `askClaude`, `tidy`, `summaryError`, the panel helpers — is
**copied into every tracker**, not shared through a file. That is the
portability rule: every page stands alone. Change one and change the others.

`tidy()` sanitizes model output — strips markdown, leading process narration
("I found…", "Let me…"), bullets, trailing source lists, and collapses to at
most two paragraphs. **Don't remove it**; prompt instructions alone did not
reliably suppress that formatting.

`summaryError()` maps error codes (`nokey`, `badkey`, `http`) to useful messages.

### Design

Dark blue-black, streaming-service shaped: a flat near-black page, a full-bleed
banner fading into it, a Keep Reading rail of wide tiles, then the shelf. CSS
variables at `:root`. Respects `prefers-reduced-motion`. Mobile breakpoint at
600px. This is the same look every page uses — see "The dark chrome" near the
top of this file.

It was Frutiger Aero until Aug 2026 — sky-blue gradients, glass panels, glossy
orbs, floating bubbles — and the book tiles, the cover ramps and the gold accent
are what is left of it.

### Cover art for books with no covers

All four volumes carry real art in `Art/X-Men/<id>.jpg`, sized through the same
`covers.save_cover` 700px/q82 pipeline as every other shelf. Since the books
were never printed there is no jacket to scan, so **each volume takes the cover
of the issue it is named after** — which is chapter 1 of that book's centrepiece
in three cases out of four.

`fetch_covers.py` cannot do this: it maps a volume id to a wiki page through the
hero's `ORDER` keys, and there is no page for an unprinted book. `tools/fetch_xmen_covers.py`
is the replacement, and its `PICKS` table holds the choice and the reasoning for
each, the way `PICKS` in `fetch_hero_art.py` does for the homescreen posters.

Two things that table records and that are worth not relearning:

- **Take whichever variant the wiki stores larger, and check what the scan
  actually is.** Three of the four picks are printed covers rather than textless
  variants, purely because the textless files are 400–550px where the printed
  ones are 1280px+. But Utopia's *main* cover is only on the wiki as a 2063px
  scan of the whole printed page — white border, copyright line, marvel.com
  footer — which reads as a photocopy on a book jacket. Bianchi's variant at
  853px is art and nothing else, and is the pick.
- **This is the opposite of the homescreen's rule** (see "Artwork"), where trade
  dress fights the poster plate. These tiles are supposed to read as real books,
  and every other shelf on the site shows a printed cover with its logo on it.

`pos` on a volume sets `object-position` on the **banner only**, exactly as on
the homescreen — the tile is the same 2:3 as the cover and crops almost nothing,
but the banner is a thin band cut out of it. Only `xm-o1` needs one (`18%`,
which lands the band on two faces instead of the abstract shards at the centre).
Retuning one means screenshotting `#obanner` and looking, not reasoning about it.

Behind the scans, each volume still declares an `.o-*` ramp, a texture and the
inline X glyph, which `artHTML()` paints when a cover is missing or fails to
load. Two things about that fallback took a second pass when it *was* the
cover, and are worth keeping if it ever is again:

- **The ramps are darker than the other shelves'.** Copying their near-white top
  stop put a white X on a white cover. Those shelves get away with it because
  the ramp is only ever a fallback there.
- **The X has more body than the other glyphs.** It is a large solid shape, so
  the fade-to-transparent gradient the crescent and claw glyphs use made its
  lower half vanish. Its stops bottom out at .48, not .18.

### Known gaps / open items

1. ~~30 of 174 issues lack Marvel deep links.~~ **Done Aug 2026 — all 174
   resolve**, the only shelf on the project at 100%. It cost one pass over
   `tools/marvel_catalog.json`, which is the point worth keeping: the long tail
   here was never hard, it was just never looked at with the catalog in hand.

   The 30 were the one-shots and minis the old marvel.com id crawl never probed
   — Lucas Bishop, the Messiah War and Utopia one-shots, Necrosha, Hellbound,
   Blind Science, Second Coming #1–2, New Mutants, Sex and Violence, King-Size
   Cable and the two Dark Avengers chapters. Twenty-nine fell out of a single
   regex sweep of the catalog's slugs; only the Utopia one-shot needed a second
   look, and only because marvel.com strips the slash out of a co-titled book
   (`dark_avengersuncanny_x-men_utopia_1_2009_1`).

   Every id was checked against the catalog before it was written, so the
   entries are Marvel's own id↔slug pairs rather than guesses. Note a live
   `curl` of those URLs answers 403 from this environment — that is marvel.com
   rate-limiting a bot, not a bad link, and it is not evidence either way.

   `MARVEL-IDS.md` still describes the old crawl. It is history now; the catalog
   is the route.
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
- Adding a chapter: it goes inside one volume's `chapters[]`, and it also needs
  an `ARC_SUMS[chapterId]` entry, or the arc button falls through to a live web
  lookup.
- Moving a chapter between volumes is free — progress is keyed by issue id, not
  by where the issue sits. Renaming a **volume** id (`xm-o1`…) only breaks
  bookmarked `#/omni/<id>` links.

## The mobile build is retired (Aug 2026)

`comics-mobile.html` and `tools/build_single_file.py` are **deleted**. Do not
recreate them.

The file composed all seven pages into one hash-routed document, and it existed
for exactly one reason: a Claude Artifact is one file per URL, so publishing the
site as an artifact meant publishing it as a single file. That artifact was
retired earlier in Aug 2026 (see below), which left the build generating a
second copy of a site that GitHub Pages was already serving page by page —
another surface to keep in sync, its own `localStorage` origin, and roughly a
thousand lines of scoping machinery to stop the composed pages colliding.

Pages was always the phone story anyway. `index.html` and every tracker are
responsive with a 600px breakpoint; the homescreen renders as a two-column
poster grid at 390px with no horizontal scroll. Nothing linked to
`comics-mobile.html` from any page, so removing it broke no navigation.

What went with it, so nobody reintroduces a constraint that no longer exists:

- **The pure-ASCII rule.** The artifact wrapper owned `<head>`, so the composed
  page carried no `<meta charset>` and had to be emitted as pure ASCII. Source
  pages declare their own charset; en-dashes and `½` are fine.
- **The 16MB ceiling**, and with it the last argument against a large cover
  scan. See "Cover art".
- **The three artifact workarounds** the builder still applied to a page nobody
  published as an artifact: forcing every tracker onto its "no key" summary
  path (rewriting `if(!IN_CLAUDE){` to `if(true){` in `askClaude`), hiding the
  homescreen gear, and rewiring the Back up button to `window.__COMICS_SAVE()`
  because `<a download>` was inert in the viewer. That was open item 10; it is
  closed by deletion. The standalone pages never had any of it — live summaries
  and the download link work on Pages.
- **`panel`, `pfx` and `route` in `heroes.py`.** Only the builder read them.

Two bugs it found are worth keeping, because both are the same shape and the
shape recurs anywhere ids get rewritten: scoping *one half* of an id pair is
worse than scoping neither, because it fails silently. Prefixing `#storeWarn`
in the markup but not in the CSS that hid it shipped a permanent "Progress
isn't saving" banner over a working `localStorage`; renaming
`<linearGradient id="hg">` but not `fill="url(#hg)"` made every HUD emblem draw
as a bare orb, since an unresolvable paint server renders as *no paint*.


### Progress does not sync

`localStorage` is per-origin **and per-device**. GitHub Pages and the local
`file://` copies each keep their own progress; nothing syncs between phone and
laptop. Export/import JSON is the manual bridge. Real sync would need
a server-side store and is not built.

## Open items — C.O.M.I.C.S.

1. ~~One of seven subjects has no reading list yet.~~ **Done Aug 2026** — all
   seven subjects now have one, Daredevil having shipped as the sixth omnibus
   shelf. Both of the last two shipped that way rather than as curated
   chronologies, and both **dropped part of their old `HEROES` brief on
   purpose**: Moon Knight's because Lemire's run has no omnibus, Daredevil's
   because "arranged so each run answers the one before it" describes a curated
   read, and an omnibus shelf reproduces the printed books instead. A `desc`
   written while a subject was still "Curating" is a brief, not a spec — expect
   to rewrite it when the shape is decided.
2. **`total` for a new hero is a hardcoded fallback.** It is only used before
   that tracker has ever been opened; after that the published record wins. Keep
   them in sync anyway, or a first visit reports the wrong percentage.
3. **Thirty-one covers are low-res** (~225–450px wide) because that is all the
   Marvel Database stores — six on the Spider-Man shelf, six on the Hulk shelf,
   eight on the Fantastic Four shelf, two on the Wolverine shelf (`aaron-o1`,
   `xforce-o1`), two on the Moon Knight shelf (`spector-o1`, `huston-o1`) and
   seven on the Daredevil shelf (`bendis-o1`, `bendis-o2`, `bru-o1`, `bru-o2`,
   `shadow-o1`, `waid-o2`, `soule-o1`); see "Cover art". Replacing them needs a
   scan from somewhere else; everything else is 600–700px. Daredevil is the
   worst-served shelf — four of its seven are 225–334px, the smallest originals
   on the project. Now that the artifact is retired **and the covers are no
   longer inlined**, there is no size budget at all arguing against a big scan.
4. **Three wiki omissions were found and fixed in Aug 2026** — Fantastic Four
   #171, Wolverine #55, and Incredible Hulk (2000) #75–76 — all restored by
   hand in their raw-contents files. **A re-pull of `ff-o6`, `wolv-o3` or
   `rotm-o1` will reintroduce all of them**, the same way re-pulling `inc-o1`
   reintroduces its ordering bug. The audit that found them, and what it can and
   cannot cover, is written up under "Auditing contents against the solicit".
5. **The `Part N` chapter labels on the interleaved volumes are generic.** Real
   arc names (Power and Responsibility, The Exile Returns, Maximum Clonage)
   would be a genuine improvement — see "Chaptering".
6. ~~The Straczynski volume has almost no Marvel deep links.~~ **Done Aug
   2026** — all 47 issues resolve. Web-searched the series id (454), pulled a
   seed, walked from #36 at id 42508.
7. ~~Hulk (2008) #1–29 is the biggest link gap on the Hulk shelf.~~ **Done Aug
   2026** — all 24 on-shelf issues resolve, walked from #1 at id 17623, found by
   web search after the series page dead-ended at #38.
8. **The Hulk shelf still carries an unreleased volume.** Incredible Hulk
   Omnibus Vol. 4 (`inc-o4`) is solicited for February 2027 and sits on the
   shelf with an "Announced" badge, which is exactly what "A shelf holds books
   you can actually buy" now forbids. It predates the rule and has not been
   removed yet; doing so means dropping it from `ORDER` and `SHELF` in
   `hulk_meta.py`, rewording `pad-o1`'s note about the #210–327 gap (which gets
   bigger), and updating the Hulk `total` on the homescreen.
9. ~~Astonishing Tales (1970) is 15 issues short on the Fantastic Four shelf.~~
   **Settled Aug 2026** — the full catalog holds 21 of its 36 issues, so the
   other 15 were pulled from marvel.com rather than missed by a harvest. Only
   #7 is still on the shelf unlinked.
10. ~~The mobile build applies artifact workarounds to a page nobody publishes
    as an artifact.~~ **Closed Aug 2026 by deleting the build.** Both halves
    went at once: the cover inlining came off when six shelves of it projected
    past the 16MB ceiling, and the rest — the disabled live summaries, the
    hidden homescreen gear, the ASCII pass — went with `comics-mobile.html`
    itself. See "The mobile build is retired".
11. ~~Deep links are a long tail on every shelf.~~ **Done Aug 2026** — the six
    shelves are at 93–99% (Spider-Man 600/606, Hulk 652/659, Fantastic Four
    644/661, Wolverine 629/636, Moon Knight 243/260, Daredevil 587/590). The
    remaining 56 are not on marvel.com at all;
    `tools/unlinked.json` names every one. What closed it was sweeping
    marvel.com's open JSON catalog rather than searching per series — see
    "Linking issues" and "How the links used to be missed". The last nine came
    from a naming pass prompted by the user finding one by hand, so a fresh
    `--dump` list is a hypothesis, not a verdict: re-test it before believing
    marvel.com lacks something. The Daredevil shelf proved that again — two of
    its five "missing" issues were in the catalog under a different number, and
    both fixes went into `link_issues.py` rather than into the id store. And
    again in Aug 2026: filling in Spider-Man vs. Venom put a fifth Marvel
    Graphic Novel on the "missing" list, and re-testing that one found four of
    the five in the catalog, filed under their story titles rather than the MGN
    line — see `ISSUE_ALIAS` under "Linking issues". The X-Men shelf closed its
    own 30 the same way in Aug 2026 and sits at 174/174, the only shelf at 100%
    — see item 12 for why no tool did it.
12. **X-Men is still the one subject `link_issues.py` cannot see** — it walks
    the heroes registered in `heroes.py`, and X-Men is deliberately not one of
    them. That no longer costs anything: its 30 missing links were closed by
    hand against `marvel_catalog.json` in Aug 2026 and the shelf is at 174/174.
    But the next issue added to that page will not be linked by any tool, and
    `link_issues.py`'s report will not mention it. The fix, if it ever matters,
    is teaching the matcher to read a hand-written shelf.

    Note the X-Men page's `MARVEL` map is **its own**, not `tools/marvel_ids.json`.
    Nothing was added to the shared store, deliberately: its keys are issue ids,
    and short ones like `nm-6` would collide with another shelf's.
13. **The X-Men shelf's four books do not exist**, which is the point, but it
    means the "a shelf holds books you can actually buy" rule now has an
    exception on the wall — and since the tiles gained real cover art and lost
    the "Never printed" badge, they look entirely like books you could buy.
    Three signals carry it now: the bold note above the shelf, "0 in print" in
    the shelf count, and "never printed" in each volume's banner. That is the
    floor, and preserving it is the thing to watch if the shelf is ever edited —
    see "A shelf holds books you can actually buy".
14. **The homescreen banner is the one image still missing.** All seven subject
    banners are in; `Art/Banners/index.jpg` is not, so the homescreen runs on
    its fallback — the seven posters in a row behind the scrim. That reads as a
    deliberate collage rather than a hole, so this is a want, not a bug.
    Two of the seven that are in are under-size and `banners.py audit` flags
    them `soft`: `wolverine.jpg` (1199px) and `moon-knight.jpg` (1200px) against
    1800px for the rest.
15. **A Keep Reading tile credits the volume, not the issue.** `creators` on an
    omnibus is usually exactly the writer and penciler of what it collects, so
    the line is right far more often than not — but on an anthology volume
    ("David Michelinie & various") it is vague, and on a mainline numbered
    volume it names the run's headline team rather than whoever drew that
    issue. The fix is per-issue credits in the raw-contents pull, which is a
    wiki request per issue across 3,412 issues and a real size increase in every
    tracker. Not attempted; the tile says what the data can support.
16. **The tile's bar measures the volume, not the issue.** The user asked for a
    per-issue progress bar, in the streaming sense of "you are 40% through this
    episode". Nothing in this project knows that — an issue is read, skipped or
    neither — so the bar is progress through the volume the next issue sits in
    and the caption is a position ("Issue 12 of 43"). Making it literal would
    mean tracking a page or a percentage per issue, which is a new interaction,
    not a new field.
17. **The Daredevil shelf is missing Daredevil Omnibus Vol. 4 for one month.**
    It ships September 2026 and is excluded by the "a shelf holds books you can
    actually buy" rule, which leaves a #120–157 hole between `dd-o3` and
    `miller-o1`. Adding it is a `daredevil_meta.py` edit plus a regenerate (the
    contents are already in the raw file), rewording `miller-o1`'s gap note,
    and bumping the Daredevil `total` on the homescreen from 590. Note it also
    reintroduces the shelf's first issue overlap — #158 is in both books.

## Testing

No test suite. Note that `file://` pages render as `data:` URLs in some preview
tools, where `localStorage` throws and relative links don't resolve — serve the
folder over HTTP (`python3 -m http.server`) to exercise navigation and progress
for real.

Verify changes with:

```bash
# JS syntax. Note a tracker has ONE <script> but index.html has several --
# concatenating only the first checks almost nothing there, so join them all.
node -e "const fs=require('fs');const p=fs.readFileSync('index.html','utf8').split('<script>');
  let js='';for(let i=1;i<p.length;i++)js+='\n;{\n'+p[i].split('<\/script>')[0]+'\n}\n';
  fs.writeFileSync('/tmp/v.js',js)"
node --check /tmp/v.js

# Shelf data round-trips (also checks SHELF/SPINE_C consistency)
python3 tools/build_omnibus_data.py --check
python3 tools/build_omnibus_data.py --check --hero hulk
python3 tools/build_omnibus_data.py --check --hero fantastic-four
python3 tools/build_omnibus_data.py --check --hero wolverine
python3 tools/build_omnibus_data.py --check --hero moon-knight
python3 tools/build_omnibus_data.py --check --hero daredevil

# Every shelf issue that can be linked, is.
# Expect: 0 matched, 0 ambiguous, and one standing rejection (tta3-1, which is
# deliberate -- see "An unmapped series is derived, not dropped").
python3 tools/link_issues.py

# Homescreen logos (every subject has one, and every one has an alpha channel)
python3 tools/logos.py audit

# Banner art (which of the eight are in, and how big)
python3 tools/banners.py audit

# Nothing on any page still draws a completion figure. Expect no matches:
# the HUD, the Up Next bar, the bubbles and .pbar were all deleted in Aug 2026.
grep -l 'class="hud"\|class="upnext"\|class="pbar"\|class="bubble"' *.html

# Cover art (every volume has one, and how heavy it is)
python3 tools/covers.py audit
python3 tools/covers.py audit --hero hulk
python3 tools/covers.py audit --hero fantastic-four
python3 tools/covers.py audit --hero wolverine
python3 tools/covers.py audit --hero moon-knight
python3 tools/covers.py audit --hero daredevil

# Data integrity (counts, duplicate ids, ARC_SUMS coverage) — see git history
# or re-derive: eval the data section and assert every chapter has a digest.

# The X-Men shelf has no build step to check it, so check the data by hand:
# 4 volumes / 174 issues / 0 unlinked / 27 chapters, all with an ARC_SUMS entry.
node -e 'const js=require("fs").readFileSync("xmen-reading-tracker.html","utf8")
  .split("<script>")[1].split("<\/script>")[0];
  const R=new Function(js.slice(0,js.indexOf("function marvelURL"))+"return{OMNI,MARVEL};")();
  const ch=R.OMNI.flatMap(o=>o.chapters), is=ch.flatMap(c=>c.issues);
  console.log(R.OMNI.length,"volumes",is.length,"issues",
    is.filter(i=>!R.MARVEL[i.id]).length,"unlinked",
    new Set(is.map(i=>i.id)).size,"unique ids")'
```

The Spider-Man shelf currently reports **16 volumes / 617 issue slots / 606
unique issues**; the Hulk shelf **17 volumes / 665 issue slots / 659 unique
issues**; the Fantastic Four shelf **18 volumes / 686 issue slots / 661 unique
issues**; the Wolverine shelf **14 volumes / 637 issue slots / 636 unique
issues**; the Moon Knight shelf **7 volumes / 260 issue slots / 260 unique
issues**; the Daredevil shelf **17 volumes / 590 issue slots / 590 unique
issues**; the X-Men shelf **4 volumes / 174 issue slots / 174 unique issues**.
If a change moves those numbers without meaning to, something is wrong.

For the look of a page, screenshot it rather than reasoning about it. Chromium
is preinstalled at `/opt/pw-browsers/chromium`; `pip install playwright` and
point `chromium.launch(executable_path=...)` at it, against a local
`python3 -m http.server`. That is what caught the Daredevil page still carrying
the Moon Knight subtitle in its shelf view — a string the identity sweep had
replaced in the markup but not in the `showShelf()` line that overwrites it.

The Keep Reading rail is worth driving rather than looking at, because most of
it only exists once something is marked: open a volume, tick three issues, go
back to the shelf and click the tile, and check that it opens the chapter and
flashes the row. Then load `index.html` and check the same volume is the first
tile there. A `pageerror` listener on the page catches the rest — the whole
rail is built in one `innerHTML`, so a bad field is a silent empty band, not a
stack trace in the console.

For behavior, `jsdom` with `runScripts:'dangerously'` and no `window.storage`
simulates plain-browser mode accurately — that's how the localStorage fallback
and the no-key summary path were verified.

## Working on this (GitHub is the source of truth)

The canonical copy lives on GitHub. Local clones are disposable; do not treat a
folder on one machine as the real project.

    git pull                              # before touching anything
    …edit…
    python3 tools/build_omnibus_data.py   # if tools/omnibus_meta.py changed
    git add -A && git commit && git push

Then publish — a push alone changes nothing anyone can see. See "Seeing a
change" below.

### Shelf work ships itself — do not wait to be asked

**Adding or changing an omnibus shelf is pre-authorised end to end: build it,
commit it, push it, open the PR, and merge it to `main`.** Do not stop to ask
for a review pass; the user has said this process does not need one. Merging is
the step that actually publishes anything (see "Seeing a change"), so a job that
stops at a pushed branch is not finished — the work is invisible to everyone,
including the person who asked for it.

That covers the whole routine pipeline: standing up a new hero's shelf, adding
or dropping a volume, re-pulling contents, refreshing covers, harvesting ids,
and the regenerate that follows any of them. Report what shipped
afterwards rather than asking first.

Two things are still worth asking about, because they are judgement calls the
tools cannot make:

- **Which books belong on a shelf.** The scope calls on every shelf so far were
  the user's, not a default — see "Scope call" in each tracker's section.
- **Anything that would destroy saved progress**, such as renaming an issue id
  or bumping a storage-key version. Those are irreversible for whoever has been
  reading.

**There is no build step for a page.** GitHub Pages serves the repo root and
runs nothing, so editing a page and committing it is the whole job. The one
generated thing left is a shelf's `OMNI`/`MARVEL` data inside a tracker —
regenerate that in the same commit as the `tools/<hero>_meta.py` change.

### Two published surfaces, two separate progress stores

| Surface | URL | Progress lives in |
|---|---|---|
| GitHub Pages | `https://nightowl952.github.io/COMICS/` | that origin's `localStorage` |
| Local `file://` | the clone | that browser's `localStorage` |

They do not sync — see "Progress does not sync". Export/import JSON is the
bridge. Publishing a new version does not disturb progress already saved there,
because progress is never in the HTML.

**Cross-device sync is wanted and not built.** Retiring the artifact made it
easier rather than harder: Pages puts no restriction on outbound requests, so
the realistic shape is now the only shape — a store reachable from the page (a
private Gist keyed by a token the user pastes in, mirroring the existing
`comics-anthropic-key` pattern). What made this awkward before was the
artifact, which blocked *every* external request and so could never have shared
one mechanism with Pages.

### Seeing a change — nothing publishes itself

**No surface updates from a `git push`.** Merging to `main` updates Pages, and
since the artifact was retired that is the only publishing step there is.
Forgetting it is still the most common way a change looks "broken" when it is
merely unpublished.

| To see it on | Do this | Lag |
|---|---|---|
| GitHub Pages | merge to `main` — do this yourself, see "Shelf work ships itself" | ~1 min, then hard-refresh |
| Local | `python3 -m http.server`, not `file://` | — |

Pages serves the repo root of `main`, so a change sitting on a branch — even a
pushed branch with an open PR — is not visible anywhere. There is no preview
URL for a branch. Confirm a Pages deploy actually landed rather than assuming:

```bash
curl -s https://nightowl952.github.io/COMICS/spiderman-reading-tracker.html \
  | grep -c bookThickness        # some string only the new version has
```

It returns 0 for a minute or so after the merge while Pages rebuilds. Browsers
cache these pages hard, so hard-refresh before believing a stale render.

`Art/` is committed, so cover images serve from Pages at their relative path —
spaces in filenames get URL-encoded by the browser and work fine.

### The Claude Artifact is retired (Aug 2026)

The site was also published as a Claude Artifact
(`https://claude.ai/code/artifact/a339fcf9-afeb-413c-880c-a4b1aa6b0f81`) until
August 2026. **It is no longer maintained — do not republish it.** GitHub Pages
is the published surface.

The URL is kept here only so a future session recognises it instead of treating
it as a surface that has silently fallen behind. Anyone still holding that link
is looking at a frozen copy with three shelves and no Wolverine.

What retiring it changes, and what it does not:

- **The 16MB ceiling stopped mattering.** That was an artifact limit, never a
  GitHub one —
  Pages serves individual files up to 100MB and a site up to 1GB, and this repo
  is 19MB in total. Cover art no longer has to be squeezed to fit. `covers.py
  add` still re-encodes to 700px/q82, because consistency across six shelves is
  worth more than sharpness on one, but that is now a choice rather than a
  constraint, and a better scan can simply be dropped in.
- **Relative image paths work.** `Art/…` resolves fine from Pages, which is why
  every cover is a path rather than a base64 data URI.
- **It took `comics-mobile.html` down with it, eventually.** That file existed
  only because an artifact is one file per URL. It outlived the artifact by a
  few weeks and was deleted in the same month — see "The mobile build is
  retired". Pages serves the seven pages directly and they are responsive, so
  nothing replaced it.
