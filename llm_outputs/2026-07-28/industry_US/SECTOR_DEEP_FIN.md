# SECTOR_DEEP_FIN — industry_US — 2026-07-28 (Tue) · **CONTINUOUS TRACK → led with the DELTA**

> Structure carried by reference to `llm_outputs/2026-07-27/industry_US/SECTOR_DEEP_FIN.md`.
> Flow `asof 2026-07-27 settled`. Benchmark **SPY** inline (C1). Analytical only (P4).
> ⚠ **Written in-run, not by a subagent** — see `BLINDSPOT_PREMORTEM.md` §0.

---

## 1 · THE DELTA — the exchanges' registered replacement observable moved, and it moved against us

**M135 retired the exchanges node's broken RS60 test** (it reported CONFIRM on frozen prices) and
replaced it with: *"equal-weight excess of the 7 vs SPY, 2026-07-24 → 2026-08-07."* **The 07-25 and
07-27 runs both reported it unchanged at −3.00pp because no settled close existed. One now does.**

```
2026-07-24 → 2026-07-27 settled, vs SPY
  NDAQ +3.89%  ·  SPGI +4.72%  ·  ICE +3.85%  ·  CME +0.41%
  MCO  +2.91%  ·  MSCI +3.35%  ·  COIN +3.93%          SPY +0.12%
  equal-weight +3.29%   ⇒   EXCESS  +3.17pp      (was −3.00pp)
```

★★★ **A +6.17pp swing in one settled session, with all seven names beating a flat SPY.** The node was
carried as *"highest sub-node flow (+0.556) with the worst RS60 (−8.9) — a de-rate"*, and **its own
replacement observable has just moved the other way.** ⚠ **Not scored** — the window runs to
**2026-08-07** and moving a verdict forward to tidy the ledger is the same class of act as moving a
threshold. **Reported because two runs called it unchanged and it is no longer unchanged.**

⚠ **The de-rate's structure is still visible underneath**: **ICE +18.7 / −8.6 · NDAQ +18.2 / −0.9 ·
CME +14.2 / −15.0 · COIN +11.0 / −11.7 · MSCI +1.5 / −8.4 vs SPY** — **RS20 strongly positive, RS60
negative** ⇒ **the whole positive number is a last-20 event.** **SPGI (+12.5 / +3.5) and MCO
(+6.6 / +1.8) are the only two positive on both windows**, which is exactly the split M137 measured by
revenue engine (*the de-rate is essentially absent from the ratings pair*).

---

## 2 · THE SECOND DELTA — a fresh adverse positioning read on the weakest of the five green tags

**MA prints 2026-07-30.** FINRA Reg SHO, settled 2026-07-27, **baseline in-band (38.2% vs the tool's
stated 40–45% band) ⇒ readable**:

| | MA |
|---|---|
| short-volume | **54.8%** vs a 38.2% 20-day baseline |
| **z** | ★ **+2.12 🔴 — a short surge** |
| 5v5 trend | **+6.9▲** |
| flow / tag | +0.617 **🟢 — but on a VELOCITY path** (`vol_surge` **0.68**, `velocity` 2.52) |
| RS20 / RS60 vs SPY | **+9.2 / +1.2** |
| implied move | **±5.6%** (expiry 07-31, D3 — event-covering) |

★ **This lands on the name M178 already called *"the least-supported of Financials' five green
tags"*** — **388% of its 60-day excess concentrated into 20 sessions, on a flat book** (current-quarter
consensus 4.85 → 4.78 = **−1.6%/90d**), **with the print still ahead of it.**
⚠ **S14-num's pre-declared no-information band is ±3.9% and is NOT re-frozen**, even though the market
now prices ±5.6%. **Any MA move inside ±3.9% may not be read as confirming the FIN OW.**
⚠ **"Short building = bearish" is in the REJECTED ledger (D6/D11).** This is reported as **positioning
context on an already-weak name**, not as a direction.

---

## 3 · The tilt's two legs, re-checked

