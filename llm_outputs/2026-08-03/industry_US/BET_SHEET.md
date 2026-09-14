# BET_SHEET — industry_US — 2026-08-03 (Mon) · ONE file, per-sector sections

## ⚠ 0 · Four instrument caveats binding on EVERY number below — read before any figure

1. ⚠⚠ **NO NEW SETTLED US TAPE.** Last settled session **2026-07-31**, identical to the 08-02 run's.
   **Every price, RS, flow and short figure on this sheet is the same bar the previous sheet used.**
   Nothing here is a "move".
2. ⚠⚠ **D126 — 10 of the board's 26 greens were MANUFACTURED by a code path on frozen prices**
   (`velocity` non-null 0/300 → 51/300 between two pulls of the same `asof`). **Affected names on this
   sheet are marked ⚠MFG and their tags may not be cited.** 8 of 11 sector `wflow` values moved and
   **three flipped sign** with no price input.
3. ⚠⚠ **`vol_surge` blocks 60 of 60** names passing `OBV-accumulation ∧ RS20>0`, max blocked surge
   **1.190 vs a 1.20 gate.** A **🟡 on this sheet frequently means "0.01 short of the gate", not
   "weak"** — that is why several 🟡 names outrank 🟢 ones here.
4. ⚠ **L2 (margin percentile) is unrunnable on the majority of this sheet** (M233: 61% of names
   attempted). **Where it is blank, NOTHING is called cheap** — the multiple is stated as a fact.

**Candidate set** = DEEP thesis leaders (ENRG · FIN · MATR · DISC) ∪ `US_LIVE_SHORTLIST.json` (15)
∪ PREMORTEM's promotions. **Sizing language below is influence illustration only — zero buy/sell
recommendation (P4).**

## §B FRESHNESS TAGS — filled by ALPHA, 2026-08-03

⚠⚠ **ZERO 🟢LIVE, for a 10th consecutive foreign-feed measurement — and F1 is stated as ARITHMETIC,
not as a complaint.** 🟢FRESH requires **age ≤14d ∧ acceleration ≥2×**. Across **16 theme probes this
run the YOUNGEST theme on the entire board is `airline fuel` at 58 days**, then `refining margin` 66d,
`data center power` 72d, `AI capex` 74d, `memory pricing` 82d, everything else ≥90d.
⇒ **🟢LIVE cannot fire by construction, and every tag below is capped at 🟡.** **The gate was NOT
loosened** (a live-gate change needs a human, D11-class).

