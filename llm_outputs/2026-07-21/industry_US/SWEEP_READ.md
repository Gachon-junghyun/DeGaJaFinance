# SWEEP read — industry_US · 2026-07-21

> Stage 2 / L1·SWEEP. Universe-wide flow **before** naming anything (anti-tunnel).
> Artifacts: `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` (this dir) · `CYCLE_EXPOSURE.md/.json`
> (day-folder root, script-owned). **All asof the 2026-07-20 close.** No buy/sell calls.
> ⚠ Serial dependency observed: sweep ran to completion before the shortlist (which reads today's
> `SECTOR_FLOW_US.json` by default path). Universe cache fresh — no >8d staleness warning.

## §1 Universe-wide sweep [`sector_flow --market us --json`, us_top300, bench SPY]
**Universe: n=300 · wflow −0.095 · 🟢 12 / 🔴 79.** The tape is net-negative and narrow: **only 12 of
300 names carry an ignition tag, against 79 in distribution.**

| Rank | Sector | wflow | eqflow | Δ (d/d) | 🟢/🔴 | breadth | Read |
|---|---|---|---|---|---|---|---|
| 1 | **Health Care** | **+0.478** | **+0.361** | +0.049 | 2 / 1 | 0.06 | ★ #1 by a wide margin, **and eqflow confirms it is not one mega-cap** |
| 2 | **Energy** | **+0.303** | +0.210 | ★ **+0.273** | **0 / 2** | 0.00 | ★★ **The largest day-over-day ignition on the board — 3.4× the next sector.** ⚠ But **zero 🟢 names** |
| 3 | **Financials** | +0.254 | ★ **+0.369** | +0.080 | **5 / 6** | 0.11 | ★ **eqflow > wflow = breadth-led, not mega-cap-narrow.** The most 🟢 names of any sector |
| 4 | Real Estate | +0.065 | +0.063 | +0.020 | 0 / 3 | 0.00 | ★ **Positive — a third independent method contradicting the RE UW** |
| 5 | Utilities | +0.011 | +0.006 | **−0.094** | 0 / 1 | 0.00 | Flat and **decelerating** — the AI-power headlines are not here |
| 6 | Consumer Disc | −0.036 | −0.144 | −0.124 | 1 / 10 | 0.04 | eqflow far worse than wflow = **the breadth is rotting under the mega-caps** |
| 7 | Consumer Staples | −0.079 | ★ **+0.161** | +0.086 | 0 / 2 | 0.00 | ★ **Inverted: breadth positive, mega-caps negative.** First staples life in 5 runs |
| 8 | Industrials | −0.166 | −0.127 | −0.044 | 2 / **15** | 0.04 | Negative — the sector ETF's silence confirmed at breadth level |
| 9 | **Information Tech** | **−0.216** | ★ **−0.334** | −0.070 | ★ **0 / 30** | **0.00** | ★★ **The worst-breadth sector on the board: 0 green of 56, 30 red** |
| 10 | Materials | −0.303 | −0.290 | −0.024 | 0 / 4 | 0.00 | Confirms the MATR UW |
| 11 | Comm Services | **−0.366** | +0.035 | +0.050 | 2 / 5 | ★ **0.15** | Worst wflow, **but the highest breadth ratio** — mega-cap-led damage, not sector-wide |

### ★ The sweep's single most important cross-check — it CONTRADICTS this run's MACRO call
**MACRO §4 moved IT from UW → Neutral because MU reclaimed its 848.95 kill-line.** The universe sweep,
run on the same 07-20 close, says **IT is the worst-breadth sector in the market: 0 green names out of
56, 30 in distribution, eqflow −0.334 (the most negative on the board).** `MRVL` −0.894, `QCOM` −0.906,
`AMD`-adjacent semis all 🔴분산 with vol_surge 0.57–0.65×.

