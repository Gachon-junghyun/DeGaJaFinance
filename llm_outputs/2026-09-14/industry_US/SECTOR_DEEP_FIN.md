# SECTOR_DEEP_FIN — Financials · industry_US · 2026-09-14 (Mon, ~14:45 KST = 01:45 ET, NYSE pre-open) · Stage 8 / L1·DEEP

> **ROTATING TRACK — PREMORTEM-PROMOTED (Lens 1+2).** Verdict in the matrix: **N−**. Last DEEP **2026-09-08 = 2 runs ago**;
> its structure (sub-node split, dispersion test, n=2 regional-bank defect `D579`, `P128` → `P148` succession) is
> **carried by reference** and re-measured here on the 09-11 settled close. Benchmark: `SPY` (named inline, `C1`).
> Price numbers filtered to `index <= 2026-09-11` (`D577`); the sweep is a byte-equivalent reprint of the 09-12 close.
> Analytical output only; no buy/sell/size language (`P4`). Written serially in-context, not as a fan-out — declared.

## 0 · Mandate — one question

*"FOMC + SEP 09-16 14:00 ET and the BoJ (statement ≈ midday JST 09-18 ≈ Thu 09-17 23:00 ET `[WebSearch 09-14]`) land on a
sector whose internal flow split already maps to the mechanism. **Which half of Financials wins a delivered hawkish
hike (level up, curve bear-flattened past a 2nd-percentile 30y−5y = 56.3 bp), and is P&C (`AIG`/`PGR`) a cleaner
expression of that leg than life (`MET` FINRA z +1.95 🔴, `PRU` 🔴)?**"* The book holds `MET` (long) and `NDAQ` (long) —
both sides of the hike. No new brackets are registered; every claim below names the existing row that scores it
(`P151` level 09-16 · `P148` slope 09-17 · `P124` credit/vol 09-18 · `P153` yen 09-21 · `S142`-C already settled).

**Odds, dated `[WebSearch 09-14]`**: CME FedWatch **85.5%** for +25 bp (as of 09-12); Kalshi **57%**, Polymarket **49%**.
The 30-pp gap between futures and prediction markets is itself the P151 story: futures price the *level*, prediction
markets price the *vote* — `SA Asks: How divided will the FOMC vote be next week` `[titles]`. A hike delivered on a
split vote with dovish dots is a live path, not a tail, and it is `P151`-B's mechanism.

## 1 · Sub-industry dispersion — the label is the wrong unit (re-confirmed)

Week = 09-04 → 09-11 (5 sessions), `SPY` −1.15%; 20 sessions `SPY` −1.75%. Equal-weight per group; flow/rs from
`SECTOR_FLOW_US.json`; OBV count = names with `obv_state` accumulating / distributing (C-grade, `D6`; read with RS20/RS60).

| sub-industry | n | mean flow | rs20 | rs60 | OBV acc/dist | week % | week vs `SPY` | 20s vs `SPY` |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| **P&C + multi-line** (`PGR TRV CB ALL HIG AIG`) | 6 | **+0.052** | +1.6 | +6.4 | **2 / 2** | −2.27 | −1.12 | **+1.62** |
| **Life** (`MET PRU AFL`) | 3 | −0.250 | −1.5 | +4.3 | 1 / 2 | −2.64 | −1.49 | −1.44 |
| Insurance brokers (`AON MRSH AJG`) | 3 | −0.424 | −7.1 | +1.1 | 0 / 2 | **−7.81** | **−6.67** | −7.14 |
| Diversified banks (`WFC C BAC PNC TFC JPM USB`) | 7 | −0.149 | −0.3 | +3.0 | 2 / 2 | **−0.61** | **+0.54** | −0.30 |
| Regional banks (`HBAN FITB`) | **2** | −0.453 | −3.6 | −2.0 | 0 / 1 | −0.81 | +0.33 | −3.59 |
| Custody / traditional AM (`STT BNY AMP BLK`) | 4 | −0.199 | −0.5 | +9.7 | 1 / 2 | −1.69 | −0.54 | −0.48 |
| **Alt managers** (`KKR BX APO`) | 3 | **−0.780** | **−10.4** | −3.3 | 0 / 3 | −6.22 | −5.07 | **−10.40** |
| Exchanges & data (`ICE CME NDAQ SPGI MCO MSCI COIN`) | 7 | −0.099 | +2.1 | +0.3 | 1 / 2 | −5.93 | −4.78 | +2.13 |
| IB & brokerage (`GS MS SCHW IBKR HOOD`) | 5 | −0.315 | +3.3 | +2.2 | 0 / 4 | −3.28 | −2.13 | +3.26 |
| Payments (`V MA PYPL XYZ`) | 4 | −0.519 | −1.8 | +11.6 | 0 / 3 | −3.86 | −2.72 | −1.82 |
| Consumer finance (`AXP COF`) | 2 | −0.621 | −4.5 | −2.3 | 0 / 2 | −3.54 | −2.40 | −4.48 |
| Multi-sector (`BRK-B`, top1 13.9%) | 1 | −0.272 | +2.4 | +1.3 | 0 / 1 | +0.44 | +1.59 | +2.43 |

