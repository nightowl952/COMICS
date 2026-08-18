# Cover art and edition metadata for the omnibus shelf

Where to get real cover scans and printed-edition metadata for the 18 volumes on
the Spider-Man shelf, and which source to trust for what. Companion to
`MARVEL-IDS.md`, which covers resolving *issue* deep links; this one covers the
*books*.

Researched 2026-08-18. Read the "What is and isn't verified" section before
trusting any single line here.

## TL;DR — the pipeline is built, run it locally

Everything is scraped **once** and baked into the HTML. The published pages make
no network requests for covers or metadata; they work with the wifi off.

    python3 tools/scrape_covers.py        # the only step that needs network
    python3 tools/build_omnibus_data.py   # bakes covers + metadata into OMNI
    python3 tools/build_single_file.py    # rebuilds comics-mobile.html

The scrape writes `Art/covers/<id>.jpg` and `tools/omnibus_editions.json`, both
committed. The generator base64-encodes the covers into the tracker's `OMNI`
block as `data:` URIs. Re-running it is cheap: it skips volumes already done,
caches every response under `tools/scrape_cache/`, and `--reparse` re-reads that
cache without touching the network.

**Run it from a local clone** — see "Where this can and cannot run" below.

If a volume never resolves, save a cover to `Art/covers/<id>.jpg` by hand. The
generator takes whatever is in that directory and does not care where it came
from.

## What we are trying to fill

Two separate things, from two different kinds of source:

**Cover art** — `cover` on each `OMNI` entry. The render path already exists:
`artHTML()` in `spiderman-reading-tracker.html` checks `o.cover` and swaps the
CSS ramp for an `<img class="artimg">`. Nothing needs building to display a
cover; it needs a URL or a path.

**Edition metadata** — none of this is on `OMNI` today. The entries carry
`creators`, `era`, `released` (month + year, hand-typed) and a prose `note`.
What a printed omnibus actually has, and what a collector wants on the tile:
ISBN-13, page count, cover price, cover artist, exact release date, printing
number, DM/variant cover, and in-print status.

## The constraint that decides the whole design

**The Claude Artifact CSP blocks remote images.** Not just scripts and fetch —
`<img src="https://…">` to any external host is blocked too. `comics-mobile.html`
is one of three published surfaces and it is the one that runs under that CSP.

So hotlinked covers give you:

| Surface | Hotlinked cover |
|---|---|
| GitHub Pages | works |
| local `file://` | works |
| Claude Artifact | **blank** — falls back to nothing, not to the CSS ramp |

That last cell is the problem. `artHTML()` returns *either* the `<img>` *or* the
CSS layers, so setting `cover` on a volume actively removes the placeholder art
that currently looks fine in the artifact.

Both mitigations are now implemented, and hotlinking is not one of them:

1. **Covers are committed and inlined.** `Art/covers/<id>.<ext>` is the source of
   truth; `tools/build_omnibus_data.py` base64-encodes each one into `OMNI` as a
   `data:` URI. That lands in `spiderman-reading-tracker.html` itself, which keeps
   the file self-contained — the project rule that every page carries its own
   data, styles, logic and artwork — and `comics-mobile.html` inherits it for
   free. Works on all three surfaces, offline.
2. **`artHTML()` layers rather than replaces.** The CSS ramp now always renders
   underneath the `<img>`, so a volume with no cover yet, or an image that fails
   to decode, degrades to today's placeholder art instead of a hole.

Measured, with 18 stand-in covers at 45 KB each: `spiderman-reading-tracker.html`
150 KB → 1.23 MB, `comics-mobile.html` 266 KB → 1.35 MB. Comfortably inside the
artifact's 16 MB limit, but the mobile build stops being a small file and every
rebuild carries the whole payload. `--width` on the scraper is the knob; 400px is
the default and is plenty at the size these render.

Base64 is ASCII, so the mobile builder's zero-non-ASCII assertion is unaffected —
verified, it still passes with covers baked in.

