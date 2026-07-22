# RESEARCH — the single source for desk research rules

> **This file is the only place research rules live.** Loaded by L1·HANDOVER at the start of every
> run, so the rules reach the point of execution instead of sitting in an archive.
>
> **Rules are written as triggers, not as advice.** "Subtract the baseline" is true and does not
> fire while you are working. "The moment you write *excess return*, is the benchmark in the same
> sentence?" fires. Every rule below names **when it activates**, **what to check**, and the
> **measured failure** that paid for it.
>
> **Where the evidence lives**: `lab/` is now the *evidence archive* — 28 experiments' worth of
> derivations, kept for "why does this rule exist", not for lookup during a run.
> [`lab/PLAYGROUND_SYNTHESIS.md`](../lab/PLAYGROUND_SYNTHESIS.md) (PLAY6–16) ·
> [`lab/ECONOPHYSICS_THEORY.md`](../lab/ECONOPHYSICS_THEORY.md) (PLAY17–28) ·
> [`lab/INFLECTION_NEWS_KR.md`](../lab/INFLECTION_NEWS_KR.md) (inflection×news) ·
> `lab/실험보고서_전체기록.docx` (PLAY1–16, lay narrative + glossary — **human-facing, never read by a desk run**).
>
> Market views live in [STANDING_VIEW.md](STANDING_VIEW.md). Not advice.

**asof 2026-07-22** · 21 triggers + 3 lenses, consolidated from 4 previously-scattered locations

---

## Why this file exists in trigger form

Measured 2026-07-22: six judgments were reversed inside one session. **Three of them broke rules
that already existed in `lab/`** — the baseline rule, the regime-contamination rule, and
"test your test before you use it". The rules were not missing. They were written as prose, filed in
a folder that `pipeline/` referenced **zero** times, and never reached the run.

Two consequences, both encoded here:
1. Rules are **triggers** — each names the moment it fires.
2. Rules are **loaded by a stage** (HANDOVER), not stored where someone might look them up.

---

# Part A · Triggers

## Group 1 — the moment you cite a number

### C1 · Baseline and benchmark
**Fires when** you write *excess*, *relative*, *outperformed*, *RS20/RS60*, or any conditional return.
**Check** (a) the benchmark is named **in the same sentence**; (b) you measured the window yourself —
including any baseline you were handed.
**Measured failure** — the same 20 days: 005930 is **−12.1% vs SPY** and **+10.1% vs `^KS11`**,
because the KOSPI fell ~26% in a month. Sign flips with the benchmark. Separately, a baseline passed
down in a brief was wrong and two experiments had to correct it: the "−1.72% over 5 days" window was
the news window only; the full year was **+0.95%**.
**Source** PLAYGROUND §7-1 · ECONOPHYSICS §V-3 · retracted R4

### C2 · Both halves of a print
**Fires when** you cite a headline economic release (exports, CPI, shipments, orders).
**Check** you quoted **both** the YoY and the sequential figure, on a **like-for-like window**
(1–20th vs 1–20th, never a partial window against a full month).
**Measured failure** — KR semiconductor exports **+180.6% YoY** cited as a bullish catalyst on the
same day the like-for-like window printed **−11.3% MoM**. Half a print is not evidence.
**Source** retracted R2 (no lab precedent — this is a new failure class)

### C3 · Keep an "unknown" column
**Fires when** you bucket anything into present/absent, hit/miss, news/quiet.
**Check** there is a **third bucket for unknown**. NaN merged into "absent" manufactures a difference.
**Measured failure** — news-z needs a 30-day baseline, so early-May events were all NaN; folding them
into "quiet" contaminated the quiet sample and produced a difference that did not exist (it happened
on the first run).
**Source** PLAYGROUND §7-3 · INFLECTION §2-⑤

### C4 · Say "indistinguishable", not "rejected"
**Fires when** a test comes back not significant.
**Check** the write-up says **indistinguishable / no power**, not "no effect". A blank beats a
falsehood (P4).
**Measured failure** — 27 results logged as "rejected" in PLAY6–10 were re-classified as
"undetectable with this data" once power was computed. Nothing had actually been falsified.
**Source** ECONOPHYSICS §V-7 · PLAYGROUND §4

