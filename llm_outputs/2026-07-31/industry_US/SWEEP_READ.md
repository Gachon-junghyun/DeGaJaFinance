# SWEEP_READ — industry_US · 2026-07-31

> Asof the **PREVIOUS close** — a same-day 07-31 catalyst is NOT in these numbers. The reading only;
> numbers live in `SECTOR_FLOW_US.json §sector_rotation` + `US_LIVE_SHORTLIST.json`, not reprinted here.

⚠ **Instrument caveat (this run, not in the JSON):** the news-velocity axis (1 of 4 flow axes) throttled
under the 300-name batch — only **48/300 names got it, and they are exactly the top-48 by mcap (all top-20,
69% of mcap weight)**. So the mcap-weighted **wflow rests on the full 4-axis**, but the small-cap tail
(rank>48) ran **3-axis / OBV-only → 🟢 tags systematically demoted** (the script's own line-357 warning).
**The green count is biased LOW; read every absence through this lens.** (Green swung 7↔15↔17 across re-runs
purely on how many names the API served; this file is the max-coverage run.)

## 1 · Universe headline
n=300 · aggregate wflow **+0.07** · 🟢15 / 🔴84 — a breadth-negative universe (5.6× more distribution than
accumulation tags), positive wflow held up only by the mega-cap heads.

## 2 · Cross-checks vs the MACRO transmission matrix (ROTATION's direct input)
- **Biggest CONFIRM+CONTRADICT — Energy.** Flow #1 wflow **+0.471** AND #1 eqflow **+0.358** / breadth 0.19
  (best on the board). Money is **accumulating Energy BROADLY**, not narrow. This **CONTRADICTS MACRO §E's
  live 07-31 tape** ("risk-on rotation OUT of energy, XLE 5d −1.99pp"): the prev-close flow says that
  5-day price fade is **deflating war premium, NOT distribution** — OBV is 매집 across the whole complex.
  **Money is on Energy-accumulation → backs S49 branch A (refining margin) over S31/S8 (war-premium unwind).**
- **CONFIRM — the IT split, mechanically.** wflow **+0.199** (rank 2, Δ+0.114 improving) but eqflow **−0.113**,
  4🟢/56, 26🔴. Mega-caps (MSFT +0.80, NVDA new-🟢) pull wflow up while breadth is the memory drag. Equipment
  suppliers are genuinely 🔴 **and news-covered (not an artifact): MU/AMAT/LRCX/KLAC all 🔴분산, rank<48.** But
  storage diverges UP — **STX new-🟢 (+0.71, beat+guided) · WDC 🟡매집.** Branch-A candidate is storage, not
  equipment; the equipment de-rate is real. Confirms MACRO's N-split, reopens branch B by ignition.
- **CONFIRM — Financials** (wflow +0.163 AND eqflow +0.121, both halves positive) but **Δ−0.222 fading d/d.**
  Money still on it, decelerating.
- **CONFIRM — the demotes.** Utilities −0.332/eqflow −0.329/0🟢 · Materials −0.364 (worst)/0🟢 — both halves
  negative, money confirms MACRO UW−/UW. Health Care −0.042/0🟢 confirms the "money reversed" fade (C7).
- **CONFIRM (narrow) — Cons Disc.** wflow +0.081 but eqflow **−0.058**, 2🟢/28 — the XLY/AMZN strength is
  **mega-cap narrow, breadth-negative** → confirms MACRO's "n≈1, live-only, not a settled tilt."
- ⚠ **Real Estate — watch.** wflow +0.056 / eqflow +0.044 (both mild-positive, rank 5) but **0🟢, breadth 0,
  Δ−0.364 (sharpest fade on the board).** A positive flow LEVEL with zero ignition and the fastest
  deceleration — not accumulation.

## 3 · Shortlist composition — the ABSENCES (names in `US_LIVE_SHORTLIST.json`)
Comp: IT 4 · Energy 3 · Financials 3 · Cons Disc 2 · Industrials 2 · Comm Svc 1. ✅clean-rise: GRMN/JPM/NVDA;
⚡squeeze-fuel (NOT a buy): STX, MA. **Five sectors produced ZERO names — diagnosed:**
- **Utilities · Materials · Health Care · Staples (0 each) = REAL evidence.** 0🟢 in flow, negative both halves.
  The absence confirms money is out.
- 🚩 **Energy's 3 shortlist names are the WRONG 3 — the 🟢-tag artifact, measured precedent replicates.** The
  shortlist shows integrated/services mega-caps (XOM velo 2.47 · CVX 2.80 · BKR) — but the **refining thesis
  (S49 / HANDOVER #1 dig: VLO/MPC/PSX) is ABSENT.** All three are **OBV-accumulating (매집; OBV +0.17/+0.33/+0.36,
  RS20 +16.7/+18.3/+20.2, flow +0.48/+0.50) yet tagged 🟡중립 — because they sit at mcap-rank 176/178/190 in the
  news-demoted tail (velocity n/a).** With the oil/refining news bucket active, their tags would likely lift to
  🟢. **This is the exact 2026-07-21 ENRG precedent: refiners accumulating, 🟡-tagged, filtered out. The refiners
  ARE accumulating; the shortlist can't see them this run.**
- ⚠ **Utilities' 0-green is partly masked too:** **CEG (+0.49, OBV +0.20 매집, rank 123) is a 🟡 news-demoted
  accumulator** — while GEV/VRT are genuinely 🔴분산 (news-covered, rank 42/92, real distribution). The AI-power
  leg is **bifurcating** (CEG accumulating vs GEV/VRT distributing, per S47 spread), not uniformly dead — "UW
  vindicated" holds on the regulated+turbine legs, not on CEG.

## Cycle-exposure GAP → hand to ALPHA
🚨 **ONE GAP** (`CYCLE_EXPOSURE.json`): rank-2 **Energy/oil-refining epicenter 6.87% < 8.0% need (−1.135pp)** —
book holds MPC/PSX in-epicenter but under min, touches the cycle mostly via LNG (consequence-beta, not the
engine). Converges with §2/§3: flow says refiners are accumulating, the book is under-exposed to that exact
epicenter. Rank-1 AI-compute ✅ (12.95%, AVGO/NVDA/TSM); rank-3 missile-defense ⚪ no threshold set (RTX).
ADD *timing* is tape-gated; the core's existence is not (P4/S6).