Also note the builder asserts **zero non-ASCII bytes** before writing. Base64 is
ASCII, so data URIs are safe there. Do not try to inline raw binary.

## Source survey

### 1. Marvel's own developer API — dead, do not build on it

`developer.marvel.com` / `gateway.marvel.com` is discontinued. Marvel first
stripped character profile data ("this information is too open for the public",
Nov 2025) leaving only cover images, then shut the API down entirely; the
Postman workspace was marked out of commission in June 2026.

This is worth stating plainly because it is the answer you would otherwise reach
for first — it was the one official, key-authenticated, thumbnail-serving,
collection-aware source, and it is gone. Every option below is a workaround for
its absence.

### 2. marvel.com collection pages — best fit for the "keep it through Marvel" rule

Marvel's own site still publishes a product page per collected edition, at the
same shape as the issue pages the tracker already deep-links:

    https://www.marvel.com/comics/collection/<id>/<slug>
    e.g. https://www.marvel.com/comics/collection/48278/annihilation_hardcover

This is the most on-brand source for this project. It is the rights holder
serving their own art from their own CDN, it is the same domain the Read buttons
already point at, and it costs no third party anything.

Everything in `MARVEL-IDS.md` applies unchanged: only the numeric ID matters
(the slug is decorative), IDs are assigned roughly in solicitation order so they
cluster contiguously by format, dead IDs soft-404 with a generic `<title>` at
HTTP 200, and naive fetching gets 403'd — use byte-range requests
(`curl -r 0-160000`), a real desktop UA, and ~1 req/sec.

`tools/harvest.py` already implements the 403-detect-and-back-off loop against
`/comics/issue/<id>/x`. Pointing it at `/comics/collection/<id>/x` is a one-line
change and gives you the same resumable, restart-cheap scan. Collections live in
their own ID block, so one sweep should surface a large run of them at once —
the same property that made the ASM issue sweep (6440–6960) return 441 issues
with no gaps.

Metadata expected on the page: cover image via the `og:image` tag (an
`i.annihil.us` URL), format, page count, price, release date, and the creator
list.

**This is the highest-value lead and the least verified.** See below.

### 3. Marvel Database wiki — best for structured edition metadata, and already our source

`marvel.fandom.com` is where the omnibus *contents* already come from, via the
structured `ReprintOf<N>` fields. The same page carries an infobox with the
edition metadata, and the same MediaWiki API call gets it — just keep the whole
wikitext instead of grepping out the reprint rows. `tools/omnibus_contents_raw.json`
currently retains only `release`, `year` and `issues`, so this is a re-pull, not
a re-parse of what we have.

    curl -s -A "$UA" -G "https://marvel.fandom.com/api.php" \
      --data-urlencode "action=parse" \
      --data-urlencode "page=Amazing Spider-Man Omnibus Vol 1 1" \
      --data-urlencode "prop=wikitext" --data-urlencode "format=json"

Infobox fields to pull: `Image`, `ReleaseDate`, `ISBN`, `PageCount`, `Price`,
`CoverArtists`, `Editors`, `Publisher`, `Format`.

The `Image` field is a filename, not a URL. Resolve it to a real URL with a
second call:

    curl -s -A "$UA" -G "https://marvel.fandom.com/api.php" \
      --data-urlencode "action=query" \
      --data-urlencode "titles=File:Amazing Spider-Man Omnibus Vol 1 1.jpg" \
      --data-urlencode "prop=imageinfo" --data-urlencode "iiprop=url" \
      --data-urlencode "format=json"

That returns a `static.wikia.nocookie.net` URL. Or skip the filename entirely
and use `prop=pageimages&piprop=original`, which returns the page's lead image
directly — for these pages that is the cover.

Coverage is the strong argument here: all 12 wiki-backed volumes are already
known to have pages, and this is the only source that will reliably have the six
**placeholder** volumes too (Venomnibus, JMS, Ultimate, etc.), since those are
pending in the tracker but long since printed.

