# SECTOR_ROTATION — industry_US — 2026-07-29 (Wed)

> **Delta-only.** MACRO owns the 11-sector verdict (`MACRO_REPORT.md §E`); `SECTOR_FLOW_US.json`
> owns the flow numbers (**asof 2026-07-28 settled**, D74-remediated). Both are on disk all run.
> This file writes **only what changes and why**, and every change is carried by a flow number.
> Benchmark **SPY** inline (C1).

## §1 · Inherited — one line, verbatim from `MACRO_REPORT.md §E`

`MACRO holds: ENRG OW− · IT N · FIN OW− · INDU OW− · HLTH N · COMM N− · UTIL N− · RE N · MATR UW ·
DISC N− · STPL N.`

## §2 · Deltas — three changes, three declines, all carried by flow

| Sector | Matrix said | Flow evidence (wflow · eqflow · breadth · Δd/d · 🟢/🔴) | New verdict | Who resolves |
|---|---|---|---|---|
| **Industrials** | OW− | **+0.028 · +0.084 · breadth 0.180 · Δ −0.028 · 9🟢/13🔴** — **breadth 0.180 is the board's highest by 1.2× (next COMM 0.150)**, **9 of the board's 17 greens** and **5 of the 8 `new_green`** sit here, and **eqflow > wflow** ⇒ breadth-led, not mega-cap-narrow | **OW** *(promote one notch)* | **DEEP-INDU** — the question is **which node**: 4 of the 9 greens are **capital goods (WAB · PCAR · MMM · ITW)**, the node M174 measured at **−0.193 flow with 0🟢/16🔴** five days ago |
| **Information Technology** | N (split unconfirmed) | **−0.068 · −0.303 · breadth 0.000 · Δ −0.237 · 0🟢/29🔴** — **eqflow is 4.5× worse than wflow** (mega-caps holding up a collapsing tail), **29 reds = 48% of the board's entire red count**, and **only 9 of 56 names even reach `OBV-매집 ∧ RS20>0`** (Financials 32/47, Industrials 21/50) ⇒ **SWEEP diagnosed this absence as evidence, not a filter artifact** | **N−** *(demote one notch, with NAMED carve-outs)* | **S13 · S30**, both settling on dated observables |
| **Materials** | UW | **−0.027 · +0.128 · breadth 0.000 · Δ +0.301 · 0🟢/12** — **Δ +0.301 is the board's largest positive delta**, and eqflow is positive while wflow is negative | **UW−** *(promote one notch, not two)* | **S36**, window to **2026-08-05** |

### Why IT's demote is not a blanket verdict — the carve-outs are named, per the standing rule

A blanket IT underweight **arithmetically shorts the four cleanest instances of the desk's only
A-grade verified signal** (STANDING_VIEW §3a, carried). **N− applies to the sector label and
explicitly NOT to:**
- **the security/observability node** — PANW · CRWD · FTNT · DDOG (RS60 **+59.8 to +86.4** vs SPY);
  ⚠ **3 of the 4 now carry NEGATIVE RS20** and that is C5's problem, not an argument for the label;
- **DELL · HPE** — the only two names on the board with a FINRA 🟢 short-collapse (z −2.28 / −2.16)
  and the only two whose 60-day excess sits in days 21–60 (**+89.9 / +52.9**);
- **AAPL** — RS20 **+20.7** / RS60 **+22.2**, the strongest two-window agreement in the sector, **and
  it still carries no thesis anywhere** (HANDOVER §4a).
**W5 stated with the verdict**: RS20 inside "Info Tech" spans **AAPL +20.7 to SNDK −46.5 = 67pp.**

### Why Materials moves one notch and not two

**S36's branch A requires *"5-day excess >0 AND green count still 0."* Both legs read true** (excess
**+5.46pp**, greens **0 of 12**). ⚠ **But SWEEP §4 measured that the second leg is partly a gate
artifact**: **5 of 12 Materials names pass `OBV-매집 ∧ RS20>0` and 5 of 5 are blocked by `vol_surge`
alone** (NUE 1.02 · STLD 1.00 · SHW 1.15 against a 1.20 gate). ⇒ **the "0 greens" is a statement about
the tag, not about Materials**, so a full move to Neutral would be reading a measurement instrument as
a market fact. **One notch, and S36 settles the rest on 08-05.**

