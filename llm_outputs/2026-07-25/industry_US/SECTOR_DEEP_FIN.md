# SECTOR_DEEP_FIN — Financials · does the Exchanges & Data confirm test have a path? · 2026-07-25 (Stage 6 / L1·DEEP ②)

> **Continuous track, run 4 of 4. Delta-led.** The 47-name map, the six-bucket re-aggregation and the
> customer/counterparty table are carried **by reference** from
> [2026-07-24 SECTOR_DEEP_FIN §1/§5/§6](../../2026-07-24/industry_US/SECTOR_DEEP_FIN.md) and are not reprinted.
> **benchmark: SPY on every RS/excess number in this file** (C1). Flow `asof` **2026-07-24 settled**;
> US markets closed 2026-07-25. Prices re-pulled and measured in this stage, not inherited.
> OBV-derived tags are **C-grade (D6)** throughout. Analytical only.

---

## §0 · Verdict on the mandate, first

**The confirm test has a path, and the path is the calendar rather than the market. The test as
registered is structurally biased toward CONFIRM and cannot answer the question it was written to
answer.**

The registered test is *confirm = ≥3 of 7 cross to positive RS60 vs SPY by 2026-08-08; falsify = ≥4
roll to negative RS20*. RS60 is a rolling window, so between 07-24 and the last settled session
before the deadline (**Fri 2026-08-07**, since 08-08 is a Saturday — **10 trading sessions**) the
window's **base date advances 10 sessions** whether or not a single share trades. I froze every price
and SPY at its 07-24 close and re-computed the same statistic on the 08-07 window:

| | RS60 now | RS60 **frozen** at 08-07 | roll-off carry | relative move vs SPY still needed | next print |
|---|---|---|---|---|---|
| **SPGI** | +0.1 | **+6.14** | +6.02 | −5.77% (has slack) | **2026-07-28** |
| **MCO** | −0.9 | **+4.26** | +5.16 | −4.07% (has slack) | 2026-10-21 |
| **NDAQ** | −2.9 | **+2.91** | +5.79 | −2.82% (has slack) | 2026-10-22 |
| MSCI | −11.2 | −5.23 | +5.93 | +5.50% | 2026-10-20 |
| ICE | −10.5 | −6.44 | +4.03 | +6.86% | **2026-07-30** |
| CME | −13.9 | −10.55 | +3.35 | +11.75% | 2026-10-21 |
| COIN | −22.5 | −24.13 | **−1.58** | +31.65% | **2026-07-31** |

**Three of the seven cross to positive RS60 with zero new information** — exactly the threshold. The
other leg does not carry the same load: the identical freeze on RS20 gives **2 of 7** negative (MCO
−1.12, MSCI −6.79) against the 4 required, with SPGI +1.17 and COIN +1.63 inside a whisker. On
unchanged prices the test reports **CONFIRM, and cannot report falsify.**

Compounding it, **4 of the 7 have no scheduled information event inside the window at all** — NDAQ
printed 07-23; CME, MCO and MSCI do not report until **2026-10-20/21/22**. Two of the three names
that pass on arithmetic (MCO, NDAQ) are precisely names that cannot print.

**The one observable that separates dead cat from turn, dated.** Replace the rolling-level test with
a forward-increment test: **the equal-weight excess return of the 7 names versus SPY accumulated from
the 2026-07-24 close to the 2026-08-07 close.** Positive ⇒ new money, new information. Zero or
negative ⇒ every RS60 crossing that occurs was roll-off and the 60-day de-rate is intact. That
statistic has no mechanical carry, and it is already leaning the wrong way: **the node's excess vs
SPY is −3.00pp over the last 5 sessions**, having peaked on 07-17 (§2).

Stated in the form the evidence supports (C4): whether the node has turned is at present
**indistinguishable** — but the *registered test* is not indistinguishable, it is **broken**, and
that is a finding rather than an absence of one.

---

## §1 · Delta since 2026-07-24

Four items, and nothing else changed enough to print.

1. **SPGI's revision book inverts the mandate's premise.** SPGI is the single name closest to
   crossing (RS60 +0.1 vs SPY) and it has **the worst forward estimate book in the node**: next-year
   EPS **−8.1%/90d** (22.08 → 20.30), next-quarter **−10.0%**, current-year **−3.9%**, breadth
   **0↑:2↓ on both 7d and 30d** for all three forward periods. Its current-quarter line is the only
   positive one (+1.0%, 3↑:0↓ 7d). Per **L2**: SPGI's forward P/E 21.00 is not a cheapness statement
   when the denominator is being cut on every forward period.
