# SECTOR_DEEP — STPL (Consumer Staples / 음식료·담배) · industry_KR · 2026-07-20 (Mon)

> **Track: ROTATING — FULL FRESH MAP.** STPL has never been deep-dived on the KR desk; this is
> the first map. Owner of **divergence D-3** from `SECTOR_ROTATION.md`.
> Zero sizing, zero buy/sell calls — BET owns those.

## ⚠ Freshness governs everything below
| Input | asof | Staleness |
|---|---|---|
| `SECTOR_FLOW_KR.json` (the sweep that promoted STPL) | **2026-07-16** | **2 sessions stale** at Monday pre-open |
| `module_flow` KIS 투자자별 20d actuals | **2026-07-20** (run today) | live |
| DART 공시 (`module_disclosure --days 60`) | 2026-07-20 pull | live |
| News FTS (`--scope domestic`) | 2026-07-20 pull | live |
| 원·달러 **1487.28원** | 07-20 [MACRO §1, brief #34] | live |

Every claim below carries its source and date. Where the 07-16 sweep and today's live re-check
disagree, **the live re-check wins and the disagreement is stated, not smoothed.**

---

## §0 D-3 VERDICT — the promotion was wrong. **Revert STPL to UW.**

**Question posed:** is 음식료·담배 **eqflow +0.205** (n=37, wflow +0.079, asof 07-16) a genuine
defensive rotation (M-07), or a won-scenario / input-cost artifact?

**Answer: ARTIFACT — but neither of the two offered artifacts.** It is a **corporate-governance
accumulation chain inside one family group, equal-weight-amplified by micro-caps.** The
won-strength hypothesis is not merely unproven, it is **contradicted by the primary bodies** — the
sector's actual live event is *price hikes forced BY a weak won*, the opposite sign of the scenario.

### The count that decided it
**6 🟢 / 0 🔴 out of 37** (breadth 0.16). Zero reds looks healthy — until the six are named:

| # | Name | Ticker | mcap | 07-16 tag | **Live 07-20 re-check** | What it actually is |
|---|---|---|---|---|---|---|
| 1 | 사조대림 | 003960.KS | ₩0.26조 | 🟢가속 | 🟢 매집, 기관 **−0.2만** | **사조 group** |
| 2 | 사조오양 | 006090.KS | ₩0.08조 | 🟢가속 | 🟢 매집, 기관 **+0.5만** | **사조 group** |
| 3 | 사조씨푸드 | 014710.KS | ₩0.15조 | 🟢가속 | 🟢 매집, 기관 **+1.5만** | **사조 group** |
| 4 | 한성기업 | 003680.KS | ₩0.06조 | 🟢가속 | 🟢 매집, 기관 +1.5만, **RS20 +215.7%, 서지 8.17x** | **애국테마주 meme** |
| 5 | 샘표식품 | 248170.KS | ₩0.10조 | 🟢가속 | 🟢 매집, 기관 **+0.2만** | micro-cap noise |
| 6 | 고려산업 | 002140.KS | ₩0.04조 | 🟢가속 | **🔴분산 — 외국인 −44.3만 / 개인 +43.4만** | **weak hands → 🟢 INVALIDATED** |

**Three numbers close it:**

1. **The six 🟢 are ₩0.70조 of a ₩46.34조 sector = 1.50% of sector market cap.** Median green
   mcap **₩0.101조** — every one is ~25× below the ₩2.5조 player floor. `eqflow` weights them
   equal to KT&G. **That gap — eqflow +0.205 vs wflow +0.079 — is not "breadth", it is the
   equal-weighting of six micro-caps.** ROTATION read the arithmetic of the metric as a market fact.
2. **Total 기관 20d net buy across the five surviving greens = +3.5만 주** (샘표 +0.2, 사조오양 +0.5,
   한성 +1.5, 사조씨푸드 +1.5, 사조대림 −0.2) [KIS via `module_flow`, 20d, asof 07-20]. **Less than
   KT&G's single-name 기관 +5.2만.** This is not institutional accumulation; it is rounding error.
   M-07 predicts *broad institutional accumulation across many mid-cap food names* — the measured
   institutional participation is **~zero**.
3. **Every one of the 4 names clearing the ₩2.5조 floor is 🟡 or worse**, and the two largest by
   flow-relevance are live-🔴 today: 삼양식품 🔴분산, **CJ제일제당 🔴분산 with 외국인 −8.5만 /
   개인 +2.9만 = ⚠개인 흡수(외국인 이탈)**. The investable sector has **zero** 🟢 names.

### The mechanism the sweep could not see — primary filings
`module_disclosure --days 60` (DART, pulled 07-20) shows a **sustained controlling-shareholder buy
chain across the 사조 group**, which is why four affiliates lit up simultaneously and read as breadth:

| Issuer | Filer (buyer) | Filing dates |
|---|---|---|
| **사조대림** (003960) | **사조산업** | 06-08, 06-25, **07-03, 07-10, 07-16** — 5 filings in 6 weeks |
| **사조오양** (006090) | **사조대림** | 06-08, **07-15** |
| **사조씨푸드** (014710) | **사조산업** | 06-25 |
| **사조산업** (007160) | **사조시스템즈**, **주진우**(회장) | 06-08, 07-02 |

Read left to right this is the group ladder **사조시스템즈 → 사조산업 → 사조대림 → 사조오양**, being
walked up by the family and its holding vehicles. The **07-16 사조산업 대량보유 + 임원소유 filings on
사조대림 land on the sweep's exact asof date.**

This explains every anomaly at once: OBV prints 매집 while 외국인/기관 are ~0 (the buyer files as
주요주주, not as 기관); multiple tickers move together (one buyer, four listcos); and the bid is
**structurally non-repeatable and not for sale to us** — an affiliate consolidating control is not a
rotation, has no float impact we can ride, and stops when the stake target is hit.

**한성기업**, the largest single contributor to eqflow (**RS20 +240.7%, RS60 +167.5%, 서지 8.17x** —
a 4× outlier that alone drags the equal-weight mean up), is a **retail patriotic-buying meme on a
delisting-risk stock**: "[특징주] 애국테마주? **'상폐 우려'** 한성기업" [yonhap 07-08]; "상폐 위기인데
주가는 급등" [hankyung 07-07]; "'애국 매수' 행렬에 20%대 강세" [chosun 07-14]; "5거래일 만에 주가 2배"
[chosun 07-10]. 69 hits/60d — the loudest name in the sector news window, and the reason is
**delisting risk, not defensive cash flow.** Including it in a defensive-rotation read is a category error.

### Why the won-scenario hypothesis is also dead — body-read, not tag-read
The sector's real dated event is **판가인상 (price pass-through)**, and its bodies state the FX sign
explicitly *against* the scenario:
- "CJ·사조, 식품가격 일제히 인상…선거 전후 도미노 인상 본격화" [yonhap **07-16**, body-read]:
  CJ제일제당 27개 품목 평균 **+8%** (햇반 +12%) from 07-30; 사조 참치캔 **+10%**, 수산캔 **+20%**,
  장류·유지 **+12%** from 08-03. Stated cause: "주요 원·부재료 가격과 **나프타 등 포장재 비용 상승**으로
  원가 부담이 지속." Government view in the same body: "**원·달러 환율 고공 행진**과 수입 원자재 가격
  상승… 하반기 식품·외식 물가의 추가 상승이 불가피."
- "사조·CJ도 가격 인상…**고환율**·중동 리스크에 '식품 인플레이션' 확산" [sedaily 07-18].
- "중동전쟁 장기화에 **원가 폭탄**, 가격 인상 '턱밑'" [mt 07-23(전월)]; "'물가 안정' 기조에 발 묶였던
  식품업계…결국 꺼낸 **가격 인상 카드**" [donga 07-19].

**Nobody in the tape is buying food on a strong won. The tape is food companies raising prices
*because* the won is weak (1487.28, 07-20) and naphtha/packaging is up.** The MACRO brief's
"환율 더 떨어지면… 1인당 GDP 4만 달러" item is a **conditional scenario, not a print** [MACRO §1
already flags this]; a bid built on it would be built on something that has not happened — and no
such bid is visible in the data anyway.

### The inversion that seals it
> **The leg with a real fundamental has negative flow; the leg with positive flow has no fundamental
> — it has a controlling shareholder.**

K푸드 export is genuinely working — "K푸드 상반기 수출 **70억달러** 돌파…중동 악재에도 역대 최대"
[mt 07-05]; "K라면 올수출 **20억弗** 예약" [mt 07-07] — and a weak won *helps* that leg. Yet its
purest listed expression, **삼양식품 (₩8.4조), is 🔴분산, RS60 −32.5%** (sweep) / **−27.9% live**.
Meanwhile the flow-positive names export nothing thematic and are being bought by their own parent.

**→ D-3 RESOLVED: artifact. STPL reverts to UW.** ROTATION's divergence rule (b) — "flow-led sector
the matrix under-rated → promote" — was correctly *applied*; its **input was contaminated**, because
`eqflow` on a 37-name sector whose movers are all sub-₩0.3조 cannot distinguish a rotation from a
group buyout. MACRO's original M-01 call (Neutral→UW, "no relief from a hiking central bank; no
fresh KR catalyst") **survives the challenge.** See §7 for the metric fix this run earns.

---

## §1 Flow — the full 37, read properly

Sector aggregate [`SECTOR_FLOW_KR.json`, **asof 07-16, 2 sessions stale**]:
`wflow +0.079 · eqflow +0.205 · green 6 · red 0 · breadth 0.16 · n 37 · sector mcap ₩46.34조`.

**A trap inside the sweep's own columns.** `rs20` is positive for **all 37 names** (min +1.3,
median **+21.6**, max +240.7) while `rs60` is negative for **35 of 37**. A 20-day relative
strength that is uniformly positive across an entire sector is **the benchmark falling, not the
sector being bid** — KOSPI 7,000 → 6,600 over the window [MACRO §1]. Staples fell *less*. That is
the defensive **beta** characteristic doing its job; it is **not** evidence of incremental demand,
and it is what makes a rate-regime defensive read superficially attractive. Live `module_flow`
(bench SPY, 07-20) puts the four large caps at RS20 **−0.6% / −4.1% / −4.5% / −4.5%** — the +20s
were entirely a KR-benchmark artifact.

