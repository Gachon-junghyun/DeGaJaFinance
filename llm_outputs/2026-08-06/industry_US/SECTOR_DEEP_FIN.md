# SECTOR_DEEP_FIN — Financials · industry_US · 2026-08-06 · **CONTINUOUS track (re-entered) → DELTA ONLY**

> Structure carried **by reference** to `llm_outputs/2026-08-04/industry_US/SECTOR_DEEP_FIN.md`.
> The 08-04 file's §2 rate-beta regression (51 tickers, 60 sessions), §3 sub-node partition, §4 M135-R
> derivation, §5 Lens-3 re-tags and §6 credit table are **not re-printed** and are **not overturned by
> anything measured here**. Only what changed, plus the four questions this slot was handed.
> Benchmark is **SPY, inline** on every relative number (**C1**). **P4 — analysis only.** No position
> language, no sizing, no entry/exit anywhere in this file.
> Prices: yfinance, **settled bar 2026-08-05** (the live 08-06 bar is excluded, **D74**). Rates: `[FRED]`,
> newest print **2026-08-04** — **D139 holds a fourth time**, the 08-05 nominal is unpublished.

---

## 0 · The one-line answer

**The breadth survives removing BRK-B and does not survive removing the velocity axis — and this is not a
counterfactual, because the desk has already printed the velocity-free number twice: Financials' breadth
was 0.043 on the 2026-08-05 run and 0.085 on the 2026-08-04 run, on the two consecutive runs where the
velocity axis happened to be OFF. The promotion is riding the 20–60 session window, and the 20-session
leg gained 2.02 of its 2.12 points on 08-05 from a bad session rolling off the back of the window rather
than from the tape.**

---

## 1 · The delta since 08-04 — and it is an instrument delta, not a market delta

**The 08-04 file measured the sector at `asof 2026-08-03`: wflow +0.093 · eqflow +0.101 · 4🟢/7🔴 ·
breadth 0.09 · 4th of 11.** Today's file reads **wflow +0.317 · eqflow +0.190 · 7🟢/7🔴 · breadth 0.15 ·
rank 1 of 11** `[SECTOR_FLOW_US.json, asof 2026-08-05]`. That is the largest two-session move in the
sector's flow record on this desk. **Here is what produced it.**

### 1a · ★★★ The velocity axis was OFF for the two runs the diff baseline was built from, and came back ON for this one

`[own calc over four consecutive SECTOR_FLOW_US.json files]`

| run file | `asof` | names with `velocity` populated | FIN names covered | FIN wflow | FIN eqflow | FIN 🟢 | **FIN breadth** |
|---|---|---|---|---|---|---|---|
| 2026-08-03 | 07-31 | **51 / 300** | 8 | +0.214 | +0.161 | 5 | **0.106** |
| 2026-08-04 | 08-03 | **0 / 300** | 0 | +0.093 | +0.101 | 4 | **0.085** |
| 2026-08-05 | 08-04 | **0 / 300** | 0 | +0.129 | +0.055 | 2 | **0.043** |
| **2026-08-06** | **08-05** | **51 / 300** | **8** | **+0.317** | **+0.190** | **7** | **0.149** |

★★★ **The axis flickers.** It was on 07-31, off for two runs, on again on 08-05. **Financials' wflow is
+0.21/+0.32 on the runs where it is on and +0.09/+0.13 on the runs where it is off.** No market event
separates those states.

### 1b · Which means the five "new-🟢" are not new

| ticker | 08-03 run (07-31, axis **on**) | 08-04 run (08-03, axis **off**) | 08-05 run (08-04, axis **off**) | **08-06 run (08-05, axis on)** |
|---|---|---|---|---|
| **JPM** | **+0.553 🟢** v 2.14 | +0.339 🟡 v — | +0.303 🟡 v — | **+0.552 🟢** v 1.95 · flagged `new_green` |
| **BAC** | **+0.600 🟢** v 1.42 | +0.362 🟡 v — | +0.296 🟡 v — | **+0.554 🟢** v 1.45 · flagged `new_green` |
| **MA** | **+0.573 🟢** v 2.24 | +0.483 🟡 v — | +0.563 🟡 v — | **+0.716 🟢** v 1.58 · flagged `new_green` |
| **WFC** | +0.298 🟡 v 1.87 | +0.033 🟡 v — | +0.125 🟡 v — | **+0.457 🟢** v 1.89 · flagged `new_green` |
| **BRK-B** | +0.163 🟡 v 1.82 | +0.119 🟡 v — | +0.257 🟡 v — | **+0.487 🟢** v 1.63 · flagged `new_green` |
| GS | +0.002 🟡 v 1.89 | **−0.485 🔴** | −0.377 🔴 | +0.095 🟡 v 1.79 |

⇒ ★★ **JPM, BAC and MA were already 🟢 on 07-31 with the same axis lit. They are `new_green` today only
because the axis blinked off across the two runs the baseline was taken from.** The flag is measuring the
instrument's own state, not an ignition. **GS's round trip 🟡 → 🔴 → 🔴 → 🟡 with no tape event of that
size is the same artifact with the sign reversed.**

### 1c · Why the code's own guard did not catch it

`scripts/sector_flow.py:181` carries the comment *"3축(nonews) vs 4축(news) flow_score는 크기가 달라
Δ를 섞으면 안 됨"* and `prev_snapshot` filters history to the same `mode`. **But `mode` is a run-level
flag (`"news"` / `"nonews"`), and every one of these four runs was stamped `"news"`.** The axis count that
actually changed is **per-name**, and nothing records it. ⇒ **The guard that exists is exactly the guard
that failed.** Handed to §7 as a human item, not fixed here.

