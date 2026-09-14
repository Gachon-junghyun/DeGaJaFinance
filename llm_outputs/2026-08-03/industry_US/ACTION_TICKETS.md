# ACTION_TICKETS — industry_US — 2026-08-03 (Mon) · analytical artifact, ZERO buy/sell advice

> ⚠⚠ **This file is NOT a ticket sheet this run.** With **no new settled US tape** (last settled bar
> 2026-07-31, identical to the previous run's), there is no new information for a ticket to act on.
> What follows is the **bracket board** — what settles when, and what each outcome would falsify.

## 1 · ⛔ Standing defect, 7th consecutive run — the one "BUY"-shaped artifact this desk emits is stale

`scripts/action_bracket.py` continues to print **`CORE-STARTER (tape-independent) — PSX (BUY)`** with
a **2026-08-05** date. Against it:

- **PSX was filed 🔴RESOLVED by this desk's own ALPHA stage on 2026-08-02** on three agreeing axes
  (exhausted base · FINRA z +1.53, the only 🔴 short surge on the pull · P/C 1.25, the only fear
  profile).
- Its `why core` rationale still descends from **R8**, retracted **2026-07-22** (*"PSX is the cheapest
  large refiner on forward"* — on a like-for-like FY26 basis it was the **most expensive** of the three).
- Its base has now deteriorated a **FOURTH** consecutive run: days 21-60 **+1.6 → −5.91 → −8.5 → −5.5**.

⚠⚠ **`core_pick` is a HUMAN-LOCKED registry field and was NOT modified by this or any stage.**
**D19 is registered, unfixed, and now 7 runs old.** A ticket whose stated premises are retracted
strings is worse than no ticket, because it reads as evidence.

---

## 2 · The bracket board — what actually settles, and when

| Date | Bracket / event | Frozen observable | Current state |
|---|---|---|---|
| **08-04 (D-1)** | **MPC** print · **S53** | equity execution leg S49 cannot see | implied **±8.9%, exp 08-21 — COVERS the print** |
| **08-04 (D-1)** | **AMD · ANET** · **S50** | **guidance DIRECTION y/y**, scored on the guide **not** the price | **S50-ANNEX registered today**: ANET is now event-priced (**±11.7%, exp 08-07**), **AMD is not (±6.4%, exp 08-03 = TODAY)** |
| **08-05** | **PSX** print · **S53** · **S31** · **S30** · **S36** · **S9** · **S19** · **S23** | S31: XOM RS20 vs SPY ≤ 0 | XOM **+13.1** ⇒ **branch A tracking AGAINST us** |
| **08-06** | **S49** · **S52** · **S14** · **CEG · LNG** prints · **C7** re-check | S49: 5-sess settled distillate change ≤ −5.0 | **+2.158** ⇒ buffer **7.16 pts** (was recorded 6.07 — **revised, MACRO §D**) |
| **08-07** | **NFP** · **S51** · **VST** print · **S35/S47** windows | S51: 2s10s ≤ +0.20 | **+0.45** ⇒ **25bp away and receding** |
| **08-08** | **S25** (RE) | already scored **ZERO-INFORMATION (D122)** | — |
| **08-10** | ★ **S54** *(registered today)* | EW{UAL,DAL} 5-sess excess vs **SPY**: **A > +8.5pp · B < −4.5pp** | thresholds set from a **measured σ 6.562pp**, not hand-set — see PREMORTEM §6 |
| **08-12** | **July CPI** · S13 · S16 · S24 · S26 · S41 · S42 | S26: HY OAS ≥ 3.10 · S41: IG ≥ 0.90 | **HY 2.84 (26bp) · IG 0.80 (10bp)** |
| **08-13** | **July PPI** · **S46** | ⚠ PPI is **deliberately unbracketed** — it lands one day AFTER every registered observable closes | date arithmetic, not judgement |

---

## 3 · Both-sides brackets for every ≤48h binary — the protocol's hard rule, satisfied

| Binary | Bracket | Both sides present? |
|---|---|---|
| AMD (08-04) · ANET (08-04) | **S50** | ✅ A/B/C, asymmetry pre-declared (only B changes a conclusion) |
| MPC (08-04) | **S53** | ✅ |
| **Iran talks — began TODAY** | **S52** | ✅ A/B/C, symmetric and high-information |

★ **This is the first US run where no ≤48h binary required a new registration to satisfy the rule** —
the brackets were already in place on arrival.

---

## 4 · 🚨 The one flag ALPHA is obliged to carry forward — and it is a CONTRADICTION, not a shortfall

**`CYCLE_EXPOSURE`: Energy / oil-refining (rank 2) — epicenter 6.89% vs an 8.0% floor, −1.109pp.**

Two reasons this may **not** be actioned as a shortfall:

1. ⚠⚠ **The magnitude is `unknown` (C3).** **R39 (2026-08-02) killed the *"XOM is 0% refining"* tag
   the registry computes this from** — XOM's own segment disclosure printed **$4.1–5.5bn, a four-year
   high**. XOM **is held** and **is a refiner** and **is not counted in the epicenter.**
   **Registry correction needs a human.**
2. ⚠⚠ **Half the counted exposure is PSX — which this desk resolved against on 08-02** (§1).
   **A shortfall flag half-carried by a 🔴RESOLVED name is not a shortfall statement.**

⇒ **Stated as a contradiction for a human to resolve. No core, no starter, no size.**

✅ Rank-1 **AI-compute reads 12.96% vs a 12.0% floor (+0.96pp)** — flipped 🚨GAP → ✅ **on
mark-to-market drift for a 9th reading**, held set (AVGO/NVDA/TSM) **unchanged, nothing bought**.
⚠ **TSM is outside `us_top300` (M252, 6th run)** ⇒ the ✅ is computed on a book the grading
instrument cannot fully see.

---

## 5 · Ledger writes this run

| Ledger | Row | Class | Condition | Recheck |
|---|---|---|---|---|
| **reject** | **AMZN** | `C.차트붕괴` | revives-if *"RS60 vs SPY turns positive AND days 21-60 turns positive"* | 2026-08-17 |
| **missed** | **AZN** (AstraZeneca) | `U.발굴부재` | enters-if *"a confirmatory filing OR a second independent primary naming terms"* | 2026-08-17 |
| **missed** | **QQQ** (Nasdaq-100 reconstitution) | `N.유니버스부재` | enters-if *"a dated reconstitution with named adds/drops inside `us_top300`"* | 2026-08-17 |
| **missed** | **RCL** | `Q.확신부족` | enters-if *"a 4Phase is written OR S54 fires branch A"* | 2026-08-17 |

**All three missed rows are `--sample prospective`** (pre-registered at the decision, not harvested
from names that already rose) ⇒ **the legacy count stays 0 for a 6th run, and the prospective stratum
grows — the only stratum from which an edge can ever be estimated (D106).**

⚠ **Zero new rejections at BET, and the reason is stated in `BET_SHEET §Z`**: with no new settled
tape, every candidate's evidence is the bar the 08-02 run already adjudicated — **filing again would
double-count the same decision**, which the ledger's ticker×date guard exists to prevent.
