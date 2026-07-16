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
- Arithmetic sanity — `python -X utf8 -m module_math_check` on any derived sizing figure that will be reported.

## Output
Per-order share count + stop + binding constraint (risk vs max-pos), plus batch concentration verdict.
**SIZE renders `ORDERS.md` from it; a breach scales the correlated basket down together, not name-by-name.**