### 1d · The coverage cutoff is a hard mega-cap prefix, not a sample

`[own calc]` The 51 covered names are **market-cap ranks 1 through 51, with no gaps and nothing past 51**
(rank 51 = RTX, `velocity` 0.35 populated; rank 52 = C, `velocity` `None`). **The cause is `unknown`
(C3)** — an exact rank-prefix is consistent with a hard cap or a per-run quota exhausting after ~102 API
calls, and is inconsistent with random failure.

⇒ ★★ **The velocity path — the only path that can light a 🟢 without volume — is available exclusively to
the 51 largest companies in the universe, and Financials holds 8 of those 51, second only to IT's 20.**
Industrials holds **4 of 50**. **"Breadth" is therefore not cap-neutral: it is partly a count of how many
of a sector's names sit in the top 51.**

⚠ **C2, the half that argues the other way, stated and not suppressed.** The 08-05 tape half-agrees with a
positive reading: XLF's daily excess vs SPY was **+0.41** on 08-05 after four negative sessions, JPM's
RS20 is **+5.38** and BAC's **+5.22** vs SPY, and **every one of the 47 names except six carries OBV 매집**.
The sector is not being called weak here. What is being called is that **the specific statistic that
carried the promotion moved for a reason that is not the tape.**

---

## 2 · ★★★ Does the breadth survive the two removals — the arithmetic

**Definitions stated as choices (C5).** `breadth ≡ 🟢 count / n`. `wflow` = mcap-weighted mean
`flow_score`; `eqflow` = equal-weighted mean. The green gate is `module_flow/_synthesize.py:13-49`:
green-axis count over **{OBV 매집, RS20 > 0, `vol_surge` ≥ 1.2, `velocity` ≥ 1.2}**, requiring **≥ 3 of 4**
plus conviction. `flow_score` = mean of `clip(obv/0.16)`, `clip(rs20/8)`, `clip((vol_surge−1)/0.6)` **and**
`clip((vel−1)/0.4)` **only when velocity exists**. ⇒ **removing the velocity axis is a 4-axis → 3-axis
recomputation, not a name deletion.** My 3-axis/4-axis recomputation reproduces all 300 published
`flow_score` values **exactly (0 mismatches)**, so the arithmetic below is the file's own.

### 2a · Removal (a) — drop BRK-B. **The breadth SURVIVES.**

| cut | n | 🟢 | **breadth** | rank of 11 | wflow | eqflow |
|---|---|---|---|---|---|---|
| all 47 (published) | 47 | 7 | **0.149** | **1** | +0.3166 | +0.1897 |
| **ex-BRK-B** | 46 | 6 | **0.1304** | **still 1** (next: ENRG / IT 0.125) | **+0.2890** (still 1) | **+0.1832** (still 1, by **0.004** over INDU +0.179) |
| ex top-5 by cap (BRK-B, JPM, V, MA, BAC = **44.65%** of sector cap) | 42 | 2 | 0.048 | — | +0.1693 | +0.1511 |

**BRK-B is 13.94% of a $7,573.9bn sector and contributes +0.0679 of the +0.3166 wflow — 21.4% of the
sector's mega-cap flow score from one name (M173 confirmed on fresh data).** Removing it costs **1.9
breadth points** and leaves the sector rank-1 on all three statistics. ⚠ **The eqflow rank survives by
0.004 against Industrials — that margin is inside any reasonable measurement noise, so eqflow rank 1 vs 2
is `indistinguishable` ex-BRK-B (C4).**

### 2b · Removal (b) — drop the velocity axis. **The breadth DOES NOT survive, and the whole board must be re-cut, not just Financials**

★ Removing the axis only from Financials would be the wrong test — **the fair cut removes it everywhere,
because 51 names board-wide have it.** Recomputed on a homogeneous 3-axis basis:

| sector | n | published breadth | **breadth, 3-axis** | published wflow | **wflow 3-ax** | published eqflow | **eqflow 3-ax** |
|---|---|---|---|---|---|---|---|
| **Financials** | 47 | **0.149 (1st)** | **0.043 → 6th** | +0.317 (1st) | **+0.231 (still 1st)** | +0.190 (1st) | **+0.162 → 2nd** |
| Industrials | 50 | 0.100 (5th) | **0.100 — unchanged, → 1st** | +0.126 | +0.118 | +0.179 | **+0.181 (1st)** |
| Health Care | 32 | 0.094 | **0.094 — unchanged** | +0.075 | −0.037 | +0.055 | +0.021 |
| Real Estate | 12 | 0.083 | 0.083 — unchanged | +0.022 | +0.022 | +0.038 | +0.038 |
| Info Tech | 56 | 0.125 | 0.071 | +0.246 | +0.089 | +0.001 | −0.083 |
| Cons Disc | 28 | 0.107 | 0.071 | +0.212 | +0.127 | +0.120 | +0.116 |
| Energy | 16 | 0.125 | **0.000** | +0.230 | +0.161 | −0.055 | −0.073 |
| MATR / COMM / STPL / UTIL | — | 0.000 | 0.000 | — | — | — | — |

