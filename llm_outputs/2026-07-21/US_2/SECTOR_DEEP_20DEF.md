# SECTOR_DEEP_20DEF — Defense / Aerospace — 2026-07-21

**Sub-sector:** Defense / Aerospace (promoted sleg of Industrials, GICS 20) · **Cycle registry #3** = Missile-defense / rearmament
**Epicenter:** RTX (broadest missile/air-defense mix, most liquid) · LMT (pure-play) · NOC · GD · LHX
**Promotion origin:** PREMORTEM Lens 1 (zero-coverage hole in #3 secular cycle) + Lens 4 (three earnings prints in-window) converged.
**Momentum tag:** EXTENDED-BUT-LIVE — backlog conversion is the KPI, still building.
**Data asof:** flow 2026-07-20 (FINRA Reg SHO), fundamentals/chart intraday 2026-07-21, NOC print 2026-07-21 pre-open.

> Scope note: this file produces deterministic data + observed catalysts and *justifies or refutes the promotion*. **Zero buy/sell recommendations.** Judgment on positioning is left to the bet-sheet stage.

---

## 1. Flow read — is defense diverging UP within a weak Industrials tape?

Parent context: **SECTOR_FLOW Industrials wflow −0.22, 20 red names** — weak sector flow. The sub-sector question is whether defense diverges.

Per-name FINRA Reg SHO short-volume ratio (asof 2026-07-20), from `scripts/us_flow.py RTX LMT NOC GD LHX`:

```
TICKER   SHORT%   BASE20      Z    5v5trend  date        verdict
RTX      57.8%    42.9%    1.64    -1.1▼   2026-07-20  short-vol spike (extreme vs own base)
LMT      37.0%    40.8%   -0.62    -3.8▼   2026-07-20  normal range
NOC      55.1%    39.5%    1.37    -2.8▼   2026-07-20  normal range
GD       36.6%    46.6%   -1.41    -3.4▼   2026-07-20  normal range
LHX      36.4%    32.7%    0.51    +3.8▲   2026-07-20  normal range
```

**Read — two-speed, not a clean up-divergence:**
- **RTX (z +1.64) and NOC (z +1.37)** carry elevated short-volume into their prints — this is pre-earnings hedging/positioning, not necessarily directional bearishness. Both have **negative 5v5 trend** (−1.1, −2.8), i.e. the short intensity is already *rolling off* day-over-day. Classic "hedge into the event, cover after."
- **LMT (z −0.62), GD (z −1.41), LHX (z +0.51)** sit in normal-to-light territory. GD is the *least* shorted relative to its own base — no bearish pressure.
- The **corroborating divergence tell is on the tape, not the short-book**: chart OBV (§6) shows **LMT +23% and NOC +28% 20-day OBV slope (accumulation)** while price sits *below all four MAs* in a bearish stack and Bollinger bands are squeezed 10–13% (coiling). Quiet accumulation under a weak Industrials tape, no price confirmation yet.

**Verdict on flow:** Defense is **NOT yet diverging UP on price** (all three primes NEUTRAL/CHOP, price 0/4–4/4 MA, momentum flat). It IS showing **stealth accumulation + pre-event short-hedging that is already rolling off** — a coiled setup, not a breakout. The divergence is *latent* and event-gated on the 7/23 prints, not confirmed. This is consistent with the EXTENDED-BUT-LIVE tag: buying pressure is building under the surface, but the tape has not broken the primes out of a weak parent.

---

## 2. Players (bounded — real ticker, mcap ≥ ~$2B)

**Primes (systems integration):**
| Ticker | Name | Mcap | Role |
|---|---|---|---|
| RTX | RTX Corp | $264B | Missiles/air-defense (Raytheon) + Collins + Pratt — broadest mix, most liquid = cleanest epicenter |
| LMT | Lockheed Martin | $116B | Pure-play prime — F-35, Missiles & Fire Control (PAC-3, JASSM), Space |
| NOC | Northrop Grumman | $73B | B-21, Sentinel ICBM, Space, munitions/solid-rocket-motors |
| GD | General Dynamics | ~$110B+ | Combat systems, Gulfstream, submarines (Electric Boat), IT |
| LHX | L3Harris | ~$45B+ | C4ISR, comms, Aerojet Rocketdyne (solid rocket motors) |

**Tier-1 suppliers / components / services (∪):**
| Ticker | Name | Role |
|---|---|---|
| HII | Huntington Ingalls | Nuclear shipbuilding (carriers, submarines) — sole/near-sole supplier |
| TDG | TransDigm | Highly-engineered aircraft components, proprietary aftermarket |
| HWM | Howmet Aerospace | Engine components, titanium structures, fasteners |
| AXON | Axon Enterprise | Tasers, body-cams (adjacent gov/defense-tech) |
| KTOS | Kratos Defense | Unmanned systems, target drones, **solid rocket motors** (munitions pure-play adjacency) |
| LDOS | Leidos | Defense IT / services integration |
| BAH | Booz Allen Hamilton | Defense consulting / digital / AI services |

**Munitions / drone pure-play adjacencies:** KTOS (SRMs, drones), AVAV (AeroVironment — loitering munitions/Switchblade, if ≥$2B). Solid-rocket-motor and energetics capacity is the scarce input (see §4 bottleneck).

---

## 3. IR anchor — NOC's actual 7/21 print + RTX/LMT 7/23 setup

### NOC Q2 2026 — reported 2026-07-21 pre-open (ACTUAL, cited)
- **EPS $7.68** diluted vs consensus **$6.89** → **beat ~+11.5%** (+$0.79) ([StockStory/FinancialContent](https://markets.financialcontent.com/stocks/article/stockstory-2026-7-21-northrop-grummans-nysenoc-q2-cy2026-sales-beat-estimates), [ChartMill](https://www.chartmill.com/news/NOC/Chartmill-51267-Northrop-Grumman-NYSENOC-Delivers-Mixed-Q2-Results-With-Strong-Earnings-Beat-and-Record-Backlog))
- **Revenue $10.88–10.9B, +5% YoY** (vs $10.4B Q2'25); ~0.3% *below* the $10.91B revenue estimate — a slight top-line miss on a big EPS beat ("mixed") ([SeekingAlpha](https://seekingalpha.com/news/4615846-northrop-grumman-raises-2026-outlook-as-backlog-hits-record-105b))
- **Record backlog $105B, +17% YoY** ([SeekingAlpha](https://seekingalpha.com/news/4615846-northrop-grumman-raises-2026-outlook-as-backlog-hits-record-105b), [GuruFocus](https://www.gurufocus.com/news/8968776/northrop-grumman-noc-reports-strong-q2-earnings-raises-2026-guidance))
- **Net awards ~$20B** in the quarter → implied **book-to-bill ≈ 1.84x** ($20B / $10.88B) — **well above the 1.0 healthy line** ([Ticker Report](https://www.tickerreport.com/banking-finance/13510480/northrop-grumman-nysenoc-updates-fy-2026-earnings-guidance.html))
- **Guidance RAISED:** FY26 MTM-adj EPS to **$28.60–29.10** (+$1.20, vs $27.95 consensus); sales to **$43.75–44.25B**; **FCF maintained $3.1–3.5B** ([GuruFocus](https://www.gurufocus.com/news/8968776/northrop-grumman-noc-reports-strong-q2-earnings-raises-2026-guidance), [Ticker Report](https://www.tickerreport.com/banking-finance/13510480/northrop-grumman-nysenoc-updates-fy-2026-earnings-guidance.html))
- **Market reaction: stock fell ~2.7% despite the beat + raise + record backlog** — a "sell-the-news" tape ([ChartMill](https://www.chartmill.com/news/NOC/Chartmill-51267-Northrop-Grumman-NYSENOC-Delivers-Mixed-Q2-Results-With-Strong-Earnings-Beat-and-Record-Backlog)).

> ⚠ Premortem-input correction: the run brief carried NOC backlog at $95.6B; the **actual print is $105B (+17% YoY)** — the demand signal came in *stronger* than the promotion assumed, while the stock still sold off. That is the single most important fact in this file (see §8).

### RTX — reports 7/23 pre-open (SETUP)
- Consensus **EPS $1.66** (range $1.61–1.74) on **revenue ~$22.88B** ($22.51–23.27B), 18 analysts ([AlphaStreet](https://news.alphastreet.com/rtx-q2-2026-earnings-preview-july-23-street-expects-1-66-eps/))
- Missile-demand watch items: **$1.1B US Navy AIM-9X Block II** award, plan to scale to ~2,500 missiles/yr; doubling Stinger capacity with European partners; SM-6/Tomahawk ramps ([CryptoDaily preview](https://cryptodaily.co.uk/2026/07/rtx-earnings-defense-demand-guidance), [Defense One](https://www.defenseone.com/business/2026/02/primed-production/411145/))
- **Book-to-bill sustainability flagged as the key watch item.** Run-context backlog anchor: RTX ~$271B.

### LMT — reports 7/23 pre-open (SETUP)
- Consensus **EPS ~$7.22–7.28** on **revenue ~$19.52B (+7.5% YoY)** ([AlphaStreet](https://news.alphastreet.com/lockheed-martin-q2-2026-earnings-preview-july-23-street-expects-7-22-eps/))
- Watch: **F-35 delivery volumes + production-rate guidance**, Missiles & Fire Control margins, classified-program awards, Europe/APAC international orders, and **any FY guidance revision** ([TradingView/Zacks](https://www.tradingview.com/news/zacks:4a984b7c6094b:0-is-lockheed-martin-stock-worth-buying-before-q2-earnings-release/)). Run-context backlog anchor: LMT ~$194B.

**Backlog / book-to-bill scoreboard (per prime):**
| Prime | Backlog | Book-to-bill signal |
|---|---|---|
| NOC | **$105B (+17% YoY, record)** | **~1.84x Q2 (confirmed healthy)** |
| RTX | ~$271B (run-context) | 7/23 — the watch item |
| LMT | ~$194B (run-context) | 7/23 — the watch item |

---

## 4. Value-chain map (DoD dollar → export) + binding constraint

```
[1] DoD BUDGET / APPROPRIATIONS
    FY27 request $1.5T (base disc. ~$1.15T + ~$350B reconciliation/mandatory);
    +$445B over FY26 = largest defense increase since Korean War.
    NATO combined >$1.5T for first time; EU €454B (2.4% GDP), path to 5% GDP.
      │  (gated by: appropriations passage / CR risk / reconciliation execution)
      ▼
[2] PRIMES — systems integration  (RTX, LMT, NOC, GD, LHX)
    Convert budget → programs → backlog. Record backlogs; NOC b-t-b ~1.84x.
      │
      ▼
[3] TIER-1 SUPPLIERS  (HII shipyards, TDG components, HWM structures, LHX/Aerojet, KTOS)
      │
      ▼
[4] COMPONENTS / MUNITIONS / ENERGETICS   ★ BOTTLENECK ★
    Solid rocket motors (long lead, constrained energetics),
    nitrocellulose (single global chokepoint), tier-2/tier-3 single-point failures.
      │
      ▼
[5] SUSTAINMENT / AFTERMARKET   (TDG proprietary aftermarket, LDOS/BAH services, spares)
      │
      ▼
[6] EXPORTS / FMS   (Foreign Military Sales — Europe rearmament, Stinger/Patriot/F-35 allied demand)
```

**Binding constraint = [4] munitions / energetics production capacity, NOT appropriations and NOT the primes.**
- The Pentagon found **"hundreds of single-point failures"** replenishing stockpiles post-2022; chokepoints sit at **tier-2/tier-3**, not final assembly ([War on the Rocks: "The Primes Aren't the Real Bottleneck"](https://warontherocks.com/2026/01/the-primes-arent-the-real-bottleneck-in-u-s-weapons-production/), [Military.com](https://www.military.com/feature/2026/04/03/americas-munitions-bottleneck-becoming-national-security-problem.html)).
- **Solid rocket motors**: long lead times, constrained energetics; output lags demand even when primes expand assembly ([Deloitte](https://www.deloitte.com/us/en/insights/industry/aerospace-defense/us-defense-manufacturing-industrial-scale.html)).
- **Nitrocellulose**: the entire small-arms/artillery chain runs through one global gunpowder chokepoint ([Homeland Arms](https://homelandarms.com/news/the-nitrocellulose-crisis-why-america-cant-make-enough-gunpowder/)).
- Policy response: **2026 spending bill = $6.3B critical munitions + $500M solid-rocket-motor industrial base**; RTX lifted munitions output +20% and wants more in 2026 (SM-6, Tomahawk) ([Defense One](https://www.defenseone.com/business/2026/02/primed-production/411145/)).

**Implication:** demand (budget, backlog) is the *tailwind*; the *rate-limiter on revenue conversion* is throughput at the energetics/SRM tier. That is exactly why book-to-bill and backlog *conversion* — not backlog size — is the KPI (EXTENDED-BUT-LIVE).

---

## 5. Chain-hop candidates (under-named suppliers — all "needs flow cross-check")

- **KTOS (Kratos)** — solid rocket motors + unmanned/target drones; direct exposure to the [4] bottleneck. *needs flow cross-check.*
- **LHX (Aerojet Rocketdyne inside L3Harris)** — SRM prime supplier to the energetics chokepoint; already in the prime set but the SRM node is the under-appreciated piece. *needs flow cross-check.*
- **HWM (Howmet)** — engine components/titanium, dual commercial-aero + defense; throughput leverage. *needs flow cross-check.*
- **TDG (TransDigm)** — proprietary aftermarket/sustainment [5], pricing power; margin-defensive. *needs flow cross-check.*
- **HII (Huntington Ingalls)** — near-sole nuclear shipbuilder; submarine/carrier backlog leverage. *needs flow cross-check.*
- **AVAV (AeroVironment)** — loitering munitions/Switchblade (verify mcap ≥$2B). *needs flow cross-check.*
- Energetics/nitrocellulose pure-plays are largely **private/foreign** — the listed chokepoint is hard to express in a single US-listed ticker; watch primes' capex guidance for who is funding the expansion.

---

## 6. Deterministic data

### Valuation table (module_fundamentals_us, asof 2026-07-21)
| | RTX | LMT | NOC |
|---|---|---|---|
| Price | $195.85 | $504.96 | $512.68 |
| Mcap | $263.7B | $116.4B | $72.8B |
| Trailing P/E | 36.74 | 24.46 | 16.07 |
| Forward P/E | 25.81 | 15.74 | 16.95 |
| PEG | 2.65 | 1.08 | 3.90 |
| P/S | 2.92 | 1.55 | n/a |
| P/B | 3.98 | 15.51 | 4.25 |
| Trailing EPS | 5.33 | 20.64 | 31.91 |
| Forward EPS | 7.59 | 32.09 | 30.24 |
| 52w range | 143.56–214.50 | 410.11–692.00 | 479.05–774.00 |
| Target mean / median | 215.36 / 220.00 | 606.68 / 600.00 | 669.50 / 652.50 |
| Target low / high | 180 / 242 | 487 / 756 | 533 / 815 |

**Valuation read (no recommendation):** RTX trades richest (fwd P/E 25.8, PEG 2.65) — the market pays up for the broadest missile mix. **LMT is the cheap prime** (fwd P/E 15.7, PEG 1.08) and sits near its 52w low ($505 vs 410–692) — de-rated. NOC (fwd P/E 17) is mid-range but ~34% below its 52w high ($513 vs $774) despite the record-backlog print. All three trade **below analyst target means**, and LMT/NOC well below.

### VERBATIM CHART_READ — module_chart --read

**RTX:**
```
OBV: 중립 (20d기울기 +1%)
다이버전스: 없음
MA정렬: 혼조 · 가격 4/4 MA 위
볼린저: 수축(코일링) 9.9% · 중단
RSI: 60.3 · 모멘텀20d +5.1%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 185.06
```

**LMT:**
```
OBV: 누적(매수압력↑) (20d기울기 +23%)
다이버전스: 없음
MA정렬: 약세스택(5<20<60<120) · 가격 0/4 MA 위
볼린저: 수축(코일링) 10.4% · 중단
RSI: 47.6 · 모멘텀20d +0.3%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>510.28 + OBV→누적 / 스탑(스윙저점): 491.64
```

**NOC:**
```
OBV: 누적(매수압력↑) (20d기울기 +28%)
다이버전스: 없음
MA정렬: 약세스택(5<20<60<120) · 가격 0/4 MA 위
볼린저: 수축(코일링) 13.4% · 중단
RSI: 51.5 · 모멘텀20d -0.1%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>520.39 + OBV→누적 / 스탑(스윙저점): 496.02
```

**Chart synthesis:** RTX = strongest tape (price 4/4 above MAs, RSI 60, +5.1% 20d momentum) but OBV only neutral. **LMT + NOC = the divergence signature**: OBV strongly accumulating (+23%, +28% slope) *while* price sits under a bearish MA stack (0/4) with bands squeezed 10–13%. Coiled, direction unconfirmed (all three NEUTRAL/CHOP). Ignition triggers: RTX already above MAs (needs OBV→accumulate), LMT close >510.28, NOC close >520.39.

---

## 7. Track-KPIs + anti-signals

**KPIs (health):**
- **Book-to-bill >1.0** — NOC ✅ ~1.84x (confirmed). RTX/LMT 7/23 = the live test.
- **Backlog $ + YoY** — NOC ✅ $105B (+17%, record). RTX ~$271B / LMT ~$194B to confirm 7/23.
- **FY27 appropriations passage** — $1.5T request; watch discretionary + $350B reconciliation execution.
- **Munitions throughput** — SRM/energetics output ramp (the §4 bottleneck); RTX +20% run-rate, scaling.
- **FMS/export bookings** — Europe €454B, NATO >$1.5T, Stinger/Patriot/F-35 allied demand.

**Anti-signals (flip the thesis):**
- **Book-to-bill <1.0** on any prime → EXTENDED tag flips to distribution. (KPI threshold from the momentum tag.)
- **Program charge** (fixed-price development write-down) — the classic prime margin landmine; would cap multiples.
- **CR / budget freeze / sequester overhang** — a continuing resolution stalls new-start funding regardless of the $1.5T request.
- **"Beat-and-raise still sells off"** — NOC beat EPS +11.5%, raised guide, record backlog, and **fell 2.7%**. If RTX/LMT repeat this pattern 7/23, it signals **the good news is priced** (valuation/positioning exhaustion), the sharpest anti-signal for an EXTENDED sub-sector.
- **Cross-bull caveat (Hormuz):** the 2026 Strait of Hormuz crisis (US strikes on Iran 7/11–7/15, shipping disruption) is a bullish *demand* catalyst for defense and cross-bull with Energy OW — but it is an **undated, event-driven** input; do not price a de-escalation or an escalation you cannot date ([CNN 7/11](https://www.cnn.com/2026/07/11/world/live-news/iran-war-trump), [Wikipedia: 2026 Strait of Hormuz crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis)).

---

## 8. Promotion verdict

### Verdict: **JUSTIFY-PROMOTION (conditional) — hold as the 5th DEEP through the 7/23 prints, with an explicit downgrade trip-wire.**

**Why the promotion was correct (evidence):**
1. **It was a real zero-coverage hole in the #3 secular cycle with live catalysts** — three prints in-window (NOC today, RTX+LMT 7/23). Lens 1 + Lens 4 convergence is vindicated on structure.
2. **The fundamental thesis is confirmed stronger than assumed.** NOC printed **EPS beat +11.5%, record backlog $105B (+17%, vs the $95.6B the premortem assumed), book-to-bill ~1.84x, and RAISED FY guidance.** The demand base case (record backlogs, $1.5T FY27 request, largest increase since Korea, NATO/EU rearmament) is intact and corroborated by primary prints and budget docs.
3. **A latent flow divergence exists** — LMT/NOC OBV accumulating hard (+23/+28% slope) under a weak Industrials tape (wflow −0.22), coiled Bollinger squeezes, pre-print short-hedging already rolling off. The setup is *live*.

**Why it is CONDITIONAL, not an unqualified win (the against-us evidence is also present):**
- **NOC beat-and-raised and still fell ~2.7%.** That is the premortem's own "against-us" scenario expressed not as a program charge but as **priced-in exhaustion** — the EXTENDED half of the tag is real. Good news is not moving these stocks up.
- **No confirmed price divergence.** All three primes are NEUTRAL/CHOP, below/among MAs, direction unconfirmed. The divergence is accumulation-only, not a breakout.
- **The binding constraint is throughput, not demand** — backlog *conversion* (KPI) gates revenue, and the energetics/SRM bottleneck is a multi-year fix.

**Decision rule for the desk (no position advice — a monitoring rule):**
- The promotion **holds** because the catalyst density (7/23 RTX+LMT) and the confirmed demand signal are exactly what a DEEP slot is for — the two biggest prints in the cycle land in 48 hours and the sub-sector was uncovered.
- **Trip-wire to DOWNGRADE-TO-WATCH:** if **RTX or LMT on 7/23 either (a) print book-to-bill <1.0, (b) take a program charge, or (c) beat-and-raise yet sell off like NOC**, the EXTENDED half wins — the news is priced, and defense reverts to the weak Industrials tape rather than diverging up. In that case downgrade to WATCH and let the flow (a confirmed OBV-driven break above the ignition triggers: LMT >510.28, NOC >520.39, RTX holding 4/4 MA) re-qualify it later.

**One-line:** The premortem was right to promote — the hole was real and the demand print (NOC $105B, b-t-b 1.84x, raise) confirms the thesis — but NOC's beat-and-fade proves the EXTENDED risk is live, so the promotion is justified **on watch for the 7/23 twin prints as the decider.**

---

*Sources: local modules (module_fundamentals_us, module_chart, scripts/us_flow.py, all asof 2026-07-20/21) + web (NOC Q2 print, RTX/LMT previews, FY27 budget, munitions bottleneck, Hormuz/rearmament — hyperlinked inline). No guessed numbers; run-context backlog anchors for RTX/LMT ($271B/$194B) flagged as unconfirmed pending 7/23. English-pure except verbatim Korean CHART_READ module output. Zero buy/sell recommendations.*
