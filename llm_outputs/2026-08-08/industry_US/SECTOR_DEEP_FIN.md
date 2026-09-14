# SECTOR_DEEP_FIN — Financials · industry_US · 2026-08-08 · **ROTATING track → fresh interrogation**

> Structure carried by reference to `llm_outputs/2026-08-07/industry_US/SECTOR_DEEP_FIN.md` (§5 primary-filing NII language, §6 sub-node table) — reprinted only where this run's own pull changes or extends it. Benchmark **SPY, inline**, everywhere (**C1**, independently reproduced via `yfinance auto_adjust=False`, not inherited). **P4 — analysis only, zero sizing.** Flow: `SECTOR_FLOW_US.json`, **asof 2026-08-07 settled**. Rates/credit: `[FRED]` via `module_macro_us --json`, pulled live — `DGS2`/`DGS10`/`DFII10`/`BAMLH0A0HYM2` confirmed to stop at **2026-08-06** (**verified, not trusted**).

---

## §0 · The verdict on the velocity-tag decomposition — it holds, and it GENERALISES past the four greens

**Reproduced independently across all 47 Financials names** `[measured]`: the four greens are **PRU**
(`vol_surge` **1.36**, `velocity` None ⇒ **volume-lit**, OBV 매집, rs20 vs SPY +2.70) · **BRK-B**
(0.85, velocity 1.47) · **BAC** (0.73, 1.42) · **JPM** (0.65, 1.56) — exactly the split SWEEP named.
**Sector-wide mean `vol_surge` is 0.826 (median 0.79)** — **the typical Financials name is trading
below its own volume average, not just the greens.**

**Extending past the greens**: only **7 of 47 names (14.9%) show `vol_surge` > 1.0 at all** (PRU 1.36,
KKR 1.14, MET 1.15, ALL 1.05, XYZ 1.23, HBAN 1.08, IBKR 1.19), and applying the full accumulation gate
used elsewhere on this desk (`vol_surge` ≥ 1.2 **AND** OBV 매집 **AND** rs20 > 0 vs SPY),
🚨 **exactly ONE name in the entire 47-name sector clears it: PRU.** KKR and MET have accumulation OBV
and positive rs20 but sit just under the volume bar (1.14, 1.15); XYZ and IBKR have volume but are in
**OBV 분산 (distribution)**, not accumulation.
⇒ **the sector has volume-confirmed accumulation in ONE name out of 47.**

**A structural reason it concentrates where it does** `[measured]`: of the 47 names, only **8 carry a
populated `velocity` field at all — JPM, BAC, WFC, BRK-B, GS, MS, MA, V** — the desk's ~50-name
coverage whitelist (SWEEP §2, **D205**) sampled inside Financials. **These eight are exactly the
sector's most-covered mega-caps. Three of the eight are green, all velocity-lit on below-average
volume; the other 39 names (83% of the sector — every insurer but one, every regional, every asset
manager, every exchange/data name, every broker) can only ever earn a green through genuine volume,
and only one of them does.**

⇒ **the whitelist artifact is NOT spread evenly across the sector — it is concentrated in the same
eight names that also carry the most market-cap weight**, which is why `wflow` (+0.172, rank 2)
survives on the same names whose `eqflow` contribution is thin (+0.050) and whose breadth is
red-dominant (4🟢/7🔴). **Verdict: confirmed and extended — the sector's #2 flow rank is a
coverage-list artifact riding on market-cap weight, not a money-flow reading.**

---

## §1 · The four assignments

### 1a · ★★★ The NIM mechanism, tested against the banks' OWN forward-looking sensitivity tables

