# Omnibus cover art

Drop `<volume-id>.jpg` / `.png` here — ids are the `id` fields in
`tools/omnibus_meta.py` (`asm-o1`, `clone-o2`, …).

`tools/scrape_covers.py` fills this directory automatically, but nothing checks
where a file came from: hand-saved scans work exactly as well.

`tools/build_omnibus_data.py` base64-encodes whatever is here into the tracker's
`OMNI` block as `data:` URIs. Nothing is fetched at page load — the trackers are
offline-only by design, and the Claude Artifact CSP blocks remote images outright.

Keep them small. Roughly 400px wide is plenty at the size they render, and every
kilobyte here costs ~1.37 KB in *both* `spiderman-reading-tracker.html` and
`comics-mobile.html`.
