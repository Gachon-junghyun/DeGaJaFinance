# ACTION_BRACKET — 2026-07-23  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 11,469,364원 · fx 1481 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** RTX earnings (D-0, axis=earnings) — both-sides armed below.

### CORE-STARTER (tape-independent) — PSX  (BUY)
- **condition:** establish NOW regardless of tape — closes Energy / oil-refining (Hormuz + Russia crack) epicenter GAP (0.0% < 8.0%)
- **size:** 4 sh @ ~$214.77 (≈$859.08 notional, risk $61.96 = 0.8% )
- **stop:** $199.74 (−7.0%) · exch NYSE
- **why core:** cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively exiting (FINRA short-vol z -1.43, 5v5 -16.6▼) = clean structural entry, not an extended one (cf. MPC RSI 85.7). Crack-spread leverage, not crude beta. Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ADDENDUM — appended by `industry_US` ALPHA, 2026-07-23

> The block above is `action_bracket.py`'s own output and is **not edited** (`core_pick` is
> **human-locked**). Everything below is the desk's correction and the both-sides brackets the script
> announced but did not emit. **Analysis only — a human executes, never the desk.**

## 1 · ⚠ Two script defects, both third-consecutive-run occurrences (dig D19)

**(a) "Nearest binary: RTX earnings (D-0) — both-sides armed below" with NOTHING armed below.**
Third run in a row. The brackets are written in §2 here instead. ⚠ Separately, the "nearest binary"
it picked is one that **already printed** at 06:30 ET this morning; the two binaries actually ahead of
us today — **INTC (AMC, implied ±12.7%)** and the **ECB decision** — are **absent from
`CATALYST_WATCH.json` entirely** (dig D18, also third consecutive run).

**(b) The PSX `why core` rationale is a frozen string and three of its clauses are now false.**

| Clause in the ticket | Measured 2026-07-23 | Status |
|---|---|---|
| *"cheapest large refiner on forward (11.2, PEG 1.17)"* | Forward P/E pulled today: **MPC 10.99 < PSX 11.72 < VLO 12.73**. On the FY26 basis (M23): **MPC 8.8 < VLO 9.4 < PSX 10.8** | ★ **FALSE on BOTH bases.** Already retracted as **R8** on 2026-07-22 and the string still ships |
| *"the only Energy name with shorts actively exiting (FINRA short-vol z −1.43, 5v5 −16.6▼)"* | PSX short-z today = **+1.03, 5v5 +4.1▲** — shorts building, not exiting. Prior readings: **+2.01 (07-20) · +0.01 (07-21) · +1.03 (07-23)** | ★ **Wrong in a third different direction on a third consecutive run.** The *actual* covering name on the board is **STT at −1.45**, which is not in Energy |
| *"Crack-spread leverage, not crude beta"* | The crack fell **−11.2%** on 07-23 while crude rose **+5.2%** | **Still the correct framing — and it is currently pointing the wrong way** |
| *"cf. MPC RSI 85.7"* (extension caveat) | MPC RS20 **+25.2 / RS60 +36.2 vs SPY**; **all three refiners now trade ABOVE their consensus targets** (−9.3% / −7.1% / −5.1%) | The extension caveat has **widened to all three**, not just MPC |

**The surviving, better-founded case for the same name** (unchanged and worth stating so the human is
not choosing between "stale string" and "nothing"): **PSX's FY26→FY27 consensus cliff is −7.2%, against
VLO −31.6% and MPC −25.8%.** It is the **least peak-dependent** of the three. That is a *different*
argument from "cheapest", and it is the one the evidence supports.

⚠ **`core_pick` is a HUMAN-LOCKED registry field and was NOT modified by this run.** The fix is for a
human: either recompute the rationale fields at generation time, or stamp each with its as-of date so
staleness is visible instead of authoritative.

## 2 · Both-sides brackets — the ones the script announced and did not emit

Every bracket carries a **frozen observable**, a **threshold**, a **date** and **both branches**, and
each is registered in `handoff/SCENARIOS.md`. A one-way tilt into a known binary is a protocol violation.

