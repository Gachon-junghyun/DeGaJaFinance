# L2 — lens — find methods, register evidence, settle the question

> Callable by any L1 that investigates a dated question. Orchestrates `module_lens` only.
> PREMORTEM registers brackets; HANDOVER starts with `score` then `due`.
> Run every command from the repository root with `python -X utf8`.

## Source of record

`data/lens_ledger.db` owns questions, evidence, probabilities, weights, thresholds, dates, and
outcomes. `data/lens.db` is the separate, derived price database. The old bracket
prose (legacy IDs, master index) is archived byte-identical in `handoff/_archive/2026-10-31/SCENARIOS*.md`;
the live `handoff/SCENARIOS.md` lists the open questions and the brackets that were **not** migrated
(`P###` · `M-###` · colliding `S##-KR`) — settle those by hand. The numbers live in the ledger. Use `find`, `show`, and `due` to read the
current record; do not create a competing numeric ledger in Markdown. Cite the returned Q ID
in the calling stage's output. Preserve the original bracket's information-content, frozen
observable/threshold, implied-move, both-sides, and date-clustering rules.

## Five steps

### 1. Find a method before registering a question

```bash
python -X utf8 -m module_lens find "<question>" --limit 8
python -X utf8 -m module_lens show Q12
```

Inspect similar questions, their outcomes, useful methods, and sample counts before choosing
how to investigate. Explicit `find` combines words and available semantic search; the prompt
hook uses words only. If an open question already covers the same observable and date, reuse
its Q ID rather than registering a duplicate. Otherwise create the question before collecting
its evidence (replace every illustrative Q/e ID below with the ID actually returned):

```bash
python -X utf8 -m module_lens ask "<question>" --subject GOOGL --market US --desk industry_US --settle "YYYY-MM-DD AMC" --observable "text:FY capex guide" --note "<why this question matters>"
```

`ask` also accepts `--legacy S1` for an existing legacy cross-reference and `--asked-at ISO` for
an authentic recorded timestamp. Never backdate a new forecast to bypass the settlement gate.
Choose the settlement date and observable now; freeze the branch thresholds before the event.

### 2. Find evidence — one reading per row

```bash
python -X utf8 -m module_lens ev Q12 "count 30-day estimate revisions up vs down" "1 up : 4 down" --kind estimates --key estimate_revision_30d --supports C --link "<source>" --note "<as-of time and context>"
```

Name a reusable method, not a ticker/date-specific slogan. Record the actual reading, its
source URL/report/evidence ID, and the branch it supports. Omit `--supports` for context-only
rows. Valid kinds: `flow`, `estimates`, `options`, `macro`, `filing`, `news`, `report`, `price`,
`positioning`, `other`. An optional `--weight 25` sets an initial percentage; final weights
are committed together with `think`.

### 3. Dig when evidence is missing; record dead methods

Dig means research with the owning data module or browser unit, then append another `ev`;
there is no `module_lens dig` command. Record unusable attempts as well:

```bash
python -X utf8 -m module_lens ev Q12 "compare supplier order revisions" "No dated comparable series" --kind filing --key supplier_orders --weight 0 --dead "Unavailable before the event" --note "<what was tried>"
```

A dead row always has weight 0. Do not turn missing data into a zero reading, or discard a
failed method silently. Evidence must be collected before an outcome exists.

### 4. Think with evidence and explicit weights

```bash
python -X utf8 -m module_lens advise --item "estimates:estimate_revision_30d:count 30-day estimate revisions up vs down:C" --item "filing:capex_guide:read prior company capex guidance:B" --item "news:capacity_plans:compare dated capacity announcements:A"
python -X utf8 -m module_lens think Q12 --branch "A:50:FY guide above USD 190B" --branch "B:40:FY guide USD 180-190B inclusive" --branch "C:10:FY guide below USD 180B" --weights e3=35,e4=35,e5=30
python -X utf8 -m module_lens show Q12
```

`advise` gives recommended evidence weights and reasons, using impact and learned credit;
with insufficient history it recommends equal weights. The desk may override the recommendation.
`think --weights` records the **actual** weights used, so the override can be evaluated later.
All alive evidence weights must sum to **100%** (CLI tolerance ±0.5); dead rows remain 0.
Always pass explicit weights and inspect `show` after committing. Branch probabilities are a
separate distribution and must also sum to 100% when all are supplied. Repeat `--branch` once
per branch; weight syntax uses `=`, not `:`. Numeric branches may use
`"A:50:<condition>:<lo>:<hi>"`; bounds are half-open `[lo, hi)`, with empty bounds unbounded.
Do not rewrite the observable or threshold after seeing the event.

### 5. Due and resolve — score the observable, then learn

At the first HANDOVER check, run these in order:

