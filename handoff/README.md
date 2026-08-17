# handoff — the standing view carried between runs

> **What this is.** A desk run starts cold. `REPORT/` tells it *what was covered*
> ([`pipeline/handoff.md`](../pipeline/handoff.md) = the mechanical tag ledger), but nothing tells it
> *what we currently believe, what we already pre-committed to, and what we already got wrong*.
> This folder is that missing half — the **analytical carry**, maintained by hand + by the
> HANDOVER stage.

> **Language**: English, same rule as `pipeline/` — these files are read INTO the desk context, and
> the US desk runs English-pure (Korean in context skews the frame). Korean-market facts are fine;
> Korean prose is not.

## ★ Split by market — 2026-07-29, and what it does NOT change

The 8-run size escalation was resolved by a human: `STANDING_VIEW` and `SCENARIOS` are now **a
shared spine plus a per-market half**. Measured effect: a **KR run reads 314 KB instead of 433 KB
(−119)**; a **US run reads 405 KB (−28)** — the asymmetry is real and is itself the finding, because
the US desk has written 33 of the 46 brackets and 98 of the 176 fact rows.

⚠⚠ **Three things the split deliberately does NOT do:**
1. **§5, the retracted ledger, is NOT split.** A retraction is cross-market by construction — R13
   killed a KR belief the US desk was carrying, R25 killed a US probe the KR desk was using.
   Splitting it would let a killed claim resurface in the other market, which is the exact failure
   the ledger exists to prevent. It stays in the spine, byte-identical, read by both desks.
2. **The master scoring log is NOT split.** An `EXPIRED` row is a process failure in whichever
   market it sits; halving the log would hide half of them from each desk.
3. **Ownership is the REGISTERING desk, not the subject market, and it confers no exclusivity.**
   S5 is about Korean exports and is US-owned; **S8 was registered by US and scored by KR**;
   **S33 and S28 were registered by KR and scored by US**. **A desk with a past-dated row in the
   other file must open that file and score it.**

## Files

| File | Holds | Written by | Read by |
|---|---|---|---|
| [STANDING_VIEW.md](STANDING_VIEW.md) | **SHARED SPINE** — regime call · the seed measured chain · §4 asymmetry · **§5 retracted ledger (never split)** · §6 open contradictions | HANDOVER (end of run) | **BOTH desks, in full** |
| [STANDING_VIEW_US.md](STANDING_VIEW_US.md) | §2 US fact rows + §3a per-name registry | `industry_US` HANDOVER | US desk in full; KR desk only when it touches a US name |
| [STANDING_VIEW_KR.md](STANDING_VIEW_KR.md) | §2 KR fact rows + §3b per-name registry | `industry_kr` HANDOVER | KR desk in full; US desk only when it touches a KR name |
| [SCENARIOS.md](SCENARIOS.md) | **SHARED SPINE** — legend · scoring rules · **the master scoring log** · **the master index of all 46 brackets** | HANDOVER, PREMORTEM | **BOTH desks, in full** |
| [SCENARIOS_US.md](SCENARIOS_US.md) | The 33 brackets registered by `industry_US` | US PREMORTEM/HANDOVER | US desk; KR desk when it scores a US-owned row (it has) |
| [SCENARIOS_KR.md](SCENARIOS_KR.md) | The 13 brackets registered by `industry_kr` | KR PREMORTEM/HANDOVER | KR desk; US desk when it scores a KR-owned row (it has) |
| [RESEARCH.md](RESEARCH.md) | **The single source for research rules** — 21 triggers + 3 lenses + the open dig list | HANDOVER (end of run) | HANDOVER (start), every stage |

### RESEARCH.md is the only place rules live (consolidated 2026-07-22)

Rules were previously split across four documents — `lab/PLAYGROUND_SYNTHESIS.md §7` (9 gates),
`lab/ECONOPHYSICS_THEORY.md §V` (7), the lay-narrative docx §5-5 (9, identical to the first), and
this file (12). Twelve were duplicates. They are now merged here in **trigger form**, and `lab/` is
[the evidence archive](../lab/README.md) — it records *how a finding was derived*, this records
*what to do about it*.