| # | Binary | Frozen observable + threshold | Branch WITH us | Branch AGAINST us — what rips |
|---|---|---|---|---|
| **S6** | **INTC FQ2 · TONIGHT 2026-07-23 AMC** | An **externally named** 18A/foundry customer, **or** capex/utilisation guided up. ⚠ Implied move **±12.7%** (expiry 07-24, D1 — covers the event) vs the **±4.4% registered at a D0 expiry**; the registration's own *"a FLOOR, not a fair estimate"* caveat is **measured to have been correct at 2.9×**. **A move inside ±12.7% carries no information** | **B** — no customer named, capex flat ⇒ company-specific; the IT tilt is unaffected | **A** — a named customer ⇒ the semicap 🔴s were a **pullback**, and an IT underweight is **short the wrong thing**: AMAT (RS20 −7.3 / RS60 **+28.1** vs SPY), LRCX (−15.9/+14.5), KLAC (−14.1/+6.3), MU (−10.7/**+88.5**), INTC (−24.3/+19.6) |
| **S12** | **ECB decision · TODAY 2026-07-23** | **DTWEXBGS vs its 120-day range [117.44, 121.41]**, last **120.53** [FRED, 07-17]. ⚠ **No options contract exists** — the threshold is the measured range boundary, declared as such | **B** — hold-with-dovish-tilt ⇒ DXY stays in the upper half; MATR UW intact | **A** — hawkish surprise ⇒ DXY closes **<117.44** within 3 sessions ⇒ **MATR UW loses its dollar leg**; FCX (flow −0.203) gets a tailwind |
| **S9** | **FOMC · 2026-07-29** | **DFII10 with T10YIE quoted alongside** (a real yield alone hides growth vs inflation). Now: real **2.37% = a 120-day high**, breakeven **2.28%** | **B** — real 10y holds **2.20–2.55%** ⇒ the tilt survives on flow | **A** — real 10y **<2.20% with breakeven rising** ⇒ **two sides of the book lose on one tick**: the life/annuity leg (MET, PRU, AFL direct; TRV +0.933, CB +0.685 second-order) **and** the UTIL/RE underweight reverses (WELL RS20 **+10.7**, VTR **+11.9** vs SPY already bid). **C** — real 10y **>2.55%** = P1's registered anti-signal, a regime call |
| **S13** ★ | **MSFT + META capex · 2026-07-29** | Cross-condition over the 10 sessions to ≈08-12: the **capex guide** × the **spenders' NTM P/E** × the **suppliers' median RS20 vs SPY** (MU, AMAT, LRCX, KLAC). ⚠ **No usable implied move** — META ±4.4% and MSFT ±2.9% both **expire 07-24, before the event**; any threshold from them would be fabricated | **B** — raised and the multiple holds ⇒ read as demand; **low information** by the pre-registered asymmetry | **A** — raised, spender P/E **compresses**, supplier RS20 vs SPY **turns positive** ⇒ **IT's single N label is wrong on BOTH halves at once.** **C** — a **cut** ⇒ breaks the volume and price legs together and extends into **AVGO, NVDA, TSM — all held in the real book** |
| **S8** | **VLO + STNG 2026-07-30 · Hormuz `[blank]` undated** | **Crude vs its pre-escalation range AND the diesel crack**, together. Cross-check KPI: **WTI COT %ile, next print Fri 2026-07-24** | **B** — crude falls but cracks hold ⇒ **input-cost relief**, and the OW stands on margin rather than on the war. ★ **This distinction is the whole bracket** | **A** — crude below range **AND** the crack still rolling ⇒ **Energy OW loses both legs at once**: VLO/MPC/PSX (RS20 +22 to +26 vs SPY) give back the premium and the tankers (RS20 −0.7 to −6.5 vs SPY) lose their only support |
| **S14** | **MA · 2026-07-30** (with **V · 07-29**) | MA cross-border volume growth **+ the RS20 vs SPY of {MA, V, PYPL} over 5 sessions**. ⚠ No implied-move figure was available — flagged, not invented | **A** — volume holds and the trio's RS20 vs SPY stays positive ⇒ FIN's breadth is genuine | **B** — a volume miss and the trio flips negative ⇒ the "breadth" was a **consumer-spend concentration**, and **FIN loses its second reason in nine days** (the steepener leg broke on 07-23) |
| **S15** | **June PCE · 2026-07-30** | **Core PCE MoM**, against core CPI's printed **−0.02% MoM**. ⚠ **Threshold is judgement, not a measurement** — no options threshold exists for a PCE print in this toolkit | **B** — ≤ **+0.3%**, in line with the CPI cool-down ⇒ P1 stands | **A** — **> +0.3%**, a clean break from CPI ⇒ **P1's "reaction-function, not inflation" collapses**; FIN's logic is hit and DISC N− deepens |
| **S16** | **META · 2026-07-29** | META's capex line **+ its RS20 vs SPY against the equal-weight of {MSFT, AMZN, AAPL}** over 10 sessions | **A** — META stays above the cohort ⇒ **COMM N− was a single-name verdict misapplied to a 13-name sector** (n≈1, S1) | **B** — META falls to or below the cohort ⇒ the sector read was right for the **S13 margin-drag** reason, i.e. a cohort effect, not a GOOGL-specific one |