★★★ **Financials loses 5 of its 7 greens — the largest loss on the board — and falls from rank 1 to rank 6
of 11 on breadth.** Industrials, Health Care and Real Estate lose **nothing**, because every one of their
greens is volume-lit. **Strip a path that Industrials had access to on only 4 of 50 names and used zero
times, and Industrials' 0.100 beats Financials' 0.043.**

**The surviving two greens, name by name:** **PRU** (`vol_surge` 1.39 · OBV 매집 · RS20 +3.4) and **MET**
(1.32 · 매집 · +3.6) — the only Financials names clearing all three of the volume-path gates.
⚠ **KKR misses by 0.01** (`vol_surge` **1.19** vs the 1.20 line, OBV 매집, RS20 +10.0 — the sector's
highest flow score at +0.772 and not a green). **A knife-edge at the third decimal is carrying a sector
verdict; that is a fragility, and it is recorded rather than rounded away (C3).**

### 2c · The counterfactual is not a counterfactual — the desk already printed it

**The 3-axis breadth I compute for today, 0.043, is the exact number Financials printed on the
2026-08-05 run (`asof 08-04`), on which the axis was off: 2 greens / 47 = 0.043.** And the 08-04 run
printed **0.085**. ⇒ **§2b's result has already been observed twice on live runs and does not depend on my
recomputation at all.**

⚠⚠ **And it is what drove the slot itself.** ROTATION dropped FIN from the continuous track on 08-05
(*"N+, no longer top-OW"*) — **on a run where the axis was off** — and re-promoted it to OW today — **on a
run where the axis came back on.** `SECTOR_ROTATION §4` calls this *"a re-entry on a fresh number, not
thrash."* **The number is fresh; the instrument that produced it is the one that changed.**

### 2d · What survives both removals, stated positively

**Combined cut (no BRK-B, no velocity axis): 2 greens / 46 = 0.043 · wflow +0.217 · eqflow +0.159.**
⇒ **The mega-cap flow leg (wflow rank 1) survives everything. The breadth leg survives BRK-B and fails
velocity. The equal-weight leg survives velocity in level but not in rank.** **The promotion's stated
carrier — *"breadth 0.15, the highest of 11"* — is the one leg that does not survive.**

⚠ **D6, binding and applied literally.** Nothing above is a claim that the five names are weak. It is a
claim about **what lit their tag**. Their price facts are separately positive and are stated in §8.

---

## 3 · The BRK-B question resolved: **both — and the two findings are different statistics that do not contradict**

`BLINDSPOT_PREMORTEM §1` records that S65's median RS20 vs SPY of {JPM, BAC, WFC, BRK-B} is **+3.405**
including BRK-B and **+5.219** excluding it, and reads that as *"the opposite of what M173's concentration
warning would predict."* **I reproduce the anchors exactly** `[own calc, settled 08-05, SPY inline]`:

| name | RS20 vs SPY | contribution |
|---|---|---|
| JPM | **+5.38** | upper pair |
| BAC | **+5.22** | upper pair |
| **BRK-B** | **+1.59** | lower pair |
| WFC | **+0.95** | lower pair |
| **median of 4** | **+3.405** | = mean(1.59, 5.22) |
| **median of 3, ex-BRK-B** | **+5.219** | = the middle value, BAC |

★ **The "drag" is a median mechanic on n = 4 (S1).** With four observations the median is the *mean of the
two middle values*; removing one low observation makes the median the *actual middle value*. **Any of the
four lower names would produce the same jump — removing WFC instead gives median(JPM, BAC, BRK-B) =
+5.22, identically.** ⇒ **The +3.405 → +5.219 move is a property of the estimator, not evidence about
Berkshire.** **BLINDSPOT's framing is arithmetically correct and causally over-read.**

**But the substantive claim behind it is true anyway, and on a cleaner measure.** BRK-B vs **its own sector
ETF**, `[own calc, settled 08-05]`:

| window | BRK-B | XLF | **BRK-B − XLF** |
|---|---|---|---|
| 5d | +1.90% | +2.33% | **−0.43 pp** |
| 10d | +6.02% | +3.48% | +2.54 pp |
| 20d | +4.86% | +5.51% | **−0.65 pp** |
| 40d | +6.54% | +11.99% | **−5.45 pp** |
| 60d | +9.02% | +13.59% | **−4.57 pp** |
| 120d | +3.77% | +10.93% | **−7.16 pp** |
| 250d | +10.65% | +13.38% | **−2.73 pp** |

⇒ ★★ **BRK-B has underperformed XLF on every window except 10 days.** So:

- **On cap: a concentration risk. Confirmed.** 13.94% of sector cap, 21.4% of wflow. M173 stands unchanged.
- **On performance: a drag. Confirmed, but on the ETF-relative measure, not on the S65 median mechanic.**
- **They do not contradict** because they are different objects: M173 is a statement about **mcap weight
  inside a weighted mean**; the drag is a statement about **equal-weight relative return**. A name can be
  simultaneously the largest weight and the worst performer, and BRK-B is.

**Its own book is the third confirmation** `[module_fundamentals_us BRK-B, 2026-08-06]`: **CY EPS
+1.6%/90d, 30-day CY revision breadth 2↑/0↓, next-year −0.8%/90d, forward P/E 24.01 against trailing
15.43** — forward EPS **$21.57** vs trailing **$33.57**, i.e. consensus carries a **−36% earnings step-down**.
⚠ **B2 applied: no margin percentile exists in this repo (D15), so that multiple is NOT read as a
valuation — it is read only against the estimate-momentum table, which is the flattest of the eight names
measured in §6.** ⚠ **S1: 2 Buy / 2 Hold is the entire covering panel — the revision book is n≈4.**

