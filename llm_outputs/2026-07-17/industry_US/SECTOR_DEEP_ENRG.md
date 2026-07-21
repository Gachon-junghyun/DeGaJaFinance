# DEEP · ENRG — 2026-07-17 (Fri) ★US-only

> Stage: DEEP (rotating pick, full fresh value-chain map — Energy was explicitly not deep-dived on 07-15).
> Runtime `--market us`. Zero buy/sell calls — analysis only, judgment stays with the human.
> Inputs read: `SECTOR_ROTATION.md`, `BLINDSPOT_PREMORTEM.md` (§1, §3, §5, §8), `CYCLE_EXPOSURE.md`,
> `SECTOR_FLOW_US.json` (asof 2026-07-16), live `module_flow`/`us_flow.py`/`module_business_us`/
> `module_fundamentals_us`/`module_news_data` pulls run today (2026-07-17).

---

## 0. The question this file must answer

ROTATION flagged ENRG as a flow/price divergence (commodity +10.2%, sector-flow rank 8 of 11).
PREMORTEM's lens 4 partly resolved it: the weak *sector* wflow is an aggregate artifact — refiners
(MPC/PSX/VLO) are already working while integrateds/E&P drag the average down. This file's job is to
**verify that claim from primary data rather than inherit it**, and to answer PREMORTEM's sharper
follow-up: **is the crack-spread leg durable against a Hormuz-open ("TACO") shock, or does it die with
the same headline that would kill the crude-price trade?**

---

## 1. Flow — split by node (the split IS the thesis)

Source: `SECTOR_FLOW_US.json` (asof 2026-07-16, top-300 mcap universe) cross-checked with a live
`module_flow` re-pull today (2026-07-17, bench SPY) for names outside the top-300 (LNG, XLE, XOP, DINO)
and `scripts/us_flow.py` (FINRA short-volume z-score, 2026-07-16 session).

| Node | Ticker | flow_score | tag | OBV | RS20 | RS60 | vol_surge | short-vol z (FINRA) |
|---|---|---:|---|---|---:|---:|---:|---|
| **Refining (crack)** | PSX | **+0.70** | 🟡중립 | 매집 | +17.0% | +23.3% | 1.06x | −1.43 (normal; 5v5 −16.6▼ = covering) |
| **Refining (crack)** | MPC | **+0.60** | 🟡중립 | 매집 | +22.1% | +36.9% | 0.88x | −0.83 (normal; 5v5 −5.5▼) |
| **Refining (crack)** | VLO | **+0.45** | 🟡중립 | 중립 | +22.9% | +26.8% | 1.03x | −0.08 (normal; 5v5 +3.7▲) |
| **Refining, non-top300** | DINO (HF Sinclair) | n/a (live pull) | 🟡중립 | 매집 | **+30.4%** | **+44.1%** | 1.19x | not pulled (outside FINRA batch) |
| Midstream (fee/vol) | WMB | +0.465 | 🟡중립 | 매집 | +4.5% | −0.5% | 0.90x | — |
| Midstream (fee/vol) | TRGP | +0.353 | 🟡중립 | 중립 | +7.9% | +15.1% | 0.86x | — |
| Midstream (fee/vol) | KMI | +0.221 | 🟡중립 | 매집 | +3.4% | −4.0% | 0.73x | **+0.92 (5v5 +5.2▲, rising into print)** |
| Midstream (fee/vol) | LNG | n/a (live pull) | 🟡중립 | 매집 | +12.1% | −3.3% | 0.81x | **+3.09 🔴 extreme (own-base) — 5v5 +5.3▲** |
| Midstream (fee/vol) | OKE | −0.124 | 🟡중립 | 분산 | +7.7% | +5.1% | 0.80x | — |
| Integrated (crude-price) | XOM | −0.157 | 🟡중립 | 분산 | +2.8% | −7.1% | 0.83x | — |
| Integrated (crude-price) | CVX | −0.417 | 🟡중립 | 분산 | +2.0% | −5.6% | 0.70x | — |
| E&P (crude-price) | EOG | −0.267 | 🟡중립 | 분산 | +4.8% | +1.3% | 0.76x | — |
| E&P (crude-price) | FANG | −0.331 | 🟡중립 | 분산 | +1.0% | −2.3% | 0.70x | — |
| E&P (crude-price) | OXY | −0.360 | 🟡중립 | 분산 | −0.1% | −7.4% | 0.84x | — |
| E&P (crude-price) | COP | −0.379 | 🟡중립 | 분산 | +1.3% | −9.0% | 0.82x | — |
| E&P (crude-price) | DVN | −0.537 | 🟡중립 | 분산 | +0.3% | −10.2% | 0.61x | — |
| Services | BKR | −0.778 | 🔴분산 | 분산 | −8.1% | −10.4% | 0.80x | — |
| Services | SLB | −0.906 | 🔴분산 | 분산 | −11.3% | −15.7% | 0.57x | — |
| Sector ETF | XLE | n/a (live pull) | 🟡중립 | 중립 | +2.9% | −2.4% | 0.88x | — |
| Sub-index ETF | XOP | n/a (live pull) | 🟡중립 | 중립 | +5.8% | −2.6% | 0.81x | — |