| Bet | Theme (accel · age · n) | Tag | Residual / why |
|---|---|---|---|
| **MPC · VLO** | `refining margin` **3.40× · 66d · n=127** | **🟡PARTIAL** | Residual is **dated and small**: **MPC prints 08-04, PSX 08-05, S49 settles 08-06.** ⚠ The commodity leg improved (§0 note 1 → MACRO §D) while the equity base narrowed to one name (VLO +3.6) — **the two axes point apart (C4)** |
| **MET** | `life insurer` **3.14× · ≥90d · n=315** | **🟡PARTIAL** | Narrative axis is **usable at n=315** and supports the carrier. Residual: **a NEGATIVE revision book (0q 1↑:2↓ at both horizons)** and **one clean name carrying a sector tilt** — M317's 4th carrier statement |
| **F · GM** | `auto sales` **⚪ECHO 1.85× · n=69** | **🟡PARTIAL** ⚠ | ⚠⚠ **The narrative is DECELERATING while the money is accumulating — this is MONEY WITHOUT NARRATIVE**, and per the stage's rule an ECHO thesis needs *stronger* live evidence to survive. **It has strong price evidence (F: both windows positive, +12.8 base) and no story.** Honest state, not a promotion |
| **NUE · STLD** | `steel tariff` 5.36× · **n=15, 7d mean 0.7** | **🟡PARTIAL** ⚠ | ⚠⚠ **The narrative axis is UNREADABLE at this n** — same class as M281's `tower REIT` 3.43× on n=11, explicitly logged there as unusable. **The ratio is not quoted as evidence.** Coverage gaps, not bets |
| **AMZN** | — | ⛔ **🔴RESOLVED — DROPPED** | **Its catalyst (the 07-30 print) FIRED and was consumed**, and it has **no 60-day base** (RS60 −3.9 vs SPY, days 21-60 −15.5, last-20 share −295%). **Filed to the reject ledger** (`C.차트붕괴`, revives-if *"RS60 vs SPY turns positive AND days 21-60 turns positive"*, recheck **08-17**) |
| **PSX** | — | ⛔ **🔴RESOLVED** (08-02, unchanged) | Three agreeing axes. ⚠ **Still printed as `CORE-STARTER (BUY)` by `ACTION_TICKETS.md` — D19, 7th run. `core_pick` is human-locked and was NOT modified** |
| **GRMN · EA · TRI · ICE** | — | ⛔ **REJECTED (08-02)** | Re-surfaced by the shortlist on **identical data**; no revival condition met. Rechecks **08-12 / 08-16** |
| **RCL · BKNG · CMG** | — | ⚠ **NO TAG ISSUED** | Reached ALPHA and received no tag because **no 4Phase exists**. **That is a MISS, not a 🔴** — **RCL filed to the missed ledger** (`Q.확신부족`, enters-if *"a 4Phase is written OR S54 fires branch A"*, recheck **08-17**, `--sample prospective`) |

---

## §ENRG — Energy · OW− (continuous)

### §A Numbers

| | **MPC** ★held | **VLO** | XOM ⚠MFG | CVX ⚠MFG | PSX ⛔ |
|---|---|---|---|---|---|
| flow / tag | +0.57 🟡 | +0.56 🟡 | +0.70 🟢⚠ | +0.70 🟢⚠ | +0.60 🟡 |
| `vol_surge` | 0.82 | 0.80 | **0.89** | **0.88** | 0.88 |
| RS20 / RS60 vs **SPY** | +18.5 / +18.3 | +16.6 / **+20.2** | +13.1 / **−2.9** | +16.0 / **−1.0** | +19.7 / +14.2 |
| **days 21-60** | **−0.2** | **+3.6** | **−15.9** | **−17.1** | **−5.5** |
| L2 margin pctile | **~37th (BELOW its own median)** | ⛔ **BLANK, 6th run (D56)** | ⛔ **BLANK (M233)** | — | ~55th |
| Short %float · P/C | 2.5% covering · **0.44** | 4.3% covering · **2.31 = fear** | — | — | — |
| Implied move | **±8.9%, exp 08-21 (D18) — COVERS its print** | ±4.9%, exp 08-07 | — | — | ±2.7% expired |

