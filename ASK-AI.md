# Ask AI — research notes and a proposed design

Written Aug 2026, in answer to: *"What if there was an Ask AI button that could answer
based on the comics I actually have on the shelf?"*

The worry that shaped this document was stated up front and is the thing to keep
holding onto:

> My biggest concern is token usage. And not taking cheap shortcuts in order to save
> tokens, and therefore giving answers that don't have all the necessary context.

Everything below is aimed at that. The conclusion is that the two goals are not
actually in tension here, because the corpus already separates its conclusions from
its prose — see "The distilled layer" below.

Nothing in this document has been built. It is a design and a set of measurements.

---

## 1. What is being asked for

A button that opens a question box. You ask it something in plain English and it
answers **grounded in the fifteen shelves**, with internet access, pointing you at
the right book:

- *"What's the highest rated Captain America run?"* — a reception question.
- *"What run goes closest to eldritch horror?"* — a tone question, and the hard one.
- *"What did people think of Immortal Hulk?"* — a reception question with a web half.
- *"What should I read after the Priest run?"* — a recommendation.
- Anything not about comics at all, answered directly.

The answer should point at volumes on the shelf, with covers, the way the guided
tour's chips already do.

---

## 2. What already exists in the repo

Most of the hard parts are built and shipping. This is worth stating plainly because
it changes the size of the job:

| Piece | Where | State |
|---|---|---|
| Browser → `api.anthropic.com` call | `askClaude()` in every tracker | working |
| CORS from a static page | `anthropic-dangerous-direct-browser-access: true` | working |
| Web search inside that call | `tools:[{type:"web_search_20260209"}]` | working |
| One API key for the whole origin | `comics-anthropic-key`, set from the homescreen gear | working |
| Output cleanup | `tidy()` | working |
| Error mapping | `summaryError()` (`nokey` / `badkey` / `http`) | working |
| Jumping to a volume from a panel | the guided tour's chips → `#/omni/<id>` | working |
| A slide-in panel over the shelf | the guided tour panel | working |
| The knowledge itself | `tools/tours/*.py` + each shelf's `OMNI` | working |

So an Ask AI button is not a new integration. It is a new **prompt**, a new
**payload**, and a **tool loop** around a function that already exists.

### One correction on how it is paid for

The key in the gear is an **Anthropic API key**, billed per token. It is not the
Claude.ai subscription and the subscription does not cover it. Every question costs
money. That is the whole reason section 5 exists.

---

## 3. What the research says

### The pattern that replaced "embed everything"

Anthropic's own guidance calls it **just-in-time context loading**: do not
pre-process the corpus into embeddings. Keep lightweight identifiers in context —
file paths, ids, names — and let the model pull the full text through tools when it
decides it needs it. The companion idea is **progressive disclosure**: the model
sees names and one-line descriptions of everything, and reads the full thing only on
demand. That is how Claude Code works on a repository, and how Skills work.

### The caveat that matters most here

From the same post, and it speaks directly to the "no cheap shortcuts" worry — they
recommend a **hybrid**, not pure just-in-time:

> The most effective agents might employ a hybrid strategy, retrieving some data up
> front for speed, and pursuing further autonomous exploration at its discretion.

And the named tradeoff:

> Runtime exploration is slower than retrieving pre-computed data.

Pure just-in-time is slow and can waste context chasing bad paths. Pure pre-loading
is the thing you were afraid of. The answer is an always-on layer good enough that
the pull is the exception, plus a pull that is always available.

Their closing advice is also worth keeping: **"do the simplest thing that works."**

### What the wider 2026 practice looks like

- Retrieval in 2026 is normally **hybrid** — BM25 plus dense embeddings, fused with
  reciprocal rank fusion, beats either alone.
- **Agentic RAG is production-ready** — retrieval moved *inside* the agent loop
  rather than sitting in front of it, so the model can ask for more evidence,
  rewrite its query, or stop early.
- The cost of that is real: a naive retrieve-once pipeline runs about **$0.001 a
  query** where an agentic one costs roughly **10× that and adds ~5 seconds**.

### Why none of the embedding machinery is needed here

Three reasons specific to this project:

1. **The corpus is small.** The entire knowledge base is under 200k tokens, which
   fits inside a single 1M-token context window with room to spare. Chunking exists
   to solve a problem this project does not have.
