# Banner art

One wide image per page that has an above-the-fold banner:

| File | Where it shows |
|---|---|
| `index.jpg` | the C.O.M.I.C.S. homescreen |
| `spider-man.jpg`, `wolverine.jpg`, `hulk.jpg`, `xmen.jpg`, `fantastic-four.jpg`, `moon-knight.jpg`, `daredevil.jpg` | that subject's shelf view |

These are hand-picked, not fetched — see `tools/banners.py`, which is the only
thing that should write here (`add <key> <file>` or `add-folder <dir>`, 2400px
wide at q82).

A missing file is not a broken page. `hbFallback()` in each tracker walks
`Art/Banners/<id>.jpg` → `Art/Heroes/<id>.jpg` → the page's `.hb-fallback` ramp,
so a subject with no banner falls back to its poster scan. The homescreen has no
poster of its own and falls back to the ramp, which is why `index.jpg` is the
one that most wants filling in.

The `.hb` box is roughly 3.4:1 at desktop width. A portrait image works but
`object-fit:cover` takes a band out of the middle of it.