Full per-name table: `SECTOR_FLOW_KR.json` key `names`, sector `음식료·담배`. Distribution —
6 🟢 (all ≤₩0.26조), 31 🟡, 0 🔴; **flow_score is negative for 18 of 37**, including 농심, 오뚜기,
대상, 하이트진로, 롯데칠성음료, 빙그레, SPC삼립, 풀무원, 삼양식품. A sector where half the names
have negative flow is not accumulating.

---

## §2 Players — large-cap universe ∪ thematic small-caps

**Floor as specified: ₩2.5조.** It leaves **4 names** — it does not empty the sector, so the floor
**stands unrelaxed**. Thematic small-caps admitted separately on the ≥2× news-mention rule.

### 2a. Large-cap universe (mcap ≥ ₩2.5조) — 4 names, **zero 🟢**
| Name | Ticker | mcap | flow (07-16) | Live 07-20 (`module_flow`, KIS 20d) |
|---|---|---|---|---|
| **KT&G** | 033780.KS | ₩18.10조 | +0.109 🟡 | 🟡중립 · 외 +9.6만 / 기 +5.2만 / 개 −14.9만 → **외국인·기관 순매수** · RS20 −0.6% · 서지 0.93x |
| **삼양식품** | 003230.KS | ₩8.40조 | −0.103 🟡 | **🔴분산** · 외 +0.2만 / 기 +7.3만 / 개 −7.8만 · RS60 **−27.9%** · 서지 0.69x |
| **오리온** | 271560.KS | ₩5.29조 | +0.385 🟡 | 🟡중립 · 외 **+23.5만** / 기 **−9.9만** / 개 −12.7만 · RS60 −11.8% |
| **CJ제일제당** | 097950.KS | ₩2.88조 | +0.036 🟡 | **🔴분산** · 외 **−8.5만** / 기 +5.2만 / 개 **+2.9만** → **⚠개인 흡수(외국인 이탈)** · RS60 −27.6% |

