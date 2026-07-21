# SECTOR_DEEP_SEMI — AI-compute / semiconductors epicenter · 2026-07-17 (Fri)

> Stage 5 / L1·DEEP. **PRE-MORTEM-PROMOTED, continuous track.** ROTATION picked 3 DEEPs (FIN/HLTH/ENRG) —
> IT/SEMI is UW and not a rotation DEEP target by rule. This leg exists because 3 of 4 PREMORTEM lenses
> independently attacked the desk's P2 "AI-capex sign-flip" proposition (`BLINDSPOT_PREMORTEM.md` §2,
> binding). **Job: resolve P2 vs P2′ vs a plain dip.** Carries the 07-15 value-chain map, players, and
> bottleneck **by reference** — see `llm_outputs/2026-07-15/industry_US/SECTOR_DEEP_SEMI.md` — and spends
> the budget on the delta. Zero buy/sell calls. Data: `module_flow`, `us_flow` FINRA short-vol,
> `module_chart --read`, `module_news_data`, EDGAR primary filings (INTC 10-Q, TSM 6-K).

---

## 1. DELTA vs 07-15 (lead with this)

On 07-15 the epicenter was in the **"not-yet-chased-by-flow"** state: news velocity accelerating (TSM
1.87x), price-flow still neutral, OBV mixed, Nasdaq 4%ile crowded-short read as squeeze fuel. Two days
later, every one of those inputs fired **and the tape did not confirm the setup as bullish**:

- **TSM (07-16 pre-open):** record Q2 — revenue **$40.20B (+33.7% YoY, +12.0% QoQ)**, gross margin 67.7%,
  operating margin 60.3% [primary: EDGAR 6-K, accession 0001046179-26-000451, EX-99.1] — **raised** Q3
  guide to **$44.6–45.8B** (implies another ~11% QoQ, ~+37% YoY at the midpoint) [primary, same filing].
  News-corroborated (multiple independent outlets, consistent figures): FY2026 capex raised to **$52–56B**
  (2025 was $40.9B) [Zacks/Yahoo 07-13], plus a **new $100bn Arizona commitment** ("four or more" fabs,
  including **advanced-packaging** capacity) taking the cumulative US pledge to **~$265bn** [SCMP, Yahoo,
  Yahoo(Nvidia-angle) — all 07-16/07-17]. This is unambiguous KPI acceleration by every fundamental measure.
- **The complex sold off anyway:** *"Chip Stocks Extend Rout as TSMC Results Fall Short of a High Bar"*
  [Bloomberg 07-17]; *"Chip Stock Selloff Deepens in Asia as TSMC Fails to Impress"* [Yahoo 07-17];
  *"no single catalyst behind the selloff, but we had TSMC's earnings shortly after"* [Deutsche
  Bank/FXStreet 07-17]; *"Trillion Dollar Chip Rout Trains Spotlight on TSMC and ASML Results"* [Bloomberg
  07-14, pre-print framing that the market front-ran].
- **The 07-15 squeeze-fuel setup did not resolve bullish.** RS20 across the named complex flipped sharply
  negative in the two trading days since (MU −16.5%, INTC −17.2%, LRCX −13.2%, KLAC −7.6%, SMH −7.7%) even
  as RS60 stayed strongly positive (MU +84.3%, INTC +41.7%, AMAT +37.3%) — a violent short-horizon de-rate
  laid on top of an intact medium-term uptrend, not a trend reversal.
- **META's capex was rewarded the same week** (+0.789 flow_score, 🟢가속, RS20 +10.7% vs RS60 −6.9% =
  reversal signature, OBV chart CONFIRMED-TURN +108% 20d slope) — this divergence is now **stronger**, not
  weaker: META's flow delta is still **+0.037** (still gaining) even after two more sessions.
- **INTC was promoted into this DEEP** on 07-15's premortem for its **07-23 earnings fulcrum** — unchanged,
  now 6 days out (see §7).
- **Net effect:** the desk's original P2 (broad AI-capex sign-flip) did not get cleaner in 2 days; the
  premortem's P2′ narrowing (capital-intensity de-rate, not a demand-side flip) is the hypothesis this run
  tests against fresh OBV/short-vol data (§2, §8).

