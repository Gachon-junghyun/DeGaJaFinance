# SECTOR_ROTATION — industry_US — 2026-08-04 (Tue) · **delta-only**

> MACRO §G owns the 11-sector verdict; `SECTOR_FLOW_US.json` (asof **2026-08-03 settled**) owns the
> flow numbers. Both are on disk. **This file writes only what changes, why, and who resolves it.**

## §0 · ⚠⚠ A measurement constraint that governs which flow comparisons are admissible today

**D126 landed on the ZERO side: `velocity` is non-null on 0 of 300** (SWEEP §2). The 08-03 controlled
experiment measured that join oscillating **0/300 ↔ 51/300 on identical data**, **flipping three
sector `wflow` signs with no price input.**

⇒ **Run-over-run flow comparisons are inadmissible in this file.** That includes the JSON's own
`delta` column, which is day-over-day and therefore straddles the join boundary.
**Every delta below is carried by a WITHIN-PULL CROSS-SECTIONAL number** — one sector against the
other ten, measured in a single pass, where a uniform join state cancels.
★ **Stated here rather than discovered downstream, because it disqualifies the easiest kind of delta
this stage writes.**

## §1 · Inherited — one line, verbatim from MACRO §G

`MACRO holds: ENRG OW−(under review) · FIN OW− · IT N(split) · HLTH N− · DISC N+ · COMM N · INDU N ·
RE OW− · STPL N · MATR UW− · UTIL UW−`

## §2 · Deltas — two carried, one attempted and DECLINED

| Sector | Matrix said | Flow evidence (within-pull cross-section, asof 08-03) | New verdict | Who resolves |
|---|---|---|---|---|
| **Information Technology** | **N (split, asymmetric)** | **wflow +0.017 vs eqflow −0.181 ⇒ gap +0.198 — the LARGEST mega-cap-narrow gap of all 11 sectors**, 1.27× the runner-up. **27 🔴 of 56 = 48.2% red**, and it is the only sector on the board where the weighted and equal-weighted signs **disagree** (positive vs negative). | **N− (split preserved)** | **DEEP-IT is NOT assigned this run (§3) — resolution passes to the 08-05 bracket cluster (S30's window) and to the next rotating slot, named in DEEP_LOG.** |
| **Consumer Discretionary** | **N+** | **wflow +0.171 vs eqflow +0.015 ⇒ gap +0.156, the 2nd-largest mega-cap-narrow gap**, with **8 🔴 against 2 🟢 of 28 (4:1 red)**. The equal-weighted sector is **flat, not positive.** | **N** | Resolved by the flow itself; **EVENT_ALPHA Card 8 (MCD 🔴분산, flow −0.533) is independent corroboration on a second axis.** |
| **Energy** | **OW− (under review)** | ⚠⚠ **ATTEMPTED DOWNGRADE — DECLINED, and logged rather than dropped.** | **OW− (unchanged)** | **MACRO owns it; the brackets settle it (S31/S53 08-05 · S49/S52 08-06).** |

### §2a · Why the Energy downgrade was declined — the rule bit, and it bit against this run's own headline

**Every reason to downgrade Energy today is a macro or bracket argument, not a flow number:**
S49 FIRED-B (a commodity observable) · a political/windfall leg (a news thread) · S52-A date risk
(a primary text) · OPEC supply (a term count). **The stage's own rule is explicit — *"If the only
reason to move a sector is a macro argument, leave it and say so"*, and the 2026-07-21 precedent
(the RE change citing "flow divergence **+ real-10Y easing**") was logged as a violation for exactly
this.**

**What the flow actually says, within-pull:** Energy is **#1 of 11 on wflow (+0.492) AND #1 on eqflow
(+0.407)** — the only sector leading both axes — with a **mega-cap-narrow gap of just +0.085**, i.e.
**the strength is broad, not four mega-caps.**

⚠⚠ **And the sector's 0 🟢 / 0 🔴 may NOT be cited in either direction.** SWEEP §3a diagnosed it:
**12 of 16 Energy names pass `OBV-매집 ∧ RS20 > 0` and every one is blocked by `vol_surge` alone**
(sector max 1.19; nine names sit 0.75–0.97). **The tag column is a gate state, not a market state.**

★ **The honest statement, which is neither the flow's nor the macro's**: the flow rank is a
**20-day-window object whose window ends on the break session**, so it is **lagging by construction**
and the next two pulls are where it would show. **Leaving the tilt where MACRO put it — OW− *under
review* — is the only reading that does not overstate one instrument over the other.**

⚠ **A second attempt was also declined**: moving **Financials** down because the sector's flow is only
**+0.093 / +0.101** while the OW− rests entirely on the rate mechanism (P13′). **Declined for the same
reason inverted** — the OW− was never carried by flow (R32 killed "breadth-led"), so a weak flow
number is not evidence against it. **It is, however, the reason FIN keeps a DEEP slot (§3).**

### §2b · ⚠ A within-run correction inherited from EVENT_ALPHA and applied here

**MACRO §B's claim that the 08-03 XLE −2.70pp is evidence about C4 (margin vs war premium) is
WITHDRAWN.** EVENT_ALPHA §1 body-read a **second named cause on the same session** — Trump's
on-record demand that Exxon and Chevron *"cut the retail price"*, with the CNBC body reporting
**"Chevron's shares were down more than 2% while Exxon traded about 1% lower AFTER Trump's comments."**
⇒ **the session cannot separate the crack from the politics.** **S49-B is untouched** (its observable
is the commodity, not the equity). **This is the 11th US instance of the D48 "verify runs after
assert" pattern, corrected in-run rather than carried.**

### §2c · Agreements worth one line each (not eleven paragraphs)

**Utilities UW− and Materials UW− are the only sectors negative on wflow AND eqflow** (−0.234/−0.229
and −0.270/−0.169) ⇒ **the UW− tilts are not mega-cap artifacts. AGREE.**
⚠ **Materials' 0 🟢 may not be cited as confirmation** — **S36's confirming leg is already disqualified
(M273/M238)** for the same `vol_surge` reason measured again in SWEEP §2.
**Real Estate is the board's only breadth-led OW-family sector** (eqflow +0.155 > wflow +0.121, gap
**−0.034**, **1 🔴 of 12**) ⇒ **AGREE with the OW−, and it is the reason RE finally takes a slot (§3).**

