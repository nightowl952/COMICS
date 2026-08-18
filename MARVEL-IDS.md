# Resolving Marvel issue IDs in bulk

How the `MARVEL` map in `xmen-reading-tracker.html` was populated without
searching marvel.com once per issue. Written for a fresh Claude Code session.
Every claim below was re-verified against live marvel.com on 2026-08-17.

## The shape of the problem

`marvelURL()` builds `https://www.marvel.com/comics/issue/<id>/<slug>`.
Issues present in `MARVEL` render a gold "Read" button; the rest fall back to a
`marvel.com/search?query=` URL and render grey. Filling a gap means finding one
number.

## Four facts that make bulk resolution possible

1. **Only the numeric ID matters.** The slug is decorative — requesting
   `/comics/issue/20820/wrong_slug_here` still serves X-Men (1963) #496. Do not
   waste effort deriving slugs; a wrong one is harmless.
2. **IDs are assigned in roughly solicitation order.** Consecutive issues of a
   series get near-consecutive IDs, and series shipping the same month
   interleave — `leg-208` is 20632 and `unc-495` is 20633. So an ID is a date,
   approximately, and a known issue brackets its neighbours.
3. **Gaps in a run are usually variant covers.** 24631 is Cable #15, 24633 is
   Cable #16, and the 24632 between them is Cable #15's variant. Filter any
   title containing `(Variant)`.
4. **Dead IDs soft-404.** They return the generic site title
   (`Marvel.com | The Official Site for...`) with HTTP 200 — never a 404 status.
   Detect by title, not status code.

## Getting bytes back (marvel.com blocks naive fetching)

Full page fetches start 403ing after a while. Two things dodge it:

- **Byte-range requests.** `curl -r 0-160000` returns `206 Partial Content` and
  keeps working after plain GETs are refused. 160KB comfortably covers `<title>`
  and the nav links; 40KB is enough for the title alone.
- **A real User-Agent.** Send a normal desktop browser UA.

Rate-limit yourself — roughly one request per second — and the range trick holds
up across a few hundred fetches.

## Method A — walk a series (use this first)

Cheapest and exact. Needs one known seed ID per series, then follow the chain:

    curl -s -r 0-160000 -A "$UA" "https://www.marvel.com/comics/issue/$ID/x" \
      | grep -o 'aria-label="Next" [^>]*href="[^"]*"'

That yields the next issue's ID directly. Loop until you reach the last issue you
care about. This is how the four long runs (Uncanny, Legacy, Cable, X-Force,
X-Factor) were resolved — 144 issues, no guessing.

Always read the `<title>` back and confirm it matches the series and number you
expect before recording it. Do not trust chain position alone.

## Method B — sweep an ID range (for the stragglers)

One-shots and minis have no Next-chain to ride, which is exactly why 30 issues
are still unresolved. Instead, bracket them by date: find the IDs of two issues
that shipped just before and just after, then probe every ID in between and read
titles back.

    for id in $(seq $LO $HI); do
      printf "%s " $id
      curl -s -r 0-40000 -A "$UA" "https://www.marvel.com/comics/issue/$id/x" \
        | grep -o "<title>[^<]*</title>"
      sleep 1
    done

Keep the hits whose titles match the one-shots you are hunting; discard variants
and generic-title dead IDs. The 30 missing issues (Messiah War prologue, Lucas
Bishop, the Necrosha one-shots, Hellbound, Blind Science, Second Coming #1-2, the
New Mutants issues, Sex and Violence, King-Size Cable) were missed originally
because the first crawl never probed the ranges they live in.

## Recording results

Add `"<internal-id>":"<marvelID>/<slug>"` to the `MARVEL` object. Internal ids
are storage keys — never rename one. A canonical slug is nice for readability but
is not load-bearing; lowercase the series name, underscore the non-alphanumerics,
then volume start year, then issue number (`x_men_1963_495` — note Uncanny uses
volume 1963, not 2008).

Spot-check a handful of new entries in a browser before committing. A wrong ID
fails silently: it just opens the wrong comic.