**Leg 1 — the steepener: still dead (R11), and it moved further away.**
`[FRED]` **T10Y2Y = 4.69 − 4.33 = +0.36**, against **+0.34** on the 07-27 run ⇒ **the curve steepened
2bp and S23's ≤+0.20 trigger is now 0.16pp away, moving AWAY.** **DGS2 4.33% is inside S19's
4.15–4.45 band ⇒ branch M ("no conclusion changes") is the live state, and S23's bear-flattener-hold
remains the branch that kills NIM without tripping S19 or S9.**

**Leg 2 — breadth: alive but narrower than when it was first called.**
`SECTOR_FLOW_US.json`: **eqflow +0.339 > wflow +0.304, gap +0.035.** ⚠ **M173 measured this gap at
+0.064 raw and +0.028 once BRK-B is removed** (BRK-B is **$1,055.7bn = 13.9% of sector cap at a flow
score of −0.145 today**, having been +0.012 on 07-24). **At +0.035 raw the gap is narrower than on the
run that first called the sector breadth-led.**

**Composition, re-aggregated from all 47 rows (C5 — the grouping is stated):**

| Sub-node | Flow leaders | Read |
|---|---|---|
| **Insurance** | **CB +0.749 🟢 (`vol_surge` 1.47 — a VOLUME path)** · **TRV +0.750 🟡** · MET +0.733 · PRU +0.628 · PGR −0.250 | ★ **The strongest sub-node, and TRV is 🟡 ONLY by `vol_surge` 1.15 — a filter artifact.** Its flow score is **higher than 9 of the 24 greens on the whole board** |
| **Banks** | JPM +0.645 🟢 · BAC +0.667 🟢 (`new_green`) · WFC · COF +0.044 · HBAN +0.075 · **C −0.713 🔴 = the sector's ONLY red** | The bank bucket has a volume leg for the first time in the carry — **but JPM/BAC greens are velocity paths** (`vol_surge` 0.83 / 0.95) |
| **Capital markets** | BX +0.767 (**the sector's #1 flow**, `vol_surge` 1.18) · AMP +0.633 · STT +0.561 · SCHW +0.544 · ⚠ **IBKR RS20 +1.3 / RS60 +15.9 and HOOD −4.5 / +30.5 vs SPY — the de-rate cohort's own A-grade axis is POSITIVE on 60 days and flat-to-negative on 20**, with OBV 분산 agreeing as a C-grade corroborant only (D6) | ★ **BX is the sector's top flow score and appears in no carried thesis** — a coverage gap |
| **Exchanges** | NDAQ +0.633 · COIN +0.628 · CME +0.544 · SPGI +0.522 · ICE +0.528 | §1 |
| **Payments** | MA +0.617 🟢 · V +0.535 🟢 | both **velocity paths** (`vol_surge` 0.68 / 0.62); **V prints 07-29, MA 07-30** |

⇒ **5 greens of 47, 1 red.** ★ **CB is the only Financials green that cleared on VOLUME.**

---

## 4 · Dispersion (W5) and the internal hedge

**RS20 vs SPY spans +18.7 (ICE) to −7.5 (C) = 26.2pp; RS60 spans +30.5 (HOOD) to −15.0 (CME) =
45.5pp**, against **XLF +1.01% on the day / +1.50% over five sessions.** **The spread is ~30× the
sector's move ⇒ the label is the wrong unit here too.**

★ **The hedge the label hides, carried and re-confirmed**: **CB (β 0.125) and TRV (β 0.339)** sit
**inside** the FIN OW, and **S26 names them among the low-beta side that rips if credit widens.**
**Financials is the only tilt on the board carrying an internal hedge**, and today the volume-confirmed
green is one of the two.

---

## 5 · Customers and counterparties (W4) — where the earnings actually come from

- ★ **NII has MIGRATED and the migration is primary-sourced** (M138): **WFC held FY26 NII at ~$50bn and
  MISSED at $12.32bn (+5% YoY)**, its CFO naming interest-bearing deposit mix; **JPM RAISED to
  ~$105.5bn on markets-related NII.** ⇒ **S23's bear-flattener hits the spread half WFC just guided
  flat, and leaves the half that belongs to GS/MS/SCHW/IBKR.** **The flattener is not a
  sector-wide NIM event any more.**
- **SPGI inverts the exchanges node's own premise** (M137): the one name at RS60 ≈ 0 carries the
  node's **worst book — next-year EPS −8.1%/90d on 0↑:2↓ at both 7d and 30d.** ⚠ **SPGI printed
  2026-07-28 and is absent from `CATALYST_WATCH` (D18)** — unread at this run's clock.
- **CME Q2, SEC XBRL**: **$1.71bn, +1.2% YoY, −9.0% QoQ** — that alone explains RS60 −15.0.

---

## 6 · Track KPIs and anti-signals

| KPI | Now | Registered test |
|---|---|---|
| **Equal-weight excess of the 7 exchanges vs SPY** | ★ **+3.17pp** (was −3.00pp) | M135's replacement observable, **to 2026-08-07** |
| **T10Y2Y with DGS2 quoted alongside** | **+0.36 / 4.33%** | **S23**, to **2026-08-05**. Branch B = **T10Y2Y ≤+0.20 with DGS2 inside 4.15–4.45** |
| **{MA, V, PYPL} RS20 vs SPY** | MA **+9.2** · V **+6.4** · PYPL (RS20 was board-leading on an **unaccepted $53bn Stripe bid**, not payments breadth — S14-ANNEX) | **S14** scored **2026-08-06**, PYPL contamination included, **with the {MA, V}-only reading recorded alongside** |
| **eqflow − wflow gap** | **+0.035** raw (M173: +0.028 ex-BRK-B) | breadth leg's own health |
| **HY OAS** | 2.79%, **+11bp off its 365-day low over three prints** | **S26** to 08-12; **31bp from the 3.10% line** |

**Anti-signals**: **HY OAS ≥3.10% on a close with NFCI turning positive WoW** ⇒ **S26 branch B, and
all three OW tilts lose together on one shared beta** (JPM 0.932 · XLF 0.789) · **T10Y2Y ≤+0.20**
⇒ S23 branch B · **a bank credit-provision surprise** (unbracketed, no dated instrument).
⚠ **NFCI is 11 days stale (07-17) against its own ≤7-day lag** — any financial-conditions claim this
week must quote that.

**Dated catalysts**: **V 2026-07-29** ⚠ **absent from `CATALYST_WATCH`, prints a day BEFORE MA, and
has no bracket of its own — logged as an under-computed leg in PREMORTEM Lens 1** · **MA 07-30
(±5.6% implied; S14-num's frozen band ±3.9%)** · **ICE 07-30** · **FOMC 07-29 (S19/S23/S9)** ·
**June PCE 07-30 (S15)** · **JPM re-check 08-08** · **CB/TRV re-check 08-06**.

---

## 7 · The divergence ROTATION handed here — verdict

**Question**: is Financials' eqflow > wflow signature real breadth, or a residue of one holding company?

**Verdict: real but narrow, and narrower than when it was named.** Removing BRK-B moves the gap
**+0.064 → +0.028** (M173); today's raw gap is **+0.035**, i.e. **already inside the range M173's
correction produced.** What survives is **insurance + payments carrying the sector** — and today the
insurance leg has **the only volume-confirmed green (CB, `vol_surge` 1.47)** while **the payments leg's
two greens are both velocity paths with prints in the next 48 hours.**
⇒ **FIN stays OW−. The breadth leg is alive; the steepener leg is still dead (R11); and the run's new
information is that the node the desk called a de-rate has just outperformed by 6.17pp.**

⚠ **What this file does NOT claim**: that the exchanges' de-rate is over. **One settled session is
n=1 (S1)**, the observable runs to **08-07**, and **four of the seven do not print inside its window**
(CME/MCO/MSCI report 2026-10-20/21/22) — a defect **M135 already recorded at the replacement's
registration.**