**Recorded as a contradiction, not reconciled here.** It is exactly the discipline the L1 asks for:
the sweep cross-checks the matrix and never replaces it. **Handed to ROTATION as the deciding evidence
on §4x(b):** one name reclaimed a line on a relief day; **fifty-six names show zero ignitions.**
The honest reading is that **MU's reclaim is a name event, not a sector event** — which is precisely
why MACRO downgraded P2a to CONTESTED rather than promoting IT to OW.

### Other cross-checks worth carrying forward
- **HLTH is #1 in the sweep on the same day XLV was the worst-performing sector (−1.14%).** Flow and
  return disagree by construction: wflow/eqflow measure accumulation, not price. **This is the third
  independent confirmation of MACRO's P7 downgrade** — "broad accumulation, uneven performance" =
  a hedge being accumulated, not a destination being bought.
- **ENRG has the biggest ignition delta (+0.273) and ZERO 🟢 names.** The refiners are accumulating
  (VLO/MPC/PSX all 매집, RS20 +33.2/+30.4/+26.3) but none carries the 🟢가속 tag — which is why they
  are absent from the shortlist below. **A tag filter is not a flow verdict.**
- **STPL's inversion (eqflow +0.161 vs wflow −0.079) is new.** Defensive breadth is finally appearing
  somewhere other than health care. Worth a look in ROTATION; not enough to move a tilt.

## §2 LIVE shortlist [`us_live_shortlist --floor-b 10 --top 15` → 12 names, asof 07-20]
Filter: mcap ≥ $10B · tag 🟢가속 · flow desc. ⚠ **US has no investor-type feed** — the verdict column is
a **FINRA short-pressure proxy**, which is positioning context, never a buy signal.

| Ticker | Name | flow | OBV | RS20 | short z | Verdict |
|---|---|---|---|---|---|---|
| **PYPL** | PayPal | **+1.00** | +0.49 | **+34.3** | **−1.55** | ✅ low-short / short-cover (clean rise) |
| CTAS | Cintas | +0.95 | +0.22 | +18.7 | −0.29 | △ normal |
| **STT** | State Street | +0.91 | +0.14 | +9.1 | **+1.50** | ⚡ crowded-short (squeeze fuel, turn-conditional) |
| ABT | Abbott | +0.89 | +0.30 | +15.6 | +0.70 | △ normal |
| TRV | Travelers | +0.88 | +0.34 | +20.3 | +0.26 | △ normal |
| **TRI** | Thomson Reuters | +0.80 | +0.17 | +22.1 | −0.51 | ✅ low-short / short-cover |
| CB | Chubb | +0.78 | +0.36 | +9.6 | +0.92 | △ normal |
| **EA** | Electronic Arts | +0.71 | **+0.52** | +4.2 | −1.01 | ✅ low-short / short-cover |
| UNH | UnitedHealth | +0.69 | +0.17 | +5.8 | +0.83 | △ normal |
| GRMN | Garmin | +0.67 | +0.20 | +5.1 | +0.37 | △ normal |
| PGR | Progressive | +0.65 | +0.23 | +4.2 | +0.44 | △ normal |
| T | AT&T | +0.50 | +0.18 | +0.4 | +0.98 | △ normal |

★ **Clean rise (🟢 AND low-short/covering): PYPL · TRI · EA.**
⚡ **Squeeze fuel, turn-conditional (not a buy on its own): STT.**

### What the shortlist's COMPOSITION says — read the absences, not just the names
- **Insurance is 4 of 12** (TRV, CB, PGR, + STT in custody/asset servicing). **Health care 2** (ABT, UNH).
  **Business-services/defensive-quality 4** (CTAS, TRI, GRMN, T). **This is a defensive-quality
  rotation signature**, and it independently corroborates the sweep's HLTH #1 / FIN #3 ranking.
- ★ **ZERO Information Technology names.** Consistent with 0 🟢 of 56 above.
- ★ **ZERO Energy names — including the refiners this desk has called its strongest lane for three
  consecutive runs.** Cause identified: the filter requires the 🟢가속 tag and ENRG has 0 green.
  **This is a filter artifact, not evidence against ENRG** — stated explicitly so ROTATION does not
  read the absence as a signal.