## 2. Flow cross-check — epicenter vs memory vs semicap vs periphery split

### 2a. `module_flow` snapshot (2026-07-17, bench SPY)
| Ticker | flow tag | OBV | RS20 | RS60 | vol surge |
|---|---|---|---|---|---|
| NVDA | 🟡중립 | 중립 | −0.1% | −3.3% | 0.81x |
| TSM | **🔴분산** | **분산 (distribution)** | −3.8% | +6.0% | **1.13x** |
| MU | 🟡중립 | 중립 | −16.5% | +84.3% | 0.73x |
| AVGO | 🟡중립 | 중립 | −0.7% | −12.2% | 0.69x |
| INTC | 🟡중립 | 중립 | −17.2% | +41.7% | 0.76x |
| AMAT | 🟡중립 | 중립 | −1.3% | +37.3% | 0.72x |
| LRCX | 🟡중립 | 중립 | −13.2% | +16.0% | 0.83x |
| KLAC | 🟡중립 | 중립 | −7.6% | +15.6% | 0.80x |
| SMH | 🟡중립 | 중립 | −7.7% | +16.7% | 0.81x |
| META | **🟢가속** | **매집 (accum)** | **+10.7%** | −6.9% | 1.22x |

**TSM is the only name in the named set with a confirmed flow tag flip to distribution AND the only
volume surge >1.0x** — the market is putting real turnover behind selling TSM specifically, not the
complex generically. Everything else is 🟡 neutral tag but with RS20 sharply negative — beta-drag, not a
confirmed independent distribution signal (see chart OBV states in §2c).

### 2b. `SECTOR_FLOW_US.json` (asof 2026-07-16, us_top300) — flow_score + 1-day delta
| Ticker | flow_score | tag | OBV state | delta (1d) | Read |
|---|---|---|---|---|---|
| META | **0.789** | 🟢가속 | 매집 | **+0.037** | still gaining — capex-reward thesis strengthening, not fading |
| ASML | 0.129 | 🟡중립 | 중립 | **+0.234** | **best delta on the board** — the EUV monopoly is diverging *positively* inside a red equipment basket |
| AVGO | −0.060 | 🟡중립 | 중립 | −0.336 | fading but not distributing |
| ANET | −0.067 | 🟡중립 | 중립 | −0.291 | fading |
| AMAT | −0.087 | 🟡중립 | 중립 | −0.176 | fading, OBV neutral (not distributing) |
| AMD | −0.088 | 🟡중립 | 중립 | −0.471 | fading |
| NVDA | −0.264 | 🟡중립 | 중립 | −0.093 | fading, OBV neutral — **the bellwether is not distributing** |
| MRVL | −0.315 | 🟡중립 | 매집(accum) | −0.034 | still accumulating on OBV despite RS20 −32.5% |
| LRCX | −0.438 | 🟡중립 | 중립 | −0.090 | fading, OBV neutral |
| INTC | −0.575 | 🟡중립 | 중립 (flow) / **분산 on chart** | −0.155 | see §2c — flow-table OBV ≠ chart OBV read, chart is more current |
| MU | −0.577 | 🟡중립 | 중립 (flow) / **매집 on chart** | −0.236 | see §2c — **chart OBV says accumulating, not distributing** |
| KLAC | −0.594 | 🟡중립 | 중립 | −0.430 | worst delta in equipment |

*(TSM is not in the us_top300 universe — foreign private issuer/ADR exclusion — hence covered via
`module_flow`/`us_flow` direct calls above, not this table.)*

