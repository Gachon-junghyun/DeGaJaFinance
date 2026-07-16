# L1 · BET — bet sheet (stage)

> Phase 3. Turn the DEEP sectors' candidates into numbers + business + flow, one file.
> Calls L2. Output: `BET_SHEET.md` — **a single file with per-sector sections** (§A–§E each);
> downstream desks read this exact filename, so never split it.

## L2 called
- [deepdive](../L2_modules/deepdive.md) — `module_valuation --peers` (KR) ·
  `module_fundamentals_us --json` (US XBRL numbers; ⚠ `--json` avoids KR scaffolding) ·
  `us_setup_screener --sector` (US wide-net setups) · `module_math_check` (verify arithmetic).
- [indicators](../L2_modules/indicators.md) — `module_flow --bench SPY|^KS11` per candidate
  (KR adds ⑦ per-investor actuals + ⑧ short balance; US adds `--positioning` for finalists only).

## What this stage does
- **Candidate set per DEEP sector = wide net, not the 3 names you already knew:**
  (deep-agent thesis leaders) ∪ (sector screener setups) ∪ (★LIVE_SHORTLIST names — this last
  one drags in cross-sector LIVE candidates beyond the DEEP sectors; they get their own section).
- Per candidate: §A numbers table (multiples, growth, margins — cross-check XBRL↔yfinance;
  state blanks as blanks) · §B narrative/thesis + freshness placeholder (ALPHA fills) ·
  §C flow/positioning cross-read · §D competition/peers · §E refutation + dated catalyst.
- Include the pre-mortem's **epicenter-starter module** if a cycle GAP was flagged: a partial core
  in the #1 cycle's epicenter exists on the sheet regardless of tape, tape gates only the remainder.
- Sizing language is *influence illustration* only — zero buy/sell recommendation.

## ✅ EXIT CHECK
- [ ] Every DEEP sector has a section; cross-sector LIVE shortlist names included or explicitly dropped with reason.
- [ ] Numbers cross-checked (math_check on any derived figure); blanks are blanks, not guesses.
- [ ] Flow/positioning cross-read present per candidate; BET_SHEET.md written as ONE file.
