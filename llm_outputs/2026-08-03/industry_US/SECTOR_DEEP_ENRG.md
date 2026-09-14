# SECTOR_DEEP_ENRG — Energy · industry_US · 2026-08-03 · **CONTINUOUS track → DELTA ONLY**

> Structure carried by reference to `llm_outputs/2026-08-02/industry_US/SECTOR_DEEP_ENRG.md`.
> This file writes the delta. ⚠ Lenses executed in-context, not by an agent fan-out (see PREMORTEM §0).

## 0 · The mandate ROTATION handed down, answered first

> *"EVENT_ALPHA Card 1 says the war premium is being priced out. ROTATION declined the demote because
> the flow is stable and the commodity move is unsettled. **DEEP owns the question.**"*

**Answer: the demote was correctly declined, and for a better reason than ROTATION had.** The
sector's problem is **not** that the tape turned — it is that **the tape has no 60-day foundation
under 14 of its 16 names, and that was already true before crude fell.**

---

## 1 · ★★★ Delta 1 — the crack's own settled bar was REVISED, and it moved the desk's bracket AWAY from firing

Full measurement in `MACRO_REPORT.md §D`. Summary, because it is the run's most load-bearing number:

| | 08-02 run (M309) | this run, same settled bars |
|---|---|---|
| 3-2-1 crack, 07-31 | **59.865** | **63.236** (**+3.371**) |
| distillate crack, 07-31 | **87.341** | **88.433** (**+1.092**) |
| **S49's observable** (5-sess distillate change) | **+1.066** | **+2.158** |
| **buffer to branch B (−5.0)** | 6.07 | **7.16** |

⇒ **The 08-02 run's *"the anti-signal is now ~1 session away"* is WITHDRAWN.** The mechanism is
**D86/M202/M236 reproducing a 4th time** — RB volume **13,997 on both 07-30 and 07-31**, HO **12,325
on both**, CL **235,395 on both** (forward-filled), so *"check the volume to see whether the bar
settled"* is unusable on exactly this stretch.

★ **Control that makes this credible rather than a pull error**: the eleven sector ETFs reproduced to
**0.01pp** on the same day from the same provider (`SWEEP_READ §2`, `MACRO §B`). **Equity closes are
stable; CME product legs are revised.**

⇒ **D140 registered**: a CHANGE observable survives *granularity* (which is what S49 was built for)
and **does not survive *revision***. **S49 is NOT re-frozen.**

---

## 2 · ★★★ Delta 2 — the base test has narrowed from two positives to ONE, and it is not the held name

Days 21-60 excess vs **SPY** (= RS60 − RS20), settled 07-31, all 16 names:

| Positive base | | Negative base | |
|---|---|---|---|
| **VLO** | **+3.6** | MPC | **−0.2** |
| | | PSX | −5.5 |
| | | XOM | −15.9 · CVX −17.1 · COP −20.3 · OXY −23.4 |
| | | FANG −22.5 · SLB −24.3 · **BKR −28.3** |

⇒ **M276 replicates a FIFTH time and DETERIORATES**: it recorded *"positive at VLO +2.8 · MPC +1.1 ·
TRGP +1.9 only"*; today **only VLO is positive**, MPC has crossed to **−0.2**, and **PSX has fallen a
FOURTH consecutive run (+1.6 → −5.91 → −8.5 → −5.5)**.

★★ **The sharpest single number in the sector, and it is a geometry statement not a price one**:
**CVX's last-20 share of its 60-day excess is −1543%** and **XOM's is −459%**. A *negative* 60-day
excess with a *large positive* 20-day excess does not mean a thin base — **it means the 60-day base is
ABSENT and the name spent the prior 40 sessions losing to SPY.** ⇒ PREMORTEM's re-tag stands:
**EXHAUSTED-BY-CONSTRUCTION**, not "extended".

⚠⚠ **And this is what makes the Iran de-escalation dangerous to the tilt rather than merely adverse**:
the crude-linked four have **nothing underneath the last 20 sessions to retreat to.** Named before
the event, not after.

---

## 3 · Delta 3 — the sector's flow is #1 and 2 of its 3 greens are instrument artifacts

`SECTOR_FLOW_US.json`: **wflow +0.567 / eqflow +0.475 — #1 on both — with ZERO 🔴 of 16**, and
**every one of the 16 reads OBV 매집 or 중립** — ⚠ **RULE D6: OBV is C-grade and carries nothing on
its own. The A-grade axis is quoted beside it and it AGREES on the 20-day and DISAGREES on the 60-day:
RS20 vs SPY is positive at 15 of 16, while RS60 is negative at 11 of 16.** The zero-red count is
therefore a 20-day statement, and §2 is the 60-day one.