**KT&G is the only large-cap with a clean two-sided institutional bid** (외국인 AND 기관 both net
buyers, 개인 net seller — the real-hands shape) and the only one whose RS20 is roughly flat rather
than sharply negative. It is also the sector's only true rate-insensitive cash-flow asset (담배 =
inelastic demand, no 곡물 exposure, no FX cost lever). **If M-07 were operating anywhere in STPL,
it would be here — and KT&G's flow_score is +0.109, i.e. 🟡, not 🟢.** That single fact is the
quietest and most damaging evidence against a defensive rotation: the one name that *should* lead
it is not leading it.

**오리온's 외국인 +23.5만 / 기관 −9.9만 is a hand-off, not accumulation** — foreigners buying what
domestic institutions are selling. Not a confirmation.

### 2b. Thematic small-caps (named ≥2× in the sector news window, real ticker, **below the floor —
admitted as thematic, flagged as such**)
| Name | Ticker | mcap | News basis (≥2×) | Verdict |
|---|---|---|---|---|
| 한성기업 | 003680.KS | ₩0.06조 | **69 hits/60d** — 애국테마주 / 상폐 우려 (yonhap ×2, chosun ×2, donga, hankyung, 주간조선) | **EXCLUDE — meme, delisting risk** |
| 사조대림 | 003960.KS | ₩0.26조 | 판가인상 (yonhap 07-16, sedaily 07-18) + 1 unrelated | **EXCLUDE — parent-buy mechanism (§0)** |
| 사조산업 / 사조오양 / 사조씨푸드 | 007160 / 006090 / 014710 | ₩0.24 / 0.08 / 0.15조 | group-level 판가인상 coverage only; **1 direct hit each** | Fail ≥2× on own name; **EXCLUDE** |
| 샘표식품 | 248170.KS | ₩0.10조 | **1 hit/60d** (국립식량과학원 가루쌀·논콩 MOU, sedaily 07-10) | Fails ≥2×; **EXCLUDE** |
| 고려산업 | 002140.KS | ₩0.04조 | 0 hits | **EXCLUDE — 0 news + weak hands** |

