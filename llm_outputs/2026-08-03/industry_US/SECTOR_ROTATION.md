# SECTOR_ROTATION — industry_US — 2026-08-03 (Mon) · delta-only

## §1 · Inherited — one line, verbatim from MACRO §G

`MACRO holds: ENRG OW− · FIN OW− · RE OW− · IT N · DISC N+ · COMM N · INDU N · STPL N · HLTH N− · MATR UW− · UTIL UW−`

---

## §2 · Deltas — **ZERO**, and the reason is a measurement, not a shrug

**No sector changes verdict this run.** The EXIT CHECK names this as a valid, informative outcome;
here it is also the *only* defensible one, for a reason this run measured rather than assumed:

> **A delta must be carried by a flow number. This run's flow numbers moved without prices moving.**

`SWEEP_READ.md §2` isolated it as a controlled experiment — same `asof 2026-07-31`, second pull:
**`velocity` non-null 0/300 → 51/300**, **🟢 16 → 26 (10 manufactured, 0 removed)**, and **8 of 11
sectors' `wflow` moved with THREE changing sign** (COMM −0.217→+0.061 · HLTH −0.112→+0.045 ·
STPL −0.130→+0.003). ⇒ **Every apparent flow improvement available to this stage is a candidate
artifact of D126, and promoting a sector on one would be promoting a code path.**

### Attempts considered and DECLINED, logged rather than dropped

| Sector | The tempting move | Why declined |
|---|---|---|
| **HLTH N− → N** | Its `wflow` **flipped sign** to +0.045, and the 08-02 demote cited negative flow | ⛔ **The sign flip is D126.** On the same settled bar. **The demote's flow leg is not reproducible — but neither is a promote.** Verdict held; the *evidence* is downgraded, not the tilt. Owner: **the D126 fix (human)**, not a DEEP |
| **COMM N → N+** | `wflow` **−0.217 → +0.061**, sign flip | ⛔ Same artifact. And **exc60d −9.60pp is still the board's worst 60-day**, which did not move |
| **STPL N → N+** | `wflow` **−0.130 → +0.003**, sign flip | ⛔ Same artifact, and the move is to *zero*, not to positive |
| **IT N → N+** | `wflow` **+0.081 → +0.264 (3.3×)**, greens 4 → 8 | ⛔ Same artifact. ⚠ **4 of the 8 greens are on the manufactured list (AVGO · NVDA · CSCO · WDC).** The N verdict rests on P3/P10/P15, none of which is a flow argument, so **the tilt survives the instrument problem intact** |
| **ENRG OW− → N** | **EVENT_ALPHA Card 1: the war premium is being priced out** (WTI −8% on Iran-talks hopes), Card 3 corrects the OPEC+ supply leg down to 188k bpd | ⛔⛔ **MACRO RE-ARGUMENT — DECLINED, and logged as one.** This is precisely the failure the 2026-07-21 rule was written from (*"3 runs of flow divergence + real-10Y easing"* — the second half did not qualify). **The flow says the opposite and it is one of the three readings this run can quote without a pull caveat: ENRG is #1 wflow (+0.567), eqflow +0.475, ZERO reds of 16, and essentially unchanged across both pulls (+0.519 → +0.567).** ⚠ The commodity move is on an **unsettled** bar (CL volume ~30–47% of a session). **If ROTATION moved ENRG on it, it would be trading a live tick against a settled instrument.** ⇒ **held, and handed to DEEP-ENRG as its #1 question** |
| **UTIL UW−** | — | ✅ **No temptation and no caveat: the one verdict on the board needing neither a stable velocity join nor the contaminated regulated-seven basket.** UTIL is **identical to 3dp across both pulls** (−0.284 / −0.289, 🟢1/🔴8) and **XLU is worst on all three windows** (−5.29 / −3.38 / −7.57pp vs SPY). **R40 binds: S35/S47 may not be cited — and the UW− does not need them** |

### The one divergence that IS carried, with its resolution owner