### 2c. `module_chart --read` — the split that resolves the flow-table ambiguity
```
MU:   OBV: 누적(매수압력↑) (20d기울기 +52%) · 다이버전스 없음 · MA 혼조 1/4위
      볼린저 확장39.6%·중단 · RSI 21.0 (deeply oversold) · 모멘텀20d −18.2%
      턴-판정: NEUTRAL/CHOP · 스탑: 853.20   ← MU's LAST PRICE (853.20) IS the anti-signal trigger, exactly.

TSM:  OBV: 분배(매도압력↑) (20d기울기 −99%) · 다이버전스 없음 · MA 혼조 1/4위
      볼린저 수축(코일링)15.4%·하단밴드 · RSI 42.1 · 모멘텀20d −5.2%
      턴-판정: PULLBACK-TO-SUPPORT · 스탑: 409.74

INTC: OBV: 분배(매도압력↑) (20d기울기 −73%) · 다이버전스 없음 · MA 혼조 1/4위
      볼린저 확장43.8%·중단 · RSI 26.4 (oversold) · 모멘텀20d −19.9%
      턴-판정: NEUTRAL/CHOP · 스탑: 96.98

META: OBV: 누적(매수압력↑) (20d기울기 +108%) · 다이버전스 없음 · MA 혼조 3/4위
      볼린저 확장30.0%·중단 · RSI 72.9 (hot/extended) · 모멘텀20d +17.1%
      턴-판정: CONFIRMED-TURN · 스탑: 542.87
```
**This is the load-bearing read of the run.** OBV (actual money flow, not price) confirms **only TSM and
INTC are genuinely distributing**. **MU's OBV is still accumulating** (+52% 20d slope) despite RS20 −16.5%
— it is oversold-on-price but not sold-on-flow, exactly the "caught in tape-wide beta, not its own
fundamental re-rate" signature the premortem flagged. MU's RSI of 21.0 and its close sitting exactly at
the 853.20 stop level means the anti-signal is live *right now*, not hypothetical.

### 2d. FINRA short-vol pressure (`us_flow.py`, Reg SHO 2026-07-16)
| Ticker | short% | base20 | Z | 5v5 trend | verdict |
|---|---|---|---|---|---|
| **NVDA** | 45.7% | 36.7% | **+1.67** | +3.3▲ | **🔴 short-vol surging (own-base extreme)** |
| TSM | 44.0% | 35.7% | +1.05 | +0.6▲ | 🟡 normal range, building |
| MU | 36.6% | 40.0% | −0.44 | −0.1· | 🟡 normal |
| INTC | 33.0% | 41.8% | −1.14 | −1.1▼ | 🟡 normal, falling — **not** a crowded-short setup |
| AMAT | 30.7% | 36.9% | −0.67 | +3.3▲ | 🟡 normal |
| LRCX | 29.8% | 33.8% | −0.41 | +5.4▲ | 🟡 normal |
| KLAC | 40.7% | 34.0% | +0.57 | +9.8▲ | 🟡 normal, building |

**New this run:** NVDA's own-base short-volume ratio is now the single most extreme reading on the board
(Z +1.67, red), even though NVDA's *price* RS is the most resilient in the complex (RS20 ≈ flat). This is
not necessarily a crowded-short (that read is the separate Nasdaq-100 COT 4%ile metric, unchanged since
07-15) — it is a rising rate of short-side hedging/dispersion activity building **underneath** a bellwether
that is otherwise holding. Flag it as a watch item, not yet a verdict-mover: NVDA's OBV is still neutral
(not distributing) and RS20 has not broken.

### 2e. The split, stated plainly
- **Epicenter core (foundry+GPU+ASIC): NVDA holds, TSM breaks (on real OBV distribution + volume), AVGO
  fades without distributing.** Not monolithic — TSM's break is idiosyncratic to the "high-bar" reaction,
  not shared by NVDA.
- **Memory (MU): price broke, flow did not.** OBV accumulating through a −16.5% RS20 drawdown.
- **Semicap (AMAT/LRCX/KLAC): red flow_score, neutral OBV, still positive RS60.** Trading as the tape's
  beta, not showing independent distribution — except **ASML**, whose delta is the best on the entire
  board (+0.234), the cleanest sign the EUV/equipment leg is not itself rolling over on fundamentals.
- **Periphery (META, the hyperscaler-owns-demand leg): still accelerating**, OBV accumulating harder than
  any other name in the set (+108% 20d slope), delta still positive.

