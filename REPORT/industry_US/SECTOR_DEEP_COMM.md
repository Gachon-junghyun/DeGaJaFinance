# SECTOR_DEEP_COMM — Communication Services · industry_US · 2026-09-01 (Tue) · Stage 8 / L1·DEEP
### ROTATING TRACK (R2) — **FULL FRESH MAP** · 1-run recency violation, declared by ROTATION

> Flow: `SECTOR_FLOW_US_REPAIRED.json`, 3-axis `nonews`, **asof 2026-08-31**. Benchmark `SPY` inline (`C1`).
> ⚠ This slot exists because repeating `D297` ("the bucket is un-measurable, n=12") would make
> Communication Services **permanently unreachable**. The mandate was narrowed to a question the data
> can answer.

## 0 · Mandate from ROTATION — one question
> *`wflow` **−0.547** against `eqflow` **−0.033** is the widest cap-vs-equal split on the board.
> **Is that `GOOGL` alone, and what is underneath it?** Answer with the other 11 names, not the bucket.*

---

## ★ 1 · The answer, and it is an INSTRUMENT DEFECT, not a sector fact

**`M1206` [measured] — Alphabet is in this bucket TWICE, and the desk's one-name guard can only see
one of the two share classes.**

| ticker | name | share of the sector's scored cap |
|---|---|---:|
| `GOOGL` | Alphabet Inc. **(Class A)** | **38.3%** ($4,491B) |
| `GOOG` | Alphabet Inc. **(Class C)** | **38.3%** ($4,484B) |
| | **Alphabet, one company** | ★ **76.6%** of a 12-name bucket |
| `META` | Meta Platforms | 12.5% |
| all nine others combined | | **10.9%** |

Recomputing the sector with the engine's own weighting:

| cut | n | `wflow` | `eqflow` |
|---|---:|---:|---:|
| all | 12 | **−0.547** | −0.033 |
| ex-`GOOGL` (what `top1_flips_sign` actually tests) | 11 | **−0.404** | +0.035 |
| ★ **ex-Alphabet (BOTH classes)** | 10 | ★ **+0.144** | **+0.112** |
| ex-Alphabet and `META` | 9 | **+0.162** | +0.111 |

★★★ **The sector's sign FLIPS — from −0.547 to +0.144 — and `SECTOR_FLOW_US.json` reports
`top1_flips_sign: False`.** The guard removes the **single largest row**, `GOOGL`; the second-largest
row is the **same company's other share class**, so 38.3% of Alphabet stays in the "ex-top1" number
and the flip is invisible. ⇒ **`D459`**.

**Consequences, stated plainly:**
1. **The mandate's answer is: yes, it is Alphabet alone — and by more than the instrument can show.**
   `GOOGL` **−0.778 🔴분산** (OBV −0.237, `rs20` **−10.4 vs `SPY`**, Δ −0.46) and `GOOG` **−0.739 🔴**
   (OBV −0.326, Δ −0.23) are **two of the sector's three reds**. Underneath them the bucket is
   **positive on both axes**.
2. **This is not only a COMM problem.** Any dual-class or dual-listed issuer inside `us_top300`
   defeats the same guard. ⇒ the fix is a **guard on the issuer, not the row** — filed as `D459`.
3. ⚠ **`D297` was right that n=12 is small and wrong about why the bucket is unreadable.** It is not
   the sample size; it is that **one issuer occupies three quarters of it under two tickers.**
4. ⚠ **ROTATION's `COMM OW−` verdict this run stands as issued** — this measurement arrived at DEEP,
   after the verdict, and **the earlier sentence is not edited away** (`D48`). **The correction is
   recorded here and handed to the next run's ROTATION**, which now has a number the flip guard could
   not give it.

---

## 2 · What is underneath — the nine names the headline buries