2. **There is no server.** Embeddings need a vector store and something to query it.
   This site is static files on GitHub Pages, and keeping it that way is a stated
   project value.
3. **It is already structured.** The tours carry `verdict.standing`, `verdict.cls`
   and `tone.modes` as *fields*. Semantic search over prose exists to recover
   structure that was never written down. Here it was written down.

---

## 4. Measurements

Measured against the repo, not estimated. Token figures are chars ÷ 4.

| Layer | Chars | ~Tokens |
|---|---:|---:|
| Volume + chapter index, 14 generated shelves | 131,103 | **~33,000** |
| Distilled tour layer (see below) | 108,107 | **~27,000** |
| Full tour prose, all 15 heroes | 615,956 | **~154,000** |

Per hero, full tour:

| Hero | Volumes | ~Tokens |
|---|---:|---:|
| The Avengers | 27 | 20,700 |
| Hulk | 17 | 14,600 |
| Captain America | 22 | 12,400 |
| Fantastic Four | 19 | 11,600 |
| Spider-Man | 16 | 12,000 |
| Daredevil | 18 | 11,700 |
| Venom | 10 | 11,100 |
| Doctor Strange | 10 | 10,300 |
| Black Panther | 7 | 10,100 |
| Wolverine | 15 | 9,300 |
| Ghost Rider | 7 | 9,200 |
| Iron Man | 9 | 6,600 |
| Moon Knight | 7 | 5,500 |
| Silver Surfer | 4 | 4,700 |
| X-Men | 4 | 4,200 |

Note the X-Men page's `OMNI` is hand-written and does not parse as JSON, so it is
absent from the index row; it is four volumes and adds little.

### The distilled layer

This is the finding the whole design rests on. For every one of the 192 volume tours,
these fields already exist as structured data:

- `verdict.standing` — the community verdict in a sentence. *This is literally the
  answer to "what's the highest rated X run".*
- `verdict.cls` — `classic` / `mixed` / `low` / `cult`.
- `verdict.body[0]` — why people say so.
- `lede` — what the book is.
- `TOUR.overview.tone.modes` — the tone map. Which volume is the cosmic one, which is
  the funny one, which is the Jekyll-and-Hyde one. *This is the answer to "what goes
  closest to eldritch horror".*

Pulling those into one object is **27,000 tokens** — 18% of the full tour corpus.

**It is not a summary and not a truncation.** It is the conclusion of each tour
lifted out whole. That is the difference between this and a cheap shortcut, and it
is only possible because the tours were written with the verdict as a separate field
rather than as a closing paragraph.

---

## 5. Cost

At Claude Opus 5 rates: **$5 / MTok input**, **$25 / MTok output**. Prompt caching:
a cache **read** is 0.1× input ($0.50 / MTok), a 5-minute cache **write** is 1.25×
($6.25 / MTok), a 1-hour write is 2× ($10 / MTok). Minimum cacheable prefix on
Opus 5 is 512 tokens, so everything here is comfortably cacheable.

### Option A — send everything, every question

Index + all tours = ~187k tokens.

| | Cost |
|---|---:|
| Uncached | **$0.94** per question |
| 1-hour cache write | $1.87, once |
| Cached read | $0.09 per question |

### Option B — layered (the recommendation)

Index + distilled layer = ~60k tokens always on. Full hero tour pulled on demand.

| | Cost |
|---|---:|
| Uncached | $0.30 per question |
| 1-hour cache write | $0.60, once |
| **Cached read** | **$0.03** per question |
| + one hero tour pulled | + $0.06 |
| + output (~800 tokens) | + $0.02 |

So a warm-cache question that needs no pull is about **3¢**; one that pulls a full
hero tour is about **11¢**. The first question of a session pays the $0.60 write.

Option B is roughly **10× cheaper on the always-on floor** than Option A, and gives
up nothing, because Option A's extra 127k tokens are still one tool call away.

### Use the 1-hour TTL, not the 5-minute default

The default cache expires in five minutes. Someone browsing their shelf will read a
page between two questions and miss it every time. The 1-hour write costs 2× instead
of 1.25×, so it **pays for itself after two hits** — which any real session clears.

