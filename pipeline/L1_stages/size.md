# L1 · SIZE — risk-based sizing (stage)

> Phase 3. Turn each ENTER/ADD verdict into a share count the risk model allows — never a gut number. Calls L2.
> Output: `ORDERS.md`.

## L2 called
- [risk_model](../L2_modules/risk_model.md) — `module_paper_book size <ticker> --price P --stop S [--core]`:
  shares from `risk_amount / (price − stop)`, capped by max-position %; plus `concentration_check` for the
  theme/correlation caps.

## What this stage does
- For each ENTER/ADD: compute the share count from the **stop distance** (risk = equity × risk% ÷ per-share-risk),
  bounded by **max-position %**. ★core uses the lower **core-risk %** (a starter, not a full bet).
- If DECIDE stamped a name "hard-stop required" (momentum-only / ⚡crowded-short) but the report gave no stop,
  the model falls back to the default stop-% — state that the stop is synthetic, not report-anchored.
- **Enforce the caps as a batch, not per-name:** after tentatively sizing every ENTER, re-run the concentration
  check on the resulting book. If a theme breaches max-theme %, scale the correlated names down together
  (the "one risk unit" is sized once) — do not let five small ENTERs sum past the correlated cap.
- Respect available cash per sleeve (KRW / USD); if cash-constrained, rank by conviction and state what was cut.

## ✅ EXIT CHECK
- [ ] Every ENTER/ADD has a module-computed share count + stop; ★core sized at core-risk %.
- [ ] Post-batch concentration re-checked; correlated breaches scaled down together (logged).
- [ ] Cash-sleeve limits respected; any name cut for cash/caps stated with reason.
