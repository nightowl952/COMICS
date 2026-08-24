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
- `captainamerica-reading-tracker.html` — the Captain America omnibus shelf.
  Same shape and tooling again (`--hero captain-america`); 22 volumes, the
  biggest shelf on the site. Its `OMNI` array is generated from
  `tools/captainamerica_meta.py`.
- `ironman-reading-tracker.html` — the Iron Man omnibus shelf. Same shape and
  tooling again (`--hero iron-man`); 9 volumes, which is *every* Iron Man
  omnibus in print. Its `OMNI` array is generated from `tools/ironman_meta.py`.
- `silversurfer-reading-tracker.html` — the Silver Surfer omnibus shelf. Same
  shape and tooling again (`--hero silver-surfer`); 4 volumes, the smallest
  shelf on the site. Its `OMNI` array is generated from
  `tools/silversurfer_meta.py`.
- `blackpanther-reading-tracker.html` — the Black Panther omnibus shelf. Same
  shape and tooling again (`--hero black-panther`); 7 volumes, and the first
  row-three placeholder to be curated. Its `OMNI` array is generated from
  `tools/blackpanther_meta.py`.
- `ghostrider-reading-tracker.html` — the Ghost Rider omnibus shelf. Same shape
  and tooling again (`--hero ghost-rider`); 7 volumes, and the second row-three
  placeholder to be curated. Its `OMNI` array is generated from
  `tools/ghostrider_meta.py`. It is the only shelf that does not open on its own
  title character — Johnny Blaze's 1972 run has never been collected in
  omnibus, so it starts in 1990 with Danny Ketch.
- `Art/Spider-Man/`, `Art/Hulk/`, `Art/Fantastic-Four/`, `Art/Wolverine/`,
  `Art/Moon-Knight/`, `Art/Daredevil/`, `Art/Silver-Surfer/`,
  `Art/Captain-America/`, `Art/Iron-Man/`, `Art/Black-Panther/`,
  `Art/Ghost-Rider/`, `Art/X-Men/` — cover scans, committed so
  GitHub Pages can serve them. Every page references them by relative path.
  `Art/X-Men/` is the odd one: its four books were never printed, so each file is
  the cover of the issue that volume is named after — see "Cover art for books
  with no covers".
- `Art/Heroes/` — one cover per homescreen subject, fifteen files named by hero
  id (the last five are the row-three placeholders).
  See "Artwork" below.
- `Art/Banners/` — the wide above-the-fold art, eleven files: `index.jpg` for the
  homescreen and `<hero id>.jpg` for ten of the twelve subjects that have a
  shelf. **Black Panther and Ghost Rider are the exceptions, and they are the
  two that actually cost something** — both have a tracker page and no banner,
  so each one's `hbFallback()` degrades to the poster scan. The other three
  row-three placeholders have none and do not need one until they get a tracker
  page. Hand-picked, never
  fetched; `tools/banners.py` normalises them. A missing one is not a broken
  page — see "The banner" below.
- `Art/covers/` — the original hand-supplied scans the `Art/Heroes/`
  files were derived from, at full size. Nothing reads this folder; it is kept
  so a poster can be re-cropped without re-sourcing the art, and since Aug 2026
  it is also the **drop box the user delivers new poster art into** — see
  "Artwork the user supplies" below.
- `Art/Logos/` — one printed logo per homescreen subject, fifteen of them,
  `<hero id>.png`,
  cropped to its artwork and alpha-backed. See "The plate" below. The
  source-named originals the user supplied are not kept; git history has them.

No build step, no package.json, no dependencies, no server. Open any of these
files directly in a browser.

Every file is individually self-contained (data, styles, logic, artwork) on
purpose. Keep it that way — portability is the point. The only thing that crosses
a file boundary is the small storage record described under "Homescreen" below.

## One tracker shape, two ways of filling it

**All twelve subjects are omnibus shelves** (Aug 2026): a shelf of volumes
rendered as CSS-3D hardcover books, each opening into its own chapter list. Two
views in one file, hash-routed (`#/omni/<id>`). What differs is where a shelf's
data comes from:

- **Wiki-backed** (Spider-Man, Hulk, Fantastic Four, Wolverine, Moon Knight,
  Daredevil, Silver Surfer, Captain America, Iron Man, Black Panther, Ghost
  Rider) — each
  volume reproduces exactly
  what the printed book collects, in
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

### A shelf holds books whose tile is finished

**The rule changed in Aug 2026, at the user's request.** It used to be "never
put an unreleased omnibus on a shelf". It is now about the *tile*, not the
date:

> An omnibus goes on the shelf when all three of the things a tile is made of
> are real — its **contents**, its **deep links** and its **cover**. A book that
> has not shipped yet passes if it can satisfy all three. A book that cannot is
> off, whether or not it is in print.

The reason for the old rule was never the release date; it was that a solicited
book usually has no cover scan and often no confirmed issue list, so it lands on
the shelf as a grey box with "not added yet" where the issue count goes. That is
the thing to avoid. Once the contents are pulled, every issue resolves to
marvel.com and a real jacket exists, an unshipped tile is indistinguishable from
a shipped one except for its badge — and it is genuinely useful, because it
closes a gap the reader would otherwise take for a missing run.

**Check all three before adding one, and in this order** — each is cheaper than
the next and any one of them can veto:

1. **Contents.** The wiki page's `ReprintOf<N>` fields have to be filled in.
   A solicited book often has only a `Solicit` blurb; if there are no ReprintOf
   fields there is no issue list, and it does not go on.
2. **Links.** Run `link_issues.py` and read its report. Older material is
   normally fine — the catalog holds the issues whatever the collection's date
   — but a volume of brand-new comics may not be in the sweep yet.
3. **Cover.** This is the one that actually fails, because the wiki has no
   jacket scan until the book is out. See below.

**The cover is the hard gate, and `fetch_covers.py` will lie to you about it.**
An unreleased volume's wiki page declares its jacket as `Image1`/`Image2` rather
than `Image`, and both are usually redlinks — the files do not exist. But
`prop=pageimages` still answers, with **the first image in the reprint gallery**,
which is a random collected issue's cover. On Silver Surfer: The Infinity
Gauntlet Omnibus that was Infinity Gauntlet #2. It looks like a successful
fetch and it is the wrong book.

So for an unreleased volume: fetch the jacket by hand and add it with
`covers.py add <id> <file> --hero <key>`, and afterwards **never run
`fetch_covers.py --all` on that shelf**, which would overwrite it with the
gallery image again.

**A shipped book is not safe from this either**, which the Captain America and
Iron Man shelves both proved: six Captain America pages and two Iron Man ones
point their infobox at a collected issue's scan rather than at a jacket, and
`prop=pageimages` answers with it. On Iron Man the giveaway was visible only by
looking — a 12¢ price box and a Comics Code stamp on what was supposed to be a
2008 hardcover. **Put every fetched shelf on a contact sheet and look at it**
before believing "9 fetched, 0 failed"; the tool cannot tell a jacket from the
comic inside it.

Where the jacket actually is, in the order worth trying:

| Source | What you get |
|---|---|
| `images3.penguinrandomhouse.com/cover/<isbn13>` | the flat jacket, ~306x450 |
| `images-na.ssl-images-amazon.com/images/P/<isbn10>.01._SCLZZZZZZZ_.jpg` | the flat jacket, ~340x500 |
| a comic retailer's product photo | often a **3D angled mock-up on white** — unusable |
| a retailer's "cover art" image | often the **source issue's** cover, price box and all — wrong |

Both flat sources are small enough that `covers.py audit` flags them `soft`.
That is acceptable; a soft-but-correct jacket beats no tile. Replace it with the
wiki's scan once the book ships.

**The badge retires itself.** `shipsLater(o)` in every shelf tracker reads
`released` — either the literal `"Announced"` or a `"Mon YYYY"` date — and puts
an amber `Ships Nov 2026` pill on the tile until the first of that month, after
which the tile shows its issue count like any other. So an unreleased volume
needs no follow-up edit to stop being labelled unreleased; only the volume note,
if it mentions the date, has to be revisited. `"Announced"` still works and
still reads "Announced", which is what a book with no date should use.

The volume's `note` should open by saying it has not shipped, and the shelf's
`hb-blurb` should say so too. Do not rely on the badge alone.

The cheap way to add one later, if you do decide to leave it off: **leave its
entry in the hero's `<hero>_contents_raw.json`**. The raw file is only read for
keys named in `ORDER`, so an unused entry costs nothing, and adding the volume
is then a meta-module edit plus a regenerate rather than a fresh wiki pull.

The omnibus shape is what to copy when the goal is "read the collections as
published" rather than "read this story in the right order".

**The X-Men shelf is still the one real exception.** All four of its volumes are
mock-ups of books Marvel has never printed — not unshipped, *nonexistent* — so
no amount of contents, links and cover art makes them buyable. What replaces the
rule is saying so: a standing note in bold directly above the shelf, "0 in
print" in the shelf count, and "never printed" where the other shelves show a
release date.

An amber "Never printed" badge on every tile was the fourth signal and **came
off at the user's request** once the volumes had cover art — four identical
warning pills over four convincing book jackets read as nagging rather than as
information, and the tile badge went back to the issue count every other shelf
shows. The three remaining signals are the floor, not a starting point: the note
above the shelf in particular is the one that has to survive any future edit.

## Adding a hero

1. Curate the reading list and build `<hero>-reading-tracker.html`, modelled on
   whichever of the two shapes fits.
2. In `index.html`, flip that hero's `HEROES` entry: set `file` to the new
   filename and `total` to its issue count. That alone makes the poster live.
3. In the new tracker, add a `.topbar` back link and a `publishIndex()` call at
   the end of `refresh()` (copy both from the X-Men file, changing the storage
   key to `comics-hero-<id>`).
4. Normalise the three images the user has already committed — see "Artwork the
   user supplies" below. **Do not go looking for poster, banner or logo art.**

Steps 1 and 2 are independent — a hero can sit on the shelf as "Curating"
indefinitely with no tracker file, and nothing breaks.

## The three levels, and what sits at the top of each (Aug 2026)

Every page is one of three levels, and they now share the same top:

| Level | Page | Banner shows | Keep Reading shows |
|---|---|---|---|
| 1 | `index.html` | `Art/Banners/index.jpg` + the C.O.M.I.C.S. wordmark | every volume open across all twelve subjects |
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
and look. Three of the eight set one: Spider-Man at `72%` (Alex Ross's figure
runs 48–90% down the plate, and the default band cut him off at the waist),
Daredevil at `0%` (the cowl is hard against the top edge) and Wolverine at
`16%`. The other four take the `50% 28%` default.

Wolverine took two passes and is the useful one to remember: that plate is
1.33:1, the most portrait of the eight, so it is cropped hard and a few points
of `object-position` move a lot of picture. `28%` cut his ears off, `4%`
overcorrected and left him sitting low under a band of empty jungle, and `16%`
is the middle. Render three values and compare them — do not solve for it.

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
homescreen has no poster of its own, so its fallback is all eight posters in a
row behind the scrim (`#hbTiles`) — they are already downloaded for the wall
below, so it costs no request.

The title treatment over the banner is the subject's printed logo from
`Art/Logos/`, with the name as text if the logo fails. Same
degrade-don't-vanish rule the plate follows.

### The Guided Tour

A researched history of the character **as a publishing object** — who made the
book, what the decade did to it, what the art is actually doing — that slides
in over the shelf rather than replacing it. Added Aug 2026 at the user's
request, and the brief is worth restating because it is easy to drift off:

> The goal is to be able to *appreciate* a 1968 page and a 1994 page as two
> different crafts. Not the character's in-universe history — the influence of
> the times, the writers, the artists, and what makes each era's craft its own
> thing. The model is Todd McFarlane naming Gil Kane and saying *when he hit
> somebody it felt like you were getting shot out of a cannon*: name the
> person, name the specific thing, point at where to look.

Two levels, one panel. The button is contextual — the shelf view offers the
character's whole arc, a volume view offers that book's chapter of it — and it
**hides itself where nothing is written**, so a hero whose history has not been
researched shows no dead control.

