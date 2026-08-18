# Omnibus cover art

Front covers for all 18 volumes on the Spider-Man shelf, keyed by the shelf id
used in `spiderman-reading-tracker.html` (`asm-o1`, `venom-o2`, …). Nothing in
the app reads these yet — they are here to be laid out.

    <id>.jpg          long edge 1200px — the master, use this one
    small/<id>.jpg    long edge 480px  — for embedding as a base64 data: URI,
                                         which is the only way a cover survives
                                         into a published artifact (their CSP
                                         blocks every external request)
    covers.json       manifest, in shelf order

Each `covers.json` record carries everything a shelf layout needs without going
back to the tracker: `id`, `shelfPosition`, `title`, `vol`, `creators`, `era`,
`released`, `issues`, `chapters`, `contentsPending`, `note`, both file paths with
their pixel sizes, and the `source` the art came from.

`contentsPending` is true for the six volumes that are shelf tiles with no issue
list yet. They have covers like everything else — only their contents are
missing, so a layout should not treat them as artless.

## Where the art came from

The Marvel Database wiki's own cover image for each collected edition, via
`prop=pageimages` — the same wiki the issue lists come from. Two pages are not
the one you would guess: the wiki files the McFarlane omnibus under its
*Complete Collection* cover, and the Death of Ultimate Spider-Man book under
*Ultimate Comics Spider-Man*.

Amazing Spider-Man Omnibus Vol. 1–3 use hand-picked scans already in
`Art/Spider-Man/` instead. Those are the raw cover paintings without the omnibus
trade dress, so they read a little cleaner but sit slightly apart from the other
fifteen, which all carry the book's logo bar. Deleting an entry from `LOCAL` in
`tools/fetch_covers.py` falls that volume back to the wiki cover.

Five volumes only exist on the wiki at roughly 325×500 and are that size here
rather than 1200px: `stern-o1`, `larsen-o1`, `clone-o2`, `ult-o1`,
`ult-death-o1`. `mcf-o1` (459×700) and `utsm-o1` (600×888) are also under the
master size.

## Regenerating

    pip install Pillow
    python3 tools/fetch_covers.py            # all 18, then rewrites covers.json
    python3 tools/fetch_covers.py venom-o1   # just these ids

Full-size downloads are cached in `tools/.cover-cache/` (gitignored), so a rerun
only re-encodes.
