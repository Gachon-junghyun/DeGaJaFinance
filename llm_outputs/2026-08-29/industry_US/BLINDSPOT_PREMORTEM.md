# BLINDSPOT_PREMORTEM — industry_US · 2026-08-29 (Stage 7 / L1·PREMORTEM ★US-only)

> Four adversarial lenses argue **AGAINST this run's own tilt** before the DEEP budget is committed.
> Anti-tunnel. P4 — analytical only, no sizing.

## §0 · How the fan-out was executed, and the deviation is logged not hidden

The L1 specifies a **4-lens subagent fan-out in one message**. This session carries a standing
instruction not to spawn subagents unless the operator asks. **Resolution taken, and stated rather
than glossed: the four lenses were run in-line, sequentially, against the same inputs the fan-out
would have received** (`SECTOR_ROTATION.md` deltas + DEEP picks · `SECTOR_FLOW_US.json` `asof
2026-08-27` settled · `CATALYST_WATCH.json` · `EVENT_ALPHA.md` cards · the settled 08-28 tape).
⚠ **What is lost is independence, and that is the point of the fan-out** — four sequential lenses
written by one author share priors. **Each lens below therefore states the specific claim of this
run's own tilt it is attacking**, so the adversarial function is at least structurally enforced.
Logged as this run's resolved open decision (skill file, unattended-run rules).

## §0b · 🚨 The implied-move instrument is dead, and the workaround is disclosed

`module_flow <TKR> --positioning` returns **`예상변동 ±nan%`** on **every** ticker probed
(`AVGO` `HPE` `XLV` `XLE` `XLC`), with `RS20`/`RS60` also `+nan%`. Cause: the tool computes off the
last bar and the **2026-08-28 bar has `Close` = NaN on 300 of 301 US names** (`M1059`).
⇒ **`M1065`** `[measured]` **the phantom-bar defect propagates from the price frame into the
positioning tool**, so it is not confined to the sweep.
- ⚠ **Second, independent defect visible in the same output** (`D315`, **6th run**): `AVGO`'s
  positioning line names expiry **2026-08-31, D2** — and `AVGO` **prints 2026-09-02**. The tool picks
  an expiry that **does not span the event** even when it works.
- ✅ **Workaround, and it is the one prior runs used**: straddles read **directly from the option
  chain** at the strike nearest the settled 08-28 close, on the first expiry **spanning** each event.
  Every threshold below is stated against that number. **No threshold is invented** (`M47`).

| name | expiry used | why that expiry | ATM strike | straddle | **implied move** |
|---|---|---|---|---|---|
| `AVGO` | **2026-09-04** | first expiry spanning the **09-02** print (the 09-02 expiry has no 370 strike) | 370.00 | 29.91 | **±8.11%** |
| `AVGO` (cross-check) | 2026-09-02 | robustness | 380.00 | 29.94 | ±8.12% — **agrees to 0.01pp** |
| `RSP` | 2026-09-04 | first expiry spanning the **08-31** MSCI print | 220.00 | 2.34 | **±1.06%** |
| `SPY` | 2026-08-31 | the print's own date | 769.00 | 3.47 | ±0.45% |
| `XLF` | 2026-09-04 | spans NFP 09-04 | 58.00 | 0.79 | **±1.36%** |
| `XLV` | 2026-09-11 | 10-session horizon | 171.00 | 3.77 | **±2.20%** |
| `HPE` | 2026-09-04 | spans its **09-03** print | 52.00 | 5.96 | **±11.39%** |

---

## LENS 1 · UNDER-COMPUTED LEGS — what did NOT get a DEEP slot and has a catalyst ≤5 sessions

**Attacking**: ROTATION's claim that the three OW sectors are where the DEEP budget belongs.

