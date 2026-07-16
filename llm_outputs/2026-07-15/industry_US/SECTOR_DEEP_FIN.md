# SECTOR_DEEP_FIN — Financials (FIN) deep-dive · 2026-07-15 (Wed)

> Stage 5 / L2 DEEP. FIN is a **top OW** this run — flow **#2 (0.361 / 0.33, broad)**, and the
> **bank-earnings leg the 2026-07-14 postmortem said we MISSED** (GS crushed Q2 + hiked dividend,
> +6% on 07-14). Fresh full map. **Zero buy/sell calls — analytical map only** (P4).
> REGIME: cool CPI (07-14) + cool PPI (07-15, −0.3% m/m) = risk-on; long end term-premium-bid
> (10Y ~4.58%), **2s10s steepening (+36bp)** — a steepener HELPS bank NIM. Bank earnings cluster
> THIS WEEK: GS + JPM (done 07-14), MS + BLK (done 07-15), regionals (PNC/FITB/HBAN) ahead.

---

## §0 — Data-freshness caveat (read first)

The price-derived flow axes came back **partially blank this run**: `last`, `RS20`, `RS60`, `RSI`,
and Bollinger width all returned **NaN** for all six FIN names — a yfinance fetch gap, **not a signal**
[flow][chart]. The axes that DID resolve and are load-bearing here: **news-velocity, OBV state, volume
surge** (module_flow) and **FINRA short-vol Z** (us_flow). Blanks stay blank (P4); relative-strength
claims are therefore withheld, and conclusions lean on OBV + short-vol + the realized earnings tape.

---

## §1 — Flow cross-check (which sub-leg has the cleanest accumulation?)

**module_flow** `JPM PNC FITB HBAN SCHW V --bench SPY` (news 7d/30d) [flow]:

| Ticker | Tag | News-velocity | OBV state (norm) | Vol surge | Note |
|---|---|---|---|---|---|
| **JPM** | 🟢 **가속 (accel)** | 1.78x | 매집 (0.149) | **1.30x** | only 🟢 + only real vol surge; money-center |
| **PNC** | 🟡 neutral | 1.89x | 매집 (0.192) | 1.16x | regional; quiet accumulation |
| **FITB** | 🟡 neutral | 2.57x | 매집 (**0.28**) | 0.90x | regional; high velocity but tiny abs news count (3/5) |
| **HBAN** | 🟡 neutral | 2.14x | 매집 (**0.32**, highest) | 0.79x | regional; abs news count 1/2 |
| **SCHW** | 🟡 neutral | 1.98x | 매집 (0.176) | **0.65x** | broker; weakest volume |
| **V** | 🟡 neutral | 1.05x | 매집 (0.219) | 0.90x | payments; velocity barely >1 |

**us_flow.py** — FINRA Reg SHO short-vol Z (asof 2026-07-14) [flow]:

| Ticker | Short% | Base20 | **Z** | 5v5 trend | Verdict |
|---|---|---|---|---|---|
| JPM | 44.7% | 45.4% | −0.13 | +4.5▲ | 🟡 normal |
| PNC | 43.7% | 47.1% | −0.33 | −13.9▼ | 🟡 normal |
| FITB | 70.4% | 69.4% | +0.10 | +1.0▲ | 🟡 normal (structurally high short-vol) |
| **HBAN** | 29.2% | 48.6% | **−2.23** | −12.2▼ | 🟢 **short collapse (cover / pressure exit)** |

**Read — cleanest accumulation is two-tracked:**
- **Live / already-firing leg = money-center + capital-markets (JPM).** JPM is the *only* 🟢가속 and the
  *only* name with a genuine volume surge (1.30x), and it's confirmed by a record print (§5). But its move
  is **partly spent**: the chart flags a bearish price/RSI divergence (§6) and the headline was inflated by
  a one-time Visa gain (§5). Accumulation is real but late.
- **Cleanest *quiet* accumulation = regionals.** Every regional is **OBV=매집** with the **highest OBV norms
  in the set** (HBAN 0.32, FITB 0.28 > JPM 0.149), and **HBAN's short-vol Z −2.23** is the single cleanest
  positioning signal in FIN (a short base collapsing). Velocity is high but the absolute news counts are
  tiny (FITB 3, HBAN 1) — this is *under-the-radar* accumulation ahead of their prints, exactly the
  premortem Lens-2 read: **"KRE is the cleaner curve/NIM lever if rates re-lift."**
