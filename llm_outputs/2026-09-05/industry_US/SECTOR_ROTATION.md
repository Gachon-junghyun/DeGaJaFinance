# SECTOR_ROTATION — industry_US · 2026-09-05 (Sat) · Stage 6 / L1·ROTATION

> **Delta-only.** MACRO §E owns the 11-sector wind; `SECTOR_FLOW_US.json` owns the flow numbers.
> Both are on disk all run. This file writes **only what changes and why**, plus the DEEP picks.
> **Analytical output only — no sizing, no buy/sell language (P4).**

## 🚨 Instrument state governing every delta below

`SECTOR_FLOW_US.json §scoring` = **`n_axes = 3` (`nonews`) · `vel_coverage` 16.39% · `scored` 299 ·
`dropped_missing_axis` 0**, asof **2026-09-04**, a settled Friday close.

- 🚫 **The news axis is DEAD. No delta below cites theme freshness or news velocity** — the cause was
  probed and is the **pipe, not the market** (`PREFLIGHT §G1`: 6/6 alive pre-sweep, 0/4 immediately
  post-sweep, alive again at t+60s; coverage is universe positions 0–48 exactly).
- ✅ **Δ is legal and citable directly from the primary file this run.** `prev` resolves to
  **2026-09-03**, same `nonews` 3-axis mode ⇒ a true **one-session** difference, and — unlike 09-04 —
  **both sides were computed off healed caches**, so no baseline repair was needed and no
  `_REPAIRED.json` exists (`PREFLIGHT §G2`).
- 🚫 **Cap weights are 52 days old (`G5`).** Where `wflow` and `eqflow` disagree, **`eqflow` is the
  citable cut** and is named on every line below.
- ⚠ The sweep is asof the **previous close**; the 09-04 payroll session IS in it, but nothing after.

## §1 · Inherited — one line

**Standing verdicts, carried from the 2026-09-02 `industry_US` ROTATION (the last run to issue any):**
`ENRG OW · HLTH OW · MATR N · IT N · STPL N · UTIL UW · RE UW · FIN UW · DISC UW · INDU UW− · COMM no-verdict issued`.

**Today's MACRO §E wind, verbatim:**
`ENRG OW · HLTH OW− · IT N · FIN N · UTIL N · MATR N− · RE UW− · STPL UW− · DISC UW · INDU UW · COMM no verdict issued`.

🚨 **`D476` reproduces, and it is this desk's own stage that did it.** MACRO §E is a **wind**, not a
verdict — ROTATION issues verdicts. Today's §E carries six labels that differ from the standing set
(`HLTH`, `FIN`, `UTIL`, `MATR`, `RE`, `STPL`). **None of those is inherited as a change.** Each is
re-derived below against a flow number or **reverted to the standing verdict** — which is exactly
what `D476` was registered for on 09-02 when `MATR OW→N` was made one stage early. Recorded rather
than quietly accepted.

## §2 · Deltas — **3 changes of 11 attempts**

### 🚨 Flip list, reproduced in full even where it changes nothing

**1 of 11 flips: Consumer Discretionary / `AMZN` / `top1_w` 40.2%** — `wflow` **−0.255 → +0.068**
ex-top1. ⇒ **no CD promotion or demotion may rest on `wflow`.**
⚠ **And the flag misses the larger case for an 11th run (`D459`)**: Alphabet is **76.6%** of
Communication Services **under two tickers**, so `top1_flips_sign` prints **False** while
ex-both-classes `wflow` goes **−0.389 → +0.272** (swing **0.661**). ⇒ **COMM is barred too.**
✅ The other nine sectors are non-flippers and their `wflow` signs survive top-1 removal.
★ Two of them are **top-heavy without being sign-dependent** and must not be rejected for it:
`XOM` is 30.5% of Energy and the sector is **more** positive without it (+0.440 → +0.621);
`WMT` is 28.9% of Staples and the sector is **less** negative without it (−0.182 → −0.080).

### The three changes