2. **CME's Q2 is on file via SEC XBRL and explains its RS60 without any flow argument.** Q2 revenue
   **$1.71B, +1.2% YoY** against $1.69B — and **−9.0% QoQ** from Q1's $1.88B (both halves, C2). Its
   analyst distribution is the node's worst: **2 Strong Sell + 1 Sell** against 5 Strong Buy / 4 Hold.
3. **NDAQ's print is the node's counter-case and it is genuinely strong.** Q2 revenue **$2.53B,
   +20.5% YoY** and **+18.2% QoQ** from $2.14B (C2); current-year EPS **+5.2%/90d**, next-year
   **+5.2%**, current quarter 0.98 → 1.03, breadth 6↑:3↓ (30d) and 1↑:0↓ (7d) — the only unambiguously
   rising book among the four names that cannot print again before the deadline.
4. **ICE's headline upside verifies, its book does not.** Mean target $181.93 vs $145.79 =
   **+24.8%** (confirmed). Against that: current-quarter EPS **−7.3%/90d** on **0↑:2↓ (30d)** and
   **0↑:1↓ (7d)**; current-year +0.2%, next-year −0.0%. A 24.8% target gap on a flat-to-falling book
   is a target-staleness reading, not an upside reading.

COIN is a separate object and should stop being counted with the other six: current-quarter EPS
**−100.4%/90d** (0.54 → −0.00), current-year **−60.7%**, breadth 0↑:2↓ (30d). Its required relative
move (+31.65%) is not a test outcome, it is a coin flip on crypto volumes.

---

## §2 · The mirror-image shape — one rotation, seen from both ends

Exchanges hold the sector's top 20-day flow (+0.556) and its worst RS60 vs SPY (−8.9). Investment
Banking & Brokerage holds the bottom flow (+0.009) and the best RS60 vs SPY (+10.9, and all five
members positive: IBKR +14.6 · HOOD +11.8 · GS +10.7 · MS +8.8 · SCHW +8.4). This is not two facts.
It is one rotation cut at a single date.

Splitting the 60 sessions into halves, mean excess vs SPY:

| node | sessions −60..−21 | sessions −20..−1 |
|---|---|---|
| Exchanges & Data (7) | **−18.08** | **+11.21** |
| Money-centre / IB (GS,MS,JPM,C,WFC) | **+8.10** | **−1.52** |

The equal-weight **Exchanges-minus-IB** spread troughed on **2026-06-25 at −24.15%**, recovered
+9.59pp to −14.56% by 07-24 — and **peaked on 2026-07-17 (−11.92%), giving back 3.00pp in the five
sessions since.** So the "top flow" at one end and the "bottom flow" at the other are the same
capital moving back the way it came, from a turn dated 06-25, and that move is already decelerating.

**Which axis I believe, and why (D6).** The flow scores are OBV-derived and therefore **C-grade**;
they may corroborate and may not carry a proposition. Stripped of them, the conflict is not C-vs-A —
it is **RS20 against RS60, both A-grade momentum**. The tiebreak is inside D6's own table: the only
momentum cell that **had power** is **12-1 / mom5 (LR 0.880, shuffle p = 0.001, 39,290 obs)** — a
long-horizon "losers keep losing" result. There is no comparable powered result on a 20-day
reversal. **So I weight RS60 over RS20, and read the exchange node's 20-day inflection as a bounce
inside an intact de-rate until a forward-increment test says otherwise.** The OBV 매집 tag on six of
seven exchange names is recorded here as agreeing with RS20 and disagreeing with RS60, and it decides
nothing.

The corroborating asymmetry is in the books, which are A-grade-independent: **GS replicates for a 4th
consecutive run** — current-quarter **+17.7%/90d on 8↑:0↓ (30d)** and **5↑:0↓ (7d)**, current-year
**+19.5%/90d on 9↑:0↓**, next-year +12.6% on 9↑:0↓ — while its price excess vs SPY is **−0.99 over 20
days**. Consensus is upgrading GS hard into a flat tape. The exchange node has nothing of that shape;
only NDAQ's +5.2% comes close, and MCO (+1.0% CY), MSCI (+0.2%), CME (+0.3%) are flat books.