⚠⚠ **Dated, and it lands inside S65's own window: BRK-B reports Q2 on 2026-08-09** `[yfinance calendar]`,
**two sessions before S65 settles 08-11.** One of the bracket's four members has an earnings event inside
the bracket. **Recorded, not adjusted — the observable is frozen (L3).**

---

## 4 · Players ∪ thematic — what the primaries actually say

### 4a · What lit the velocity axis, named with print dates (**A6**)

The axis is an **OR-count of `TICKER|Company Name` over 7 days ÷ the 30-day rate × 30/7**
(`module_flow/_news_velocity.py:141`). For 3-letter tickers it degrades to **company name only**. I
re-measured the counts and they reproduce the published velocities:

| name | query used | 7d | 30d | recomputed vel | published |
|---|---|---|---|---|---|
| JPM | `JPMorgan Chase` | 602 | 1316 | **1.96** | 1.95 |
| WFC | `Wells Fargo` | 378 | 853 | **1.90** | 1.89 |
| BAC | `Bank of America` | 331 | 978 | **1.45** | 1.45 |
| MA | `Mastercard` | 107 | 283 | **1.62** | 1.58 |

**JPM's spike has a named, dated cause and it is a corporate-policy announcement, not a rate or earnings
event:** *"JPMorgan Chase to Invest $750 Billion to Boost U.S. Housing Supply"* `[wsj + yahoo_finance +
businessinsider, 2026-08-03; body read]` — 1m affordable units by 2035, mortgage lending up ~40%, 850 new
lending advisers, chairing the US Chamber's new Housing Advisory Council. **A ten-year balance-sheet
commitment announced on 08-03 is the largest single contributor to a 7-day news count that lit a flow tag
on 08-05.**

★★ **And the axis has a contamination the desk has not named: it counts the bank as a research byline.**
Sampling the 30 top-ranked 7-day hits per name and classifying **subject** vs **third-party mention**
`[own classification, foreign scope]`:

| name | hits where the company is the **subject** | hits where it appears as **analyst byline / shareholder filing / fund sponsor** |
|---|---|---|
| **JPM** | ~28 / 30 | ~2 |
| **BAC** | ~13 / 30 | ~17 — incl. **6 identical Umicore transparency notifications** (Dutch/French/English × 2 dates) and BofA notes on Apple, Micron, Meta, the yen and the S&P target |
| **WFC** | ~8 / 30 | ~22 — Atmus coverage initiation, eBay bearish, Microsoft target reset, Snowflake, Intel, SSR Mining, plus a **Wells Fargo Commercial Mortgage Trust 8-K** |
| **GS** | ~6 / 30 | ~24 — Brent target, diesel squeeze, China AI, payroll forecast, Applied Materials, Pearson, Apple |

⇒ ★ **For the large sell-side banks the axis substantially measures the volume of research the bank
publishes about other companies, plus its regulatory shareholder disclosures.** ⚠ **C2 — the honest
counter, and it matters: velocity is a RATIO, so a constant background of byline noise inflates the 30-day
base as well and partially cancels.** What it does not cancel is a **burst**: WFC's 08-03/08-04 cluster is
six research notes in two days, none about Wells Fargo. **The correct statement is not "the velocity is
fake" — it is "for WFC and GS the numerator's composition is majority-not-about-the-company, and the axis
has no discriminator for that." Grade C (D6).**

⚠ **M152 acknowledged and it bites in exactly one place.** `C` (Citigroup) returns `velocity None` today.
**That is the rank-52 cutoff (§1d), not the `_US_STOP` list** — two different instruments, and conflating
them would be an error. **No zero-coverage inference is drawn anywhere in this file for A, AIG, ALL, C,
CB, GS, ICE, MA, MET, MS, V or WELL.** MA's velocity of 1.58 came from `module_flow`'s own FTS path, which
is not the tag layer M152 describes.

### 4b · Positioning — a clean null

`[scripts/us_flow.py, FINRA Reg SHO, date 2026-08-05]`: **JPM z −0.35 · BAC −1.16 · WFC −0.49 · PRU +0.68
· MET +0.29 · GS +0.08 — every one inside ±1.5, all 🟡 정상범위. BRK-B: `no data`.**
⇒ **No short-side divergence for or against the narrative (C4).** **D6: this is a proxy; the US desk has no
investor-type feed and none of this is evidence about who bought.**

---

## 5 · Value chain, with the binding constraint marked

Nodes ordered from the input price of money to the fee tail. **Every node's evidence is a primary filing
or a dated print; nodes with no instrument are marked `unknown` (C3).**

