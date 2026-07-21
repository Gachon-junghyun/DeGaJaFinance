# L2 · mandate — sector mandate, drift, beta, rebalance plan (orchestration)

> Called by L1·MANDATE_SET, DRIFT_CHECK, REBALANCE_PLAN. Runs the wrap-account discipline of
> `module_paper_book._allocate`: target weights live **inside** `data/paper_book.db` (no second DB),
> marks reuse `_mark`, concentration caps reuse `_risk`. Composes L3.

## Calls (all `python -X utf8`)
- Declare / inspect the mandate —
  `python -X utf8 -m module_paper_book mandate --market us --band 5 --set '{"Information Technology":25,"Energy":12,…}'`
  · `mandate --market kr --set '{"전기·전자":10,"화학":6}'` · `mandate` (show) · `mandate --json`.
  Weights are **% of total equity (KRW-translated)**; their sum must be ≤ 100 and the residual is the
  **cash target**. Sector strings must match the universe CSVs verbatim
  (`data/kr_universe/kr_all.csv:sector`, `data/us_universe/us_top300.csv:gics_sector`).
- Pin a sector the universe does not know —
  `mandate --map TSM="Information Technology" --map LNG=Energy`. ADRs and non-top300 names resolve to
  `(unmapped)` until a human pins them; the module never guesses a sector.
- Risk-appetite target — `mandate --target-beta 1.00 --beta-band 0.15`.
- Measure — `python -X utf8 -m module_paper_book drift [--fx r] [--period 1y] [--no-beta] [--json]`:
  per-sector target vs current weight, drift in **pp**, band-breach flag, plus the book beta from
  L3 [portfolio_beta](../L3_functions/portfolio_beta.md).
- Plan — `python -X utf8 -m module_paper_book rebalance [--to target|band] [--fx r] [--json] [--commit]`:
  deterministic trims/adds. **DRY-RUN unless a human passes `--commit`**; the plan is always written to
  `out/paper_book/WRAP_REBALANCE_{date}.json`.

## What the module decides — and what it refuses to
Deterministic (module): the drift in pp · the KRW amount to move · which **held** name absorbs it
(trim = smallest stop-distance first, i.e. the weakest; add = largest stop-distance first; ties by size)
· the single-name `MAX_POS_PCT` ceiling and the post-plan `MAX_THEME_PCT` re-check (both from `_risk`).

Refused (protocol's judgment, P4): **which new name enters an underweight sector**. A sector with no
holding returns `NEEDS_CANDIDATE` plus the amount — that gap is handed to INTAKE/DECIDE, never
auto-filled. The module also never decides *whether* a breach should be traded today.

## Output
Mandate table + cash target · per-sector drift/band table · per-name and book beta vs the beta band ·
a trim/add leg list with resulting weights + an unfilled list. **The calling L1 renders
`MANDATE.md` / `DRIFT_REPORT.md` / `REBALANCE_PLAN.md` from it.**