## §3 · DEEP picks and DEEP_LOG

**Protocol DEEP budget: N = 4 (2 continuous + 2 rotating).**
**Recency input, `DEEP_LOG` lines read from disk**: `07-30 [ENRG,FIN]/[HLTH,RE]` ·
`07-31 [ENRG,FIN]/[IT,UTIL]` · `08-02 [ENRG,FIN]/[IT,INDU]` · `08-03 [ENRG,FIN]/[MATR,DISC]`.

**① Continuous (⌈N/2⌉ = 2) — anti-thrash continuity applied, and stated:**
- **ENRG** — held the continuous slot in the previous run and is **still #1 OW-family and #1 on both
  flow axes** ⇒ **KEEPS the slot.** ★ **And it is the run's #1 question**: a fired bracket (S49-B)
  against the board's best flow, on a jointly-caused session.
- **FIN** — held the slot and is still OW-family ⇒ **KEEPS the slot.** ★ Its mandate is sharper than
  usual: **R32 killed "breadth-led" and the flow axis is offering no replacement**, so the OW− rests
  on **P13′ alone** with **NFP 08-07 (S51)** three sessions out.

**② Rotating (⌊N/2⌋ = 2) — and only ONE qualifies. N = 3 this run, stated rather than padded.**
- **RE** — the **only OW-family sector not deep-dived in the last three runs** (last covered 07-30),
  and it has now been **logged "uncovered, we looked and passed" for two consecutive runs**. Today it
  is the board's **only breadth-led OW-family sector**. ⇒ **takes the rotating slot on the recency rule.**
- **The second rotating slot is LEFT EMPTY.** The rotating pool is *"next-highest **OW** not
  deep-dived in the last ~3 runs"*, and after ENRG · FIN · RE **the OW family is exhausted** —
  every remaining sector is N, N−, N+ or UW−. **The rule says "Never pad with Neutral/UW to reach N —
  fewer is fine if stated."** ⇒ **N = 3, stated.**
- ⚠⚠ **The cost of that discipline is named rather than hidden: Information Technology is where three
  independent instruments converged this run** — SWEEP's **+0.198 mega-cap-narrow gap / 27🔴 of 56**,
  MACRO's **S30 FIRED-A reversing to a −9.55 median in one settled session**, and EVENT_ALPHA Card 6's
  **MU/SNDK 🔴분산**. **It gets a delta (§2) and no DEEP.** It is written into DEEP_LOG as the **next
  run's first rotating pick**, so "we looked and passed" stays distinguishable from "we never looked."

## DEEP_LOG 2026-08-04: continuous=[ENRG, FIN] rotating=[RE] · N=3 of 4 (OW family exhausted — no padding) · uncovered=[IT(★next run's first rotating pick — 3 instruments converged, N− this run), DISC(N, covered 08-03), UTIL(UW−, covered 07-31), MATR(UW−, covered 08-03), INDU(N, covered 08-02), HLTH(N−, covered 07-30, C7 re-check 08-06), COMM(N, covered 07-28), STPL(N, no proposition claims it — ADM on the missed ledger, recheck 08-16)]