### What is not in these numbers

- **Web search results enter the context.** A question that triggers three searches
  adds however many tokens those results are. This is genuinely variable and is the
  one line item that cannot be predicted from the corpus.
- **Cache misses on prefix drift.** Caching is a prefix match — one byte changes and
  everything after it is re-billed at full rate. See section 7.

---

## 6. Proposed design

### The shape

```
                        ┌──────────────────────────────────────┐
   always in context    │  system prompt (frozen)              │
   ~60k tokens          │  shelf index      ~33k               │  ← cache_control
   cached, 1h TTL       │  distilled tours  ~27k               │     ttl: "1h"
                        └──────────────────────────────────────┘
                        ┌──────────────────────────────────────┐
   per question         │  the question                        │  ← after the
   (never cached)       │                                      │     breakpoint
                        └──────────────────────────────────────┘
                                        │
                        ┌───────────────┴───────────────┐
                        ▼                               ▼
                 read_tour(hero)                   web_search
                 client-side, in JS               server-side
                 4.2k–20.7k tokens                Anthropic runs it
```

### The always-on layer

One generated file, `ask-index.json`, fetched once by whichever page has the button
and cached in memory. Built by a new `tools/build_ask_index.py` from the fifteen meta
modules and the fifteen tour modules — the same shape as `build_omnibus_data.py` and
`build_tours.py`, and for the same reason: it is derived data and must never be
hand-edited.

It carries, per volume: id, hero, title, creators, era, ship date, issue count, the
shelf `note`, its chapter headings, and the four distilled fields above. Plus each
hero's tone map.

**Why a fetched file rather than inlined.** The portability rule says a page is
self-contained. This bends it, and the justification is that `Art/` already bends it
the same way — covers are relative paths, not data URIs. The alternative is inlining
240KB into all fifteen pages, which is 3.6MB of duplicated data that must be
regenerated in fifteen places. One fetched file is the better trade, and it fails
gracefully: no `ask-index.json` means the button hides itself, exactly as the tour
button hides where no tour is written.

### The tool loop

One client-side tool:

```
read_tour(hero)  →  the full TOUR object for that hero, as JSON
```

The page implements it in JavaScript against the file it already fetched. No network,
no latency beyond the extra API round trip. The loop is the standard one: call the
API, and while `stop_reason === "tool_use"`, execute the tool, append a `tool_result`
block, call again.

`web_search_20260209` sits in the same `tools` array and is executed by Anthropic —
nothing to implement.

That is the entire agentic surface. Two tools. Anthropic's guidance is to promote an
action to a dedicated tool when you need to gate, render, audit, or parallelize it;
nothing here needs gating, so nothing more is warranted.

### The system prompt

The rules that keep the answers honest, and they mirror the guided tour's rules
because the tour is the standard this has to meet:

1. **The shelf is the world.** Recommend only what is on it. When the right answer is
   a book that is not on any shelf, say so plainly and name it — the shelves have
   real gaps (Ennis and Crain's *Road to Damnation*, Vaughan and Martin's *The
   Oath*, Ewing and Ram V on Venom) and pretending otherwise is worse than admitting
   it.
2. **Cite volume ids.** Every recommendation names `<hero>:<volume id>` so the page
   can render it as a chip.
3. **A verdict is reported as a verdict.** "Widely held to be", "readers split on" —
   never as fact. Same rule the tours already hold themselves to.
4. **Pull the tour when the answer needs craft detail.** The distilled layer says what
   a book is and how it landed; it does not say what Trimpe is doing with a figure.
5. **Say when you searched.** A claim from the web is not a claim from the shelf.

### Rendering

Answers come back with `<hero>:<volume>` markers. The page turns them into chips that
close the panel and route to `#/omni/<id>`, reusing the tour's chip mechanism. A chip
can carry the volume's cover, which is already on disk at `Art/<Hero>/<id>.jpg`.

**Interior comic pages do not exist anywhere in this project.** There are 145 jackets
and 284 individual issue covers in `Art/Tours/`, and that is all. It can show you a
cover; it cannot show you a panel.

### Request parameters