| # | node | who | measured state | source |
|---|---|---|---|---|
| 1 | **Policy rate (input price)** | FOMC | **held 3.50–3.75% on 2026-07-29, "hawkish pause", three policymakers favouring a +25bp HIKE** | `[news body, yahoo_finance 07-31]` |
| 2 | 🔒 **Funding cost / interest expense** | GS, MS, all banks | **GS interest expense $66,814m (2025) vs $73,341m (2024) = −$6.5bn**, explicitly *"reflecting the impact of lower average interest rates"* | `[GS 10-K, FY2025, filed 2026-02-13]` |
| 3 | **Balance-sheet origination (loans, cards, deposits)** | JPM, BAC, WFC | JPM FY26 NII guide raised to **~$105.5bn from ~$103bn**, attributed *"primarily to stronger balances"* | `[news body 07-31; M138 carried]` |
| 4 | **Markets / financing** | BAC, GS, MS | **BAC NII +$4.0bn to $60,096m, "primarily driven by higher net interest income related to Global Markets activity"**; GS market making **$17,993m** > all of GS NII | `[BAC 10-K FY2025; GS 10-K FY2025]` |
| 5 | **Fee / advisory / wealth** | GS, BAC, MS | GS investment banking **$9,348m, +21%**; GS investment management **$11,749m**; BAC investment & brokerage services **$19,956m vs $17,766m, +12.3%** | `[both 10-Ks]` |
| 6 | **Payments rails** | V, MA | MA Q2-2026 revenue **$9.28bn, +14.07% YoY** (XBRL-confirmed, 0.0% variance) | `[module_fundamentals_us MA]` |
| 7 | **Insurance float / spread** | MET, PRU, TRV, ALL | the **only two greens that survive §2b**; PRU forward EPS $14.60 vs trailing $9.72 | `[flow file; fundamentals]` |
| 8 | **Exchanges & market data** | ICE, CME, NDAQ, SPGI, MSCI, MCO | **4 of the sector's 7 reds sit here** (MCO −0.618, SPGI −0.633, MSCI −0.744, + IBKR/HOOD/AON/AJG); node RS60 remains the sector's worst | `[flow file; 08-04 §3b unchanged]` |

★★ **The BINDING CONSTRAINT is node 2, the cost of funds — and it is binding because it has stopped
delivering.** Both primaries locate the 2025 P&L move on the **liability** side or in **activity volume**,
not in asset yields or curve shape. **GS's NII rose 68% because interest expense fell.** That mechanism
requires the policy rate to keep falling — and node 1 measured a **hold with three hike dissents on
07-29**. ⇒ **The chain's one measured engine is running on an input that has been switched off, and the
node that would replace it (node 4, markets) is a volume story with no rate sign at all.**

⚠ **W5 / B5 — the label is the wrong unit, restated on this run's numbers.** Sub-node spread across the 47
runs **KKR +0.772 to HOOD −0.789 = 1.561**, versus the sector's own eqflow of **+0.190 — a spread 8.2×
the sector's move.** **"Financials" is not a usable unit of analysis.**

---

## 6 · Rate sensitivity: where it actually lands now (M138 / W3), and what the curve leg is worth

### 6a · Two primaries, and they carry **opposite** rate signs

| | **BAC** `[10-K FY2025, filed 2026-02-13, period 2025-12-31]` | **GS** `[10-K FY2025, period 2025-12-31]` |
|---|---|---|
| NII | **$60,096m** vs $56,060m (**+7.2%**) | **$13,559m** vs $8,056m (**+68%**) |
| Total revenue | $113,097m — **NII = 53.1%** | $58,283m — **NII = 23.3%** |
| **The bank's own attribution** | *"primarily driven by higher net interest income related to **Global Markets activity**, fixed-asset repricing, and deposit and loan growth, **partially offset by the impact of lower interest rates**"* | *"reflecting a **decrease in interest expense**, partially offset by a decrease in interest income… (each reflecting the impact of **lower average interest rates**)"* |
| **⇒ sign on falling rates** | **NEGATIVE — rates are named as the offset** | **POSITIVE — falling rates ARE the driver** |

★★★ **The sector does not have one rate sign. It has at least two, and they are opposite, in the same
fiscal year, in the two banks' own filed words.** ⇒ **"Financials benefits from a steepener" is not a
statement that can be true or false at the sector level — it is under-specified (C4).** **M138's migration
is confirmed on primary filings for the first time on this desk, and it is stronger than stated: the leg
did not only move from NIM to markets/financing, it INVERTED at GS.**

★ **A third, weaker corroboration on the volume half**: JPM raised FY26 NII to **~$105.5bn from ~$103bn**,
attributed *"primarily to stronger balances, while noting that rates were also modestly higher than
assumed"* `[news body, yahoo_finance 2026-07-31 — single outlet, grade C, D6]`. **Balances, not slope.**

⚠ **Staleness declared: both filings are FY2025, period 2025-12-31 — eight months old.** `module_disclosure_us
JPM` shows **no 10-Q in the last 90 days**; the Q2-2026 primary exists only as an **8-K Item 2.02 dated
2026-07-14** whose exhibit body this desk's tooling does not retrieve. **The Q2-2026 segment attribution is
`unknown` (C3) and is not guessed.**

### 6b · The curve leg, measured against its own distribution

`[FRED, DGS10 − DGS2, C5; newest print 2026-08-04 — D139, the 08-05 nominal is unpublished]`

| settled | DGS2 | DGS10 | **2s10s** |
|---|---|---|---|
| 07-31 | 4.28 | 4.75 | **+0.47** |
| 08-03 | 4.25 | 4.70 | **+0.45** |
| **08-04** | **4.20** | **4.63** | **+0.43** |

