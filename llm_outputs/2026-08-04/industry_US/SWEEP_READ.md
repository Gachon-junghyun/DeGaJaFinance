# SWEEP_READ — industry_US · 2026-08-04 · **asof 2026-08-03 settled**

> The numbers live in `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.json`.
> This file holds only what those cannot say. No table below exists in the JSONs.

## 0 · D74 handled, and QUANTIFIED rather than asserted

The US market was **open** at this stage (10:2x ET). The first pull stamped **`asof 2026-08-04`** on a
live bar. **Measured contamination before trimming**, 08-04 live volume as a share of the 08-03
settled bar: **DLR 9.5% · VLO 14.9% · SPY 16.5% · XOM 18.1% · MPC 20.1% · NVDA 21.7% · AMD 38.6%.**
Price drift on the same bar: **AMD +6.11% · NVDA +1.27% · SPY +0.92% · XOM −1.83%.**

⇒ cache backed up (`prices_2026-08-04.pkl.contaminated_bak`), **trimmed to ≤ 2026-08-03**, sweep
re-run. **The output JSON stamps `asof 2026-08-03`.** ★ **This is the fifth D74 firing on a US run and
the first one caught *before* any number was written**, rather than remediated after.

## 1 · Universe headline — three numbers

**n = 300 · board wflow ranges +0.492 (Energy) to −0.270 (Materials) · 14 🟢 / 81 🔴.**

## 2 · ★★★ D126 landed on the ZERO side, and that single fact re-dates every green on the board

**`velocity` is non-null on 0 of 300.** The 08-03 controlled experiment measured this join oscillating
**0/300 ↔ 51/300 on identical data**, manufacturing 10 greens and flipping 3 sector `wflow` signs.
**Today it is 0/300** ⇒ **the gate ran in its M25 form (3-axis unanimity: OBV ∧ RS20>0 ∧ vol_surge≥1.2),
not its M203 form (3-of-4 with a velocity escape).** **Zero of the 14 greens cleared on velocity.**

⇒ **The green count is not comparable to the 08-02/08-03 runs' green counts.** A run-over-run delta in
🟢 across that boundary is measuring the join, not the market. **Stated here so ROTATION does not read
14 vs 24 as a breadth collapse.**

★ **And the blocked side replicates an 8th time across two markets**: **93 names pass
`OBV-매집 ∧ RS20>0`; 79 are blocked; 79 of 79 — 100% — are blocked by `vol_surge` < 1.2 alone.**
**D6 therefore binds every 🟢 count in this run: it is a volume test wearing a flow label.**

## 3 · Cross-checks against the MACRO matrix

### 3a · ⚠⚠ CONTRADICTION — Energy: the money axis and the price axis point opposite ways, and the money axis is the stale one

MACRO put Energy **OW− → UNDER REVIEW** on the settled 08-03 session: **XLE −2.70pp excess, the
board's worst on a +1.42% SPY day**, with **S49 FIRED-B**.

**The sweep, on the SAME settled bar, ranks Energy #1 of 11 on wflow (+0.492) and #1 on eqflow
(+0.407) — and gives it 0 greens and 0 reds.**

**Diagnosed, because the L1 requires an absence to be diagnosed before it is cited:**
**all 16 Energy names are 🟡중립. ELEVEN of the 16 carry `obv_state = 매집` AND positive RS20 — they
pass the accumulation pre-condition — and every one of them is blocked by `vol_surge` alone
(sector maximum 1.19 at BKR; TEN of the eleven sit below 1.00).** ⇒ **the "0 green" is a gate artifact,
exactly the measured 2026-07-21 case, now reproduced on 16 names instead of 3.**

⚠ **CORRECTED AT PREMORTEM (this file first wrote "twelve").** The 12th name was **TRGP, whose
`obv_state` is 매집 but whose RS20 is −0.4** — it fails the pre-condition's second leg. **Caught by
PREMORTEM Lens 4's independent re-count, not by this stage.** The verdict is unchanged; the count is
11 of 16, and the miscount is logged rather than silently fixed (**C1** — re-measure a handed number,
including one you handed yourself).

⇒ **Which side is the money on?** Neither, yet. **`flow_score` is built from 20-day-window objects
(OBV state, RS20) and has absorbed one bad session as a `delta` of −0.075** — the sector's rank is
inherited from the 20 days that preceded the break. **ROTATION must treat the #1 flow rank as a
LAGGING statement about a window that ends on the day the thesis broke, not as a contradiction of it.**

### 3b · ★★ CONFIRMATION — Information Technology, and it is the sharpest number on the board