| Parameter | Value | Why |
|---|---|---|
| `model` | `claude-opus-5` | |
| `thinking` | `{type:"adaptive"}` | the reasoning is the product here |
| `output_config.effort` | `"medium"` or `"high"` | the summary engine's `"low"` is wrong for this |
| `max_tokens` | ~4000 | answers, not essays |
| `cache_control` | `{type:"ephemeral", ttl:"1h"}` on the last always-on block | section 5 |
| `tools` | `read_tour` + `web_search_20260209` | |

Streaming is worth having so the answer appears as it is written rather than after a
long pause, especially on a question that searches. Not required for a first version.

---

## 7. Things that will bite

- **Prompt caching is a prefix match.** One byte changes anywhere in the prefix and
  everything after it is re-billed. Do not interpolate the date, the question, a
  session id or the user's progress into the system prompt — all of that goes
  *after* the breakpoint. Keep the tool list in a fixed order. Serialize
  `ask-index.json` deterministically, the way `build_omnibus_data.py` already pins
  `json.dumps(..., indent=0, ensure_ascii=False)` with a fixed key order.
- **Verify the cache is actually hitting.** `usage.cache_read_input_tokens` on the
  response. If it is zero across repeated questions, something is invalidating the
  prefix and every question is costing $0.30 instead of $0.03. This fails silently —
  there is no error, only a bill.
- **A tool call is a second HTTP round trip.** A question that pulls a tour is
  visibly slower. With 27k of distilled layer always present, most questions should
  not pull; if they all pull, the distilled layer is not doing its job and that is
  the thing to fix rather than the latency.
- **Web search errors return HTTP 200.** They arrive as a
  `web_search_tool_result` block whose `content` is an error object rather than a
  list. Branch on that before indexing, or a failed search reads as a crash.
- **The chrome duplicates fifteen times.** Same rule as the summary engine and the
  Keep Reading rail. Build it on the homescreen, prove it, then copy.
- **The button needs its own no-key state.** The homescreen gear is where the key is
  set; an Ask AI panel with no key should say so and link there, exactly as the
  summary panel does.

---

## 8. Recommendation

Build the layered version. Specifically:

1. `tools/build_ask_index.py` → `ask-index.json`. The shelf index plus the distilled
   tour layer, ~60k tokens, deterministically serialized.
2. An Ask AI button and panel on `index.html`, modelled on the guided tour panel.
3. `askAI()` beside the existing `askClaude()`: same fetch, cached system block,
   `read_tour` tool, `web_search`, and a `while stop_reason === "tool_use"` loop.
4. Chip rendering for `<hero>:<volume>` markers, reusing the tour's chip handler.
5. Prove it against the four questions in section 1, then copy the chrome into the
   fifteen trackers.

Steps 1–4 are a few hours. Step 5 is mechanical.

**Do not build a vector store, an embedding index or a chunker.** The corpus is
under 200k tokens, there is no server to run one on, and the structure semantic
search would try to recover is already written down as fields.

**If it turns out 60k is not enough** — if answers keep missing things the full
tours would have caught — the fix is not to add retrieval machinery. It is to raise
the always-on layer toward Option A, which is affordable: the ceiling is 9¢ a
cached question with the entire corpus in context. That is the real reassurance on
the original worry. **There is a version of this that takes no shortcut at all and
costs single-digit cents per question.** The layered design is the default because
it is 3× cheaper again, not because the honest version is out of reach.

---

## Sources

- [Effective context engineering for AI agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Prompt caching — Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Claude prompt caching pricing: 5-min vs 1-hour cache (2026)](https://www.respan.ai/articles/claude-prompt-caching)
- [AI Agents Don't Need Vector Search Anymore: the agentic search stack replacing RAG in 2026](https://buzzgrewal.medium.com/ai-agents-dont-need-vector-search-anymore-inside-the-agentic-search-stack-replacing-rag-in-2026-58efcabe4f6f)
- [Progressive Disclosure in AI Agents — MindStudio](https://www.mindstudio.ai/blog/progressive-disclosure-ai-agents-context-management)
- [RAG Techniques Compared: a practical guide, 2026](https://blog.starmorph.com/blog/rag-techniques-compared-best-practices-guide)
- [Rethinking Agentic RAG: toward LLM-driven logical retrieval beyond embeddings](https://arxiv.org/html/2605.27123v1)