★ **First: it is a BULL flattener, and MACRO does not say so.** Over the three prints **DGS2 fell 8bp and
DGS10 fell 12bp** — the whole curve shifted **down**. This is not the front-end-led bear flattening the
NIM thesis fears; it is a rally in which the long end rallied more. **Per the 08-04 file's §2 regression,
the only names with a statistically significant rate beta are the exchanges/payments/payroll complex and
their LEVEL betas are POSITIVE (CME +26.3 t+4.2, ADP +20.1 t+2.9, SCHW +17.5 t+3.2) — so a falling level
is a headwind for the significant loaders and remains indistinguishable from zero for all 9 banks + KRE +
XLF.** Nothing this run found reverses that.

**Second: the leg carries almost no information, and this is now measured over 273 sessions:**

| statistic | value | reading |
|---|---|---|
| current level | **+0.43** | **14.7th percentile** of the trailing year (range 0.27–0.74, median 0.54) |
| sessions with 2s10s ≤ **+0.20** (S23/S51 kill) | **0 of 273 (0%)** | the line has **never** been touched in a year |
| move required to reach it | **−23bp** | vs an **all-year maximum 5-day flattening of −13bp** |
| P(5-day move ≤ −23bp) | **0 of 268** | **structurally unreachable by 08-07** |
| **base rate of "three consecutive flattening prints"** | **51 of 270 = 18.9%** | **one session in five** |
| conditional on 3-consecutive-down, next 5-day slope change | **mean +0.011 · median 0.000 · 44% flatten further** | **a coin flip** |

⇒ ★★★ **P13‴'s "the direction claim has survived" is true and is worth ~zero bits. A three-print monotone
flattening is a 19%-frequency event whose forward continuation is 44% — indistinguishable from a coin (C4).**
**And the 08-04 file's finding that S23 cannot fire is confirmed on a longer window: 0 of 273.**

### 6c · Which side is the money on

**Neither leg is carrying money in the direction its owner claims.**
- **The rate leg cannot resolve** (0/273 on its kill line; 19%-base-rate direction claim; 44% continuation).
- **The flow leg's headline statistic is instrument-driven** (§1, §2).
- **What is left, and it is the only durable thing:** the **wflow rank-1 (+0.231 even on 3 axes)** and the
  **20–60 session price lead** (§8). ⇒ **The money is on the 40–60 day window and on the mega-caps —
  which is to say it is on the leg the promotion did NOT cite.** ★ **Stated positively: the OW has a
  carrier; it is concentration and 40–60 day relative strength, not breadth and not the curve.**

### 6d · The revision books — the independent axis, and it inverts the tag ranking

`[module_fundamentals_us, all 2026-08-06]` **B2 applied: forward P/E is quoted ONLY beside the
estimate-momentum table; this repo has no margin-percentile instrument (D15), so no name below is called
cheap or expensive — C3.**

| name | tag | CY EPS 90d | **CY 30d breadth** | CY 7d breadth | fwd P/E | note |
|---|---|---|---|---|---|---|
| **GS** | 🟡 flow **+0.095**, RS20 **−0.3** | **+19.2%** | **19↑ / 0↓** | **19↑ / 0↓** | 14.35 | ★★ **the best revision book in the sector belongs to a name the flow file does not light** |
| JPM | 🟢 velocity-lit | +7.6% | 6↑ / 0↓ | 5↑ / 1↓ | 14.34 | |
| WFC | 🟢 velocity-lit | +4.6% | 17↑ / 1↓ | **3↑ / 1↓**, next-qtr **7d 1↑/3↓** | 11.18 | near-book softening |
| BAC | 🟢 velocity-lit | +4.5% | 16↑ / 0↓ | 16↑ / 0↓ | 11.95 | cleanest of the velocity-lit set |
| PRU | 🟢 **volume-lit** | +2.5% | 8↑ / 3↓ | 9↑ / 1↓ | 8.21 | ⚠ panel **0 Buy / 13 Hold / 3 Sell / 2 Strong Sell**, mean target **−11.7%** below price |
| BRK-B | 🟢 velocity-lit | +1.6% | 2↑ / 0↓ | 0↑ / 0↓ | 24.01 | n≈4 panel (S1) |
| MA | 🟢 velocity-lit | +1.3% | 7↑ / 5↓ | 3↑ / 3↓ | 24.70 | breadth at parity |
| **MET** | 🟢 **volume-lit** | **+0.6%** | **5↑ / 9↓** — current-qtr **−6.5%/90d, 30d 2↑/12↓, 7d 0↑/3↓** | 0↑ / 3↓ | 9.15 | ⚠⚠ **the worst book of the eight** |

★★★ **Compose §2b with this row and the surviving breadth shrinks again.** The two greens that survive
removing the velocity axis are **PRU and MET** — and **MET's revision book is the worst of the eight
measured, on exactly the shape Lens 3 tagged EXHAUSTED at AMGN: price-live, KPI-dead.** ⇒ **the
velocity-free breadth is arithmetically 2 names and substantively closer to 1.** ⚠ **MET reports Q2 today,
2026-08-06** `[yfinance calendar; XBRL confirms no 2026-06-30 quarter filed]` — **analysts have cut the
current quarter 6.5% in 90 days into the print.**

⚠ **C2, and it is the strongest thing that can be said for the sector: the revision books are broadly
positive.** Six of eight carry double-digit-count 30-day up-breadth with zero or near-zero downgrades.
**That is a real, independent, non-flow, non-curve leg — and no proposition on this desk owns it.**

---

## 7 · Track KPIs · anti-signals · dated observables