## 3 · The 🚨 cycle GAP, split by leg — the correction the single core-starter ticket cannot express

`CYCLE_EXPOSURE.md`: rank-2 **Energy / oil-refining, epicenter 0.0% vs a required 8.0% (−8.00pp)**.
The script resolves that into **one PSX ticket**. The registry bucket mixes **three different KPIs**,
and today they gave **three different answers** — so a single ticket is the wrong shape:

| Leg | Registry names | KPI today | Does an "engine deteriorated" objection apply to 0%? |
|---|---|---|---|
| **Crude / integrated** | XOM, CVX, EOG | **Accelerating** — crude +5.2%; XOM 🟢가속 · `new_green`, RS20 **+8.6 vs SPY** | **No objection at all.** The GAP here is clean |
| **Refining margin** | MPC, PSX, VLO | **Deteriorating** — crack **−11.2%**, but **gasoline-led (−19.7%) vs distillate (−3.6%)**, so the diesel bottleneck is intact | A dated caution against **adding**, not a resolution of the GAP: RS20 +22 to +26 and RS60 +25 to +36 vs SPY are positive and the 🟡 is a `vol_surge` artifact. **The 0% is the desk not owning it, not the market voting no** |
| **Tankers** | FRO, STNG, INSW, DHT (**TNK missing from the registry**) | Narrative violent (**108.86×**), **money absent** — RS20 vs SPY **−0.7 / −6.5 / +1.7 / −5.9 / −2.2** | No objection either. The cleanest case in the run that a **crowded narrative ≠ owned exposure** |

**Governing rule, unchanged**: a crowded or deteriorating tape gates **ADD timing**; it never justifies
0% core in a top-rank cycle. **A structural GAP flag and a deteriorating KPI are different objects —
both go forward, neither cancels the other.**

## 4 · For the human — nothing below was applied

1. **`core_pick` rationale is stale in three clauses** (§1b). Recompute at generation time, or stamp
   each field with its as-of date. **R8 already retracted the "cheapest" claim on 2026-07-22.**
2. **`action_bracket.py` announces brackets it does not emit** — third consecutive run (D19).
3. **`catalyst_calendar` missed both of today's forward binaries** (INTC, ECB) while listing two that
   had already printed — third consecutive run (D18).
4. **Registry (`data/cycles/cycle_registry.json`, `updated: 2026-07-17`, 6 days stale)**: add an
   **AI-security row** (0% book exposure, no GAP can fire); **split rank-1** (MU +88.5 vs AVGO −10.8
   RS60 vs SPY = a 99pp spread inside one "epicenter"); **split rank-2** into the three legs above;
   **add TNK**; **fix the `data_build/cycles/…` footer path** (that directory does not exist); **set a
   real floor for rank-3 or document it as permanently unguarded** (the GAP rule only checks rank ≤ 2).