**Why trigger form.** Prose rules do not fire while you work. Measured: of the six reversals below,
**three broke rules that already existed in `lab/`** — and `pipeline/` referenced `lab/` **zero**
times, so they never reached a run. "Subtract the baseline" is true and inert; "the moment you write
*excess return*, is the benchmark in the same sentence?" fires.

**Editing rule**: a new rule is added **here**, in trigger form, with its measured failure — never to
`lab/`. If a rule changes, change it here; the lab anchor stays as the evidence trail.

## Why it exists (the failure it prevents)

Measured over the 2026-07-22 session, six judgments were made and then reversed **inside the same
session** — each reversal caused by something a prior run already knew or could have checked:

1. A cross-listed name's domestic foreign-flow read as directional (it was venue migration).
2. A record YoY export print cited without its negative MoM half.
3. A KR-measured sentiment signal applied to a US index (the source doc says US replication failed).
4. Excess return described without naming the benchmark — the sign flips between SPY and `^KS11`.
5. An unsourced "leads by 12–18 months" claim carried from a desk file and repeated; 16y of data
   showed lag-12 correlation ≈ 0.02 vs same-month 0.63. It is a coincident series.
6. Hyperscaler earnings — the demand side of the whole memory thesis — not examined at all.

None of these were data problems. All were **carry problems**: the run did not inherit what was
already known. That is what this folder fixes.

## Toolkit added 2026-07-22 — run these, they close measured blind spots

A capability nothing invokes is a capability that does not exist (that is the failure this whole
folder was built for). These are the exact commands.

| What | Command | Closes |
|---|---|---|
| **Credit & liquidity** | `python -X utf8 -m module_macro_us --series hy_oas,ig_oas,breakeven_10y,nfci --days 120 --json` | The catalog had **zero** credit spreads. HY OAS is daily — fresher than CPI. Enforced by MACRO EXIT CHECK. |
| **Estimate momentum** | `python -X utf8 -m module_fundamentals_us <TKR>` → §추정치 모멘텀 | Valuation was a snapshot; the denominator's *direction* was invisible. Enforced by DEEP EXIT CHECK. |
| **Implied move** | `python -X utf8 -m module_flow <TKR> --positioning` → `예상변동 ±x%(D±n)` | Scenario thresholds were hand-set. Enforced by PREMORTEM EXIT CHECK. |
| **Rule linter** | `python -X utf8 scripts/report_lint.py <written file>` | Rules depended on the model remembering. Checks C1·C2·S6·D6 mechanically. Enforced by MACRO·ROTATION·DEEP·BET. |
| **Structural calendar** | `python -X utf8 scripts/catalyst_calendar.py --days 12` → `[STRUCTURAL]` block | Lockups, block deals, conversions, index rebalances. The desk logged missing its biggest KR binary **twice**. |
| **Estimate snapshot (daily)** | **Scheduled** — Windows task `DeGaJa-EstimateSnapshot`, daily 08:10 KST via `run_snapshot_estimates.bat`. Manual: `python -X utf8 scripts/snapshot_estimates.py --limit 120` · `--status` | `eps_trend` is a **snapshot, not history** — a single run yields only 2 non-overlapping windows. **Not retroactively recoverable**: every unstored day is gone. Started 2026-07-22, needs ~40 days. |
| **Measure a signal's IC** | `python -X utf8 scripts/measure_ic.py --limit 90` | Turns `--ic` from an assumption into a number — with a built-in concentration check that flips the verdict when the top quintile is one theme. |
| **Sizing under uncertainty** | `python -X utf8 scripts/kelly_size.py <TKR> --ic <가정> --ic-n <n>` | The book sized by **stop distance only** — volatility, edge quality and the edge estimate's own error were absent. 1/4 Kelly + 1.5σ no-trade band (PLAY28). Enforced by SIZE EXIT CHECK. |
| **Long-run margin** | `python -X utf8 scripts/margin_history.py <TKR> --current <gm>` | "A multiple without a margin percentile is not a valuation" (lens L2) — now on our own SEC series, not a press quote. |