Licensing: wiki text is CC BY-SA 4.0 and wants attribution. The cover scans are
Marvel's, hosted by Fandom under a fair-use claim — Fandom is not the rights
holder and cannot grant you anything. Re-hosting a scan pulled from Fandom is
weaker ground than pulling the same image off Marvel's own CDN, which is the
main reason source 2 outranks this one for *art* even though this one wins for
*metadata*.

### 4. Open Library — free, keyless, ISBN-addressed, and a good fallback

Once the wiki has given you ISBNs, covers are a bare URL with no key and no
auth:

    https://covers.openlibrary.org/b/isbn/<isbn13>-L.jpg     # L, M or S

and the metadata side is `https://openlibrary.org/search.json?q=…&fields=…`.
Rate limit is 100 requests per IP per 5 minutes, which for 18 volumes is a
non-issue. Data is CC0-ish and the project is Internet Archive-run, so the
posture is friendly.

The catch is coverage: Open Library's cover store is patchy for Marvel
collected editions, and a missing cover returns a placeholder or a 404 rather
than an error you'd notice. Treat it as a fallback tier, not the primary, and
check each result rather than trusting the URL resolved.

### 5. Comic Vine — deepest metadata, non-commercial only

Free API key, 200 requests per resource per hour, actively maintained. Terms
require non-commercial use only, caching responses, and linking back to Comic
Vine wherever you display their data. A personal reading tracker is squarely
inside that. Good for cover artist credits and printing/variant detail that the
wiki infobox sometimes omits. Adds a key to manage, which this project has so
far only done for the X-Men summaries.

### 6. Grand Comics Database — best bulk metadata, explicitly not covers

`comics.org` publishes a **full database dump every two weeks**, free with a
registered account, CC BY-SA 4.0, requiring a visible "Grand Comics Database™"
credit on any page using it. For 18 volumes a dump is overkill, but it is the
right answer if the shelf ever grows to hundreds of books, because it is one
download instead of N scrapes.

For art it is a dead end by policy, not by accident: the GCD claims no copyright
on cover scans, notes they belong to their respective holders, and states
plainly that it **will not distribute cover images in bulk**.

### 7. Google Books / ISBNdb — deprioritise

Google Books is ISBN-addressable and returns thumbnails plus page counts and
publisher blurbs, but it is quota-managed per calling project and returned HTTP
429 with `quota_limit_value: 0` from this environment. It may behave differently
from a residential IP, but it is not something to build a pipeline on. ISBNdb is
paid.

## What was implemented

`tools/scrape_covers.py` does tiers 1 and 3 below against the Marvel Database
wiki, with Open Library as the cover fallback. Tier 2 (marvel.com) is documented
but **not** built, because its page structure could not be verified from here —
see "What is and isn't verified".

The wiki parser reads `| Key = Value` pairs generically rather than assuming one
infobox template, since the omnibus pages do not all use the same one. It unwraps
`[[links]]`, keeps a wrapping template's last argument (so `{{USD|99.99}}` yields
a price instead of vanishing), joins `<br>`-separated creator lists, drops `<ref>`
notes, and prefers a link's target over a `Last, First` display form so
`[[Steve Ditko|Ditko, Steve]]` reads as "Steve Ditko". That parsing was exercised
against realistic hand-written wikitext, not against the live wiki.

The original three-tier plan, for reference:

1. **Marvel Database wiki → all metadata, all 18 volumes.** One `action=parse`
   per page, parse the infobox, write `tools/omnibus_editions.json` keyed by the
   shelf `id` with `{isbn, pages, price, released, coverArtists, editors,
   format, wikiImage}`. This also gets the six placeholders their real release
   dates, which currently read "Contents pending".
2. **marvel.com collection scan → cover art + a per-volume deep link.** Sweep
   the collection ID block with the existing harvester, match titles against the
   shelf, keep `og:image`. A volume that resolves gets a real cover *and* earns
   a "View on Marvel" link on its detail page, matching the issue-level
   convention.
3. **Open Library by ISBN → fallback cover** for anything step 2 misses.

The hosting question from the constraint section is settled: covers are
committed and inlined, never linked.

## Where this can and cannot run

