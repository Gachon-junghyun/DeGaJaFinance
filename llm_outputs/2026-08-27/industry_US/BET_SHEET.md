# BET_SHEET — industry_US · 2026-08-27 (Stage 9 / L1·BET)

> **ONE file, per-sector sections §A–§E.** Downstream desks glob this exact filename.
> **Analytical output only. No buy/sell recommendation. No position sizing (P4).**
> Price frame = **equal-weight `us_top300` constituents, excess vs `SPY` (named inline), settled closes
> through 2026-08-26.** Flow = this run's sweep, **asof 2026-08-27, a pre-market stub bar** (median
> volume 4.65% of the prior session) ⇒ **`vol_surge` and the 🟢/🔴 tag carry no claim anywhere in this
> file.** Upstream artifacts are **cited, not reprinted**.

---

## §0 · Gates this sheet ran before writing anything

**1. Company scoreboard — consulted, and it covers nothing here.**
`REPORT/COMPANY_SCOREBOARD.md` is dated **2026-08-21 (`company_batch` run 1)** and holds **5 rows, all
KR** (`036460` PASS 92.5 · `011200` PASS 79.5 · `316140` HOLD 76.2 · `028050` HOLD 64.7 · `000660`
PASS 58.8). ⇒ **zero US candidates carry a row**, so the confirmation gate has nothing to confirm and
**every name below is a RE-DIG by construction, not by choice.** The failing test is **coverage**, not
age. ⚠ Its own two reading rules are honoured here: **the score measures research quality, not
expected return**, and **the sheet's #1 row is a `PASS`.** Nothing on it is treated as a candidate.
⚠ `module_report_tags show` was cross-read at HANDOVER — **no US name in this sheet has a company-level
report row**, so "no scoreboard row" is genuine absence of coverage, not a batch skip.

**2. 🚨 The screener's own instrument was checked before its output was used — and it FAILED.** See §0-a.

**3. Exposure state (carried from HANDOVER §4)**: rule state **`정상`**, target **95%**, accrued
**85.4%**, band gap **−9.6pp**, cumulative n=15 total **−13.48pp = cash −6.21 + selection −7.27**.
⇒ **The state is `정상`, not `복귀`**, so this sheet carries **no obligation to supply enough candidates
to reach a target** — the EXIT rule's unfillable-target trap does not arise. Stated, not assumed.
⚠ `exposure_rule state` could not read the account (`투자비중미상`); 85.4% is **stated from the accrued
ledger row, not substituted** (P5).

### §0-a · 🚨 `D385` — the screener's RSI is a different formula from the thresholds it is gated on

`us_setup_screener` buckets on **RSI < 45 (leader pullback) · 30–52 (de-rate) · < 28 (washout)** —
the **Wilder convention**. But the repo's single RSI source (`module_chart/_indicators.py:46`,
`rsi_series`) computes a **simple rolling mean** of gains and losses — **Cutler's RSI**, not Wilder's
smoothed average. **Measured this run on all 18 screener candidates:**

| bucket | ticker | repo RSI | Wilder RSI(14) | gap | still in bucket under Wilder? |
|---|---|---|---|---|---|
| A | `ITW` | 20.3 | 44.8 | **−24.5** | YES (barely) |
| A | `PCAR` | 31.3 | 43.9 | −12.7 | YES |
| A | **`RTX`** | 31.4 | **46.9** | −15.4 | 🚨 **NO** |
| A | `SYY` | 39.9 | 47.5 | −7.5 | 🚨 **NO** |
| A | `CL` | 41.8 | 48.0 | −6.2 | 🚨 **NO** |
| A | `ROST` | 28.4 | 43.0 | −14.7 | YES |
| A | **`AMZN`** | 30.4 | **48.0** | −17.6 | 🚨 **NO** |
| B | `ISRG` | 43.9 | 43.2 | +0.7 | YES |
| B | `MNST` | *(nan in raw formula)* | 51.3 | — | YES |
| B | `WMT` | 31.6 | 32.0 | −0.3 | YES |
| B | `NKE` | 35.3 | 37.4 | −2.1 | YES |
| B | `AZO` | 30.0 | 42.3 | −12.3 | YES |
| C | `FER` | 17.3 | 27.7 | −10.4 | YES |
| C | `HON` | 22.3 | 38.5 | −16.2 | 🚨 **NO** |
| C | `WM` | 24.3 | 34.3 | −10.0 | 🚨 **NO** |
| C | `TJX` | **4.8** | 20.8 | **−16.0** | YES |
| C | `CCL` | 23.3 | 37.6 | −14.3 | 🚨 **NO** |
| C | `HD` | 26.0 | 41.6 | −15.7 | 🚨 **NO** |