The 08-07 file established, from **backward-looking** Q2 MD&A language, that JPM/BAC/GS attribute
realised NII growth to balance-sheet volume rather than rates. **This run pulled the FORWARD-LOOKING
12-month rate-sensitivity tables from the same three 10-Qs plus WFC's** `[measured, fetched directly
from EDGAR this run — JPM 10-Q filed 08-06 p.83; BAC 10-Q filed 07-31 Table 41; WFC 10-Q filed 07-28
Table 22; all period 2026-06-30]`:

| Bank | **Short-end DOWN** (the bull-steepener analog) | **Long-end UP** (the bear-steepener analog) | Overall parallel-shift sign |
|---|---|---|---|
| **JPM** | **−$1.2bn** (−100bp short) | **+$1.1bn** (+100bp long) | asset-sensitive: +100bp parallel = +$1.8bn, −100bp = −$2.4bn |
| **BAC** | **−$1.8bn** (−100bp short) | **+$0.2bn** (+100bp long) | *"we continue to be asset sensitive… majority of that impact coming from the short end"* `[BAC 10-Q, quoted]` |
| **WFC** | **−$1.4bn** (−100bp short) | **+$0.4bn** (+100bp long) | asset-sensitive: +100bp = +$1.3bn, −100bp = −$1.9bn |

★★★ **All three banks independently QUANTIFY the exact asymmetry the mandate asks about.** A curve
move driven by the **front end falling** — which is the 2026-08-07 shape (**2y −4.35bp vs 10y
−1.44bp**) — sits on their **"short-end down" scenario line, which all three score NII-NEGATIVE**,
while a move driven by the **long end rising** scores NII-positive.

⇒ **This is now `[measured]`, not `[inferred]` from qualitative language, and it directly FALSIFIES
reading the 08-07 bull steepener as a NIM tailwind** — corroborating **S51**'s pre-committed refusal
and **P35**'s Direction A **with three independent first-party numbers rather than one qualitative
synthesis**. **A5 satisfied: the inherited transmission claim was tested, not carried as `[unverified]`.**

⚠ **C2, the other half**: all three remain net **asset-sensitive to rate LEVEL** (positive to a
parallel hike, negative to a parallel cut). **"It's volume now, not rates" describes what drove the
REALISED Q2 print, not what the banks say they are EXPOSED to going forward.** Both are true at once
and they are **not the same claim.**
**W4**: the volume leg those tables reference is named — **JPM's wholesale loan and Card Services
revolving balances · BAC's Global Markets counterparties and deposit/loan growth · WFC's commercial-
and-industrial and auto borrowers** — real counterparties, not an abstraction.

### 1b · Grading S65 / S66 / S70 BEFORE they settle (L3)

**`S65`** (median rs20 vs SPY of {JPM, BAC, WFC, BRK-B}, settles **08-11**) — **reproduced
independently at +3.352**, matching the registered read exactly. HANDOVER's reachability check calls
it **"genuinely two-sided"** (3.01pp to A / 3.46pp to B, roughly symmetric). ⚠ **Unlike S57** (0.59pp
from a branch that fires inside its own D6 implied move), **this bracket is NOT degenerate against
Lens 2's option-implied test**: JPM's ±2.1% D6 is a **single-name, absolute-price** threshold, whereas
S65 needs **the median of four names' RELATIVE excess** to move ~3pp in two remaining sessions
(08-10, 08-11) — a materially harder ask than "inside what's priced."
⇒ **Worth its slot — with one live contamination risk (§1d).**

**`S66`** (ΔDGS2 + ΔHY OAS jointly from the 08-05 anchor) — **confirmed un-scoreable** this run
(`DGS2` and `BAMLH0A0HYM2` both stop 08-06, **verified live**). Its own registration rationale for
spinning off S70 was that *one lagging leg can swallow the whole question*; on the evidence here (the
2y already moved −4.35bp per `[news]`, tracking the direction FRED will likely confirm), **S66's
information content once both legs print will mostly be INHERITED from S70's credit leg** — a fire on
S66 will largely **confirm** what S70 already settled. ⇒ **marginal value, given S70 exists.**

**`S70`** (HY OAS alone, first `[FRED]` close ≥ 08-07, expect **08-10**) — the registration itself
discloses that **branch A requires no widening at all** (2.71% is the current print), i.e.
**A is the modal, expected outcome and a fire on A mostly confirms the relief narrative the equity and
curve tape already show.** ★ **Branch B (≥ 2.96%, a ~2.3σ five-session move) is where the real
information sits** — it would be the **first primary evidence that the payroll shock was read as a
growth scare rather than rate relief**, and it reopens every cyclical UW on the board.
⇒ **Asymmetric value: worth its slot specifically for what B would say, not for what A would say.**

### 1c · ★★ WFC — credit quality is IMPROVING; the hypothesis was wrong and the real story is margin

`[measured, WFC 10-Q filed 2026-07-28, period 2026-06-30, fetched directly]`:
- **Net charge-offs FELL to $883mm from $997mm y/y (−11%)**
- **Commercial NCOs fell to 10bp** of average commercial loans **from 18bp**
- **Consumer NCOs fell to 74bp from 81bp**
- **Non-performing assets fell $559mm**, *"driven by lower commercial real estate nonaccrual loans"*
- **The ACL coverage ratio itself FELL (1.40% from 1.45%)**, *"reflecting a decrease in the allowance
  for our commercial real estate portfolio driven by **improved credit performance**"*
- The half-year provision rose ($2.1bn vs $1.9bn) but the bank's own text attributes it to **higher
  loan balances** in C&I and auto, *"partially offset by a lower allowance for commercial real
  estate"* ⇒ **growth-driven, not quality-driven**
- **FINRA short-vol z on WFC is −1.57** (5v5 trend −9.9pp) `[measured, us_flow.py 08-07]` ⇒ short
  pressure is **collapsing** — the opposite signature of a market pricing credit fear

**What IS real**: **NIM compressed to 2.43% from 2.68% y/y** (and 2.47% Q1-26 → 2.43% Q2-26
sequentially), while **average loans grew +12% y/y and NII grew only +5%** — a materially worse
volume-to-income translation than JPM's (assets +11.5%, NII +10%, roughly matched).
**L2**: WFC's forward P/E is **11.04**, below JPM's 14.30 and near BAC's 11.93, against a **ROTCE that
is RISING (17.7% Q2-26 vs 15.2% Q2-25)** — **the multiple is not pricing a de-rate.**

⇒ **Answer: WFC is NOT the credit-quality canary the mandate hypothesised — its own primaries show
credit improving.** Its rs20 (−2.32) sits close to the **true regional-bank sub-node mean**
(USB/PNC/TFC/FITB/HBAN/STT/BNY: mean rs20 ≈ **−1.23 vs SPY**) and far from its GICS money-centre peers
(JPM/BAC/BRK-B: +3.3 to +3.8), and **KRE's exc5 is −3.31.** ⇒ **WFC trades with the regional complex
it is not classified alongside, on a margin-compression fact that is real but not credit-driven — a
LABELLING mismatch, not a hidden credit story.**

### 1d · ★★★ Ex-BRK-B recomputed, and the Berkshire contamination is LIVE, not hypothetical

`[own calc, reproducing the printed row before adjusting: eqflow 0.0497 ≈ printed 0.05; wflow 0.1722 =
printed 0.172 — C1]`. **Ex-BRK-B (46 names)**: **eqflow 0.0497 → 0.039 (−22%)** · **wflow 0.1722 →
0.1124 (−35%)** · breadth **4🟢/7🔴 of 47 → 3🟢/7🔴 of 46**. The **wflow-over-eqflow premium** (the D9
mega-cap distortion) shrinks from **+0.1225 to +0.0734 — a 40% reduction**, reproducing the prior
run's *"roughly halves"* finding on today's numbers, independently, on the opposite sign convention.
**BRK-B is 13.94% of the sector's market cap (reproduced exactly)** and is one of only three green
tags carrying the sector's #2 flow rank.

🚨🚨 `[measured, `fts search`, 08-08]`: **Berkshire reported Q2 2026 net earnings of $25.667bn vs
$12.370bn a year ago** (operating earnings **$12.983bn vs $11.160bn, +16.3%**), released **TODAY,
2026-08-08 — a day earlier than the 08-09 date the 08-07 file expected, and one day AFTER the 08-07
close this DEEP's flow and rs20 numbers are computed from.**
⇒ **BRK-B's current flow tag, `vol_surge` and rs20 (+3.26) ALL PREDATE this print and cannot reflect
it.** With markets closed until 08-10, this is a **dated, unpriced catalyst sitting directly inside
S65's 08-11 settlement window**, on the one leg that is **13.9% of sector weight** and one of only
three velocity-lit greens.
⚠ **Ex-WFC and ex-BRK-B counterfactuals of S65's median are both +3.44** (vs +3.352 actual) ⇒
**BRK-B is not currently swinging the branch.** But **a large earnings-driven Monday move could push
the median toward branch B for a reason ORTHOGONAL to the NIM/curve mechanism S65 nominally tests**,
which would make a B-fire look like tilt vindication when it is single-name earnings noise.
⇒ **Flagged as a live read-contamination risk for the 08-11 settle, not yet realised.**

---

## §2 · The sector's node map and its binding constraint

The 47-name sector is **not one object; it is at least three**:
1. **An 8-name velocity-whitelisted core** (JPM, BAC, WFC, BRK-B, GS, MS, MA, V) that can produce a 🟢
   **on news coverage alone at below-average volume**, and which carries nearly all the sector's
   market-cap weight.
2. **39 non-whitelisted names** (every insurer but PRU, every regional, every asset manager, every
   exchange/data name, every broker) that **can only earn a green through a genuine volume surge**, of
   which **exactly one (PRU) has.**
3. **BRK-B specifically** — a $1tn+ holding company inside bucket (1) whose flow and rs20 numbers are
   **structurally lagged relative to its own earnings calendar**, and whose weight alone moves the
   sector aggregate **22–40%** (§1d).

**The binding constraint**: the instrument's **coverage-whitelist distortion (§0)** and the
**market-cap concentration distortion (D9)** are **not independent — they are the SAME EIGHT NAMES**,
so **any un-decomposed Financials aggregate compounds both defects at once.** A sub-node read
(money-centres vs regionals vs insurers vs asset managers) remains the correct unit;
**"Financials" as a single flow number is not.**

---

## §3 · Track-KPIs · anti-signals · dated observables

| KPI | State (this run) | Anti-signal, dated | Date |
|---|---|---|---|
| Sector volume-confirmed accumulation | **1 of 47 (PRU)** clears `vol_surge`≥1.2 + OBV 매집 + rs20>0 | a second name (KKR 1.14 / MET 1.15, both just under the bar) crossing 1.2 with OBV/rs20 intact | rolling |
| Velocity-whitelist breadth inside FIN | **8/47 populated; 3 of 8 green, all `vol_surge` < 1.0** | a whitelisted name going green on `vol_surge` ≥ 1.2 (a real volume event, not coverage) | rolling |
| **S65** | **+3.352**, branch C, genuinely two-sided (3.01 / 3.46pp) | 🚨 **BRK-B's Monday earnings reaction pushing the median past +3.46 for reasons unrelated to the NIM/curve mechanism ⇒ read as CONTAMINATION, not vindication**, if rs20 moves on BRK-B alone | **08-10 / 08-11** |
| **S66** | un-scoreable, `[FRED]` stops 08-06 (verified live) | first FRED print ≥ 08-07; expected to mostly track S70 | 08-10 |
| **S70** | **2.71% (08-06)** — branch A requires **no** widening | **HY OAS ≥ 2.96% (branch B) — the only branch with real information content** | 08-10 |
| WFC NIM | **2.68% → 2.47% → 2.43%** (Q2-25 → Q1-26 → Q2-26) | a sequential NIM print that stops falling would separate WFC from a pure margin story | Q3 (~10-13/14) |
| WFC credit | NCOs and NPAs both **improving**; short-vol z −1.57 (covering) | a reversal in commercial or consumer NCO trend, or short-vol z crossing back above its 20d base | rolling |
| Ex-BRK-B wflow premium | **+0.1225 → +0.0734 (−40%)** on removing one name | a further single-name removal (e.g. JPM) producing a comparable swing would generalise the concentration finding past BRK-B | on demand |
| Bank NII sensitivity (3 banks quantified) | **all three: short-end-down NII-NEGATIVE ($1.2–1.8bn / 100bp); long-end-up NII-POSITIVE ($0.2–1.1bn / 100bp)** | Q3 10-Qs re-quantifying these tables against an actually-realised bull-steepener quarter | ~10-13/14 |

---

## §4 · Carried unchanged, by reference

`llm_outputs/2026-08-07/industry_US/SECTOR_DEEP_FIN.md` **§6** (sub-node dispersion: insurers
+0.356/+2.77 · asset managers +0.472/+6.98 · money-centres +0.178/+0.05 · regionals +0.030/−0.59 ·
exchanges −0.097/+0.12 · brokers −0.211/−3.22, mean flow / mean rs20, **not re-pulled this run**) and
its finding that *"Financials" is not a usable single unit* (5.5× the sector's own eqflow move in
spread) — **reconfirmed structurally by §2's whitelist/mcap overlap finding, not superseded.**
**GS's five-run flow/fundamental split** (§4 of the 08-07 file) is **not re-tested** — outside the four
assigned questions, handed forward unchanged.

**No position sizing and no buy/sell language appears anywhere in this file (P4).**