This is not the shape of a demand-side, complex-wide sign-flip. It is the shape of **one name (TSM)
genuinely re-rated on a "high bar" plus one entangled name (INTC) genuinely distributing on its own
setup, sitting inside a basket where everything else is beta-dragged but not independently sold.**

## 3. Players (carried from 07-15, unchanged monopoly-layered chain — see prior file for the full 8-node
map). Bounded set named ≥2x in this run's news window, real ticker, mcap ≥ ~$2B:
**NVDA, TSM, AVGO, MU, INTC, AMD, ASML, AMAT, LRCX, KLAC, META, MRVL, ANET.** GOOGL appears only as
context (COMM-UW driver per premortem §3a, not a SEMI player). No new node/player entered the bounded set
this run — SK Hynix/Samsung/Foxconn appear repeatedly in the news window but are foreign-listed, out of
scope for this US-desk universe.

## 4. IR anchor — primary filings, verified this run

**TSM — primary source is a 6-K (foreign private issuer; no 10-K exists — `module_business_us TSM` returns
"no 10-K filing found," confirmed, this is expected FPI status, not a data gap).** Pulled directly from
EDGAR: 6-K filed **2026-07-16**, accession **0001046179-26-000451**, exhibit EX-99.1 (earnings release):
- Q2 2026 consolidated revenue **US$40.20B** (+33.7% YoY, +12.0% QoQ); gross margin 67.7%; operating margin
  60.3%; net margin 55.6%. 2nm shipments 3% of wafer revenue (ramping); advanced tech (≤7nm) = 77% of wafer
  revenue.
- Q3 2026 guide (management, primary): revenue **US$44.6–45.8B**; gross margin 65–67%; operating margin
  56–58%.
- The FY2026 capex raise (**$52–56B**, vs $40.9B in 2025) and the **$100bn Arizona / ~$265bn cumulative US**
  commitment are **not present in the EX-99.1 press release or the EX-99.2 investor-presentation exhibit
  filed with this 6-K** (checked directly — the presentation exhibit contains no extractable capex text,
  likely image-only slides) — those figures come from the earnings-call transcript, reported consistently
  across independent outlets (SCMP, Yahoo Finance ×2, Zacks) but **not independently re-verified against a
  primary transcript in this run**. Flagged, not treated as unverified-and-discarded: the multi-outlet
  consistency on exact dollar figures is a reasonable corroboration bar, but it is news-sourced, not
  primary-sourced, for the capex number specifically.

**INTC — primary source: 10-Q for the quarter ended 2026-03-28, filed 2026-04-24, accession
0000050863-26-000079** (most recent primary financials ahead of the 07-23 print). Intel Foundry segment,
verified directly from the filing text:
| | Q1 2026 (ended Mar 28) | Q1 2025 (ended Mar 29) | YoY |
|---|---|---|---|
| Intel Foundry segment revenue (intersegment) | **$5,421M** | $4,667M | **+16.2%** |
| Intel Foundry operating loss | $(2,437)M | $(2,320)M | loss widened in $, narrowed in % |
| Intel Foundry operating margin | (45)% | (50)% | **improving** |
| Third-party (external) foundry/assembly/test revenue | **$174M** | $31M | **+461%** (small base) |

This is the primary-source confirmation behind the "Intel Foundry revival" narrative cited in news
(HSBC 07-09, Bristlemoon Q2 letter 07-14): segment revenue growing, losses narrowing as a percentage, and
external-customer revenue — the number that actually matters for the "foundry pitch is working" thesis
— up more than 5x YoY off a small base. The 10-K (filed 2026-01-23, FY2025) risk factors explicitly flag
*"the shift in data center spend to GPUs to support AI workloads"* as a named risk to Intel Products —
i.e., Intel's own filing acknowledges the AI-GPU shift is a headwind to its non-foundry segments, which is
consistent with foundry (not CCG/DCAI) being the segment with the cleaner AI-capex-driven growth story
into the 07-23 print.

## 5. Value-chain node map — carried by reference

