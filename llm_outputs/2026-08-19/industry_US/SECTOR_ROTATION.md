# SECTOR_ROTATION — industry_US · 2026-08-19 · Stage 6/11 (L1·ROTATION)

> **Delta-only.** MACRO §G owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers.
> Both are on disk. This file writes **what changes and why**, and the DEEP picks.

## §0 · Instrument bindings inherited (they decide what may move)

- 🚫 **G3 flippers — `Financials`/`BRK-B` 13.9% · `Industrials`/`CAT` 8.7% · `Materials`/`LIN` 24.7%
  may not be promoted or demoted on `wflow`.** Use `eqflow`/`breadth` or hold.
- 🚫 **`breadth` is news-contaminated (G1)** and may not be read as an independent statistic.
- 🚫 **Every Δ is TWO sessions (08-14 → 08-18), not one** (G2). Sector weights **35 days stale** (G5).
- ★ **New binding from MACRO §G**: **no sector may be moved on a RAW excess return alone** — 8 of 11
  "outperformed" `SPY` in a −1.34% week and three flip sign under β-adjustment.

## §1 · Inherited from MACRO §G — one line, verbatim

`ENRG OW · INDU OW− · IT N+→N(watch) · HLTH N · FIN N− · MATR N− · DISC N− · COMM UW · STPL UW− ·
UTIL UW · RE UW`

## §2 · Deltas — where the money disagrees with the thesis

**Two verdict changes. Both are carried by a flow number, both survive top-1 removal, and neither
re-argues the macro thesis.** After five runs of `ZERO verdict deltas` on a frozen tape, this is the
first run with two settled sessions behind it.

