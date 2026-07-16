# SECTOR_ROTATION — industry_US · 2026-07-15 (Wed)

> Stage 3 / L1·ROTATION. **Transmission matrix (why) × SECTOR_FLOW sweep (money now)** → 11-sector
> OW/UW + 4 DEEP targets. ⚠ Sweep is **asof 2026-07-14 previous close** — a same-day catalyst
> (June PPI 08:30, any Hormuz move, IBM −23% earnings) is NOT in the flow numbers yet.

---

## §1 Matrix × Flow reconciliation (every AGREE / DIVERGE named)

| GICS | Matrix tilt | Flow rank (wflow / eqflow) | Verdict | Divergence type & owner |
|---|---|---|---|---|
| **Utilities** | Neutral | **#1  0.415 / 0.376 (broad)** | **PROMOTE → OW** | **(b) flow-led, matrix under-rated** — money moved before the thesis (AI-power electricity demand); broad (wflow≈eqflow). → DEEP resolves whether it's early-cycle or a rate-relief bounce |
| **Financials** | OW | **#2  0.361 / 0.33 (broad)** | **AGREE — top OW** | Confirmed: broad flow + **GS/JPM Q2 crush + div hikes** + cool-CPI risk-on. The missed leg, now live |
| Health Care | Neutral | #3  0.316 / **0.366 (breadth)** | nudge → modest OW | (b) flow-led defensive bid (eqflow>wflow = broad); HCA is a clean 🟢 riser. Watch-promote, not DEEP |
| **Information Tech** | OW | #4  0.263 / **0.129 (NARROW)** | **AGREE — top OW, w/ caveat** | wflow≫eqflow = **mega-cap-narrow**: the squeeze is concentrated in mega-caps, not broad. Houses the 🚨 #1 AI-compute cycle → **mandatory DEEP** |
| Real Estate | UW | #5  0.233 / 0.259 | hold UW | Flow better than matrix (rate-relief bounce) but structural long-end ~4.6% keeps it UW. No DEEP |
| Consumer Disc | Neutral→UW | #6  0.232 / 0.15 (narrow) | UW | AGREE; ⚠ correlated-UW with RE (premortem lens-2 checks) |
| Consumer Staples | UW | #7  0.217 / 0.252 | UW | Mild breadth but risk-on rotates out of defensives |
| **Industrials** | OW | **#8  0.207 / 0.213 (lukewarm)** | **OW, rotate DOWN a notch** | **(a) matrix-OW but flow-not-here-yet** — "right thesis, money lukewarm." Continuity sector (06-22). → DEEP must resolve early-vs-trap and LEAD WITH THE DELTA |
| Comm Services | modest OW | #9  0.101 / 0.176 | Neutral→watch | **META is the #1 🟢 ignition** universe-wide (clean short-cover). Watch; folds into BET cross-sector [⚠ "1 of 3" corrected: 46 greens — see below] |
| **Energy** | tactical OW | **#10  0.06 / 0.09 (absent)** | **OW-on-positioning-only, NO DEEP** | **(a) matrix-tactical-OW but flow ABSENT** — the OW is *purely* the WTI crowded-short-13%ile × live-Hormuz squeeze asymmetry, not flow. **Resolution owner = PREMORTEM lens-2 both-sides bracket, not a deep-dive** |
| Materials | UW | #11  0.042 / 0.115 (dead) | **UW** | AGREE — **copper crowded-long 95%ile = overheated**, flow dead, strong-dollar headwind |

### Flow-tape context
- Universe **broadly RED** (green=3, red=21): only **3 🟢-accel names universe-wide** — IBM, META, HCA. Narrow, defensive tape. **[⚠ NaN ARTIFACT — corrected to 46 green / broad risk-on; see DATA-INTEGRITY CORRECTION below]**
- ⚠ **IBM's 🟢 (score 0.887) is a STALE-FLOW TRAP** — the sweep is asof 07-14 prev close; **IBM then crashed −23% on earnings 07-14**. Dropped from consideration. Clean risers = **META, HCA** only.
- **delta = null** this run (first ROTATION here → no day-over-day history yet). No new-🟢 ignition signal available; noted, not inferred.

---

## §2 11-sector OW/UW — final tilt (after reconciliation)

**OW:** Financials · Information Tech · Utilities *(promoted)* · Industrials *(down a notch)* · Energy *(positioning-only)*
**Modest OW / watch:** Health Care · Comm Services (META)
**Neutral:** —
**UW:** Real Estate · Consumer Disc · Consumer Staples · Materials