**The button sits under the banner copy, left-aligned, immediately above Keep
Reading** (the user's placement — it was top-right in the topbar for a day and
read as page chrome rather than as part of the subject's introduction). It is
**one element moved**, not two kept in sync: `trSyncBtn()` appends it into
whichever `.hb-in` is showing. That has to run *after* `buildOmni()`, which
replaces `#obanner`'s innerHTML wholesale — `route()` calling `showOmni()`
first is what makes it safe, so do not reorder those two.

- **`TOUR.overview`** — the character tour. A run of sections, one per era,
  each with an era-coloured rail, maker cards, cover figures and *on your
  shelf* chips. It ends with a **tone map**: which volume is the
  Jekyll-and-Hyde one, which is the cosmic one, which is the funny one. That
  map is the thing the feature is actually for.
- **`TOUR.volumes[<id>]`** — one book, narrowed, and ending in a **reception
  block**: is this a classic, a low point, divisive, and *why do fans say so*.

**Rules that keep it worth reading:**

- **It is hand-written and researched, and it is deliberately not wired to the
  summary engine.** An issue summary is a live model call needing an API key;
  this is the layer that has to be trustworthy with no key and no network.
- **A maker card names one person and one thing to look at.** If it does not
  tell you where to point your eyes, cut it — a biography is not a maker card.
- **A community verdict is reported as a verdict, not as fact.** "Widely held
  to be", "the recurring criticism is", "readers split on". Where a book has a
  real stain on it — the *Immortal Hulk* #43 imagery — say so plainly rather
  than leaving the reader to find out later.
- **A chip closes the panel onto the book it names.** The tour points, you go
  look; that is what makes it a tour rather than an essay. Scroll position is
  kept per tour, so reopening returns you where you were.

**Content is a source module, not HTML.** `tools/tours/<hero>.py` holds the
`TOUR` dict and `tools/build_tours.py` splices it in — same shape as
`build_omnibus_data.py`, and for the same reason: ten thousand words of prose
hand-edited inside an HTML file would make every change an unreviewable diff.
The build **fails loudly** on a chip naming a volume that is not on the shelf
and on a figure whose file is not on disk, because both fail silently in the
browser: a bad chip renders as nothing, and a missing image hides its own
figure through the `onerror` hook. A tour that has quietly dropped half its
pictures still looks finished.

`build_tours.py` knows about X-Men even though `heroes.py` deliberately does
not — an `EXTRA` table names it, because that shelf has a tour like any other.

**Tour artwork is per-issue, and `tools/tour_art.py` fetches it.** The omnibus
jackets cannot illustrate "look at what Trimpe does with a figure here" — there
are 17 of them for 665 issues. The same bifrost record that carries
`published_date` also carries `image_url`, so a tour figure resolves the same
way a deep link does (shelf issue id → marvel id → asset) and nothing is
hand-sourced. Art lands in `Art/Tours/<hero>/<issue id>.jpg` at the usual
700px/q82.

**All twelve shelves have one** (Aug 2026) — 145 volume tours plus twelve
character tours, about **73,500 words and 202 issue covers**. Hulk was written
first on purpose so the voice could be checked before the rest.

| Hero | Volume tours | Words |
|---|---:|---:|
| Hulk | 17 | 9,700 |
| Black Panther | 7 | 6,700 |
| Captain America | 22 | 8,000 |
| Spider-Man | 16 | 7,900 |
| Daredevil | 18 | 7,600 |
| Fantastic Four | 19 | 7,500 |
| Wolverine | 15 | 6,100 |
| Iron Man | 9 | 4,400 |
| Moon Knight | 7 | 3,500 |
| Ghost Rider | 7 | 6,300 |
| Silver Surfer | 4 | 3,100 |
| X-Men | 4 | 2,800 |

**X-Men's tour is shaped differently and has to be.** That shelf covers only
2008–2010, so a straight decade-by-decade walk would describe books that are
not on it. Its character tour does the franchise's sixty-year publishing
history — the 1963 failure, the 1975 relaunch, Claremont's sixteen years, the
8.1-million-copy 1991 #1, Morrison, House of M — and then explains why the
shelf stops where it does. Every one of its four volume tours also carries a
paragraph saying the book does not exist, which is the fourth signal alongside
the three CLAUDE.md already requires.

`tour_art.py` grew a `name:slug` form for exactly that tour: a character tour
often wants a cover from outside its own shelf, and the X-Men one needs 1963,
1975 and 1991. It also reads the X-Men page's own `MARVEL` map, since that
shelf is deliberately outside the shared id store.

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
  right edge and solid 34px past it.

**Everything right of the cover is placed off `--cw`, not off a percentage of
the tile.** The tile width is a `clamp()`, so a percentage stop drifts off the
cover's edge at some widths and the gradient starts cutting into the art. One
variable, redeclared in the 600px media query along with the tile height, keeps
the geometry right at both sizes.

**Four tiles to a screen, and the cap is arithmetic** (Aug 2026, the user's
call — the rail was showing two and a half tiles and everything else meant
scrolling). The rail is 1144px inside the 1180px wrap, so four tiles and three
14px gaps put the cap at 274px, down from 440. `--cw` and the tile height moved
with it: the cover is 2:3 of the height, so 147px tall gives 98px wide, and
changing either alone stops the scan being shown whole. Five to a row would
need a 217px tile, which leaves about 60px of text beside the cover — four is
the floor, not a starting point. The type came down with the tile (title 14px,
credits 10px) and the cover-to-text gap from 66px to 38px; the run line above
the title ellipsises at this width, which is what it is there for.

**Every tile carries a dismiss X**, top right, which clears that volume out of
the rail (Aug 2026). Three things about it:

- **The X is a sibling of the tile's `<a>`, not a child of it.** A `<button>`
  nested in an anchor is invalid markup and its click fights the link's own
  handler, so the tile is now a `.kr-cell` wrapper holding the `<a>` and the
  button side by side. The cell took the flex sizing, the snap point and the
  hover lift off `.kr-card` — without that last move the card lifts on hover and
  the X stays put. The two click handlers cannot collide, because the button
  never matches `closest(".kr-card")`.
- **A dismissal is a timestamp, not a flag**, and that is what makes it
  temporary. `comics-kr-hidden` maps `"<hero>|<volume>"` to when it was
  dismissed; a volume is hidden only while that stamp is *newer* than its
  `touch`. So marking anything in the volume brings the tile straight back, and
  nothing is ever hidden for good. That behaviour is stated on the page in both
  empty states — do not turn it into a permanent hide.
- **One key, shared by all twelve pages**, read and written through each page's
  own `store` — the same origin-wide pattern as `comics-anthropic-key`. It has
  to be shared: the homescreen rail is cross-subject and a tracker's is not, so
  an X in one place has to mean what an X means in the other. The trackers
  filter in `spots()`, which is what `publishIndex()` serializes, so a dismissal
  on a tracker also removes the tile from the homescreen; the homescreen filters
  its own overlay on read and never edits the record a tracker published.

The X is hover-revealed on a pointer device and pinned visible under
`@media (hover:none)` — without that it is unreachable on a phone. `.kr-run`
gives up 20px of padding permanently rather than reflowing when the X fades in;
that line already ellipsises at this tile width, so the cost is a couple of
characters.

An empty rail now means one of two different things — everything finished, or
everything dismissed — so `paintKR()` asks the *unfiltered* spot list which it
is before choosing the message. Saying the wrong one is worse than saying
nothing.

**Two things on the tile are approximations, and both are deliberate:**

- **The bar is progress through the volume, not through the issue.** There is no
  such thing as being halfway through one issue in this data — an issue is read,
  skipped or neither. The position line reads "Issue 12 of 43" for the same
  reason: it is an episode number, not a score.
- **The credits are the volume's `creators`, not the issue's.** For most
  omnibuses that is exactly the writer and penciler, because the book is named
  for them. Per-issue credits are not in the shelf data at all; getting them
  means a wiki pull per issue across 3,500 issues. See open item 15.

A tile is an `<a href="#/omni/<id>">`. Inside that volume already, the hash does
not change and no route fires, so the click handler does the jump itself —
`pendingJump` → `jumpToIssue()`, which opens the chapter, scrolls the row into
view and flashes it. Crossing from the homescreen loses `pendingJump` (different
document); the volume view opens the right chapter anyway.

### The eight ages, and the year on every row

Two things landed together in Aug 2026 because they are the same idea seen at
two scales: **a shelf tile says which age its book belongs to, and an issue row
says which year it came out**, both tinted by the same palette. Scrolling one
chapter you watch the colour shift under you when the book crosses an age,
which is the whole point of reading a shelf historically.

`ERAS` is duplicated in all twelve pages like the rest of the chrome. The bands are
**the user's own, not the textbook ones**, and re-deriving them from a standard
reference is the wrong move:

| Age | Years | Dot |
|---|---|---|
| Golden | 1880–1960 | `#e0a72e` gold |
| Silver | 1961–1969 | `#c3cfdd` silver |
| Bronze | 1970–1984 | `#b0703a` bronze |
| Copper | 1985–1991 | `#d95c46` copper |
| Chromium | 1992–1999 | `#8fd8ee` foil cyan |
| Plastic | 2000–2009 | `#9d7bf0` violet |
| Modern | 2010–2020 | `#3fb98f` teal |
| Contemporary | 2021–2029 | `#ec5f9e` magenta |

Golden runs back to 1880 so nothing on any shelf can fall off the front. An
eleven-band variant was considered and rejected: it only adds seven multi-era
tiles across the 145 volumes and turns most of the modern half of every shelf
into a hyphenated two-era label. Its finer distinctions — 1992 as the Image
line, 2000 as decompression, 2005 as the event era — live in the guided tour
prose instead, which is where they read as history rather than as a label.

**The era tag needs no new data.** `eraSpan()` reads the years out of a
volume's own `era` string, so a book that straddles a boundary shows both dots
and both names ("Copper – Chromium Age") rather than picking the bigger half.
49 of the 145 volumes are two-era.

**The placard sits under the book, not on it.** `.eratag` is a sibling of
`.book` inside `.cell`, which reads as a museum placard under an exhibit. Do
not move it into `.plate` — the plate is printed trade dress, which is why the
progress bar came off it, and a UI pill in there is the same mistake.

**The year is generated, like `MARVEL`.** `YEARS` maps shelf issue id to a
four-digit year and is spliced by `build_omnibus_data.py` — do not hand-edit
it. The join is two stores deep: `marvel_ids.json` is keyed by shelf issue id,
`marvel_years.json` by marvel's own comic id. Keeping the dates keyed
marvel-side is deliberate — the id store is shared, so the same comic dates the
same way on every shelf, and a re-link that repoints an issue redates it for
free.

The source is one field nobody had looked at: `bifrost.marvel.com/catalog/
comics/<id>` returns **`published_date`**, and `tools/years.py` probes only the
~6,100 ids already linked rather than the 140,000-id space `catalog.py sweep`
walks. It came back **6130 of 6130**, so every shelf carries years at exactly
its link coverage (93–100%). The dates are cover dates — Incredible Hulk #1
answers 1962-05-01 — which is what a reader means by "what year is this".

That endpoint also carries **per-issue creators**, which is open item 15 and is
suddenly cheap. Not done; worth knowing it is one field away.

**X-Men has its own `YEARS`**, hand-built and pasted, exactly as its `MARVEL`
map is, because that page is deliberately not in the build pipeline. All 174
issues are dated, 2008–2010.

### The dark chrome

The palette is one block of variables at the top of every page's `<style>`,
under a comment naming the two rules that make it work: the page background is
flat `--bg` (see "The banner"), and panels are a low-alpha white wash over it
rather than their own colour, so retinting the site is one variable.

    --bg #141b29   --line rgba(255,255,255,.10)   --txt #e9eff7   --dim #9db0c6

**`--bg` has a floor, and it is set by the books rather than by taste.** It was
`#0a0e15` for a week and the shelf lost: a book spine is real Marvel trade
dress, which means it is black, and against a near-black page the spines simply
disappeared. The page has to read as lighter than the objects standing on it.
Anything darker than roughly `#0f1420` puts that back.

What survived from the old look, because it is artwork rather than chrome: the
CSS-3D book tiles and their spines, the `.o-*` cover ramps, the `.tex-*`
textures, the `.a-*` poster ramps, the poster plates and printed logos, and the
gold `--xyellow` accent.

What went: the sky gradient, the four floating `.bubble`s, every glass panel
with a white inner highlight, the glossy orb buttons, and the gradient-clipped
italic headings.

The chrome is duplicated in all twelve files on purpose — same portability rule
as the summary engine. Change one, change the others.

## Homescreen (`index.html`)

The `HEROES` array is the whole configuration. Each entry:
`{id, name, art, tex, emblem, cover, pos, plate, logo, logow?, era, file, total, desc, light?}`.
- `file: null` → poster renders dimmed with a "Curating" badge, and clicking it
  opens the dossier modal instead of navigating.
- `file: "…"` → clicking the poster navigates straight to the tracker. The small
  "i" button opens the dossier.

**The three filter chips are gone** (Aug 2026, the user's call). They were
All / Protocol ready / In curation above the poster grid. Seven posters do not
need filtering, and with every subject live the two states they sorted on were
six-to-one — the chips were a control that could only ever hide one poster.
`.filters` and its handler went with them; `.chip-btn` stays, because the
settings modal is built out of it, and `data-state` stays on each cell as the
hook a future filter would want.

**There is no "Ready" badge** (Aug 2026). It was a gold pill on every live
poster, and once every subject was live it labelled nothing — eight
identical badges is not information. The badge element itself stays, because
"Curating" on a subject with no list *is* worth flagging; only the `.live`
variant went. Re-adding a distinction between live posters means finding
something that actually differs between them.

### The order of the wall is fixed, and it is the user's

**`HEROES` order IS the poster order** — the grid renders the array, five to a
row at desktop width — and that order is a decision the user has made. As of
Aug 2026 it is:

| Row | Posters |
|---|---|
| 1 | Spider-Man, Wolverine, Hulk, X-Men, Fantastic Four |
| 2 | Moon Knight, Daredevil, Captain America, Iron Man, Silver Surfer |
| 3 | The Avengers, Black Panther, Ghost Rider, Venom, Doctor Strange |

Row three was **five placeholders** (Aug 2026), added in the order the user
named them. **Black Panther and Ghost Rider are both live as of Aug 2026 and
both stayed where they were** — curating a subject is not a reason to move it,
and the order rule below applies to a promotion exactly as it does to an
insertion. So the wall now has two live shelves in the middle of row three,
which is correct. The other three still have real poster art, a printed logo
and a plate colour the user picked, with `file:null` and `total:0` — no reading
list, no tracker file, no banner. See "The placeholder row" below.

**Do not reorder it, and do not insert a new subject into the middle of it.**
This is not a style preference to re-derive each time: the user asked for it
explicitly after Silver Surfer was inserted between Moon Knight and Daredevil,
and the instruction was that the order stays put "going forward unless I change
it". A new hero goes **at the end** unless the user says where it goes — which
is what happened with Captain America, placed third on row two because the user
named the row they wanted, and again with Iron Man, which the user asked to sit
**between Captain America and Silver Surfer**. Both times the instruction named
neighbours rather than an index; insert against those neighbours rather than
counting positions, because the row a subject lands on then follows for free.

There is no sort anywhere in the page to fix if this looks wrong; `wall()` just
walks `HEROES`. So an accidental reorder is always an edit to that array, and
the fix is to put the array back.

### Artwork

**Every subject shows a real comic cover** (Aug 2026). One scan per subject in
`Art/Heroes/<id>.jpg`, pointed at by `cover` in that hero's `HEROES` entry, run
through the same `covers.save_cover` 700px/q82 downscale as the omnibus shelf
covers so the whole site's art is sized identically.

**Daredevil's is an Alex Ross piece as of Aug 2026** — the whole figure
mid-shout in a burst of light, replacing the earlier head-against-the-moon
cover. That is a *different picture*, not a bigger scan of the same one, so its
`pos` had to be re-derived from scratch and went from 11% to 27%; the old value
put a band of empty black across the modal banner. Expect the same whenever a
poster is genuinely replaced rather than upscaled.

**All fifteen are hand-supplied art, not wiki scans** (Aug 2026). The user
dropped the originals into `Art/covers/` and they replaced the fetched covers
outright. They are painted pieces rather than printed covers, and that turns
out to matter for this particular job: no logo, no barcode strip and no trade
dress fighting the poster plate, so the subject name sits on clean art on every
one of them. Keep that property in mind when swapping one — a scan of a printed
cover will put a logo where the plate goes.

#### Artwork the user supplies — do not source these three

**The poster scan, the banner and the printed logo are the user's to provide,
and they are committed before the request to add the subject is made.** That is
a standing arrangement, not a one-off: when asked to add a hero, the three files
are already in the repo. Go and find them; do not fetch, pick or generate any of
them.

Where they land, and what they are called: the user names each file after the
subject as a person would write it (`Silver Surfer.png`), not by hero id, so
match on the name rather than expecting `<id>`.

| Element | The user drops it in | You normalise it to |
|---|---|---|
| poster scan | `Art/covers/` **or** `Art/Heroes/` | `Art/Heroes/<id>.jpg` |
| banner | `Art/Banners/` | `Art/Banners/<id>.jpg` |
| printed logo | `Art/Logos/` | `Art/Logos/<id>.png` |

**Check both folders for the poster scan.** Silver Surfer's arrived in
`Art/covers/`; Captain America's arrived in `Art/Heroes/`, beside the normalised
files rather than in the archive. Either is fine and neither is worth correcting
— just look in both before concluding a subject's art is missing. The quickest
sweep is `ls Art/*/ | grep -i "<subject>"`, which finds all three at once
whichever folder each landed in.

A source-named file sitting in `Art/Heroes/` is **not** a normalised poster: the
page reads `Art/Heroes/<id>.jpg`, so `Captain America.jpg` there is still raw
input. **This has now bitten three times.** In Aug 2026 the user replaced the
Daredevil poster by uploading `Art/Heroes/Daredevil.jpg` and deleting
`Art/Heroes/daredevil.jpg`, which left `HEROES` pointing at a file that no
longer existed. Pages is case-sensitive, so it 404s and the poster silently
falls back to the handmade `.a-daredevil` ramp — it looks like the new art
"isn't populating" rather than like a broken path.

**The third time was the same shape one folder over**, and is worth knowing
because it happens *mid-task*: while the Ghost Rider shelf was being built the
user pushed `Art/Logos/Ghost Rider.png` and deleted `Art/Logos/ghost-rider.png`
in the same commit. The same fix applies — `logos.py add ghost-rider "Art/Logos/
Ghost Rider.png"`, then delete the source-named file. **The lesson that is new
is to `git fetch origin main` when the user says they have just uploaded
something**: the clone this session started from is a snapshot, so a file
uploaded through the GitHub web UI is not on disk and `ls` will not show it.

**So when a poster or logo does not show the art the user just uploaded, check
the filename case before anything else**, with `ls Art/Heroes/` or
`ls Art/Logos/`. A capitalised twin beside a missing lowercase one is the whole
bug, and `adopt` (or `logos.py add`) is the whole fix. Delete the source-named
copy afterwards — `Art/Heroes/` and `Art/Logos/` hold one file per subject named
by id. Only `Art/covers/` keeps its originals.

Three one-line commands, one per element, all of which only resize and rename —
none of them fetches anything:

```bash
python3 tools/fetch_hero_art.py adopt silver-surfer "Art/covers/Silver Surfer.png"
python3 tools/banners.py add          silver-surfer "Art/Banners/Silver Surfer.png"
python3 tools/logos.py   add          silver-surfer "Art/Logos/Silver Surfer.png"
```

Then wire the printed paths into that subject's `HEROES` entry (`cover`, `logo`)
and the tracker's `hbFallback()`, and **delete the two source-named originals in
`Art/Banners/` and `Art/Logos/`** — those folders hold one file per subject,
named by id, and a stray `Silver Surfer.png` beside `silver-surfer.jpg` reads as
a duplicate. The one in `Art/covers/` is **kept**: that folder is the archive of
full-size originals, which is what lets a poster be re-cropped later.

Two lists are hardcoded and will reject a new subject until it is added to them:
`KEYS` in `banners.py` and `HERO_IDS` in `logos.py`. Neither derives from
`heroes.py`, so adding a hero means one line in each.

All five row-three placeholders are already in both lists, and in `PICKS` in
`fetch_hero_art.py` (`adopt` validates against it and refuses an id it does not
know). So the only thing missing for those subjects is the art itself.

#### The placeholder row

Five subjects added at the user's request (Aug 2026) to see them on the wall
before any of them was curated. **Black Panther and Ghost Rider are no longer
among them** — both were built out later the same month and are live shelves —
but their rows are left in the table below, because their ramps, textures,
emblems and `pos` values are all still the ones chosen here. Only one thing
changed on the way: **Ghost Rider's plate went from orange to pitch black**, at
the user's request, when the new logo landed. See the plate table below.

| Subject | id | Plate | Ramp / texture / emblem |
|---|---|---|---|
| The Avengers | `avengers` | blue `22,92,186` | `a-avengers` / `tex-assemble` / `avengers` |
| Black Panther | `black-panther` | purple `74,34,146` | `a-panther` / `tex-weave` / `panther` |
| Ghost Rider | `ghost-rider` | **pitch black `14,11,10` → `0,0,0`** (was orange `176,66,10`) | `a-ghost` / `tex-flame` / `skull` |
| Venom | `venom` | black `34,44,36` | `a-venom` / `tex-symbiote` / `fangs` |
| Doctor Strange | `doctor-strange` | green `18,114,86` | `a-strange` / `tex-mandala` / `eye` |

Four things about them worth not relearning:

- **The plate colours are the user's, not derived.** Ghost Rider's started as
  a deep orange (`176,66,10`) so it could carry white text, and **the user
  replaced it with pitch black** when the new logo landed — see the plate table
  below for why that is right rather than a third near-black on the wall.
  **Venom's is the interesting one**: asked for black, and
  black is what Moon Knight already owns, but the failure mode here was the
  opposite of Silver Surfer's. Venom's poster art is a black symbiote in a
  black sewer, so at Moon Knight's depth (`26,28,34`) the band vanished *into
  the picture* rather than duplicating another subject. It is lifted to
  `34,44,36`, with a faint green cast so it still reads as its own black.
- **All five have their printed logo** (Aug 2026, a day after the posters), so
  row three reads as one set with the ten above it. **None needed `logow`**,
  which is worth knowing because four of the five are wide single-line marks
  and that is exactly the shape the field exists for: they are 2.0–2.6:1, so
  the 56px `max-height` binds before the width does and Avengers lands at
  almost exactly the width Spider-Man reaches at `logow:"84%"`. Reach for
  `logow` only after rendering — the two knobs pull against each other.
- **No banners, and Black Panther and Ghost Rider have now both proved what
  that costs.** A banner is only ever read by a *tracker* page, so for the three
  still in curation it costs nothing. Both live ones fall through
  `hbFallback()` to their poster scan — Black Panther at
  `objectPosition:"50% 30%"`, Ghost Rider at `"50% 28%"` — and both happen to
  look good, because each poster is a head-on face that fills a 2.4:1 band. It
  is still the fallback rather than the intended art. See open item 19.
- **Every `pos` was rendered and looked at**, the same as the ten above. The
  Avengers plate is the one to remember: it is a crowd, so the band has to land
  on the face row (`39%`) or it is a picture of torsos. Black Panther went
  26% → 30% because 34% clipped the ear tips and 26% clipped the big panther
  eyes behind him into a smear along the top edge — 30% drops them and keeps
  the mask whole, which is the better trade.

The remaining three `desc` strings are **briefs, not specs** — each one ends
"Nothing is decided yet", because the scope call on every one of them is the
user's. Black Panther's and Ghost Rider's said the same until they were built,
and both briefs turned out to be right about the hard part: "Shuri's and
Killmonger's books are the obvious scope question" and "two characters and a
scope call before a single issue is picked" are exactly the calls the user had
to make. The Avengers is the hard one (omnibuses run to dozens of volumes plus
the spin-off teams); Venom overlaps the Spider-Man shelf, which already carries
Spider-Man vs. Venom and briefly carried both Venomnibus volumes; Doctor
Strange starts in the back of Strange Tales and has no numbered run to anchor
on.

`fetch_hero_art.py` keeps its wiki `PICKS` table for every subject including new
ones, but only as the fallback it has been since Aug 2026 — `SUPPLIED` lists
every hero and `--all` refuses to overwrite them. The `adopt` subcommand above
is the live route.

`tools/fetch_hero_art.py` is now the **fallback** route, not the live one. Its
`PICKS` table still holds a wiki pick and the reasoning for every subject, and
`SUPPLIED` beside it lists the ten whose art is hand-supplied; `--all` skips
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

**The posters have no white edge** (Aug 2026, the user's call). `.poster`
carried `border:1px solid rgba(255,255,255,.55)` and an
`inset 0 1px 0 rgba(255,255,255,.5)` top highlight; both were Frutiger Aero
glass trim that survived the dark-chrome rewrite, and against ten pieces of real
painted cover art they read as a sticker border round each poster rather than as
a frame. Both are gone, from the resting and the hover state. **The gold ring on
hover stays** (`0 0 0 2px var(--xyellow)`) — that is an affordance, not chrome.
Removing the border cost no layout, because `box-sizing:border-box` is global.

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
| daredevil | 27% | the shouting head, horns and the light burst |
| silver-surfer | 39% | the brow, eyes and nose bridge, star field either side |
| captain-america | 26% | the mask, the A and the shield edge — 32% clipped the head |
| iron-man | 11% | the gold faceplate, the shoulders and the chest repulsor |
| black-panther | 30% | the mask, the eyes and the shoulder ribbing — 34% clipped the ear tips, 26% smeared the big panther eyes behind him along the top edge |
| ghost-rider | 28% | the burning skull in profile — set while the subject was still a placeholder and unchanged since, because the poster art did not change when the shelf went live |

Silver Surfer's is the clearest illustration of why this is rendered rather
than reasoned about. The poster is a chrome head against black; the obvious
guess is the top of the frame, and `28%` gives the dome and jaw with no
features in the band at all — a silver blob. `44%` pushes the eyes onto the top
edge. The whole head spans 13–60% of the plate, nearly double the band, so it
cannot all fit and the face row is the only strip that reads as a face.

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
| silver-surfer | dark stone grey-blue | the user's call; see below |
| captain-america | deep blue | the poster's foot is pale sky, so the plate has to be dark; the logo is white |
| iron-man | red, run deep | the user's call; see below |
| black-panther | purple | set when it was a placeholder and kept — the poster is a purple-lit night piece and the logo is gold, so the plate had to be deeper than the art rather than a different hue |
| ghost-rider | **pitch black** | the user's call, and the only true `0,0,0` on the wall; see below |

**Ghost Rider's plate is pitch black, and it is the exception to the rule the
Silver Surfer plate below exists to state.** It was a deep orange
(`176,66,10` → `44,12,2`) for as long as the subject was a placeholder, and the
user asked for pitch black when they uploaded the new logo. That is normally
the wrong instinct — Moon Knight already owns the one true black, and Venom had
to be lifted *off* black for the opposite reason — but this logo settles it:
**the letters are black brushwork knocked out of a solid flame field**, so the
mark carries its own light and needs a ground with none. `14,11,10` → `0,0,0`
is darker than any other plate on the wall, and against a poster whose lower
third is dark smoke the band reads as the poster continuing rather than as a
panel. The logo needs no `logow` — it is 1.66:1, so the 56px `max-height`
binds first.

**The flame in that logo is recoloured, and a re-upload will undo it.** As
supplied it was a flat amber `#F8C000` with no gradient at all, which read as
*yellow* rather than as fire — the user's word — and sat on the wall as a cool
yellow object against a poster and a banner that are both orange. It now
carries a vertical fire ramp, `#FF9A1F` → `#F0600F` → `#C22406` top to bottom.

The recolour is worth writing down because a naive one leaves a fringe: the
mark is two-tone, black letters knocked out of the flame, and every
antialiased pixel sits on the straight line between those two colours. So a
flame pixel is identified by **saturation** — which stays near 1.0 the whole
way down that line, where value does not — and is recoloured by substituting
the ramp's hue and saturation while scaling the pixel's own value by
`target_V / 0.973`. Black brushwork (`S < 0.25` or `V < 0.10`) is left alone,
and the alpha channel is never touched. Four candidates were rendered on the
real plate at real size before picking: flat orange was clean but dead, and the
two ramps that kept yellow in them still read as the old logo at 56px.

The original amber file is not kept beside it — `Art/Logos/` holds one file per
subject — but git history has it, and so does the commit that first normalised
it.

**The Ghost Rider poster's background is recoloured too, and the same warning
applies.** As supplied it is a teal-green smoke field behind the burning skull,
which fought the pitch-black plate under it — the plate read as a panel stuck
on the bottom of a green picture rather than as the picture continuing. At the
user's request the teal is now neutral black smoke: fire, embers and the red
chains are untouched, and the art runs into the plate. `tools/deteal.py` does
it, and it is written down there rather than here because the *how* is the
interesting part — a hue band speckles where the smoke meets the flame, and a
darkening pass that is not gated on brightness punches grey holes through the
white-hot core.

`Art/covers/Ghost Rider.jpg` is still the untouched original, because that
folder is the archive. So **`fetch_hero_art.py adopt ghost-rider` on it would
put the teal straight back** — re-run `deteal.py` instead:

```bash
python3 tools/deteal.py ghost-rider "Art/covers/Ghost Rider.jpg"
```

**`DARK` in that tool is the shelf's setting, not a suggestion** — it is what a
fully cool, fully dark pixel is scaled to, and the command above reproduces the
poster that is on the wall. It went to `0.22` on a second pass, at the user's
request for a darker background; `0.50` was the first version. Four values were
rendered on the real tile before picking, which is the only way to choose one:
below about `0.15` the smoke stops being smoke and the top of the poster reads
as a flat cutout, and above `0.5` the plate starts to look like a separate
panel again. `1.0` desaturates without dimming at all.

**Silver Surfer's plate was black for a day and is now dark stone grey-blue**
(`74,86,102` → `28,34,44`), at the user's request. The black version did work,
in the sense that the poster is chrome on deep space and the plate read as more
of the same black with the logo floating on it — but that is also the failure
mode the Hulk's purple plate exists to avoid, and it left two of the eight
subjects with the same near-black band. The grey-blue reads as a band again
while still belonging to the art, and it is the only plate on the wall that is
a neutral rather than a hue. Moon Knight keeps the one true black.

**Iron Man's plate is red because the user asked for red**, and it is run deep
for the reason the next paragraph gives. The logo is the one case on the wall
where the two halves pull opposite ways: the letters are **gold**, which wants a
deep ground to sit on, but their extrusion is **red**, which disappears if the
plate is as red as the letters' shadow. `150,24,18` is brighter than Daredevil's
`124,14,20` — gold on red carries its own contrast, so it can afford to be — and
warm enough that the two red plates on row two read as different subjects rather
than as a repeat. They are two apart on the wall, with Captain America's blue
between them.

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
  56px. Changing that number means re-checking all eight, not just the one that
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

### Start over — the one destructive control on the site

The same modal carries **Reset all progress** (Aug 2026). It clears every
subject's marks on that device and nothing else: the API key and every cached
summary survive, because neither is progress and both cost something to replace.

Two things about it are load-bearing:

- **It clears both halves, and the order matters less than the completeness.**
  `PROGRESS_KEYS` names each tracker's own progress key and `RECORD_KEY` /
  `OLD_RECORD_KEY` the homescreen's cache of it. Wiping only the cache looks
  right until the next tracker visit republishes the progress that was never
  actually erased. A regex sweep of `localStorage` follows the explicit list as
  belt and braces, for a subject added without updating `PROGRESS_KEYS`.
- **It arms on the first click and fires on the second**, rather than calling
  `confirm()` — some browsers suppress a confirm inside a modal, and it would
  be the only thing between a stray click and every mark on the site. The
  armed state expires after six seconds.

`store` on the homescreen grew `set` and `remove` for this and for the Keep
Reading dismissals; it was read-only until the rail became editable.

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
  `buildShelf()` were tuned to a 196px desktop tile and are now running on a
  ~249px one (four books to a row, not five — see below), so they have slack;
  the 600px breakpoint still hides `.screds` outright, because a 142px tile
  leaves only ~207px of spine, which fits the title but not a credit line under
  it. Lengthening a `spine` label past ~22 characters means re-checking both
  breakpoints.

**Four books to a row, not five** (Aug 2026, the user's call — bigger and
further apart). `.shelf` is `minmax(238px,1fr)` with a `56px 40px` gap: 238 is
chosen so a fifth column cannot fit inside the 1180px wrap, and `1fr` then
spends the leftover on the books rather than on the gutters, which is what
takes the tile from 196px to about 249px. Changing either number means
re-checking that arithmetic, not just looking at one width.

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
choice rather than a constraint: twelve shelves of art at one size is worth more
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

Four Graphic Novels are pinned (`mgn-49`, `-65`, `-67`, `-68`); only `mgn-50`
is genuinely absent from the catalog. A fifth pin, `mvoi-1`, is a different
problem entirely and is described under "The Black Panther tracker" — one comic
filed under two series ids, so there was nothing for `tiebreak()` to choose
between. All four had been recorded as "not on marvel.com" for
months, which is the same lesson as the naming pass: **re-test a "not in the
catalog" verdict before believing it.** `catalog.py find "<story title>"` is the
whole check. The pin stores the id only — the slug is read back out of the
catalog — and the run exits loudly if a pinned id is not in it.

### What is left, and why

**5264 of 5355 unique issues across the eleven registered shelves resolve
(98%).** The 84 that do not were each checked against the catalog: they are not
on marvel.com at all. Seven more are **standing rejections** — issues that ARE
in the catalog and are deliberately not linked, because the series that carries
the number is a different comic sharing the name: `tta3-1`, `mk3-1`–`mk3-4`,
`cap8-25` and `mhs-1` (see "An unmapped series is derived, not dropped", "Two
shelf issues on one marvel.com comic" and the Ghost Rider shelf's link
section). `tools/unlinked.json` is the written record of the 84, refreshed by
`link_issues.py --dump`; the seven rejections are named in every run's report
instead.

The largest are Epic Illustrated (10 — a magazine, never digitised; nine on
the Fantastic Four shelf and #1 on the Silver Surfer one), Hulk!
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

### Two shelf issues on one marvel.com comic is a mislink

Found in Aug 2026 by looking at a cover, which is the whole lesson. Fetching
tour art for `dd5-1` (Daredevil (2015) #1) returned **What If: Daredevil**, and
pulling that thread found **17 wrong deep links across four shelves** that
nothing had ever reported.

They were all one shape: **a later volume's #1 carrying an earlier same-named
book's id.** `cap6-1`–`cap6-10` (Captain America 2011) pointed at the 2004
series; `dd4-1`, `dd5-1` and `dd7-1` all pointed at the *same* What If one-shot;
`mk3-*` pointed at Marc Spector; `wvann4-1` pointed at the 1997 annual. They are
old entries from the superseded `series_harvest.py` route, and they survived
every catalog-era run because **`link_issues.py` only ever adds a link and never
re-examines one it wrote earlier**.

**Two checks now run on every pass**, because one of them alone was not enough:

- `audit_collisions()` — the shelf shares an **issue id** when two omnibuses
  collect the same comic, so one id means one link. Two *different* shelf ids
  resolving to one catalog record means one of them is wrong.
- `audit_strays()` — an issue whose link sits in a **different marvel.com
  series from the rest of its own prefix**. This is the same bug seen from the
  other side, and it catches more: `cap7-1` pointed at *What If: Captain
  America* while its other 24 siblings pointed at Captain America (2012), and
  nothing else claimed that id, so no collision was reported. It was found by
  fetching a cover, again, after the first sweep had already run.

A shelf issue id prefix **is** a series — that is what it means — so a lone
dissenter against a clear majority is a mislink.

Both report and neither auto-fixes, because the exceptions are real. One
standing collision: **Marvel Graphic Novel #67 and Wolverine: The Jungle
Adventure #1 are the same comic published under two names.** Nine standing
strays, all legitimate — year-titled annuals (`caan1-2000`, `caan1-2001`,
`hkann-1997`), half-, zero- and infinite-comic issues (`usm-½`, `imm-0`,
`ddp7c-7`, `ddp7c-8`) that marvel.com files as their own one-issue series, and
`xm2-175` / `xm2-176`, where the wiki files 1991–2008 as one continuous X-Men
volume and marvel.com splits it at the 2004 renumbering.

**Neither audit can see a prefix that is uniformly wrong, and that is a real
blind spot.** Found in Aug 2026 while building the Ghost Rider shelf: **all
eight `xm2` ids — the wiki's `X-Men Vol 2` — pointed at X-Men (1963)**, on the
Wolverine and Black Panther shelves as well as this one. `audit_strays()` looks
for a minority dissenting from its prefix's majority and there was no minority;
`audit_collisions()` looks for two shelf ids on one comic and nothing else
claimed those 1963 records. Both stayed silent for months.

What found it was **the publication year**, not a cover: a volume whose issues
run 1992–1993 reported an `actual` span starting in 1965. That check is one
node one-liner over a tracker's own `OMNI` and `YEARS`, it needs no network,
and it should be run on every new shelf:

```bash
node -e 'const fs=require("fs");
  const js=fs.readFileSync("<tracker>.html","utf8").split("<script>")[1].split("</scr"+"ipt>")[0];
  const R=new Function(js.slice(0,js.indexOf("const KEY_P"))+"return{OMNI,YEARS};")();
  R.OMNI.forEach(o=>{const ys=o.chapters.flatMap(c=>c.issues).map(i=>R.YEARS[i.id]).filter(Boolean);
    console.log(o.id, "era="+o.era, "actual="+Math.min(...ys)+"-"+Math.max(...ys));});'
```

A volume whose `actual` range is wider than its `era` by more than a year or
two has a mislinked issue in it. Print the outliers and look at them.

Two of the repairs were to *unlink* rather than repoint, and both are worth
recording because the tempting fix was wrong:

- **Captain America (2017) #25 does not exist.** That series runs #695–704.
  Its link was pointing at the 2018 series' #25, a different comic.
- **Moon Knight Vol 3 (1998, *Resurrection War*) is not on marvel.com.** The
  catalog's only four-issue Moon Knight of that period is the 1999 *High
  Strangeness* mini, which is the shelf's `mk4`. Repointing `mk3` at it just
  moved the collision — the give-away was the catalog description (*Aliens!
  Mind Control!*), not the title or the date.

Both are now refused by the "two shelf series cannot be one marvel.com series"
rule on any future run, so the bad links cannot come back.

### Tooling (`tools/`)

- `catalog.py` — **the id harvester to use.** Sweeps marvel.com's open JSON
  catalog (`bifrost.marvel.com`) into `marvel_catalog.json` / `marvel_series.json`;
  `status` reports coverage, `find` searches it. Resumable — probed ids, dead
  ones included, are recorded in `marvel_catalog_probed.json`. See "Linking
  issues" above.
- `link_issues.py` — matches every shelf issue against that catalog and writes
  `marvel_ids.json`. No table of series prefixes to maintain; reports ambiguity
  instead of guessing. Its three last-resort tables (`ALIAS`, `NUM_ALIAS`,
  `ISSUE_ALIAS`) hold fourteen entries between them and cannot grow silently,
  because every run reports what it could not match. `--write` to commit,
  `--dump` to refresh `unlinked.json`.

  `era_fits()` beside them is a *guard*, not a table: a name match is refused
  when the candidate series' catalog years and the volume's era do not overlap
  within a year. It exists because `tiebreak()` only runs when several
  candidates carry the issue number, so a title with exactly one candidate used
  to be accepted with no date check at all — which read the Ghost Rider shelf's
  Marvel Holiday Special #1 (1991) as the 2005 series' #1.
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
  `daredevil_contents_raw.json`, `silversurfer_contents_raw.json`,
  `captainamerica_contents_raw.json`, `ironman_contents_raw.json`,
  `blackpanther_contents_raw.json`, `ghostrider_contents_raw.json` — the raw
  ReprintOf lists pulled from the Marvel Database, one entry per omnibus, one
  file per hero. Regenerate only if a volume's contents change.
- `heroes.py` — the hero registry. One entry per omnibus-shelf subject, holding
  its tracker filename, art directory, metadata module, panel key and route.
  Every other tool takes `--hero <key>` (default `spider-man`) and reads its
  paths from here. `python3 tools/heroes.py` lists what is registered.
- `omnibus_meta.py` (Spider-Man), `hulk_meta.py` (Hulk), `ff_meta.py` (Fantastic
  Four), `wolverine_meta.py` (Wolverine), `moonknight_meta.py` (Moon Knight),
  `daredevil_meta.py` (Daredevil), `silversurfer_meta.py` (Silver Surfer),
  `captainamerica_meta.py` (Captain America), `ironman_meta.py` (Iron Man),
  `blackpanther_meta.py` (Black Panther), `ghostrider_meta.py` (Ghost Rider)
  — the hand-written half,
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
- `fetch_hero_art.py` — the homescreen's poster art. **`adopt <hero-id>
  <image>` is the live route**: it normalises a scan the user supplied into
  `Art/Heroes/<hero id>.jpg` through `covers.save_cover`, so it is sized
  identically to the shelf art, and leaves the source in `Art/covers/`. The
  wiki fetch is the fallback and has been since Aug 2026 — `PICKS` holds which
  cover and why, `SUPPLIED` lists every subject and it will not overwrite one
  without `--replace`. Nothing is generated from it — the `cover` field in
  `HEROES` is hand-written — so a new poster is an edit in both places.
- `deteal.py` — takes the cool colour cast out of a poster and writes the
  result into `Art/Heroes/<id>.jpg` through the same `covers.save_cover`
  downscale `adopt` uses. Written for the Ghost Rider poster's teal background;
  `--dark` sets how far the neutralised pixels are dimmed (1.0 desaturates
  without dimming), `--out` writes the full-size result instead. Needs Pillow
  and numpy.
- `banners.py` — the above-the-fold banner art. `add <key> <image>` normalises
  one to 2400px/q82 into `Art/Banners/<key>.jpg`; `add-folder <dir>` matches a
  whole folder against the keys by filename; `audit` lists what is there
  and flags anything under 90% of that width as `soft`. `KEYS` is hardcoded, so
  a new subject needs a line there before `add` will take it.
  There is no fetch route — these are hand-picked wide art, like the logos.
  Needs Pillow.

  Two things `add-folder` learned the hard way, both because the homescreen
  banner sat unplaced for two rounds while the file was sitting in the folder:
  it **names every file it did not place**, including ones it cannot even open
  (a `.heic` off a phone used to vanish silently, which reads as the tool
  ignoring an image that is plainly there); and `match()` splits camelCase
  before testing, then falls back to a substring test, because `IndexPage.png`
  is a single token to a whole-word matcher.
- `logos.py` — the homescreen logo pipeline. `add <hero-id> <image>` crops a
  logo to its alpha bounding box, downscales to 500px and writes
  `Art/Logos/<hero-id>.png`; `audit` lists what every subject has and flags any
  file with no alpha channel, which would render as a box. `HERO_IDS` is
  hardcoded, the same trap `banners.py` has. There is no fetch
  route — a printed logo is not on the Marvel Database as a clean transparent
  asset, so these are supplied by hand and the tool only normalises them.
  Needs Pillow.
- `build_tours.py` — splices `tools/tours/<hero>.py` into a tracker as the
  `TOUR` object. `--hero <key>`, `--all`, `--check`. Fails on a tour chip
  naming a volume that is not on the shelf and on a figure file that is not on
  disk; both are silent failures in the browser. Knows about X-Men through its
  own `EXTRA` table, since `heroes.py` deliberately does not.
- `tours/<hero>.py` — the guided tour content, hand-written and researched.
  See "The Guided Tour" above for what belongs in one.
- `tour_art.py` — fetches the individual issue covers a tour points at, from
  the catalog's `image_url`, into `Art/Tours/<hero>/`. `--list` shows what a
  hero already has. Takes a shelf issue id, or `name:slug` / `name:<catalog id>`
  for an issue that is on no shelf at all — which a character tour needs
  constantly. Falls back to the X-Men page's own `MARVEL` map.
- `years.py` — harvests `published_date` for every linked issue into
  `marvel_years.json`. Resumable; `status` reports coverage. See "The eight
  ages" above.
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
- `marvel_ids.json` — id → marvel.com path fragment, **shared by every hero**.
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
shared, so `link_issues.py --write` means regenerating all eleven trackers, not
just the shelf you were working on. The Iron Man harvest was a clean
demonstration: 288 ids written, all of them Iron Man's, and every other shelf
still needed a regenerate because `MARVEL` is spliced in whole. Black Panther
did the same with 293, and Ghost Rider with 196.

**`years.py` is the same trap one step later**, and it is easy to skip because
the build does not fail on it: a harvest that adds links leaves every shelf's
`YEARS` map short until `years.py` runs, and the first Black Panther build
reported **14%** year coverage until it did. Read the coverage line the build
prints; that is what it is there for.

All of these take `--hero <key>`; without one they act on Spider-Man.

`link_issues.py`'s three last-resort tables still hold fourteen entries between
them, and the Ghost Rider shelf needed none. `ISSUE_ALIAS["mvoi-1"]` is the
newest and is not the Marvel Graphic Novel shape the other four are: marvel.com
carries **one comic under two series ids**, so the matcher had two candidates
that were the same issue and no rule could pick between them.

The one thing that shelf did add is a rule rather than an entry — `era_fits()`,
above — which is the outcome to prefer every time: **fix the matcher when the
fix generalises, and reach for a table only when nothing can derive the
answer.**

### Adding an omnibus hero

The tooling is hero-agnostic; what is not automated is curation and the id
harvest. Roughly in order:

0. **Find the art the user already committed.** The poster scan, banner and
   logo are supplied before the request is made, named after the subject rather
   than by hero id — see "Artwork the user supplies". Do not source any of the
   three. Three `add`/`adopt` commands normalise them; add the new key to
   `KEYS` in `banners.py` and `HERO_IDS` in `logos.py` first.
1. **Decide the shelf.** Enumerate candidate volumes with
   `list=allpages&apprefix=<Character>` filtered for `Omnibus`, then make the
   judgement call the tools cannot: which books are *this character's* rather
   than ones they merely appear in. That is a question for the user, not a
   default — **except** when every printed omnibus is plainly the character's
   own solo title and the only exclusion is the release rule, which is what
   happened on Moon Knight and again on Silver Surfer. Then there is nothing to
   ask about; say what you included and why.
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
7. **Generate and publish**: `fetch_covers.py --hero <key> --all`,
   `build_omnibus_data.py --hero <key>` (in that order — fetch writes the
   `cover=` lines the generator reads), then flip the `HEROES` entry in
   `index.html` and set its `total` to the unique-issue count the generator
   printed, and add the hero's progress key to `PROGRESS_KEYS` there or Start
   over will leave that shelf's marks behind.

   `--all` is not optional on a first run if the meta module already carries
   `cover=` paths: `fetch_covers.py` decides what is missing from the meta
   field, not from the filesystem, so it reports "every volume already has a
   cover" while the art directory is empty.
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
2026 and has not been printed. Under the amended rule (see "A shelf holds books
whose tile is finished") it is now a **candidate rather than a refusal** — the
test is whether its contents, links and jacket are all real. Nobody has run that
check on it yet.
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

Off, for now, under the shelf-eligibility rule — these predate the Aug 2026
amendment and have not been re-checked against it (see "A shelf holds books
whose tile is finished"): **Wolverine: Old Man
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
  shelf-eligibility rule excludes nothing.

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
- **Daredevil Omnibus Vol. 4** is off, but only because nobody has re-checked
  it since the rule changed — it ships **September 2026**, which is next month,
  and under "A shelf holds books whose tile is finished" a date alone no longer
  excludes it. Its
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


## The Captain America tracker (omnibus shelf)

Same code as the other seven shelf pages, same tooling, different data: 22
volumes, 727 issue slots, 725 unique issues, all 22 with contents and cover art.
No placeholders, and nothing unreleased. `tools/captainamerica_meta.py` is the
hand-written half; run everything with `--hero captain-america`.

It is the **biggest shelf on the site** — 22 volumes against Fantastic Four's
19 — and the only one that starts in 1941.

### Scope call — Steve Rogers' own book

Twenty-two volumes: Golden Age Captain America Omnibus Vol. 1–2, Captain
America Omnibus Vol. 1–5, by Mark Gruenwald Vol. 1–3, by Waid/Garney/Kubert, by
Dan Jurgens, by Ed Brubaker, Death of Captain America, Captain America Lives!,
The Trial of Captain America, Return of the Winter Soldier, by Rick Remender,
by Nick Spencer Vol. 1–2, Black Widow & Captain America by Waid & Samnee, and
by Ta-Nehisi Coates.

Two are deliberately off, and both are the "different book" call:

- **Invaders Omnibus** — the Invaders' own title, a WWII team book with Namor
  and the original Human Torch. The same call that keeps Marvel Two-In-One off
  the FF shelf and Marvel Team-Up off Spider-Man's.
- **Captain America by Jack Kirby Omnibus** — a strict **subset** of Captain
  America Omnibus Vol. 4. All 25 of its issues are in Vol. 4, which adds FOOM
  #11 on top. Keeping both would put 25 duplicate issues on the shelf and two
  near-identical tiles beside each other for no extra reading. Its entry stays
  in the raw file, so putting it back is one edit plus a regenerate.

**One inclusion is genuinely arguable**: Black Widow & Captain America by Waid
& Samnee is 12 Black Widow issues and 10 of Captain America's own. It is on the
shelf because those ten — Captain America (2017) #695–704, Waid's run — are
collected in omnibus nowhere else, so dropping it opens a hole rather than
removing a duplicate. Contrast the Daredevil shelf, where Elektra by Frank
Miller is off because Matt is barely in it.

**Five gaps are Marvel's, not ours**, which is more than any other shelf:
Captain America Comics #25–75 (the Golden Age line stops at #24), Captain
America #261–306, #419–443 (the end of Gruenwald), the whole Heroes Reborn year
plus Captain America (2002), and Captain America (2017) #1–25. The tile notes
say so where the jump is visible.

### Two enumeration traps, both new

Worth knowing before standing up the next hero, because both cost real time:

- **`apprefix=<Character>` misses books whose title starts elsewhere.** DEATH OF
  CAPTAIN AMERICA OMNIBUS is exactly the volume that closes the Captain America
  (2004) #26–42 hole — the death and the eighteen issues after it — and a prefix
  sweep never sees it. **Search as well as enumerate**, and search on the
  storyline as well as the character.
- **One book, two page titles.** The Waid & Samnee volume is filed as both
  "Captain America & Black Widow…" (no ReprintOf fields at all) and "Black Widow
  & Captain America…" (the real page). A probe that finds the first one
  concludes the book has no contents and drops it. Take whichever page has the
  ReprintOf fields.

### Contents

Pulled the same way as the other shelves, into
`tools/captainamerica_contents_raw.json`. Two repairs were needed:

- **Twenty-five short-form entries.** The Golden Age volumes list
  `Captain America Comics #1` rather than `Captain America Comics Vol 1 1` —
  the Hulk shelf's short-form problem, and here it is a whole volume's worth.
  Rewritten to the long form; without it the ids come out `cac-#1` and the
  titles read `Captain America Comics ##1`.
- **One stray `#`** inside an otherwise long-form entry
  (`Captain America Vol 5 #615.1`), which the short-form repair does not catch
  because the entry does contain " Vol ". It is worth checking for both shapes:
  a `#` anywhere in a repaired file is a bug.

Re-apply both if any volume is re-pulled.

### Chaptering

Fourteen volumes take the automatic per-series chapters. Eight carry
`chapterby="series"` — the Waid, Lives!, Trial, Return of the Winter Soldier,
Remender, both Spencer volumes and the Waid & Samnee book. All eight are the
anthology shape: an ongoing with minis and one-shots threaded through it, which
scores under the 3.5 average-run-length threshold for the same reason the Hulk
anthologies do and reads far better as one chapter per book than as "Part N".

### Issue ids and the overlaps

727 slots against 725 unique — two overlaps, and both are the same shape as
Daredevil's single one: a volume that starts on the issue the previous one ends
on. Captain America (2004) #25 is in both the Brubaker volume and Death of
Captain America; Captain America: The Legend #1 is in both Waid and Jurgens.

### Marvel deep links

**721 of 725 unique issues (99%).** The rest fall back to
`marvel.com/search?query=` and a grey Read button. Complete: Captain America
Comics all 24 on the shelf, Tales of Suspense, Captain America (1968) all 295,
(1998), (2004), (2011), (2012), (2017), (2018), the annuals, Sam Wilson, Steve
Rogers, Winter Soldier and every Secret Empire tie-in.

Three things this shelf's link pass is worth remembering for:

- **698 issues matched on the first run with 0 ambiguous**, which is the
  "what a brand-new hero actually gets" number holding up on the biggest shelf
  on the site.
- **17 rejections, and every one was a real error in this module.** The
  "two shelf series cannot be one marvel.com series" rule caught `capann` and
  `cap9` duplicating codes the Wolverine shelf already owns for the same
  comics (`caan1`, `cap18`). The fix was to adopt Wolverine's codes, not to
  invent new ones — the id store is shared and Captain America Annual #8 is
  literally the same issue on both shelves. **Read the rejection list; it is
  not noise.**
- **Two more `.NOW` issues**, `cap7-16.NOW` and `wsolbm-1.NOW`, pinned in
  `NUM_ALIAS` alongside the Silver Surfer one for the same reason: `.NOW` is
  cover branding, marvel.com numbers both plainly, and folding the suffix away
  inside `numkey()` would mislink runs where a `.NOW` really is a separate
  issue.

The 4 that marvel.com does not have: FOOM #4 and #11 (a fanzine, and #4 was
already missing for the Fantastic Four shelf), Captain America: Sentinel of
Liberty Rough Cut #1, and Captain America: Red, White & Blue #1. Captain
America (2017) #25 is also unlinked and is a genuine absence — marvel.com
carries no #25 for that series, only #695–704.

### Cover art — six jackets are not the wiki's

**`fetch_covers.py` returns an issue cover, not a jacket, for six of these**,
and it looks like a successful fetch every time. The pages for Golden Age Vol.
1–2 and Captain America Omnibus Vol. 1–3 and 5 either declare a redlinked
`Image1` or point their infobox `Image` straight at a collected issue's scan,
so `prop=pageimages` answers with `Captain_America_Vol_1_100.jpg` and friends.

All six were replaced by hand from the flat cover-by-ISBN endpoints (see "A
shelf holds books whose tile is finished"). **Do not run `fetch_covers.py
--hero captain-america --all`** — it will put the issue covers back.

One extra hazard the Silver Surfer shelf did not hit: **a retailer's flat cover
sometimes includes the spine.** Captain America Omnibus Vol. 2 came back at
413x500, aspect 0.83, and `covers.save_cover` said so — that warning is the
tell. Cropping to the rightmost `height × 2/3` gives the front face. Trust the
aspect warning; it is the only thing that catches this.

Twelve of the 22 covers are `soft` (under 500px), which is the price of taking
flat jackets from booksellers rather than scans from the wiki.

## The Silver Surfer tracker (omnibus shelf)

Same code as the other six shelf pages, same tooling, different data: 4
volumes, 141 issue slots, 141 unique issues, all 4 with contents and cover art.
No placeholders. `tools/silversurfer_meta.py` is the hand-written half; run
everything with `--hero silver-surfer`.

It is still the smallest shelf on the site — half of Moon Knight's — but that is
the character, not an omission: **every Silver Surfer omnibus that exists is on
it**, which is true of no other shelf.

One of the four has not shipped yet. Silver Surfer: The Infinity Gauntlet
Omnibus is dated **3 November 2026** and is on the shelf under the amended
eligibility rule, because its contents, its links and its jacket are all real —
see "A shelf holds books whose tile is finished", which also explains why its
cover had to be added by hand.

### Scope call — every Surfer omnibus there is, which is four

There was no judgement call to make on the books themselves, and that is worth
stating rather than leaving implicit. The Marvel Database lists exactly four
Silver Surfer omnibuses, all four are the character's own solo title, and all
four are on the shelf:

- **Silver Surfer Omnibus** (May 2007) — the 1968 Lee/Buscema series.
- **Silver Surfer: Return to the Spaceways Omnibus** (May 2025) — the 1980s.
- **Silver Surfer: The Infinity Gauntlet Omnibus** (3 Nov 2026) — Starlin.
- **Silver Surfer by Slott & Allred Omnibus** (Dec 2018) — 2014–2017.

Nothing here is the Surfer equivalent of She-Hulk or Laura Kinney; no spin-off
character has an omnibus. There is no team book to argue about either — the
Defenders volumes are the Defenders'. Note the Surfer omnibuses were already
named as deliberately off the Fantastic Four shelf, which is what left them
free to be their own subject.

**`gauntlet-o1` is not the 2014 Infinity Gauntlet Omnibus**, and confusing the
two would put the wrong contents and the wrong jacket on the shelf. The 2014
book is the *event* edition: it stops the Surfer run at #60, carries no annuals
and no Marvel Comics Presents, and adds the crossover tie-ins (Cloak and Dagger,
Spider-Man, Hulk, Doctor Strange, Quasar, Sleepwalker). The 2026 book is the
Surfer edition: #34–66, Annual #3–4, Thanos Quest, Infinity Gauntlet #1–6 and
seven Marvel Comics Presents, and nothing that is not his. The wiki has a real
cover for the 2014 one, which makes it a tempting and wrong answer to the
missing-jacket problem.

`SHELF` is a reading order that here is also publication order, so nothing is
resequenced.

**Two things that look like gaps, only one of which is one:**

- **1970–1982 is not a gap, it is a hiatus.** The 1968 series ended at #18 and
  the Surfer had no title of his own for twelve years — he was in Fantastic
  Four and the Defenders. There is nothing uncollected to complain about; the
  note on `spaceways-o1` says so, because a reader looking at a 1970 → 1980
  jump will otherwise assume something is missing.
- **1992–2014 is a real hole**, and it used to be a 24-year one. `gauntlet-o1`
  closes its first third: what is left is Silver Surfer (1987) #67–146, the 2003
  Straczynski series and the 2011 mini, none of which has an omnibus. The note
  on `slott-o1` says so.

### Contents

Pulled the same way as the other six shelves (the `ReprintOf<N>` MediaWiki call
above), into `tools/silversurfer_contents_raw.json`. As clean a pull as Moon
Knight's:

- **ReprintOf order matched the rendered gallery order on all four volumes**,
  so nothing needed reordering by hand the way `inc-o1` did. That includes the
  unreleased one — its ReprintOf fields are fully filled in, which is the first
  of the three gates it had to pass.
- **Every page writes the full form** (`Silver Surfer Vol 1 1`), so no gallery
  cross-reference was needed — and there are eight volumes of a series called
  "Silver Surfer" for it to have gone wrong on.
- **Not one ReprintOf entry was missing from the rendered page**, on any of the
  four.

**One repair was needed**, the familiar one: two Marvel Graphic Novel entries
carry a subtitle after the issue number (`Marvel Graphic Novel Vol 1 38: Silver
Surfer: Judgment Day` and `... 58: Silver Surfer: The Enslavers`), which the
`<series>`/`<issue>` split on the last space cannot survive. Truncated at the
first colon after the issue number, the same shape as three on the FF shelf,
three on Wolverine's and one on Daredevil's. Re-apply it if either volume is
ever re-pulled.

**The solicit audit could not say anything here.** Not one of the four volumes
carries an explicit `COLLECTING` range — the same worst-case coverage as the
Daredevil shelf — so the shelf-wide gap check did the whole job. Its only
finding is the 1990–2014 hole above, which is the missing omnibus, not missing
contents.

### Chaptering

All four volumes take the automatic per-series chapters and **none carries
`chapterby`** — the only shelf where that is true. They score 6.7, 4.1, 9.2 and
10.0 on the average-run-length test, well clear of the 3.5 threshold, because
each book is one long ongoing with a short tail rather than a month-by-month
crossover or an anthology of minis.

`gauntlet-o1` is the one worth checking, because it is a crossover and those
usually score low: it comes out at five clean chapters (Infinity Gauntlet,
the Surfer run, the annuals, the Thanos Quest, Marvel Comics Presents) because
the book prints each series in a block rather than interleaving them month by
month. Its Surfer chapter renders `#34–38, #40, #44–66`, which is `spanlabel()`
correctly refusing to claim issues the book does not hold.

`spaceways-o1` is the interesting one: eleven chapters, of which eight are a
single issue. That is the book, not the heuristic misfiring — it prints the
1987 run straight through and then hangs ten one-off pieces off the end (both
graphic novels, Parable, Epic Illustrated #1, the first Marvel Comics Presents,
Fantastic Four #325, Super-Villain Classics #1, Marvel Fanfare #51), and one
chapter per piece names each of them where "Part N" would not.

Note `Marvel Graphic Novel` appears as **two** separate chapters in that volume
(#38 and #58, with other series between them). That is `gen()` computing runs
correctly, not a duplicate.

### Issue ids — no overlaps at all

141 issue slots and 141 unique issues: the third shelf after Moon Knight and
Daredevil where those two numbers are equal, so nothing carries the gold "in N
omnibuses" pill. Unlike Daredevil's, this is not a consequence of a scope call
— the four books simply tile four separate stretches with nothing reprinted
between them. `gauntlet-o1` fits into that exactly: it opens at Silver Surfer
(1987) #34, the issue after the one `spaceways-o1` stops on.

### Marvel deep links

**140 of 141 unique issues (99%) resolve** — joint-best with Daredevil and
Wolverine. The one that does not falls back to `marvel.com/search?query=` and a
grey Read button, same convention as the other trackers. Complete: Silver
Surfer (1968) all 18, (1982), (1987) #1–66, (2014) and (2016) in full, all four
annuals, Parable, Thanos Quest, Infinity Gauntlet, and every guest appearance.

**The id harvest was not a step** — the catalog already held everything, so
this was `link_issues.py --write` twice, 90 issues matched on the first pass
with 0 ambiguous, and another 39 when `gauntlet-o1` was added.

**All 46 of the unreleased volume's issues resolve**, which is the point worth
taking from it: a book's own release date says nothing about whether its
*contents* are in the catalog. These are 1990–92 comics; the catalog has had
them for decades. Expect the links gate to pass for any unshipped omnibus of
older material, and to be the one to actually check for a collection of
this year's comics.

Two more results are worth keeping:

- **Both Marvel Graphic Novels linked from their numbers.** `mgn-38` and
  `mgn-58` resolve to `marvel_graphic_novel_1982_38` and `_58`, which is *not*
  what the MGN entries on the FF and Wolverine shelves do — four of those had
  to be pinned in `ISSUE_ALIAS` because marvel.com files them under their story
  titles. So the MGN line is filed both ways in the catalog, and the pin is a
  per-issue last resort rather than a rule about the imprint. Try the number
  first.
- **Silver Surfer: Parable resolved to the right one of two.** The catalog
  carries `Silver Surfer: Parable (1988)` and `(1989)`; the 1988 series holds a
  single `#0` (the collected edition) and the 1989 one holds `#1` and `#2` (the
  Epic mini the book actually reprints). No tiebreak was needed — only one
  series carries those numbers, which is the first rule in the matcher and the
  reason it is first.

One `NUM_ALIAS` entry was needed, the second on the project: **All-New Marvel
NOW! Point One shipped as #1.NOW** and marvel.com files the one issue that
series has as `#1`. `.NOW` is cover branding, not an issue number. It is
deliberately *not* folded away inside `numkey()`, because elsewhere a `.NOW`
issue sits beside a plain `#1` in the same run and is a different comic —
generalising it would link those to the wrong book. This is the only `.NOW` on
any shelf.

The 1 that marvel.com does not have: **Epic Illustrated #1**. A magazine, never
digitised — the same shape as the nine Epic Illustrateds already missing from
the Fantastic Four shelf, and the tenth on `tools/unlinked.json`.

### The page itself

Built from `moonknight-reading-tracker.html`, which is the one to copy for a
small shelf. What changed beyond the identity sweep:

- **Four `.o-*` ramps**, all with `SPINE_C` entries: `o-chrome` (polished
  silver into black), `o-cosmic` (deep purple space), `o-gauntlet` (gold into
  Thanos purple) and `o-dawn` (Allred's teal-and-orange).
- **Three textures**: `tex-starfield`, `tex-cosmic` (radiating rays from a
  bright point) and `tex-popdot`, which is a coarser benday than the shared
  `tex-halftone` because the Allred volume is pop art.
- **The glyph is a figure on a board over its own wake**, replacing the
  crescent. Same `split("GID").join(...)` fresh-id mechanism, prefix `ss`.
- **`SC`** rewritten for the sixteen series these three books collect.

**One cover on this shelf was not fetched, and must not be.** `gauntlet-o1`'s
jacket does not exist on the Marvel Database — the page declares `Image1` and
`Image2` and both are redlinks — so `fetch_covers.py` answers with Infinity
Gauntlet #2's cover out of the reprint gallery instead, which looks like a
success. The real jacket came from Amazon's flat cover image by ISBN and went in
through `covers.py add`. **Do not run `fetch_covers.py --hero silver-surfer
--all`** until the book ships; it will silently replace it with the wrong image.
`covers.py audit` flags it `soft` at 340x500, which is the price of having the
right cover early.

One naming trap this shelf hit and the next one will too: **`ss` was already
taken** by Scarlet Spider on the Spider-Man shelf, so every Surfer series code
uses an `ssf` stem. `autocode()` would have avoided the collision on its own,
but the codes it derived were worse, and an issue id is a saved-progress key —
so they are pinned in `SERIES_EXTRA` before anyone reads with them, which is
the window CLAUDE.md says to use.

Also note the SC block in a tracker ends with a bare `}` on its own line, not
`};`. Splicing a new one in by matching `\n};` silently swallows the whole
`OMNI` and `MARVEL` arrays below it, and the failure surfaces much later as
`build_omnibus_data.py` reporting "substring not found".


## The Iron Man tracker (omnibus shelf)

Same code as the other eight shelf pages, same tooling, different data: 9
volumes, 341 issue slots, 340 unique issues, all 9 with contents and cover art.
No placeholders, and nothing unreleased. `tools/ironman_meta.py` is the
hand-written half; run everything with `--hero iron-man`.

Like Moon Knight and Silver Surfer it is **complete**: the Marvel Database lists
exactly nine Iron Man omnibuses and all nine are on the shelf.

### Scope call — there wasn't one, and the absences are Marvel's

Nothing here needed the judgement call the other shelves needed. Every one of
the nine is Tony Stark's own solo book, there is no family character with an
omnibus to rule out (War Machine, Ironheart and Superior Iron Man have none),
there is no team book to argue about, and nothing is unreleased — the most
recent volume shipped in **May 2026**, three months before this shelf was built.

**The runs people will ask about are missing because they have no omnibus, not
because of a scope call.** This is worth stating plainly, because their absence
looks like an editorial decision and is not:

| Run | What exists |
|---|---|
| Fraction & Larroca (2008–2012) | `Invincible Iron Man by Fraction & Larroca HC` and a Complete Collection TPB — no omnibus |
| Ellis's Extremis (2005) | `Iron Man: Extremis TPB` — no omnibus |
| Gerry Duggan (2022) | three `Invincible Iron Man by Gerry Duggan TPB` volumes — no omnibus |

Searching the storyline as well as the character — the Captain America lesson —
turned up nothing the `apprefix` sweep had missed.

`SHELF` is a reading order that here is also publication order, so nothing is
resequenced. Four numbered volumes carry 1963–1978, then the creator books.

**Four gaps are Marvel's, not ours:**

- **Iron Man #113–114** — two issues, and the most annoying kind. Vol. 4's own
  solicit says it collects `#68-112`, and the Michelinie volume is a "by"
  collection starting at #115, so Bill Mantlo's last two issues fall down the
  crack between a numbered volume and a creator one.
- **#158–218** — 61 issues, the big one: the end of Michelinie's first run, the
  whole Denny O'Neil stretch, and the run-up to Armor Wars.
- **#233–257** — the material *between* the two Armor Wars stories. Not an
  omission: `armor-o1` is a storyline book, not a run.
- **#267–332 plus the whole Heroes Reborn year** — everything between 1991 and
  the 1998 relaunch, and then everything between 2002 and 2018.

### Contents

Pulled the same way as the other shelves (the `ReprintOf<N>` MediaWiki call
above), into `tools/ironman_contents_raw.json`. As clean a pull as Moon
Knight's, and cleaner than most:

- **Not one ReprintOf entry was missing from the rendered gallery**, on any of
  the nine — so nothing of the Fantastic Four #171 / Wolverine #55 shape.
- **Every page writes the full form** (`Iron Man Vol 1 1`), so no gallery
  cross-reference was needed to disambiguate — and there are seven volumes of a
  series called "Iron Man" for it to have gone wrong on.
- **No doubled spaces, no subtitles after the issue number, no short-form
  entries.** Nothing needed repairing.

**One volume's order was corrected by hand, and it is the `inc-o1` hazard
again.** The wiki's ReprintOf fields for `iim-o2` group by series and so put
**Iron Man and Sub-Mariner #1 last**, after Iron Man #25. It belongs between
Tales of Suspense #99 and Iron Man #1: it is the April 1968 one-shot that exists
only because the shared book was splitting in two, and it was published between
them. The rendered gallery agreed with the fields, so this is a judgement call
against both wiki sources rather than a repair of one — but a book that prints
its own bridging issue as an appendix after the run it bridges into is not a
book anyone has made. **Re-apply this if `iim-o2` is ever re-pulled.**

**The solicit audit could check only two of the nine**, and both matched the
shelf exactly: Vol. 3 (`IRON MAN (1968) #26-67 and DAREDEVIL (1964) #73`) and
Vol. 4 (`#68-112 and ANNUAL (1970) #3-4`). The other seven carry no explicit
range, so the shelf-wide gap check did the rest — and every gap it found is one
of the four above, confirmed by creator credits (#113–114 Mantlo, #158 O'Neil
and Infantino, #233 Michelinie and Guice inside a storyline book).

One entry that looks wrong and is not: **the Slott volume ends on Iron Man
(1998) #25**, a 1999 Busiek issue at the back of a 2018–2020 book. That is
backmatter, printed there deliberately — #25 is where Arno Stark was set up, and
Iron Man 2020 is Arno's story. It is also the shelf's only overlap.

### Chaptering

Eight volumes take the automatic per-series chapters. Only `busiek-o1` carries
`chapterby="series"`, and it is the closest call on the project: it scores
**3.27**, just under the 3.5 threshold, because 25 issues of Busiek's run are
followed by nine single crossover issues and then a two-issue mini. Those nine
are each a named book from "The Eighth Day", so one chapter per book names them
where "Part N" would not — the same call the Hulk anthologies take.

`mlr-o1` comes out as a single 43-issue chapter, which looks wrong and is not:
the volume is Iron Man #115–157 and nothing else.

### Issue ids and the one overlap

341 issue slots against 340 unique — one overlap, **Iron Man (1998) #25**, in
both `busiek-o1` (which collects #1–25) and `tsim-o1` (which reprints it as
backmatter). It shares its id across both on purpose, as on every other shelf,
and the UI flags it with the gold "in 2 omnibuses" pill.

`im` was already the code for Iron Man (1968) on four other shelves, and `tos`,
`tta`, `dd`, `cap3`, `ff3` and `imcaann` were likewise already owned. All seven
are repeated verbatim in this module's `SERIES_EXTRA` — the id store is shared
and the same comic has to key the same way everywhere.

### Marvel deep links

**339 of 340 unique issues (100%) resolve** — joint-best on the project with
Daredevil. The id harvest was not a step: the catalog already held everything,
so this was `link_issues.py --write` twice with a regenerate between, 288 ids
written, **0 ambiguous and 0 rejected on the second pass**.

The 1 that marvel.com does not have is **Iron Man Annual 2001**. Re-tested
before being believed, as the standing rule says: Marvel files each year-titled
annual as its own one-issue series, the catalog carries `iron_man_annual_1999`
and `iron_man_annual_2000`, and then jumps to 2021. There is no 2001.

**One tool fix came out of this shelf, and it generalises.** All six Iron Man
2020 issues came back ambiguous on the first run, and no `tiebreak()` rule could
separate the candidates, because `norm()` was stripping a **bare** trailing
year-shaped number:

    norm("Iron Man 2020 (2020)")    -> "iron man"
    norm("Iron Man (2020 - 2022)")  -> "iron man"

Two different comics, folded to one string — and their marvel.com slugs collide
too (`iron_man_2020_2020_1` is Iron Man 2020 #1; `iron_man_2020_1` is Iron Man
#1 from the 2020 Cantwell ongoing). The strip ran *after* the line that removes
a parenthesised `(1988 - 1997)`, so anything year-shaped it could still see was
part of the NAME — Iron Man 2020, Machine Man 2020, Spider-Man 2099, Doom 2099.
Removing it gained 6 matches across all nine shelves and lost none, and
re-pointed **zero** existing ids. That is the Daredevil `1.50` precedent again:
fix the matcher when the fix generalises, reach for `NUM_ALIAS`/`ISSUE_ALIAS`
only when nothing can derive the answer. No alias entry was needed for this
shelf.

### Cover art — two jackets the wiki does not have

**`fetch_covers.py` returns an issue cover, not a jacket, for two of these**, and
it looks like a clean fetch both times. **Do not run `fetch_covers.py --hero
iron-man --all`** — it will put them back. The detail is written down in
`tools/ironman_meta.py` beside the volumes it affects; in short:

- **`iim-o1`** — the page declares `Image1` under the omnibus's own name, but
  that file is itself a scan of **Tales of Suspense #39**, price box and Comics
  Code stamp and all, and `Image1_ReprintOf` says so. The jacket on the shelf is
  the **Parel variant** (600x901), the only file on the page carrying omnibus
  trade dress. Added by hand with `covers.py add`.
- **`iim-o2`** — the page declares `Image1 = Iron Man Vol 1 1.jpg` outright; the
  wiki has no jacket for this book. Left as fetched, because three independent
  sources — that file, the Larroca variant, and Amazon's image keyed to the
  book's own ISBN — all show the same Iron Man #1 artwork. The printed jacket
  really does reproduce the 1968 cover, so the art is right for the book even
  though the scan is an issue.

Worth knowing for the next shelf: **the flat-jacket-by-ISBN endpoints are not a
reliable rescue.** Penguin Random House returned a "Cover Coming Soon"
placeholder for both of these ISBNs, and Amazon returned the same issue art the
wiki had. They worked on Silver Surfer and Captain America; they did nothing
here.

Five of the nine covers are `soft` (under 500px). That is what the Marvel
Database stores.

## The Black Panther tracker (omnibus shelf)

Same code as the other nine shelf pages, same tooling, different data: 7
volumes, 354 issue slots, 350 unique issues, all 7 with contents and cover art.
No placeholders, and nothing unreleased. `tools/blackpanther_meta.py` is the
hand-written half; run everything with `--hero black-panther`.

It is the **first row-three placeholder to be curated**, and it stayed where it
was on the wall — see "The order of the wall is fixed".

### Scope call — six obvious books and one argument

The Marvel Database lists seven Black Panther omnibuses and all seven are on the
shelf. Six needed no judgement at all: The Early Marvel Years, Panther's Prey,
both Priest volumes, Hudlin and Coates are either a numbered run collection or a
"by <creator>" book, there is no family character with an omnibus to rule out
(Shuri and Killmonger have minis, not omnibuses), and nothing is unreleased —
the most recent, Panther's Prey, shipped in February 2026.

**The one call was WAKANDA: WORLD OF BLACK PANTHER, and the user put it ON.**
It is an anthology rather than a run: sixty-five issues of minis set in Wakanda,
roughly two-thirds of them T'Challa's (Rise of the Black Panther, Long Live the
King, the three Wakanda Forever one-shots, Black Panther vs. Deadpool, Agents of
Wakanda, King in Black: Black Panther) and the rest other people's — World of
Wakanda, Shuri, Killmonger, The Crew. It is the only volume here that is not a
Black Panther title, and it is the reason the shelf has any overlap at all.

**Two enumeration traps, both the Captain America lesson repeating:**

- **`apprefix=Black Panther` never sees Wakanda: World of Black Panther.** A
  wiki *search* for "Wakanda Omnibus" does. Search as well as enumerate, and
  search on the storyline as well as the character.
- **"Black Panther: Revenge of the Black Panther Omnibus Vol 1 1" is a live wiki
  page and is a `#REDIRECT`.** The book was retitled to Panther's Prey before it
  shipped. Its ReprintOf pull comes back empty, which looks like a solicited
  book with no contents and is actually one book counted twice. Fetch the
  wikitext before concluding a page has no issue list.

`SHELF` is a reading order that on the first six volumes is also publication
order. **wakanda-o1 sits last** rather than beside the Coates run it grew out
of: it is a cross-era anthology, which is the placement the Doom and Ultimate
volumes take at the end of the FF shelf, and reading it in sequence would mean
stopping the Coates run twice.

**Two gaps are Marvel's, not ours**, and unusually both are at the modern end:

- **Black Panther (2009) #7–12 and the whole #513–529 run** — David Liss's
  *The Man Without Fear* / *The Most Dangerous Man Alive*, 2011–12, which put
  T'Challa in Hell's Kitchen with no money and no country. No omnibus.
- **Black Panther (2021) #1–15 and (2023) #1–10** — John Ridley's spymaster run
  and Eve Ewing's after it. No omnibus, which is why the shelf stops in 2021.

The tile notes and the guided tour both say so.

### Contents

Pulled the same way as the other shelves (the `ReprintOf<N>` MediaWiki call
above), into `tools/blackpanther_contents_raw.json`. It is the cleanest pull on
the project so far in one respect and the messiest in another:

- **Every page writes the full form** (`Black Panther Vol 1 1`), so no gallery
  cross-reference was needed to disambiguate — and there are **seven** volumes
  of a series called "Black Panther" for it to have gone wrong on.
- **The ReprintOf fields matched the rendered gallery exactly on all seven
  volumes**, in content and in order, once filename punctuation is folded (a
  wiki image cannot hold a `:` or a `/`, so `Black Panther: Long Live The King
  Vol 1 1` is stored as `Black Panther Long Live The King Vol 1 1` — that is
  not a disagreement).
- **No doubled spaces, no subtitles after the issue number, no short-form
  entries.** None of the three repairs the other shelves needed applies here.

**Two hand fixes are in the raw file and a re-pull will undo both:**

- **`early-o1`'s order is corrected.** The wiki's ReprintOf fields *and* its
  gallery both put **Jungle Action #6–24 first**, grouped by series. Marvel's
  own solicit puts it last, and the blurb says why — "Then, Don McGregor
  launched T'Challa's first solo series". Moved to the end; everything else in
  the wiki's order is the solicit's order exactly. This is the `inc-o1` hazard
  from the Hulk shelf, and here it is a 19-issue block, not one issue.
- **Fantastic Four #54 is restored by hand.** It is in neither the ReprintOf
  fields nor the gallery. The official collecting line reads
  `THE FANTASTIC FOUR (1961) #52-53, and #56, #119 and material from #54`, which
  settles it — the same shape as Fantastic Four #171 and Wolverine #55, and the
  same lesson: the solicit is the independent source, and here it was not even
  on the wiki page, it was on the retail listing.

**The solicit audit covered two of the seven** and both matched exactly:
Panther's Prey (`Black Panther (1977) #1-15, Marvel Two-in-One (1974) #40-41,
…`) and Hudlin (`Black Panther (2005) 1-41, X-Men (1991) 175-176, …`). The
other five carry no explicit range, so the shelf-wide gap check did the rest,
and every gap it found is one of the two above.

### Chaptering

Six volumes take the automatic per-series chapters. Only `wakanda-o1` carries
`chapterby="series"`, and it is the closest call on the project after
`busiek-o1`: nineteen runs across sixty-five issues scores **3.42**, just under
the 3.5 threshold, so the heuristic would have chunked an anthology of eleven
named minis into "Part 1"–"Part 11". One chapter per mini names Shuri,
Killmonger and World of Wakanda where "Part N" would not.

Two volumes look wrong at a glance and are not:

- **`coates-o1` comes out as two chapters of twenty-five issues.** The book is
  two series and nothing else, and `spanlabel()` correctly renders the Legacy
  renumbering as `#1–18, #166–172` rather than claiming 172 issues.
- **`hudlin-o1` splits Black Panther (2005) into three chapters** around two
  single-issue X-Men chapters. That is the *Wild Kingdom* crossover printed in
  reading order — BP #7, X-Men #175, BP #8, X-Men #176, BP #9 — which is how
  the book prints it. Same shape as `mackay-o1` on the Moon Knight shelf.

### Issue ids and the overlaps

354 issue slots against 350 unique — four overlaps, and all four are
`wakanda-o1` doubling back:

| Overlap | Volumes |
|---|---|
| Black Panther Annual (2018) #1 | `hudlin-o1` + `wakanda-o1` |
| Black Panther (2018) #23–25 | `coates-o1` + `wakanda-o1` |

They share ids on purpose, exactly as on every other shelf, and the UI flags
them with the gold "in 2 omnibuses" pill. Drop `wakanda-o1` and the shelf has
no overlap at all.

Two Black Panther series were **already coded by other shelves** and are
repeated verbatim in this module's `SERIES_EXTRA`: `bp98` (Moon Knight's, for
the Priest run T'Challa and Marc Spector share) and `bp16` (Wolverine's). The
id store is shared and the same comic has to key the same way everywhere.
`bp` on its own is deliberately unused — there is no single Black Panther
series to give it to, and a bare code would read as if there were.

### Marvel deep links

**343 of 350 unique issues (98%) resolve.** The rest fall back to
`marvel.com/search?query=` and a grey Read button, same convention as the other
trackers. Complete: Jungle Action all 19 on the shelf, Black Panther (1977),
(1988), (1998) all 62, (2005) all 41, (2009), (2016) and (2018), plus Rise of
the Black Panther, World of Wakanda, Shuri, Killmonger, Agents of Wakanda, The
Crew and every guest appearance.

**The id harvest was not a step** — the catalog already held everything, so this
was `link_issues.py --write` twice with a regenerate between: 292 matched on the
first pass with **1 ambiguous and 0 rejected**, and 0 of either on the second.
That is the "what a brand-new hero actually gets" number holding up again.

The one ambiguity is a new shape and is worth knowing: **`mvoi-1` had two
candidate series ids, 29653 and 31412, and both hold the same comic** —
`marvels_voices_2020_1`, filed twice by marvel.com. `tiebreak()` genuinely
could not choose because there was nothing to choose between. It is the fifth
entry in `ISSUE_ALIAS`, pinned to 84188, which is the copy flagged as being on
Marvel Unlimited.

The 7 that marvel.com does not have, all re-tested against a fully-swept catalog
before being believed: **Black Panther: Panther's Prey #1–4** (the 1991 prestige
mini — the catalog has no Panther's Prey at all), **Black Panther Saga #1** (a
2008 free primer one-shot), **Astonishing Tales #6** (that series is confirmed
short at source — see the FF shelf) and **What The--?! #9** (the catalog holds
exactly one issue of it, #20).

### Cover art — the cleanest fetch on the project

`fetch_covers.py --hero black-panther --all` returned **7 fetched, 0 failed**,
and unlike Captain America and Iron Man **every one of them is a real jacket**.
Checked on a contact sheet, as the rule requires: all seven carry omnibus trade
dress and a creator credit block, none has a price box or a Comics Code stamp.
Nothing needed hand-fetching by ISBN.

None is `soft` either — the smallest is 600x883 — which makes this the only
shelf on the site with no low-resolution cover on it.

### The page itself

Built from `moonknight-reading-tracker.html`, which is still the one to copy for
a small shelf. What changed beyond the identity sweep:

- **Seven `.o-*` ramps**, all with `SPINE_C` entries and all single-quoted:
  `o-savannah` (ochre into deep olive-black, for the Jungle Action years),
  `o-kirby` (Kirby magenta and orange), `o-attache` (cool slate — Priest's
  political-thriller register), `o-frog`, `o-royal` (gold into purple-black),
  `o-empire` (violet into indigo) and `o-nation`.
- **Four new textures**: `tex-kente` (two crossing chevron bands over a fine
  warp — woven cloth, which is what the Wakandan trade dress is built on in
  every era), `tex-krackle` (coarse Kirby dots, for the volume Kirby drew),
  `tex-vibranium` (an isometric weave) and `tex-nanite` (a fine circuit grid).
  `tex-halftone` and `tex-crosshatch` are kept from the template.
- **The glyph is a panther mask** — one silhouette with two ears, two eye slits
  and a muzzle cut out of it by an SVG `<mask>`, so the ramp behind shows
  through the eyes. Same `split("GID").join(...)` fresh-id mechanism, prefix
  `bp`.
- **`SC`** rewritten for the fifty-five series these seven books collect.

**There is no banner file**, so `hbFallback()` drops to `Art/Heroes/black-panther.jpg`
at `objectPosition:"50% 30%"`. That was rendered and looked at rather than
guessed, and it happens to work very well — the poster is a head-on mask that
fills the band — but it is the fallback, not the intended art. See open item 19.

## The Ghost Rider tracker (omnibus shelf)

Same code as the other ten shelf pages, same tooling, different data: 7
volumes, 288 issue slots, 288 unique issues, all 7 with contents and cover art.
No placeholders. `tools/ghostrider_meta.py` is the hand-written half; run
everything with `--hero ghost-rider`.

Like Moon Knight, Silver Surfer, Iron Man and Black Panther it is **complete**:
the Marvel Database lists exactly seven Ghost Rider omnibuses and all seven are
on it. **Two of them have not shipped** — Danny Ketch Vol. 3 and the Percy book
are both dated October 2026 — and both are on under the amended eligibility
rule, having passed all three gates.

### Scope call — the user put all seven on

Five of the seven needed no judgement: the three Danny Ketch volumes and the
Aaron and Percy books are the Ghost Rider ongoing title and its minis, start to
finish. The other two wear the name and are not Johnny Blaze or Danny Ketch,
and that was a real call the tools could not make — CLAUDE.md's own
placeholder brief had flagged it as "two characters and a scope call before a
single issue is picked". **The user was shown the choice and put both ON.**

- **GHOST RIDER 2099** is Zero Cochrane, a murdered hacker downloaded into a
  warbot in a cyberpunk future. On for the reason Hulk: Maestro is on the Hulk
  shelf — an alternate thread, but every issue in it is a Ghost Rider book, and
  it is a complete 25-issue solo run.
- **COSMIC GHOST RIDER** is Frank Castle, and unlike 2099 it is not a solo run:
  **17 of its 35 issues are Thanos, Guardians of the Galaxy and Avengers
  comics**. That is the shape that keeps Heroes Reborn off the FF shelf and
  Devil's Reign off Daredevil's, and it was the reason to offer it as a
  separate option. The user took it anyway, which is what makes the shelf
  complete.

**What is missing is Marvel's doing, not a scope call, and it is the largest
hole on any shelf on the site.** JOHNNY BLAZE'S ORIGINAL RUN HAS NO OMNIBUS:
Marvel Spotlight #5–12 and Ghost Rider (1973) #1–81 — the 1972 debut, the whole
Friedrich/Ploog era, the character's entire first life — are Epic Collections
and Masterworks only. **So this is the one shelf on the site that does not open
on its own title character.** It starts in 1990 with the man who replaced him.

Three smaller holes, all the same cause:

- **Ghost Rider (2006) #1–19**, Daniel Way's run, which is why the Aaron volume
  opens at #20 rather than #1.
- **Everything between 1998 and 2007** — Devin Grayson's 2001 Marvel Knights
  series and, more painfully, Garth Ennis and Clayton Crain's *Road to
  Damnation* (2005), which is the best-regarded thing the character did in
  twenty years.
- **All-New Ghost Rider (2014)** and every later Robbie Reyes book. Tradd
  Moore's art on that series is the most distinctive any Ghost Rider comic has
  had since Ploog and none of it is collected in omnibus.

The tile notes and the guided tour both say so where the jump shows.

`SHELF` is a reading order that here is also publication order of the material.
The one placement worth stating is that **gr2099-o1 sits with the era it came
out of** rather than being exiled to the end as a cross-era oddity: the Doom and
Ultimate volumes go last on the FF shelf because their contents span decades,
and this one does not — it is two years of a single ongoing, published while
dk-o3 was on the stands.

### Contents

Pulled the same way as the other shelves (the `ReprintOf<N>` MediaWiki call
above), into `tools/ghostrider_contents_raw.json`. **Nothing here is
hand-corrected**, which is only the third time that has been true (Moon Knight
and Iron Man are the others):

- **The ReprintOf fields matched the rendered gallery on all seven volumes**, in
  content and in order.
- **Every page writes the full form** (`Ghost Rider Vol 1 1`), so no gallery
  cross-reference was needed to disambiguate — and the catalog carries eleven
  series simply called "Ghost Rider" for it to have gone wrong on.
- **No doubled spaces, no subtitles after the issue number, no short-form
  entries.** None of the three standing repairs applies.

**One thing about that gallery comparison is worth writing down, because it
reads as four volumes disagreeing with themselves and is not.** Four of these
pages carry an `Image2_ReprintOf` naming the issue whose cover art the DM
variant reproduces, and that link renders *ahead of* the reprint gallery. So a
naive "every issue link on the page, in order" check comes back shifted by one
or two and looks like a reordering. Discount the cover-credit links first —
same hazard as Marvel Fanfare #45 on the Daredevil shelf.

**Danny Ketch Vol. 3 lists GHOST RIDER (1990) #50 twice**, as `ReprintOf28` and
`ReprintOf29` with `ReprintOfStory` 1 and 2. That is the double-length
anniversary issue's two stories, not a duplicate: `gen()` dedupes globally on
first occurrence and the volume comes out at 50 issues. No repair needed.

**The solicit audit could say nothing here** — not one of the seven volumes
carries an explicit `COLLECTING` range, the same worst case as the Daredevil and
Silver Surfer shelves — so the shelf-wide gap check did the whole job, and every
gap it found is one of the four uncollected runs above.

### Chaptering

Three volumes take the automatic per-series chapters. **Four carry
`chapterby="series"`, which is the highest proportion on the site**, and it is
one decision made four times: this shelf is mostly crossovers.

`dk-o2` (22 chapters for 55 issues) and `dk-o3` (28 for 50) are the extreme
cases, and the heuristic would have chunked both into "Part N" — they score 2.5
and 1.8 on the average-run-length test, well inside the month-by-month
crossover band the "parts" strategy exists for. **They are overridden to
`series` anyway, and the reason is what the chapter title is *for*.** The Clone
Saga volumes on the Spider-Man shelf rotate four Spider-Man titles a reader
already knows, so "Part 3" costs nothing. Rise of the Midnight Sons and Siege of
Darkness rotate *Morbius*, *Nightstalkers*, *Darkhold* and *Doctor Strange,
Sorcerer Supreme* — books whose names are the information. Naming them is worth
the long chapter list.

`percy-o1` is the ordinary anthology case (the ongoing with one-shots and both
crossover bookends printed inside it), and `cosmic-o1` needs no override at all:
nine clean chapters, because that book prints each series in a block.

`gr2099-o1` comes out as a single 25-issue chapter, which looks wrong and is
not — the volume is one series and nothing else, the same shape as `mlr-o1` on
the Iron Man shelf.

Two chapter lists look out of order and are not, and both are the book printing
a crossover in reading order: `dk-o2` renders `Ghost Rider (1990) #31, #29–30,
#32–39` (Rise of the Midnight Sons puts #31 after the four launch issues) and
`Ghost Rider/Blaze: Spirits of Vengeance #13, #2–4` (Midnight Massacre). Same
shape as `hudlin-o1`'s Wild Kingdom on the Black Panther shelf.

### Issue ids — no overlaps at all

288 issue slots and 288 unique issues: the fourth shelf after Moon Knight,
Daredevil and Silver Surfer where those two numbers are equal, so nothing
carries the gold "in N omnibuses" pill. The seven books tile seven separate
stretches with nothing reprinted between them.

**One code had to be adopted rather than invented, and the run said so.**
`Ghost Rider/Blaze: Spirits of Vengeance` was pinned as `sov` on the first
build, and `link_issues.py` rejected all 23 issues with "that series already
belongs to another shelf series" — two links under the prefix **`grbsov`** were
already sitting in the shared id store from an old `series_harvest.py` run.
Adopting the existing code is the fix, exactly as the Captain America shelf
adopted Wolverine's `caan1` and `cap18`. **Read the rejection list; it is not
noise.**

Nine other series codes were reused verbatim by `autocode()` because other
shelves already own them (`gr6`, `msmk`, `pwj`, `mcp`, `mhs`, `xm2`, `av18`,
`wolv7`, `spm`, `web`) — that is the mechanism working as designed.

### Marvel deep links

**272 of 288 unique issues (94%) resolve.** The rest fall back to
`marvel.com/search?query=` and a grey Read button, same convention as the other
trackers. Complete: Ghost Rider (1990) all 50, Ghost Rider (2006) all 16,
Ghost Rider (2022) all 21, Ghost Rider 2099 all 25, Marvel Comics Presents all
65, Morbius, Darkhold, Nightstalkers, Ghost Riders: Heaven's on Fire, the whole
35-issue Cosmic Ghost Rider block and every Percy-era one-shot.

The id harvest was not a step — the catalog already held everything, so this was
`link_issues.py --write` twice with a regenerate between: **196 matched on the
first pass with 0 ambiguous**, and 0 of either on the second.

The 16 unlinked issues break down as **15 genuine absences and one standing
rejection**, all re-tested against a fully-swept catalog before being believed:

| Unlinked | Why |
|---|---|
| Spirits of Vengeance #14–16, #19–23 (8) | the catalog holds only #1–13, #17 and #18 of that series; the ids in the gaps are probed and dead |
| Blaze: Legacy of Blood #1–4 | the catalog has no Legacy of Blood at all, under any name |
| Midnight Sons Unlimited #2 | the catalog holds #1, #3, #4 and #6 of it and not #2 |
| Ghost Rider and the Midnight Sons Magazine #1 | a magazine, never digitised — the Epic Illustrated and Hulk! Magazine shape |
| Marvel Holiday Special 1993 | already recorded as absent for the Wolverine and Daredevil shelves |
| Marvel Holiday Special #1 (1991) | **a rejection, not an absence** — see below |

**Two pre-existing mislinks on OTHER shelves were found while building this
one, and both were found by looking at a year rather than a cover.** The
shelf's era spans are derived from `YEARS`, so a volume whose issues span
1990–1992 and reports `actual=1990-2005` is a link pointing at the wrong comic.
Do this check on any new shelf; it costs one node one-liner.

- **`xm2-*` — every one of the eight ids for the wiki's `X-Men Vol 2` pointed at
  X-Men (1963).** They are used by the Wolverine and Black Panther shelves as
  well as this one. `audit_strays()` could not see it because the whole prefix
  was uniformly wrong — there was no dissenting minority to flag — and
  `audit_collisions()` could not, because nothing else claimed those 1963 ids.
  Repointed: #4, #5, #6, #7, #9 and #25 to X-Men (1991), and **#175 and #176 to
  X-Men (2004)**, because the wiki files 1991–2008 as one continuous volume
  where marvel.com splits it at the 2004 renumbering. Those last two are
  **two new standing strays** and are correct.
- **`mhs-1` — Marvel Holiday Special #1 (1991) linked to the 2005 series.** That
  one was written by this shelf's own first pass, and it exposed a real gap in
  the matcher: `tiebreak()` only runs when SEVERAL candidate series carry the
  issue number, and when exactly one does the match was accepted **with no date
  check at all**. Only the 2005 series has a plain #1, so a 1991 comic linked to
  a 2005 one.

  The fix is `era_fits()` in `link_issues.py`, and it generalises: a name match
  is refused when the series' catalog years and the volume's era do not overlap
  within a year. That is the Daredevil `1.50` and Iron Man 2020 precedent again
  — **fix the matcher when the fix generalises**, reach for `NUM_ALIAS` /
  `ISSUE_ALIAS` only when nothing can derive the answer. It gained nothing and
  lost nothing anywhere else, and it moved `tta3-1` from the ownership
  rejection to the era one, which reads better. `mhs-1` is now a permanent,
  legible rejection rather than a wrong link.

### Cover art — six real jackets and one that looks wrong

`fetch_covers.py --hero ghost-rider --all` returned 7 fetched, 0 failed, and the
contact sheet the rule requires found one real problem and one false alarm.

- **`percy-o1` was the real problem.** The wiki's file is the cover *art*
  without the trade dress — no logo, no Marvel box, no creator block — because
  the page declares `Image1_ReprintOf = Ghost Rider Vol 10 1.jpg`. The jacket on
  the shelf now is the flat cover-by-ISBN image (9781302966676) added by hand
  with `covers.py add`. **So do not run `fetch_covers.py --hero ghost-rider
  --all`** — it will put the untrimmed art back.
- **`dk-o3` was the false alarm, and it is worth knowing why.** It has no Marvel
  corner box, no omnibus logo and no credit block either, and it looks exactly
  like Ghost Rider (1990) #46's cover. It is not: Marvel's own retail listing
  for 9781302970161 shows the same image, because the book is titled "Danny
  Ketch Omnibus Vol. 3 **Henry Martinez Cover**" and the jacket really is that
  bare. **Check the ISBN endpoint before overriding a suspect jacket** — it
  settles both cases in one request.

Four of the seven are `soft` (under 500px): `dk-o3` and `percy-o1` because they
are unshipped, `aaron-o1` and `cosmic-o1` because that is what the wiki stores.
Refetch `dk-o3` and `percy-o1` after October 2026.

### The page itself

Built from `moonknight-reading-tracker.html`, which is still the one to copy for
a small shelf. What changed beyond the identity sweep:

- **Seven `.o-*` ramps**, all with `SPINE_C` entries and all single-quoted:
  `o-hellfire` (white-hot into orange into oxblood), `o-midnight` (violet night,
  for the Midnight Sons volume), `o-brimstone` (ember into charcoal), `o-neon`
  (cyan into magenta, for 2099), `o-heaven` (pale gold — Aaron's angels),
  `o-void` (violet space) and `o-pyre` (bone and ash over ember).
- **Five new textures**: `tex-flame` (two sets of licks at slightly different
  angles, so the field reads as moving rather than as stripes), `tex-chain`
  (interlocking ellipses on two offset grids), `tex-circuit`, `tex-tread` (the
  only texture on the site that is about the bike) and `tex-starfield`.
  `tex-halftone` and `tex-crosshatch` are kept from the template.
- **The glyph is a burning skull** — cranium, jaw and cheekbones as one filled
  path, with the eye sockets, nasal cavity and the gaps between the teeth cut
  out by an SVG `<mask>` so the ramp shows through, same trick as the Black
  Panther mask. The flame licks sit *behind* the skull in their own hotter
  gradient. **They needed a second pass**: at the first size they cleared the
  cranium by so little that they read as horns rather than as fire. Render the
  glyph on a coloured square and look at it — the shelf never shows it, because
  every volume has a cover, so a bad glyph is invisible until a cover 404s.
  Same `split("GID").join(...)` fresh-id mechanism, prefix `gr`.
- **`SC`** rewritten for the thirty-seven series these seven books collect.

**There is no banner file**, so `hbFallback()` drops to
`Art/Heroes/ghost-rider.jpg` at `objectPosition:"50% 28%"` — the poster's own
burning skull, which fills a 2.4:1 band unusually well. It is still the
fallback, not the intended art. See open item 19.


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

The practical consequence, since it comes up: **a second computer is a second,
completely independent read.** Opening the site there starts empty, and
everything logged on it stays on it — neither device ever sees the other's
marks, and Start over on one leaves the other untouched. Two parallel
progressions is the default behaviour, not something to arrange. What you
cannot currently do is the opposite: make two devices agree.

## Open items — C.O.M.I.C.S.

1. ~~One of seven subjects has no reading list yet.~~ **Done Aug 2026** — all
   twelve subjects that are not still placeholders now have one (Black Panther
   was the eleventh and Ghost Rider the twelfth, the first two row-three
   placeholders to be curated): Daredevil shipped as the sixth omnibus shelf,
   Silver Surfer as the seventh and Captain America as the eighth. Both of the last two shipped that way rather than as curated
   chronologies, and both **dropped part of their old `HEROES` brief on
   purpose**: Moon Knight's because Lemire's run has no omnibus, Daredevil's
   because "arranged so each run answers the one before it" describes a curated
   read, and an omnibus shelf reproduces the printed books instead. A `desc`
   written while a subject was still "Curating" is a brief, not a spec — expect
   to rewrite it when the shape is decided.
2. **`total` for a new hero is a hardcoded fallback.** It is only used before
   that tracker has ever been opened; after that the published record wins. Keep
   them in sync anyway, or a first visit reports the wrong percentage.
3. **Fifty-seven covers are low-res** (~225–500px wide). Black Panther is the
   one shelf with none — its smallest is 600x883. For all but three that
   is because it is all the Marvel Database stores; the exceptions are the
   **unshipped** volumes, where the only flat jacket anywhere is a retailer's
   thumbnail: `gauntlet-o1` at 340x500 (replace after 3 November 2026),
   `dk-o3` at 399x616 and `percy-o1` at 337x500 (both after October 2026).
   Otherwise — six on the Spider-Man shelf, six on the Hulk shelf,
   eight on the Fantastic Four shelf, two on the Wolverine shelf (`aaron-o1`,
   `xforce-o1`), two on the Moon Knight shelf (`spector-o1`, `huston-o1`), two
   on the Silver Surfer shelf (`slott-o1` at 325x500, `gauntlet-o1` at 340x500),
   twelve on the Captain America shelf (six of them flat jackets taken from
   booksellers because the wiki has only issue covers for those volumes) and
   seven on the Daredevil shelf (`bendis-o1`, `bendis-o2`, `bru-o1`, `bru-o2`,
   `shadow-o1`, `waid-o2`, `soule-o1`) and five on the Iron Man shelf
   (`iim-o2`, `mlr-o1`, `busiek-o1`, `mask-o1`, `tsim-o1`) and four on the
   Ghost Rider shelf (`dk-o3`, `aaron-o1`, `cosmic-o1`, `percy-o1`); see
   "Cover art". Replacing them needs a
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
8. ~~The Hulk shelf still carries an unreleased volume.~~ **Resolved Aug 2026
   by the rule change.** `inc-o4` ships February 2027 and was a standing
   violation of the old rule. It was checked against the new one and passes all
   three gates: 41 issues from real ReprintOf fields, 41/41 linked, and
   `Art/Hulk/inc-o4.jpg` is the genuine Wein/Trimpe/Buscema jacket at 700x1045,
   not a reprint-gallery image. Its `released` went from `"Announced"` to
   `"Feb 2027"` so the tile now reads "Ships Feb 2027" and retires the badge by
   itself.
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
11. ~~Deep links are a long tail on every shelf.~~ **Done Aug 2026** — the
    eleven shelves are at 92–100% (Spider-Man 600/606, Hulk 652/659, Fantastic
    Four 671/688, Wolverine 658/665, Moon Knight 239/260, Daredevil 630/633,
    Silver Surfer 140/141, Captain America 720/725, Iron Man 339/340, Black
    Panther 343/350, Ghost Rider 272/288). The
    remaining 84 are not on marvel.com at all;
    `tools/unlinked.json` names every one, and seven more are standing
    rejections named in every run's report rather than in that file. What closed it was sweeping
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

    **Ghost Rider is the lowest-coverage shelf at 94%, and it is honest.** Its
    sixteen are eight Spirits of Vengeance issues the catalog simply does not
    carry, the four-issue *Blaze: Legacy of Blood*, one Midnight Sons
    Unlimited, a magazine and two Marvel Holiday Specials — all re-tested. The
    same shelf is also where two *pre-existing* mislinks on other shelves were
    finally caught, which is the more useful lesson: see "Two shelf issues on
    one marvel.com comic is a mislink" for the year check that found them.
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
    means the shelf-eligibility rule now has an
    exception on the wall — and since the tiles gained real cover art and lost
    the "Never printed" badge, they look entirely like books you could buy.
    Three signals carry it now: the bold note above the shelf, "0 in print" in
    the shelf count, and "never printed" in each volume's banner. That is the
    floor, and preserving it is the thing to watch if the shelf is ever edited —
    see "A shelf holds books whose tile is finished".
14. **Moon Knight and Iron Man are the two banners still under-size.** All ten
    that exist are in — Black Panther and Ghost Rider both have a shelf and no
    banner at all, which is open item 19, not this one — and seven were replaced in Aug 2026 with the user's own upscales
    — 4096px sources, normalised to the new 2400px target. `moon-knight.jpg` was
    not in that batch and is still the original 1200px; `iron-man.jpg` arrived
    later at 1966px, which misses the threshold by a little. `banners.py audit`
    flags both `soft`. Both are the user's own art, so replacing them means
    asking for a bigger source, not fetching one. Note `wolverine.jpg` is 2398px and deliberately unresized: its
    source was two pixels under the target, which is why the soft threshold is
    90% of `WIDTH` rather than `WIDTH` itself.

    The target was 1800px until that batch. The banner is the only image on the
    site displayed edge to edge, so it is the one that shows softness first on a
    retina display; 2400 covers a 1200pt viewport at 2x, at 300–700KB a page.
    Every one of the seven matched its old plate's aspect ratio exactly, so no
    `object-position` crop needed retuning — expect to re-check that if a future
    replacement is a different piece of art rather than a bigger scan of the
    same one.
15. **A Keep Reading tile credits the volume, not the issue.** `creators` on an
    omnibus is usually exactly the writer and penciler of what it collects, so
    the line is right far more often than not — but on an anthology volume
    ("David Michelinie & various") it is vague, and on a mainline numbered
    volume it names the run's headline team rather than whoever drew that
    issue. The fix is per-issue credits in the raw-contents pull, which is a
    wiki request per issue across 3,553 issues and a real size increase in every
    tracker. Not attempted; the tile says what the data can support.
16. **The tile's bar measures the volume, not the issue.** The user asked for a
    per-issue progress bar, in the streaming sense of "you are 40% through this
    episode". Nothing in this project knows that — an issue is read, skipped or
    neither — so the bar is progress through the volume the next issue sits in
    and the caption is a position ("Issue 12 of 43"). Making it literal would
    mean tracking a page or a percentage per issue, which is a new interaction,
    not a new field.
17. ~~Four books were excluded by date alone and are now eligible.~~
    **Three of four done Aug 2026.** All were run through the three gates:

    | Book | Ships | Verdict |
    |---|---|---|
    | Daredevil Omnibus Vol. 4 | Sep 2026 | **on** — wiki jacket, 44 issues, all link |
    | FF by Dan Slott Vol. 2 | Dec 2026 | **on** — jacket by ISBN, 27 issues, all link |
    | Wolverine: Old Man Logan | Dec 2026 | **on** — jacket by ISBN, 37 issues, all link |
    | Wolverine: The Return of Weapon X | Jun 2027 | **off** — no cover anywhere |

    The Return of Weapon X fails gate three: the wiki page returns the
    `No_Image_Cover.jpg` placeholder, it has no ISBN yet, and no retailer
    carries art. It is worth re-checking once an ISBN appears. Note it also has
    a **scope** problem independent of the gates — it is mostly Weapon X (2002)
    #1–28, the ensemble series CLAUDE.md already records as deliberately off the
    Wolverine shelf, so it may not belong there even when its cover exists.

    `No_Image_Cover.jpg` coming back from `prop=pageimages` is the cleanest
    "there is no cover" signal the wiki gives. Treat it as a hard gate-three
    failure rather than something to work around.
18. ~~The Silver Surfer shelf is missing its middle for three months.~~
    **Done Aug 2026** — the rule changed and `gauntlet-o1` went on, three months
    ahead of its 3 November ship date. It passed all three gates, though its
    cover had to be hand-added because the wiki has no jacket for it; see
    "A shelf holds books whose tile is finished". The shelf is now 4 volumes /
    141 issues and carries every Silver Surfer omnibus that exists.

    One follow-up when the book ships: **refetch that cover.** It is a 340x500
    retailer thumbnail, the smallest on the shelf, and the Marvel Database will
    have a proper scan once the jacket is photographed.

19. **Row three still has no banner art, and two of its subjects now need
    theirs.** All five posters landed in Aug 2026 and their printed logos the
    day after, so the wall itself is finished — fifteen logo plates, no text
    fallbacks. What is missing is `Art/Banners/<id>.jpg` for all five.

    **Black Panther and Ghost Rider are the two that have stopped being free.**
    Both were curated later the same month, so both have a tracker page, and a
    banner is only ever read by a tracker page. Each falls through
    `hbFallback()` to its own poster scan on both its shelf view and every
    volume view: `Art/Heroes/black-panther.jpg` at `objectPosition:"50% 30%"`,
    and `Art/Heroes/ghost-rider.jpg` at `"50% 28%"`.

    That degrade is working exactly as designed and both look good — one is a
    head-on panther mask and the other a burning skull in profile, and each
    fills a 2.4:1 band well, which is luckier than it sounds — so this is "the
    intended art is missing", not "the page is broken". Confirmed by driving
    both pages: the only 404 anywhere on either is its own
    `Art/Banners/<id>.jpg`.

    They are the user's to supply (see "Artwork the user supplies") — do not go
    looking for one. `banners.py add <id> <file>` already accepts both ids, and
    the `<img class="hb-art">` in each tracker already points at the path, so
    dropping the file in is the whole fix with no code change.

    The other three cost nothing until one of them is curated.


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
python3 tools/build_omnibus_data.py --check --hero silver-surfer
python3 tools/build_omnibus_data.py --check --hero captain-america
python3 tools/build_omnibus_data.py --check --hero iron-man
python3 tools/build_omnibus_data.py --check --hero black-panther
python3 tools/build_omnibus_data.py --check --hero ghost-rider

# Every shelf issue that can be linked, is.
# Expect: 0 matched, 0 ambiguous, SEVEN standing rejections (tta3-1, cap8-25,
# mk3-1..4 and mhs-1 -- all deliberate, see "An unmapped series is derived, not
# dropped", "Two shelf issues on one marvel.com comic" and the Ghost Rider
# shelf's link section), exactly ONE collision (Marvel Graphic Novel #67 /
# Wolverine: The Jungle Adventure #1, which really are the same comic under two
# names) and NINE strays -- the seven annuals and half/zero issues marvel.com
# files as their own series, plus xm2-175/176, where the wiki files one X-Men
# volume across a renumbering marvel.com splits. More of either is a bug.
python3 tools/link_issues.py

# Guided tour content round-trips, and every chip/figure it names exists
python3 tools/build_tours.py --all --check

# Homescreen logos. Expect 15/15, every one with an alpha channel -- a logo
# without one renders as a box.
python3 tools/logos.py audit

# Banner art. Expect 11 of 16 in (index plus ten of the twelve subjects that
# have a shelf); the five row-three placeholders are blank, which is open item
# 19, not a regression -- but black-panther AND ghost-rider are now LIVE shelves
# with no banner, so both pages fall back to their poster scan. iron-man and
# moon-knight are soft.
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
python3 tools/covers.py audit --hero silver-surfer
python3 tools/covers.py audit --hero captain-america
python3 tools/covers.py audit --hero iron-man
python3 tools/covers.py audit --hero black-panther
python3 tools/covers.py audit --hero ghost-rider

# Every volume's era string agrees with the years its issues actually carry.
# This is how a whole mislinked PREFIX gets caught -- neither audit in
# link_issues.py can see one, because there is no dissenting minority to flag.
# See "Two shelf issues on one marvel.com comic is a mislink".
node -e 'const fs=require("fs");
  const js=fs.readFileSync("ghostrider-reading-tracker.html","utf8")
    .split("<script>")[1].split("<\/script>")[0];
  const R=new Function(js.slice(0,js.indexOf("const KEY_P"))+"return{OMNI,YEARS};")();
  R.OMNI.forEach(o=>{const ys=o.chapters.flatMap(c=>c.issues)
      .map(i=>R.YEARS[i.id]).filter(Boolean);
    console.log(o.id,"era="+o.era,"actual="+Math.min(...ys)+"-"+Math.max(...ys));});'

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
issues**; the Fantastic Four shelf **19 volumes / 713 issue slots / 688 unique
issues**; the Wolverine shelf **15 volumes / 674 issue slots / 665 unique
issues**; the Moon Knight shelf **7 volumes / 260 issue slots / 260 unique
issues**; the Daredevil shelf **18 volumes / 634 issue slots / 633 unique
issues**; the Silver Surfer shelf **4 volumes / 141 issue slots / 141 unique
issues**; the Captain America shelf **22 volumes / 727 issue slots / 725 unique
issues**; the Iron Man shelf **9 volumes / 341 issue slots / 340 unique
issues**; the Black Panther shelf **7 volumes / 354 issue slots / 350 unique
issues**; the Ghost Rider shelf **7 volumes / 288 issue slots / 288 unique
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
tile there. Drive the dismiss X in the same pass — click it on a tracker and
confirm the tile also leaves the homescreen rail, then mark something in that
volume and confirm it comes back. The touch half needs a real device profile:
`p.devices["iPhone 13"]`, because a desktop Chromium at a 390px viewport still
reports `hover:hover` and the X stays invisible under emulation that looks
mobile. A `pageerror` listener on the page catches the rest — the whole
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
  Pages serves individual files up to 100MB and a site up to 1GB, and the whole
  repo is under 100MB (`Art/` is most of it). Cover art no longer has to be squeezed to fit. `covers.py
  add` still re-encodes to 700px/q82, because consistency across twelve shelves
  is worth more than sharpness on one, but that is now a choice rather than a
  constraint, and a better scan can simply be dropped in.
- **Relative image paths work.** `Art/…` resolves fine from Pages, which is why
  every cover is a path rather than a base64 data URI.
- **It took `comics-mobile.html` down with it, eventually.** That file existed
  only because an artifact is one file per URL. It outlived the artifact by a
  few weeks and was deleted in the same month — see "The mobile build is
  retired". Pages serves the thirteen pages directly and they are responsive,
  so nothing replaced it.