| leg | why it is under-computed | catalyst ≤5 sessions | verdict |
|---|---|---|---|
| 🚨 **Information Technology / AI-compute** | **Declined for promotion** (three admissible numbers, three signs) and **holds no DEEP slot** — while it is the desk's **largest book concentration** and the sector whose grouping `S79` Leg 2 measured as **`U-MIXED`, i.e. described by neither candidate risk unit** | **`AVGO` earnings 2026-09-02 (D-4)** — held, and carrying the **worst `rs60` on the book (−24.4)**. **`HPE` earnings 2026-09-03 (D-5)** — also held; surfaced from a `brief` single-source line, **not** from `catalyst_calendar`, which does not carry it | 🚨 **PROMOTE-TO-DEEP as the 5th slot.** ROTATION deliberately left slot 4 unfilled rather than pad with a Neutral; this lens supplies the reason to fill it that ROTATION could not: **two held names print inside five sessions and no stage in this run has looked at either** |
| **Financials** | Demoted `OW−`→`N` on flow, then handed here unresolved. **Both flow reads agree and are negative (−0.144 / −0.144, no flipper) while the settled tape is +0.605pp `exc5` vs `SPY`** — the only contradiction on the board with **no instrument defect available** | **MSCI quarterly review 08-31 (D-2, inside 48h)** + the **PayPal/Advent-Stripe collapse** (`PYPL` `rs60` **+36.5**, built on a withdrawn offer) | **WITHIN-RUN-WATCH** + bracketed as **`S134`**. Not promoted: a DEEP slot for a sector this run demoted would be reverse-engineering |
| **Utilities** | **Last actual DEEP 2026-08-02 = 27 days**, the least-covered sector on the board, and the AI-power leg is uniformly `🟡`/`🔴`: `NEE` **🔴분산 −0.674**, `VST` **🔴분산 −0.700**, `PWR` −0.321, `GEV` −0.376, `CEG` −0.040 | none dated ≤5 sessions | **WITHIN-RUN-WATCH.** The absence of a catalyst is what keeps it out — recorded so "we never looked" stays distinguishable |
| **Materials** | `UW` held after a declined promotion. **Copper speculative net at the 100th percentile of one year** — the single most extreme positioning reading on the board | none dated ≤5 sessions | **WITHIN-RUN-WATCH.** Contrarian ammunition, not a direction (the tool's own caveat) |
| **Industrials** | `UW−`, declined ON METHOD, no slot | **Aug NFP 09-04 (D-6)** and **Canada tariffs effective 09-08** | **WITHIN-RUN-WATCH** — already bracketed twice (`S126` into the print, `P114` out of it), so a third row would be redundant (`D343`) |

⇒ **DEEP set updated: `HLTH` · `ENRG` · `COMM` · **`IT` (PREMORTEM-promoted 4th slot)**.** N = 4/4.

---

## LENS 2 · REGIME-FLIP / BOTH-SIDES — the against-us branch for every dated binary

**Attacking**: this run's four promotions/demotions, by asking what would have to happen for each to
be wrong on a date that is already on the calendar.

`catalyst_calendar --days 14` returns **5 binaries**. Graded by information content **before** the
event (`B4`), and one is dropped for failing that grade:

| binary | date | already spanned? | against-us branch | graded |
|---|---|---|---|---|
| **MSCI quarterly review** | **08-31 (D-2, ≤48h)** | 🚨 **NO.** Six rows settle 08-31 (`S92` `S94` `S104` `S112` `S124` `S103`) and **not one observes the rebalance itself** — they observe NVDA, IT breadth, PCE and single names | The passive print concentrates **into the mega-caps**, `RSP` loses to `SPY`, and this run's `M1051` ("sector breadth ≠ stock breadth") gets a mechanical rather than a behavioural explanation | **BRACKETED → `S131`.** Mandatory: a ≤48h binary with no both-sides coverage is a protocol violation |
| **`AVGO` earnings** | 09-02 (D-4) | Partially — `S127` is armed, **but its bands (A ≥ +5.928 / B ≤ −4.922) sit INSIDE the ±8.11% implied move** ⇒ **pre-declared NO-INFORMATION** | The print is good and `AVGO`'s −24.4 `rs60` was a discount, not a franchise loss — which would falsify the `MRVL`-took-the-socket reading `S116` left leaning toward B | **BRACKETED → `S132`**, thresholds **outside** ±8.11%. 🚫 **`S127` is NOT re-frozen** (`D242`); it runs beside this row and **if the two disagree, the disagreement is the finding** |
| **Aug NFP** | 09-04 (D-6) | ✅ Yes, twice — `S126` (five sessions **into** it) and `P114` (five sessions **out of** it) | — | **Not re-bracketed.** A third row on one event is `D343` |
| **Aug PPI · Aug CPI** | 09-10 · 09-11 | 🚨 **No rows on either** (MACRO §10 named the gap) | — | 🚫 **DROPPED, with the reason**: neither branch would change a conclusion this run reached. Every verdict above rests on `eqflow`, settled excess returns, or an options-implied move — **none is conditioned on an inflation print**, and `P108` already brackets the credit consequence at 09-11. **Spending a bracket here would be spending it on an event this desk has no exposed claim to** |
| **Hormuz "strait open" statement** | **undated, 2nd run** | ✅ `P107` (through 09-08) and `P112` (through 09-11) | — | **Not re-bracketed.** ⚠ But the calendar is **wrong**: a temporary Iran–Oman transit deal was struck **2026-08-26** and the item is still carried as undated |

### 🚨 The correlated-UW check the field note requires — and it FAILS this run

Two `UW` sectors that are one bet in disguise: **`RE` + `UTIL` + `STPL`** are all booked as duration
underweights. **`M1052` measured them 1.48pp apart on 08-28** (`XLU` −0.815pp · `XLRE` −0.176pp ·
`XLP` **+0.662pp**), reproducing `S108`'s inverted result for a second observation.
⇒ **They are NOT one bet, and this run books them as three — which is correct.** What is *not*
correct is the inherited language that treats them as a group; **`P113` is the registered decider**
and it sits **0.39pp from its informative branch**. Recorded as a **passed** check, not a found one.

---

## LENS 3 · MOMENTUM-CONTINUATION — "already ran" ≠ avoid

**Attacking**: the implicit assumption in this run's `HLTH` promotion and `ENRG` promotion that
names up 28–37% over 60 days are still entries.

| name | state (`asof 2026-08-27` settled) | re-tag | flip condition |
|---|---|---|---|
| **`MPC`** | `rs60` **+36.7**, `rs20` +11.8, **OBV 매집**, flow +0.661 | **EXTENDED-BUT-LIVE** — the 20-day is still positive **under** the 60-day, and OBV is accumulating, not distributing | ⇒ **EXHAUSTED** if OBV turns 분산 on any settled sweep, **or** `P112` branch A fires (Brent ≤84.00) — because then the sector has **no instrument** left to prove the margin is separable (`R89` + `P83` both dead) |
| **`PSX` · `VLO`** | `rs60` +29.8 / +32.7, `rs20` +9.9 / +7.2, both **OBV 매집** | **EXTENDED-BUT-LIVE**, same shape | same, plus `L2` (peak-margin): **`VLO` trades 8.4% ABOVE its mean target** on the carried registry row |
| **`REGN` `AMGN` `TMO` `BDX` `MRK` `VRTX`** | `rs60` **+32.4 / +31.6 / +29.3 / +28.7 / +27.8 / +27.3**, `rs20` all positive (+5.4 to +11.3), **all six OBV 매집** | ★★ **EXTENDED-BUT-LIVE, and this is the run's strongest single finding** — see below | ⇒ **EXHAUSTED** if `S133` branch B fires (EW6 − `XLV` exc10 ≤ −3.00pp) |
| **`DASH`** | `rs60` **+46.2 = the universe's best**, `rs20` +13.4, OBV 매집, flow +0.611 | **EXTENDED-BUT-LIVE** — but it sits in **`DISC`, which this run just demoted to `UW` on `eqflow` −0.325.** ⚠ **The sector call and the best runner on the board point opposite ways**; disclosed, not netted |
| **`PYPL`** | `rs60` **+36.5** but `rs20` **+2.7**, **OBV 중립**, flow +0.078 | 🚨 **EXHAUSTED** — and the mechanism is dated: a third of that 60-day move was a **take-private premium withdrawn on 08-28** (`EVENT_ALPHA` Card 8). **The `rs60` is a carry, not a thesis** | already flipped |
| **`APP`** | `rs60` **−49.9**, `rs20` −26.6, **OBV 분산**, flow **−0.833** | **EXHAUSTED** — the universe's worst on every axis simultaneously | ⇒ EXTENDED-BUT-LIVE only if OBV turns 매집 **and** `rs20` > 0 on two consecutive settled sweeps |
| **`COHR` · `ORCL`** | `rs20` **+14.6 / +15.1** on `rs60` **−32.3 / −39.4**, **both OBV 매집** | **TURN CANDIDATES, not runners** — a 20-day reversal with accumulation under a broken 60-day | ⇒ dead if `rs20` falls back below 0 with OBV 분산. ⚠ **`ORCL` is already in the missed ledger** (`Q.확신부족`, recheck **09-16**); **`COHR` is optical and see Lens 4** |

★★ **`M1066`** `[measured]` **6 of the 14 highest 60-day relative-strength names in the entire
`us_top300` are Health Care, and all six are OBV 매집** — `REGN` `AMGN` `TMO` `BDX` `MRK` `VRTX`,
`rs60` **+27.3 to +32.4**, `rs20` all positive. **This is what `eqflow` +0.102 was measuring, and it
answers ROTATION's "early or trap" mandate directly**: the median Health Care constituent is in a
broad, accumulating 60-day uptrend while **`XLV`'s `exc5` is the board's worst (−2.456pp vs `SPY`)**.
⇒ **`XLV` is cap-weighted and `LLY` is its `top1` flipper — the ETF is reporting on `LLY`, the
constituents are reporting on the sector.** The promotion made in ROTATION §2 is corroborated by a
**second, independent, non-cap-weighted** measurement.
⚠ **`L2` (peak-margin) is not waived**: `MRK` **trades ABOVE its mean target** (upside −4.4%) on the
carried registry row. **The basket is live; the sector's one prior 🟢 is the expensive member.**

---

## LENS 4 · CYCLE-EXPOSURE — registry vs coverage vs the real book

**Attacking**: `cycle_exposure`'s ✅ verdict.

`cycle_exposure --json`: **no GAP.** AI-compute epicenter **16.93%** (need ≥12.0%; `NVDA` `ANET`) ·
Energy/refining **9.97%** (need ≥8.0%; `MPC` `PSX`) · missile-defense 3.83% (⚪ **no threshold set**).

**Three things the ✅ does not cover:**

1. 🚨 **`D250`, 13th consecutive run: `cycle_registry.json` has NO optical row**, so optical exposure
   is **unmeasurable, not zero** — and this run has a live optical signal that the registry cannot
   see: **`COHR` `rs20` +14.6 on `rs60` −32.3 with OBV 매집**, plus `LITE` carrying a standing §3a
   thesis. **A cycle with no registry row cannot produce a GAP flag, so a ✅ is not evidence about it.**
2. 🚨 **`RTX`'s cycle carries `⚪ n/a (기준 미설정)`** — missile-defense has **no minimum set**, so its
   3.83% cannot pass or fail. **And `W4` (name the customers) is unpaid on `RTX` for 210 days.**
   The ✅ is therefore a verdict on **two** of the three registered cycles, not three.
3. **The epicenter names are not confirming.** `NVDA` `🟡중립` flow +0.547 with **OBV 중립**; `ANET`
   `🟡중립` +0.533 **OBV 매집**; `AVGO` **`🟡중립` −0.517, OBV 중립, `rs60` −24.4.**
   ⇒ **the desk holds its core and the core is not accumulating.** Per the standing rule this
   **does not** justify cutting core in a rank-1 cycle — **it gates ADD timing**, and that is the only
   claim made here.

**Cleanest epicenter expressions available, named as the rule requires**: `ANET` (the only held
epicenter name with OBV 매집 **and** positive `rs20` +13.6 / `rs60` +13.2) and — outside the book —
`SHOP` (`rs20` **+22.1**, `rs60` +30.4, OBV 매집, IT) as a non-epicenter chain expression.
🚫 **No sizing** (P4). Handed to BET as candidates, not as weights.

---

## §5 · Brackets registered — four, all both-sided, all thresholds outside the implied move

> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`:
> `S131`–`S134` → **0 hits**. IDs issued by `module_evidence next-id S` (highest existing **`S130`**),
> not hand-grepped (`D76`).
> ⚠ All spot prices are **settled 2026-08-28** via `fast_info.last_price` (`D402`); benchmarks named
> inline (`C1`); **settlement mode TERMINAL** on both branches (`D242`).
> ⚠ **`D388-KR` applied at registration**: every basket row below **enumerates its membership**.

### `S131` — ★★★ MSCI 08-31: does the passive print concentrate or broaden? *(the ≤48h mandatory bracket)*

| | |
|---|---|
| **Event** | MSCI quarterly review, **2026-08-31** — **D-2, inside 48h.** Six rows settle that date and **none observes the rebalance itself** |
| **Frozen observable** | **`RSP` − `SPY` 1-session excess return**, settled closes, **2026-08-28 → 2026-08-31** |
| **Implied move** | `RSP` **±1.06%** (09-04 expiry, ATM K=220, straddle 2.34) · `SPY` **±0.45%** (08-31 expiry). **Both thresholds are outside `RSP`'s own priced move** |
| **A (broadening)** | `RSP` − `SPY` **≥ +1.30pp** — the passive print favours the median stock ⇒ `M1051`'s breadth split narrows and `P106`'s narrowing claim weakens |
| **B (concentration)** | `RSP` − `SPY` **≤ −1.30pp** — the rebalance pushes further into the mega-caps ⇒ **`M1051` gets a mechanical explanation instead of a behavioural one**, and every `eqflow`-based delta this run made is standing on a number the index is actively working against |
| **C** | between — disclosed favourite |
| **Information grade (B4)** | **HIGH on both.** A and B change opposite halves of this run's central reading. **This run made four verdict deltas entirely on `eqflow`; B is the branch that says the market is paying for the other number** |
| **Anti-signal (VOID)** | a market-wide trading halt, **or** MSCI postponing/withdrawing the review, inside the window. ⚠ Base rate: low, and the review date is calendar-confirmed |
| **Owner** | `industry_US` |

### `S132` — ★★★ `AVGO` 09-02: the held name with the book's worst 60-day, on a threshold that can actually carry information

| | |
|---|---|
| **Event** | `AVGO` FQ3 earnings, **2026-09-02 (D-4)**. Held. `rs60` **−24.4 = worst on the book** |
| **Frozen observable** | **`AVGO` 1-session excess vs `SPY`** on the first settled close after the print (**2026-09-03**), each vs its own 09-02 close |
| **Implied move** | **±8.11%** — ATM straddle K=370.00 = 29.91 on the **2026-09-04** expiry, the first that spans the print. Cross-checked on the 09-02 expiry (K=380): **±8.12%, agrees to 0.01pp** |
| **A (the discount was wrong)** | excess **≥ +9.00pp** — outside the implied move ⇒ the −24.4 `rs60` was a discount, not a franchise loss, and `S116`'s B-leaning read (`MRVL` took the socket) is falsified |
| **B (the discount was right)** | excess **≤ −9.00pp** — the franchise loss is real and the AI-compute epicenter is **narrower than the book's three names assume** |
| **C** | between — **disclosed favourite, and disclosed as large**: the band spans 18pp against an 8.11% priced move |
| **Relationship to `S127`** | 🚫 **`S127` is NOT re-frozen** (`D242`). Its bands (**A ≥ +5.928 / B ≤ −4.922**) sit **inside** ±8.11% ⇒ **pre-declared NO-INFORMATION**, which is exactly what `D295` predicted when it flagged them as hand-set. **This row is `D295`'s prescription executed**, four runs late. If the two disagree, **the disagreement is the finding** (`S14-ANNEX` precedent) |
| **Anti-signal (VOID)** | `AVGO` postpones the print, **or** an announced acquisition of/by `AVGO` inside 08-31 → 09-03 |
| **Information grade** | **HIGH on both** — both branches change a standing thesis on a **held** name |
| **Owner** | `industry_US` |

### `S133` — ★★★ Health Care: is the promotion the constituents or the ETF?

| | |
|---|---|
| **Why it exists** | ROTATION promoted `HLTH` `N`→`OW` on **`eqflow` +0.102 (board's highest)** *against* **`XLV` `exc5` −2.456pp vs `SPY` (board's worst)**. **This row brackets the promotion this run just made** |
| **Frozen observable** | **`EW{REGN, AMGN, TMO, BDX, MRK, VRTX}` 10-session excess return vs `XLV`**, settled closes, **2026-08-28 → 2026-09-14**. ⚠ **Benchmark is `XLV`, not `SPY`, and named inline (`C1`)** — the question is constituents-vs-cap-weighted, so the sector ETF *is* the correct counterparty. **Membership enumerated** (`D388-KR`): the six `us_top300` Health Care names with the highest `rs60` on the 2026-08-27 settled sweep, all six OBV 매집 |
| **Implied move** | `XLV` **±2.20%** (09-11 expiry, ATM K=171.00, straddle 3.77). Thresholds set **outside** it |
| **A (the constituents are the sector — promotion right)** | EW6 − `XLV` **≥ +3.00pp** ⇒ `XLV` is reporting on `LLY`, `eqflow` was the better instrument, and G5's "prefer `eqflow`" rule earned its keep |
| **B (the ETF is the sector — promotion wrong)** | EW6 − `XLV` **≤ −3.00pp** ⇒ **the promotion made in `SECTOR_ROTATION §2` was wrong**, and a 60-day `rs` screen picked six names that were about to mean-revert together |
| **C** | between — disclosed favourite |
| **Information grade (B4)** | **HIGH on B, MEDIUM on A.** A largely confirms a direction this run already took; **B falsifies a verdict change this run made today**, which is the rarer and more useful outcome. **Stated at registration, not discovered at scoring** |
| **Anti-signal (VOID)** | an **FDA action or trial readout with a named date** at ≥2 of the six inside the window. ⚠ **Base rate checked and NOT remote** — `LLY` took an FDA Mounjaro CV approval on 08-28 (7 outlets) and the head layer carried three other FDA items the same day. **Disclosed as live** |
| **Owner** | `industry_US` |

### `S134` — ★★ Financials: the contradiction with no instrument defect to blame

| | |
|---|---|
| **Why it exists** | The only sector where **both** flow reads agree (`wflow` −0.144, `eqflow` −0.144), **neither is a flipper**, and the settled tape is **positive** (`XLF` `exc5` **+0.605pp vs `SPY`**). Every other contradiction on the board has an instrument defect available; this one does not |
| **Frozen observable** | **`XLF` 5-session excess vs `SPY`**, settled closes, **2026-08-28 → 2026-09-04** |
| **Implied move** | `XLF` **±1.36%** (09-04 expiry, ATM K=58.00, straddle 0.79). Thresholds outside it |
| **A (the tape was right, the flow axes were late)** | `XLF` exc5 **≥ +2.00pp** ⇒ ROTATION's demotion `OW−`→`N` was wrong, and a sector's `eqflow` can be negative for a week while it outperforms |
| **B (the flow was right)** | `XLF` exc5 **≤ −2.00pp** ⇒ the demotion was early and correct |
| **C** | between — disclosed favourite |
| **Information grade (B4)** | **HIGH on A** — A falsifies a demotion this run made **and** would be the first evidence this desk has that `eqflow` can be wrong for a full week on a non-flipper bucket. B confirms |
| **Anti-signal (VOID)** | **Aug NFP prints 09-04, the window's last day** — the window deliberately ends **on** the print so the observable is the five sessions **before** it. If the print is moved earlier, the row VOIDs |
| **Hypothesis recorded, NOT adopted** | `EVENT_ALPHA` Card 8: a take-private premium unwinding inside the sector (`PYPL` `rs60` **+36.5** built on an offer withdrawn 08-28). **Named so a later run can test it; the row does not depend on it** |
| **Owner** | `industry_US` |

---

## §6 · Outputs handed forward

| destination | what |
|---|---|
| **DEEP (Stage 8)** | **Final set: `HLTH` · `ENRG` · `COMM` · `IT`** — N = **4/4**, the 4th filled by this stage's Lens-1 promotion. `IT`'s mandate: **two held names print inside five sessions (`AVGO` 09-02, `HPE` 09-03) and no stage in this run has looked at either** |
| **ALPHA (Stage 10) — action brackets** | `S131` (08-31, ≤48h) · `S132` (09-02) · `S133` (09-14) · `S134` (09-04) |
| **BET (Stage 9) — epicenter starters** | `ANET` (only held epicenter name with OBV 매집 **and** both `rs` positive) · `SHOP` (non-epicenter chain, `rs20` +22.1). **No sizing** (P4) |
| **BET — momentum re-tags** | EXTENDED-BUT-LIVE: `MPC` `PSX` `VLO`, the six HLTH names, `DASH` · EXHAUSTED: `PYPL`, `APP` · TURN CANDIDATES: `COHR`, `ORCL` |
| **Human / `idle_probe`** | `D250` (no optical row, **13th run**) · `RTX`'s cycle threshold **unset** · `D315` (`--positioning` picks a non-spanning expiry, **6th run**) · **`M1065`** (the phantom bar reaches `module_flow`, not just the sweep) |

## ✅ EXIT CHECK
- [x] **4 lenses run**, each attacking a **named claim of this run's own tilt**, each returning **named tickers + dated catalysts**. ⚠ The fan-out was executed **in-line, not as parallel subagents**, and the deviation, its reason, and **what it costs (independence)** are stated in §0 rather than omitted.
- [x] **Every bracket names observable + frozen threshold + date, with BOTH branches.** Four registered (`S131`–`S134`); zero one-way. Registration into `handoff/SCENARIOS_US.md` + the `SCENARIOS.md` MASTER INDEX follows this file (see the run log).
- [x] **Every magnitude threshold stated against the implied move**, and the implied move was **re-derived from the option chain** because `module_flow --positioning` returned `±nan%` on every ticker (`M1065`). **`S127`'s inherited bands are pre-declared NO-INFORMATION** for sitting inside ±8.11% — the tool's failure was measured, not worked around silently.
- [x] **Each branch graded by information content before the event**, and **one binary was DROPPED for failing that grade with the reason written** (Aug PPI/CPI — no verdict this run is conditioned on an inflation print, and `P108` already owns the credit consequence).
- [x] `BLINDSPOT_PREMORTEM.md` written — legs · brackets · re-tags · cycle GAP.
- [x] **Every catalyst-bearing leg promoted or logged**; brackets to ALPHA; the cycle findings to BET and to the human queue. **Nothing silently dropped** — the four WITHIN-RUN-WATCH legs are named with the reason they stayed out.
- [x] **DEEP set updated and stated**: `HLTH` · `ENRG` · `COMM` · **`IT` (promoted here)**.
- [x] 🚨 **The ≤48h binary (MSCI 08-31) is bracketed both ways** (`S131`). A one-way tilt into it would have been a protocol violation, and **six rows already settling on that date observe something else** — the gap was real.