### Deltas DECLINED, logged rather than dropped

| Sector | The delta that exists | Why it is declined |
|---|---|---|
| **Energy** | **wflow +0.380 = the board's #1**, and yet **0🟢 of 16 with breadth 0.000** — matrix-OW with the flow tag absent, which the rule says should rotate DOWN a notch (case a) | ★ **The absence is DIAGNOSED, and diagnosis is what the rule requires before citing it.** **8 of 16 pass `OBV-매집 ∧ RS20>0` and 8 of 8 are blocked by `vol_surge` alone** — MPC (surge 0.96, RS20 +18.1 / RS60 +20.2), PSX (0.95, +18.3 / +11.8), XOM (0.85, +12.5 / −3.9). **The money is in Energy without a volume surge.** ⇒ **no rotate-down. OW− held.** ⚠ Adverse fact carried anyway: **PSX's days-21-60 excess has flipped negative (−5.91)**, so M177's clean integrated-vs-refiner split is degrading at the `core_pick` end for a second run |
| **Health Care** | **eqflow +0.241 > wflow +0.162, Δ +0.051**, and **XLV was the 2nd-best 5-day sector (+4.37%)** | ★ **The money moved and C7's REGISTERED observable did not.** C7 resolves on *"one 🟢 from OUTSIDE the top-6 by cap"*; the sector produced **exactly one green, TMO, which is inside the named top-6 block (LLY·JNJ·ABBV·MRK·TMO·UNH)** ⇒ **the observable reads ZERO for a 4th consecutive run.** Promoting on the ETF tape while the registered test reads zero is **moving a threshold after the fact.** **N held; C7 resolves on its own horizon, 2026-08-06** |
| **Consumer Staples** | eqflow **+0.032 > wflow −0.074**, Δ +0.068, and **XLP was the 3rd-best 5-day sector (+3.57%)** | **Breadth 0.000, 0🟢 of 19.** The 5 names passing `OBV∧RS20>0` are all blocked by `vol_surge` (CCEP 0.98 · ADM 0.97 · KO 1.00) ⇒ **the same gate artifact as Energy and Materials — but unlike those two, Staples has no proposition, no bracket and no thesis on this board.** **Promoting a sector nothing claims, on a tag the desk has just measured to be broken, would be inventing a view.** N held, and the gap is stated |

### Deltas that CONFIRM the matrix — one line, no re-derivation