**Verified, not inherited: the split is real and clean.**
- Refiners (PSX/MPC/VLO + the non-top300 DINO) are the *only* clean 🟢-shaded cluster — all four **OBV
  accumulating-or-neutral**, all four **RS60 positive and large (+23% to +44%)**. DINO in particular
  (mcap **$15.7B** [yfinance], news-named 2× in a 14-day window: *"PBF Energy... refining boom"* co-search
  and *"Phillips 66 upgraded, HF Sinclair cut at Mizuho"* [SA/07-09,07-16]) **out-RS's the named majors** —
  this was not in PREMORTEM's carve-out and is new.
- Midstream is genuinely mixed, not uniformly "insulated": WMB/TRGP have real RS60, KMI/LNG do not
  (RS60 −4.0% / −3.3%). This matters for §3.
- Integrateds and E&P are uniformly OBV-분산 (distributing) with negative-to-flat RS60 — the "monetize
  crude, not the crack" split holds up under direct verification, not just as an inherited claim.
- Services (BKR/SLB) are the worst node on the board — 🔴 both, and this is the only place COT-style
  "cyclical trough" logic would apply if oil holds; it is *not* part of the epicenter thesis and is flagged
  only as a laggard, not a candidate.
- ⚠ **New finding, not in PREMORTEM**: LNG's FINRA short-volume is at **z = +3.09**, the single most
  extreme reading of any name checked in this file — well beyond KMI's +0.92. That is a standalone
  anti-signal on LNG specifically (see §6).

---

## 2. Players — bounded universe (named ≥2× in window + real ticker + mcap ≥ ~$2B)

| Ticker | Name | Node | mcap | Named-in-window evidence |
|---|---|---|---:|---|
| MPC | Marathon Petroleum | Refining | $89.3B [yfinance] | Flow epicenter; RS20 +22.1%/RS60 +36.9% |
| PSX | Phillips 66 | Refining | $80.7B [yfinance] | Flow epicenter; *"Phillips 66 declares $1.27 dividend"* [SA 07-09]; *"Phillips 66 upgraded... at Mizuho"* [SA 07-16] |
| VLO | Valero Energy | Refining | $89.2B [yfinance] | Flow epicenter; near 52wk high ($300.26 vs $303.64 high) |
| **DINO** | HF Sinclair | Refining | **$15.7B** [yfinance] | *"HF Sinclair cut at Mizuho"* [SA 07-16] + prior mention — 2 hits/14d; flow-verified RS20 +30.4%/RS60 +44.1%, **not** in top-300 universe |
| CVI | CVR Energy | Refining | — | *"CVR Energy: Refining Margin Benefits Are Underpriced... wider crack spreads"* [SA 07-02] — **1 hit only, below the ≥2× bar → logged, not promoted** |
| PBF | PBF Energy | Refining | — | *"PBF Energy: Refining Boom Appears Stronger Than Ever"* [SA 07-16] — **1 hit only, below the ≥2× bar → logged, not promoted** |
| KMI | Kinder Morgan | Midstream (fee) | $70.3B [yfinance] | Held book position (14.1%); Q1 print 8-K [EDGAR 2026-04-22, Item 2.02] |
| LNG | Cheniere Energy | Midstream/export (fee) | — | Held book position (9.87%) |
| WMB | Williams Companies | Midstream | $89.4B [SECTOR_FLOW_US] | Best midstream RS60 (−0.5%, i.e. least negative) |
| XOM | ExxonMobil | Integrated | $571.2B [SECTOR_FLOW_US] | Largest-cap Energy name, benchmark for "crude, not crack" |
| CVX | Chevron | Integrated | $345.8B [SECTOR_FLOW_US] | Same |
| COP | ConocoPhillips | E&P | $131.3B [SECTOR_FLOW_US] | Largest pure E&P in the flow set |
| BKR / SLB | Baker Hughes / Schlumberger | Services | $58.0B / $71.9B | Worst-flow node; not part of the epicenter thesis |

