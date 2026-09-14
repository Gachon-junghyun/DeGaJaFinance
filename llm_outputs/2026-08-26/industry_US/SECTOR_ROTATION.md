# SECTOR_ROTATION — industry_US · 2026-08-26 (Stage 4 / L1·ROTATION)

> **Delta-only.** MACRO §E owns the 11-sector verdict and `SECTOR_FLOW_US.json` owns the flow numbers;
> both are on disk all run. This file writes **only what changes and why**, plus the DEEP picks.
> **Zero sizing, zero buy/sell (P4).**

**Axis count this run scored on: `n_axes` = 3** (`SECTOR_FLOW_US.json §scoring`), `vel_coverage`
**17.06%** ⇒ 🚫 **no delta below cites theme freshness or news velocity**, and Δ-vs-prior-snapshot is
read only against the 08-25 snapshot, which is also `n_axes` = 3. ✅ Same scale on both sides.

---

## §0 · 🚨 CORRECTION to the inherited line before §1 can be written (`D48` — recorded, not edited away)

**MACRO §E of THIS RUN carried `Materials` at `N+`. The standing verdict was `N`.** The 2026-08-25
ROTATION demoted it (`DEEP_LOG 2026-08-25: TWO verdict deltas (STPL N+→N · MATR N+→N)`), so MACRO's
`N+` is an **undeclared re-promotion of a sector that had been demoted one session earlier**, carried
forward from the 08-24 state rather than the 08-25 one.