| KPI | State (settled) | Anti-signal, as a dated observable | Date |
|---|---|---|---|
| ★★★ **FIN-VEL — velocity-axis coverage state** | **51/300 today · 0/300 on 08-04 and 08-05 · 51/300 on 08-03.** FIN breadth tracks it 1:1 (0.106 / 0.085 / 0.043 / 0.149) | ⛔ **the next run printing 0/300 coverage will mechanically re-print breadth ≈ 0.04–0.09 with no market event.** ★ **Pre-declared so that print is a second observation, not a first** | **next run** |
| ★★★ **FIN-BREADTH-3AX** — breadth on a homogeneous 3-axis cut | **0.043 (2/47: PRU, MET) — rank 6 of 11** vs published 0.149 rank 1 | **a 3-axis breadth ≥ 0.09 (≥ 4 names clearing OBV 매집 ∧ RS20>0 ∧ `vol_surge` ≥ 1.2) rebuilds the breadth leg on the axis it actually failed** | 08-11 |
| ★★ **XLF exc20 mechanical decay** | **+2.12** at 08-05, of which **+2.02 came from a −1.62 session rolling off the back on 08-05** and only **+0.41** from the tape | ⛔ **on a tape where XLF exactly matches SPY, exc20 decays to +0.52 by 08-12 and turns NEGATIVE (−0.36) at the 08-13 close.** ★ **XLF exc20 still > 0 on 08-13 requires genuine outperformance and is therefore informative; exc20 falling is not** | **08-13** |
| **S65** (owned by ALPHA, re-verified here) | median RS20 {JPM +5.38, BAC +5.22, WFC +0.95, BRK-B +1.59} = **+3.405** ✅ reproduces; ex-BRK-B **+5.219** ✅ | ⚠ **BRK-B reports 2026-08-09, two sessions inside the window.** ★ The median mechanic is n=4 — **removing WFC gives +5.22 identically**, so "BRK-B drags" is estimator, not evidence | 08-11 |
| **P13‴ / S23** — derived 2s10s | **+0.43** (14.7th pct of 1y), **bull** flattener (2y −8bp, 10y −12bp) | ⛔ **S23's ≤ +0.20 is unreachable: 0 of 273 sessions, needs −23bp/5d vs an all-year max of −13bp.** ★ The 08-04 file's **S23-R at ≤ +0.40** (needs −3bp) is inside the distribution and is the only version that can fire | 08-07 |
| ★ **P13‴ information content** (new) | 3-consecutive-flattening base rate **18.9% (51/270)**; conditional next-5d **median 0.000, 44% further flattening** | **a 4th and 5th consecutive print would take the run to a base rate under 5% and start to mean something.** Three does not | 08-07, 08-10 |
| ★★ **MET revision book** — one of only 2 velocity-free greens | **CQ −6.5%/90d · 30d CQ 2↑/12↓ · CY 5↑/9↓ · 7d 0↑/3↓** — worst of the 8 | **Q2 print TODAY 2026-08-06.** A beat with the CY line revised **up** repairs the leg; a miss leaves the velocity-free breadth at **1 clean name (PRU)** | **08-06** |
| ★ **PRU — the one clean surviving green** | `vol_surge` 1.39 · OBV 매집 · RS20 +3.4 · CY +2.5%/90d, 7d 9↑/1↓ | ⚠ analyst panel **0 Buy / 13 Hold / 5 Sell-side-negative**, mean target **−11.7% below price**; fwd EPS $14.60 vs trailing $9.72 with **no margin percentile available (B2/C3)** | 08-11 |
| ★★ **GS — best book, no tag** | **CY +19.2%/90d, 30d 19↑/0↓, 7d 19↑/0↓**; Q2-2026 revenue **$20.34bn, +39.5% YoY**; flow +0.095 🟡, RS20 −0.3 | **the tag and the book disagree by the widest margin in the sector.** Falsifier: CY breadth net-down for two consecutive weeks | 08-11 |
| ★ **KKR knife-edge** | `vol_surge` **1.19** vs the **1.20** gate; sector's **highest** flow score **+0.772**, OBV 매집, RS20 **+10.0** — **not green** | a `vol_surge` ≥ 1.20 print turns the velocity-free breadth from 2 to 3 on a third-decimal move | 08-11 |
| **Rate sign, primary-sourced** | **BAC: lower rates are the OFFSET. GS: lower rates are the DRIVER (NII +68% via interest expense).** FY2025 10-Ks, **8 months stale** | **Q2-2026 segment attribution is `unknown` (C3)** — JPM has no 10-Q in 90 days and the 07-14 8-K exhibit body is not retrievable by this desk's tooling. **A Q3 10-Q with the same BAC wording confirms; the opposite wording retires M138** | 10-13/10-14 |
| **Node 1 — policy rate** | **held 3.50–3.75% on 07-29, three dissents favouring a HIKE** | **the binding constraint (§5 node 2) requires falling funding costs; a hike ends it outright** | NFP 08-07 · CPI 08-12 |
| **FINRA short z** | JPM −0.35 · BAC −1.16 · WFC −0.49 · PRU +0.68 · MET +0.29 · GS +0.08 — **all inside ±1.5** · BRK-B **no data** | **a clean null (C4).** Any name crossing ±1.5 becomes a divergence worth reading | rolling |
| ⚠ **`sector_flow.py` mode guard** (human item) | the 3-axis/4-axis guard at `save_snapshot` is **run-level (`mode`)**, but the axis count that changed is **per-name**; all four runs stamped `"news"` | **stamp the per-name axis count into the snapshot so `new_green` cannot fire on an instrument change.** Needs a human (D37) | standing |
| ⚠ **velocity coverage = mcap rank 1–51** (human item) | exact prefix, no gaps; rank 51 RTX populated, rank 52 C `None`; **cause `unknown` (C3)** | **either extend coverage to the full 300 or exclude the axis from cross-sector breadth comparisons** — as built, breadth is partly a top-51 membership count | standing |