- SCHW (broker) is the weakest of the six on volume (0.65x); V (payments) barely registers velocity (1.05x).

---

## §2 — Sub-leg map (FIN is NOT one trade)

| Sub-leg | Names (flow leaders in **bold**) | Primary driver | Steepening + risk-on benefit |
|---|---|---|---|
| **Money-center banks** | **JPM**, BAC, WFC, C | NII / NIM on curve; card credit; huge buybacks | **High** — NIM levered to 2s10s; JPM NII +10%, FY guide raised |
| **Regionals / super-regionals** | **PNC**, **FITB**, **HBAN**, KRE | **NIM / curve is the PUREST lever**; loan growth; CRE credit tail | **Highest (cleanest)** — asset-sensitive, deposit-beta rolling down; PNC FY26 NII +14% |
| **Capital-markets / brokers** | GS, MS, **SCHW** | **Trading revenue** (equities/FICC) + IB/DCM reopening | **High via risk-on** — GS equities +72%, MS +69% (§5); the realized catalyst leg |
| **Payments** | **V (Visa)**, MA | Consumer spend volume, cross-border; NOT rate-levered | Indirect (risk-on consumer) — flow flat; also the source of JPM's one-time gain |
| **Insurers** | ALL, TRV, AIG, PGR | Underwriting cycle + **investment-income reinvestment at higher long yields** | **Moderate** — higher-for-longer long end *helps* reinvestment yields (a rate *level* play, not a curve-slope play) |

**Which benefits most from steepening + risk-on?**
- **Steepener (NIM) → regionals win cleanest.** They are the most asset-sensitive, least diversified away
  from spread income, and their deposit betas are now rolling *down* (PNC: −18bp on interest-bearing
  deposits) while asset yields re-price up on a bull/bear-steepener [WebSearch].
- **Risk-on (activity) → capital-markets win biggest *this quarter*** — the record equities-trading prints
  (§5) are a pure risk-on/volatility harvest, not a rate story.
- Net: **regionals = cleanest forward NIM/curve lever; capital-markets = the leg that already delivered the
  catalyst.** These are different clocks — do not blend them.

---

## §3 — IR / filings anchor (JPM 10-K, FY2025, filed 2026-02-13) [filing]

`module_business_us JPM --full --json` → 10-K, accession 0001628280-26-008131, period 2025-12-31.
$4.4T assets, $362.4B stockholders' equity; leader in IB, consumer/SMB banking, commercial banking,
transaction processing, asset management [filing].

- **Item 7 MD&A is incorporated by reference** (pages 46–160 of the annual report), so the fetched MD&A body
  is a pointer only — NIM/credit/capital-return quantities here come from the **live Q2 print (§5)**, not the
  stale 10-K text. Noted, not inferred (P4).
- **Item 1A risk taxonomy = the sector's anti-signal checklist** [filing]:
  - **Credit risk** — "adverse changes in the financial condition of clients… declines in the value of
    collateral… concentrations." → the binding constraint (§4).
  - **Market risk** — "changes in **interest rates and credit spreads**" on earnings & capital. → the NIM/curve lever, both directions.
  - **Capital risk** — distributions/buybacks "could be limited if it does not satisfy regulatory capital
    requirements." → gates the capital-return leg.
  - Liquidity, strategic (competition), country (hostilities — Hormuz tail), conduct/reputation, people.

Budget note: PNC/SCHW `--full` not pulled this run (JPM as the money-center anchor + live regional prints
in §5 cover the same value-chain nodes); flagged, not silently skipped.

---

## §4 — Value chain / competitive structure → the bottleneck

```
deposit franchise ─▶ NIM / curve ─▶ loan growth & credit quality ─▶ capital-markets/trading ─▶ fee income ─▶ capital return (buyback/div)
   (deposit beta)     (2s10s +36bp)      (★ CREDIT COSTS ★)          (risk-on harvest)         (AWM/cards)     (regulatory-capital gated)
```

- **Deposit franchise / beta** — *easing* constraint. PNC's rate paid on interest-bearing deposits **−18bp**;
  cheaper funding is currently a tailwind, not a bottleneck [WebSearch].