⚠ **M315 replicates**: **12 of 16 pass `OBV-accumulation ∧ RS20>0` and are blocked from 🟢 by
`vol_surge` alone** — XOM 0.89 · CVX 0.88 · PSX 0.88 · MPC 0.82 · VLO 0.80 · COP 0.93 · FANG 0.80 ·
OXY 0.80, all against a 1.20 gate while carrying RS20 vs SPY of **+13.1 to +19.7**.
⚠⚠ **New this run: XOM 🟢 (surge 0.89) and CVX 🟢 (surge 0.88) are on SWEEP §2's MANUFACTURED list** —
they cleared on the velocity path that was null in the 08-02 pull. **Only BKR (surge 1.37) is a
genuine volume-path green.** ⇒ **Energy's "3 greens" is really 1 green plus 2 code paths, and BKR has
the sector's WORST base (−28.3).**

⚠ **BKR's ledger row is still open and is still wrong, and it is NOT resolved early**: filed 07-27 as
*"the only negative flow score of 11 Energy names"*; it is now **#1-adjacent at +0.87**. **Recheck
date 2026-08-14 stands** — pulling it forward on an unchanged bar is the S1 error the 07-30 run
already named. **Logged so the 08-14 audit cannot call it unforeseen.**

---

## 4 · Delta 4 — R39's consequence, quantified as far as it can be

**R39 killed *"XOM has 0% refining"*** — its Energy Products segment printed **$4.1–5.5bn, a
four-year high, comparable to or above CVX's $4.9bn.**

⇒ **The registry tag that computes the rank-2 cycle GAP is wrong.** `CYCLE_EXPOSURE` reads Energy
epicenter **6.89% vs an 8.0% floor (−1.109pp)** with held = **MPC · PSX**. **XOM is held and is a
refiner and is not counted.** ⇒ **the GAP's existence survives; its magnitude is `unknown` (C3).**

⚠⚠ **And the contradiction PREMORTEM surfaced is real**: **PSX — half of the counted exposure — was
filed 🔴RESOLVED by this desk's own ALPHA stage on 08-02** on three agreeing axes. **A shortfall
flag half-carried by a resolved name is not a shortfall statement.** → ALPHA.

⚠ **W4 status**: the customer side (M34: DAL/UAL/FDX/LUV, fuel costs **+66% to +84% YoY**, **UAL and
LUV cut or missed Q3 guidance citing fuel/crack**) is **closed and primary-sourced** — and
**PREMORTEM's Lens 1 shows it runs in reverse**, which is now bracketed as **S54**.

---

## 5 · Lens L1 (second derivative) — run on the corrected series

Settled 3-2-1 daily increments: **07-27 +3.813 · 07-28 +4.102 · 07-29 −0.359 · 07-30 −4.547 ·
07-31 −4.077.** ⇒ **three consecutive negative increments** on the composite.
Settled distillate 5-session change: **+11.665 (07-29) → +3.048 → +2.158.** ⇒ **the RATE is
decelerating on both series, and on the distillate it is still POSITIVE.**

★ **L1's condition ("two consecutive declines in the rate") is met on the composite and met on the
distillate — but M129 measured this exact conditioning to SUBTRACT information on this series**:
over 130 settled weeks, P(4-week crack decline | two consecutive negative accelerations) = **37.0%
(n=27) against a 43.1% unconditional base rate.** ⇒ **`indistinguishable` (C4). The lens is reported
and is not used to move a verdict.**

⚠ **Live 08-03 (Globex, ~30–47% of a session): 3-2-1 60.808 · distillate 87.756**, 5-session changes
**−7.308** and **−2.322**. **NOT SCOREABLE** — S49 says settled bars only, and scoring branch B off
this would be M201/D83's error a third time. **DRIFT settles it tonight.**

## 6 · Track KPIs · anti-signals · dates

| KPI | State | Anti-signal (kills the thesis) | Date |
|---|---|---|---|
| **S49** — 5-sess settled distillate change | **+2.158** (branch A) | **≤ −5.0** | 08-06 |
| **S31** — XOM RS20 vs SPY | **+13.1**, branch A tracking against us | **≤ 0** | 08-05 |
| **S52** — Iran | branch **C** (§EVENT_ALPHA P18) | a dated primary reopening (A) / a named-infra strike (B) | 08-06 |
| **S53** — MPC/PSX execution | pending | — | 08-05 |
| **S54** — {UAL,DAL} 5-sess excess | registered today | **< −4.5pp** falsifies M34's reverse channel | 08-10 |
| L2 margin percentile | **MPC ~37th (BELOW its own median) · PSX ~55th** | — | — |
| ⚠ **VLO · XOM** | **`margin_history` structurally BLANK, 6th/3rd run (D56/M233)** | — | **no cheapness claim is made on either** |

**Verdict: OW− HELD**, on a narrower base than the file it replaces. The commodity leg is **stronger**
than the 08-02 run recorded (§1); the **equity geometry is weaker** (§2); and **the two are pointing
apart, which is the honest state (C4).** MPC prints **08-04**, PSX **08-05**.