```bash
python -X utf8 -m module_lens score
python -X utf8 -m module_lens due
python -X utf8 -m module_lens resolve Q12 A --value "FY26 guide USD 195-205B" --scorer industry_US --link "<release URL>" --note "Raised above the frozen USD 190B threshold"
```

`score` automatically settles supported numeric observables: `px:<TICKER>:<h>` (raw return),
`pxx:<TICKER>:<h>` (same-market excess return), and `fred:<SERIES>:<h>` (level change).
`text:<description>` requires desk judgment through `resolve`. Do not assume other observable
forms auto-score. Price reaction is separate from whether the registered observable fired.
Every past-due question, including another market's question, must be resolved this run or
explicitly recorded as AMBIGUOUS with a reason in the ledger:

```bash
python -X utf8 -m module_lens resolve Q12 AMBIGUOUS --scorer industry_US --note "<why the frozen observable cannot identify a branch>" --link "<source if available>"
python -X utf8 -m module_lens due
```

Use `VOID` only for a genuinely voided question, with a reason. Do not silently carry a due row,
move its date, or change its thresholds to manufacture a result. Automatic AMBIGUOUS outcomes
also need a recorded explanation. Resolution fills Brier and price-horizon fields when the
scoring layer and data are available; unavailable derived values are not invented.
At run end, export the ledger backup; the existing nightly routine runs `score` — `learn` ?
`export`, and the weekly routine runs `calib` (this protocol does not create a scheduler):

```bash
python -X utf8 -m module_lens learn
python -X utf8 -m module_lens export
python -X utf8 -m module_lens calib
```

`export` writes recovery JSONL to `handoff/lens/`; it is a backup, not the source of record.

## Rejections — exit 2 is a failed registration, never a completed step

The CLI returns exit 2 with a one-line reason for:

- `think` on or after the settlement date, except genuinely backfilled questions;
- branch probabilities not summing to 100 when all are given;
- alive evidence weights not summing to 100 (±0.5) after `--weights`;
- a weight referring to evidence belonging to another question;
- a dead evidence row with positive weight;
- `resolve` with a key outside the registered branches, except `VOID` or `AMBIGUOUS`;
- `ev` after the question already has an outcome.

On exit 2, retain the reason in the calling stage's output, inspect `show`, correct the input
without changing the frozen forecast, and retry only when valid. Stop the dependent registration
or exit check until it succeeds. For a missed settlement gate, record the process failure and
resolve the original question or mark it AMBIGUOUS with a reason; never fake a pre-event timestamp.
`hook-prompt` is the exception to error signaling: it reads stdin JSON `{"prompt":"..."}`,
emits at most six lines or nothing, and always exits 0 (target under 2 seconds; hook timeout 10 s).
A quiet hook does not replace explicit `find` or HANDOVER's `score`/`due` calls.

## Worked example — S1-shaped Alphabet capex bracket

Illustrative pre-event transcript, not a new historical forecast or verified market readings.
The registration commands would have had to run **before 2026-07-22**; do not execute them now
or use `--asked-at` to bypass that gate. Assume `ask` returned Q12 and the next evidence IDs
were e3/e4/e5 (alive) and e6 (dead):

```bash
python -X utf8 -m module_lens find "Alphabet FY26 capex guidance"
python -X utf8 -m module_lens ask "Will Alphabet change FY26 capex guidance?" --subject GOOGL --market US --desk industry_US --settle "2026-07-22 AMC" --observable "text:FY26 capex guide" --note "A raise confirms volume; a cut can falsify the memory thesis"
python -X utf8 -m module_lens ev Q12 "count 30-day estimate revisions up vs down" "1 up : 4 down" --kind estimates --key estimate_revision_30d --supports C --link "<pre-event estimate source>"
python -X utf8 -m module_lens ev Q12 "read prior company capex guidance" "USD 180-190B" --kind filing --key capex_guide --supports B --link "<prior release>"
python -X utf8 -m module_lens ev Q12 "compare dated capacity announcements" "Capacity expansion planned" --kind news --key capacity_plans --supports A --link "<pre-event announcement>"
python -X utf8 -m module_lens ev Q12 "compare supplier order revisions" "No dated series" --kind filing --weight 0 --dead "Unavailable before the event"
python -X utf8 -m module_lens think Q12 --branch "A:50:FY guide above USD 190B" --branch "B:40:FY guide USD 180-190B inclusive" --branch "C:10:FY guide below USD 180B" --weights e3=35,e4=35,e5=30,e6=0
```

First inspect `advise` as in step 4; here the desk chooses 35/35/30 (100 total). After the
release, step 5's `resolve Q12 A --value "FY26 guide USD 195-205B"` records A regardless of
the stock's reaction. Keep the S1 narrative/index cross-reference in the archive; use Q12 to
retrieve the numeric record.