**W4 — who pays this node.** Four different payers under one label: venue/volume (NDAQ, ICE, CME) is
paid per contract by broker-dealers and hedge funds — NDAQ disclosed it directly (record Market
Services $340M, Index ETP AUM through $1 trillion, 26 IPOs raising $106B incl. SpaceX at $86B; M107
carried); ratings (MCO, SPGI) is paid by **corporate debt issuers**, so its driver is gross issuance
volume, which §4 bears on; index/analytics (MSCI) is paid by asset managers on subscription plus ETF
AUM; COIN on crypto volumes. **Disclosed-spend checks inside the test window: SPGI 07-28 and ICE
07-30 only.** CME/MCO/MSCI cannot be checked before 2026-10-20 — recorded as unknown (C3).

---

## §3 · TRV's EXHAUSTED tag — partly upheld, and the pre-mortem's own statistic is the weakest part of it

**Verified independently:** 60-day excess vs SPY **+21.34**, 20-day excess **+21.04** → **98.6%**,
reproducing the pre-mortem exactly. Mean target **$355.50** vs $387.26 = **−8.2%**. Current-year EPS
moved 28.63 → 34.01 in **one week (+18.8%)** = one print, **n≈1 (S1)**.

**But the 98.6% is an artifact of cancellation, not concentration.** In three 20-session blocks of
excess vs SPY: last 20 **+21.04**, middle 20 **≈ +9.89**, oldest 20 **≈ −9.59**. TRV earned excess in
*two* of three blocks; the ratio only reaches 98.6% because the middle gain and the oldest loss nearly
annihilate. Its 40-day excess is **+30.93**, *larger* than its 60-day. A statistic that blows up
whenever its denominator shrinks toward zero is not a concentration measure — the same column prints
**10,916% for SPGI** and **−624% for NDAQ**.

**The real n≈1 is a day, not a window.** On **2026-07-17** TRV outperformed SPY by **+10.21pp in one
session** — 48.5% of the entire 20-day excess in one print. That is the S1 objection stated correctly.
Against it: the node kept earning *after* the print (+2.39 on 07-23, +2.79 on 07-24, **+5.54 over the
last 5 sessions vs SPY**), which is follow-through rather than fade.

**The breadth claim is a period-selection artifact (C5).** "2↑:1↓ (30d) → 0↑:1↓ (7d)" is the
**current-quarter** line — the one period already superseded by the 07-17 print. On the three forward
periods the 7-day breadth is **1↑:0↓, 1↑:0↓, 1↑:0↓** (next-quarter, current-year, next-year), and
30-day is 3↑:0↓, 2↑:0↓, 2↑:1↓. Quoting only the stale line reverses the sign of the reading.

**A stronger bear case exists and it is the one to carry (L2).** TRV's forward P/E is **12.88** —
cheap-looking — but consensus current-year EPS **34.01 falls to 30.04 next year, −11.7%**. The
denominator is being marked as this year's peak by the same analysts. Put that next to M106 (carried):
Chubb's Evan Greenberg on the record that softness "*[has] begun to extend beyond property into more
casualty lines*," with NA commercial rate **−1.4%**, property **−6%**, major account & specialty
premiums **−9%**. **Adjudication: the EXHAUSTED tag stands, but on the peak-earnings/soft-pricing
argument, not on the 98.6% statistic or the breadth line — both of which do not survive
re-measurement.** The C-grade corroborant agrees (TRV flow delta **−0.111**, the sector's second-worst,
against RS60 +21.1 vs SPY) and does not carry it (D6).

---

## §4 · The rate leg — what S23's bear-flattener does to NIM, from the banks' own Q2 disclosures

S23 (DGS2 held inside 4.15–4.45% and T10Y2Y ≤ +0.20 by 08-05) is a **funding-cost** event before it
is a spread event, and the transmission channel is already disclosed and already visible:

- **WFC (Q2, 07-21)** — NII **$12.32B, +5% YoY**, a **miss** against the $12.38B consensus, and the
  stock fell ~3% on a quarter that beat on revenue ($22.62B, +8.6% YoY), EPS ($2.00 vs $1.71) and
  ROTCE (17.7%, +250bp). **FY2026 NII guidance held UNCHANGED at ±$50B** (~$48B non-markets + ~$2B
  CIB) against a $50.1B street number. CFO Santomassimo named the mechanism: growth in
  **interest-bearing** deposits, and "*financing balances in the markets business are lower spread*."
- **JPM (Q2, 07-14)** — record net income **$21,155M**, diluted EPS **$7.70**, and FY2026 NII
  guidance **raised to ~$105.5B**, explicitly attributed in part to **markets-related** NII.