**Financials** (eqflow **+0.374** > wflow +0.294, 2🟢, Δ −0.010) · **Comm Services** (Δ **−0.306**, the
board's most negative, wflow −0.197) · **Cons. Discretionary** (Δ **−0.281**, wflow −0.283) ·
**Utilities** (wflow −0.265 / eqflow −0.270, 1🟢/6🔴) · **Real Estate** (Δ +0.147 but **1🟢 of 12**).
⚠ **Comm Services carries the board's 2nd-highest breadth (0.150) with 2 greens (T, EA) under a
−0.197 wflow** — the cap-weighted drag is its two largest constituents and its tail is alive. **W5
applies to the N− exactly as it applies to IT. DEEP does not own it this run; it is stated.**

### ⚠ Macro re-arguments attempted and DECLINED

- **Energy**: the settled 3-2-1 crack made a window high (72.219) with the kill line 12.22 points away.
  **That is MACRO P4's evidence, not a flow number.** It does **not** justify a notch here and was not
  used for one — the Energy hold above rests on the diagnosed 🟢-gate artifact only.
- **Utilities**: the FCC's foreign-inverter import ban (EVENT_ALPHA Card 4) is a **policy** argument.
  **Declined.** UTIL's flow is unambiguous on its own (−0.265 / −0.270, 6 reds).

## §3 · DEEP picks — **three**, by the rule, with no padding

**Recency input, `DEEP_LOG` lines read from disk**: `07-23 [ENRG,FIN]/[HLTH]` · `07-24 [ENRG,FIN]/[HLTH]`
· `07-25 [ENRG,FIN]/[RE]` · `07-27 [ENRG,FIN]/[INDU]` · `07-28 [ENRG,FIN]/[IT,COMM]`.

**① Continuous-track 2 — `ENRG` · `FIN`.** Both held a continuous slot in the previous run and both
are still top-4 OW today (**ENRG OW−, FIN OW−**) ⇒ **the anti-thrash rule keeps the slots. Stated.**

**② Rotating — `INDU`, and the run is RECENCY-STARVED. Stated.**
After the §2 promote, the OW set is exactly **{INDU, ENRG, FIN}** — three sectors. ENRG and FIN hold
the continuous slots, so the only rotating candidate is **INDU**, which was deep-dived **07-27, two
runs ago** and is therefore *"recently covered"* under the ~3-run rule. **Fallback applied per the
rule: next-highest OW regardless, and it is named as recency-starved rather than hidden.**
★ It is also the right pick on its own evidence: **INDU is the only sector whose internal composition
changed this run** (capital goods igniting inside the node M174 measured at 0🟢/16🔴).

**★ There is no second rotating slot, and this is a decision, not an omission.**
The rule says *"never pad with Neutral/UW to reach 4 — fewer is fine if stated."* The two
highest-information questions on the board — **IT's split** and **Materials' re-argument** — sit in
**N−** and **UW−**, so neither is eligible, **and more importantly a DEEP on either would re-derive
what a dated bracket is about to settle**:
- **IT** → **S13** (capex cross-condition, prints tonight, 10-session window to 08-12) and **S30**
  (supplier median RS20, to 08-05). It was also deep-dived **yesterday**.
- **Materials** → **S36** (5-day excess × green count, to 08-05).
- **Health Care** → **C7's own registered observable**, horizon **08-06**.
**Three DEEPs. No padding.**

### What each DEEP must resolve — the divergence, not the sector

| DEEP | The #1 question, stated as the divergence |
|---|---|
| **ENRG** (continuous) | **The board's #1 wflow produces zero 🟢, and the diagnosis says `vol_surge`.** Is the refining bid **real accumulation arriving quietly**, or **an OBV artifact on thinning volume**? ⚠ **PSX's days-21-60 excess flipped negative while MPC's stayed +2.30** — the `core_pick` is the leg that is degrading. **VLO 07-30 · XOM 07-31 (inside S31's own window) · MPC 08-04 · PSX 08-05** |
| **FIN** (continuous) | **eqflow > wflow for a 5th run — but M173 measured that 56% of that gap was BRK-B and this run did not re-decompose it.** Re-decompose it. ★ And **BX is now a `new_green` (flow +0.783, `vol_surge` 1.21, RS20 +16.6) with no thesis, no 4Phase and no coverage** — the exact shape that surfaced 009150 and T. **S23 is 0.14pp from firing and moved toward the trigger** |
| **INDU** (rotating, recency-starved) | **Is M174's three-way split inverting at the capital-goods end?** M174: primes +0.667 / rails +0.368 / **capital goods −0.193 with 0🟢/16🔴**. Today **WAB (flow 1.00, surge 1.84) · PCAR (0.89, 1.40) · MMM (0.78, 1.21) · ITW (0.78, 1.21)** are all 🟢 and three are `new_green`. ⚠ And **CAT is 🔴분산 −0.76 with RS20 −18.6** inside the same node — so the answer is not "capital goods turned". **W5 first, verdict second** |

## §4 · Linter

```
# REPORT_LINT — 1 file · rules C1, C2, S6, D6 → ✅ SECTOR_ROTATION.md · 총 0건.
```
⚠ Form only; a clean lint is not a correct report.

## DEEP_LOG 2026-07-29: continuous=[ENRG, FIN] rotating=[INDU]

## ✅ EXIT CHECK

- [x] **§1 is ONE line**, inherited verbatim from MACRO §E. No unchanged sector received a row,
      paragraph or restated flow number — the confirming eight are one line in §2.
- [x] **Every §2 delta cites a flow number** (wflow · eqflow · breadth · Δ · 🟢/🔴). **Two macro
      re-arguments were attempted and are logged as declined** (Energy's crack, Utilities' FCC ban);
      neither was used to move a verdict.
- [x] Every matrix×flow divergence named with a resolution owner: Energy → DEEP-ENRG · IT → S13/S30 ·
      Materials → S36 · Health Care → C7's 08-06 horizon · Comm Services → stated, unowned this run.
- [x] **Three DEEP targets picked by the rule** — continuity applied and stated (ENRG, FIN), recency
      starvation applied and stated (INDU). **No padding with a Neutral or UW sector**, with the reason
      written out rather than left as an absence.
- [x] Linter run (§4).
- [x] DEEP_LOG line appended.