⚠ **Tanker names (FRO/STNG/INSW/DHT) are outside the top-300 flow universe — flow-unverified.** Direct
yfinance pull (10-day close): DHT $17.29→$17.84, FRO $37.66→$37.17, INSW $85.23→$88.23, STNG $74.32→$77.95
(2026-07-07 to 2026-07-16). **No clean directional breakout** in this window despite the live Hormuz
freight-risk headlines — a genuinely flat/rangebound tape, not a confirmation of the "tanker rate spike"
narrative one might expect from the news volume. Logged as a negative/inconclusive result, not a candidate.

---

## 3. IR anchor — verified from primary filings, not news

### KMI — 10-K Item 1/2 (FY2025, filed 2026-02-13) [EDGAR]
> *"Our business strategy is to: •focus on stable, **fee-based** energy transportation and storage assets
> that are central to the energy infrastructure of growing markets... In addition to fee-based
> arrangements, **some of which may include minimum volume commitments**, we also provide some services
> based on **percent-of-proceeds, percent-of-index, and keep-whole contracts**."**
**Verdict: the "fee-based, take-or-pay-adjacent" characterization is directionally correct and confirmed
in KMI's own words — but it is not literally 100%.** A minority sleeve of the gathering/processing segment
is genuinely commodity-price-sensitive (POP/POI/keep-whole). No literal string "take-or-pay" appears in
KMI's Item 1 (it appears in LNG's, see below) — KMI's own vocabulary is "fee-based" + "minimum volume
commitments," which is the pipeline-industry synonym for the same structural insulation, with a real but
minority exception.

### LNG — 10-K Item 1/2 (FY2025, filed 2026-02-26) [EDGAR]
> *"Our long-term counterparty arrangements form the foundation of our business... and include SPAs, in
> which our customers are generally required to **pay a fixed fee with respect to the contracted volumes
> irrespective of their election to cancel or suspend deliveries** of LNG cargoes... While IPM agreements
> are not revenue contracts for accounting purposes, the payment structure under the IPM agreements
> generates a **take-or-pay style fixed liquefaction fee**."**
**Verdict: literal take-or-pay language, confirmed.** But the 10-K's own forward-revenue table complicates
the "100% insulated" framing: estimated cumulative future SPA revenue is **$107.7B "fixed fees" vs $182.9B
"variable fees"** (i.e. **~63% of disclosed future dollar revenue is in the variable-fee bucket**, index-linked
to global LNG/gas prices, not fixed). **Important nuance for the epicenter question: even LNG's "variable"
exposure is to the global LNG/natural-gas index — not to the US diesel/gasoline crack spread that is this
cycle's actual epicenter mechanism.** So the crack-spread carve-out claim (LNG has ~zero *crack* exposure)
survives even after this correction; the "100% take-or-pay, zero commodity sensitivity of any kind" claim
does not, and should not be repeated as written.

### MPC — 10-K Item 1 (FY2025, filed 2026-02-26) [EDGAR]
> *"We operate one of the nation's largest refining systems with approximately 3.0 million barrels per day
> of crude oil refining capacity... Our operations consist of three reportable operating segments: Refining
> & Marketing, Midstream and Renewable Diesel."* Risk-factor bullets (Item 1A) name **"global and regional
> development by competitors of new refining or renewable conversion capacity"** and **"temporary and
> permanent closures, utilization levels and capacities of other refineries in our markets and globally"**
> as explicit earnings drivers — i.e. MPC's own 10-K identifies *refining capacity destruction elsewhere*
> (which is exactly what is happening to Russian refineries) as a named driver of its own margin.