⇒ **`Materials` is restored to `N`. That restoration is a CORRECTION, not a delta**, and it is not
counted in the delta tally below. **MACRO §E's line is left standing with this correction appended**,
per §4c.
⚠ **The same paragraph of MACRO §E also mis-attributed the `STPL N+ → N` demotion to this run** — it
happened on **08-25**. Today's MACRO carried `STPL N` correctly; only its *narration* was wrong.
★ **Both errors are the `D358-KR` class on a non-PREFLIGHT object**: a state inherited from the
run-before-last rather than the last run. **This is the third instance in two days** (the crack-kill
counter and `P96`'s branch were the other two, both logged in `MACRO_REPORT §F`).

---

## §1 · Inherited from MACRO §E — one line, verbatim (with §0's correction applied)

`MACRO holds: ENRG OW · HLTH OW · STPL N · MATR N · COMM N · DISC N · FIN N · RE N− · UTIL UW− · INDU UW− · IT UW`

---

## §2 · Deltas — **1 change from 10 attempts.** Every decline is carried by a number.

### 🚨 The flipper list, reproduced in full even though it changes one verdict
`SECTOR_FLOW_US.json §sector_rotation[].top1_flips_sign`, this run's own snapshot — **3 of 11**, and
**the set changed for the 3rd consecutive run** (08-23/24 Consumer Staples → 08-25 Health Care → today):

| 🚨1名 sector | `top1` | `top1_w` | `wflow` | `eqflow` |
|---|---|---:|---:|---:|
| **Consumer Discretionary** | `AMZN` | **40.2%** | +0.035 | −0.270 |
| **Materials** | `LIN` | 24.7% | −0.059 | −0.106 |
| **Energy** | `XOM` | 30.5% | −0.111 | −0.011 |

Eight print `false`: Information Technology (`NVDA` 19.4) · Financials (`BRK-B` 13.9) ·
**Health Care (`LLY` 19.4 — the restriction PREFLIGHT attached this morning is LIFTED)** ·
Industrials (`CAT` 8.7) · **Consumer Staples (`WMT` 28.9 — `false`, which is what makes today's
delta admissible at all)** · Communication Services (`GOOGL` 38.3) · Real Estate (`WELL` 16.9) ·
Utilities (`NEE` 17.7).
⚠ **`D297`, 8th run**: COMM is treated as a flipper **regardless of its `false` flag** — `GOOGL` +
`GOOG` ≈ **76.6%** of a 12-name bucket across two ticker rows (`M877`, a demonstrated false negative).
**No `wflow` claim is made on COMM at any cut.**

### The one delta

| sector | matrix said | flow evidence (`eqflow` · rank · breadth · 🟢/🔴 · red-rate) | new verdict | who resolves |
|---|---|---|---|---|
| **Consumer Staples** | **N** | `eqflow` **−0.404 = rank 9 of 11** · `wflow` −0.361 · **breadth 0.00** · **0 🟢 / 8 🔴 of 19** · **red-rate 42.1% = 2nd worst on the board, behind only Utilities (66.7%)** · **NOT a flipper** (`WMT` `top1_flips_sign` = false) | **N−** | **DEEP not available (recency 2 runs) — logged to DEEP_LOG with its mandate** |

**Why this one clears the bar and the other nine do not.** It is argued on **absolute `eqflow` level
and rank**, on **breadth**, and on a **red-rate** — three non-cap-weighted flow numbers, none of them
a Δ (the snapshot is a stub-bar snapshot, `D355`), and **none of them a macro re-argument**. The
sector is not a flipper this run, so no substitution is needed.
⚠ **Price corroborates independently but is MACRO's evidence, not this stage's**, and is named only
so the delta is not read as contradicting it: `exc1 −1.233` (board's worst single session),
`exc20 −6.739` with **17 of 19 negative**.

### The nine declines, each with its number

| # | Attempt | Declined because | Routed to |
|---|---|---|---|
| 1 | **`IT` UW → N** (flow-led promotion, rule (b)) | 🚫 **`C4` — the top three `eqflow` levels are not distinguishable**: `HLTH −0.000` · `IT −0.009` · `ENRG −0.011`. **A 0.011 spread across three sectors is not a ranking.** And the second leg of the case — *"IT holds 4 of the board's 6 greens"* — rests on a green count I declared **unreadable** in `SWEEP_READ §5` (`vol_surge` 0.41–0.60 on 3 of those 4, on a bar carrying **2.48%** of normal volume, `D355`). **Promoting on a number this run called unreadable would be the cheapest available error today** | **`C16` — the carried open contradiction. ROTATION may not resolve it by picking a side. Routed to PREMORTEM and to `P101` (settles 09-04)** |
| 2 | **`DISC` N → N−** | `eqflow` **−0.270 = rank 8 of 11 — not bottom**, against price `exc5 +2.348` = **4th best of 11** with 19 of 28 positive. **Two instruments, opposite halves of the board, neither decisive.** ⚠ And it is a **🚨1名 bucket** (`AMZN` 40.2%), so even the permitted `eqflow` substitution sits under a caveat | Left at `N`; the contradiction logged to DEEP_LOG (**5th run** as the board's widest `C5` gap) |
| 3 | **`RE` N− → UW** | `eqflow` **−0.430 = rank 10**, breadth 0.00, 0🟢/3🔴 — **but the price median contradicts it**: `exc5` median **+1.881 = 1.8× its own mean**, i.e. the sector is better than its aggregate. 🚨 **And `P78`'s pre-settle range is 4.889pp, ABOVE its branch-A line (4.71)** ⇒ the "duration complex" the UW rests on **is dispersing**, so demoting RE on a complex-wide read is about to be falsified by the desk's own registered row | **Routed to a DEEP slot (R1) — see §3** |
| 4 | **`FIN` N → N−** | `eqflow` **−0.169 = rank 6 of 11**, dead middle. 1🟢/10🔴 of 47 is a **21.3% red-rate = 7th of 11**. **A mid-rank sector does not carry a notch on rank alone** | **Routed to a DEEP slot (R2) — see §3** |
| 5 | **`ENRG` OW → N+** (rule (a): matrix-OW, flow-absent) | `eqflow` **−0.011 = rank 3 of 11** — the flow is **not** absent; it is third-best on the board. 🚨 **And `ENRG` is a `top1_flips_sign` bucket this run (`XOM` 30.5%)**, so `wflow −0.111` may not carry a demotion **by rule**; the permitted substitute (`eqflow` rank 3) argues the opposite way | Held at `OW`; the price/commodity break is bracketed by **`P100` (09-01)** and covered by a continuous DEEP slot |
| 6 | **`HLTH` OW → N+** | `eqflow` **−0.000 = rank 1 of 11**, red-rate **15.6% = 2nd best**. Nothing supports a notch down. ✅ **And the G3 restriction PREFLIGHT attached to HLTH this morning is LIFTED** — this sector's sign is no longer `LLY`'s on its own snapshot | Held at `OW`, continuous DEEP slot |
| 7 | **`MATR` N → N−** | `eqflow` **−0.106 = rank 4 of 11** and the board's **lowest red-rate (8.3%, 1 of 12)**. 🚨 **A `top1_flips_sign` bucket (`LIN` 24.7%)** ⇒ `wflow` unusable by rule; the substitute says rank 4. **No demotion is carried** | Held at `N` (per §0's correction); the two-name concentration is bracketed by **`P102` (09-09)** |
| 8 | **`COMM` N → any** | 🚫 **DECLINED BY RULE, 8th run.** The Alphabet complex is **76.6%** of a 12-name bucket while `top1_flips_sign` prints `false` (`D297`). **This sector's number is one company and the flag does not say so** | Left at `N`; `D297` count incremented |
| 9 | **`UTIL` UW− → lower** · **`INDU` UW− → lower** | **No notch exists below `UW−`.** Both are the run's best-supported verdicts — `UTIL` `eqflow −0.564` rank 11 with a **66.7% red-rate**, `INDU` **12 reds (the board's most in absolute terms)**, and **both agree with MACRO's price read on all three windows.** A DEEP here would resolve the least of any sector | Held; named in DEEP_LOG so "we looked and passed" stays distinguishable from "we never looked" |

### Named AGREE / DIVERGE (the divergences, with a resolution owner each)

| Divergence | Money side | Price side | Owner |
|---|---|---|---|
| 🚨 **`IT`** — the board's largest | `eqflow` **rank 2 of 11**, red-rate **10.7% = 2nd best on the board** | `exc5 −1.449`, **36 of 56 negative**, `UW` | **PREMORTEM + `P101` (09-04)** — this is `C16` pointed at the desk's biggest sector call |
| **`ENRG`** | `eqflow` rank 3; `MPC`/`PSX`/`VLO` all OBV 매집 with `rs60 +30.9…+36.8` | `exc1 −1.991` and `exc5 −2.763` = **board's worst**, 14/16 negative; the registered crack kill **FIRED** | **`P100` (09-01)** + continuous DEEP |
| **`MATR`** | `eqflow` rank 4, breadth 0.00, **0 greens** | `exc5 +3.740` = **board's best**, but it is `FCX` + `NEM` | **`P102` (09-09)** |
| **`DISC`** | `eqflow` rank 8, breadth 0.00, 0🟢/10🔴 | `exc5 +2.348` rank 4, 19/28 positive | **Unowned — logged to DEEP_LOG, 5th run, no live bracket since `S91` VOIDed** |
| **`RE`** | `eqflow` rank 10, breadth 0.00 | `exc5` median **1.8× mean**; `P78` says the complex disperses | **DEEP R1 (this run)** |
| ✅ **AGREE, both instruments** | `UTIL` (rank 11, 66.7% reds ↔ worst `exc20`) · `INDU` (most reds ↔ negative on all three windows) · `STPL` (rank 9, 42.1% reds ↔ worst `exc1`) | | Nothing to resolve |

---

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

### Continuous track (⌈N/2⌉ = 2) — **`ENRG`, `HLTH`** · continuity rule applied, **6th consecutive run**
Both held a continuous slot in the 08-25 run **and** are still the board's only two `OW` sectors
today. **The anti-thrash continuity rule keeps them, and it is stated rather than assumed.**
Each has a live, dated question this run created:
- **`ENRG`** — the registered crack kill **fired on settled bars** (`M936`) with a **36.1%**
  unconditional base rate, while `eqflow` ranks 3rd and all three refiners read OBV 매집 with
  `rs60 +30.9…+36.8`. **Mandate: is the 20-day leadership the margin or the barrel?** (`P100`, 09-01)
- **`HLTH`** — `eqflow` **rank 1** and the only sector positive on both price windows, and **`M945`
  says the desk's carried "nine-name payer overhang" has closed**: Distributors `exc5 +3.25` at 100%
  participation (`exc1 +2.11`, the sector's best) and Managed Care +1.15 at 100%, against the 08-25
  reading of *"participation 11.1%, all five sector 🔴 there."* **Mandate: verify the node inversion —
  the weak node is now Health Care EQUIPMENT (+0.19, 37.5% participation), a different node.**

### Rotating track (⌊N/2⌋ = 2) — **`RE`, `FIN`** · 🚨 **declared recency-starved deviation, 13th consecutive run**

**The rule cannot be satisfied as written and the deviation is declared, not hidden.** The rule asks
for the *next-highest `OW`* not covered in ~3 runs. **There are only two `OW` sectors on the board and
both took continuous slots.** The next tier (`MATR` at `N`) was covered **2026-08-25 = 1 run ago**,
inside the bar. ⇒ **Fallback: fill from non-`OW` by evidence density, with recency as the tiebreak,
and say so.**

**Recency table (runs since last DEEP, read from `DEEP_LOG` 08-23 / 08-24 / 08-25):**

| Sector | Last covered | Runs ago |
|---|---|---:|
| **RE · FIN · INDU** | 2026-08-22 | **4 — the board's worst, three-way tie** |
| DISC · UTIL | 2026-08-23 | 3 |
| COMM · STPL | 2026-08-24 | 2 |
| ENRG · HLTH · MATR · IT | 2026-08-25 | 1 |

**The tie at 4 runs is broken on evidence density, and the loser is named:**

- **R1 = `RE`** — 🚨 **a registered row of this desk's own is about to falsify the framing the UW rests
  on, TODAY.** `P78`'s pre-settle range is **4.889pp, ABOVE its branch-A line of 4.71**
  (`XLV +3.476` · `XLRE +1.836` · `XLP +1.299` · `XLU −1.412`), and `S108` settled with its three legs
  **2.46pp apart and one negative**. ⇒ **two independent registered observables now say the "duration
  complex" is four objects, not one** — and `RE`'s `N−` inherits `XLU`'s evidence. Add the internal
  contradiction (`eqflow` rank 10 and breadth 0.00 against a price median **1.8×** its mean) and the
  4-run recency, and this is the slot that resolves the most.
- **R2 = `FIN`** — three things converge that no other 4-run sector has: **(i)** `M946` — the
  mean/median sign agreement the 08-25 run recorded as *"CLOSED"* has **RE-OPENED** (mean **+1.842**
  vs median **+0.542** = 3.4×, with **20 of 47 negative**); **(ii)** **`COIN` — the board's single
  highest flow score (+0.978), highest `vol_surge` (1.56), and one of only two names clearing a 1.2
  surge on this bar — sits in Financials**, and EVENT_ALPHA handed it forward as CONFIRMED-EARLY into
  a sector nobody has deep-dived in four runs; **(iii)** two book names (`NDAQ`, `MET`) live here and
  both read 🟡 with `flow_score` −0.347 / −0.422 and `rs20` −1.4 / −5.7 (**RULE D6** — the C-grade OBV
  state is named alongside three non-OBV axes, never alone).
- **`INDU` LOSES the tie, and the reason is stated**: it is the run's **best-supported** verdict —
  `eqflow` rank 7 with **12 reds, the board's most**, 0 greens of 50, and MACRO negative on **all
  three** price windows with 40/50 negative on twenty. **Three instruments already agree.** A DEEP
  slot spent where nothing disagrees buys the least information (`L3`). ⚠ **Its cost is real and is
  logged**: the Canada thread is the board's **#1** by every measure and its **09-08 effective date**
  is unbracketed on the implementation side except by `S123` (09-12).

**No padding.** N = 4 of 4 filled. **No 5th slot promoted** — the one candidate (`IT`, on the `C16`
contradiction) is **routed to PREMORTEM instead**, because its question is *"which instrument is
right"*, which is a pre-mortem question, not a sector-deep-dive question.

## DEEP_LOG 2026-08-26: continuous=[ENRG, HLTH] rotating=[RE, FIN] · N=4/4 · **ONE verdict delta (STPL N→N−) from TEN attempts, carried by three non-cap-weighted flow numbers (`eqflow` −0.404 rank 9 of 11 · breadth 0.00 · red-rate 42.1% = 2nd worst on the board) and by absolute levels rather than Δ, because `D355` makes this a stub-bar snapshot for a 2nd consecutive run (median volume 2.48% of the prior session, 0 of 299 names above 50%)** · 🚨 **§0 CORRECTION, not a delta: this run's own MACRO §E carried `MATR` at `N+` when the standing verdict was `N` (demoted 08-25) — an undeclared re-promotion inherited from the run-before-last; restored to `N` and recorded rather than edited away (`D48`, 3rd instance in two days)** · **flip list 3 of 11 and the set changed for the 3rd consecutive run — Consumer Discretionary/`AMZN`/40.2% · Materials/`LIN`/24.7% · Energy/`XOM`/30.5%; Health Care LEFT the set, so PREFLIGHT's G3 restriction attached this morning was already stale by SWEEP (the 08-25 run recorded the identical sequence with STPL→HLTH — flipper identity has NO run-to-run persistence and must never be inherited)** · 🚨🚨 **the run's structural instrument headline is `M947`/`D366` at SWEEP: the news axis is NOT dying stochastically — the 51 velocity-measured names are `us_top300` ranks 1–51, CONTIGUOUS, and BYTE-IDENTICAL to 08-25's set (overlap 51 of 51). A burst-load drop cannot produce a contiguous rank prefix twice. The axis is CAPPED, and because the cap is a rank prefix of a 42-day-old market-cap file, G1 and G5 are the SAME defect — this retires six runs of "the tunnel drops under burst load", which the 08-25 run's own `M856` already contradicted inside the same run** · 🚨 **`D364` filed at MACRO: a `burst` z computed on a partial-day denominator is systematically overstated — `RUBIN` read z 8.4 (denominator 2,102) on 08-25 and z 3.3 today (denominator 4,973) on the IDENTICAL 8 articles / 5 outlets / 75% market relevance, a 61% fall with zero change in the data; `D354` was built on the 8.4 and its number is withdrawn while its observation survives** · 🚨 **`D367` filed at EVENT_ALPHA: precursor-form threads are selected BEFORE the direction body-read, so a thread-linker artifact gets FIRST pick of eight slots — the "US tariff threat upends copper surplus" thread presented as `BUILDING` 2→2→2→2→3 (the textbook early shape) and its timeline is four days of `fxstreet` FX price-forecast boilerplate with one Reuters article appended; 6 of 10 precursor candidates were of this class, and the failure is asymmetric because it DISPLACES a real card** · 🚨 **`D362` filed: `Canada tariff` accel FELL 10.99× → 5.10× on the same day its thread BUILT 21 → 29 outlets and became the day's #1 head cluster — `D345`'s class measured for the first time on a RISING event, which is the more dangerous direction because a decelerating term reads as CALM on a sector the desk is underweight** · **★★ the tape headline is that the 08-25 close ERASED most of the prior run's governing fact: `EW{STPL+HLTH} − EW{IT}` 5-session went +9.336 (97.6th %ile, 08-24) → +3.905 (85.7th %ile) = −5.43pp, 58% of the distance back to the median, one session after `P79` rolled +7.9pp — two consecutive percentile-extreme readings this desk called load-bearing, both substantially erased by the next single close (`M944`); at a 5-session sd of ~4.7pp the estimator sheds ~20% of its content per day and a p97 reading has a ONE-DAY half-life** · **★★ the registered refiner kill FIRED on settled bars (5-session crack rate −2.862 → −1.675 = two consecutive negatives, `M936`) with Energy `exc1 −1.991` = the board's worst — and the kill's unconditional base rate re-measured at 36.1% of the trailing 252, so a regime marker that fires one day in three fired; `P100` brackets whether the 20-day refining leadership (`exc20 +11.597` = 77.4th %ile) was the margin or the barrel** · **★ the AI narrative is decelerating on THREE independent in-band terms into the epicenter's own D-0 print — `AI capex` 0.66× (base 1,189, 2nd run) · `memory prices` 0.80× (970) · `HBM` 0.88× (1,336) (`M942`) — while the AI-inference chain thread BUILDS and its body-read reverses its headline (Cerebras/AMD in the title; `NVIDIA` design wins at SpaceXAI and Cisco in the last two legs)** · **★ `M937`: the 42-day-old universe has a priced casualty — `EA` ($50.69bn, Comm Svcs) has 6 price bars in a 90-day frame and last traded 08-10; the sweep scored 299 of 300 and named no name for the drop, and Comm Svcs `exc20` silently ran on n=12** · **`M939`: the AI-compute short book is SPLITTING not moving as a bloc — `ANET` FINRA z +2.06 / 5v5 +6.7▲ (board's highest) and `NVDA` +1.78 into its own print, against `AVGO` −2.17 / −10.4▼ and `HPE` −1.73 / −13.2▼ (board's two largest exits), a 4.23 z-unit spread inside one complex on one day** · **rotating slots are a DECLARED recency-starved deviation for a 13th run: only 2 OW exist and both took continuous slots, `MATR` (the next tier) was covered 08-25 at 1-run recency ⇒ R1/R2 filled from non-OW by evidence density with recency as tiebreak; RE and FIN both sit at the board's worst 4-run recency and INDU LOSES the same tie explicitly because three instruments already agree there (`eqflow` rank 7, 12 reds = board's most, 0 greens of 50, negative on all three price windows) and a slot spent where nothing disagrees buys the least information** · **uncovered=[INDU(UW−, 08-22 = 4 runs, tie-loser NAMED not dropped — the Canada thread is the board's #1 (`BUILDING` 23→9→11→24→20→21→29, 370 articles, peak 29 outlets) and inverted from "Trump pauses tariffs" to "Canada matches dollar-for-dollar" in six days; the 09-08 effective date is bracketed only by `S123` (09-12) because `P93` settles 08-28, eleven days early — `D342`), DISC(N, 08-23 = 3 runs, the board's widest `C5` gap for a 5th run: `eqflow` rank 8 with breadth 0.00 and 0🟢/10🔴 against `exc5` rank 4 with 19/28 positive, a 🚨1名 bucket at `AMZN` 40.2%, and NO live bracket since `S91` VOIDed), UTIL(UW−, 08-23 = 3 runs, `eqflow` −0.564 rank 11 with a 66.7% red-rate and `exc20` −7.923 — both instruments agree, nothing to resolve, and unlike 08-25 there is no longer a single-session bounce to disclaim (`exc1` −0.034 ≈ flat)), COMM(N, 08-24 = 2 runs, un-measurable BY RULE for an 8th run — the Alphabet complex is 76.6% of a 12-name bucket while `top1_flips_sign` prints false, `D297`; and `EA`'s disappearance shrank the bucket to 12 names in both instruments), STPL(N− — DEMOTED today, 08-24 = 2 runs, and the demotion's own mandate is the contradiction: red-rate 42.1% = 2nd worst on the board and breadth 0.00, against a price `exc5` +1.817 with only 2 of 19 negative; Canada's 09-08 retaliation list names dairy and agricultural goods and `ADM` is that leg's name with NO bracket — `D342`'s unbracketed half, 2nd run), MATR(N, 08-25 = 1 run, recency-blocked; the entire sector move is `FCX` +20.69 / `NEM` +16.72 while the other ten carry an `exc20` MEDIAN of −8.211 with 9 of 12 negative, Copper COT sits at the 100th percentile for a 4th run, and `P102` now brackets the two-name spread at its 98.8th percentile), IT(UW, 08-25 = 1 run, ROUTED TO PREMORTEM as the `C16` carrier — `eqflow` rank 2 and red-rate 10.7% (2nd best) against 36/56 negative on price, `NVDA` prints TONIGHT at D-0 with FINRA z +1.78 and an implied ±6.0%, and `P101` settles the software−hardware gap 09-04)]**

---

## ✅ EXIT CHECK
- [x] **§1 is ONE line**, inheriting MACRO §E verbatim — with §0's correction applied and the
      correction itself written out rather than silently folded in. No unchanged sector has a row.
- [x] **Every §2 delta cites a flow number.** The single delta rests on `eqflow` level + rank,
      breadth, and red-rate — **no Δ** (stub-bar snapshot) and **no macro argument**.
- [x] **No promotion or demotion rests on a `top1_flips_sign` bucket.** The flip list is reproduced in
      full (3 named, 8 explicitly `false`), and the three attempts touching flipper buckets
      (`DISC`, `MATR`, `ENRG`) are each declined with the substitution or the rule stated inline.
      `COMM` is declined by rule regardless of its `false` flag (`D297`).
- [x] **Axis count stated**: `n_axes` = 3, `vel_coverage` 17.06% ⇒ no freshness/velocity citation in
      any delta, and Δ is read only against a same-axis-count snapshot.
- [x] **Every matrix×flow divergence named with a resolution owner** — `IT`→PREMORTEM/`P101`,
      `ENRG`→`P100`+DEEP, `MATR`→`P102`, `RE`→DEEP R1, `DISC`→DEEP_LOG (unowned, stated).
- [x] **N = 4 DEEP targets picked by the rule**, continuity stated (6th run) and the recency-starved
      fallback **declared** (13th run) with the tie-break and the **tie-loser (`INDU`) named**.
      No padding. **All seven uncovered sectors named in DEEP_LOG with last-covered date and mandate.**
- [x] Linter run on this file.
- [x] `DEEP_LOG` line appended for the next run's recency rule.