| sector | matrix said | flow evidence (`wflow` · `eqflow` · Δ 2-session · 🟢/🔴 · top1 test) | **new verdict** | who resolves |
|---|---|---|---|---|
| **Health Care** | **N** | **+0.114 · eqflow +0.163 · Δ +0.228 · 0🟢/2🔴** · top1 `LLY` 19.4%, `wflow_ex_top1` **+0.149 — HIGHER than the headline, no sign flip** | ★ **N → N+** | `S76` settles tonight (both legs) |
| **Consumer Staples** | **UW−** | **+0.083 · eqflow −0.020 · Δ +0.325 — the largest two-session improvement on the board · 1🟢/3🔴** (`WMT` = one of the run's two new-🟢) · top1 `WMT` 28.9%, `wflow_ex_top1` **+0.027, still positive, no sign flip** | ★ **UW− → UW** (one notch) | `S80` settles tonight |

### 2a · Health Care N → N+ — rule (b), and it is breadth-carried, not mega-cap-narrow

**`eqflow +0.163` sits ABOVE `wflow +0.114`**, and removing `LLY` (19.4%) *raises* the sector to
**+0.149**. That is the opposite of the concentration failure the flipper rule exists to catch: the
median Health Care name is better than the cap-weighted print, and the largest name is a drag.
**Rank 2 of 11 by `wflow`**, second-largest two-session Δ, and the sector is **the only one besides
Energy with a β-adjusted excess above +1pp (+1.158 vs `SPY`, β 0.27, 252d)**.

⚠ **The one thing that does NOT support the promotion, stated rather than buried**: `breadth 0.00`,
`0🟢 of 32`. SWEEP §3 diagnosed this — **17 of 32 names pass `OBV 매집 ∧ RS20>0` and 0 of 17 clear
`vol_surge` 1.2; the sector's maximum `vol_surge` is 1.00.** That is a volume gate, not an absence of
money, and it is `M144`'s 7th replication. **The promotion is made on `eqflow` and Δ, which are not
cap-weighted and not news-dependent — not on `breadth`, which G1 forbids.**

⇒ **N+, not OW.** A sector with zero names clearing the volume gate does not get an overweight.

### 2b · Consumer Staples UW− → UW — rule (b), and it is explicitly mega-cap-narrow

**Δ +0.325 is the board's largest by 0.097** (next: Health Care +0.228), the sector is one of only two
with a positive `wflow`, and it survives `WMT`'s removal (**+0.027**, no sign flip).

⚠ **`wflow +0.083 ≫ eqflow −0.020` ⇒ mega-cap-narrow, NOT broad strength** — the protocol requires
this to be said, and it is: the median staples name is still negative. **That is exactly why this is
one notch (UW− → UW) and not two.**

🚨 **And the contradiction is carried, not resolved.** MACRO's β-adjusted column reads **−0.592** for
`XLP` — its raw excess of **+0.852 vs `SPY` flips sign** once β (−0.08) is removed. **The flow axis says
Staples improved more than anything on the board over these two sessions; the risk-adjusted price says
it is a laggard whose raw print was misleading.** Both are measured. The verdict moves one notch on
the flow evidence (this stage's mandate) and **the price disagreement is handed to `S80`, which settles
tonight**, rather than being argued away here.

### 2c · IT — MACRO's change is CONFIRMED by an independent flow number; the "(watch)" is removed

Not a new verdict — a **resolution**. MACRO moved IT `N+ → N (watch)` on `XLK` being the week's worst
raw sector. The flow axis reaches the same place independently and **more strongly**:
**IT's Δ is −0.218, the board's ONLY materially negative two-session delta** (next worst `RE` −0.015),
and `wflow_ex_top1` **−0.268 is WORSE than the headline −0.195** — i.e. removing `NVDA` makes the
sector look worse, so this is **not** a one-name artifact and `top1_flips_sign` is **False**.

⇒ **IT = N, watch removed.** Two independent instruments, same direction, and the flipper rule does
not block it.

### 2d · Blocked by the flipper rule — stated, not silently skipped

| sector | `wflow` | `wflow_ex_top1` | top1 | verdict |
|---|---|---|---|---|
| **Financials** | **+0.028** | **−0.015** 🚩 sign flip | `BRK-B` 13.9% | **held N−** — `eqflow` **−0.087** is negative and would argue for a *demote*, but the sector already sits at N− and a demote on a flipper bucket is exactly what G3 forbids |
| **Industrials** | **−0.028** | **+0.032** 🚩 sign flip | `CAT` 8.7% | **held OW−** — an **8.7%** weight inverting a −0.028 print means the sign rests on one company. `eqflow −0.002` ≈ 0 gives no independent signal either. **Held, and the reason is written down** |
| **Materials** | **−0.117** | **+0.060** 🚩 sign flip | `LIN` 24.7% | **held N−** — `eqflow −0.060` is negative but small. **`S77` settles tonight at −3.231 with 10 of 11 non-`NEM` names negative**, which is the NEM-free evidence this UW has never had; the verdict waits for the settle rather than front-running it |

### 2e · Held with the reason named

- **Energy — held OW.** Rank 1 by `wflow` (+0.354), `eqflow` +0.295, `ex_top1` +0.347 (no flip),
  Δ +0.137, and **the only sector whose lead survives β-adjustment (+3.919 vs `SPY`)**.
  🚨 **Its `0🟢 / 0🔴 of 16` is NOT evidence against it** — 7 of 16 names accumulate with positive
  RS20 and **not one clears `vol_surge` 1.2; the sector maximum is 1.06** (SWEEP §3). This is the
  documented ENRG-shortlist artifact reproducing, and it may not be cited as weakness.
  **No promotion to OW+**: the case for one would rest on the diagnosed artifact, and diagnosing an
  artifact is not the same as having the signal it hid.
- **Communication Services — held UW**, and it becomes a DEEP mandate instead. `wflow −0.439` vs
  `eqflow −0.009` is a **0.430 gap, the widest on the board** — the cap-weighted print is nearly all
  `GOOGL` (38.3%) while the median name is flat. But `ex_top1` is **−0.432, no sign flip**, so the
  flipper rule does **not** block a move — and MACRO's β-adjusted column puts `XLC` at **−0.930, the
  board's worst**. **Two flow-grade instruments point opposite ways.** Moving on either alone would be
  picking a side; the sector is held and the disagreement is handed to Rotating-2.
- **Utilities — held UW.** `eqflow −0.376` ≈ `wflow −0.397` ⇒ uniform, not one name; **0 of 15** pass
  `OBV 매집 ∧ RS20>0` *before* the volume gate, though the sector max `vol_surge` is **1.45** — the
  volume existed and the accumulation did not. **The only genuine absence of the five SWEEP diagnosed.**
  ⚠ Carried contradiction: MACRO §A-1 re-inverts the rate mechanism (bear steepener ⇒ **headwind**
  again, reversing `P65`'s tailwind reading), which now *agrees* with the UW. Noted; **the verdict did
  not move on it, because that is a macro re-argument and does not qualify as a delta.**
- **Real Estate UW · Consumer Discretionary N− — held, no flow delta** (Δ −0.015 and −0.001, i.e. flat
  across two settled sessions).

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

| Slot | Sector | Basis and mandate |
|---|---|---|
| **Continuous 1** | ★ **ENRG (OW)** | **Anti-thrash continuity honoured**: held a continuous slot on 08-15/16/17 and is **still rank 1 OW** today ⇒ keeps the slot. **Mandate**: `P75`/`P70` are being decided by **0.37pp on the control leg** — `EW{MPC,PSX,VLO}` exc5 vs `SPY` **+8.886** against a `BZ=F` 5-session **+2.37%** that clears the ≤+2.0% gate by a hair, while the distillate crack ran **88.41 → 101.96 $/bbl (+13.56)**. **Resolve: is the refining bid margin or barrel?** Second question: does the `0🟢/16` volume-gate artifact hide a name that would otherwise shortlist? |
| **Continuous 2** | ★ **INDU (OW−)** | Held continuous on 08-15/16/17, still rank 2. **Mandate**: `RTX` is one of the run's **two new-🟢** and defense OBV is the broadest accumulation on the board (**6 of 6** names accumulating, **6 of 6** positive RS20 vs `SPY`) — yet the sector's `wflow` is **negative and sign-dependent on `CAT` (8.7%)**. **Resolve: is Industrials a defense sector wearing a machinery label?** `S97` (`LHX`, exc5 −1.862) settles 08-21 and `M719` already measured the EW **+4.32pp better with `LHX` removed** |
| **Rotating 1** | ★★ **MATR (N−)** | **Longest gap on the board — last covered 2026-08-13, 4 runs** (08-14/15/16/17 all passed it over), so the recency rule selects it without a tiebreak. **Mandate — the sector has its first NEM-free evidence and a contradicting positioning extreme in the same run**: `S77` settles **tonight** with the non-`NEM` EW at **−3.231, 10 of 11 negative** (`CTVA` +2.62 the sole positive), which is the confirmation this UW− has never had — while **`Copper` COT sits at the 100th percentile, the most extreme reading on the entire positioning board**. **Resolve which of the two is the sector.** ⚠ `wflow` is inadmissible here (`LIN` 24.7% flipper) |
| **Rotating 2** | ★★ **COMM (UW)** | **Second-longest gap — last covered 2026-08-14, 3 runs.** **Mandate — the widest instrument disagreement in this sweep**: `wflow −0.439` vs `eqflow −0.009` (a **0.430** gap, the board's largest) says *"one name, `GOOGL` at 38.3%"*; the β-adjusted excess vs `SPY` of **−0.930** says *"the board's worst sector."* **Resolve which reading owns the sign**, and do it without `breadth` (G1) and without `wflow` alone. ⚠ Second question forced by G5: **`EA` has been unmeasurable for 7 consecutive runs and it is a Communication Services name** — the sector's composition is 12 of 13 |

**Not selected, and why** — every sector, with its last-covered date:

| sector | last DEEP | why not selected |
|---|---|---|
| **IT** | **2026-08-17** | Covered in each of the last two runs ⇒ recency rule excludes. ⚠ **It has the strongest single flow delta on the board (Δ −0.218)** and two brackets settling 08-21 (`S85`, `S96`), so this exclusion is a real cost and is logged as such |
| **HLTH** | 2026-08-17 | Recency ⇒ excluded, **on the same run it was promoted to N+**. `S76` settles tonight and will inform the next slot |
| **STPL** | 2026-08-17 | Recency ⇒ excluded, **on the same run it was promoted UW− → UW** |
| **UTIL** | 2026-08-16 | Recency; and its UW is the one absence SWEEP graded genuine, so there is least to resolve |
| **CONSUMER** | 2026-08-16 | Recency (5th-slot PREMORTEM promotion) |
| **DISC** | 2026-08-15 | Δ −0.001 — nothing moved |
| **RE** | 2026-08-15 | Δ −0.015 — nothing moved |
| **FIN** | 2026-08-14 | Flipper-blocked (`BRK-B`); `S78` settles tonight and may create a mandate for the next run |

⚠ **Rotating slots were filled from non-OW sectors.** Only two sectors carry an OW-grade verdict
(`ENRG` OW, `INDU` OW−) and both hold continuous slots, so a strict *"next-highest OW"* read would
return **N=2**. **Resolved by following the desk's most recent documented practice** — the 08-15/16/17
runs all filled rotating slots from N/UW sectors with a stated mandate (`DISC`, `RE`, `IT`, `UTIL`,
`STPL`, `HLTH`) — **and the deviation is logged here rather than silently taken.** Both picks carry a
flow-carried mandate; neither is padding.

## DEEP_LOG 2026-08-19: continuous=[ENRG, INDU] rotating=[MATR, COMM] · N=4/4 · **TWO verdict deltas — HLTH N→N+ (eqflow +0.163 > wflow +0.114, `ex_top1` +0.149 HIGHER, Δ +0.228 = 2nd largest) and STPL UW−→UW (Δ +0.325 = board's largest, `ex_top1` +0.027 positive, explicitly mega-cap-narrow since eqflow −0.020) · plus one resolution, IT's "(watch)" removed on Δ −0.218 with `ex_top1` −0.268 WORSE than headline** · ★ **the first non-zero delta count in five runs, and the reason is mechanical: the tape advanced TWO settled sessions (08-14 → 08-18), 298/299 flow_scores moved, median |Δ| 0.127, 44 tag changes** · **blocked by G3 flippers: FIN(`BRK-B` 13.9%) · INDU(`CAT` 8.7%) · MATR(`LIN` 24.7%) — all held** · **uncovered: IT (08-17, ⚠ strongest delta on the board, excluded on recency — a logged cost) · HLTH (08-17, promoted today) · STPL (08-17, promoted today) · UTIL (08-16) · CONSUMER (08-16) · DISC (08-15) · RE (08-15) · FIN (08-14, `S78` settles tonight and may create next run's mandate)** · **rotating slots filled from non-OW per documented 08-15/16/17 practice, deviation logged** · **five brackets settle tonight (S75 S76 S77 S78 S80) — the 08-20 run inherits them as past-due on arrival**

## ✅ EXIT CHECK
- [x] **§1 is one line, verbatim from MACRO §G** — no re-derivation, no per-sector prose for anything
      not changing.
- [x] **§2 carries only deltas, and every delta is carried by a flow number** — `eqflow`/Δ for both
      changes; no macro re-argument was used to move a sector (Utilities' rate-mechanism re-inversion
      was explicitly **not** counted).
- [x] **Every delta survives top-1 removal** — `HLTH` +0.114 → **+0.149** · `STPL` +0.083 → **+0.027**,
      neither flips sign; `IT`'s resolution −0.195 → **−0.268** (worse, so not a one-name artifact).
- [x] **All three G3 flipper buckets named with `top1`/`top1_w` and explicitly held** (§2d).
- [x] AGREE/DIVERGE named: **AGREE = §1's one line**; **DIVERGE** = §2's two rows plus the carried
      `COMM` and `STPL` instrument disagreements, each with the side the money is on.
- [x] new-🟢 read: **`RTX`, `WMT`** — `WMT` is cited as part of the STPL delta, `RTX` as part of the
      INDU mandate.
- [x] **N=4 filled by rule, never by gut**: continuous by anti-thrash continuity (both stated),
      rotating by longest-gap recency (MATR 08-13, COMM 08-14), and the non-OW deviation logged.
- [x] **DEEP_LOG appended** with all four slots, every uncovered sector with its last-covered date,
      the flipper blocks, and the deviation.

---

## ⚠ APPEND-ONLY CORRECTIONS — three claims in this file were refuted by later stages of the same run

*(§1–§3 above are left exactly as written. §4c forbids editing them away. **No verdict in §1–§3
moves** — in every case the underlying price/flow number carried the call unaided and only the
supporting leg is struck.)*

### C-1 · 🚨 §2e's Communication Services reasoning is WRONG — the flipper rule tests TICKERS, not ISSUERS

**What §2e said**: *"`ex_top1` is **−0.432, no sign flip**, so the flipper rule does **not** block a
move here."*

**What broke it** (DEEP-COMM §1.1, re-measured independently from `SECTOR_FLOW_US.json §names`):
**the rule removed `GOOGL` (38.3% of sector cap) and left `GOOG` (38.3%) — the other share class of the
same issuer.**

| removal | `wflow` | `eqflow` | n |
|---|---|---|---|
| none | **−0.439** | −0.008 | 12 |
| ex-`GOOGL` — *the rule's own test* | **−0.432** | +0.032 | 11 |
| **ex-Alphabet (both classes)** | **−0.289** | +0.087 | 10 |
| **ex mega-platform (`GOOGL`+`GOOG`+`META` = 89.1% of sector cap)** | ★ **+0.222** | ★ **+0.178** | 9 |

⇒ **A sign flip does exist and `top1_flips_sign: false` could not see it.** The nine non-mega names run
**6 of 9 positive** (`WBD` +0.604 · `NFLX` +0.494 · `CMCSA` +0.429 · `VZ` +0.400 · `T` +0.383 ·
`DIS` +0.372, against `TMUS` −0.696 · `TTWO` −0.311 · `LYV` −0.075).

**Consequence for §2e**: the sentence *"the flipper rule does not block a move"* is **withdrawn** —
the rule is **structurally blind here**, which is neither a block nor a clearance. **The verdict
(COMM held UW, disagreement handed to Rotating-2 DEEP) does not move**, because it was made by
*declining* to move on either instrument, and that remains the right call for a stronger reason than
the one given: **the sector's cap-weighted sign is 89.1% three companies, and its other nine names
are majority-positive.**
★ Generalised, and this is the transferable part: **`top1_flips_sign` removes the largest TICKER; a
dual-class issuer therefore defeats it by construction.** Registered as dig **`D291`** — *the flipper
test must group by issuer before ranking.* It would bite anywhere dual-class shares sit in one GICS
bucket, not only here.

### C-2 · §2b and §3's new-🟢 legs are struck — both new-🟢 rest on the revoked velocity axis

`RTX` `vol_surge` **0.83** / `velocity` **1.55**; `WMT` `vol_surge` **0.83** / `velocity` **1.35**.
**Only 3 of the run's 8 greens clear `vol_surge` ≥1.2.** Full measurement and the `M25`/`R78`
implications are appended to `SWEEP_READ.md`.
- **§2b (STPL UW−→UW)**: the clause *"(`WMT` = one of the run's two new-🟢)"* is **withdrawn**.
  **The promotion stands** on Δ **+0.325** and `wflow_ex_top1` **+0.027**, both price-only.
- **§3 (INDU mandate)**: *"`RTX` is one of the run's two new-🟢"* is **withdrawn**. The mandate stands
  on `RTX`'s **OBV 매집 +0.368** and **RS20 +13.9 vs `SPY`**.
- 🚫 **No stage after this point may cite the 🟢/🔴 tag, the new-🟢 count, or shortlist membership as
  evidence.**

### C-3 · §3's INDU mandate is ANSWERED, and the answer is NO — with a correction to its premise

DEEP-INDU measured, and this desk re-measured: the mandate's premise (*"`RTX` is a new-🟢 clearing the
volume gate"*) is false — **`RTX` `vol_surge` 0.83, and 0 of 50 Industrials names clear 1.2.** The
mandate's *answer* is nonetheless clean: **defense primes are 11.3% of sector cap and correlate
+0.082 raw-60d with the other 40 names**, while machinery (+0.862 to `XLI`) and electricals (+0.836)
**are** the label. ⇒ **Industrials is a cyclical sector carrying an uncorrelated defense annex, not a
defense sector in disguise.**
★ And the run's own `S99` premise inverts with it: **`ETN`–`CMI` +0.811 and `ETN`–`CAT` +0.807 both
exceed `ETN`–`ANET` +0.722**; joint betas **`XLI` 1.396 (t 6.00) vs `XLK` 0.619 (t 5.12)**.
**`RTX`–`XLK` is −0.242** ⇒ **`RTX`, not `ETN`, is the book's Industrials diversifier.** `S99`'s
thresholds are frozen and unchanged; the construction defect is logged in the master scoring log.

### C-4 · A fourth instrument caveat, from the same DEEP — β-adjustment at SECTOR level hides per-name β

DEEP-COMM measured that `XLC`'s β-adjusted **−0.930** applies **one blended β of 0.68** to constituent
betas running **−0.39 (`TMUS`) to +1.43 (`META`)** (252d to 08-18). Re-done with **per-name** betas the
sector reads **+0.049 cap-weighted / −0.166 equal-weighted — flat both ways**, and the attribution is
stark: over 08-13→08-18, **`META` alone contributed −1.078pp of the −1.613pp (67%)** while the other
nine names (10.9% of weight) contributed **−0.0002pp**; `GOOGL`/`GOOG` β-adjusted excess vs `SPY` are
**+1.227 / +1.051 — positive**.
⚠ **This does NOT overturn MACRO's headline**, which compared **four separate ETFs each with its own
β** (`XLU` 0.15 · `XLRE` 0.27 · `XLP` −0.08 · `XLV` 0.27) rather than one blended β across names — the
2-2 split stands. **What it adds is the general caveat**: a sector-level β conceals per-name β
dispersion, so a β-adjusted *sector* print is a weaker object than a β-adjusted *ETF-vs-ETF* print.
Registered as dig **`D292`**.

### C-5 · Dig ledger opened by this run
`D287` revival/entry conditions must be instrument-covered before registration (`EMR`/`AME` are
permanently blocked) · `D288` G5 must read the same book `cycle_exposure` reads · `D289` `LITE`'s
short **stock** (12.2% float, crowded) contradicts the shortlist's "low-short" label built on short
**flow** · `D290` `flow_tag` must take the run-level axis set as `flow_score` does · `D291` the
flipper test must group by **issuer** before ranking · `D292` β-adjusted sector prints conceal
per-name β dispersion.

---

## 🚨🚨 C-6 · THE Δ THAT CARRIED BOTH OF TODAY'S PROMOTIONS IS MOSTLY WINDOW ROLL-OFF — one verdict is withdrawn

*(Found by DEEP-STPL; **re-measured independently here across all 11 sectors** before anything was
changed. §2 above is left exactly as written.)*

### The mechanism, stated plainly

`rs20` is a **rolling 20-session excess vs `SPY`**. Advancing `asof` from 08-14 to 08-18 does two
things at once: it **adds** the two new sessions at the front and it **drops two sessions off the
back**. `ΔRS20` is therefore the sum of two unrelated quantities —

**Δ RS20 = (excess EARNED over 08-14 → 08-18) + (minus the excess of the two sessions that ROLLED OFF)**

— and **nothing in this pipeline separates them.** A sector whose dropped sessions were bad gets a
free RS20 lift while losing ground to `SPY` in real time. Since `flow_score` eats `rs20`, the sweep's
`delta` inherits the contamination, and **`delta` is the number this stage's own rule requires a
verdict to be carried by.**

### The decomposition, all 11 sectors, equal-weighted, measured here — **[measured]**

| sector | n | **EW ΔRS20** | **earned** | **roll-off** | roll-off share |
|---|---|---|---|---|---|
| **Energy** | 16 | **+3.28** | **+3.75** | **−0.56** | ★ **−16.9%** |
| **Health Care** | 32 | **+2.96** | **+1.55** | +1.19 | **40.2%** |
| **Consumer Staples** | 19 | **+2.52** | **+0.57** | **+1.96** | 🚨 **77.7%** |
| Utilities | 15 | +1.41 | +0.41 | +0.95 | 67.1% |
| Financials | 47 | +1.32 | +0.11 | +1.08 | 81.8% |
| Communication Services | 12 | +1.04 | **−0.23** | +1.17 | **112.8%** |
| Real Estate | 12 | +0.94 | **−0.23** | +1.16 | **123.5%** |
| Materials | 12 | +0.75 | **−0.66** | +1.56 | **206.4%** |
| Industrials | 50 | +0.51 | **−0.48** | +0.95 | **186.5%** |
| Consumer Discretionary | 28 | +0.51 | **−0.67** | +1.21 | **236.4%** |
| Information Technology | 56 | **−5.23** | −1.97 | −3.11 | 59.4% |

*(identity `earned + roll-off = ΔRS20` holds; max residual 0.219pp, from names with incomplete history.)*

★★ **Six of eleven sectors show a POSITIVE ΔRS20 while their earned excess vs `SPY` is NEGATIVE** —
COMM, RE, MATR, INDU and DISC all *lost* ground to `SPY` across 08-17 and 08-18 and still printed an
improving Δ. **"The board improved" is, for a majority of the board, a statement about which two days
fell out of the window.**

### What it does to this file's two verdict changes

| verdict | Δ that carried it | earned | **status** |
|---|---|---|---|
| **STPL UW− → UW** | +0.325 (`wflow`) · EW ΔRS20 **+2.52** | **+0.57pp, 77.7% roll-off** | 🚨 **WITHDRAWN — reverted to UW−** |
| **HLTH N → N+** | +0.228 (`wflow`) · EW ΔRS20 **+2.96** | **+1.55pp, 40.2% roll-off** | ✅ **HELD at N+** |

**STPL — the promotion is withdrawn, and the reason is arithmetic, not judgement.** Its carrying
evidence was *"the board's largest two-session improvement."* Corrected for roll-off it is **+0.57pp
earned — 6th of 11, not 1st of 11.** Every other leg was already weak or against it: `eqflow` **−0.020**
(the median staples name is negative), β-adjusted excess vs `SPY` **−0.592**, `0 of 19` names clearing
`vol_surge` 1.2, and its new-🟢 leg (`WMT`) **already struck in C-2** as velocity-derived. **With the Δ
corrected, nothing carries the promotion.** ⇒ **Consumer Staples returns to UW−**, its verdict before
this run. ⚠ `S80` (tonight) and `S100` (08-21) are **unchanged and still settle** — the brackets were
frozen and a withdrawn verdict does not release the desk from scoring what it registered.

**HLTH — the promotion survives, and now on a narrower base than it was granted.** +1.55pp earned is
**2nd of 11 on the corrected measure**, and it is the only promotion candidate whose three independent
legs (`eqflow +0.163` **above** `wflow +0.114`; `wflow_ex_top1 +0.149` **higher** than the headline;
β-adjusted excess **+1.158 vs `SPY`**, 2nd-best on the board) do not use Δ at all. ⇒ **N+ stands.**

★ **And the sector this file HELD rather than promoted is the only one that earned its improvement
outright**: **Energy +3.75pp earned against a −0.56 roll-off *drag*** — the sole negative roll-off
share on the board. §2e declined to promote Energy to OW+ because the case rested on a diagnosed
volume-gate artifact. **The corrected numbers say Energy was the strongest earned improvement of the
eleven, and the desk under-rated it while over-rating Staples.** Energy is nonetheless **held at OW,
not raised**: this correction arrives after the stage's own analysis closed, and raising a verdict on
a number found at DEEP would be the same order-of-operations error being corrected here.

### Registered

**`D293`** — *`sector_flow` must publish `rs20_earned` and `rs20_rolloff` alongside `delta`, or the
desk must not carry a verdict on `delta` at all.* Measured cost this run: **one wrong promotion out of
two**, and six of eleven sectors printing an improving Δ while losing ground to `SPY`.
⚠ This is a **new defect class** for the run's log — not a stale window (`C1`) and not an axis drop
(`D225-KR`), but **a rolling-window endpoint effect inside a difference the desk treats as a return.**
It is invisible to every gate in `PREFLIGHT` because every number involved is real.

### DEEP_LOG amendment
The `DEEP_LOG 2026-08-19` line above records **TWO verdict deltas**. **Corrected: ONE** — `HLTH N→N+`
holds; **`STPL UW−→UW` is withdrawn to UW−** on the roll-off decomposition. The `IT` "(watch)" removal
also stands, and is **strengthened**: IT's Δ is negative on **both** components (**−1.97 earned,
−3.11 roll-off**), so it is the one sector whose Δ needed no correction to mean what it said.