**Result: 10 of 18 survive; 8 of 18 (44%) would not be in their bucket under the formula the
thresholds are calibrated for.** Mean gap ≈ **−12.4 points**, max **−24.5 (`ITW`)**.
⚠ **This is not the stub bar.** Measured separately: dropping the 08-27 pre-market bar moves RSI by
only **0.1–7.0 points** (`TJX` 20.7 → 22.1, `ITW` 44.7 → 51.6, `RTX` 46.8 → 48.4). **The formula gap
is ~2× the stub effect and is systematic in one direction.**
⚠ **`TJX` reading 4.8** is the tell — a Wilder RSI essentially cannot print below ~10 on a liquid
large-cap, and 4.8 should have been read as an instrument reading, not a market reading.
🚫 **Consequence enforced in this sheet: no screener bucket membership is used as evidence for any
name.** Where a screener name appears below it appears **on its own price/flow numbers**, and the eight
that fail the Wilder check are **explicitly marked ✗bucket-fails-Wilder.** ⇒ **`D385`, `M993`.**
✅ Also stated: **Cutler's RSI is not "wrong"** — it is a legitimate variant. **The defect is the
mismatch between the formula and the threshold convention**, and it is a one-line fix (either switch
the source to Wilder, or recalibrate the three thresholds). **Human-approval item; not fixed here.**

---

## §A-CROSS · The one number that runs through every section

**Five of the six candidate leaders this run surfaced trade AT OR THROUGH their mean analyst target:**

| name | sector | upside to mean target | forward P/E | PEG | Hold+Sell / total ratings |
|---|---|---|---|---|---|
| `MPC` (held) | ENRG | **−10.8%** | 11.30 | 1.76 | 9 of 19 |
| `ABNB` | DISC | **−5.8%** | 30.58 | 2.03 | 18 of 42 |
| `TGT` | STPL | **−3.2%** | 17.58 | 2.57 | **22 of 34** |
| `MRK` | HLTH | **−1.4%** | 15.80 | 10.73 | 8 of 28 |
| `DASH` | DISC | **+9.3%** | 28.34 | **5.22** | 10 of 44 |
| *(reference)* `NVDA` (held) | IT | **+45.9%** | 15.18 | 0.59 | 3 of 61 |

⇒ 🚨 **Every momentum leader on this board is at or through consensus, and the only name with real
consensus upside is the epicenter that just guided its gross margin down 100bp.** That is the
cross-cutting fact of this sheet, and it is why **§E's refutations are stronger than §B's theses
almost everywhere.** ⇒ **`M994`.**
⚠ **Rule stated**: analyst targets are a **consensus artifact**, not a measurement of value, and this
sheet uses them only as **a crowding read** — where the sell side has already moved, the incremental
buyer is thinner. No target is used as a price objective (P4).

---

## §ENRG · Energy — `OW`, and the OW is a node call

**Candidates**: `MPC` (held), `PSX` (held), `VLO` (rejection ledger, `H.밸류소진`, recheck 09-04).
**Screener contributed ZERO names in Energy** — buckets A/B/C all empty on 16 names. ⚠ **Diagnosed, not
cited as evidence**: with the sector's three best names at `RS60` +31 to +37, none can be near a 52-week
low or a de-rate, so **an empty screener here is the screener working, not an absence of setups.**

**§A numbers** — `MPC`, cited from `SECTOR_DEEP_ENRG §3` rather than reprinted: forward P/E **11.30**,
current-year EPS **+81.9% / 90d**, **next-year 32.20 vs current-year 50.23 = −35.9%**, mean target
**10.8% BELOW price**, ratings **4 SB · 6 B · 8 H · 1 S**.
🚨 **Arithmetic verified**: 32.20 ÷ 50.23 − 1 = **−35.90%**. 90-day current-year move
27.61 → 50.23 = **+81.93%**. Both recomputed here, not carried.

**§B thesis + freshness** — refining margin is the binding constraint of the sector; the node carries
`exc60` **+36.43** vs the sector's +10.10 and **zero negatives on 5 days**.
**Freshness: `UNMEASURED (G1 FAIL)`.**

**§C flow / positioning** — `MPC` OBV **+0.289 매집**, `RS20` +12.3, `RS60` +37.3, flow +0.550;
`PSX` +0.151 매집, +11.7 / +31.8; `VLO` +0.148 매집, +8.8 / +34.5. `XOM` (sector `top1`, **30.5%**,
**a G3 flipper**) is **flow −0.621 🔴분산, OBV −0.255 분산** — so the sector's cap-weighted number is
unusable by rule and the node reading above is equal-weight throughout.

