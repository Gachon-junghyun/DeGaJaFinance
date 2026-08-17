# L2 · risk_model — sizing & concentration (orchestration)

> Called by L1·SIZE. Converts a decision into a share count the risk budget allows, and enforces the
> single-name / correlated-theme caps. Same risk grammar as `scripts/action_bracket.py` (risk% · stop · max-pos).
> Composes L3.

## Calls (all `python -X utf8`)
- Size one name — `python -X utf8 -m module_paper_book size <ticker> --price P [--stop S] [--core] [--fx r]`
  → shares from `risk_amount ÷ (price − stop)`, bounded by max-position %; `--core` uses the lower core-risk %.
  L3 [size_from_risk](../L3_functions/size_from_risk.md) is the atomic per-name computation.
- Concentration guard — `concentration_check` (exposed via `module_paper_book mark`) flags single-name > max-pos%
  and theme > max-theme%. **Run it on the *post-batch* book**, so correlated ENTERs are sized as ONE risk unit
  (the premortem guard), not summed past the cap by accident.
  🚨 **Feed it the MEASURED units, not just the labels** (D9, wired 2026-08-10). The theme cap groups by
  the `theme` string a human typed on the position, so a **parent and its subsidiary with different
  labels count as different risk units** — PLAY15: 6 of the top-20 correlated pairs are holdco–subsidiary.
  ★ No mapping table is needed: residual correlation merges them automatically.
  ```bash
  python -X utf8 scripts/risk_units.py --book --exposure     # → llm_outputs/{date}/RISK_UNITS.json
  python -X utf8 -m module_paper_book mark                   # reads it; label vs measured, side by side
  ```
  `concentration_check(..., units=…)` adds `measured_unit` breaches plus two mismatch flags —
  `unit_split_across_labels` (market says one unit, labels say many ⇒ **cap too loose**) and
  `label_split_across_units` (⇒ cap too tight). Verified on a synthetic book: labels each 33.3% < 40%
  **pass** while the measured unit is **66.7% > 40%** and fails.
  ⚠ The measured units are **window-sensitive** — same 8 names give **5** units at `--days 250` and
  **7** at 500/750, and 500 is an unchosen default (C5). ⇒ report both views and state the `--days`;
  do not replace the label view. ⚠ Do **not** rank windows by the tool's `ARI` — it scored two windows
  with *identical* groupings at 0.239 and 1.0.
- Arithmetic sanity — `python -X utf8 -m module_math_check` on any derived sizing figure that will be reported.

## Output
Per-order share count + stop + binding constraint (risk vs max-pos), plus batch concentration verdict.
**SIZE renders `ORDERS.md` from it; a breach scales the correlated basket down together, not name-by-name.**