- **NIM / curve** — *tailwind*. 2s10s +36bp steepening re-prices asset yields above rolling-down deposit
  costs. JPM NII +10% to $25.6B, FY guide **raised to ~$105.5B** (ex-markets $96.5B, up from $95B); PNC FY26
  NII guide **~+14%** with NIM expanding [WebSearch]. This leg is firing.
- **Loan growth & credit quality** — **THE BOTTLENECK (binding constraint).** Everything upstream (funding,
  NIM) and downstream (trading, capital return) is currently green; the one variable that can flip the whole
  sector is **credit costs**. JPM credit costs $2.5B; card NCO guided ~3.2% FY ("better than expected" but
  still the watch item). PNC Q2 flagged explicitly as **"FirstBank tailwind, but credit still matters"**
  [WebSearch]. Regional CRE/office is the fat tail. → **Bottleneck = credit costs / provisions**
  (secondary: deposit beta, if the Fed turns hawkish and re-lifts short rates).
- **Capital-markets / trading** — *firing hardest* (§5), but cyclical/volatility-dependent — not a durable moat.
- **Fee income** — AWM (BLK record AUM), cards, payments; diversifier.
- **Capital return** — *accelerating but regulatory-capital gated*. GS div → $5.00 (from $4.50); JPM/MS
  buyback pace elevated. Gate = CET1 / stress-capital-buffer, per Item 1A capital risk.

---

## §5 — Earnings read (the live catalyst — 07-14 & 07-15 prints) [WebSearch]

**Goldman Sachs (GS) — 07-14 — CRUSHED.** Net revenue **+39% YoY to $20.34B** (est ~$16.1B); EPS **$20.98**
vs ~$14.48 est (**+45.9% beat**). Global Banking & Markets +53% YoY to $15.52B. **Record equities trading
$7.42B (+72% YoY)**; FICC +32% to $4.59B. **Dividend hiked to $5.00/qtr** (from $4.50). Stock +6% on the day.
→ *This is the leg the postmortem said we missed. Driver = risk-on trading harvest + IB reopening + capital return.*

**JPMorgan (JPM) — 07-14 — record, but read past the headline.** Net income $21.2B / EPS $7.70 — **but
includes ~$5.6B pretax one-time gains (mainly a $4.6B gain on Visa shares)**; ex-items net $16.9B / EPS $6.14.
**NII $25.6B (+10%)**; FY NII guide raised to ~$105.5B (ex-markets $96.5B). Credit costs $2.5B; card NCO
~3.2% FY ("better than expected"). Adjusted expense guide raised to ~$107.5B. → *Clean NII beat + curve
tailwind; the profit "jump" is partly the Visa mark, so weight NII/credit over the headline EPS.*

**Morgan Stanley (MS) — 07-15 — record revenue & profit.** Net revenue **$21.35B (+27%)**; net income +58%
to $5.58B / EPS $3.46 (vs $2.94 est). **Equities trading +69% to $6.3B** (vs ~$4.4B est — a ~$1.9B beat);
FICC +13% to $2.46B. **Wealth Management record net revenue $8.86B (+14%)**, pre-tax margin 30.5%, **+$148.1B
net new assets** (>2× the $59.2B a year ago); total client assets $10T. → *Confirms the GS trading read AND
adds the durable wealth-management annuity — the highest-quality print of the cluster.*

**BlackRock (BLK) — 07-15 — record AUM.** EPS **$13.91** vs $12.57 est; revenue **$7.08B (+31%)**. **AUM
$15.3T**; record 1H net inflows $321B ($192B in Q2 alone), 10% organic base-fee growth; adj operating margin
**45.9%** (from 43.3%). → *Fee-income / asset-gatherer leg firing on broad inflows (ETF + private markets + HPS).*

**PNC (regional preview of the leg) — Q2 2026** [WebSearch]. Net income $2.1B; EPS $4.81 GAAP / $4.85 adj.
**NII $4,107M** (seq up from $3,961M); NIM 2.95% (+11bp, on −18bp deposit cost); avg loans +7%; FirstBank
integration a tailwind; **FY26 NII guide ~+14%** → implies further NIM expansion. Caveat: "**credit still
matters**." → *The clean read on the regional NIM/curve thesis — spread income compounding, credit the only doubt.*

