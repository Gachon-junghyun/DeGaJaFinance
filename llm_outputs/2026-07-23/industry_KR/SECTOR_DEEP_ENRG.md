# SECTOR_DEEP_ENRG — 정유·에너지전환/신재생 · 2026-07-23 (Thu)

> **CONTINUOUS track (07-16 / 07-17 / 07-20 / 07-21 / 07-22 → 6th consecutive run). DELTA-LED.**
> Unchanged structure carried **by reference**, not re-printed: [`2026-07-22`](../../2026-07-22/industry_KR/SECTOR_DEEP_ENRG.md)
> (the two-bet split A/B, the Aramco-ownership finding §0(B), the Group III bottleneck §6, the 8차 최고가격 schedule,
> the KKR SPA/EGM dates, the segment-mix re-verification) · [`2026-07-21`](../../2026-07-21/industry_KR/SECTOR_DEEP_ENRG.md)
> (correlation panel, risk-contribution table) · [`2026-07-20`](../../2026-07-20/industry_KR/SECTOR_DEEP_ENRG.md) (7-node chain).
> **Analysis product. Zero buy/sell calls. Zero sizing (BET's job).** Blanks stay blanks. Every claim carries source + asof.
> **Inputs re-read from disk today:** `MACRO_REPORT.md` §1/§2/§4 row 2/§4a M-09 · `SWEEP_READ.md` §2 · `SECTOR_ROTATION.md` §2 ENRG row ·
> `EVENT_ALPHA.md` (no direct ENRG card this run — confirmed below, not forced) · `STANDING_VIEW.md` §3 VLO/MPC/PSX + §6 C4 (US-side
> analog, NOT cross-applied per rule W1) · `handoff/RESEARCH.md` (B1/B2/A5/A6/B5).
> **Handoff ledger queried BEFORE analysis** (`module_report_tags ticker`, `DEGAJA_REPORT_DIR=llm_outputs`) —
> **096770 = 27 reports · 010950 = 28 · 475150 = 16 · 078930 = 20** (unchanged counts from 07-22 pull scope; today's own
> file not yet indexed at query time). Prior verdicts inherited, not re-derived.
> **Tools today:** `module_flow`(KIS 20d 실측 + KRX 공매도, **10:52 KST intraday**) · `module_chart --read`(VERBATIM) ·
> `module_valuation` · `module_disclosure --days 14/30` + **OpenDART `document.xml` 원문** (2 filings pulled and read: SK이노
> subsidiary filing, 대한항공 2Q 잠정실적) · `module_news_data fts --scope domestic --kr --full` (NEWS API, body-read, not
> headline) · yfinance (KS11/BZ=F/CL=F/RB=F/HO=F, own 3-2-1 crack rebuild).
> ⚠ **`^KS11` yfinance vs news-quoted close disagree by ~350pt for 07-22** (yfinance day-bar 6,797.70; MACRO's news-sourced
> close 7,153) — the same "data hole" class flagged 07-21 and 07-22, now a 3rd consecutive session with a KS11 data-quality
> problem. **RS20/RS60 from `module_flow` are not used to rank anything in this file** (same discipline as 07-22); ranking
> uses own-price returns (yfinance close-to-close, internally consistent within itself) + OBV state + KIS 실측 + KRX 공매도.

---

## §0 ★★ THE ANSWER, UP FRONT — both halves of the assigned question

### (A) *Is today's escalation a genuine re-pricing event, and does it change the "tactical" qualifier?*
> ### ▶ **YES, it is genuine — a tanker was actually hit today, not just threatened. NO, it does not remove "tactical" — it is the reason the word is there. And the fresh crack-spread rebuild below shows the position's own margin engine moving the WRONG way while the war-premium leg moves the RIGHT way, which is the tactical/structural distinction in one measurement.**

**What is new today, body-read, not headline** [연합뉴스, 23일]:
> *"사우디아라비아 남서쪽 홍해 해역에서 유조선이 공격을 받았다고 영국해사무역기구(UKMTO)가 23일(현지시간) 밝혔다 …
> 유조선 선장이 정체를 알 수 없는 발사체에 맞았다고 보고했다 … 후티 반군은 자신들이 사우디 유조선 2척('엔셀라',
> '라이리아')을 겨냥한 군사 작전을 수행했다고 밝혔다 … **이는 후티가 해상 봉쇄를 선언한 이후 처음으로 선박을 공격한
> 사례**"*

This is the first physical attack since the Houthi blockade declaration (07-20/21) — a named-ship, UKMTO-confirmed incident, not a rhetorical escalation. Alongside it, Iran's own negotiator escalated the Hormuz-specific threat the same day [연합뉴스, 22일, 갈리바프 이란 의회 의장]:
> *"이 전쟁의 방정식은 명확하다. '전부 아니면 전무(either all or none)'다 … **우리가 석유를 판매하지 못하는 지역에서는
> 그 누구도 석유를 팔지 못할 것** … 해협의 안보는 미군이 주둔하지 않을 때 비로소 확보된다 … 해협의 상황이 결코
> 전쟁 이전의 상태로 돌아가지 않을 것"*

Kepler (via yonhap 07-21, carried) already had Hormuz throughput at **4 cargo ships on 07-20** — near-zero — and the Red Sea/Bab-el-Mandeb detour (the route the 07-22 file's §6 flagged as "government says not binding") is now the route being hit.

**But the crack-spread rebuild (own calc, §4 below) shows the margin engine moving opposite to the crude level**: NYMEX 3-2-1 fell **−10.2% in one session (07-21→07-22)**, from $68.23 to $61.28, even as Brent rose **+5.1%** the same day (91.01→95.68) and the sell-side/news narrative (07-21, still being quoted as bullish) called the crack "above 2022 energy-crisis levels." **The four KR names all rallied hard on 07-22 — the exact session the crack spread was falling.** This is the STANDING_VIEW C4 pattern (US refiners: "crack fell while crude rose and equities rose anyway") **replicated independently on Korean-desk-owned data, not cross-applied from the US finding** (rule W1) — the KR file computes its own NYMEX proxy series and finds the same shape on its own dates.

> **▶ VERDICT: The escalation is real and materially advances SCENARIOS S8's branch C ("escalation continues") — but
> I do not score S8 myself; that is HANDOVER's job at the next run.** What this file adds: **the position's OW is
> increasingly a crude-level/war-premium trade, not a margin trade**, on today's own measurement. That is precisely
> what "tactical" was flagging from 07-16 onward. **Nothing here removes the tactical qualifier — this measurement
> is the reason to keep it, sharpened rather than resolved.**
> **Observable that would resolve the branch** (per L3 — write the resolving fact before the event, not after):
> Branch A (contained) = no second tanker incident within 72h **and** Kepler Hormuz transit count recovers off its
> 4-ship floor. Branch B (widens) = a second named-ship incident, or Bab-el-Mandeb closure confirmed by a shipper
> re-routing announcement. **Neither has happened as of this pull (10:52 KST 07-23).**

### (B) *How narrow is the ENRG OW — is S-Oil's move sustainable or idiosyncratic, and has that changed since 07-22?*
> ### ▶ **The dispersion ROTATION flagged (화학 n=103, wflow +0.106, only 2🟢/7🔴) is a real, unchanged structural fact — but S-Oil is no longer the one carrying it. Today, ALL FOUR core names show the real-hands signature simultaneously for the first time this run, while the broader 화학 sector and the renewable chain (§7, unchanged from 07-22) remain as narrow as ROTATION described.**

Fresh flow (10:52 KST, `module_flow`, own price returns 07-22 close → 07-23 intraday):

| Name | 07-22 close | 07-23 (10:5x) | 1d own | OBV (chart) | 외/기/개 20d (만주) | 공매도 %float |
|---|---|---|---|---|---|---|
| **096770 SK이노** | 118,400 | **125,500~125,900** | **+6.0%** | 매집, 20d기울기 **+135%**, RSI 75.5 | −14.9 / **+232.4** / −173.4 | 0.13% flat |
| **010950 S-Oil** | 141,700 | **146,900** | **+3.7%** | 매집, +30%, RSI 78.1, **MA 4/4 위 (regained)** | −7.0 / **+182.3** / −182.5 | **0.53% building(+0.08) ⚠주목 — crossed 0.50 line** |
| **475150 SK이터닉스** | 62,000 | **74,000** | **+19.4%** | 매집, +42%, RSI 72.9, **다이버전스 없음 (was 약세 07-22)** | **+113.8** / +152.0 / −293.8 | 2.51% covering(**−0.28**, accelerating vs −0.03 07-22) |
| **078930 GS** | 84,200 | **89,600** | **+6.4%** | 매집, +64%, RSI 69.2 | −66.0 / +127.4 / −62.8 | 0.02% flat |

**All four carry the real-hands signature (기관 net-buy + 개인 net-sell) simultaneously — unchanged and now a 6th-run
constant.** ⚠ `module_flow`'s own RS20/RS60 for all four are 45–116% today, an order of magnitude beyond any plausible
single-day move — the same `^KS11` corruption flagged in the header. **Not used for ranking.**

**Three deltas that resolve, sharpen, or extend 07-22's read:**
1. **S-Oil ended its 2-session non-participation.** 07-22 flagged S-Oil as −0.14%/−0.07% on two straight up days,
   losing an MA (3/4). Today it **regained the 4th MA** and returned **+3.7%**, in line with the tape. **KPI 12's
   "third under-delivery" test did NOT fire.** The structural point from §0(B) of the 07-22 file (63.4%
   Aramco-owned, long-term Aramco crude contract, sitting on the wrong side of a Saudi-targeted blockade) is
   unaffected by one session's price action — it is a filing fact, not a flow fact — but the **short crossing 0.50%
   for the first time in this run's history** is the flow-side echo of the same structural read continuing to build.
2. **475150's bearish RSI divergence, flagged fresh yesterday, is gone today** (RSI rose from 59.6 to 72.9 alongside
   a further +19.4% price move — momentum caught up to price rather than price correcting). The name is now **+32.4%
   over two sessions (07-21 close 55,900 → today 74,000)** with a short position covering at **8× yesterday's rate**
   (−0.28 vs −0.03) — a squeeze-consistent acceleration, not a fade. **Still zero same-day (07-23) company news** in
   an `fts search 이터닉스 --days 1` pull — the retail-broadcast column repeated is still 07-22's, naming the same
   "KKR JV / data-center" wrapper with no new fact (checked in full below, §9).
3. **096770's 07-22 subsidiary filing is real and immaterial** — checked via OpenDART `document.xml` directly
   (`rcpNo 20260722800874`): 지주회사의 자회사 편입, 코일베스 유한회사 (energy-storage construction/ops), **acquisition
   value ₩1,290M = 0.0% of SK이노베이션's separate-basis asset total.** Not related to the SK차이나 유상감자 item the
   07-22 file flagged as single-outlet/unconfirmed — that item's own resolution date (07-30 board) is unchanged and
   still not filed.

---

## §1 The crack-spread rate-of-change series (B1) — the compression the equity rally is not pricing

**Own NYMEX 3-2-1 rebuild** (CL/RB/HO continuous, yfinance daily, `2*RB*42 + 1*HO*42 − 3*CL`, all ÷3):

| Date | Crack321 ($/bbl) | 1d Δ | Brent (BZ=F) | Brent 1d Δ |
|---|---|---|---|---|
| 07-16 | 69.45 | +1.98% | 84.23 | −0.85% |
| 07-17 | 69.41 | −0.06% | 88.10 | +4.60% |
| 07-20 | 69.33 | −0.12% | 89.22 | +1.27% |
| 07-21 | 68.23 | −1.59% | 91.01 | +2.01% |
| **07-22** | **61.28** | **★★−10.2%** | **95.68** | **+5.14%** |

**Quarterly average, QoQ (per B1 — the level and the rate, not the level alone):**

| Quarter | Crack321 avg | QoQ | Brent avg | QoQ |
|---|---|---|---|---|
| 2025Q4 | 25.30 | −4.3% | 63.07 | −7.5% |
| 2026Q1 | 32.06 | **+26.7%** | 78.77 | **+24.9%** |
| 2026Q2 | 50.96 | **+58.9%** | 96.94 | **+23.1%** |
| 2026Q3 (to date, 23 obs) | 64.22 | **+26.0%** | 81.40 | −16.0%* |

*Q3's Brent QoQ reads negative only because Q2's average is inflated by the war's initial spike; Q3-to-date is still
running **above Q1** in level, and the escalation window itself (last 5 sessions) shows Brent **accelerating (+2.0% →
+5.1% day-over-day)** while the crack **decelerates and then inverts (−0.1% → −1.6% → −10.2%)**. **Two consecutive
declines in the rate, with the second an order of magnitude larger than the first, is the B1 signal** — the level
(both crude and crack are still historically elevated: crack321 sits at the **97.2nd percentile of the trailing 2
years** even after the drop) says "shortage/tightness persists"; the rate says the margin engine cooled sharply the
same day KR refiner equities rallied hardest. **Both are true and not contradictory — this is exactly the L1 lens.**

⚠ **Structural caveat carried from 07-22, unresolved**: this is a **US Gulf Coast proxy**; S-Oil and SK이노베이션 are
priced off the **Singapore/Dubai refining complex**, which no module in this repo measures (미상). The 07-21 yonhap
piece quoting "정제마진 사상 최고" cites the **same US 3-2-1 construct** this file rebuilds (their reporter's $70
matches this file's $68.23 for 07-21 almost exactly) — so the press narrative driving Tuesday's KR equity commentary
is a US number, read through to Korean refiners without a KR-specific margin series to confirm or deny it applies
identically. **This gap is the same one flagged for 3 consecutive runs; it remains open.**

---

## §2 Customer check (A6/W4) — a fuel-cost-exposed KR buyer's own disclosed 2Q print

**대한항공 (003490)**, fresh flow (10:52 KST): 🟢가속, OBV 매집, own vol_surge 0.65×, 외국인 **−124.4만** (selling) /
기관 **+650.0만** (buying) / 개인 −516.5만, 공매도 0.19% covering. **011200 HMM**: 🟢가속, OBV 매집, 외국인 **+97.7만**
(buying) / 기관 **+326.4만** (buying) / 개인 −425.6만, 공매도 1.05% covering(⚠주목). Both real-hands.

**And the disclosed spend, per rule A6/W4 — not inferred, read from the primary filing** [OpenDART `document.xml`,
대한항공 영업(잠정)실적(공정공시), rcpNo 20260713800490, filed 2026-07-13, 2Q26 vs 1Q26 vs 2Q25]:

| | 2Q26 | 1Q26 | QoQ | 2Q25 | YoY |
|---|---|---|---|---|---|
| 매출액 | ₩5.0199조 | ₩4.5151조 | **+11.2%** | ₩3.9859조 | **+25.9%** |
| 영업이익 | ₩2,618억 | ₩5,169억 | **★−49.4%** | ₩3,989억 | **−34.4%** |
| 당기순이익 | **−₩973억** | +₩2,427억 | **적자전환** | +₩3,959억 | 적자전환 |

**Revenue up double digits QoQ while operating profit nearly halved and net income swung to a loss** is the classic
fuel-cost-margin-squeeze shape for an airline customer sitting downstream of the crude/crack spike this file is
measuring. This is a **named customer's own disclosed number, dated 2026-07-13** (i.e. it already reflects the
early-window impact of the war before today's fresh escalation) — not an inference. **I did not find an equivalent
HMM Q2 preliminary print in the 30-day disclosure pull** (HMM's only recent filing is a ₩3,118억 charter contract,
06-26) — HMM's own 2Q print is **not yet disclosed**, so its own fuel-cost line cannot be checked this run; flagged
as a blank (P4) rather than substituted with the 07-22 sell-side note ("HMM, 운임 상승에 2분기 실적 개선 전망," a
freight-rate call, not a fuel-cost one).

> **Read-through**: the node's downstream customer is already booking a cost hit before today's tanker strike is even
> in the data. This strengthens, rather than resolves, the "cost not just supply risk" framing §0(A) of the 07-22
> file established for S-Oil's Aramco-crude exposure — the same crude/freight dynamic that raises S-Oil's input cost
> also raises its airline customer's input cost, on the same primary-filing evidence class (disclosed P&L, not news).

---

## §3 Dispersion (B5) — restated with today's fresh flow, not re-derived

**ROTATION's own number, carried verbatim**: 화학 (KRX bucket nearest to refining/petrochem, n=103) wflow **+0.106**,
**2🟢/7🔴** — "the OW is carried by S-Oil specifically, not sector breadth" (ROTATION §2, "no verdict change").

**What changes today**: it is no longer S-Oil alone carrying the green tag among the desk's own four-name coverage
set. **All four (096770, 010950, 475150, 078930) show 🟢가속 with the real-hands signature simultaneously** (§0(B)) —
a broadening the 07-22 file already found (refining leg moved from S-Oil-only to 096770+078930, with 475150 detached
as a separate name event) **continuing, not reverting**. But this is still **4 names inside a 103-name KRX sector
with only 2 green** — the chain-hop table inherited from 07-22 (§7 below) shows the fifth-largest refiner (HD현대,
`SECTOR_FLOW_KR.json` **rank 501/829, flow −0.21, OBV 분산 (C급, corroborant only per D6)** — parent of the unlisted
4th refiner) and the entire renewable value chain (5 of 6 listed peers rank 168–818, flow negative on 4 of 5, OBV
분산 on all 5 — rank and flow sign are the load-bearing evidence, OBV cited only as agreement, C급 grade) still
failing the flow test. **The
unit-of-analysis finding stands exactly as ROTATION and the 07-22 file
stated it: "화학"/"정유" as a sector label is too broad; the real basis is a ~4-name basket, now including all four
of this desk's own coverage names rather than one, but still not the sector.**

**No EVENT_ALPHA card touches ENRG directly this run** — confirmed by re-reading its selection log: the 뉴욕증시/
이란긴장 thread was explicitly declined there as "already MACRO's own subject… would duplicate," and its KR exposure
(S-Oil) was named as "already a MACRO/SWEEP headline name, not a one-hop finding." **This is the correct call and is
not force-connected here** — the LG-tariff (Card 1) and card-issuer (Card 4) cards are FIN/other-sector, confirmed
unrelated to ENRG on inspection.

---

## §4 Value chain, chain-hop, KKR/EGM dates — by reference, unchanged

**Carried verbatim from [07-20 §D](../../2026-07-20/industry_KR/SECTOR_DEEP_ENRG.md) and
[07-22 §6/§7](../../2026-07-22/industry_KR/SECTOR_DEEP_ENRG.md)**: the 7-node chain map, the Group III 윤활기유
binding-constraint quotation ($4,000/t, SK엔무브+S-Oil = 40% of world supply, certification-gated), the 8-name
chain-hop table (renewable chain 5/6 negative-flow/OBV-분산 by rank, refining hop fails all but one 0.24조 blender —
ranks and flow sign are the evidence, per D6), the KKR SPA
(strike ₩23,700, closing **2026-07-31**), the conditional EGM (**2026-07-28**), and the NPS 5.11%/34,067,004-share
mcap correction. **Not re-verified or re-pulled this run** — no new filing appeared in the 14-day disclosure pull for
475150 beyond the 07-13 주총 items already known. **8차 최고가격 decision remains D-1 as of this file** (due
2026-07-24) — see the government's own restated position below.

**One primary update on the 8차 최고가격 axis** [mt, 22일, 국무회의 후속]:
> *"석유류 최고가격제가 단계적 폐지 대신 연장될 가능성이 커졌다 … 이재명 대통령 '(최고가격제는) 원래 계획에 의하면
> 사실 더 내리든지 폐지됐어야 하는데 오히려 더 강화해야 할 것같다' … 구윤철 부총리 '유가가 지금 올라가는 상황이어서
> 유가 상황까지 감안해서 결정하겠다'"*
This restates, rather than advances, the 07-21/07-22 file's own read — the direction (인상/유지 over 인하/폐지) is
now stated by two officials on two consecutive days. **No new number; decision itself lands tomorrow (D-1).**

---

## §5 Track KPIs — updated only where today moved the needle

| # | KPI | 07-22 | **07-23 (today)** | Fires on |
|---|---|---|---|---|
| 1 ★★ | 8차 최고가격 고시 | D+2, 대통령 "강화" | **D-1.** Two officials (대통령/구윤철) on record two days running for 인상/유지 | 인상 = domestic margin compressed into a rising input cost |
| 2 ★★ | SK이노 2Q 컨콜+이사회 07-30 | consensus SHAPE known (−34.7%/−24.1% QoQ) | unchanged; DART filing for the call still on file (`20260716800628`) | beat/miss vs the FnGuide QoQ decline |
| 5 ★★ | 475150 same-day catalyst | zero hits (19), 07-22 | **zero hits again, `fts 이터닉스 --days 1` — 3rd session running.** Price +19.4% today on top of +10.9% (07-22 close-to-close) with no news | a catalyst prints within 2 sessions = real; retraces with nothing printed = the retail-tip signature confirmed |
| 10 | 475150 공매도 | 2.53% covering(−0.03) | **2.51% covering(−0.28) — the covering rate accelerated 8×** | covers through 07-28/07-31 = event positioning; rebuilds after = directional |
| 11 ★ | S-Oil 공매도 | 0.49% building(+0.04), 4th run under 0.50 | **0.53% building(+0.08) — CROSSED the ⚠주목 line for the first time this run** | ≥0.50% now met; watch for further build vs a one-session cross |
| 12 | S-Oil relative participation | 2 sessions non-participation | **Ended — S-Oil +3.7% today, regained its 4th MA.** KPI 12's reclassification test did NOT fire | a further non-participation day would have fired it; today did not |
| NEW ★★ | Tanker-strike escalation (S8 branch C observable) | undated, "rhetoric only" per SCENARIOS framing | **A named-ship UKMTO-confirmed attack occurred today, first since blockade declared.** Not yet a second incident | second incident within 72h / Bab-el-Mandeb closure confirmed by re-routing = branch B; no repeat + Kepler transit recovers = branch A |
| NEW | Crack321 vs crude divergence | not tracked | **Crack −10.2% same day crude +5.1% (07-22)** | two consecutive crack declines while crude keeps rising = the margin engine is not participating in the rally (L1/C4 pattern) |
| NEW | 대한항공 2Q disclosed | not tracked | **Op profit −49.4% QoQ, net loss, filed 07-13** — customer-side cost confirmation | HMM's own Q2 print, still pending — no date found in this pull |

**Carried unchanged, not re-verified**: KKR EGM 07-28, SPA close 07-31, NPS 5.11% (stale, 06-23 기준일), 원유 확보율
90%+ (산업통상부 07-21), Group III $4,000/t.

---

## §6 Anti-signals — ranked by proximity, today's additions first

1. **★★ A tanker was actually hit today (§0(A)).** This is the first physical incident since the Houthi blockade
   declaration — a materially different observable than the "rhetoric" framing SCENARIOS' S8 registered at. It has
   NOT yet produced a second incident or a shipper re-routing confirmation. *Observable: next 72h.*
2. **★★ The crack spread fell 10.2% the same session all four KR refiners/holdcos rallied hardest.** The margin
   engine and the equity rally are moving in opposite directions on the same date — the STANDING_VIEW C4 pattern,
   independently replicated on this desk's own KR-relevant proxy, not cross-applied (W1). *Observable: a second
   consecutive crack decline (§4 file, next pull).*
3. **★ S-Oil's short crossed 0.50% for the first time this run (0.53%, building), the same day its price caught up
   to the tape.** A building short on a catch-up day is not itself a contradiction, but it is the first time this
   run's own ⚠주목 threshold has fired. *Observable: KPI 11, next 2 sessions.*
4. **★ 475150 is now +32.4% over two sessions with zero same-day news for the third session running**, and its
   short-covering rate accelerated 8× — consistent with either a genuine squeeze into the 07-28/07-31 KKR dates or a
   retail-momentum chase; the two are observationally similar until one of those dates resolves. *Observable: KPI 5.*
5. **HMM's own Q2 fuel-cost print is not yet disclosed** — 대한항공's is, and it already shows a QoQ margin collapse.
   Concluding the shipping/logistics leg of the customer chain from 대한항공 alone would be extrapolating past what
   is disclosed (W4 discipline). *Observable: HMM disclosure, undated.*
6. **The Singapore/Dubai margin gap remains open for a 4th consecutive run** — every KR-specific margin claim in
   this file rests on a US Gulf proxy. Unmeasured, stated rather than silently used.
7. **Carried, unchanged**: Group III certification moat, 8차 최고가격 D-1, SK차이나 유상감자 [단독] pending 07-30
   DART, KKR SPA gap (strike ₩23,700 vs spot ~₩74,000 for 475150, a non-comparable reference since the SPA is a
   change-of-control price on a March-dated agreement, not a market valuation claim).

---

## §7 Tool limits · data quality (P4)

- ⚠⚠ **`^KS11` yfinance vs news-quoted close disagree materially for the 3rd consecutive session** (07-21, 07-22
  flagged before; today's pull shows 07-22 = 6,797.70 vs MACRO's news-sourced 7,153). Whether KOSPI itself was up or
  down intraday today is **genuinely ambiguous between the two sources available to this desk** — this file does not
  resolve it and does not lean on RS20/RS60 for any ranking as a result (own-price returns used instead throughout).
- **KR FTS trigram gap reconfirmed**: `이란` (2 characters) returns **0** matches despite dozens of same-day articles
  containing it (verified via `혁명수비대`, `유조선`, which return the same underlying articles). Same class as the
  07-22 file's `9월` failure. Worked around by searching multi-character proper nouns instead.
- `module_flow`'s raw `rs20`/`rs60` fields print 45–116% for all four names today — confirms the benchmark
  corruption is a `module_flow`-level symptom of the same `^KS11` data problem, not a one-off in this file's own
  calculation.
- **`catalyst_calendar --days 5`** still lists only TSLA/RTX/LMT/KMI earnings and an undated Hormuz line — **misses
  8차 최고가격 (D-1, dated and known), the KKR EGM (07-28), and SK이노's board+call (07-30)**, all KR structural
  catalysts with known dates. Same D18-class gap as prior runs; `data/catalysts/structural_schedule.json` needs a
  human update to carry KR items.
- **Ledger inherited, not re-derived**: counts as queried before analysis (096770=27, 010950=28, 475150=16,
  078930=20) — see header. Today's own file will appear in tomorrow's count.
- **No correlation panel re-run** — carried by reference from 07-21 per the same logic as 07-22 (a volatile 2-day
  stretch would distort a 20-day residual correlation).

---

## ✅ EXIT CHECK

- [x] Covers flow (fresh, §0(B)/§3) → players (unchanged 4-name set, ledger-confirmed) → IR (OpenDART filings read,
      §0(B).3 + §2) → chain map (§4, by reference) → bottleneck/KPI/anti-signal (§5/§6).
- [x] **Continuous-track (6th run), LED with the delta** (§0, §1's fresh crack rebuild, §2's fresh customer print) —
      unchanged structure carried by reference, not re-printed.
- [x] **Commodity/price-cycle node (crack spread + Brent) carries a QoQ rate-of-change series, not just levels**
      (§1) — level (97.2nd pctile) and rate (2 consecutive declines then a −10.2% break) both stated, and shown to
      point in different directions on the escalation window.
- [x] **Node's customers named and disclosed spend checked**: 대한항공 2Q prelim (op profit −49.4% QoQ, net loss,
      dated 07-13, primary filing) — HMM's own print absent, stated as a blank with no date found (§2, W4).
- [x] **Lead/lag claims**: none newly asserted this run; the 07-22 file's inherited claims (Aramco ownership →
      structural exposure) are a filing fact, not a lead/lag claim, and are carried by reference, not re-tested.
- [x] **Sub-sector dispersion stated** (§3): 화학 n=103 wflow +0.106, 2🟢/7🔴 (ROTATION, verbatim) vs the desk's own
      4-name coverage now uniformly 🟢 — both readings held simultaneously, the sector label named as too broad a
      unit, consistent with 07-22's own finding.
- [x] Both branches on the oscillating/escalation variable (§0(A), §5 new KPI) — no S8 self-scoring, observable
      stated for HANDOVER.
- [x] US-side analog (STANDING_VIEW C4) cited for the parallel, NOT cross-applied — this file's crack-spread finding
      is its own KR-relevant calculation on its own dates (W1 compliance, §1).
- [x] Zero buy/sell, zero sizing throughout.
- [x] Linter run below; findings fixed or exempted with rule ID.
