# L1 · STAGE_ORDERS — push recommendations to the KIS order desk (stage) ★mirror-only

> Final phase. Turn the sized decisions into **human-fireable intent cards** on the real KIS order desk stack —
> the same cards that appear in `module_order_desk`. Calls L2. Output: `STAGED_ORDERS.md`.

## L2 called
- [kis_sync](../L2_modules/kis_sync.md) — `module_paper_book stage --from-json <intents.json>` writes
  `out/order_desk/kis_stack.json` (`module_order_desk` intents); optional epistemics feedback for the staged names.

## What this stage does
- Convert each ENTER/ADD/TRIM/EXIT verdict (already sized) into an intent `{market, side, code, qty, price, note}`.
  The **note carries the thesis + gate** (e.g. "epicenter core, tape-independent" / "GATED add — hard-stop required"
  / "TRIM exhausting IPP") so the human sees *why* on the card before firing.
- **The paper book was already updated** (the mirror reflects the applied judgment); STAGE_ORDERS additionally puts
  the SAME actions on the real order desk as a plan.
- **Epistemics feedback:** record each staged name's driving factor to `epistemics/sensitivity/` so the basis
  accumulates and next run can consult it (`learned_sensitivity`).
- ⚠ **Absolute rule:** this writes *intents* only. No order is sent, no `--execute`, no auto-fire. A human opens
  the desk and fires each card individually with its confirmation dialog. Frame every recommendation as analytical /
  illustrative — the desk does not place trades, and this is not licensed financial advice.

## ✅ EXIT CHECK
- [ ] Each sized verdict staged as an intent card (note = thesis + gate); `kis_stack.json` written.
- [ ] Paper book and order stack agree; epistemics factors recorded for staged names.
- [ ] Output states plainly: intents only, human fires each card, not advice, nothing executed.