**Cross-read:** the cluster is a **two-engine beat** — (1) a risk-on **trading/markets** harvest (GS/MS,
cyclical) and (2) a curve-driven **NII/NIM** grind (JPM/PNC, more durable) — bolted onto record **fee/AUM**
(BLK, MS-WM). No credit blow-up surfaced *yet*; that silence is the thing to keep watching (§7).

---

## §6 — Chart read (verbatim, module_chart --read) [chart]

**JPM** (money-center anchor):
```
OBV: 중립 (20d기울기 +2%)
다이버전스: 약세(가격 고점↑ · RSI 고점↓)
MA정렬: 강세스택(5>20>60>120) · 가격 0/4 MA 위
볼린저: 확장 nan% · 중단
RSI: nan · 모멘텀20d +nan%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 317.97
```
*Read: bullish MA stack (5>20>60>120) intact, but a **bearish price/RSI divergence** — price made a higher
high, RSI a lower high. Late-stage / momentum-fading caution on the money-center leg, consistent with §1
"accumulation real but partly spent."*

**PNC** (regional):
```
OBV: 중립 (20d기울기 -12%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 0/4 MA 위
볼린저: 확장 nan% · 중단
RSI: nan · 모멘텀20d +nan%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 230.56
```
*Read: bullish MA stack, **no divergence** (cleaner structure than JPM), but short-term OBV slope −12% =
mild near-term distribution vs the module_flow 매집 tag — a chop/consolidation ahead of its print. No
bearish divergence = more room than JPM structurally.*

(RSI / Bollinger / momentum NaN this run — same yfinance gap as §0; MA-alignment, OBV-slope, and divergence
are the resolved, load-bearing reads.)

---

## §7 — Track-KPIs + anti-signals (observables)

**Track (the tailwind gauges):**
1. **2s10s slope (+36bp now)** — ★ **TOP KPI**. The single variable that drives NIM for the whole book;
   steeper = NIM expands, re-inversion = thesis dies.
2. **NIM / NII guidance revisions** — co-primary. JPM FY NII ~$105.5B (raised); PNC FY26 NII ~+14%. Watch for further raises vs cuts.
3. **Loan-loss provisions / card NCO** — JPM card NCO ~3.2% FY; provision $2.5B. The bottleneck gauge (§4).
4. **Deposit costs / betas** — PNC −18bp; watch for re-acceleration if short rates re-lift.
5. **IB / trading revenue run-rate** — GS equities +72%, MS +69%; is Q3 sustaining or was Q2 a vol peak?
6. **Buyback pace + dividend actions** — GS div→$5.00; JPM/MS buyback tempo (CET1-gated).
7. **Regional M&A / integration** — PNC-FirstBank, HBAN roll-ups; the KRE re-rate catalyst.

**Anti-signals (what flips the map):**
- ⚑ **Credit deterioration** — card NCO breaking above ~3.5%, rising provisions, or **CRE/office charge-offs
  in the regionals**. This is the binding constraint; it flips the sector before anything else.
- ⚑ **Curve re-inverting** — 2s10s rolling back toward flat / short-end re-lift on a hawkish-Fed turn
  (Warsh: price-stability mandate "not met"; the premortem's re-arm trigger is core PPI ≥+0.5% OR 10Y >4.75%).
  A hawkish re-lift kills the NIM lever *and* raises deposit betas — a double hit.
- ⚑ **Risk-off flip** — a Hormuz escalation ("a rates-tightening event in an energy costume," per premortem)
  or vol collapse would gut the trading-revenue leg (GS/MS) that carried this quarter's beats.
- ⚑ **Late-cycle exhaustion in money-center** — the JPM bearish price/RSI divergence (§6) is the early tell.

---

**EXIT CHECK:** ✅ flow cross-check run (module_flow + us_flow) with data-gap caveat named · ✅ 5 sub-legs
mapped with drivers + steepening/risk-on beneficiary · ✅ JPM 10-K filing anchor (Item 1 / 1A / 7-by-ref) ·
✅ value chain → bottleneck (credit costs) · ✅ live earnings read GS/JPM/MS/BLK/PNC cited [WebSearch] ·
✅ JPM + PNC CHART_READ embedded verbatim · ✅ 7 track-KPIs + 4 anti-signals as observables. Blanks (RS/RSI/
Bollinger) left blank (P4). Zero buy/sell calls.
