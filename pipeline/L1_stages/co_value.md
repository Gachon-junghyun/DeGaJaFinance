# L1 · CO_VALUE — what is already priced, what I measured, and what the price is worth

> Company stage 6 (all modes; depth by mode). Merges the old SET_DIFF (+ L3 set_difference) and VALUATION.
> **Reads**: upstream files only (DATAPACK, SOURCES, STRUCTURE, MACRO_LINK, MONEY) + global peer multiples (dated) +
> `llm_outputs/SECTOR_ALPHA_MAP_KR.md` row if present. **Writes**: `VALUE.md` (cap **10 KB**).
> **Next stages use**: alpha_delta / risk_unseen (FALSIFY, CO_VERDICT tier), the own target (G4), transition signals (observation points).

## Why one stage
A multiple level decides nothing; the edge is a **set difference**. But without an own target the desk
computed G4 (reward/risk) from the **broker consensus target** — measured 034020: that target was **2028E PER 103×**,
so the desk was passing its own gate with someone else's momentum target. Once an own target existed, G4 flipped to fail.

## Step 1 · Set difference (pure method on two lists already built)
- **① market knows** — consensus target and rating, analyst/news narrative, 52-week implied expectation,
  rally decomposition (earnings-driven vs multiple-driven — from the revision table).
- **② I measured** — labeled findings from CO_FILINGS, CO_STRUCTURE, CO_MACRO, CO_MONEY.
- **② − ① = alpha_delta** (verified, not priced) · **① − ② = risk_unseen** (priced, not confirmed).
- To write «already priced», attach the **list** of what is priced; a bare «밸류 부담» is rejected; high PER is an input to ①.
- 🚨 Before writing «측정 불가» in risk_unseen because «unlisted / private / no audited counterparty», pass driver_link's
  U1 three checks (is the counterparty listed · does a listed firm carry it by equity method/VIE · does the subject name it).
  NVDA 2026-09-03 closed two rows that way (ACIE solvency, OpenAI credit); both were measurable (CRWV/NBIS 10-Q, MSFT equity-method note).
  risk_unseen lists what was **not measured**, not what **cannot be**.
- Sector cross-read: agree or clash with the top-down sector row; a clash is itself alpha or risk.

## Step 2 · Valuation (L3 [valuation_math](../L3_functions/valuation_math.md))
| step | research | report | forensic |
|---|---|---|---|
| split (§A, cite CO_STRUCTURE) | ✔ | ✔ | ✔ |
| implied expectation (§B, ≥ 3 candidate multiples, WACC/g printed) | ✔ | ✔ | ✔ |
| ladder with the **market-price row** + one target (§C route A) | ✔ | ✔ | — |
| scenario PV + ≥ 2 independent cross-checks (§C route B) | — | ✔ | — |
Trust weight: if the revision table shows cuts, write it on the ladder's earnings metric and haircut if needed.
Grade any prior scenario on this name first (`module_lens show <Q>`), then build.
**Transition signals** (with the target): `signal · current value · check date · multiple if met · target then`
(034020: two of three met ⇒ 46.5× → 63×, 55,000 → 74,600). ⚠ A signal without a date is not a signal — the next run never checks it.
Broker target converted to a multiple and printed beside the own target. This step does not decide the trade.

## ✅ EXIT CHECK
- [ ] ① and ② explicit; alpha_delta and risk_unseen populated or «비어있음» with meaning; every «priced» claim carries its list.
- [ ] Parent EV / earnings stated or «상장 자회사 없음»; implied table with ≥ 3 multiples and assumptions printed.
- [ ] research/report: ladder includes the market-price row; **one** target + why + the estimate it hangs on.
- [ ] report: ≥ 2 independent cross-checks. Transition-signal table has dates. Broker target converted to a multiple.
