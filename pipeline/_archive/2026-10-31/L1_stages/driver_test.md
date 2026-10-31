# L1 · DRIVER_TEST — what actually moves this company, and what the market thinks it is buying

> Phase 2. The stage that stands between the datapack and every downstream number. It answers three
> questions in order — **what does it sell** (segments), **what moves each segment** (drivers), **what
> frame is the tape using** (peers) — and it refuses to let the run proceed on a one-word label.
> Calls L2/L3. Output: `DRIVER_TEST.md`.

## Belief
A company is not its sector label, and a thesis inherits the label's blind spots for free. This stage
exists because a desk run on 2026-08-21 modeled a five-segment company entirely off one spread, twice
mis-signed the driver, and wrote up sector beta as name alpha — **all three errors were mechanical and
all three are caught by the three units below.** Nothing here is a judgment; it is the denominator.

## L2/L3 called
- L3 [segment_pnl](../L3_functions/segment_pnl.md) — segment pre-tax income + share of level **and of
  the swing** + the scope-change (consolidation) line. **Cite it from the pack; do not re-pull.**
- L3 [driver_link](../L3_functions/driver_link.md) — one driver per segment ≥10% of level, measured at
  the source, with the **roll guard** applied. Policy drivers get `미확보`, never a price proxy.
- L3 [peer_pricing](../L3_functions/peer_pricing.md) — competing frames → which one the tape moves with.
- [indicators](../L2_modules/indicators.md) — the flow/positioning axis **and its A/B/C grade table**.
  ★ Read the grade table before weighting anything here: an OBV reading is C-grade and may not carry a
  proposition, while RS20/RS60 is A. That table replaces the old 11-branch chart matrix (see below).
- [deepdive](../L2_modules/deepdive.md) — business/filings/valuation/chart, for anything the pack left blank.

## ★ The three mechanical checks, stated as gates
| # | Gate | Fails when | Consequence for the run |
|---|---|---|---|
| **D1** | **Segment coverage** | the named driver covers <80% of pre-tax income | every downstream claim must state the covered share; a thesis may not be written as if it explains the company |
| **D2** | **Roll integrity** | a `>3σ` daily driver move decomposes to **one leg** | the raw series is **not quotable**; report the back-adjusted series and label the roll date |
| **D3** | **Frame attribution** | the subject's recent leg is shared by its peer frame | that leg is **sector beta** and may not be cited as name-specific evidence in BET_VERDICT |

## ⚠ What this stage deliberately does NOT do
It does not rank, size, or conclude. A driver at its 12-month percentile high is evidence the **earnings**
are real — it is silent on whether they are **priced**, which is the valuation stage's job and
[peer_pricing](../L3_functions/peer_pricing.md)'s open question. Reporting a high driver percentile as
bullish is the exact P4 violation this stage was built to stop.

## ⚠ Removed on purpose — the 11-branch chart matrix
The legacy company flow ran an 11-branch technical analysis (`PROMPT_MAP §5`) plus an M1–M4 conflict
matrix. It is **not** in this protocol. Reason: L2 indicators' **A/B/C/REJECTED grade table already does
M1 (weighting) and M3 (uncorrelated confluence) with measurements instead of assertion**, and it grades
OBV — a full branch of the old matrix — as *corroborant only, no leading power once real flow is known*.
Eleven branches printed at equal visual weight is the failure the grade table exists to prevent.
What survives: `module_chart --read` (CHART_READ verbatim) + the grade table + the flow tag's own caveat.

## ✅ EXIT CHECK
- [ ] Segment table present with **share of the swing**, not just share of level; scope-change line filled (`none` is an answer).
- [ ] Every segment ≥10% has a driver row; unmeasurable drivers are `미확보` **with a reason**, not omitted.
- [ ] Roll guard run: `>3σ` days in window listed with their leg decomposition, or "none in window".
- [ ] Peer frames ≥2, each with 2+ pure-plays; dominant frame named; any frame whose earnings share exceeds its tape share named as an open observation point.
- [ ] D1/D2/D3 each marked PASS/FAIL, and each FAIL's consequence written into the file (not just flagged).