---

## 8 · Verdict on the promotion: does it stand, and on which window

**1 · Which window — measured, not asserted.** `[own calc, XLF vs SPY, settled 08-05]`

| window | 5d | 10d | 20d | **40d** | **60d** | 120d | 250d |
|---|---|---|---|---|---|---|---|
| **XLF − SPY** | **−3.20** | +0.48 | **+2.24** | **+7.59** | **+8.96** | **−0.91** | **−9.62** |

⇒ ★★ **The Financials lead is a 40–60 session object. It does not exist at 5 days, barely exists at 10,
is thin at 20, peaks at 60, and is GONE at 120 (−0.91) and deeply negative at 250 (−9.62).**
**The promotion rides the 40–60 day window. MACRO §G's framing — "the 20-day lead is intact, the 5-day is
not" — names the two windows where the signal is weakest and omits the two where it is strongest.**

**2 · And the 20-day leg is mechanically scheduled to expire.** Decomposing the 20-session window of daily
excesses (sum **+2.12**): **11 positive sessions summing +6.92 against 9 negative summing −4.80**, and
**62% of the positive sum comes from four sessions (07-13 +1.41, 07-28 +1.03, 07-27 +0.99, 07-16 +0.88)**.
**On 08-05 the statistic rose from +0.09 to +2.12 — a +2.02 move of which only +0.41 was that day's tape;
the other +1.62 was a bad session (07-08, −1.62) rolling off the back.** On a tape where XLF exactly
matches SPY, **exc20 → +0.52 by 08-12 and −0.36 at the 08-13 close.**

**3 · The verdict.**

★★ **The promotion to OW stands on a leg the promotion did not cite, and fails on the leg it did cite.**

- ✅ **Stands: mega-cap flow.** wflow **+0.317 published, +0.231 on a homogeneous 3-axis cut, +0.289
  ex-BRK-B — rank 1 of 11 under every removal.** This is the durable statistic.
- ✅ **Stands: the 40–60 session relative lead** (+7.59 / +8.96 vs SPY) — the window the desk is not
  quoting.
- ✅ **Stands: the revision books.** Six of eight names carry 30-day up-breadth with ~zero downgrades, led
  by **GS at CY +19.2%/90d with 19↑/0↓**. **No proposition owns this leg. It is the sector's strongest
  un-instrumented evidence.**
- ❌ **Fails: breadth 0.15 "the highest of 11".** On a homogeneous 3-axis cut it is **0.043, rank 6 of 11**
  — and **that exact number printed on the desk's own 08-05 run.** Industrials, unchanged at 0.100, is
  rank 1 on that cut.
- ❌ **Fails: the five new-🟢 as evidence of ignition.** **JPM, BAC and MA were already 🟢 on 07-31 with the
  same axis lit**; the `new_green` flag fired because the axis blinked off for the two runs the baseline
  came from. **This is an instrument delta.**
- ⚠ **Neither: the curve.** S23 cannot fire (0/273); the three-print flattening is a 19%-base-rate event
  with 44% continuation; the flattening is a **bull** flattener whose only significant beta sits in the
  🔴 exchanges node with a **positive level** sign. **The rate leg does not point either way — it is
  `indistinguishable` (C4), which is a verdict, not a gap.**
- ⚖ **BRK-B: both.** A cap concentration (13.94% of cap, 21.4% of wflow — **M173 stands**) **and** a
  performance drag (underperforms XLF on 6 of 7 windows, −4.57pp/60d, −7.16pp/120d). The two are different
  statistics and do not contradict. **The S65 median mechanic is an n=4 estimator artifact and should not
  be carried as evidence about Berkshire.**

**4 · What I could NOT measure, stated rather than guessed (C3).**
- **Q2-2026 segment attribution for any bank.** No 10-Q inside 90 days for JPM; the 07-14 8-K Item 2.02
  exhibit body is not retrievable by this desk's tooling. §6a rests on **FY2025 filings, 8 months stale**,
  and that staleness is load-bearing for the M138 conclusion.
- **The cause of the velocity axis's on/off flicker and its rank-51 cutoff.** The pattern is measured
  exactly; the mechanism is unknown.
- **Any margin percentile.** D15 / PLAY23 empty ⇒ **no forward multiple in this file is read as a
  valuation** (B2 satisfied by refusal, not by a number).
- **BRK-B FINRA short data** — `no data` returned.
- **W3 restated:** every "real" leg above is a revenue or activity leg. **Real ≠ profitable, and no
  profitability claim is made for any node.**

⚠ **R41 — superlative scope declared.** Every "highest / worst / only / best / rank-N" above is scoped to a
fully-scanned set: **the 47 GICS Financials in `SECTOR_FLOW_US.json` (`asof 2026-08-05`)**, **the 11
sectors / 300 names in the same file**, **the four consecutive `SECTOR_FLOW_US.json` files 08-03 → 08-06**,
**the 273-observation FRED 2s10s series**, or **the 8 names run through `module_fundamentals_us` and named
in §6d.** No superlative ranges over an unscanned universe.