**Result: the union is 4 large caps and nothing else.** Not one thematic small-cap survives both
gates. `module_industry_map` (seeds `음식료 가공식품 원재료 판가인상 K푸드`, separate argv) returned a
30-name corp pool / 6 clusters, but its top-30 is contaminated by section_text false positives
(유한양행, HLB글로벌, 영풍, 비비안, DH오토넥스 rank in the top 21) — **used for value-chain node
shape in §4 only, not for player selection.** Genuine additions it surfaced that are outside the
sweep's 37: 신세계푸드(031440), 더본코리아(475560), 동원산업(006040), GS리테일(007070) — noted as
chain nodes, none carries a flow signal here.

---

## §3 IR anchor — primary filings (DART, `--days 60`, pulled 07-20)

| Name | Total 공시 | 수주 | 자기주식 | 자본변동 | 지분변동 | Anchor read |
|---|---|---|---|---|---|---|
| **CJ제일제당** (097950) | **3** | 0 | **0** | 0 | 1 | **A near-empty 60 days.** Sole 지분변동 = **국민연금공단 약식 (06-23)**. No buyback, no capital action, no contract. For the company executing the sector's largest price increase, the filing record is silent — **the pass-through is a press event, not yet a disclosed financial one.** |
| **KT&G** (033780) | 10 | 0 | **0** | 0 | 5 | 지분변동 filers are **passive global managers — Capital Research (07-03), BlackRock Fund Advisors (06-10)**. Index/passive ownership churn, i.e. *not* discretionary defensive accumulation. **No 자기주식 filing in 60 days** — notable for a name whose equity story has historically rested on buyback+dividend. |
| **사조대림** (003960) | **14** | 0 | 0 | 0 | **6** | **6 of 14 are 지분변동, every one filed by 사조산업** (06-08 → 07-16). The busiest filing record in the sector is **entirely ownership, zero operations.** |
| **사조산업** (007160) | — | 0 | 0 | 0 | 2 | Filed on by **사조시스템즈 (07-02)** and **주진우 회장 (06-08)** — the top of the ladder. |
| **사조오양** (006090) | — | 0 | 0 | 0 | 4 | Filed on by **사조대림 (06-08, 07-15)** and **주지홍 (05-29, 06-08)**. |