### C5 · Expose the arbitrary choice
**Fires when** you pick a weighting, a smoothing, a group count, a scoring panel, or a prior.
**Check** the choice is stated **and** its alternative's effect is known.
**Measured failure** — choices that flipped conclusions: market weighting (R² **0.237 ↔ 0.315**),
filtering vs smoothing (**19.8%** of days disagreed), group-count matching, which residual panel
scores, and the prior (most-likely cause reversed on **41.4%**).
**Source** PLAYGROUND §7-7

---

## Group 2 — the moment you make a statistical claim

### S1 · Fold by date before trusting a t
**Fires when** you cite n ≥ ~20 pooled observations, or any panel t-statistic.
**Check** count the **distinct dates**. If n / distinct-dates > ~3, the effective sample is the date
count. (Long-short portfolios are already cross-sectional aggregates — harmless, SE inflation 0.92–1.11.)
**Measured failure** — the same data went from **t = +6.55 to t = −0.74** when folded by date:
233 shock events, 65 of them on one day (2026-06-08). Also 2026-07-21: 18/18 US semis green,
median +5.0% — that is **n≈1**, not n=18.
**Source** PLAYGROUND §7-2 · ECONOPHYSICS §V-2 · INFLECTION §2-③ · retracted (lens B3 merged here)