### VLO — 10-K Item 1 (FY2025, filed 2026-02-25) [EDGAR]
> *"We own 15 petroleum refineries located in the U.S., Canada, and the U.K. with a combined throughput
> capacity of approximately 3.2 million barrels per day (BPD)... We manage our operations through our
> Refining, Renewable Diesel, and Ethanol segments."* Pure refining-margin (crack) exposure confirmed;
> no midstream fee-based buffer segment (unlike MPC).

**Net: the epicenter/non-epicenter split PREMORTEM asserted is confirmed from primary filings, with one
correction (LNG's revenue mix is majority "variable fee," not majority fixed) that narrows but does not
overturn the carve-out.**

---

## 4. Value-chain node map (7 nodes, left → right)

```
[E&P / crude          [Crude logistics/       [Refining              [Product distribution   [Retail/      [LNG liquefaction
 production]            midstream (pipe/       (crack-spread           & storage               end-use        & export
                        storage, fee-based)]    epicenter)]             (terminals, fee-based)] (gasoline,     (fee/index
                                                                                                  diesel        mixed)]
                                                                                                  pumps)]
 XOM CVX COP EOG        WMB TRGP KMI OKE         MPC PSX VLO DINO       KMI terminal segment      (unlisted     LNG (Cheniere)
 OXY FANG DVN           (OKE/WMB most            (CVI/PBF logged,                                 mostly)
 (crude-price            leveraged to gas         below bar)
 monetizers)             gathering volume)

  [Oilfield services layer, cross-cutting all upstream nodes: BKR, SLB — worst flow on the board]
```

**Bottleneck = refining CAPACITY (specifically product-grade, diesel-capable), not crude supply.**
Tested directly: crude is *not* scarce — WTI at $78.96 [yfinance, 07-17] is nowhere near a supply-panic
level (Iran-war peak context aside), and the news window shows "dark ships and Oman transfers indicate
Hormuz transits continue" [Bloomberg 07-16] — physical crude flow is degraded but not stopped. What *is*
scarce, per the DB pull, is **finished diesel**: Russian refinery runs are at "the lowest in more than two
decades" [Bloomberg 07-13], multiple named Russian refineries have been struck (Afipsky, Syzran) [Bloomberg
07-10, 07-12, 07-14], and Russia has imposed its own diesel export ban [SCMP 07-11]. **Demand is not the
constraint either** (nothing in the window shows demand destruction). This is a textbook capacity-side
bottleneck at the refining node specifically — which is exactly the node where the flow data shows the
epicenter (§1), and exactly the node the 10-Ks (§3) name as their own key sensitivity.

---

## 5. Chain-hop candidates — flow-cross-checked, none headline-named at entry

Ran `module_news_data chain-hop "refinery" "diesel"` (14d/foreign) and `chain-hop "Hormuz" "tanker"`
(second call timed out on the news API twice — server contention, not resolved in this run window,
logged rather than silently dropped).

- **The "refinery"/"diesel" chain-hop result was noise, not signal.** HEADLINE-NAMED came back META/AMZN/
  TSLA/MSFT/ORCL/MMM; the ★CHAIN-HOP candidates were GOOGL/GOOG/AAPL — all mega-cap tech names picking up
  generic "crack"/"diesel" token collisions in unrelated macro articles, not genuine value-chain
  co-mentions. **None of these survive as energy candidates — discarded, not promoted.**
- **The genuine chain-hop candidate this run surfaced came from the Players pass, not the automated
  tool: DINO (HF Sinclair).** It is body-proximate-named (Mizuho analyst-note co-mention with PSX, not a
  standalone headline), passes the ≥2×/mcap bar, and — critically — **flow-cross-checked positive and
  stronger than the majors** (RS20 +30.4%, RS60 +44.1%, OBV 매집, vol_surge 1.19x). This is the one name
  in this file that reaches the bar PREMORTEM's own rule requires ("a news co-mention alone is NOT a
  candidate — flow-cross-check before BET").
