# L1 · MANDATE_SET — declare the mandate the book is managed against (stage)

> Phase 1 of the wrap desk. Before measuring anything, state **what the book is supposed to look like**:
> sector target weights, the drift band, the cash target, and the beta the client (the human) is paying for.
> Calls L2. Output: `MANDATE.md`.

## L2 called
- [mandate](../L2_modules/mandate.md) — `module_paper_book mandate --set … --band … --map … --target-beta …`
  writes the targets into `paper_book.db`; `mandate` (no flags) prints the standing mandate.

## What this stage does
- **Read the standing mandate first.** If one exists, this stage is a *review*, not a rewrite: a mandate that
  changes every run is not a mandate, and drift measured against a moving target is meaningless. Change it only
  on a stated reason (regime change from the MACRO desk, a new risk budget, a client-level constraint) and
  record that reason in `MANDATE.md`.
- **Set targets per market**, using the universe's own sector strings (`--market us` → GICS sectors,
  `--market kr` → the KRX sector names). Weights are % of total equity; the residual is the cash target — so
  a deliberately defensive book is expressed as targets summing to 80, not as a vague intention to hold cash.
- **Pin the unmapped names.** Any holding outside `us_top300.csv`/`kr_all.csv` (ADRs like TSM, mid-caps) shows
  as `(unmapped)` and would otherwise silently sit outside every sector bucket. Pin it with `--map`.
- **State the beta target and band** (`--target-beta` / `--beta-band`). This is the risk-appetite dial: a book
  mandated at beta 1.0 ±0.15 is making a different promise than one at 1.4.
- ⚠ The mandate is a *constraint*, not a forecast. It says how much of the book may sit in a sector — never
  that the sector will work. Conviction still comes from the research desks.

## ✅ EXIT CHECK
- [ ] `MANDATE.md` written: per-market sector targets + band, cash target (100 − Σ targets), beta target ± band.
- [ ] Σ targets ≤ 100 and every target sector name matches the universe CSV verbatim.
- [ ] No holding left `(unmapped)` — each pinned with `--map` or explicitly declared off-mandate.
- [ ] If the mandate changed from the prior run, the reason is recorded.