| sector | standing verdict | flow evidence (`eqflow` · Δ · breadth · 🟢/🔴 · flipper?) | **new verdict** | who resolves |
|---|---|---|---|---|
| **Energy** | **OW** | `eqflow` **+0.562 rank 1/11** · Δ **+0.054** · breadth **0.19 rank 1** · **3🟢 / 0🔴 of 16** · non-flipper (ex-`XOM` **+0.621**, more positive) | **OW+** | — (DEEP continuous) |
| **Financials** | **UW** | `eqflow` **−0.023, from −0.220 = +0.197 in one session** · Δ **−0.004, from −0.220 = +0.216** · 1🟢/10🔴 of 47 · non-flipper (`BRK-B` 13.9%, −0.118 → −0.061, sign holds) | **N** | `S142` (09-11) · `P128` (09-08) |
| **Consumer Staples** | **N** | `eqflow` **−0.098** (from −0.086) · Δ **−0.018** · breadth **0.00** · **0🟢 / 7🔴 of 19** · **non-flipper** — `WMT` 28.9% *holds it up*, ex-top1 −0.080 vs −0.182 | **UW** | DEEP (unslotted, see §3) |

**Why each one qualifies, stated so it can be checked:**

- **`ENRG OW → OW+`.** The delta is **not** the level — the level was already board-best on 09-02 and
  a promotion was **declined then** ("no notch; all three numbers board-best"). **The new information
  is the Δ sign flip.** The 09-04 run recorded the board's sharpest internal contradiction on this
  sector — *rank-1 on level, rank-11 on clean Δ (−0.151)* — and handed it forward unresolved.
  **In one session Δ went −0.151 → +0.054**, and Energy is now the only sector on the board positive
  on `eqflow`, Δ, breadth **and** both price windows (`exc5 +1.89 / 1 of 16 negative`,
  `exc20 +12.29`), with the board's only zero-red row. ⇒ a flow-carried resolution of a flagged
  tension, which is the one thing this stage exists to write.
  ⚠ **Counterweight, stated at the moment of promotion, not after:** the *narrative* on this sector
  is decelerating on every news instrument the desk owns (`crude oil` −14.7%, `Strait of Hormuz`
  −10.4%, `refining margin` **0.66× for a third run**). **`P136` brackets exactly this and settles
  2026-09-14.** The promotion is issued **with its own falsifier already registered**.
- **`FIN UW → N`.** The 09-02 run demoted FIN `N → UW` on `eqflow −0.220` and `Δ −0.220`, calling it
  "2nd demotion in 2 runs but on NEW numbers on both axes". **Both of those numbers have now
  reversed on the same two axes**: `eqflow` −0.023 and Δ −0.004. It is a non-flipper, so the number
  is the bucket's and not `BRK-B`'s. ⚠ **The macro leg is deliberately NOT used**: `hy_oas` at the
  **2.0th percentile** is the strongest fact standing for Financials and it is a **macro
  re-argument** — the exact half of the 2026-07-21 RE change that this stage's rule disqualifies.
  **The promotion rests on `eqflow` + Δ alone.** ⚠ It also runs *against* today's price legs
  (`exc1 −0.58`, `exc5 −0.07`) — stated because a delta that only agrees with itself is not a delta.
- **`STPL N → UW`.** ★ **This delta was BARRED on 09-02 and is admissible today for an instrument
  reason, which is the honest way to say it.** That run declined `STPL N→UW` because the primary and
  repaired sweeps **disagreed about whether `WMT` owned the sign** (`G3` bar). **There is no repaired
  file today** — the 08-28 hole healed and stayed healed — so there is one file, `top1_flips_sign`
  is `False`, and removing `WMT` makes the sector **less** negative (−0.182 → −0.080), i.e. the
  negative sign belongs to the other eighteen names. With `eqflow` −0.098, Δ −0.018, breadth
  **0.00** and **0 greens against 7 reds of 19**, the demotion is carried.

### 8 declines, each with its number