- ★ **ZERO defense names**, despite `Lockheed` attention going 2.6× and RTX/GD flipping to accumulating.
  Consistent with MACRO P4's finding that **volume never showed up** (LMT 0.71× · RTX 0.72× · GD 0.88×).

## §3 ★ CYCLE EXPOSURE GAP [`cycle_exposure --json`; registry ↔ REAL KIS book, read-only]
Book ≈ **$8,199** total (₩11,314,206) · invested $5,233 · cash ₩3,559,022.

| Cycle | rank | epicenter % | need ≥ | any-layer % | held epicenter | GAP |
|---|---|---|---|---|---|---|
| AI-compute / semiconductors | 1 | 12.0% | 12.0% | 40.99% | AVGO, NVDA, TSM | 🚨 **GAP** (margin **−0.001pp**) |
| **Energy / oil-refining (Hormuz + Russia crack)** | **2** | **0.0%** | **8.0%** | 23.21% | ***(none)*** | 🚨 **GAP** (margin **−8.00pp**) |
| Missile-defense / rearmament | 3 | 9.49% | — | 9.49% | RTX | ⚪ n/a (no threshold set) |

### Reading the two flags differently, because they are not the same finding
- **AI-compute: a rounding artifact, not a gap.** Epicenter exposure is **12.0% against a 12.0%
  requirement — short by 0.001pp.** Flagging this as 🚨 alongside a −8pp hole would flatten a real
  finding into noise. **Recorded as effectively MET.**
- ★ **Energy/oil-refining: the real GAP, and it is this desk's own thesis pointed at itself.**
  **Rank-2 cycle. Epicenter exposure 0.0%. Required 8.0%.** For three consecutive runs MACRO has
  called refining its **single strongest lane** (P3′; VLO RS20 +33.2%, MPC +30.4%, PSX +26.3%, all
  accumulating, +25–31%/1m), and the book holds **none of it** — only adjacent/fuel names (KMI, LNG),
  i.e. **beta to the consequence, none to the engine.**
  **This is the 2026-07-14 postmortem failure recurring in a different cycle**: the desk was right on
  the analysis and held zero of the epicenter. **The registry's rule applies as written — a 🔴 or
  crowded tape gates ADD *timing*; it does not justify a zero core in a rank≤2 cycle.**
  ⚠ **And the ceasefire proposal makes the timing genuinely two-sided** (MACRO P3 anti-signal) — which
  is an argument about **size and entry**, not about **zero**.

**→ Handed to ALPHA's action bracket (per the L1 rule), and flagged for PREMORTEM**: a both-sides
bracket is required because the epicenter's binary (10-day ceasefire) is live and undated.

---
**EXIT CHECK:** ✅ `sector_flow` sweep complete → **`SECTOR_FLOW_US.json` written to the protocol path**
(`llm_outputs/2026-07-21/industry_US/`, the path `us_live_shortlist` reads); sector ranking + wflow-vs-
eqflow + day-over-day Δ + new-🟢 read, **and the one finding that contradicts this run's own MACRO call
(IT: 0 green / 56, eqflow −0.334) recorded rather than smoothed** · ✅ **`US_LIVE_SHORTLIST.json`
written**; 12 names with FINRA short-pressure verdicts read, **and the shortlist's structural absences
(0 IT, 0 ENRG, 0 defense) diagnosed — the ENRG absence identified as a 🟢-tag filter artifact, not a
signal** · ✅ **CYCLE_EXPOSURE GAP read**: 2 🚨, **triaged rather than passed through** — AI-compute is a
−0.001pp rounding flag (effectively met), **Energy/oil-refining is a real −8.00pp hole in the desk's own
highest-conviction lane**; handed to **ALPHA's action bracket** and flagged to **PREMORTEM** for a
both-sides bracket. **→ proceed to EVENT_ALPHA.**