**§D competition / peers** — the three refiners are peers of each other and **sit in one valuation
state**; `VLO`'s 11.16× (carried from 08-26) against `MPC`'s 11.30× is a 1.2% spread. **There is no
dispersion inside this node to arbitrage** — it is one bet in three tickers, which is also what
`risk_units` measures (`{MPC, PSX}` merge into one unit at **250d, 500d and 750d** — the only grouping
stable across all three windows).

**§E refutation + dated catalyst** — 🚨 **The strongest refutation on this sheet, and it is arithmetic
rather than narrative**: consensus has raised `MPC`'s current-year EPS **82% in 90 days** and
**simultaneously models next year 36% lower**, while the **mean target sits below the price**. That is
`L2`'s peak-margin trap with the sell side already on the other side.
⚠ **The contract-terms check the rule requires was RUN and returned nothing**: `module_disclosure_us MPC
--days 60` → 11 filings, and the `수주/계약`, `Item 2.02`, `Item 7.01` and `증자/채무` sections are
**all empty**. ⇒ **contracted share `unknown` (C3)**, and **this sheet does NOT assert the margin must
mean-revert** — only that expectations already do.
**Dated catalysts**: **`P96` and `P83` settle at tonight's 08-27 close** — 🚨 **both on a bar containing
an RBOB contract roll that moves them in opposite directions** (`SECTOR_DEEP_ENRG §1b`); **`P103`
settles 09-02** as the roll-free re-read; `VLO`'s ledger recheck **09-04**.

---

## §HLTH · Health Care — `OW`, narrowed to "ex-payers"

**Candidates**: `MRK`, `JNJ` (both from `US_LIVE_SHORTLIST.json`), `ISRG` (screener B, ✅ survives Wilder).

**§A numbers — `MRK`**: trailing P/E **123.58** (charge-distorted), forward **15.80**, **PEG 10.73**,
P/S 5.59, mean target **1.4% BELOW price**, ratings 5 SB · 15 B · 8 H.
🚨 **Revisions**: current quarter **−4.2% / 90d** (2.31 → 2.21), next quarter +5.3%, current year
+0.4%, next year **+0.1%**. ⇒ **`MRK` is the sector's ONLY 🟢가속 in the sweep and its near-quarter
estimate is being cut.** The flow axis and the denominator axis point opposite ways on the same name.
**Stated as a disagreement; no verdict issued.**
**`JNJ`**: flow +0.162 (🟢가속), OBV **+0.335 매집**, `RS20` +0.7, `RS60` +18.6, FINRA `z −1.81` —
**the cleanest low-short reading in the shortlist.** 🚫 No valuation pulled — **blank stated as blank.**
**`ISRG`**: `exc60` **−11.14**, `exc20` −0.12, OBV +0.182 매집, RSI 43.9 (repo) / **43.2 (Wilder)** —
**the one screener name whose two RSI formulas agree**, and therefore the only bucket membership in
this sheet that is instrument-clean.

**§B thesis + freshness** — the OW rests on `eqflow` rank 1, **the board's only positive breadth
(0.06)**, red-rate **9.4% = best of 11**, and **6 of 8 nodes positive on `exc60` between +9.8 and
+21.7**. **Freshness: `UNMEASURED (G1 FAIL)`.**

**§C flow / positioning** — shortlist verdicts: `MRK` **△정상숏** (FINRA `z +1.16`), `JNJ`
**✅저숏/숏커버** (`z −1.81`). ⚠ **`C18` applies**: FINRA short-**volume** z and `module_flow` short-
**interest** are different objects; **neither overrules the other and no `⚡crowded-short` stamp is
issued.**

**§D competition / peers** — the leadership is **cross-node, not a peer group**: `REGN` +34.66 (biotech),
`AMGN` +32.80 (biotech), `MRK` +31.94 (pharma), `BDX` +29.89 (equipment) on `exc60`. **Four names, three
GICS boxes** ⇒ there is no single competitive set to rank.

**§E refutation + dated catalyst** — 🚨 **The payer node is the binding constraint and this sheet holds
nothing in it**: `Health Care Services` `exc20` **−13.13** (`CVS` −15.97, `CI` −10.28), `UNH` `exc20`
**−9.67**. Every candidate above is downstream of a reimbursing node that is being repriced.
**Second refutation**: `MRK`'s **PEG 10.73** and a mean target below the price.
**Dated catalysts**: none registered on any HLTH name this run. 🚫 **Stated as a gap** — the sector has
a continuous DEEP slot and **no bracket**, which means it cannot be scored.

---

## §INDU · Industrials — `UW−`, and the sheet's job here is to say what is NOT bought