Those two guides look opposed and are not. **Both banks' NII is increasingly earned on
markets/financing balances rather than on deposit spread.** A 2-year pinned at 4.15–4.45% is exactly
the configuration that keeps pulling non-interest-bearing deposits into CDs and money funds, so
S23 hits the **spread half** of the NII book — the half WFC just missed on and guided flat — while
leaving the **markets half** intact, which is the half that is growing and the half that belongs to
GS/MS/SCHW/IBKR. That is the same split §2 measured in prices, arriving from the income statement.

**And it reaches the exchange node.** Ratings revenue (MCO, SPGI) is paid on gross debt issuance. A
flattener that holds the front end high without letting the long end fall keeps all-in corporate
coupons high, which is an issuance headwind — a plausible mechanism for SPGI's −8.1% next-year
revision. Marked **`[inferred]` — no lag table has been run (W2)**, and it must not be cited as
evidence until one is. **First check: SPGI 2026-07-28.** The steepener (R11) is retracted and is not
used anywhere above.

**S26 verified, with the window exposed (C5).** Regressing daily returns on SPY, the handed betas
replicate **only at a ~500-session window**: JPM **0.927** (claim 0.932) · XLF **0.784** (0.789) ·
CB **0.128** (0.125) · TRV **0.337** (0.339). On the 120-session window the same regressions give
**JPM 0.691 · XLF 0.560 · CB −0.452 · TRV −0.244** — CB and TRV flip sign. **The directional claim
survives and strengthens on the recent window**: the FIN OW does carry an internal low-beta leg its
label hides, and on recent data that leg is an outright negative-beta hedge. The *magnitudes* are
window-dependent and should always be quoted with the window attached.

---

## §5 · Dispersion and the grouping choice, exposed (W5 / C5)

**Grouping used:** the flow file's own GICS sub-industry field, unmodified — 12 groups over n=47.
Chosen because it is the field the mandate's node was defined in, so any re-cut would answer a
different question than the one asked.

**Dispersion (W5), with the ratio.** Sub-node mean RS60 vs SPY: Insurance **+9.53** · IB & Brokerage
**+6.46** · Payments **+5.60** · Exchanges & Data **−8.82**. The spread **of the means is 18.35pp**.
XLF's own 60-day move is **+8.98% absolute / +4.89 vs SPY**. Ratio: **2.04× the sector's own absolute
move, 3.75× its excess.** Across the 23 names the RS60 range is **43.89pp** (TRV +21.34 to COIN
−22.54), sd 10.04. **The sector label is the wrong unit of analysis and this file says so; "Financials
OW" describes no single object.**

**The arbitrary choice that is load-bearing (C5).** "Financial Exchanges & Data" bundles **four
distinct revenue engines**. Split them and the node's −8.9 decomposes into: **venue/volume (NDAQ, ICE,
CME) −9.08 · ratings (MCO, SPGI) −0.39 · index/analytics (MSCI) −11.16 · crypto brokerage (COIN)
−22.54.** The de-rate is essentially **absent from the ratings pair**. And the two names that clear
the confirm test on roll-off alone without a possible print — **MCO and NDAQ** — sit in the two
buckets that either never de-rated or already reported well. **A test defined on the 7-name label
would report a node-wide turn that, decomposed, is one bucket that never fell.** This is the same
failure that got the prior run's "payments concentration" claim rejected (a 7-name node hiding inside
a 17-name residual); flagged here before it is repeated, not after. Effect of the alternative
grouping: the mandate's confirm test **loses its meaning entirely** under the 4-way split, because no
sub-bucket then has enough members for a 3-of-N threshold.

---

## §6 · Track KPIs and anti-signals — dated observables