- **CVI (CVR Energy) and PBF (PBF Energy)** are logged, not promoted: each has exactly 1 mention in the
  14-day window (below the ≥2× threshold) despite CVI's mention being thesis-perfect (*"Refining Margin
  Benefits Are Underpriced... wider crack spreads"*). Flagged for a future run once/if a second mention
  appears.
- **Tanker names (FRO/STNG/INSW/DHT)**: not flow-verifiable (outside top-300 universe) and the raw price
  action (§2) shows no confirming breakout — do not promote to BET on news volume alone.

---

## 6. Track-KPIs + anti-signals (stated as observables)

| KPI | Current reading | Source | Falsifier / watch level |
|---|---|---|---|
| Diesel retail price | "$5/gal, up 33% since start of Iran war" | NYT 07-16 | Reversion toward pre-war levels |
| Russian refinery utilization | "lowest in more than two decades" | Bloomberg 07-13 | Confirmed repair/restart of named refineries (Afipsky, Syzran) |
| Russian diesel export ban | In effect | SCMP 07-11 | Ban lifted |
| Hormuz transit status (as of today) | **NOT open** — "US Launches New Strikes on Iran as Hormuz Traffic Slumps" / "Dark Ships and Oman Transfers Indicate Hormuz Transits Continue" | Bloomberg 07-16 | A durable (>24h) "strait open/blockade lifted" statement — the 07-14 toll-plan reversal already fired and faded in <48h, this bar has **not** been met |
| CL=F level | **$78.96** [yfinance 07-17], holding the +10.2% 5-session gain, not reversing | live pull today | <$72 (premortem's own invalidation level) |
| WTI COT positioning | 13%ile, crowded-SHORT (asof Tue-close 07-14, 3-4d lag — not re-pulled fresh this run) | inherited from ROTATION/PREMORTEM | Flip to crowded-long |
| MPC technical state | **RSI 85.7, MA강세스택 (5>20>60>120), CONFIRMED-TURN, Bollinger expansion 31.0% at upper band** [module_chart --read] | live pull today | Swing-low stop at $242.91 per the chart module |
| MPC/PSX/VLO vs 52wk high | MPC $305.85 vs $308.42 high · PSX $201.32 vs $202.72 high · VLO $300.26 vs $303.64 high — **all three within ~1% of 52-week highs** | yfinance | Failure to make new highs on the next leg = exhaustion tell |
| Dated earnings | **KMI 2026-07-23** (D+6) · **VLO 2026-07-30** (D+13) · **MPC 2026-08-04** · **PSX 2026-08-05** · **LNG 2026-08-06** [module_fundamentals_us, confirms PREMORTEM's "07-22" to within 1 day] | live pull today | Crack-spread commentary on the Q2 call is the first hard confirm/deny of the thesis from management |
| LNG short-vol pressure | **z = +3.09, 5v5 +5.3▲ — most extreme reading in this file** | FINRA/us_flow.py 07-16 | Normalizes toward z<1.5 |
| KMI short-vol pressure | z = +0.92, 5v5 +5.2▲, rising into the print | FINRA/us_flow.py 07-16 | Same |

**Anti-signals, ranked:**
1. **All three refiner majors are simultaneously within ~1% of 52-week highs AND MPC prints RSI 85.7** —
   this is a *technical* exhaustion risk that exists independent of the fundamental crack thesis. A
   pullback here would not, by itself, falsify the crack spread; it would just be mean reversion after a
   fast move.
2. **LNG's short-vol z (+3.09) is the single most extreme positioning reading surfaced in this file** —
   more extreme than KMI's pre-earnings short build. This was not flagged by PREMORTEM and is new.
3. **The tanker-equity confirmation is absent** (§2) — if the Hormuz/freight story were the dominant
   driver of the crack thesis, tanker equities should show it, and in this window they do not.

---

## 7. RESOLUTION VERDICT

**A. Early or trap? — EARLY-BUT-NOW-SUBSTANTIALLY-DE-RISKED-AT-THE-EQUITY-LEVEL, not a trap.**
The refining-node flow (§1) is unambiguously positive and OBV-confirmed, independently verified today
(not just inherited from the 07-16 sweep): PSX/MPC/VLO all show accumulation and large positive RS60, and
the newly-verified DINO out-performs all three. The "trap" reading is refuted at the flow level. But the
refiner names are simultaneously **technically extended** (§6: near 52wk highs, RSI 85.7 on MPC) — so
"early" applies to the *thesis* (the crack driver is structural, not exhausted), not necessarily to the
*entry price* in the specific epicenter names today.

**B. Does the crack thesis survive a Hormuz-open ("TACO") branch? — Largely YES, with one important
qualifier that actually improves the mechanics for refiners specifically.**
The primary driver of the diesel/crack widening in this DB (Russian refinery destruction from Ukrainian
strikes on named facilities + Russia's own diesel export ban) is **mechanically independent of the Strait
of Hormuz** — it is Russia-Ukraine war damage and a Kremlin policy choice, not an Iran/Hormuz supply
event. A durable Hormuz-open headline would not repair a bombed Russian refinery or lift Russia's own
export ban. **Further: because refiners buy crude and sell diesel, a Hormuz-driven crude-price collapse
(if it happened) would actually widen the crack, not narrow it**, as long as diesel stays supply-constrained
by the Russian-refinery mechanism — refiners are a spread business, not a crude-price-long position. This
directly refutes PREMORTEM's implicit framing that a Hormuz-open shock hits "OW-ENRG" as one undifferentiated
block. **The qualifier**: near-term *equity* price action for MPC/PSX/VLO would very plausibly still see a
beta-driven, basket-wide Energy-sector sell-off on such a headline (algorithmic/sector-rotation selling does
not distinguish fundamental exposure), especially given how extended these names already are (§6). **So:
the fundamental crack thesis is structurally decoupled from Hormuz; the stocks are not — that gap is the
actual tradable risk**, not a reason to doubt the crack driver itself.

**C. Epicenter-exposure verdict (book / cycle-registry question): the GAP is REAL and confirmed from
primary filings, with a nuance.**
KMI's and LNG's fee-based/take-or-pay characterization is **confirmed in the companies' own words** (§3) —
they are volume names, structurally different from a margin/crack name. The book's 23.97% "any-layer"
Energy exposure, 100% KMI+LNG, is genuinely **~0% exposed to the specific crack-spread mechanism** that is
this cycle's actual epicenter (MPC/PSX/VLO/DINO), independent of the minor commodity-sensitive sleeves
disclosed in both 10-Ks. The GAP flagged by PREMORTEM is not a data artifact — it survives primary-source
verification.

**D. New, not-in-PREMORTEM findings from this file**: (1) DINO/HF Sinclair is a flow-confirmed epicenter
name stronger than the named majors and was not previously surfaced; (2) LNG's own 10-K shows a majority
of *disclosed future revenue* is in the "variable fee" bucket, softening (not reversing) the pure
take-or-pay framing; (3) LNG's short-volume positioning (z +3.09) is the most extreme single reading in
this file and is a standalone risk on the held book position, separate from and additional to the KMI
earnings binary already flagged.

---
**EXIT CHECK:** ✅ Flow split by node (refiners vs midstream vs integrateds vs E&P vs services), verified
today, not just inherited · ✅ Players bounded (≥2×, real ticker, mcap≥$2B) — DINO promoted, CVI/PBF logged
below bar · ✅ IR anchor from primary 10-K text (KMI/LNG take-or-pay language + MPC/VLO crack exposure),
with a correction to the LNG "100% insulated" framing · ✅ 7-node value-chain map, bottleneck tested
(refining capacity, not crude supply, not demand) · ✅ chain-hop run twice, one leg timed out (logged, not
hidden), automated candidates discarded as noise, DINO promoted via manual flow-cross-check per the rule ·
✅ Track-KPIs stated as observables with dated earnings for all five names · ✅ RESOLUTION VERDICT given on
early-vs-trap, crack-vs-TACO durability, and epicenter exposure — no buy/sell call issued.