| Divergence | Evidence | Owner |
|---|---|---|
| **RE is OW− with NO live instrument at all** | Flow **+0.078 wflow / +0.091 eqflow, identical across both pulls, ZERO 🟢 and ZERO 🔴 of 12** — the only sector with no tag in either direction. **S25 was already scored ZERO-INFORMATION (D122)** — its threshold was true on its own registration bar. ⇒ **an OW− tilt whose sector is neither bought nor sold and whose only bracket cannot discriminate.** ⚠ Not a delta (no flow number moved against it — nothing moved at all) | ⚠ **Unresolved and it does NOT get a DEEP slot this run** (recency rule, §3). **Named here and in DEEP_LOG so "we looked and passed" stays distinguishable from "we never looked."** Binding variable is credit: **IG OAS 0.80 vs S41's 0.90 = 10bp**. Window **08-08 / 08-12** |

---

## §3 · DEEP picks and DEEP_LOG

**Protocol DEEP budget: N = 4** (2 continuous + 2 rotating) — read from `industry_us.md`, which states
the budget was **deliberately left unchanged when `industry_kr` cut to N=2**, because importing that
cut across markets is the W1 violation this repo keeps logging.

**Recency input, `DEEP_LOG` lines read from disk:**
`07-28 [ENRG,FIN]/[IT,COMM]` · `07-29 [ENRG,FIN]/[INDU]` · `07-30 [ENRG,FIN]/[HLTH,RE]` ·
`07-31 [ENRG,FIN]/[IT,UTIL]` · `08-02 [ENRG,FIN]/[IT,INDU] · uncovered=[UTIL, MATR, DISC, HLTH, RE, COMM, STPL]`

### ① Continuous track — ⌈4/2⌉ = 2

- **ENRG** — top OW rank; **held the continuous slot in the previous run and is still top-OW today
  ⇒ anti-thrash continuity applies, slot KEPT (stated).**
- **FIN** — 2nd OW rank; same continuity rule, slot KEPT.

### ② Rotating track — ⌊4/2⌋ = 2 · **recency-starved fallback, stated**

**The rule's first branch is exhausted**: the OW set is `{ENRG, FIN, RE}`; ENRG and FIN hold the
continuous slots, and **RE was deep-dived 2026-07-30 — inside the last ~3 runs** ⇒ **no OW sector
remains that has not been recently covered.** ⇒ **fallback invoked: next-highest regardless,
least-recently-covered tiebreak, and the fallback is declared rather than hidden.**

- **MATR** *(UW−)* — **zero DEEP in the entire 07-22 → 08-02 window**, named as uncovered by the
  previous run and still uncovered. **Mandate**: **S36 settles 2026-08-05 — in two sessions — and its
  CONFIRMING leg is disqualified** (M273/M238, re-confirmed by this run's SWEEP: 5 of 12 pass the
  accumulation pre-condition, all 5 blocked by `vol_surge` alone, sector max 1.14 vs a 1.20 gate)
  ⇒ **the bracket can only FALSIFY the UW, never confirm it.** DEEP must answer: *on what evidence
  does the UW− stand if its own bracket cannot confirm it?* ⚠ Copper COT **96th percentile =
  crowded long** is context, not a signal (**D6 REJECTED row**).
- **DISC** *(N+)* — **zero DEEP in the entire window**, and it carries **an unexamined promote**: the
  08-02 run moved it N− → N+ on **exc5d +5.01pp (the board's biggest 5-day)** against **exc20d
  −1.18pp**, explicitly declaring **n≈1 (AMZN's print)**. **No DEEP has ever tested it.** Mandate:
  *is the N+ a rotation or a single print?* ⚠ **AMZN is on this run's manufactured-green list** —
  its flow tag may not be cited.

**Never padded to reach N**: all four slots are filled by the rule, none by convenience.

### OW / high-value sectors left WITHOUT a slot — logged, not dropped

- **RE (OW−)** — excluded by recency (covered 07-30), **and it is the divergence named in §2.**
  ⚠ This is the second consecutive run in which an OW− sector's un-instrumented state is logged
  rather than resolved.
- **UTIL** — "next-in-line" on the 08-02 log; **passed over deliberately this run** because it is the
  one verdict needing no further evidence (§2). *We looked and passed*, not *we never looked*.
- **HLTH · COMM · STPL** — all three had their flow **sign-flip on D126** this run, so a DEEP would be
  investigating an artifact. **IT · INDU** — covered 08-02.

## DEEP_LOG 2026-08-03: continuous=[ENRG, FIN] rotating=[MATR, DISC] · uncovered=[RE(OW−, covered 07-30, un-instrumented — 2nd run logged), UTIL(passed deliberately), HLTH, COMM, STPL, IT, INDU]