**wflow +0.017 against eqflow −0.181 · 1 🟢 / 27 🔴 of 56 · delta −0.247 (the board's worst).**
**The mega-cap leg is flat-positive while the breadth leg is deeply negative** — which is
**C8's shape stated in flow terms**, and it independently confirms MACRO's IT **N(split)** and §F/P10's
finding that **S30's FIRED-A reversed to a −9.55 median in one settled session.**
⚠ **W5: "Information Technology" is not the unit here.** 27 reds of 56 is not a sector view.

### 3c · ★ CONFIRMATION — Utilities and Materials, the two UW− tilts, are the board's two worst on BOTH axes

**Utilities −0.234 / −0.229 (1🟢/8🔴) · Materials −0.270 / −0.169 (0🟢/6🔴).** Both negative on
wflow **and** eqflow ⇒ **the UW− tilts are not mega-cap artifacts.** ⚠ **Materials' 0-green may not be
cited as confirmation** — **S36's confirming leg is already disqualified (M273/M238)** for exactly the
`vol_surge` reason §2 measures again here.

### 3d · ⚠ CONTRADICTION — Financials, the OW−, has the board's second-worst flow delta

**wflow +0.093 · eqflow +0.101 · 4🟢/7🔴 · delta −0.121.** The sector is barely positive on flow while
MACRO carries it OW− on the **rate mechanism** (2s10s +0.47), not on flow. ★ **The two are not in
conflict — they are different objects — and this is the run where that must be said out loud**, because
**R32 already killed "breadth-led" as the OW's stated reason** and the flow axis is now offering no
replacement. **The OW− rests on P13′ alone.**

## 4 · Shortlist composition — the ABSENCES are the finding

**14 names of 300 clear `mcap ≥ $10B ∧ 🟢`.**

- **ZERO Energy names**, from the sector with the **#1 wflow on the board** ⇒ **gate artifact, §3a.**
  **This absence is not evidence and may not be cited as one.**
- **ZERO Materials · ZERO Consumer Staples · ZERO Real Estate** — all three have `green = 0` at
  sector level, so the shortlist is reporting the gate, not a scan of those sectors.
- **The list's centre of gravity is insurance / exchanges / payroll-and-services**: MET · TRV · MRSH ·
  ICE · ADP · TRI. ★ **That is the same insurance-and-market-infrastructure node M40/M136 identified
  as Financials' real carrier**, surfacing again from a wide sweep rather than from a thesis.
- **FINRA short verdicts** (the US substitute for KR's investor actuals — **positioning context, never
  a trigger**): **✅ clean rise at BMY (z −2.23) · TRV (−3.34) · MET (−1.55)**; **⚡ crowded-short at
  ICE (+2.74) · MRSH (+2.01) · TRI (+1.61) · ITW (+1.50).**
  ⚠ **TRV carries M150's exhaustion geometry** (98.6% of its 60-day excess in the last 20 sessions)
  **and a clean-rise short read at the same time** — the two axes disagree and **neither is promoted**.
- ⚠ **GRMN tops the list at flow +0.94 and still has no thesis anywhere in the desk's files** — a
  coverage gap logged for the third run, **not a candidate** (a bracket needs a proposition to threaten).

## 5 · Cycle exposure — one ✅ that moved a lot, and one 🚨 whose magnitude is unquotable

| Cycle | rank | epicenter | floor | verdict |
|---|---|---|---|---|
| AI-compute / semiconductors | 1 | **13.56%** | 12.0% | ✅ (**AVGO · NVDA · TSM**) |
| Energy / oil-refining | 2 | **2.88%** | 8.0% | 🚨 **GAP −5.124pp** (**MPC** only) |
| Missile-defense / rearmament | 3 | 8.02% | — | ⚪ no floor set (**RTX**) |

★ **The rank-1 ✅ is not marginal any more.** It ran **8.23% (07-28, GAP) → 13.56% today**, clearing by
**1.56pp** against the 1.1-basis-point clearance M146 measured on 07-25. ⚠ **M146's finding still
binds**: this is **mark-to-market drift on an unchanged held set**, not construction — nothing was
bought, and the movement is the AI names' own prices.

⚠⚠ **The rank-2 🚨 GAP's magnitude may NOT be quoted as a level.** **R39 killed the registry tag it is
computed on** (*"XOM is 0% refining"* is false — its own segment printed $4.1–5.5bn, a four-year high).
**Today the Energy epicenter resolves to MPC alone**, so whether XOM belongs in the numerator is
exactly the open question. ⇒ **the GAP's existence is `[measured]`; its size is `unknown` (C3)** until a
human corrects `data_build/cycles/cycle_registry.json`. **Handed to ALPHA's action bracket in that form.**

## 6 · Hand-forward to EVENT_ALPHA / ROTATION

1. **Energy's #1 flow rank is a lagging 20-day object that ends on the break session.** Do not read it
   as a contradiction of S49-B; do not read the 0-green as evidence either.
2. **IT is the board's clearest split** (wflow +0.017 vs eqflow −0.181, 27🔴/56) — W5 binds.
3. **The green count is not run-over-run comparable** (D126 landed 0/300 today).
4. **The Financials OW− has no flow leg. It rests on P13′ alone.**
5. **🚨 Energy cycle GAP exists; its size is unquotable.** ALPHA's bracket carries it that way.