### §B Thesis · freshness `[ALPHA fills]`
**MPC** — the refining-margin expression whose commodity leg **improved** this run (S49 buffer
**7.16 pts, not 6.07** — MACRO §D's revision) and whose **equity base is now flat (−0.2)**. It is
**the only name where a margin percentile exists and reads BELOW its own median**, i.e. the one
Energy name L2 does not forbid discussing. **Prints 08-04 (S53), and its straddle covers the print.**
**VLO** — ★ **the ONLY Energy name with a clearly positive 60-day base (+3.6)** after M276's fifth
replication narrowed the list from three to one. ⚠ **P/C 2.31 = the sheet's only genuine fear
profile**, and ⚠ **its margin percentile is a 6th-run structural blank ⇒ no cheapness claim.**

### §C Flow / positioning cross-read
**12 of 16 Energy names pass the accumulation pre-condition and are blocked by `vol_surge` alone**
(M315 replicates). ⚠⚠ **XOM's and CVX's 🟢 are MANUFACTURED** — only **BKR (surge 1.37)** is a real
volume-path green in this sector, **and BKR has the sector's worst base (−28.3)**.

### §D Competition / peers
One risk unit: **MPC–VLO SPY-residual ρ +0.878** (M147). **They are not two positions.**
**XOM/CVX/COP/OXY** are the crude-linked leg — **all four base-ABSENT**, last-20 shares **−233% to
−1543%**.

### §E Refutation · dated catalyst
- **S49** ≤ −5.0 on the settled 5-session distillate change (**+2.158** today) → **08-06**
- **S31** XOM RS20 ≤ 0 (**+13.1**, branch A tracking **against us**) → **08-05**
- **S52** Iran, branch **C** currently → **08-06** · **S53** MPC/PSX execution → **08-05**
- ⚠⚠ **The live 08-03 bar has crude −6.9% AND the crack down** ⇒ products fell more than crude ⇒
  **margin-led, not supply-led. UNSETTLED (~30–47% of a session), not scoreable. DRIFT settles it.**
- ⛔ **PSX stays 🔴RESOLVED (08-02, three agreeing axes). It is NOT re-promoted by re-appearing here.**

---

## §FIN — Financials · OW− (continuous)

### §A Numbers

| | **MET** | PRU | TRV | BAC/JPM/MA ⚠MFG | ICE ⛔ |
|---|---|---|---|---|---|
| flow / `vol_surge` | **+0.80 / 1.36 ✅volume** | +0.76 / 1.18 | +0.72 / 1.16 | 0.85 / 0.76 / 1.03 | +0.79 / 1.22 |
| RS20 / RS60 vs **SPY** | +6.4 / **+17.1** | +7.8 / **+18.5** | +9.1 / **+21.0** | +5.2/+13.4 · +4.9/+10.5 · +5.9/+12.1 | +14.4 / **−5.0** |
| **days 21-60** | **+10.7** | **+10.7** | **+11.9** | +8.2 · +5.6 · +6.2 | **−19.4** |
| fwd / trailing P/E | **8.77 / 18.63** | — | — | — | — |
| PEG · target | **0.51** · **−14% to $97.75** | — | — | — | — |
| revisions (0q) | ⚠ **7d 1↑:2↓ · 30d 1↑:2↓ — NEGATIVE** | — | — | — | — |

### §B Thesis · freshness `[ALPHA fills]`
**MET** — ★ **the sector's only clean, non-rejected, volume-path green**, in the node M317 named as
the OW's third carrier. **Insurance/custody is the only group positive on flow, RS20, RS60 AND
days-21-60 at once**, with bases ~2× the banks'. ⚠⚠ **And it is thin**: **one name, with a NEGATIVE
revision book**, carrying a sector tilt. ⚠⚠ **M317's warning is not resolved — this is the FOURTH
carrier statement in four runs**, and a carrier that changes every run is on its way to being
unfalsifiable. **Stated as thin (P4), not sold.**
⚠ **No margin percentile exists for any insurer (C3) ⇒ MET's 8.77× is NOT called cheap.**

### §C Flow / positioning · §D Peers
**3 of Financials' 5 greens are manufactured (BAC · JPM · MA)**; of the two real ones, **ICE is on
the reject ledger.** **MA–JPM residual ρ +0.238** ⇒ payments and banks are separate units (M147);
**{CB, TRV} is a third.** ⚠ **R32 binds: "breadth-led" is dead as a reason and is not rebuilt here** —
74% of the surviving gap is BRK-B (M316).

### §E Refutation · dated catalyst
**S23** 2s10s ≤ +0.20 (**+0.45**, 25bp away) → **08-05** · **S51** NFP → **08-07** ·
**S14/S14-num** MA, any move inside **±3.9%** pre-declared no-information → **08-06**.
⚠ **W3: M138's NII migration means the steepener does not reach every bank** — it supports the
insurance carrier better than the bank carrier, which is where §B put it.

---

## §MATR — Materials · UW− (rotating, first-ever DEEP)

### §A–§E, compressed

| | **NUE** | **STLD** | *(the UW's actual object)* MLM · VMC · CRH · LIN · NEM |
|---|---|---|---|
| flow / `vol_surge` | +0.73 / **1.12** blocked | +0.64 / **0.96** blocked | −0.46 to −0.61, all 🔴 분산 |
| RS20 / RS60 vs **SPY** | **+16.3 / +7.7** | **+13.7 / +2.6** | **−3.7 to −12.7 / −7.6 to −18.8** |
| fwd / trailing P/E | **13.86 / 20.16** | — | — |
| revisions (0q) | ⚠ **7d 1↑:3↓ vs 30d 5↑:0↓ — the two horizons DISAGREE (C2, both quoted)** | — | — |
| Short %float · implied | — | 3.1% covering · **±8.2%, exp 08-21 (D18)** | — |

★★ **The UW− is really an aggregates/cement + industrial-gas underweight wearing a sector name.**
**Dispersion NUE +16.3 vs MLM −12.7 = 29.0pp inside one label, ~9× the sector's own −3.34pp move
vs SPY (W5, the desk's 5th measured instance).**
⛔ **NO 4Phase on NUE or STLD ⇒ NO THESIS MAY BE BUILT. Filed as COVERAGE GAPS, not rejections** —
their measured axes do not reject them, and *"we have not written a thesis"* is not a rejection reason.
**§E**: **S36 → 08-05**, and it **can only falsify** (confirming leg disqualified, 3rd measurement).
⚠ **Copper: COT 96th-%ile long vs FCX 분산 — both instruments inadmissible (D6 REJECTED + C-grade)
⇒ `indistinguishable` (C4), deliberately UNBRACKETED.**

---

## §DISC — Consumer Discretionary · N+ (rotating, first-ever DEEP)

### §A Numbers

| | **F (Ford)** ★new | GM | AMZN ⚠MFG (the promote's carrier) | RCL |
|---|---|---|---|---|
| flow / `vol_surge` | **+0.74 / 1.14** blocked | +0.70 / 1.06 | +0.78 / 1.37 | +0.20 / 1.03 |
| RS20 / RS60 vs **SPY** | **+9.6 / +22.4** | +16.6 / +13.5 | **+11.6 / −3.9** | +7.1 / **+17.4** |
| **days 21-60** | **+12.8** | −3.1 | **−15.5** | **+10.3** |
| fwd / trailing P/E | **7.88 / — (trailing EPS −$1.87)** | **6.06 / 39.79** | — | — |
| PEG · target | 8.48 · $15.78 | **0.35** · $100.04 | — | — |
| revisions (0q) | 7d **1↑:0↓** · 30d **1↑:0↓** | ⚠ **0↑:0↓ — FROZEN book** | — | — |
| Short · P/C · implied | n/a · **0.47, skew −18.7** · ±4.5% exp 08-07 | — | — | — |

### §B Thesis · freshness `[ALPHA fills]`
★★★ **The N+ promote's carrier (AMZN) has NO 60-day base (RS60 −3.9, days 21-60 −15.5, last-20 share
−295%)** — the same geometry the desk tags EXHAUSTED-BY-CONSTRUCTION on the crude-linked four.
**What actually carries this sector is the auto node**: **F is positive on both windows with a
+12.8 base, OBV agreeing, blocked from 🟢 by `vol_surge` 1.14 alone — and it appears NOWHERE in any
desk file.** ⇒ **"direction stands, driver retracted"** (the R15/R32/R33/R38 shape), filed as a
within-run correction of ROTATION's inherited evidence.
⛔ **NO 4Phase on F or GM ⇒ NO THESIS. Coverage gaps.** ⚠ **GM's margin series terminates FY2021
(M233) ⇒ its 6.06× is NOT called cheap.** ⚠ **F has no trailing multiple at all (negative trailing
EPS) — stated as a blank, not filled.**

### §C–§E
**Travel node RCL/BKNG/CMG** carries RS60 **+17.4/+11.9/+12.0** with real bases — ★ **the
un-bracketed sibling of S54's {UAL, DAL}**, exposed to the same fuel variable. ⚠ **`[inferred]`, no
lag table (W2) ⇒ not admissible as evidence.**
**§E**: AMZN RS20 ≤ 0 ⇒ N+ reverts to N (**08-12**) · F RS60 ≤ 0 ⇒ this DEEP's central finding dies
(**08-12**) · **NFP 08-07 · CPI 08-12** are the household-demand tests (**W4's equivalent**, named
with dates).

---

## §X — Cross-sector LIVE (from `US_LIVE_SHORTLIST.json`, outside the DEEP sectors)

| Name | Status | Why it is here and what it is NOT |
|---|---|---|
| **GRMN · EA · TRI · ICE** | ⛔ **REJECTED (08-02), re-surfaced on IDENTICAL data** | **4 of the 15 shortlist rows.** Rechecks **08-12 / 08-16**; **no revival condition has been met because nothing happened.** ⚠ **EA and TRI additionally wear the "✅청정상승" badge — a rejected name carrying the instrument's most persuasive label is the highest-risk row on this sheet.** **They stay rejected.** |
| **MSFT · STX · MPWR · MET · ITW · BKR · AMZN · XOM · CVX · ETN · PCG** | tagged, various | MET is covered in §FIN. **BKR's ledger row is open with a now-false basis and is NOT resolved early — recheck 08-14 stands (the S1 error the 07-30 run named).** |
| **PSX** | ⛔ **🔴RESOLVED** | Still printed as `CORE-STARTER (BUY)` by `ACTION_TICKETS.md` — **D19, 7th consecutive run.** `core_pick` is **human-locked; NOT modified.** |

### Epicenter-starter module (PREMORTEM flagged a cycle GAP)
🚨 **Energy / oil-refining, rank 2: epicenter 6.89% vs an 8.0% floor (−1.109pp), held = MPC · PSX.**
⚠⚠ **The GAP's MAGNITUDE is `unknown` (C3) — R39 killed the *"XOM is 0% refining"* tag the registry
computes it from, and XOM's own segment printed $4.1–5.5bn (a four-year high).** **Registry
correction needs a human.**
⚠⚠ **And half the counted exposure is PSX, which this desk resolved against on 08-02.** ⇒ **the
correct output is a CONTRADICTION to state, not a shortfall to fill** — handed to ALPHA.
✅ **Rank-1 AI-compute reads 12.96% vs a 12.0% floor (+0.96pp)** — ⚠ **but TSM is outside
`us_top300` (M252, 6th run), so the ✅ is computed on a book the instrument cannot fully see.**

---

## §Z — Names set aside this run, and why NONE was newly rejected

**Zero new `reject_ledger` entries.** Stated with its reason rather than left as an absence:

> **Nothing new was set aside, because nothing new was measured.** With **no new settled tape**, every
> candidate's evidence is the same bar the 08-02 run already adjudicated — and **that run filed five
> rejections (GRMN · EA · TRI · PSX · ICE) on exactly this data.** Filing again would **double-count
> the same decision**, which is precisely what the ledger's ticker×date guard exists to prevent.

⚠ **The four names that WOULD have been candidates for rejection — NUE · STLD · F · GM — are filed as
COVERAGE GAPS instead**, because their measured axes (flow positive, both RS windows positive on
three of four, real 60-day bases) **do not reject them.** The desk's standing rule: *a name is not
rejected on a sector label while its measured flow passes*, and *"no 4Phase exists"* is a reason to
write one, not a reason to kill.
★ **This is the missed-ledger's territory, and two entries were filed at EVENT_ALPHA** (AZN, QQQ),
both `--sample prospective`, keeping the legacy count at **0 for a 6th run.**
