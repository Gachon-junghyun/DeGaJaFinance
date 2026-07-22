# handoff — the standing view carried between runs

> **What this is.** A desk run starts cold. `REPORT/` tells it *what was covered*
> ([`pipeline/handoff.md`](../pipeline/handoff.md) = the mechanical tag ledger), but nothing tells it
> *what we currently believe, what we already pre-committed to, and what we already got wrong*.
> This folder is that missing half — the **analytical carry**, maintained by hand + by the
> HANDOVER stage.

> **Language**: English, same rule as `pipeline/` — these files are read INTO the desk context, and
> the US desk runs English-pure (Korean in context skews the frame). Korean-market facts are fine;
> Korean prose is not.

## Files

| File | Holds | Written by | Read by |
|---|---|---|---|
| [STANDING_VIEW.md](STANDING_VIEW.md) | The live thesis: macro regime, per-name theses, what is measured vs inferred | HANDOVER (end of run) | HANDOVER (start), MACRO |
| [SCENARIOS.md](SCENARIOS.md) | Pre-registered dated branches + their scoring | HANDOVER, PREMORTEM | HANDOVER (start), PREMORTEM |
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

## Rules

- **Append-only for reversals.** A retracted claim is never deleted — it moves to the retracted
  ledger with the measurement that killed it. Deleting it lets it resurface next run.
- **Every carried claim is tagged `[measured]` or `[inferred]`.** An inferred claim may still be
  carried; it may not be cited as evidence.
- **Every scenario carries both branches and a date.** A one-way scenario is not a scenario.
- **Staleness is explicit.** Every entry has `asof`. HANDOVER flags anything older than its horizon
  instead of silently trusting it.
- **This folder is not advice** and holds no position sizing. It is analysis carry only.