⚠ **Two of these carry a trap worth remembering.** `module_flow` needs the **`.KS` suffix** on KR
tickers or it returns empty rows *without erroring*. `margin_history` filters XBRL by **period length**,
not by the `fy` field — `fy` is the *filing* year, so filtering on it pairs mismatched periods and
produces gross margins near **−200%**.

## Retention — this folder is read IN FULL every run, so it has a size budget

★ **Added 2026-07-25, from a measurement.** `handoff/` had grown to **286 KB read at every HANDOVER**,
growing ~30 KB per run. `STANDING_VIEW.md` alone was **132 KB, of which 76% was un-curated per-run
append blocks** — the 07-25 `industry_US` run appended **26.9 KB in one pass, more than the file's
entire live view (25.7 KB)**. Meanwhile the evidence for the file's own top-line regime call (the
84.6% / 59% margin series) appeared **nowhere in the live view** — it was buried in an 07-22 block,
under 100 KB of spent observations.

**The cause was a misread of the rule below.** *"Append-only"* is scoped to **reversals** — the §5
retracted ledger. It was being applied to everything.

| | Rule |
|---|---|
| **Budget** | `STANDING_VIEW` ≤ 60 KB · `SCENARIOS` ≤ 60 KB · `RESEARCH` ≤ 85 KB. Run `python -X utf8 scripts/handoff_compact.py --budget-only` at HANDOVER; a breach is a **finding to report**, not an error. |
| **§2 is ONE table** | A run **appends rows to §2**; it does not open a new `### Added by …` section. Surviving facts carry a `run` column. |
| **§3 is ONE registry** | A run **OVERWRITES the row for a name it touched.** It does not append a per-run per-name block. (Five such blocks, 24.3 KB, were merged on 07-25 — VLO/MPC/PSX had been living in **four** places while §3 still called 009150 *"UNOWNED"* six days after C2 closed.) |
| **Row length** | **≤ 0.35 KB per fact row.** A fact row is *a number plus its source*, not a paragraph — the argument belongs in §3 or in the run's own report. Measured 07-25: 0.59 KB/row. |
| **Expiry** | A fact leaves §2 for `ARCHIVE_FACTS.md` when nothing cites it and it is **not** (a) pinned as load-bearing, (b) from the current run, or (c) the newest member of a replication family. **Nothing is deleted — it moves, and stays greppable.** |
| **Replications collapse** | N measurements of one mechanism become **one row plus a counter**, not N rows. (The 🟢-gate was 5 rows; R7's spread was 4.) |
| **§5 is untouchable** | The compaction script **asserts §5 is byte-identical** before it writes, and refuses otherwise. |

⚠ **Why an archive and not a delete.** The desk's most expensive measured errors come from *losing*
carry, not from carrying too much (see "Why it exists" below, and the 475150 rejections that cost
+41.2pp / +26.9pp). Compaction is only safe because it is a **move**: after the 07-25 pass,
**0 of 154 facts were lost** — 88 live, 80 in the archive.

## Rules

- **Append-only for reversals.** A retracted claim is never deleted — it moves to the retracted
  ledger with the measurement that killed it. Deleting it lets it resurface next run.
  ⚠ **This is scoped to reversals.** It is not a licence to append everything else forever.
- **Every carried claim is tagged `[measured]` or `[inferred]`.** An inferred claim may still be
  carried; it may not be cited as evidence.
- **Every scenario carries both branches and a date.** A one-way scenario is not a scenario.
- **Staleness is explicit.** Every entry has `asof`. HANDOVER flags anything older than its horizon
  instead of silently trusting it.
- **This folder is not advice** and holds no position sizing. It is analysis carry only.