**Not from this Claude Code web session.** This environment's network policy
egress-blocks every host involved. Verified by direct attempt on 2026-08-18:

    openlibrary.org        403 CONNECT (policy denial)
    covers.openlibrary.org 403 CONNECT
    marvel.fandom.com      403 CONNECT
    www.marvel.com         blocked
    gateway.marvel.com     blocked
    developer.marvel.com   blocked
    metron.cloud           blocked
    googleapis.com/books   reachable, but HTTP 429, project quota 0

Run the harvest from a local clone, which is where the existing wiki and
marvel.com harvests were run from and where they are known to work. A session in
an environment with a permissive network policy would also do, but the local
route is proven.

## Status, 2026-08-18

**Metadata: seeded for all 18 volumes.** `tools/omnibus_editions.json` carries
format, publisher, ISBN and page count (14 of 18), plus a marvel.com collection
id for 13 of 18. Gathered by **web search against retail listings**, not the
wiki, because this environment cannot reach marvel.fandom.com. Anchored to the
printing matching each volume's existing `released` month wherever that
printing's figures were quoted; where sources conflicted or only described a
different printing, the field was left empty rather than guessed. Every entry
records `printing` and `source`.

This also settled a question the survey left open: **marvel.com collection pages
are real and findable**, at `/comics/collection/<id>/<slug>` exactly as
predicted. Confirmed ids include 6332 (ASM Vol. 1), 58980 (Vol. 2), 92004 (Roger
Stern), 41736 (Michelinie & McFarlane, 2011 printing) and 42201 (Death of
Ultimate Spider-Man). Note that search surfaces new-printing ids as readily as
first-printing ones — 70527 and 41736 are the same book, eleven years apart.

Still missing a collection id: `utsm-o1`, `larsen-o1`, `mcf-o2`, `clone-o2`,
`ult-o1`.

**Covers: none yet.** No cover can be fetched from a Claude Code web session —
there is no binary fetch path at all, only text search, and the account has a
single environment. `tools/scrape_covers.py` run from a local clone is the only
route, and it will upgrade the metadata to wiki-sourced in the same pass.


## What is and isn't verified

Verified this session: the Marvel API discontinuation; Comic Vine's limits and
non-commercial terms; the GCD dump cadence, CC BY-SA licence and its no-bulk-covers
policy; Open Library's keyless cover URL shape and 100-per-5-minutes limit;
Google Books returning 429 here; the full egress-block list above; and the
`/comics/collection/<id>/<slug>` URL shape, from a live example.

**Not verified, and the first thing to check:** the actual field set on a
marvel.com collection page — whether it exposes `og:image`, page count, ISBN and
a collected-issues list, and whether the collection ID block scans as cleanly as
the issue blocks did. The whole of source 2 rests on that, and it could not be
fetched from here. Probe one known collection ID by hand before writing any
scanner.

Also unverified: the exact infobox field names on a Marvel Database *omnibus*
page. The list above is the Marvel Database trade/novel template's field set;
confirm against a real page's wikitext before parsing, since the wiki uses
several templates and omnibus pages may not use the one documented.

## Rights posture

The reading itself stays on Marvel Unlimited — nothing here changes that, and
none of these sources carry interior pages. Covers are a different question from
comics: they are the marketing face of a book, published to be reproduced, and
every comic database on the internet shows them.

The cleanest posture, in order:

1. **Hotlink Marvel's own CDN.** Marvel serves the art, Marvel bears the
   bandwidth, no copy is made. Breaks in the artifact.
2. **Commit copies for a personal, non-commercial tracker.** Standard practice
   and low risk, but it is redistribution from a public repo. Keep them small —
   thumbnail-scale, not print-scale — since a 400px cover is plainly a
   thumbnail and a 2000px scan is plainly a copy.
3. **Re-host scans pulled from Fandom.** Weakest. Fandom holds no rights to
   grant.

Whatever wins, credit the metadata sources on the page: the Marvel Database
under CC BY-SA, and Comic Vine or the GCD if either is used.
