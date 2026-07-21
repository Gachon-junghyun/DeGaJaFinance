# SECTOR_DEEP_FIN — Financials (FIN) deep-dive · 2026-07-17 (Fri)

> Stage 5 / L2 DEEP. CONTINUOUS track — FIN was deep-dived 2026-07-15
> (`llm_outputs/2026-07-15/industry_US/SECTOR_DEEP_FIN.md`, referenced throughout as **[07-15]**).
> Re-picked on **today's rank**, not continuity (ROTATION §3): #2 flow rank, **eqflow 0.279 > wflow
> 0.181 = breadth-led**, #1 news bucket (2,759→3,643 hits/7d), the strongest AGREE on the 11-sector
> board, and upgraded on quality by PREMORTEM lens 3 (XLF RS60 only +1.9% = early, not extended).
> **Zero buy/sell calls — analytical map only** (P4). Unchanged structure carried BY REFERENCE, not
> re-printed; effort spent on the 2-day delta below.

---

## §1 — DELTA vs 07-15 (lead with this)

**1. The curve leg got objectively stronger.** 2s10s **+36bp → +42bp** [FRED, asof 07-15]. 10Y eased to
4.55% (from 4.62 on 07-13) while 2Y fell faster (4.18→4.13) — the front end is doing the steepening, not
a long-end selloff. Real 10Y holds at 2.32% (+42bp/120d). This is the single cleanest "still firing" fact
in the whole book [MACRO_REPORT §1].

**2. The [07-15] data gap is resolved — and what it revealed is not comfortable.** [07-15] flagged RS20/
RS60/RSI/Bollinger as NaN for all six FIN names (yfinance gap). This run they resolved, and the two
verbatim chart reads below are the sharpest new finding of this DEEP:

```
SCHW — module_chart --read (2026-07-17)
OBV: 분배(매도압력↑) (20d기울기 -16%)
다이버전스: 없음
MA정렬: 혼조 · 가격 4/4 MA 위
볼린저: 확장 21.2% · 중단
RSI: 86.9 · 모멘텀20d +8.8%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 89.44
```
*Read: RSI **86.9** is extreme-overbought territory, and OBV has flipped to **distribution** (20d slope
−16%) even though price sits above all four MAs. This is the technical signature of a name that has run
into its own binary (07-21, D-4) already priced for perfection — structurally the same setup ("high bar")
that just broke TSM.*

```
PNC — module_chart --read (2026-07-17)
OBV: 중립 (20d기울기 +10%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 4/4 MA 위
볼린저: 수축(코일링) 11.9% · 중단
RSI: 65.2 · 모멘텀20d +9.5%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 232.04
```
*Read: RSI 65.2 is elevated but nowhere near extreme; Bollinger is **coiling** (contraction, 11.9%) — a
consolidation, not a blow-off top; MA stack fully bullish and OBV neutral (mild accumulation, +10%
slope). PNC's setup is healthy and has room; SCHW's does not. This is a materially different technical
state between the two names carrying the same "FIN OW" label.*

