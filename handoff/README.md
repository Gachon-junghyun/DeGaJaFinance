# handoff — the analytical carry between desk runs

> **What this is.** A desk run starts cold. This folder carries *what we currently believe, what we already got wrong,
> which research rules fire, and which dated questions are open*. **When to read:** HANDOVER at run start (the files
> marked "every run" below, in full). **Not here:** run outputs (`llm_outputs/`), the tag ledger (`pipeline/handoff.md`),
> numbers for dated questions (the `module_lens` ledger), and anything older than the live view (`_archive/`).

> **Language**: English, same rule as `pipeline/` — these files are read into the desk context.

## ★ Thinned 2026-10-31 — what changed

The seven ledgers had grown to **4.63 MB read at every HANDOVER**; the 2026-07-25 budget (STANDING_VIEW ≤ 60 KB,
SCENARIOS ≤ 60 KB, RESEARCH ≤ 85 KB) had been breached for two months and only reported. On 2026-10-31 the full files
were moved, byte-identical, to [`_archive/2026-10-31/`](_archive/2026-10-31/README.md) and replaced by thin files with the
**same names** (so stage references keep resolving).

| File | Before (bytes) | After (bytes) | Read |
|---|---:|---:|---|
| `STANDING_VIEW.md` | 967,724 | 30,470 | every run, both desks |
| `STANDING_VIEW_US.md` | 683,599 | 14,105 | US desk; KR desk when it touches a US name |
| `STANDING_VIEW_KR.md` | 668,715 | 12,942 | KR desk; US desk when it touches a KR name |
| `RESEARCH.md` | 970,700 | 30,129 | every run |
| `SCENARIOS.md` | 573,533 | 9,625 | every run |
| `SCENARIOS_US.md` · `SCENARIOS_KR.md` | 565,296 · 204,732 | 1,057 · 1,057 | pointer only |
| **Total read by a desk** | **4,634,299** | **99,385** | −97.9% |

(This README is not loaded by the desk.)

## Files

| File | Holds | Written by |
|---|---|---|
| [STANDING_VIEW.md](STANDING_VIEW.md) | **Shared spine** — regime call · seed measured chain · the asymmetry · **§5 retracted ledger: every `R` ID, one line, never split** · §6 open contradictions · plumbing state | HANDOVER (end of run) |
| [STANDING_VIEW_US.md](STANDING_VIEW_US.md) / [STANDING_VIEW_KR.md](STANDING_VIEW_KR.md) | Per-market registry (one row per name, latest wins) + recent fact rows | that market's HANDOVER |
| [RESEARCH.md](RESEARCH.md) | **The single source for research rules**, ranked by impact (Tier 1 = read earnings, guidance, competition, the money environment; Tier 2 = measurement hygiene) + the live dig list | HANDOVER |
| [SCENARIOS.md](SCENARIOS.md) | How to use the `module_lens` ledger · its open questions · **open brackets not in the ledger** · scoring rules | HANDOVER, PREMORTEM |
| `SCENARIOS_US.md` / `SCENARIOS_KR.md` | Pointers to the above | — |
| `lens/` | `module_lens export` recovery JSONL (backup, not the source of record) | `module_lens export` |
| `ARCHIVE_FACTS.md` | Fact rows expired by `scripts/handoff_compact.py` before 2026-07-29 | (legacy) |
| `_archive/<date>/` | Full prior versions, byte-identical, with a README saying what moved and how to restore | whoever thins |

Older snapshots (`.STANDING_VIEW*.bak_*`, `*.md.bak_*`, `.bak_20260805/`, `.bak_20260806/`, `.presplit_bak_20260729/`)
are untouched.

## Rules (kept from the old README, adjusted)

- **Retractions are append-only and never split by market.** A killed claim must not resurface in either desk; §5 keeps
  every `R` ID with its date and archive line. New retraction = one line in the same format.
- **Every carried claim is tagged `[measured]` or `[inferred]`, with a date and a source path.** Inferred may be carried,
  never cited as evidence. Staleness is explicit: flag anything older than its horizon instead of trusting it.
- **Dated questions live in `module_lens`, not in prose.** Register with `find → ask → ev → think`, settle with
  `score → due → resolve` (`pipeline/L2_modules/lens.md`). Do not keep a competing numeric ledger in Markdown.
- **Size budget, enforced by moving, not by reporting.** Each thin file ≤ 30 KB (SCENARIOS ≤ 15 KB); the desk reads
  ≤ 100 KB here in total. When a file outgrows it, move older blocks to `_archive/<date>/` with a README — **never delete**.
  ⚠ `scripts/handoff_compact.py` assumes the old layout (it asserts §5 byte-identity on the old section shape) — do not
  run it on the thin files until it is updated.
- **Find before you re-measure.** `python -X utf8 -m module_evidence cite <words>` · `where <TICKER>` · `show <M####>` scan
  `handoff/**` including `_archive/`; allocate IDs with `module_evidence next-id <M|D|R|P|C|S>`.
- **This folder is not advice** and holds no position sizing.

## Why it exists (the failure it prevents)

Measured 2026-07-22: six judgments were reversed inside one session, each because the run did not inherit what was
already known (venue migration read as selling, a record YoY print without its negative MoM half, a KR signal applied to
the US, excess return without a benchmark, an unsourced lead/lag claim, hyperscaler earnings not examined at all). None
were data problems; all were carry problems. The 2026-10-31 thinning keeps that purpose: the carry has to be small
enough to actually be read. The full history of this folder's retention rules and toolkit table is in
[`_archive/2026-10-31/handoff_README_pre-2026-10-31.md`](_archive/2026-10-31/handoff_README_pre-2026-10-31.md).

## Change log
- 2026-10-31 — thinned to 99 KB read per run; full ledgers moved to `_archive/2026-10-31/` (orchestra branch K3).
- 2026-07-29 — split by market (spine + halves). 2026-07-25 — retention budget. 2026-07-22 — folder created.