**IR anchor conclusion (primary source):** across the entire sector, **zero 수주, zero 자기주식,
zero 자본변동 in 60 days.** There is no capital-return catalyst, no contract catalyst, and no
capital-structure catalyst anywhere in STPL. The *only* filing activity of substance is the 사조
family walking up its own group ladder. **A sector with no buyback, no contract, and no capital
action is not a sector institutions are being given a reason to rotate into.**

---

## §4 Value chain — 6 nodes, left → right

```
[1] 원재료 수입/곡물          [2] 가공·제조            [3] 브랜드/판가
    곡물·수산·유지·원당            대한제분 대한제당           CJ제일제당 오뚜기 농심
    수입 100% · USD 결제           삼양사 사조동아원           대상 롯데칠성 사조 KT&G
    ⚠ FX = 원가 (1487.28)          선진 팜스코 고려산업        ⚠⚠ BINDING CONSTRAINT
         │                              │                          │
         └──────────────┬───────────────┘                          │
                        ▼                                          ▼
[4] 유통 (대형마트/편의점)  ◄── 판가 승인 게이트 ──►   [5] 내수 소비자
    이마트 GS리테일 BGF                                    가격탄력 · 물가 정치
    "대형마트 등 주요 유통                                  6/3 지방선거 = the gate
     채널과 협의를 마쳤다"
                        │
                        ▼
[6] 수출 / K푸드  ── 삼양식품 오리온 CJ제일제당 · 상반기 70억달러 역대 최대
                   ⚡ weak won = TAILWIND here (opposite sign to node [1])
```

### The bottleneck — **가격전가력, and its gate is POLITICAL, not economic**
Strong K푸드 export demand is **not** a bottleneck (demand is abundant — 70억달러, 역대 최대).
The binding constraint is **whether a domestic price increase is permitted**, and the tape names
the gatekeeper explicitly:

> "선거 기간 정부의 간접적인 **물가 안정 압박**에 눈치를 보던 식음료 기업들이 **선거가 끝나자마자**
> 일제히 가격을 올리는 모양새" [yonhap 07-16, body]

and "'물가 안정' 기조에 **발 묶였던** 식품업계…결국 꺼낸 가격 인상 카드" [donga 07-19].

**This constraint RELEASED after the 6/3 지방선거** — that is a real, dated, verifiable change and
**the single most bullish fact in this file.** Node [1] cost pressure (won 1487.28 + naphtha +
중동) has been building all year; the ability to pass it on was politically frozen and is now thawed.
CJ +8%, 사조 +10~20%, 오뚜기 +6.1~17.0%, 롯데칠성 +5.3% are all dated instances.

