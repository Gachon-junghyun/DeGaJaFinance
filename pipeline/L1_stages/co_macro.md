# L1 · CO_MACRO — how the financial environment reaches this company's numbers

> Company stage 4 (all modes; short). New 2026-10-31 — no company protocol had this step, so rates,
> dollar, oil and credit never entered a single-name verdict except as a vibe.
> **Reads**: same-day `MACRO_REPORT.md` of the industry desk if it exists (cite, do not redo);
> otherwise FRED via `module_macro_us --json` (`DGS10`, `DTWEXBGS`, `BAMLH0A0HYM2`, `NFCI`, `DFF`) and
> close series for WTI (`CL=F`) and USD/KRW (`KRW=X`) via yfinance — name the source on every value;
> the company's own debt note, FX note and cost structure from the pack. **Writes**: `MACRO_LINK.md` (cap **4 KB**).
> **Next stages use**: the sensitivity rows become CO_VALUE scenario inputs and CO_VERDICT lens evidence (`--kind macro`).

## Rule — measure the **change**, then the **channel**
1. **Change size, not level.** 20-day and 5-day change of 10y yield (bp), dollar index (%), WTI (%),
   HY OAS (bp). Measured (lab/NEWS3D_20261030 E2): S&P same-day |return| on 10y ±10bp days **1.98×** normal,
   ±15bp **3.02×**, WTI ±5% **2.08×**, dollar ±0.7% **2.21×**. Below those bands the environment is
   background — say so in one line and stop.
2. **Channel to this company** — one row per channel that touches the P&L or the multiple:
   `channel · company exposure (from the filing) · direction · size per unit move · source`.
   Channels: floating-rate debt / refinancing wall (debt note) · FX revenue vs FX cost share (FX note;
   KR exporters, USD-reporting subsidiaries) · input cost share (oil, metals) · customer financing
   (capex cycles that run on credit) · discount-rate sensitivity of the multiple (long-duration names).
3. **No channel found ⇒ write «전달 경로 없음»**. A macro paragraph without a company exposure number is the
   decoration this stage replaces.

## Guards
- Monthly series lag ~1 month — state it; do not present CPI/M2 as today's reading.
- KR has no FRED-equivalent module: cross-read the US MACRO_REPORT and the KRW series; do not invent a KR rate path.
- This stage does not forecast the macro path. It converts a measured move into a company number.

## ✅ EXIT CHECK
- [ ] Change sizes printed with source and date; each compared to its band.
- [ ] ≥ 1 channel row with a company exposure figure from the filing, or «전달 경로 없음» stated.
- [ ] Upstream MACRO_REPORT cited by path if it existed (not re-printed).