The two moves the flow forced on the matrix: **Utilities promoted** (flow #1 beat the thesis) and **Industrials cut a notch** (thesis intact, money lukewarm).

---

## §3 — 4 DEEP targets (by rule, not gut)

| Slot | Sector | Rule basis | DEEP mandate |
|---|---|---|---|
| **Continuous-track** | **INDU** | Deep-dived 06-22 AND still top-4 OW today → anti-thrash keeps the slot | **LEAD WITH THE DELTA** (new prints/contracts since 06-22; defense re-rate fired? AI-power moratorium impact?); carry unchanged structure by reference |
| **Rotating** | **FIN** | Top OW; flow #2 broad; **live bank-earnings catalyst this week**; not deep-dived in last ~3 runs (postmortem-corrected promotion) | Full fresh map |
| **Rotating** | **IT** | Top OW; **houses the rank-1 AI-compute cycle the book holds 0% epicenter of (🚨 GAP)**; Nasdaq squeeze | Full fresh map — **epicenter (semis/GPU) is the priority node** |
| **Rotating** | **UTIL** | **Flow #1**, promoted from Neutral (money-before-thesis); never deep-dived here | Full fresh map — resolve early-cycle vs rate-relief-bounce |

**Not selected (stated):**
- **Energy** — matrix-tactical-OW but flow absent (#10). It is a *binary/positioning* play, not a structural deep-dive → **owner = PREMORTEM lens-2** (Hormuz both-sides bracket). Deep-diving a flow-absent sector would be padding.
- No Neutral/UW padding used. 4 is the set (not fewer — all four carry a real OW + a resolution question).

---

---

## ⚠ DATA-INTEGRITY CORRECTION (appended post-run — original §1/§2 above left intact)
The original sweep (asof 07-14) ran during a **transient yfinance failure**: the bulk 300-ticker download
could not align today's bar, so **`last` came back NaN for 87% of names and `rs20`/`rs60` (relative-strength
vs SPY) were 100% NaN.** `flow_score` still computed by skipping the dead axis, but **RS is a 🟢-ignition
trigger** — so with it NaN the sweep reported only **3 green names** universe-wide and painted a "narrow,
defensive tape." A refreshed sweep (asof **07-15, 0% NaN**) corrects this:

| | Corrupted (RS-less, used above) | Corrected (RS-fixed) |
|---|---|---|
| Universe 🟢 / 🔴 | 3 green / 21 red ("narrow") | **46 green / 81 red (BROAD risk-on)** |
| #1 flow sector | Utilities (w0.415) | **Financials (w0.159)** |
| Utilities | #1 | **#2** (green but **weak RS** — confirms bond-proxy, not outperformance) |
| Industrials | #8 (lukewarm) | **#6** (firing sub-legs RTX/ETN show up in RS) |
| Real Estate | #5 | #7 (correctly demoted) |

**Do the decisions change? No — they are strengthened. Two attributions are corrected:**
1. **UTIL was promoted citing "flow #1" — it is actually flow #2** (FIN is #1). The promotion still holds, and the
   DEEP verdict is now *better* supported: UTIL is green on OBV/volume but **weak on RS** (NEE +2.6, SO +0.3) =
   exactly the rate-relief bond-proxy signature, not AI-growth outperformance.
2. **INDU is #6, not the lukewarm #8** — the firing sub-legs (RTX RS +4.3, ETN +3.9) lift it; the "express via
   firing sub-legs" DEEP verdict is confirmed, the "rotate down a notch" framing was too harsh.
3. The "narrow defensive tape / only 3 🟢" line in the §Flow-tape context above was a NaN artifact — the real tape
   is **broad risk-on (46 🟢)**, which is *more* consistent with the cool-CPI+PPI read, not less.

**The 4+1 DEEP set is unaffected** (FIN #1, IT #4, UTIL #2, INDU #6 are all top-6; SEMI/cycle-GAP is independent
of RS). **Newly-surfaced clean LIVE names the NaN had hidden** (RS-driven greens) → handed to BET cross-sector:
**PSX** (Phillips 66 refiner, RS **+13.9** — a clean Hormuz-crack expression) · FIN breadth **V/SCHW/ALL/FITB/HBAN** ·
cyber **PANW RS +23.6 / FTNT +12.3 / AXON +22.4** · a **Health-Care green cluster VRTX/DHR/TMO/ABBV** (RS +9–12).
The corrupted shortlist showed only IBM(stale)/META/HCA; the corrected one has 15 names. `SECTOR_FLOW_US.json`
and `US_LIVE_SHORTLIST.json` on disk have been replaced with the clean 07-15 data.

---

## DEEP_LOG 2026-07-15: continuous=[INDU] rotating=[FIN,IT,UTIL]

---
**EXIT CHECK:** ✅ 11-sector OW/UW table written; every matrix×flow divergence named with a resolution owner · ✅ 4 DEEP picked by rule (INDU continuity→delta; FIN/IT/UTIL rotating; Energy→premortem not padded) · ✅ DEEP_LOG appended.
**→ proceed to PREMORTEM (US-only) before committing the deep budget.**