**But it is margin *defense*, not margin *expansion*.** Node [1] and node [3] move in opposite
directions from the same weak won: FX raises the cost, and the price hike merely recovers it. The
bodies say "원가 부담이 지속된 데 따른 결정" — recovery, not gain. And the second bottleneck holds:

> "'가격결정 유연' 해외시장이 살린 K푸드…**내수는 '원가의 늪'**" [mt 07-02]

**The chain is split.** Export (node 6) has pricing freedom and a weak-won tailwind. Domestic
(nodes 3–5) has a politically-gated, cost-recovery-only pass-through. **A defensive rotation thesis
needs node 6 — and node 6's flow is the sector's worst (삼양식품 🔴, RS60 −27.9%).**

---

## §5 Candidates — **NONE QUALIFY**

Stated plainly, per the stage's own standard: it is a valid outcome to return nothing.

- **All 6 🟢 names are excluded** — 4 by the 사조 parent-buy mechanism (§0), 1 as a delisting-risk
  meme (한성기업), 1 by weak-hands invalidation (고려산업: 외국인 −44.3만 / 개인 +43.4만, live 🔴).
- **All 4 floor-clearing large caps are excluded** — none is 🟢; two are live 🔴; and the one with
  clean real-hands flow (**KT&G**) has no catalyst in 60 days of filings (no buyback, no capital
  action) and a flow_score of +0.109.
- **No chain-hop candidate is proposed.** The chain nodes with the real event (node 1 원재료 —
  대한제분 flow +0.333 but **OBV −0.34**; 대한제당 +0.678 🟡; 삼양사 +0.661 🟡) are all
  sub-₩0.5조 and none clears the floor. A news co-mention is not a candidate.

**WATCH-ONLY, promoted to no list, carried for the next run:**
**KT&G (033780.KS)** — the sector's only genuine rate-insensitive cash-flow asset and the only
name with a two-sided institutional bid. It is the correct *place* for M-07 to appear if M-07 is
real. It has not appeared yet. **If a defensive rotation is coming, KT&G goes 🟢 before the
micro-caps do — and it hasn't.** That ordering is the cleanest live test available.

**CJ제일제당 chart structure** [`module_chart 097950.KS --read`, 07-20, verbatim]:
```
OBV: 중립 (20d기울기 +11%)
다이버전스: 없음
MA정렬: 약세스택(5<20<60<120) · 가격 0/4 MA 위
볼린저: 수축(코일링) 13.2% · 중단
RSI: 56.0 · 모멘텀20d -4.4%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>187,260 + OBV→누적 / 스탑(스윙저점): 177,500
```
The stock executing the sector's flagship +8% price increase is in a **bearish MA stack, below all
four moving averages, NEUTRAL/CHOP**. The market is not paying for the pass-through.

---

## §6 Track-KPIs and anti-signals — all stated as OBSERVABLES

### Track-KPIs (what would make me wrong about the UW)
| # | Observable | Where measured | Threshold that reopens the case |
|---|---|---|---|
| K1 | **KT&G goes 🟢** in the flow sweep with 외국인 AND 기관 both net buyers | `SECTOR_FLOW_KR.json` + `module_flow 033780.KS` | flow_score ≥ +0.5 with the two-sided shape held. **The primary test of M-07 in STPL.** |
| K2 | **eqflow stays positive with the 사조 four removed** | recompute `eqflow` over the 33 non-사조 names | If eqflow ≥ +0.10 ex-사조, the breadth was real and §0 is wrong |
| K3 | **Price hikes actually take effect on schedule** | CJ 07-30 (대형마트) / 08-01 (편의점); 사조 08-03 | Rollback, deferral, or 정부 압박 headline = the political gate re-closed |
| K4 | **Sector 자기주식 or 수주 공시 appears** | `module_disclosure` — currently **0 across all names, 60d** | Any buyback from KT&G/CJ = the capital-return catalyst that is missing today |
| K5 | **삼양식품 flow turns** (the K푸드 export leg) | `module_flow 003230.KS` | 🔴분산 → 🟢 with 외국인 net buy = the node-6 leg activating, which *is* a real thesis |
| K6 | **원·달러 breaks below ~1450** | daily FX print (today **1487.28**, week 1493→1484.7→1480s→1487.28) | Would make the won-strength margin thesis a *print* rather than a scenario. **It is not one today.** |