**Candidates**: `RTX` (held) · screener A `ITW`, `PCAR` · screener C `FER`, `HON`, `WM`.
**Bucket-integrity marks (§0-a)**: `ITW` ✅ · `PCAR` ✅ · `FER` ✅ · **`RTX` ✗** · **`HON` ✗** · **`WM` ✗**.

**§A numbers** — 🚫 **No valuation was pulled for any INDU name this run. Blanks are stated as blanks**,
not filled with a guess. ⇒ **no cheapness claim appears in this section**, and the margin-percentile +
revision-trend rule therefore does not fire.

**§B thesis + freshness** — the `UW−` is a statement about **capital goods and construction**, not about
the sector: block F (Construction & Engineering) is the **worst node on `exc5` (−6.16), `exc60` (−10.50)
and `eqflow` (−0.681) simultaneously**, while block E (services) carries `exc60` **+13.02**.
**Freshness: `UNMEASURED (G1 FAIL)`.**

**§C flow / positioning** — `RTX` (held): flow −0.251, OBV **+0.052 중립**, `RS20` −4.9, `RS60` +20.2,
`exc5` **−3.41 inside a 10-of-10 negative aerospace week**. ⚠ `B3` binds: **ten names moving together on
one week is n≈1, not n=10.**
`PCAR` **−0.932 🔴분산** and `CMI` **−0.811 🔴분산** are the two worst flow readings in the sector and
both are tariff-exposed; `DE` is **+0.321 with OBV 매집 and the sector's best 5-day name (+9.67)**.

**§D competition / peers** — 🚨 **The tariff channel is pricing name-by-name, not node-by-node**: inside
Construction Machinery, `PCAR`/`CMI` are 🔴분산 while `DE` (agricultural) is the sector's best week.
**Trucks and engines are being sold; agriculture is being bought** — the opposite of a broad trade-war
read, and it is measured on the settled frame.

**§E refutation + dated catalyst** — **`ITW` is the single clearest instrument casualty on this sheet**:
it entered the "leader pullback" bucket on **RSI 20.3**, and its Wilder RSI is **44.8** — a **24.5-point
gap**, the largest measured. On the standard formula it is a hair inside the bucket rather than deeply
washed out. **The setup is not what the printout said it was.**
**Dated catalysts**: 🚨 **09-08 Canadian tariffs take effect and the only bracket on that date settles
09-12 (`S123`) — four days late.** `D342`, 3rd run. **The agricultural leg is now bracketed by `S129`
(09-09), but on the STAPLES side (`ADM`), not here** — see §STPL.

---

## §STPL · Consumer Staples — `N−`, and one name carries a registered bracket

**Candidates**: `ADM` (`S129`) · `TGT` · screener A `SYY`, `CL` · screener B `MNST`, `WMT`.
**Bucket-integrity marks**: `MNST` ✅ · `WMT` ✅ · **`SYY` ✗** · **`CL` ✗**.

**§A numbers — `TGT`** (this closes the gap `SECTOR_DEEP_STPL §4` named): trailing P/E **17.31**,
forward **17.58**, **PEG 2.57**, P/S 0.70, mean target **3.2% BELOW price**, ratings **2 SB · 10 B ·
22 H** — 🚨 **65% of the sell side is on Hold after a +31.6pp 60-day run.**
**Revisions**: current quarter **+7.7%**, next quarter +5.1%, **current year +21.3%** (8.33 → 10.10),
**next year +6.9% — but next-year EPS 9.50 is BELOW current-year 10.10 (−5.9%).**
🚨 **Verified arithmetic**: 9.50 ÷ 10.10 − 1 = **−5.94%**. ⇒ **the same shape as `MPC`, milder**:
consensus marks up this year 21% and models next year lower. **`L2` fires on `TGT` too**, and the sheet
says so rather than treating the sector's best name as unambiguous.
**`ADM`**: 🚫 no valuation pulled — **blank stated as blank.** What is measured: flow **−0.643 🔴분산**,
OBV −0.154 분산, `exc60` −4.06, and — **the only primary-source reading in this entire sheet** — its
own 10-K Risk Factors state *"Increases in tariff and restrictive trade policies around the world **has,
and could, negatively impact** the Company's ability to enter certain markets"*, plus an
**`S-3ASR` + two `424B2` + an `FWP` filed inside 60 days** (a live shelf/debt takedown).

**§B thesis + freshness** — the `N−` is a **20-day verdict**: **9 of 9 nodes negative on `exc20`**,
range −4.37 to −15.04. The 5-day positive (`exc5` +0.939, 15 of 19 names up) is a **bounce**, and the
two are not comparable. **Freshness: `UNMEASURED (G1 FAIL)`.**