**Dispersion test.** Sector equal-weight week **−3.32%** = **−2.17 pp vs `SPY`**. Name-level σ **2.87 pp**, range
**11.1 pp** (`AJG` −9.88 … `WFC` +1.23); sub-industry means span **8.25 pp** (brokers −7.81 … `BRK-B` +0.44).
σ / |sector excess| = **1.32×**; sub-industry span / excess = **3.8×**; name range / excess = **5.1×**. ⇒ **Dispersion
exceeds the sector move on every metric; "Financials N−" is an average of opposite things and the sub-industry is the
unit** (same finding as 09-08's 50.9× on the eqflow basis — a different metric, same conclusion, `D566`).

**What the split is, stated on the numbers.** The *price* winners of the CPI/hike week are **diversified banks
(+0.54 vs `SPY`), `BRK-B`, and — only relatively — insurers (−1.1/−1.5)**; the losers are **brokers, alt managers,
exchanges, IB** (−4.8 … −6.7). That is a *fee-on-assets / deal-volume / long-duration-equity* complex losing to a
*spread-on-rates* complex — a rates-sensitivity split, not a credit one (`hy_oas` 2.70, `nfci` −0.564, `M1471`).
Flow agrees only in part: P&C is the sole group with positive mean flow, and the OBV accumulators (C-grade; RS20 of
the seven: +3.6 / +4.2 / +1.8 / +15.6 / +1.4 / +0.8 / +5.9 — all positive, so momentum agrees) are `STT WFC C COIN
MET AIG PGR` = **7 by `obv_state`** (the mandate's "9" is not reproduced — §9); distributors = **26**. `D579` stands:
regional banks are n=2, so no regional-bank claim is made.

## 2 · Transmission per sub-industry, tied to the rows that score it

| sub-industry | (i) hike + hawkish dots → `P151`-A (`SHY` ≤ −0.236%) and/or `P148`-A (`IEF−SHY` ≤ −0.3469%) | (ii) hike + dovish dots / no hike → `P151`-B (`SHY` ≥ +0.134%), `P148`-B (≥ +0.2856%) | (iii) BoJ hawkish / carry unwind → `P153`-A (`FXY` ≥ +0.855%) with `P124` |
|---|---|---|---|
| **P&C** | Front-end level up = fastest reinvestment reset in the sector (short-tail liabilities, short asset books, §3). Combined ratio unaffected by the print. **Wins (i)** on the level; indifferent to the flattening | Loses the *incremental* NII story; underwriting engine untouched. Relative loser vs exchanges, absolute loser small | Mostly untouched (USD books); `[unverified]` yen-hedged reinsurance immaterial |
| **Life** | Level up helps new-money yield, **but** bear-flattening (long end up less than front) is neutral-to-negative for the long-duration book and for VII/private-equity marks (`MET` spread 97 bp *below* the 100–120 bp guide on weaker PE in Q2 `[WebSearch]`). **Wins the level, loses the slope** — a half-win | Steepening from the front (front rallies) is the best curve for life; **`P151`-B is the branch that falsifies `MET`'s thesis per the row's own text** — but it is also the curve shape life prefers. Ambiguous by construction; the tell is `[FINRA]` z, not the row | `MET`/`PRU` carry large Japan franchises (share `[unverified]`): a stronger yen is translation-positive, a carry-unwind risk-off widens spreads (`P124`-A `hy_oas` ≥ 2.85). Net sign unknown; `hy_oas` decides |
| **Diversified banks** | NIM widens on the front end while deposit betas lag `[unverified lag]`; a flat curve caps it. **Wins (i)** on level, capped | Loses NIM story; lower funding stress. Neutral | Funding/markets desks: risk-off volumes help, credit widening hurts; `P124` |
| **Custody (`STT BNY`)** | NII on deposits + securities lending; level up helps; `STT` revisions 13:0 up (§5). Wins (i) | Neutral | Vol spike = FX/sec-lending revenue up |
| **Exchanges & data** | **Loses (i)**: duration-of-earnings multiple (NDAQ fwd P/E 19.5) compresses on the level; transaction revenue only helps if vol rises. `NDAQ` z +1.21 trend +9.3▲, `ICE` +0.98 trend **+18.7▲** = shorts building into it | **Wins (ii)**: multiple relief + `SHY` rally. `NDAQ` is the book's *dovish* leg | Vol spike lifts volumes (quad witching 09-18 compounds); `CME`/`ICE` futures desks first, `NDAQ` cash/options second |
| **Alt managers / IB** | **Loses (i)** hardest (already −10.4 rs20; exit/deal math worsens on level) | Wins (ii) | Loses on carry unwind (private-credit marks) |
| **Payments / consumer finance** | Consumer credit sensitivity; `COF` z −1.83 🟢 (shorts leaving) is the one contrary tell | Wins (ii) mildly | Neutral |

**Reading**: (i) is a **spread-complex win, exchange/alt-manager loss** — the book's `NDAQ` is on the losing side and
its `MET` is a half-win. (ii) is the mirror, and `MET` is *not* a clean loser (life prefers a front-led steepening).
**The two holdings are therefore not a hedge pair; they are two different bets on P151, and only one of them (`NDAQ`)
has a clean sign.**

## 3 · P&C vs life — is P&C the cleaner expression? Yes, for the LEVEL leg; life is a slope+credit+PE composite

| | `PGR` | `AIG` | `MET` | `PRU` |
|---|---|---|---|---|
| Earnings engine | Underwriting: combined ratio **87.3** Q2 (86.2 yr-ago), **86.8** July `[WebSearch]` | Underwriting: CY combined ratio **89.0** Q2, −30 bp `[WebSearch]`; NII $1.1 bn vs $1.5 bn yr-ago (cause not read) | Spread + fees: adj EPS $2.43 +20%, adj ROE 17%, **investment spread 97 bp < 100–120 guide (weak PE in VII)** `[WebSearch]` | Spread + fees: adj op EPS $4.08 +14%, op ROE 15.5% `[WebSearch]` |
| Liability duration | short-tail (personal auto ≈ 1 yr `[unverified]`) | short/medium-tail commercial | long-tail (decades) | long-tail |
| Rate sensitivity | **level** (reinvestment on a short book resets fast); slope ≈ irrelevant | level; slope minor | level **and** slope **and** credit **and** PE marks | same as `MET` |
| `[FINRA]` z 09-11 | +0.58 (+5.6▲) | +1.36 (+7.9▲) | **+1.95 🔴** (+4.6▲) | **+2.57 🔴** (short% **83.9** vs base 69.4) |
| Where the shorts are | not here | building | **here** | **here, more** |

**Frame-transfer question, answered explicitly.** *Does a regulated-return / take-or-pay frame apply?* **No.** Personal
auto (`PGR`) is filed-rate regulated at state level, which caps *pricing speed*, not return — there is no allowed-ROE
mechanism and no volume guarantee; combined ratio is earned competitively. Commercial lines (`AIG`) are less regulated
still. Life insurers earn a spread on assets they choose; nothing is contracted like take-or-pay. The correct frame for
P&C is **"short-duration float repriced at the front end + an underwriting margin the Fed cannot touch"**; for life it is
**"a levered long-duration bond fund with a PE sleeve"**. That is why the *hawkish* branch is cleaner in P&C: the hike
hits the one variable P&C is exposed to (the front-end level) and nothing else, whereas for life the same print moves
three variables with mixed signs. **The `[FINRA]` tape independently agrees**: z +1.95 / +2.57 on life, +0.58 on `PGR`.
`AIG` (+1.36, trend +7.9▲) is between — its 🟢 is the sector's only ignition but shorts are building into it. **Within
P&C, `PGR` is the cleaner name on the money axis and on revisions (§5); `AIG` is the cleaner name on multiple (P/B 0.97)
with the worse tape.** No sizing is implied (`P4`).

## 4 · The book's two sides — what each needs

| holding | what it needs | which row scores it | the against-us tell |
|---|---|---|---|
| `MET` (long) | `P151`-A/C **with** `P148` not-A (level up, slope *not* flattening further) **and** `P124` not-A (`hy_oas` < 2.85 on the 09-18 close) **and** PE marks stabilising (unmeasurable until Q3 print, 11-10) | `P151` 09-16 · `P148` 09-17 · `P124` 09-18 | **`[FINRA]` z +1.95 🔴, trend +4.6▲**, and `PRU` at +2.57 says the short is on the *sub-industry*, not on `MET` alone. Card 3 KPI: z back < +1.0 by 09-18; kill if z > +2.5 with OBV flipping |
| `NDAQ` (long) | `P151`-B (dovish surprise) for the multiple; or a vol spike into quad witching 09-18 for volumes | `P151` 09-16 · `P124`-A would be the "vol" path (VIX) | rs20 −4.8, OBV distributing (C-grade; RS20 confirms), z +1.21 with trend **+9.3▲**; revisions 16:0 up (§5) — the fundamentals are fine, the *multiple* is the exposure |

**The book holds the hawkish half-win and the dovish clean-loss.** If `P151` scores C ("hike delivered, nothing learned",
the ≈90% base case by construction), neither holding is resolved by the print — `P148` (slope) and the `[FINRA]` z path
into 09-18 decide instead.

## 5 · Fundamentals table (L2 lens) — margin/ROE percentile `unknown` (module carries no margin history, `C3`)

Revision direction = consensus EPS 90 d ago → now (`eps_trend`); up:down = 30-day revision counts (`eps_revisions`).
"Cheap" is never asserted below without the revision trend beside it.

| name | fwd P/E | trailing P/E | P/B | tgt mean vs last | FY0 EPS 90d | next-Q EPS 90d | up:down FY0 · next-Q | margin/ROE pctile |
|---|--:|--:|--:|---|---|---|---|---|
| `AIG` | 8.6 | 13.7 | **0.97** | 88.5 vs 75.33 | 8.03 → 8.05 (**flat**) | 2.148 → 2.110 (**−1.8%**) | 16:3 · **6:9** (FY+1 **4:12**) | `unknown` |
| `PGR` | 13.4 | 10.9 | 3.68 | 232.0 vs 217.62 | 16.43 → 17.98 (**+9.4%**) | 4.114 → 4.186 (+1.7%) | **18:1** · 10:10 | `unknown` |
| `MET` | 8.9 | 18.6 | 2.26 | 105.1 vs 97.14 | 9.90 → 9.85 (−0.5%) | 2.557 → 2.602 (+1.8%) | 14:0 · 7:2 | `unknown` (adj ROE 17% Q2 `[WebSearch]`) |
| `PRU` | 8.0 | 10.8 | 1.30 | **113.4 vs 119.24 (below price)** | 13.66 → 14.52 (**+6.3%**) | 3.328 → 3.324 (flat) | 12:0 · 8:1 | `unknown` (op ROE 15.5% `[WebSearch]`) |
| `C` | 10.8 | 15.0 | 1.21 | 155.2 vs 138.82 | 10.80 → 11.15 (+3.2%) | 2.500 → 2.332 (**−6.7%**) | 6:0 · **0:8** | `unknown` |
| `STT` | 12.6 | 17.1 | 2.22 | 199.5 vs 193.40 | 12.48 → 13.70 (**+9.8%**) | 3.225 → 3.582 (**+11.1%**) | **13:0** · 9:1 (FY+1 14:0) | `unknown` |
| `NDAQ` | 19.5 | 26.6 | 4.27 | 109.7 vs 91.19 | 3.94 → 4.14 (+4.9%) | 1.044 → 1.083 (+3.8%) | **16:0** · 11:2 | `unknown` |

**Reads.** `AIG` is the sector's lowest multiple (P/B < 1) **with the worst revision mix in the table** (next-Q 6:9,
FY+1 4:12) — the low multiple carries a falling-estimate trend and is not called cheap here. `PGR` is the highest-multiple
insurer with the best FY0 revision trend (+9.4%, 18:1). `STT` (custody, OBV accumulating with RS60 +11.0) has the
cleanest revision profile in the sector (13:0 / 14:0). `NDAQ`'s revisions are 16:0 up — the week's −7.6% is multiple,
not estimates, which is exactly the duration-of-earnings exposure §2 names. `PRU` trades **above** its mean target with
the sector's highest short ratio — the pair is the sub-industry's own "priced" signal.

## 6 · Customers / demand side

- **Insurers**: the "customer" for the asset leg is the rate level and the credit market. `DGS2` 4.56 / `DGS10` 4.95
  (`[FRED]` 09-10), `hy_oas` 2.70, `ig_oas` 0.80, `nfci` −0.564 — new-money yields are at cycle highs with credit shut
  (`M1471`): the best possible reinvestment environment, and the one that `P124`-A (≥ 2.85) would end. The underwriting
  customer is unaffected by the print: `PGR` CR 86.8 July, `AIG` 89.0 Q2 `[WebSearch]`. Title pool: `insurers face surge
  in subsidence claims` (Guardian, UK), `Mortgage lending standards are so tight… sales head for 31-year low` (Fortune) —
  the latter is a consumer-credit/mortgage-volume item that touches banks and `COF`/`AXP`, not insurers `[titles]`.
- **Exchanges**: volumes. **Quad witching + S&P rebalance 09-18** (`P124`/`P149`/`P150` terminal day; SpaceX NDX
  weighting mechanism, Card 5) is a dated volume event inside the window — it favours `CME`/`ICE` (index futures/options)
  before `NDAQ` (cash equities/options/data). A FOMC-driven vol spike is the only path on which `NDAQ` wins *and*
  the level goes up.
- **Dated sell-side events, `[WebSearch 09-14]`**: **Barclays 24th Global Financial Services Conference, NYC, 09-14 →
  09-16** — `SPGI` CFO 09-14 11:15 ET; `FITB` 09-15 07:30 ET; `RGA` 09-15 08:15 ET; `JPM` (Petno, CIB) 09-15 14:45 ET.
  Guidance datapoints from banks/insurers land *before* the FOMC print — a tell for deposit-beta and NII commentary.
  The `POW:CA` slideshow at Scotiabank's Financials Summit `[titles]` is the same week's Canadian analogue.

## 7 · KPIs and anti-signals — dated observables, all on existing rows

| | observable | current | scored by |
|---|---|---|---|
| KPI 1 | `SHY` 1-session 09-15 → 09-16 close | thresholds A ≤ −0.236 / B ≥ +0.134 | **`P151`** 09-16 |
| KPI 2 | `IEF − SHY` 2-session 09-15 → 09-17 | registration state −0.650% = 2.8th pctile (already inside A before the meeting, PREMORTEM 09-12) | **`P148`** 09-17 |
| KPI 3 | `hy_oas` at first `[FRED]` close covering 09-18; `VIXCLS` | 2.70 / 17.84 | **`P124`** 09-18 (A ≥ 2.85 · B ≤ 2.50 & VIX ≤ 15.5) |
| KPI 4 | `FXY` 5-session 09-14 → 09-21 (the BoJ leg) | 89th pctile at registration | **`P153`** 09-21 |
| KPI 5 | `[FINRA]` z on `MET`/`PRU` vs `PGR`/`AIG`, 09-18 close | +1.95 / +2.57 vs +0.58 / +1.36 | Card 3 KPI (no bracket; a description) |
| KPI 6 | Diversified-banks week vs exchanges week (the split) | +0.54 vs −4.78 vs `SPY` | descriptive; `S142`-C already settled the `XLF` aggregate on CPI |
| ANTI-SIGNAL 1 | `hy_oas` ≥ 3.10 on a close 09-15/16 | 2.70 | `P151` VOID clause — then it is a credit event and life is the worse-hit half, not P&C |
| ANTI-SIGNAL 2 | US bank failure / unscheduled Fed action | none | `P148`/`P151` VOID |
| ANTI-SIGNAL 3 | P&C OBV count going 0 accumulating (was 5-of-5 distributing on 09-08; now 2/2) | 2 / 2 | the 09-08 file's ANTI-SIGNAL 2 has **already fired** — §9 |
| ANTI-SIGNAL 4 | BoJ date moved outside 09-14 → 09-21 JST; MoF intervention ≥3 outlets | date **09-17/18 confirmed** `[WebSearch]` | `P153` re-label / VOID |

## 8 · Chain-hop / news velocity

**Unmeasurable.** Remote news dead from 13:19 KST; `chain_hop`, `theme_age`, `thread` cannot run; the local 09-13 pull is
titles only with an uneven per-day denominator. Nothing in this file is a rate; every headline citation is `[titles]`
presence. No "quiet" claim is made anywhere.

## 9 · D48 — asserted then refuted inside this file

1. **The mandate's "9 OBV-accumulating Financials … ~20 distributing"** is not reproduced on `obv_state`: **7 accumulating
   (`STT WFC C COIN MET AIG PGR`) / 26 distributing**. The direction of the split (insurers + banks + custody vs
   alt-managers/payments/consumer-finance/exchanges) is confirmed; the counts are corrected.
2. **The 09-08 DEEP's one "clean node-level fact" — P&C 5-of-5 distributing — has dissolved**: P&C is now 2 accumulating
   (`PGR` obv +0.40 = the sector's highest, `AIG` +0.26) / 2 distributing (`ALL`, `HIG`). Its own ANTI-SIGNAL 2 fired;
   the node is no longer a unanimity, it is the sector's *positive* flow outlier. Stated as a reversal, not smoothed.
3. **"The book holds both sides of the hike"** (Card 3) is refined, not refuted: `NDAQ` is a clean dovish leg; `MET` is
   *not* a clean hawkish leg (§2 — life prefers a front-led steepening on the slope axis). The pair is two bets, not a
   hedge.

## Verdict handed upward (no verdict change; ROTATION holds `FIN N−`)

**A delivered hawkish hike is won by the spread complex — diversified banks, custody, and P&C — and lost by exchanges,
alt managers and IB; life is a half-win (level) / half-loss (slope, PE marks) and is where the shorts are.** P&C is the
cleaner expression of the level leg because it is exposed to *one* variable the print moves; the frame is short-duration
float + an underwriting margin, **not** regulated return or take-or-pay. `MET` needs `P151`-A/C **and** `P148` not-A
**and** `P124` not-A simultaneously, and its `[FINRA]` z +1.95 (with `PRU` +2.57) is the against-us tell to watch into
09-18; `NDAQ` needs `P151`-B or a vol spike into quad witching. Regional banks remain n=2 (`D579`) — no claim.

## ✅ EXIT CHECK
- [x] Dispersion stated (σ 2.87 pp / range 11.1 pp vs −2.17 pp sector excess vs `SPY`; 1.32× / 3.8× / 5.1×) — label is the wrong unit.
- [x] Every "cheap" mention carries the revision trend (§5: `AIG` P/B 0.97 with 6:9 / 4:12 down; margin pctile `unknown`, `C3`).
- [x] Frame-transfer answered explicitly (§3: regulated-return / take-or-pay does **not** apply; the P&C frame is short-duration float + underwriting margin).
- [x] Customers named (§6: rate level + credit for insurers; volumes / quad witching 09-18 for exchanges; Barclays GFS 09-14→16 datapoints).
- [x] Lead/lag claims tagged: deposit-beta lag `[unverified lag]`; liability durations `[unverified]`; Japan share `[unverified]`; combined ratios / spreads `[WebSearch]` dated.
- [x] Chain-hop / velocity: **unmeasurable**, stated; no "quiet".
- [x] No new brackets; every claim mapped to `P151` / `P148` / `P124` / `P153`; `S142`-C cited as settled.
- [x] OBV cited only with RS20/RS60 beside it and labelled C-grade (`D6`); benchmark `SPY` inline (`C1`).
- [x] WebSearch calls: 5 (FedWatch/Kalshi/Polymarket odds; BoJ date; Barclays GFS conference; `AIG`/`PGR` combined ratios; `MET`/`PRU` Q2) — all tagged `[WebSearch 09-14]`.
- [x] Linter: `python -X utf8 scripts/report_lint.py llm_outputs/2026-09-14/industry_US/SECTOR_DEEP_FIN.md` — result appended to `_lint_deep_fin.txt`.