### Anti-signals (what confirms the UW / kills any revival)
| # | Observable | Current reading (asof) |
|---|---|---|
| **A1 ★ BIGGEST** | **CJ제일제당 외국인 이탈 + 개인 흡수** — the sector's flagship pass-through name distributing to retail | **FIRED. 외국인 −8.5만 / 개인 +2.9만, 20d, 🔴분산, RS60 −27.6%, 약세스택 0/4 MA** (KIS, 07-20). The company that just raised 27 SKUs by 8% is being sold by foreigners and absorbed by retail. **If the price hike were a margin thesis, this is the exact tape that would not exist.** |
| A2 | 사조산업/사조대림 filings **stop** | 5 filings in 6 weeks through 07-16. When they stop, the four 사조 🟢 tags lose their engine — mechanically, not sentimentally |
| A3 | 한성기업 애국테마 unwind | RS20 +215.7%, 서지 8.17x on a **상폐 우려** name. A −50% round trip removes ~the entire eqflow excess by itself |
| A4 | 원·달러 holds ≥1480 | **1487.28 (07-20)**. Node-1 cost pressure persists; every won of weakness must be re-passed through the political gate again |
| A5 | 곡물/원자재 + 나프타 keep rising | "중동전쟁 장기화에 원가 폭탄" [mt]; "유럽 폭염에 우유·올리브 생산도 비상" [sedaily 07-06] — a *second* cost wave before the first pass-through has landed |
| A6 | 정부 물가 압박 headline returns | The gate that opened 6/3 can re-close. Watch 농식품부 (already running 할인 programs: "하나로마트·생협서 국산밀·콩 가공품 할인" [yonhap 07-12]) |
| A7 | RS60 negative for **35 of 37** names | Sector has underperformed for a quarter. RS20's uniform +21.6 median is benchmark collapse, not sector demand (§1) |
| A8 | Zero 자기주식 / 수주 / 자본변동, sector-wide, 60d | Structural absence of catalyst (§3) |

---

## §7 What this run owes the pipeline — a metric fix

**D-3 was not an analyst error; it was a metric error, and it will recur.** `eqflow` on a sector
whose movers are two orders of magnitude below its large caps cannot separate a rotation from a
single buyer with four listcos. Recommended for the next SWEEP/ROTATION revision (**not implemented
here — flagged for the human**):

1. Report **eqflow with a mcap floor** (e.g. ex-names < ₩0.5조) alongside raw eqflow. STPL's
   headline number would have been ~0 with that floor and no promotion would have occurred.
2. Flag **issuer-cluster concentration** — 4 of 6 greens sharing a corporate family should raise a
   `same_group` warning before breadth is claimed.
3. Cross-check any 🟢 whose `vol_surge > 4` against the news window for a **meme/이벤트 tag**
   (한성기업: 8.17x + 상폐 우려).

ROTATION's standing rule — *"when narrative and measured flow invert, the flow sets the tilt"* — is
sound and was applied honestly and symmetrically. **This run does not overturn the rule; it adds a
precondition: the flow must first be shown to be third-party and tradable.** Here it was neither.

---

## §8 One-line handoff to BET

**STPL → UW. No candidates. Do not carry the 음식료 eqflow +0.205 forward as a breadth signal** —
it is 1.50% of sector market cap, four of six greens are one family group buying its own ladder
(DART 06-08→07-16), one is a delisting-risk meme, and the sixth is weak-hands invalidated.
**KT&G is watch-only as the live test of M-07** — no sizing, no entry, no call.