**§C flow / positioning** — `TGT` flow **+0.733** (sector's highest), OBV **+0.226 매집**;
`WMT` **−0.589 🔴분산**, OBV −0.282 분산, and it is **46.1% of the sector with `COST`**.
⚠ **`MNST` is excluded from every aggregate in this sheet**: `RS20` **−55.8** with **OBV +0.380 매집**
— a `D6` grade-C conflict PREMORTEM ruled **unresolvable**. **No verdict, no tag, and it is not a
candidate.**

**§D competition / peers** — the Merchandise Retail node is `WMT` **−9.95**, `COST` **+0.06**,
`TGT` **+31.61** on `exc60` — a **41.6pp spread across three peers in one GICS box** — **all three measured as excess return versus
`SPY`** (RULE C1: the benchmark is `SPY`, named here and in this file's header; the comparison below is
between two `SPY`-benchmarked numbers, not against an unnamed baseline). **`TGT` is not outperforming a
sector; it is outperforming its two direct competitors, `WMT` and `COST`, on the same `SPY` benchmark.**

**§E refutation + dated catalyst** — **`TGT`**: 22 of 34 analysts on Hold, target below price, and next-
year EPS below this year's. **`ADM`**: its own filing says the impairment is **past tense**, and its
flow was already 🔴분산 **before** the effective date — which is `S129`'s branch B in advance.
**Dated catalyst**: 🚨 **`S129` settles 2026-09-09** (`ADM` 5-session excess vs `SPY`, 09-02 → 09-09,
A ≤ −4.00pp / B ≥ +2.50pp) — **this closes `D342`'s unbracketed agricultural half after 3 runs.**

---

## §DISC · Consumer Discretionary — `N−` (demoted today), and its two winners are through consensus

**Candidates**: `DASH`, `ABNB` (the PREMORTEM promotion's subjects) · screener A `ROST`, `AMZN` ·
screener B `NKE`, `AZO` · screener C `TJX`, `CCL`, `HD`.
**Bucket-integrity marks**: `ROST` ✅ · `NKE` ✅ · `AZO` ✅ · `TJX` ✅ · **`AMZN` ✗** · **`CCL` ✗** ·
**`HD` ✗**.

**§A numbers — `DASH`** (cited from `SECTOR_DEEP_DISC §3`): forward P/E **28.34**, trailing 120.22,
**PEG 5.22**, mean target **+9.3%**, **current-quarter revisions +10.5% / 90d but NEXT quarter −0.3%.**
**`ABNB`** (this closes the gap `SECTOR_DEEP_DISC §3` named): trailing P/E **43.35**, forward **30.58**,
**PEG 2.03**, P/S **8.54**, mean target **5.8% BELOW price**, ratings 4 SB · 20 B · **18 H**.
Revisions: current quarter **+3.7%**, next quarter +3.0%, current year +4.0%, next year **+2.5%** —
🚨 **flat-to-decelerating across every horizon, after a +35.4pp 60-day run.**
🚨 **Verified**: `ABNB` next-year EPS 6.19 vs current-year 5.29 = **+17.0%** growth against a **30.58×**
forward multiple ⇒ **PEG 2.03**, consistent with the printed figure.

**§B thesis + freshness** — the demotion is a statement about **big-ticket, credit-sensitive
consumption**, with `DGS30` at the **92nd percentile of 365 days (5.17 @08-25)** as the named mechanism.
**9 of 11 nodes negative on `exc20`; 9 of 11 negative on `eqflow`.**
**Freshness: `UNMEASURED (G1 FAIL)`.**

**§C flow / positioning** — `DASH` OBV **+0.670 매집 — the highest in the top-12 `RS60` cohort**,
`RS20` +13.1 / `RS60` **+45.7 (universe #1)**. `ABNB` OBV +0.269 매집, +19.9 / **+38.7 (#2)**.
Against them: `HD`/`LOW` both **🔴분산 with negative OBV**, `eqflow` **−0.643 = the worst multi-name
node in the sector**; `F` **−0.856 🔴분산**; `TJX` **OBV −0.360 분산** (its `exc20` is −20.36).

**§D competition / peers** — 🚨 **Neither winner has a peer group inside its own sector.** `DASH` is
**alone in its GICS industry (n=1)**; `ABNB` sits in a 6-name node whose other five average roughly −5
on `exc60` and which carries **3 of the sector's 11 reds**. ⇒ **"beating the peer group" is not
available as evidence for either name** — there is no group.

**§E refutation + dated catalyst** — **`DASH`**: PEG **5.22**, only **+9.3%** to a mean target after
+42.8pp, and **revision acceleration confined to the current quarter (next quarter −0.3%)** — the shape
of a beat being priced, not an estimate cycle turning. **`ABNB`**: target **below** price, PEG 2.03,
**every revision horizon +2.5% to +4.0%** — no acceleration at all.
**The screener names**: **`HD` and `CCL` are not washouts** (Wilder 41.6 and 37.6 against a <28 gate),
and **`AMZN` is not a pullback** (48.0 against a <45 gate). **Three of the sector's screener candidates
are instrument artifacts.**
**Dated catalyst**: none registered on any DISC name this run. 🚫 **Stated as a gap.**

---

## §LIVE · Cross-sector shortlist names (beyond the DEEP sectors)

`US_LIVE_SHORTLIST.json` produced **5 names**; `MRK` and `JNJ` are handled in §HLTH. The other three:

| name | sector | flow read (asof 08-27) | FINRA verdict | disposition |
|---|---|---|---|---|
| **`COIN`** | Financials | flow **+0.828 = universe #1**, OBV +0.174 매집, `RS20` +9.4, `RS60` +5.1, `delta` −0.150 | △정상숏 (`z −0.29`) | 🚫 **NOT a candidate.** The 08-26 BET measured **CY consensus +1.01 → −2.06 (−303.5%)** (`M956`) and 🚨 **the cause is still unread — the single largest `C3` gap the desk carries.** A name cannot enter this sheet on a flow rank while its denominator is a measured, unexplained collapse |
| **`MSTR`** | Info Tech | flow **+0.789 = #2**, OBV **+0.458 = the sweep's highest**, `RS20` +26.3, `RS60` −7.8 | ✅저숏/숏커버 (`z −0.81`) | 🚫 **NOT a candidate.** Already on the **rejection ledger** (`H.밸류소진`, recheck **09-16**); consensus **+43.82 → −6.69 (−115.3%)** and a **2.52× forward P/E** — `L2` in its purest form. **The ledger row stands; it is not revived** (`due` returned 0 and its recheck date has not passed) |
| **`MRVL`** | Info Tech | flow +0.417, OBV **+0.362 매집**, `RS20` **+32.6**, `RS60` −15.3 | ✅저숏/숏커버 (`z −0.64`) | ⏸ **Deferred by construction — it reports TONIGHT.** `S116` brackets it (settles 08-28) with **A ≥ +12.0pp / B ≤ −12.0pp on `MRVL − AVGO`**, and §0-a of `BLINDSPOT_PREMORTEM` verified that threshold sits **outside** the ±9.9% implied move. **Entering a name on the evening of its own binary is what the bracket exists to prevent** |

⚠ **`C18` narrowed on `MRVL` today** (`M991`): FINRA `z −0.64` "저숏" and `module_flow` **3.8% float
COVERING, DTC 1.2** — **the two instruments agree**, where on 08-25 `module_flow` read **BUILDING**.
First movement in the contradiction; `NVDA` and `ANET` legs untested.

---

## §HELD · The book, read against this sheet's own findings

**11 US names.** Two require a line here because this run's own work moved them:

- 🚨 **`AVGO` — PREMORTEM tagged it EXHAUSTED and this sheet confirms it on the numbers**: flow
  **−0.715 🔴분산**, OBV **−0.103 분산**, `RS20` −9.5, `RS60` **−25.4**, `exc60` **−23.69** — negative
  on every axis, **the worst-reading held name on the board.** It has **no live narrative thread in a
  154-thread alive set** (`EVENT_ALPHA §2`), its **customer has been unnamed for the life of the
  position (`W4`, still open)**, and it **prints 09-02** with `S127` armed. ⚠ Its implied move reads
  **±2.8% at an 08-28 (D1) expiry for a 09-02 print** — `D353`'s **9th** reproduction; `S127`'s
  thresholds were correctly not taken from that.
- **`NVDA`** — `P90` **scored `FIRED-A`** this run (gross margin **75.0%** vs 74.9% prior; FQ3 guide
  **~74.0% = −100bp**), i.e. **pass-through, not pricing power**, with **memory cost named in the
  documents**. And a **$12.9bn Hugging Face acquisition** was reported today with **no company
  announcement** ⇒ **`S130` registered (settles 09-10)**. ⚠ Its own event has **not settled** —
  `S79`, `S81`, `S115`, `S117` all settle at tonight's close — so **no tag is issued on it here.**

---

## §B-FRESHNESS · Freshness tags, by rule

| section | freshness |
|---|---|
| ENRG · HLTH · INDU · STPL · DISC · LIVE · HELD | **`UNMEASURED (G1 FAIL)`** |

🚫 **Every row reads `UNMEASURED`, never `stale` / `cold` / `quiet`.** `vel_coverage` **16.7%** against
an 80% bar, and the covered set is **`us_top300` ranks 1–50, contiguous** — a mega-cap-only sample.
**`F1`'s counter is NOT incremented** (`D16`).
🚨 **Standing trap, armed again**: `D369` — the tag extractor manufactured `CONFIRMED FRESH GO LIVE`
from prose on 08-26 in a report whose every freshness row read `UNMEASURED`, and it reproduced at scale
on KR this morning (39 of 58 rows). **The same trap is armed on this file.**

### ALPHA verdict, written by Stage 10 into this section (the tags are ALPHA's, the section is BET's)

**🟢LIVE = 0 · 🟡PARTIAL = 0 · 🔴RESOLVED = 0. No freshness verdict was issued at all — BY RULE.**

🚫 **`theme_age` was NOT RUN this run.** Not "run and returned nothing" — **not run**, because
PREFLIGHT **G1 FAILed** and the removed right is explicit: *ALPHA may not issue a freshness verdict when
G1 fails.* Running the tool and then declining to quote it would have produced a number in a log that a
later run could mistake for evidence.

🚨 **`F1`'s counter is NOT incremented** (`D16`). The desk's standing count — *"🟢LIVE fired 0 times in
N consecutive runs"* — **may not take a tick from this run**, because a gate that was never opened is
not a gate that failed to fire. Reporting a zero here would be the estimate-snapshot daemon's error:
counting files and calling them days.

✅ **The falsification probe WAS run, and the pipe is alive**: `Nvidia` **4,756** · `Nucor` **31** ·
`Marathon Petroleum` **22** · `Nasdaq Inc` **6** (`--days 7 --scope foreign`) — three orders of
magnitude apart, i.e. **discriminating**. 🚫 **`Nasdaq Inc` at 6 and `Nucor` at 31 are NOT read as
"quiet".** And the reason the sweep's axis is nonetheless dead is now measured rather than guessed:
**the 50 covered names are `us_top300` ranks 1–50, contiguous** (`M987`, a 4th reproduction of `R103`).

**Carry-forward list — ALPHA tags follow the NAME, not the sector's turn in the rotation.** These
names are handed to the next run's inheritance packet **regardless of whether their sector holds a DEEP
slot**, each with a dated appointment:

| name | why it is carried | dated appointment |
|---|---|---|
| `MRVL` | reports tonight; `S116` settles on it | **2026-08-28** |
| `AVGO` (held) | PREMORTEM **EXHAUSTED**; `W4` open; prints 09-02 | **2026-09-02** / `S127` **09-08** |
| `NVDA` (held) | `P90` FIRED-A; Hugging Face deal unconfirmed | `S130` **2026-09-10** |
| `MPC` · `PSX` (held) | `P96`/`P83` settle tonight **on a contract roll**; `P103` is the clean re-read | **2026-09-02** |
| `ADM` | `S129`'s subject | **2026-09-09** |
| `VLO` | rejection ledger `H.밸류소진` | **2026-09-04** |
| `TGT` · `DASH` · `ABNB` | missed ledger `Q.확신부족` | **2026-09-11** |
| `COHR` · `LITE` | missed ledger; the un-registered optical cycle | **2026-09-10 / 09-09** |
| `HON` · `CCL` · `FN` | rejection ledger | **2026-09-10** |

**Momentum-only / positioning stamps, graded before use (`D6`):**
- 🚨 **`MNST` — momentum and accumulation disagree and the disagreement is C-grade**: `RS20` **−55.8**
  with **OBV +0.380 매집**. OBV alone is **grade C** (r≈0.49 to real flow, no leading power, t=1.00)
  ⇒ **downgraded to a reported disagreement, NOT converted into a tape trade, and NO tag issued.**
- **`MRVL`** — `RS20` +32.6 with OBV **+0.362 매집**: the two axes **agree**, so no momentum-only
  stamp. ⚠ `C18` narrowed on it today (`M991`): FINRA `z −0.64` and `module_flow` **3.8% float
  COVERING** now agree, where 08-25 read **BUILDING**.
- **`ANET`** (held) — `RS20` +14.7 / `RS60` +14.2 with OBV **+0.315 매집**, against a FINRA `z +2.06`
  on 08-25 (the board's highest). **`C18`'s untested leg. No `⚡crowded-short` stamp issued** — neither
  instrument is graded highly enough to overrule the other.

**No name received a 🔴 this run**, so **no ALPHA rejection row was written** — the two rejections filed
today (`HON`, `CCL`) came from **BET on instrument grounds**, not from a freshness verdict. Stated so
the ledger's provenance is unambiguous.

---

## §LEDGER · Rows written by this stage

| ledger | ticker | class | condition | recheck |
|---|---|---|---|---|
| **missed** | `TGT` | `Q.확신부족` | `TGT` mean analyst target rises **above** the price **AND** next-year EPS stops being below current-year | **2026-09-11** |
| **missed** | `DASH` | `Q.확신부족` | next-quarter EPS revision turns **positive** on a fresh pull **AND** OBV still 매집 on a settled bar | **2026-09-11** |
| **missed** | `ABNB` | `Q.확신부족` | mean target rises above price **AND** any revision horizon exceeds +6% / 90d | **2026-09-11** |
| **reject** | `HON` | `A.flow미도착` | screener "washout" membership is an artifact — Wilder RSI **38.5** against a **<28** gate (`D385`); flow −0.900, OBV −0.239 분산, `exc20` −13.50 | **2026-09-10** |
| **reject** | `CCL` | `A.flow미도착` | same class — Wilder **37.6** against **<28**; flow −0.774 🔴분산, `exc20` −13.00 | **2026-09-10** |

*(Rows already written by EVENT_ALPHA this run: reject `FN`; missed `COHR`, `LITE`.)*
⚠ **Every condition carries a market-side conjunct** — checked against **`C19`**.
⚠ **Boundary respected**: names *stated and set aside* (`HON`, `CCL`) went to the **rejection** ledger;
names that *surfaced and simply did not make the sheet* (`TGT`, `DASH`, `ABNB`) went to **missed**. The
script enforces the boundary (`missed_ledger add` refuses a ticker×date already rejected).
✅ **No name was removed on narrative grounds while its flow still passed.** The two rejections are
**instrument-grounded**, and both names' flow also fails (−0.900 and −0.774).

---

## §IDs registered by this stage
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`, excluding this
> run's own files: **`M993` `M994` → 0 hits · `D385` → 0 hits.** Highest before this append: `M992`,
> `D384` (both this run).

- **`M993`** — the screener's RSI is Cutler's (SMA) while its buckets use Wilder thresholds; measured
  mean gap **−12.4 points**, max **−24.5** (`ITW`), and **8 of 18 candidates (44%) fail their own
  bucket** under the convention the thresholds come from. Not a stub-bar effect (stub moves RSI 0.1–7.0).
- **`M994`** — five of six candidate leaders trade **at or through** their mean analyst target
  (`MPC` −10.8% · `ABNB` −5.8% · `TGT` −3.2% · `MRK` −1.4% · `DASH` +9.3%), while the epicenter that
  guided margin **down** carries **+45.9%**.
- **`D385`** — the formula/threshold mismatch above, with its one-line remedy (switch the source to
  Wilder **or** recalibrate 28/45/30–52). Human-approval item.

---

## ✅ EXIT CHECK
- [x] **Company scoreboard consulted before any re-derivation** (§0): 5 rows, all KR, **zero US
      coverage** ⇒ every name is a RE-DIG with the failing test named (**coverage**). No matured
      observation point on any cited row (none of the 5 is cited). Its two reading rules honoured.
- [x] **Every DEEP sector has a section** (ENRG · HLTH · INDU · STPL · DISC), and the **cross-sector
      LIVE shortlist names are handled in §LIVE** — `MRK`/`JNJ` inside §HLTH, `COIN`/`MSTR`/`MRVL`
      explicitly dropped or deferred **with reasons**.
- [x] **Numbers cross-checked** — `MPC` −35.90% / +81.93%, `TGT` −5.94%, `ABNB` PEG 2.03 all recomputed
      here. **Blanks are stated as blanks** (`ADM`, `JNJ`, all INDU names): no figure is guessed.
- [x] **Flow/positioning cross-read present per candidate**; **written as ONE file** with per-sector
      sections.
- [x] **Every set-aside name is in a ledger with a class AND a `--revives-if` / `--enters-if` AND a
      `--recheck-date`** (§LEDGER, 5 rows this stage + 3 from EVENT_ALPHA). No permanent bans filed.
- [x] **No name removed on narrative grounds while its measured flow passed** — the two rejections are
      instrument-grounded and both names' flow also fails.
- [x] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** with a
      class and an `--enters-if`. **This sheet produced 2 rejections and 3 missed entries**, so the
      funnel is scored on both sides.
- [x] **Sizing language consistent with the exposure state** — state is **`정상`, not `복귀`**, so no
      target-filling obligation arises; that is stated in §0 rather than assumed, and **no sizing
      appears anywhere in this file** (P4).
- [x] Linter run — see the run log.