| # | Observable | Date | Confirms | Falsifies |
|---|---|---|---|---|
| K1 ★ | **Equal-weight excess return of the 7 exchange names vs SPY, 07-24 close → 08-07 close** (the replacement for the broken RS60 test) | **2026-08-07** | > 0 ⇒ new money; the 20-day inflection is information | ≤ 0 ⇒ every RS60 crossing was roll-off; the de-rate is intact |
| K2 | **SPGI Q2 print** — the only in-window disclosure from a name at RS60 ≈ 0 with a −8.1% next-year book | **2026-07-28** | Guide raise + next-year breadth turning ↑ | Another cut ⇒ the node's best RS60 name is de-rating on fundamentals, not multiple |
| K3 | **ICE Q2 print** — 0↑:2↓ (30d) current-quarter book against a +24.8% mean-target gap | **2026-07-30** | Book turns up ⇒ the target gap is real | Book cut again ⇒ the gap was stale targets |
| K4 | **FOMC + DGS2/T10Y2Y (S23)** — bear-flattener hold | **07-29 → 08-05** | DGS2 in 4.15–4.45% **and** T10Y2Y ≤ +0.20 ⇒ spread-NII leg impaired without tripping any prior threshold | DGS2 out of the band or T10Y2Y > +0.20 ⇒ S23 does not fire |
| K5 | **V (07-29) and MA (07-30) prints (S14)** — MA's current-quarter book is **0↑:1↓** with CY EPS **+0.4%/90d**, i.e. flat, against RS20 +9.7 vs SPY | **07-29 / 07-30** | Both beat + guide ⇒ payments breadth is earnings-backed | Either guides down ⇒ the FIN OW's surviving breadth leg is the thing that broke |
| K6 | **TRV — no print until 2026-10-15.** Nothing can confirm or falsify the peak-earnings read for ~12 weeks | **2026-10-15** | CY 34.01 held and next-year 30.04 revised **up** | Next-year revised further down ⇒ L2 peak-earnings confirmed |
| A1 | **Anti-signal — an 08-08 "CONFIRMED" headline.** Per §0 this prints on unchanged prices | 08-08 | — | Treat a bare RS60 crossing count as **no evidence** unless K1 is also positive |
| A2 | **Anti-signal — COIN counted inside the node.** −100.4%/90d current-quarter, β ≈ 3.0 | ongoing | — | Any node statistic that moves materially when COIN is dropped is a COIN statistic |
| C3-unknown | **CME · MCO · MSCI have no disclosure before 2026-10-20/21/22.** Their contribution to any 08-08 verdict is **`[blank]` — unknown, not neutral** | — | — | — |

---

## ✅ EXIT CHECK

- [x] **§0 answers the narrowed mandate first, with a measurement**: the path is **roll-off** — 3 of 7
      cross on frozen prices while the falsify leg reaches only 2 of its 4. Both legs measured; the
      dated separating observable is named (**K1, 08-07**).
- [x] **Delta-led**; the 47-name map, six-bucket re-aggregation and counterparty table carried **by
      reference** to 2026-07-24, not reprinted.
- [x] **C1** benchmark **SPY** declared in the header and named at every excess/RS claim · **C2** both
      halves cited (NDAQ +20.5% YoY / +18.2% QoQ; CME +1.2% YoY / −9.0% QoQ) · **C3** CME/MCO/MSCI have
      no in-window disclosure and are recorded `[blank]`, never guessed · **C4** the node's turn is
      written **indistinguishable** — what is rejected is the *test*, not the hypothesis.
- [x] **C5** — grouping stated (flow file's own GICS sub-industry, 12 groups / n=47) **and the
      alternative's effect measured**: the 4-way split leaves ratings at −0.39 and dissolves the 3-of-7
      threshold. Beta-window choice also exposed (500 vs 120 sessions; CB/TRV flip sign).
- [x] **D6** — RS60 (A) weighted over the OBV-derived flow tags (C); the OBV 매집 reading on six of
      seven exchange names is reported as agreeing with RS20 and disagreeing with RS60 vs SPY, and
      decides nothing. The RS20-vs-RS60 tiebreak is resolved on D6's own powered 12-1 cell.
- [x] **L2** — SPGI fwd P/E 21.00 vs −8.1% next-year; TRV fwd P/E 12.88 vs CY 34.01 → 30.04 (−11.7%) ·
      **S1** TRV's one-week +18.8% book move and the 07-17 **+10.21pp single session** tagged n≈1 ·
      **W2** the issuance→ratings channel tagged `[inferred]`, no lag table, not cited as evidence.
- [x] **W4** four payer groups named, spend checks dated (SPGI 07-28, ICE 07-30), the three uncheckable
      names given their October dates · **W5** dispersion with the ratio (18.35pp of sub-node spread =
      **2.04×** XLF's own 8.98% 60-day move) and the label called the wrong unit.
- [x] **Pre-mortem: all three adjudicated** — TRV EXHAUSTED **upheld on a different argument** (§3);
      S23 traced to WFC's and JPM's own Q2 NII disclosures (§4); S26 **verified and strengthened**,
      window exposed (§4).
- [x] **R11 (retracted steepener) not cited as evidence anywhere.** No sizing, no buy/sell language (P4).