Unchanged from 07-15 (`llm_outputs/2026-07-15/industry_US/SECTOR_DEEP_SEMI.md` §Players+IR anchor): the
8-node monopoly-layered chain (EDA/IP → litho/ASML → WFE/AMAT-LRCX-KLAC → foundry/TSM → advanced
packaging-CoWoS → HBM/MU → compute silicon/NVDA-AVGO-AMD → networking/ANET-AVGO). **No new node this run.**

**Bottleneck — binding constraint confirmed unchanged and intensifying, not resolved:** advanced-packaging
(CoWoS) + HBM remain the throttle, not GPU demand. New evidence this run **strengthens** rather than
changes this: HBM/DRAM described as *"unprecedented supply shortage"* [07-16]; TSM's new $100bn Arizona
commitment explicitly includes "advanced packaging fabs" [Yahoo 07-17] — i.e., TSM itself is treating
advanced packaging as the capacity to add, which is confirmation-by-capex-allocation that this is still
the binding constraint, not a solved problem. This is a multi-year capacity build, not a near-term fix —
the bottleneck persists through the horizon relevant to this run.

## 6. Chain-hop candidates

`chain-hop "TSMC capex" "Intel foundry" --days 14 --scope foreign` returned **zero body-proximate,
headline-unnamed candidates** — every ticker that surfaced (INTC 11 headline hits, NVDA, GOOGL, AAPL,
NDAQ, MU, ASML, UNH) is headline-named, i.e., already crowded/named, not a chain-hop candidate by the
stage's own rule (a news co-mention alone is not a candidate; the bar is proximity ≥2 co-mentions **with
zero headline appearances**). **No candidates cleared the bar this run.** Stated explicitly rather than
stretching a headline name into a "discovery."

## 7. Track-KPIs + anti-signals (observables)