| chain node | names (flow · OBV · `rs20`/`rs60` vs `SPY` · Δ) | read |
|---|---|---|
| **Content / studios** | **`WBD` +0.539** OBV **+0.444** · +8.1/+4.4 · **`DIS` +0.500** OBV **+0.476** · +8.4/+6.9 · `NFLX` +0.315 · +9.3/−1.9 · `LYV` −0.307 | ★ **`WBD` and `DIS` carry the two highest OBV readings in the sector** — higher than anything in the Alphabet/Meta layer |
| **Distribution / cable** | `CMCSA` +0.390 OBV +0.237 · +7.1/**+12.8** | positive on both horizons |
| **Telecom** | `T` +0.350 OBV +0.269 · +8.5/**+12.4** · `VZ` +0.102 · +4.4/+10.2 · **`TMUS` −0.487** OBV −0.190 | ⚠ **`T` is the desk's own un-owned position** — carried in `C23`/`M1130` as ~13.6% of real invested capital with **no thesis attached**. It is quietly the **4th-best flow row in this sector** |
| **Platforms** | `META` +0.128 OBV +0.158 · **−4.3/−10.1** · **`GOOGL` −0.778 🔴** · **`GOOG` −0.739 🔴** | the entire negative |
| **Games** | **`TTWO` −0.406 🔴** OBV −0.308 · −11.6/+0.1 · **`vol_surge` 1.47** | distribution **on rising volume** — the worst combination in the bucket |

**Dispersion (lens B5)**: `flow_score` spans **`WBD` +0.539 to `GOOGL` −0.778 = 1.317** against a
sector `eqflow` of −0.033. ⇒ **the label is the wrong unit**, for the third sector in a row.

## 3 · The customer / demand side, named (rule A6)
- **`GOOGL`'s** demand is not in question — quarterly revenue **96.43 → 102.35 → 113.83 → 109.90 →
  119.80 $B**, QoQ **+6.1% → +11.2% → −3.5% → +9.0%**, latest **+24.23% YoY** (`C2`: both halves; the
  one negative QoQ is Q1 seasonality, not a trend). ⇒ **the −0.778 flow is a POSITIONING fact, not a
  fundamental one**, and this file does not claim otherwise.
- **What is dated and adverse for the platform layer**: *"EU places ChatGPT, Reddit and Roblox under
  strictest digital safety rules"* [8 outlets, 08-31] and *"Sony, Warner Music sue Anthropic, saying
  it pirated songs to train its AI"* [6 outlets] — both are **AI-content regulation/litigation**
  landing on the layer that owns the sector's cap weight. ⚠ Neither names `GOOGL` directly; carried as
  **environment, not evidence**.
- **`T`/`VZ`/`CMCSA`'s** demand is subscriber ARPU under a **+14bp front-end repricing** (`P121`) —
  a duration-proxy headwind that the tape has **not** delivered (`T` `rs60` **+12.4 vs `SPY`**).
  ⇒ recorded as a divergence between the macro frame and this node.

## 4 · Frame-transfer question — answered
> *Does the contracted-revenue / take-or-pay frame apply here?*

**Checked. It applies to exactly one node, and the desk does not own it deliberately.**
**Telecom (`T`, `VZ`, `TMUS`)** runs on multi-year subscriber contracts and spectrum-backed
regulated-adjacent cash flows — the closest analogue in this sector to `KMI`'s RPO. **Content and
platforms have no such structure**: advertising is spot-priced and re-prices with the cycle, which is
why lens **B2**'s peaking-denominator mechanism applies to `META`/`GOOGL` **without an escape hatch**.
★ **Transferable point**: the desk holds `T` **with no thesis** (`C23`), and `T` is the one name in
this sector where the frame the desk trusts elsewhere actually fits. **The un-owned position is in the
structurally best-protected node, by accident.**

## 5 · Positioning and structure
`[FINRA 08-31]` was **not** pulled for this sector's names this run — ⚠ **stated as a gap**, not
filled by inference. The `us_flow` call covered the book and the DEEP leaders in other sectors.
⚠ `module_chart` was **not** run for COMM names — the render is restored (G7) but the budget went to
`SLB`. **Named as a gap.**
`TTWO`'s `vol_surge` **1.47** against OBV **−0.308** is the one structural tell available from the
sweep alone: **volume arriving into distribution.**

## 6 · Track KPIs and anti-signals
| KPI | now | what changes the verdict |
|---|---|---|
| **`wflow` ex-Alphabet(both classes)** | **+0.144** | the number the next ROTATION should read instead of −0.547 |
| `GOOGL` OBV | **−0.237 분산** | a turn to 매집 ⇒ the sector's headline repairs without anything underneath changing |
| `WBD` / `DIS` OBV | **+0.444 / +0.476** | a turn to 분산 ⇒ the positive underlayer was one week |
| `T` flow | **+0.350**, `rs60` **+12.4 vs `SPY`** | the un-owned position's own KPI, finally attached to something |
| `TTWO` `vol_surge` vs OBV | **1.47 / −0.308** | convergence either way |

**Anti-signals that would kill this file's reading**: (i) a GICS reclassification moving Alphabet's
classes; (ii) `WBD`/`DIS` OBV turning 분산 while `GOOGL` stays 🔴 — that would make the bucket
uniformly negative and the ex-Alphabet number meaningless; (iii) evidence that the sweep's universe
file de-duplicates share classes elsewhere (which would make `M1206` a COMM-specific artifact rather
than a general defect).

## 7 · Handed forward
- **To BET**: **no COMM name is handed as CONFIRMED-EARLY.** `WBD` and `DIS` are logged as the
  bucket's strongest accumulation but neither is 🟢 and neither cleared the shortlist.
- **To the next ROTATION**: ★ **read Communication Services at `wflow` +0.144 (ex-Alphabet, both
  classes), not −0.547.** The sector has been carried on a number that a dual-share-class artifact
  makes wrong by **0.691**.
- **To the desk (`D459`)**: *the one-name concentration guard is applied per ISSUER, not per row;
  dual-class and dual-listed tickers are collapsed before `top1_w` and `wflow_ex_top1` are computed.*
  ⚠ **Not fixed here** — code changes are a human-approval item (preflight rule 1). **Measured,
  recorded, handed over.**
- **To `C23`**: `T` — the position no instrument owns — is this sector's 4th-best flow row and sits in
  its only contractually-protected node. **The gap now has a candidate thesis; assigning one is a
  human call.**