**3. PYPL's 🟢가속 tag is now RESOLVED — and it resolves OUT of the FIN-OW thesis, not into it.** The DEEP
brief flagged PYPL as ⚠CAUTION/pending-KPI-confirm with "no PYPL-specific catalyst found." Extended search
this run found it: **Stripe and private-equity firm Advent International offered ~$53B ($60.50/share) to
acquire PayPal, reported 07-15** [Reuters via multiple outlets, Yahoo Finance 07-15: *"PayPal Soars 19% on
a Reported $53B Stripe-Advent Takeover Offer"*; *"PayPal has its best day ever"* [Yahoo 07-15]]. As of
07-17, *"PayPal board views $53B Stripe-Advent takeover bid as inadequate"* [SeekingAlpha/Reuters 07-17] —
the situation is live and unresolved, with sell-side split on whether the bid undervalues the franchise
(*"PayPal: $53 Billion Is A Such A Lowball Offer It Has To Go Up"* [SA 07-16] vs *"A Bargain For Stripe, A
Bad Deal For Shareholders"* [SA 07-15]). **This is idiosyncratic M&A-arbitrage optionality, not a
bank-earnings or curve signal.** PYPL's RS20 +29.9% / vol surge 1.83x (the largest on the board) should be
**excluded** from any read of FIN-sector breadth momentum — it is a single-name deal catalyst that happens
to sit in the Financials GICS bucket, not evidence the OW thesis is broadening. (us_flow short-vol z is
mildly elevated at +0.71 — consistent with ordinary merger-arb short interest building against the deal
spread, not a bearish tape read.)

**4. Fresh earnings prints since [07-15]:** **BNY (07-15)** — *"Bank Of New York Mellon: Digging Into
Back-To-Back Record Quarters, Hiking My Target"* [SeekingAlpha 07-15]; **dividend hiked 19% to
$0.63/share** [PRNewswire/SA 07-15]. This is a genuine earnings-leg confirmation for BNY's 🟢가속 tag (RS20
+11.3%, RS60 +12.9%, the best RS60 of the FIN shortlist) — unlike PYPL, BNY's flow is validated by an
actual beat-and-raise, not deal speculation. **First Horizon (FHN, 07-15)** — Q2 net income $260M (+12%
YoY), EPS $0.54 (+$0.09 YoY) [PRNewswire 07-15]; management guides ~10% standardized RWA reduction while
holding CET1 ~10.5% [SA earnings-call insights 07-15] — a capital-discipline signal, regional-bank
confirmation. **M&T Bank (MTB, 07-15, carried)** — GAAP EPS $5.32 beat by $0.66 [SA 07-15], but *"M&T Bank
Q2 Review: Slow Growth But Solid Credit Quality"* [SA 07-15] — the beat coexists with a soft-growth
framing, an early beat-but-fade tell at the regional level.

**5. The beat-but-fade risk is confirmed live, not hypothetical.** *"Bank of America's stock falls
**despite** blockbuster earnings report"* [MarketWatch 07-14]; *"Big Banks Smash Earnings Records, but
'Tectonic' Risks Loom"* [NYT 07-14]. And predating the run-up: *"Financials sector is overheated as big
names prepare to release earnings reports — analysts"* [SeekingAlpha 07-10] — an overheating call made
**before** the current leg, now looking directionally early but not wrong. One buy-side data point in the
same direction: ClearBridge Value Strategy's Q2 2026 letter states *"We also exited Charles Schwab
(SCHW)... In Schwab..."* [SeekingAlpha 07-15] — a value manager trimming SCHW specifically, timing
unclear (valuation vs event-risk), logged as a soft sentiment data point, not a KPI.

**6. Kill-switch proximity:** none of the track-KPIs from [07-15] have fired (§7). The nearest is now
**SCHW's own chart** (RSI 86.9) rather than a macro or credit variable — the anti-signal moved from
"watch the curve" to "watch the name walking into D-4."

---

## §2 — Flow cross-check

**module_flow** `SCHW PNC PYPL BNY XLF --bench SPY` (news 7d/30d) [flow, 2026-07-17]:

| Ticker | Tag | OBV | RS20 | RS60 | Vol surge |
|---|---|---|---|---|---|
| SCHW | 🟡중립 | 매집 | +9.7% | +4.4% | 0.70x |
| PNC | 🟢가속 | 매집 | +8.7% | +6.5% | 1.24x |
| PYPL | 🟢가속 | 매집 | +29.9% | +4.3% | 1.83x |
| BNY | 🟢가속 | 매집 | +11.3% | +12.9% | 1.26x |
| XLF | 🟡중립 | 매집 | +4.4% | +1.9% | 0.98x |

**us_flow.py** — FINRA Reg SHO short-vol Z (asof 2026-07-16) [flow]:

| Ticker | Short% | Base20 | Z | 5v5 | Verdict |
|---|---|---|---|---|---|
| SCHW | 31.4% | 35.4% | **−0.42** | +8.8▲ | 🟡 normal (short interest ticking UP into the print) |
| PNC | 42.8% | 48.4% | **−0.62** | −6.3▼ | 🟡 normal — still the only ✅ clean-rise on the board |
| PYPL | 52.6% | 48.4% | +0.71 | −2.8▼ | 🟡 normal — merger-arb short building, expected for a deal target |
| BNY | 55.7% | 46.6% | +0.60 | +5.7▲ | 🟡 normal |

No short-vol Z crossed the ±1.5 spike/exit threshold — no divergence-vs-narrative tell fired this run.
**Read:** flow confirms the [07-15] two-track split still holds — PNC remains the single cleanest
accumulation signature in FIN (OBV 매집, shortZ most negative, technicals coiling not extended). SCHW's
flow tag is unchanged (🟡중립) but its short-vol trend (+8.8▲ into a 5-day window) plus the chart's RSI
86.9/OBV-distribution (§1) is the first negative-divergence signal against SCHW specifically — narrative
(binary catalyst, "high-bar" framing in the news) and tape (short interest rising, momentum
overbought) are now pointing the same cautious direction, which is itself the tell.

---

## §3 — Players (large-cap universe UNION thematic small-caps)

**Large-cap universe** — all 47 Financials-GICS names in `SECTOR_FLOW_US.json` (us_top300, asof 07-16),
by sub-leg, flow-ranked within each:

| Sub-leg | Names (flow-ranked) |
|---|---|
| **Payments/transaction processing** | **PYPL** (1.00, 🟢가속 — M&A, see §1) · XYZ/Block (0.606) · **MA** (0.517) · **V** (0.506) |
| **Regional/diversified banks** | **PNC** (0.80, 🟢가속) · USB (0.617) · FITB (0.60) · TFC (0.578) · HBAN (0.557) · **JPM** (0.511) · WFC (0.294) · BAC (0.293) · **C** (−0.468, 🔴분산) |
| **Asset mgmt / custody banks** | **BNY** (0.651, 🟢가속) · STT (0.516) · AMP (0.324) · BLK (−0.035) · BX (−0.04) · KKR (−0.067) |
| **Insurance (P&C, life, multi-line)** | TRV (0.65) · PRU (0.578) · CB (0.524) · MET (0.464) · PGR (0.443) · ALL (0.424) · AIG (0.321) · HIG (0.181) · AFL (0.052) |
| **Insurance brokers** | AJG (0.522) · AON (0.506) · MRSH (0.108) |
| **Consumer finance** | COF (0.494) · AXP (0.291) |
| **Investment banking / brokerage** | HOOD (0.544) · **SCHW** (0.50, 🟡중립) · MS (−0.04) · GS (−0.278) · IBKR (−0.558) |
| **Financial exchanges / data** | NDAQ (0.506) · MCO (0.494) · SPGI (0.384) · MSCI (0.335) · ICE (−0.144) · COIN (−0.395) · CME (−0.79, 🔴분산) |
| **Diversified holding** | BRK-B (−0.483) |

**Thematic small/mid-cap union** (named ≥2x in this run's news window, real ticker, mcap ≥$2B, not in the
top-300 table above):
- **First Horizon (FHN)** — Memphis regional bank, Q2 2026 net income $260M (+12% YoY), EPS $0.54
  [PRNewswire 07-15]; named across 6 items (earnings call transcript, SA analysis, 8-K) [module_news_data,
  fts, 5d].
- **M&T Bank (MTB)** — GAAP EPS $5.32 beat by $0.66, revenue $2.53B beat by $70M [SA 07-15]; named 6x
  across news window incl. 8-K filing.

Both are confirmatory regional-bank prints that sit outside the us_top300 large-cap table but reinforce
the same NIM/curve read as PNC/USB/FITB/HBAN inside it — no new sub-leg, no divergent signal.

---

## §4 — IR anchor (primary filings — NEW this run: SCHW; JPM carried by reference from [07-15] §3)

`module_business_us SCHW --full --json` → **10-K, accession 0000316709-26-000009, filed 2026-02-25,
period 2025-12-31** [filing]:

- **Business** — Charles Schwab Corporation (CSC) is a savings-and-loan holding company operating through
  three principal subsidiaries: **Charles Schwab & Co. (CS&Co)**, a securities broker-dealer (est. 1971);
  **Charles Schwab Bank, SSB (CSB)**, the principal banking entity; and **Charles Schwab Investment
  Management (CSIM)**, advisor to Schwab Funds/ETFs. At 2025-12-31: **$11.90T client assets, 38.5M active
  brokerage accounts, 5.7M workplace-plan participant accounts, 2.2M banking accounts** [filing].
- **Item 1A risk taxonomy, the load-bearing lines for this DEEP's question:** *"The monetary policies of
  the Federal Reserve... can affect our financial results, including **net interest revenue and bank
  deposit account fees**"* [filing]. This is the mechanism-level answer to §8's earnings-vs-curve
  question: **SCHW's own 10-K names net interest revenue (a curve-sensitive line) and deposit account
  fees as directly Fed-policy-exposed** — SCHW's 07-21 print is therefore not a pure "earnings" test
  cleanly separable from the curve; it is a hybrid, because a large share of Schwab's revenue base is the
  spread on client cash sweep balances. Also flagged: risk from *"higher or lower client cash
  balances"* on capital requirements and liquidity — the same client-cash-sorting dynamic that drove
  Schwab's 2023 stress episode.
- **Competitive scope (Item 1)** — competes across brokerage, wealth management, and asset management with
  banks, trust companies, fintechs, and retirement-service providers (Investor Services); institutional
  custodians, wirehouses, and fintech custodians (Advisor Services). Competitive advantage cited: scale
  (amortizing costs over $11.9T client assets).

`module_disclosure_us SCHW` → **62 filings/90d, 5 8-K, 0 in Item 2.02 (earnings) / Item 7.01 (guidance) /
M&A categories** [filing]. **This directly confirms the binary is still live and unfired**: no earnings
8-K has been filed yet — the 07-21 print is genuinely ahead, not already in the tape. 30 of the 62 filings
are Form 4 insider transactions (routine, not concentrated in any pre-earnings pattern worth flagging).

JPM 10-K anchor (Item 1A credit/market/capital risk taxonomy) carried by reference from [07-15] §3 —
unchanged this run.

---

## §5 — Value-chain node map (carried by reference from [07-15] §2/§4 — unchanged; one node note)

```
deposit franchise ─▶ NIM / curve ─▶ loan growth & credit quality ─▶ capital-markets/trading ─▶ fee income ─▶ capital return
   (deposit beta)     (2s10s +42bp)      (★ CREDIT COSTS ★)          (risk-on harvest)         (AWM/cards)     (regulatory-capital gated)
```
Sub-leg map, bottleneck (credit costs/provisions), and steepening-beneficiary ranking are **unchanged from
[07-15] §2/§4** — regionals remain the cleanest NIM/curve lever, capital-markets remain the leg that
delivered the realized catalyst, credit costs remain the binding constraint. 2s10s strengthening
(+36bp→+42bp) reinforces the existing chain; it does not add a node.

**Node note (new, not a structural change):** the **PYPL M&A special-situation** (§1.3) sits **outside**
this value chain entirely — it is not payments-volume growth, not NIM, not capital-markets activity. It is
a corporate-control event. Treating it as part of the "payments" sub-leg's organic momentum would
mis-attribute an M&A premium to the FIN-OW's operating thesis. Logged, not mapped into the chain.

---

## §6 — chain-hop candidates (body-proximate only; flow cross-checked before promotion)

`module_news_data chain-hop "bank earnings" "NIM steepener" --days 14 --scope foreign` [chain-hop, 40
articles scanned]:

| Ticker | Body-proximate mentions | Headline mentions | Example article |
|---|---|---|---|
| **GS** | 7 (13 body total) | 0 | *"SpaceX & Google will boost big bank earnings, but can the AI-driven supercycle really last"* |
| **WFC** | 7 (11 body total) | 0 | *"Financials sector is overheated as big names prepare to release earnings reports — analyst"* |
| **C** | 7 (11 body total) | 0 | same article |

All three cleared the "body-proximate, never headline-named" bar. **Flow cross-check (mandatory before
BET-eligibility) fails all three:**
- **GS** — flow **−0.278**, OBV **분산 (distributing)**. Fails: distributing tape, not accumulating.
- **C** — flow **−0.468**, tag **🔴분산**. Fails outright — the worst tag in the sector.
- **WFC** — flow +0.294 (🟡중립), but OBV **중립/−0.033** (flat-to-mildly-distributing), RS60 only +1.5%.
  Weak positive at best, not an accumulation signature.

**Verdict: zero chain-hop candidates promoted this run.** The news co-mention (an "overheated" warning
piece and a bank-earnings roundup) generated proximity without flow confirmation — exactly the failure
mode this check exists to catch. Nothing forwarded to BET from this axis.

`chain-hop "PayPal takeover" "Visa Mastercard"` [5d] returned no proximate (non-headline) candidates — V,
MA, GOOGL, GOOG, COIN, AXP were all already headline-named in the PYPL-deal coverage (crowded), disqualifying
them by rule.

---

## §7 — Track-KPIs + anti-signals (observables)

**Track (unchanged from [07-15], reaffirmed):**
1. **2s10s slope** — now **+42bp** (was +36bp). ★ top KPI, strengthening.
2. **NIM/NII guidance revisions** — JPM ~$105.5B FY NII, PNC FY26 NII ~+14% (carried); watch for BNY/FHN/
   MTB commentary to corroborate on next prints.
3. **Loan-loss provisions / card NCO** — unchanged bottleneck; no new data this run.
4. **SCHW 07-21 (D-4)** — now the sharpest near-term KPI given the RSI 86.9 / OBV-distribution setup
   (§1.2). This is the run's genuinely new track item.

**Anti-signals (observables, one new):**
- ⚑ **Credit deterioration** (carried) — card NCO >~3.5%, rising provisions, CRE/office charge-offs.
- ⚑ **Curve re-inverting** (carried) — 2s10s rolling back toward flat, or real 10Y >2.50%.
- ⚑ **NEW — SCHW technical exhaustion into its own binary.** RSI 86.9 (extreme) + OBV **분산** (distribution,
  20d slope −16%) while price still sits above all MAs. **Falsifying level:** if SCHW's OBV flips back to
  매집 (accumulation) and RSI cools below ~70 into 07-21 *without* a price breakdown, this anti-signal is
  defused; if instead SCHW beats and still closes red (the BAC/beat-but-fade pattern, §1.5), the anti-signal
  is confirmed and the earnings leg of OW-FIN should be marked broken, independent of what the curve leg
  does.
- ⚑ **PYPL de-risk trigger (new, narrow scope)** — if the Stripe-Advent bid is withdrawn or collapses,
  PYPL's RS20/vol-surge reverses hard; this has **zero read-through to the rest of FIN** per §1.3/§5 and
  should not be treated as a sector tell either way.

---

## §8 — RESOLUTION VERDICT (mandatory)

**The curve leg and the earnings leg are not one bet, and they are not equally healthy right now.**

- **Curve leg — intact and strengthening.** 2s10s widened further (+36bp→+42bp) over the two days since
  [07-15]; PNC — the board's only ✅ clean-rise (shortZ −0.62) — carries a *healthy, non-extended*
  technical profile (RSI 65.2, Bollinger coiling/consolidating, OBV mildly accumulating). Per PREMORTEM
  lens 3, XLF RS60 is only +1.9%, meaning **the aggregate curve-driven bid is early, not extended** — and
  PNC's own chart (coiling, not overbought) is the name-level confirmation of that read. **PNC's clean rise
  is paying for the curve leg**, and that leg has more room, not less, than it had on 07-15.
- **Earnings leg — bifurcated, and its riskiest test is now visibly extended.** BNY (record quarters,
  dividend +19%) and the regional prints (FHN, MTB) confirm the earnings leg *has* delivered where it has
  already reported. But **SCHW, the direct 07-21 test of this leg, is technically the opposite of PNC**:
  RSI 86.9 (extreme) and OBV in distribution — the same "priced for perfection, walking into a high bar"
  signature that broke TSM this week, and the same dynamic the "beat-but-fade" news cluster (BAC, "Tectonic
  Risks") is already describing for banks broadly. **This is not a contradiction of lens 3's "early, not
  extended" read — it is a name-level exception inside a sector-level early read.** The sector is early;
  SCHW specifically is not.
- **PYPL is resolved OUT of this question entirely.** Its accel tag is M&A-arbitrage optionality (Stripe/
  Advent $53B bid, still unresolved as of 07-17), not a bank-earnings or curve signal, and should not be
  counted as breadth confirming either leg (§1.3, §5).

**Net:** the FIN OW's foundation — the curve — is real, dated (2s10s), and getting stronger, with its
cleanest named proof (PNC) technically un-extended. The exposure that could break independent of the curve
is concentrated and specific: **SCHW's 07-21 print, walking in technically overbought with distributing
OBV**, is where the beat-but-fade risk actually lives. A SCHW disappointment — or even a beat that still
fades — would not invalidate the curve leg (PNC/USB/FITB/HBAN would be unaffected), but it would be exactly
the kind of headline that gets mis-read as invalidating the whole FIN OW. Track SCHW's OBV state and RSI
into 07-21 as the disambiguator, not the sector tape.

---

**EXIT CHECK:** ✅ DELTA led (curve strengthened, data gap resolved with a load-bearing SCHW/PNC technical
divergence, PYPL resolved, beat-but-fade confirmed live) · ✅ flow cross-check (module_flow + us_flow, no
±1.5 spike, PNC still cleanest) · ✅ Players = 47-name large-cap union + 2 news-bounded small-caps (FHN,
MTB) · ✅ IR anchor from primary filing (SCHW 10-K + 8-K list, JPM carried by reference) · ✅ value chain
carried by reference, one node note (PYPL M&A excluded from chain) · ✅ chain-hop run, 3 candidates
surfaced, all 3 failed flow cross-check, zero promoted · ✅ track-KPIs + anti-signals as observables, one
new (SCHW technical exhaustion) · ✅ RESOLUTION VERDICT stated explicitly: curve leg early/strengthening
via PNC, earnings leg bifurcated with risk concentrated in SCHW's 07-21 binary, PYPL excluded. Zero
buy/sell calls. Blanks stayed blank where unconfirmed.