| attempt | declined because |
|---|---|
| `HLTH OW → OW−` (MACRO's wind) | **Reverted to standing `OW`.** `eqflow` **+0.190 = rank 2 of 11** and one of only **two** positive readings on the board; `exc5 +0.63/+0.98` and `exc20 +3.63/+3.74` with **median ≥ mean on both windows**. The only negative is Δ **−0.043**, which is not enough to move a rank-2 level. MACRO's `OW−` was a **wind**, not a verdict (`D476`) |
| `MATR N → N−` (MACRO's wind) | **Reverted to standing `N`.** The numbers do support deterioration (`eqflow` +0.030 → −0.076 → **−0.107** over three runs; `exc20` median **−2.99**; 1🟢/4🔴 of 12; non-flipper — `LIN` 24.7% holds it up, −0.025 → ex-top1 **−0.048**). **Declined on `D343` grounds instead:** **`P102` settles on 2026-09-09** and asks precisely whether Materials is a sector or **two names** (`FCX`+`NEM`). Moving the verdict four days before its own registered bracket settles would make the bracket unscoreable-as-designed. ⚠ `C24` carried a **6th** run: copper spec at the **100th percentile** `[COT 09-01]` |
| `IT N → UW` | **Declined for a 5th consecutive run, and on a NEW reason each time** (method → newness → Δ-direction → axis disagreement → **this**). Today the number moved **the wrong way for a demotion**: `eqflow` **−0.252 rank 10 → −0.195 rank 5** and Δ −0.173 → **−0.010**. Breadth is still terrible (1🟢/17🔴 of 56) but it is no longer deteriorating. ★ And **`P101` settled today inverting the carried split** — software **−4.46%** vs hardware **+2.05%** over 5 sessions, participation **21.1% vs 73.0%** — so the sector's weak half is not where the standing thesis puts it. **Routed to PREMORTEM for a 5th run; `S140` settles 09-08** |
| `UTIL UW → N` (MACRO's wind) | **Reverted to standing `UW`. 5th consecutive decline on a 5th distinct reason: the two axes SWAPPED SIGNS.** On 09-02 the pair was `eqflow` −0.223 (bad) vs Δ **+0.267** (best-but-one); today it is `eqflow` **+0.050** (positive) vs Δ **−0.037** (negative). The disagreement did not resolve — **it inverted**, which is weaker evidence than either reading alone. Breadth **0.00**, **0🟢/3🔴 of 15**. ⚠ The whole positive `eqflow` is two names (`VST` Δ **+0.491**, `CEG` +0.644 flow) — see §3's PREMORTEM offer |
| `RE UW → UW−` (MACRO's wind) | **Reverted to standing `UW`.** The numbers are consistent (`eqflow` −0.124, Δ −0.020, breadth 0.00, 0🟢/2🔴, **11 of 12 negative on exc5**) but they are **not newly worse** — Δ −0.020 is the 4th-smallest on the board. **Deepening a notch on unchanged numbers is padding**, which this stage forbids |
| `DISC UW → UW−` | **Declined.** 🚨 **1名 flipper — `AMZN` 40.2%, `wflow` −0.255 → +0.068.** The non-cap-weighted cut is admissible and **agrees** (`eqflow` **−0.251**, board's 2nd-worst; **21 of 28 negative** on exc5; `exc20 −4.11/−5.27`) — but it moved only −0.232 → −0.251 in a session. **Verdict stays where it is; the flipper status is written out rather than worked around** |
| `INDU UW− → UW` or lower | **Declined — the two axes disagree and the Δ is decomposable.** INDU carries the **board's largest positive Δ (+0.082)** against the **board's worst 20-session leg** (`exc20 −5.04/−5.90`, 33 of 50 negative) and 2🟢/**28🔴** of 50 = the board's worst red rate. ★ **The Δ is four names, not a sector**: `VRT` +0.444, `NSC` +0.403, `GWW` +0.352, `CAT` +0.352 inside a 50-name bucket (SWEEP_READ §4). A Δ that survives no decomposition cannot carry a promotion, and the level does not justify a further demotion beyond `UW−`. ⚠ `S126` settled **`FIRED-C`** on this sector at −1.165pp — no directional information from the bracket either |
| `COMM` — any verdict | **Barred, 15th consecutive run** (`D459`, 11th measured reproduction). Alphabet **76.6%** under two tickers; `top1_flips_sign` prints **False**; ex-both-classes swing **0.661**. `eqflow` **−0.035** is the only citable aggregate and it is **flat**. ⚠ `exc20` **median +3.70 vs mean +1.27** — the same one company dragging the mean. **A sector this desk cannot aggregate is a sector this desk does not rank** |

**Macro re-arguments attempted and declined: 2** — `hy_oas` at the 2.0th percentile for FIN
(the promotion stands on `eqflow`+Δ alone) and the rate complex at the 96th–99th percentile for
RE/STPL (STPL's demotion stands on `eqflow`+breadth+greens alone; RE's was reverted).

### Matrix × flow divergences, each with a resolution owner

| divergence | owner |
|---|---|
| **Energy: every flow and price instrument agrees, every news instrument decelerates** | `P136` (settles **09-14**) · DEEP-ENRG this run |
| **IT: board-best `exc1` (+1.52) against 1🟢/17🔴 of 56** — the rip is storage/memory (`STX` Δ +0.728, `WDC` +0.718, `AMD` +0.566), not the sector | **PREMORTEM** (5th consecutive routing) · `S140` (09-08) · EVENT_ALPHA Card 5 |
| **Industrials: worst level, best Δ — and the Δ is 4 of 50 names** | DEEP (unslotted — logged, see §3) · `P137` indirectly |
| **Utilities: `eqflow` and Δ swapped signs between runs; the positive half is 2 names in a lane spanning 3 GICS labels** | **PREMORTEM offer** · `P123` (09-08) · `D416` |
| **`ETN` (held) is 🔴분산 in a lane where 4 peers accumulate** | **book desk + BET** (EVENT_ALPHA Card 6 book flag) |

## §3 · DEEP picks + DEEP_LOG

**Protocol DEEP budget: N = 4 (2 continuous + 2 rotating).**

**① Continuous (⌈4/2⌉ = 2) — today's top OW ranks: `ENRG`, `HLTH`.**
Anti-thrash continuity applies and is stated: **both held a continuous slot in the 2026-09-02 run and
both are still top-2 OW today ⇒ both KEEP the slot.**

**② Rotating (⌊4/2⌋ = 2) — UNFILLED, for the second consecutive run.**
The rule takes the *next-highest OW* not covered in ~3 runs. **After today's deltas the board has
exactly two OW sectors** (`ENRG OW+`, `HLTH OW`), and **both are already in the continuous slots**.
Padding with N/UW sectors is forbidden by the rule, so **N = 2 of 4 is filled and the shortfall is
stated rather than hidden.**

🚨 **`M1304` [measured] — a second consecutive run cannot fill its own DEEP budget, and the cause is
the board, not the stage.** 09-02 filled 2 of 4; today fills 2 of 4. The protocol's *DEEP budget*
line says a US cut to N=2 would need **its own measurement** rather than an import of the KR
argument (`W1`). **Two consecutive unfillable runs is the beginning of that measurement** — recorded
here so the next run can count a third rather than re-discover the first. ⚠ `C4`: n = 2.

**Both empty slots are offered to PREMORTEM promotion, with named candidates and reasons:**

| candidate | why it is worth a promoted slot today |
|---|---|
| **IT** (verdict `N`) | Declined for a 5th run, and the reason changed again. **`P101` settled today and inverted the carried split** (`M1251`'s "weak half = semicap" is dated — the 5-session drag is **EDA + security software**: `ADSK` −16.40, `CDNS` −14.01, `SNPS` −11.02, `PANW` −10.32, `DDOG` −10.15). **EVENT_ALPHA Card 5 is CONFIRMED-EARLY on a node inside it** whose three names carry the board's largest Δs and **are invisible to the 🟢 gate because `vol_surge` < 0.70** — the axis under `C29`. `S140` settles **09-08**, and IT is the book's largest concentration |
| **UTIL / the AI-power lane** (verdict `UW`) | The lane **spans three GICS labels** (`ETN`,`VRT` in Industrials; `VST`,`CEG` in Utilities; `GEV` in Industrials) so **no sector verdict can express it** — `D416`, unbuilt. EVENT_ALPHA Card 6 emitted a **BOOK FLAG**: the book's only AI-power holding (`ETN`) is the lane's **only 🔴분산** while four peers accumulate. `P123` settles **09-08**. ⚠ UW sectors do not take DEEP slots by rule, which is precisely why this needs a PREMORTEM promotion rather than a rotation |

**OW sectors left without a slot: none** — both OW sectors got one.

## DEEP_LOG 2026-09-05: continuous=[ENRG, HLTH] rotating=[] · **N=2/4 filled for a SECOND consecutive run — the board has only 2 OW sectors and padding is forbidden; both empty slots offered to PREMORTEM with named candidates (IT, UTIL/AI-power lane) and reasons (`M1304`)** · **verdict deltas 3 of 11 attempts: `ENRG OW→OW+` (carried by the Δ SIGN FLIP −0.151 → **+0.054** that resolves the tension the 09-04 run handed forward unresolved; `eqflow` +0.562 rank 1, breadth 0.19 rank 1, **3🟢/0🔴 = the board's only zero-red sector**, non-flipper where `XOM` 30.5% HOLDS IT DOWN (+0.440 → ex-top1 +0.621); ⚠ issued WITH its own falsifier already registered — `P136`, 09-14, because every news instrument on this sector decelerates), `FIN UW→N` (both axes that carried the 09-02 demotion have reversed: `eqflow` −0.220 → **−0.023** and Δ −0.220 → **−0.004** in one session; non-flipper `BRK-B` 13.9%; ⚠ the `hy_oas` 2.0th-percentile leg was available and was **NOT used** — macro re-argument, declined), `STPL N→UW` (★ **barred on 09-02 by the `G3` two-file disagreement about `WMT`, admissible today because the 08-28 heal held and there is only ONE file**: `top1_flips_sign` False, `WMT` 28.9% HOLDS IT UP (−0.182 → ex-top1 −0.080), `eqflow` −0.098, Δ −0.018, breadth **0.00**, **0🟢/7🔴 of 19**)** · **8 declines each with its number: `HLTH OW−` REVERTED (MACRO wind ≠ verdict, `D476` — `eqflow` +0.190 rank 2, `exc20` median ≥ mean), `MATR N−` REVERTED (numbers DO support it — `eqflow` +0.030→−0.076→−0.107 over three runs, `exc20` median −2.99 — but declined on `D343`: **`P102` settles 09-09** asking whether MATR is two names, and moving four days early would make it unscoreable-as-designed; `C24` carried a 6th run, copper 100th %ile), `IT N→UW` (5th consecutive decline on a 5th distinct reason — **the number moved the wrong way**: `eqflow` rank 10 → rank 5, Δ −0.173 → −0.010; routed to PREMORTEM), `UTIL UW→N` REVERTED (5th decline on a 5th distinct reason — **the two axes SWAPPED SIGNS**: 09-02 `eqflow` −0.223/Δ +0.267 vs today `eqflow` +0.050/Δ −0.037; breadth 0.00, 0🟢/3🔴), `RE UW−` REVERTED (consistent but **not newly worse**; Δ −0.020 is the 4th-smallest on the board — deepening a notch on unchanged numbers is padding), `DISC UW−` (🚨1名 `AMZN` 40.2%, −0.255 → +0.068; the admissible `eqflow` −0.251 AGREES but moved only 0.019 in a session), `INDU UW−→lower/higher` (**the Δ is 4 names of 50** — `VRT`+0.444, `NSC`+0.403, `GWW`+0.352, `CAT`+0.352 — against `exc20` −5.04 worst and 28🔴 of 50; `S126` settled FIRED-C, no directional info), `COMM` any (**barred, 15th run**; `D459` 11th reproduction, swing 0.661, `eqflow` −0.035 flat, `exc20` median +3.70 vs mean +1.27)** · **flip list 1 of 11 — Consumer Discretionary/`AMZN`/40.2%; ★ the LARGER case is invisible to the flag for an 11th run (Alphabet 76.6% of COMM under two tickers, `top1_flips_sign` False)** · **macro re-arguments attempted and declined: 2 (`hy_oas` for FIN, the rate complex for RE/STPL)** · 🚨 **instrument state: `n_axes` 3 (`nonews`), `vel_coverage` **16.39%** ⇒ ZERO deltas cite velocity or freshness, and the cause was PROBED (6/6 alive pre-sweep, 0/4 post, alive again at t+60s — a self-inflicted burst outage, `D502`); Δ IS legal and comes from the PRIMARY file for the first time since 08-28 — prior same-mode snapshot 09-03, **both sides post-heal**, no `_REPAIRED.json` exists; cap weights **52 days stale** so `eqflow` is named as the citable cut on every line** · ★★ **the structural line: `eqflow` is positive in exactly 3 of 11 sectors (ENRG +0.562, HLTH +0.190, UTIL +0.050) and Δ is positive in exactly 3 (INDU +0.082, ENRG +0.054, COMM +0.007) — and the two sets INTERSECT IN ONE NAME, Energy. Every other sector is positive on at most one axis, which is why 8 of 11 attempts were declined on "the two axes disagree" rather than on "the number is small"** · **uncovered=[IT(N, last DEEP 09-02 = 0 runs, routed to PREMORTEM 5th consecutive run, book's largest concentration, `P101` settled today INVERTING the carried split, `S140` 09-08), UTIL(UW, last DEEP 09-02 = 0 runs, offered to PREMORTEM, AI-power lane spans 3 GICS labels `D416`, BOOK FLAG on held `ETN`, `P123` 09-08), MATR(N, last DEEP 09-01 = 1 run, `P102` settles 09-09, `C24` 6th run), COMM(no-verdict, last DEEP 09-01 = 1 run, un-measurable by rule 15th run), FIN(N — PROMOTED TODAY, last DEEP 08-30 = 4 runs, `P128` 09-08 and `S142` 09-11 both bracket it), INDU(UW−, last DEEP 08-27 = 6 runs, board's worst `exc20` AND board's best Δ, the Δ decomposes to 4 names), STPL(UW — DEMOTED TODAY, last DEEP 08-27 = 6 runs, 0🟢/7🔴 of 19, the demotion the two-file disagreement blocked on 09-02), DISC(UW, last DEEP 08-27 = 6 runs, 🚨1名 `AMZN` 40.2%, 21 of 28 negative on exc5), RE(UW, last DEEP 08-26 = **7 runs, the longest recency gap on the board for a 2nd consecutive run**, 11 of 12 negative on exc5 — the board's most internally consistent bucket and consistently bad; NOT slotted because UW sectors do not take DEEP slots)]**

---

## ✅ EXIT CHECK — ROTATION

- [x] **§1 is one line** (two, because MACRO's wind and the standing verdict set differ and `D476`
      requires both to be visible). **No unchanged sector has a row, a paragraph, or a restated flow
      number** — the eleven-sector table lives in `MACRO §E` and `SECTOR_FLOW_US.json` and is not
      reprinted here.
- [x] **Every delta cites a flow number.** ENRG: Δ sign flip −0.151 → +0.054 with `eqflow` +0.562.
      FIN: `eqflow` +0.197 and Δ +0.216 in one session. STPL: `eqflow` −0.098, breadth 0.00,
      0🟢/7🔴. **Two macro re-arguments were available, attempted and logged as declined**
      (`hy_oas` for FIN; the rate complex for RE/STPL).
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** DISC declined with
      *"this sector's sign is `AMZN` at 40.2%"* written out; COMM barred entirely on the dual-class
      case the flag misses. **The flip list is reproduced in §2 even though it changed nothing**, and
      the two top-heavy-but-not-sign-dependent cases (`XOM`, `WMT`) are distinguished from flippers.
- [x] **Axis count stated** — `n_axes = 3`, `vel_coverage` 16.39%. **Zero deltas cite freshness or
      velocity.** Δ is read only against a **same-mode** (`nonews`) snapshot, 2026-09-03, and both
      sides are post-heal.
- [x] **Every matrix × flow divergence named with a resolution owner** (§2, five rows).
- [x] **DEEP targets picked by the rule at the protocol's budget** — continuity stated for both
      continuous slots; **rotating slots UNFILLED and the shortfall stated, not padded**; both
      offered to PREMORTEM with named candidates. **OW sectors without a slot: none.**
- [x] **Linter run** — `report_lint.py` ⇒ **0 findings** (C1/C2/S6/D6). ⚠ Form only; a clean run is
      not a correct report.
- [x] **DEEP_LOG line appended** with the uncovered list and each sector's last-DEEP recency.
- [x] Delta count is 3, not 0 — and the eight declines are written with their numbers so a reader can
      see the difference between *"we looked and passed"* and *"we never looked"*.