### S2 · Diagnose the null before you use it
**Fires when** you run a permutation / shuffle / bootstrap test.
**Check** measure `n_eff` and the **achievable minimum p** first. If the null cannot reach your
target p, do not report a conclusion. Run **circular-shift and cross-sectional-shuffle side by side** —
they ask different questions ("is the time alignment informative?" vs "is *which name you picked*
informative?") — and always state what was held fixed and what was randomized.
**Measured failure** — daily circular shift had adjacent-correlation **0.9996**, `n_eff` **12.3**,
and **missed** a known-good 12-1 momentum control (p = 0.088) that cross-sectional shuffle caught at
**p = 0.0005**. The broken null was usable in **0 of 36** held statistics.
**Source** PLAYGROUND §4 · §7-4 (`nulldiag.py` is reusable)

### S3 · Compute power before running
**Fires when** you design any test on a fixed window.
**Check** the minimum detectable effect for that window. If it exceeds plausible effect sizes, you
already know the answer is "no power" — do not spend the run.
**Measured failure** — 244 trading days has a minimum detectable effect of **annual Sharpe 2.85**;
real factors run 0.3–1.0. Momentum needs **3,934 trading days (15.6 years)** for 80% power. The 244-day
point estimate (+19.90%/yr) was almost identical to the 15-year one (+20.05%/yr) — but with
CI **[−48.7, +113.8]**.
**Source** PLAYGROUND §5 · §7-5

### S4 · In-sample significance is the start of falsification
**Fires when** an in-sample result looks significant.
**Check** all four gates: ① generalization to other names/sectors ② ex-ante calibration
③ transaction costs ④ honest multiple-testing aggregation.
**Measured failure** — DGS10 (t −2.0) and the foreign-flow IC (t 2.27) both died or halved at the
generalization/OOS gate. DGS10 lost to buy-and-hold after costs (**t −2.21**).
**Source** ECONOPHYSICS §V-1 · PLAY26

### S5 · Short samples invent structure
**Fires when** your window is under ~1 year and you report a grouping, cluster, or regime.
**Check** stability separately from fit — they move in opposite directions on short windows.
**Measured failure** — cutting to 244 days dropped membership stability (ARI) to **0.093** while
**within-group correlation went up**. The structure looked better and was less real.
**Source** PLAYGROUND §7-9

### S6 · Tag any label that uses the future
**Fires when** you use pivot, regime, smoothed-state, or any variable defined with hindsight.
**Check** it is marked `[label]` and never used as a signal.
**Measured failure** — the pivot classifier uses **10 forward days**; its rows show +18~20% moves
that are pure circularity. Warnings are hardcoded into the code and output for this reason.
**Source** PLAYGROUND §7-6 · INFLECTION §2-③ note

---

## Group 3 — the moment you read data (contamination checks)

### D1 · Check for a second listing venue before reading domestic flow
**Fires when** you cite foreign/institutional net-buying as directional.
**Check** does the name have an ADR/GDR/dual listing, and is conversion between venues **blocked**?
If yes, mark the flow read **SUSPENDED with the date it clears** and record it in STANDING_VIEW.
**Do not retroactively clean** the contaminated stretch once conversion opens.
**Measured failure** — SK hynix listed ADRs 2026-07-10 ($26.5B); the ADR ran **+50%** over the home
line (~25% later) because two-way conversion was closed. Seoul "foreign selling" was substantially
venue migration; US money bought Seoul shares via EWY instead (**$1.1B in one day**). The sibling
with no ADR (005930) carried the clean read — the intuitive ranking **inverted**.
**Source** retracted R1 (no lab precedent — new failure class)

### D2 · Verify the proxy's sign
**Fires when** you substitute a proxy for an unavailable series.
**Check** the proxy's sign against a known case before using it directionally.
**Measured failure** — FINRA imbalance **inverts sign** through market-maker hedging; it is unusable
for direction. Conversely, KRX official investor data matched the Naver proxy at **corr 1.0000** —
so proxies are not all bad, they are all **unverified until checked**.
**Source** ECONOPHYSICS §V-5 · PLAY17 · PLAY21

### D3 · Signed and unsigned variables are different physics
**Fires when** you model impact, flow, or pressure.
**Check** whether your variable carries a sign. Do not carry a result from one to the other.
**Measured failure** — unsigned volume is **linear** (exponent 1.0–1.6); signed net flow is
**concave** (δ = 0.33–0.38). Concavity is a property of *signed* flow only.
**Source** ECONOPHYSICS §V-4 · Law 1

### D4 · Check regime contamination in the window
**Fires when** you fix a sample window.
**Check** for short-selling bans, single-direction markets, coverage gaps in the field you rely on.
**Measured failure** — `published_at` exists only from 2026-05-01, capping the news axis at
**53 trading days**, all of it one falling regime (zero rising-market sample). Recovery added rows
but **biased** them: recovered days averaged 335 articles from 30 sources vs 2,378 from 71.
**Source** ECONOPHYSICS §V-6 · INFLECTION §5 · PLAYGROUND §5

### D6 · Weight a signal by its measured grade, not by how visible the tool makes it
**Fires when** you cite any flow/technical indicator as evidence — especially **OBV**, an OBV-derived
🟢/🟡/🔴 tag, or "accumulating / distributing".
**Check** the signal's grade below. **A C-grade signal may corroborate; it may never carry a
proposition alone**, and it may never override an A- or B-grade signal that disagrees.

| Grade | Signal | Measurement |
|---|---|---|
| **A** — powered and gate-passed | **mom5 Q1 / 12-1 momentum** (losers keep losing) | LR **0.880** [0.801, 0.966], shuffle **p = 0.001**, 199 trading days, **39,290 obs** — *the only cell that had power*. Cross-confirmed: KR large-cap short-reversal factor sign **inverts** (−9.0%/yr) |
| **A** | **Residual clusters beat sector labels** | out-of-sample within-group corr **0.1289 vs 0.0786**, paired diff **+0.0511 [0.0435, 0.0588] ≈ 13 SE**; membership ARI 0.568 vs null 0.0165 |
| **A** | **Concave impact of signed flow** | δ = **0.33–0.38** (KR), 0.08–0.20 (US signed). Linear and √ both rejected; reproduced in both markets |
| **A** | **Impact is transient** | 5 of 6 names ΣG/G(0) < 1; large caps **partially revert within 5 days** (G(5)<0) |
| **A** | **Fat tails** | Hill α ≈ 3.4–4.4 (KR) / 2.9–3.9 (US) — normal rejected. Sizing/stops must not assume normality |
| **B** — passed but conditional | **Foreign net buying** (KR, KIS actuals) | The **only** surviving leading axis: 20d excess NW-t **3.73**; Q5−Q1 **+1.417pp**, shuffle **p = 0.0005**. ⚠ **Non-stationary** — first 18 months IC ≈ **+0.015 ≈ 0**. Use as confirmation on top of another reason; **never as a standalone system** |
| **B** | **Short balance as liquidity supply** | Net-buy→return slope falls monotonically across short-ratio terciles **0.112 → 0.084 → 0.066**, all p < 0.001. Heavy-short days are *easier* to execute into |
| **C** — demoted | **OBV / 매집·분산 / OBV-derived flow tags** | **Half a shadow of real flow**: r ≈ 0.49 vs foreign net buying (per name **0.005–0.67**), and **no leading power (t = 1.00)** once foreign flow is known. Corroborant only |
| **REJECTED** — do not re-buy | COT crowded-long contrarian · VIX/fear contrarian · DGS10 early warning · pre-disclosure smart-money accumulation · foreign-buy × short-cover squeeze combo · **"short interest building = bearish"** | All indistinguishable or reversed. The last one matters here: rising short balance was **indistinguishable** from noise (16-month post-resumption power limit) — and Law 3 says shorts *supply* liquidity |

**Measured failure** — 2026-07-21 the US desk built its semiconductor de-rate KPI on OBV
(*"two of {MU,TSM,AVGO} flip OBV to accumulation"*). Scored the next day after a +12~14% memory
rally: still **0 of 3**, SMH RS20 still −13.2%. The KPI happened to hold, but it rested on a C-grade
signal — the same read was available from A-grade momentum and B-grade foreign flow, which is where
it belonged.
**Practical substitution** — when tempted to write "OBV accumulating", ask instead:
(1) what does **RS20/RS60 momentum** say (A)? (2) for KR, what do **KIS foreign/institution actuals**
say (B)? (3) is the move **date-clustered** (S1)? OBV enters only as agreement or disagreement with
those, and is reported as such.
**Source** PLAY19 · PLAY25 · PLAY28 · PLAYGROUND §1 · ECONOPHYSICS §I·§III

**부록 — 측정된 IC 눈금** (자기 IC 를 부풀리지 않기 위한 참조. `scripts/kelly_size.py --ic` 근거)

| 신호 | IC | 상태 |
|---|---|---|
| 외국인 순매수 (좋았던 부분표본, 전력기기 2종목) | **0.33 ~ 0.44** | 측정됨 · **비정상** |
| 외국인 순매수 (앞 18개월) | **≈ 0.015** | 측정됨 — 사실상 0 |
| **추정치 리비전 (US)** | 창별 **+0.36 / +0.28** → 접은 값 **+0.32** | ⚠ **구분 불가** — Q5 의 72% 가 IT 한 섹터. 유효 창 2개(자유도 1). 부호는 두 창에서 일치 |

⚠ 세 줄 모두 **"쓸 수 있는 IC"가 아니다.** 위 둘은 비정상(non-stationary), 아래는 단일 테마 집중.
`--ic` 에 넣을 때 `--ic-n` 에 **종목 수를 넣지 마라** — 유효 표본은 날짜 수다(규칙 S1).

### D5 · Cross-check providers before theorizing about a late series
**Fires when** data looks missing or stale.
**Check** a second and third independent source before concluding the provider is lagging.
**Measured failure** — KIS, Naver, and KRX returned **identical** investor figures through the same
date and all three stopped there, proving the day was unpublished rather than one feed lagging.
One source cannot distinguish those two cases.
**Source** this session (lens B6 merged here)

---

## Group 4 — the moment you write a conclusion

### W1 · A signal's market of measurement is part of the signal
**Fires when** you cite a statistical result measured in a different market.
**Check** was it replicated **here**? Does the source document record a replication failure?
**Measured failure** — a KR-measured fear-gauge result (t −3.5) applied to VIX/US, while the source
document states the **US mirror failed to replicate**. The repo already enforces this for the news
feed (`--scope domestic|foreign`); it applies identically to statistical results.
**Source** retracted R3 · ECONOPHYSICS §IV-3

### W2 · An inherited lead/lag claim is tested or tagged
**Fires when** you write *leads*, *precedes*, *early indicator*, *n months ahead* — especially if you
got it from a prior report.
**Check** is there a lag-correlation table? If not, tag `[unverified]` and do not cite it as evidence.
**Measured failure** — "EDA leads semis by 12–18 months" was carried between reports uncited and
repeated as the one genuine leading indicator. 199 monthly observations (2010–2026):
same-month **+0.63**, lag-12 **+0.05**, lag-18 **−0.05** (SPY-excess +0.24 / +0.02 / −0.06).
**Coincident, not leading.** Second lesson: the weak name's −66.7% 12-month relative was
**company-specific** (guide cut 40%→36%, China −22%, $35B acquisition amortization, an open-source
EDA demo threatening the moat) — never a cycle signal.
Lead-lag is one correlation table to test and expensive to get wrong; it is the claim class most
likely to be repeated on authority.
**Source** retracted R5 (new failure class; cousin of S2)

### W3 · Information being real is not the same as it being profitable
**Fires when** you claim an edge, an alpha, or a tradable signal.
**Check** you reached the **enterable** window and subtracted round-trip cost.
**Measured failure** — unscheduled preliminary earnings disclosures produce a D+1 open gap of
**+50.6bp** (shuffle p = 0.0005) — real information, confirmed. But filings arrive after the close,
so the only enterable window (D+1 open→close) is **−5.3bp, p = 0.79**, and **−40.3bp net** of a
35bp round trip. The built-in placebo: scheduled periodic filings move **+4.0bp**.
**Source** PLAYGROUND §3 · §7-8

### W4 · Name the customers of the node you are concluding on
**Fires when** you write a verdict on any supply-chain node.
**Check** who buys from it, and whether their **disclosed spend** confirms or contradicts. If their
prints are pending, say so **with the date** rather than concluding around them.
**Measured failure** — an entire memory-supply analysis was produced without examining hyperscaler
earnings, the buyers who set the demand. The omission was caught by the user, not the desk.
**Source** retracted R6 (new failure class)

### W5 · State the dispersion inside the sector
**Fires when** you write a sector-level verdict.
**Check** the spread between sub-nodes. If it exceeds the sector's own move, the sector label is the
wrong unit of analysis and the file must say so.
**Measured failure** — 2026-07-21: memory/storage **+12~14%** while GPU/ASIC managed **+2.0~2.2%** —
a ~10pp spread inside "semiconductors" in one session. Calling that day a "semiconductor rebound"
describes something that did not happen.
**Source** this session (lens B5 merged here)

---

# Part B · Lenses (analytical tools, not triggers)

### L1 · Read the second derivative in a price-cycle industry
Commodity-cycle equities track the **rate of change of price**, not the level. The two routinely
point opposite ways, producing the apparent paradox "shortage persists but the equity struggles".
Measured: server DRAM contract prices **+90~95% → +58~63% → +13~18% QoQ** across three quarters while
physical supply stayed short into 2027.
**Use** — for memory, steel, shipping, refining, chemicals, any commodity node: tabulate the **QoQ
change series**. Two consecutive declines in the *rate* is the signal; the level is the distraction.

### L2 · The peak-margin / low-multiple trap
A cyclical at its earnings peak prints its **lowest** forward multiple, because the denominator is
peaking.
**Now measured on our own series** (dig D2 closed 2026-07-22 — `scripts/margin_history.py MU`,
SEC XBRL, 17 years FY2009–2025):

```
peak    FY2018  58.9%      trough  FY2009  −9.2%  (FY2023 −9.1%)
median          32.0%      current FQ3'26  84.6%  → 100th percentile, +25.7pp above the 17y peak
```

The press figure we had been citing ("59%") is confirmed exactly — **but it is now our data, not a
quotation.** Two negative-margin years inside 17 is the amplitude this industry actually runs.
**Use** — put the forward multiple **next to** the margin percentile before calling anything cheap.
A multiple without a margin percentile is not a valuation. `scripts/margin_history.py <TKR> --current <gm>`
prints the percentile directly; it works for any SEC filer, so build the series once per cyclical.
⚠ XBRL trap baked into the script: `companyfacts.fy` is the **filing** year, so a 10-K carries prior
comparatives — filtering by that field pairs mismatched periods and yields margins near **−200%**
(measured on the first attempt). Filter by **period length (340–400 days)** instead.
**Counter held open** — long-term agreements with price floors may raise the trough structurally
(STANDING_VIEW C1, unmeasured).

### L3 · Grade branches by information content before the event
Outcomes are not symmetric: one branch may only confirm, while the other can falsify.
Measured framing — a hyperscaler capex **cut** breaks both the volume and the price leg of a memory
thesis; a **raise** confirms volume only, and cannot un-measure the contract-price series because the
same buyers signed the price caps.
**Use** — before bracketing a binary, write down which branch would change the conclusion. **If
neither would, the event is not worth waiting for.** Score the observable, not the price reaction.

---

# Part C · The open dig list

Ordered by how much each would change the standing view. D9/D10 are **recovered from `lab/`, where
they sat unread** — both are code defects the lab found, documented, and never fixed.

| # | Dig | Why it matters | Owner stage |
|---|---|---|---|
| **D1** | Do LTA price floors actually hold margin? Pull Micron/Hynix/Samsung long-term-agreement language from filings + call transcripts. | The best counterargument on file (STANDING_VIEW C1). If floors are real, the margin-peak call weakens and this cycle's *shape* differs from every prior one. | DEEP |
| ~~D2~~ ✅ | ~~Memory gross-margin history~~ — **CLOSED 2026-07-22**. `scripts/margin_history.py` (SEC XBRL, 17y). MU peak FY2018 **58.9%**, trough −9.2%, median 32.0%; current 84.6% = **100th pct, +25.7pp over peak**. KR makers still open (DART, not SEC). | Lens L2 rests on "84.6% vs a 59% prior peak" — and that peak came from press, not a series we own. Build once, reuse. | DEEP |
| **D3** | Hyperscaler capex → memory revenue lead-lag, tested the way W2 demands. | M9's "30%→48% of capex" is a two-firm estimate. If capex genuinely leads, that is the real leading indicator W2 killed the fake version of. | DEEP |
| **D4** | Score S1–S5 in SCENARIOS.md as their dates pass. | Unscored scenarios are how a desk keeps wins and forgets losses. | HANDOVER |
| **D5** | 009150 Samsung Electro-Mechanics — resolve STANDING_VIEW C2. | An explicit coverage gap the KR desk flagged on itself. Substrate/MLCC is a distinct node and may run on the equipment clock. | DEEP |
| **D6** | Re-run the 000660 flow read after 2026-07-29. | The D1 suspension has a known expiry. Reading before is invalid; forgetting after wastes the resolution. | HANDOVER |
| **D7** | Verify KR semiconductor exports MoM from the customs primary. | R2 was created by a half-quote, and the correction is currently **derived** (own arithmetic on two press figures), not a primary read. | MACRO |
| **D8** | Does the equipment cycle actually lag the price cycle? The 042700 thesis assumes it. | Currently `[inferred]` with no measurement — exactly the shape W2 punishes. | DEEP |
| **D9** ★ | **Holdco–subsidiary concentration defect.** `module_paper_book/_config.py:43 MAX_THEME_PCT = 40.0` has no holdco/subsidiary logic, so a parent and its subsidiary count as **different** risk units. | PLAY15 measured **6 of the top 20 correlated pairs are holdco–subsidiary** (LS · 한미사이언스 · 영원무역홀딩스 · HD한국조선해양 ×2 · GS), because KRX classifies holdcos as *financials*. **The wrap-account book is running with this defect now.** ⚠ Code change needs human approval (CLAUDE.md). | wrap_account / human |
| **D11** ★ | **`module_flow` scoring gives a C-grade signal veto power, and weights a rejected one.** `_synthesize.py:26` — `has_conviction = (obv_state == "매집") or (vel >= 1.2)`. On the **US** path there is no investor feed, so **OBV alone unlocks 🟢가속** with nothing to override it. Separately `_synthesize.py:44` adds `red += 1` for *building* short interest. | OBV has **no leading power (t=1.00)** and r≈0.49 vs real flow (PLAY19) — it should not hold a gate. And "short building = bearish" is in the **rejected ledger** (PLAY25: indistinguishable; Law 3 says shorts *supply* liquidity). Proposed: drop OBV from `has_conviction` (keep it as a green-count axis), and drop or invert the short-building red weight. ⚠ **Behavioural change to a live shared module — needs human approval** and a before/after diff on a day of desk output. Until then the interpretation-layer rule D6 handles it. | module_flow / human |
| **D10** ★ | **News body boilerplate.** asiae/sedaily carry **100% page furniture in the first 400 chars**; measured boilerplate share asiae **55.6%**, donga 32.2%, sedaily 16.6%. | Documented as comments in **three** files (`_brief.py:54`, `_burst.py:87`, `_export.py:53`) and never fixed. The lab calls this **"the ceiling on every news experiment"** — fixing it raises the ceiling on all prior work, which beats running a new experiment. | module_news_data / human |

| **D12** | **Borrow fee & utilization**, not just short balance. KRX publishes 대차잔고; US borrow data is harder. | We measure *how much* is short (KRX %float, FINRA daily volume) but not *how expensive/scarce the borrow is* — which is the actual squeeze pressure a trading desk watches. A crowded short on cheap, plentiful borrow is not the same trade as one on a hard-to-borrow name. | module_flow / L2 indicators |
| ~~D13~~ ✅ | **CLOSED 2026-07-22** — `data/catalysts/structural_schedule.json` + `catalyst_calendar` STRUCTURAL block. **Corporate-action & index calendar**: lockup expiries, block deals / secondary offerings, MSCI-FTSE rebalance dates, KRX short-selling overheated designations. | `catalyst_calendar` currently carries earnings and macro only — and the desk logged its own failure: *"catalyst_calendar 모듈이 2런 연속 KR 최대 바이너리를 놓침"*, patched by hand both times. These are **dated, mechanical, knowable in advance** — the cheapest class of catalyst to stop missing. | scripts/catalyst_calendar |
| **D14** | **Intraday order-flow imbalance (OFI)** — signed trade flow, VWAP deviation, opening/closing auction imbalance. | ★ **The lab's own §IV-4 lists this as unresolved**: "Hawkes 전염·진짜 OFI·공시 시각 정밀 이벤트는 일별 데이터의 벽". Daily net-buying is not order flow. Every impact law we measured (concavity δ, 5-day decay, Kyle λ) is a *daily* approximation of an intraday process. Check whether KIS exposes minute bars / tick data first — that determines feasibility. | module_KIS feasibility check first |

| **D15** ★ | **PLAY23 never produced a result.** `Finance_PLAYGROUND/PLAY23_multiple_vs_flow_duel/out/` is **empty** — code and README exist, output does not. The lab doc carried it as "진행 중" for ~3 months. | It is the **only** experiment that directly tests this repo's founding hypothesis — *"multiples are an agreed-upon artificial yardstick; what moves price is flow and crowd psychology"* — via a KOSPI200 cross-sectional Fama-MacBeth duel. **The central claim has never been tested.** ⚠ Its own README flags the constraint: 3y / 20-day non-overlapping = only **27–31 rebalance points**, so "indistinguishable" is the likely honest outcome (rules C4 · S3) — which is still worth knowing, and must be written that way rather than stretched. | Finance_PLAYGROUND / human |

| **D16** 🟢 **AUTOMATED 2026-07-22** (day 1/~40 stored; Windows task `DeGaJa-EstimateSnapshot`, daily 08:10 KST) | **Snapshot `eps_trend` daily so revision IC becomes a time series.** yfinance returns a *snapshot* (current / 7 / 30 / 60 / 90 days ago), not history — so a single run yields **one** non-overlapping observation window. Store the snapshot each day into `data/estimates/` and the panel builds itself. | `scripts/measure_ic.py` can only produce a **single-date cross-sectional IC** today. Per rule S1 the effective sample is the **date count (1)**, not the ticker count — so the IC cannot yet justify an `--ic-n` in `kelly_size.py`. ~40 stored days would give a usable series; the cost is one cron-ish snapshot, and **the data is unrecoverable retroactively** — every day not stored is gone. That asymmetry makes this the cheapest dig on the list to start and the most expensive to postpone. | module_fundamentals_us / human |

**Dig discipline** — D1, D3 and D8 are all mechanism or lead-lag claims the standing view currently
carries as `[inferred]`. Per W2 each is cheap to test and expensive to keep assuming. Test before the
next verdict cites them.

---

# Appendix · Where each rule came from

Consolidated 2026-07-22 from four locations that each held a partial, overlapping list. Twelve rules
were duplicated across two or more; those were merged, keeping every measured example.

| Origin | Held | Disposition |
|---|---|---|
| `lab/PLAYGROUND_SYNTHESIS.md §7` | 9 gates | Merged → C1·C3·C5·S1·S2·S3·S5·S6·W3 |
| `lab/ECONOPHYSICS_THEORY.md §V` | 7 rules | 3 were duplicates of the above; unique → C4·D2·D3·D4·S4 |
| `lab/실험보고서_전체기록.docx §5-5` | 9 rules | **Identical** to PLAYGROUND §7 in plain language. Kept as human-facing narrative; **not a rule source**. |
| This session (2026-07-22) | 12 | New execution-failure classes → C2·D1·D5·W1·W2·W4·W5 + lenses L1·L2·L3 |

**Rule for future edits**: a new rule is added **here**, in trigger form, with its measured failure.
It is *not* added to `lab/` — `lab/` records how a finding was derived, this file records what to do
about it. If a rule ever needs to change, change it here; the lab anchor stays as the evidence trail.
