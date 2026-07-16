# L2 · indicators — regime & flow indicators (orchestration)

> Called by L1s. Assembles regime/flow indicators to confirm or refute direction. Composes the below.

## Calls (all `python -X utf8`)
- Macro regime — `python -X utf8 -m module_macro_us --series fed_funds,us_10y,us_2y,real_10y,core_cpi,cpi,unemployment,dxy,vix,m2 --days 120 --json`
  ⚠ always `--json` (markdown view has KR headers; each series carries `label_en`); cite `[FRED]`;
  monthly series (CPI/M2) lag ~1 month — flag staleness (e.g. a VIX print that pre-dates an overnight shock).
  *KR desk: no FRED module → cross-read the same-day US MACRO_REPORT §A.*
- US positioning — `python -X utf8 scripts/us_flow.py --cot` (CFTC COT: net-spec, weekly Δ, 1yr %ile —
  ≥80 crowded-long / ≤20 crowded-short; Tue-close +3–4d lag ⇒ context, not trigger)
  and `python -X utf8 scripts/us_flow.py <TICKERS…>` (FINRA daily short-vol z per name;
  z≥+1.5 spike / z≤−1.5 exit — divergence vs narrative = the order-flow tell).
- Name/sector flow tag — `python -X utf8 -m module_flow <tickers…> --bench SPY|^KS11 --json`
  (🟢/🟡/🔴; KR adds `--names` per-investor actuals; `--positioning` is slow — finalists only).
- News velocity — `python -X utf8 -m module_news_data fts search "<theme>" --count` (corroborant, not primary).

## Output
Regime verdict + per-sector/name flow direction with crowding context.
**The calling L1 uses it to support/refute propositions — never as a standalone buy signal.**
