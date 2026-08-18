# X-Men Messiah Saga Reading Tracker

Single-file web app for tracking a chronological read of the 2008–2010 X-Men
"Messiah saga." Built in a Claude chat session; this file exists so a fresh
Claude Code session can pick it up cold.

## Files

- `xmen-reading-tracker.html` — the entire app. No build step, no package.json,
  no dependencies, no server. Open it directly in a browser.

Everything (data, styles, logic) lives in that one file on purpose. Keep it that
way unless there's a strong reason not to — portability is the point.

## What the app does

Tracks 174 comic issues across 27 story arcs, grouped into 6 acts, in a
researched chronological reading order (not publication order). Per issue you
can: mark read, mark skipped, open it on Marvel, or pull a spoiler summary.

## Architecture

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

### Storage (dual-mode)

`IN_CLAUDE` detects whether `window.storage` exists.
- Inside Claude → `window.storage`
- In a normal browser → `localStorage`

The `store` object abstracts both. Keys:
- `xmen-saga-progress-v2` → `{read:[ids], skip:[ids]}`
- `xmen-saga-summaries-v3` → cached generated summaries
- `xmen-anthropic-key` → user's own API key (browser mode only)

**Bumping a key version wipes that data.** That's the intended mechanism for
invalidating bad cached summaries — it's been used once already (v2 → v3).

Export/import to JSON exists (`exportProgress` / `importProgress`) because
localStorage is fragile. Progress does NOT live in the HTML file — copying the
file to a new machine does not carry progress.

### Summaries — two tiers

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

## Design

Frutiger Aero / early-2000s: sky-blue gradients, glass panels, glossy orbs,
floating bubbles, italic uppercase display type, X-Men gold accents. CSS
variables at `:root`. Progress bars stack green (read) + grey (skipped).
Respects `prefers-reduced-motion`. Mobile breakpoint at 600px.

## Known gaps / open items

1. **30 of 174 issues lack Marvel deep links.** They fall back to a
   `marvel.com/search?query=` URL and render as a grey "Read" button instead of
   gold. These are one-shots and minis (Messiah War prologue, Lucas Bishop,
   Necrosha one-shots, Hellbound, Blind Science, Second Coming #1–2, New
   Mutants, Sex and Violence, King-Size Cable). The 144 resolved IDs were
   obtained by crawling marvel.com; the one-shots were not in the probed ID
   ranges. Resolving them means finding each numeric Marvel issue ID.
   Note: marvel.com 403s full page fetches after a while, but byte-range
   requests (`curl -r 0-160000`) still work, and `aria-label="Next"` nav links
   allow walking a series forward from a seed issue.
2. **One disputed reading order.** X-Force #12–13 currently sits before the
   Messiah War crossover (publication order). Some guides argue Messiah War
   should be read first because X-Force returns from the future slightly earlier
   than they left. Flagged in that chapter's `note`.
3. **Per-issue summary quality varies** for obscure issues even with web search.
   Arc digests are the trustworthy layer.

## Reading order sources

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

## Conventions

- Preserve existing internal issue ids (`unc-495`, `leg-208`, `xfo-14`,
  `cab-25`, `sc-1`…). **They are the storage keys.** Renaming one silently
  orphans that issue's saved progress.
- Adding issues: append to the right chapter's `issues[]`, and add a `MARVEL`
  entry if a real ID is known.
- Adding a chapter: it also needs an `ARC_SUMS[chapterId]` entry, or the arc
  button falls through to a live web lookup.

## Testing

No test suite. Verify changes with:

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