### KPIs (accelerating, unchanged direction from 07-15, several now primary-confirmed)
- TSM Q3 guide $44.6–45.8B (primary, EDGAR 6-K) — sequential acceleration confirmed.
- FY26 capex $52–56B / cumulative US commitment ~$265bn (news-corroborated, not primary-verified this run).
- Intel Foundry segment revenue +16.2% YoY, external-customer revenue +461% YoY (primary, 10-Q Q1'26).
- HBM/DRAM "unprecedented shortage" persisting/intensifying [07-16].
- META capex-reward flow delta still positive (+0.037) two sessions after the original read.
- ASML flow_score delta +0.234 — the single best-improving name in the whole named set.

### Anti-signals — the desk's standing set, unchanged, plus one live-right-now flag
1. **MU holds 853.20** — unchanged from 07-15, but MU's **last print (853.20) is exactly at this level
   right now** [SECTOR_FLOW_US.json asof 07-16]. This is not a distant trigger; it is live.
2. **SMH RS20 turns positive** — currently −7.7%, unchanged direction (still negative) since 07-15.
3. **(New, from premortem) If META rolls over** (RS20 negative + OBV → distribution) — currently the
   opposite is true: META's OBV chart read is CONFIRMED-TURN, RS20 +10.7%, flow delta still rising.
4. **New this run: NVDA short-vol Z +1.67 (red, own-base extreme)** — a building-pressure watch item, not
   yet a trigger (OBV still neutral, RS20 not broken), but the first FINRA-level red flag on the
   bellwether since this leg opened.
5. **TSM distribution persisting 2+ sessions on rising surge** (from the 07-15 file's refutation-path
   framing) — **already partially live**: TSM chart shows OBV distribution (−99% 20d slope) and the
   `module_flow` volume surge (1.13x) is the only >1.0x reading in the set. One more session of the same
   pattern would confirm rather than merely flag this.

## 8. RESOLUTION VERDICT

**(b) — narrow capital-intensity de-rate (P2′), not (a) a broad AI-capex sign-flip and not (c) a plain
dip in a uniformly live cycle. Committing to this, not splitting it.**

**Defense:** the OBV (money-flow) split in §2c is the decisive evidence, not price/RS20 alone. Distribution
— actual selling pressure, not just a red RS number — is confirmed in exactly **two** names: **TSM** (the
capital-intensive foundry leg reacting to a genuinely high bar despite record results and a raised guide)
and **INTC** (its own distinct, entangled setup — see §7 of the 07-15 file's promotion and §7 above).
Everywhere else the picture contradicts a demand-side sign-flip:
- **MU's OBV is still accumulating** through a −16.5% RS20 drawdown — it is being sold on the tape's beta,
  not on its own fundamentals (no MU-specific KPI miss exists; HBM shortage and $250B AI-memory investment
  and $100B Ford backlog are all still-live tailwinds).
- **The semicap basket (AMAT/LRCX/KLAC) shows negative flow_score but neutral OBV** — beta-drag, not
  independent distribution — and **ASML's delta is the best-improving name in the entire named set**,
  the opposite of what a capex-demand sign-flip would produce in the EUV monopoly.
- **META's capex-reward thesis has not just held, it strengthened** two sessions later (flow delta still
  positive, OBV accumulating hardest of any name here, RS20/RS60 reversal signature intact).
- **NVDA — the bellwether — has not broken**: OBV neutral, RS20 ≈ flat. The one new wrinkle (short-vol Z
  +1.67) is a positioning/hedging signal building underneath, not yet a price or flow break.

This is the signature of **a valuation reset concentrated in the capital-intensive foundry leg (TSM),
entangled with one idiosyncratic name (INTC) ahead of its own binary, sitting inside a basket that is
trading on beta but has not itself re-rated on fundamentals.** It is narrower than (a) and it is not (c)
either — (c) cannot explain why TSM alone shows genuine distribution+volume while MU/NVDA/META do not; a
uniform "live cycle, just a dip" read would not produce this split.

**What would flip this verdict:**
- **→ toward (a) broad sign-flip:** MU's OBV flips from 매집 to 분산 **and** SMH RS20 fails to reclaim
  positive **and** TSM's distribution persists 2+ more sessions on rising volume surge — i.e., the
  distribution currently isolated in TSM spreads into the names that are still flow-clean.
  **MU's 853.20 stop is live right now** — the single closest trigger to firing.
- **→ toward (c) plain dip, nothing narrow about it:** if the entire named set's RS20 reclaims positive
  within the next 1–2 weeks without any KPI deterioration, the "capital-intensity" distinction was never
  load-bearing — it was just noise in a uniform snap-back.
- **INTC 07-23 is the dated fulcrum that cuts across both branches** (see below) — because TSM's raise was
  reported as partly defensive against Intel Foundry share gains [Barron's/Yahoo 07-16: *"Taiwan Semi
  Plans Extra $100 Billion in U.S. Investment as It Fights Intel Challenge"*], INTC's print is not a
  side-show: a genuine data-center/foundry beat corroborates the "TSM raised because Intel's foundry pitch
  is real" reading (supports P2′ — TSM's re-rate is idiosyncratic-defensive, not demand-side); an
  in-line/miss removes that leg of the P2′ case and would make TSM's distribution look more like the
  leading edge of a broader capital-intensity unwind. Primary-source Intel Foundry data (segment revenue
  +16.2% YoY, external revenue +461% YoY, loss margin narrowing) points toward the beat side of that
  binary, but is one-quarter-old (Q1, not the Q2 print itself) — genuinely unresolved. **Falsifier for the
  whole INTC leg: in-line/miss on data-center/foundry revenue + RS20 making new lows post-print.**

---
**EXIT CHECK:** ✅ DELTA led (§1) · ✅ flow cross-check with epicenter/memory/semicap/periphery split (§2)
· ✅ players bounded (§3) · ✅ IR anchor — primary EDGAR sources pulled and verified for both TSM (6-K) and
INTC (10-Q), discrepancy between primary and news-only figures flagged explicitly (§4) · ✅ value-chain
carried by reference, bottleneck re-confirmed with new evidence (§5) · ✅ chain-hop run, zero candidates
cleared the bar, stated not stretched (§6) · ✅ KPIs/anti-signals as observables, one flagged live-now
(MU 853.20) (§7) · ✅ RESOLUTION VERDICT committed (b), flip observables named, does not split the
difference (§8).
