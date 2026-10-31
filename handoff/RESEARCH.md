# RESEARCH — desk research rules, ranked by impact (thin)

> **What this is.** The research triggers the desk must fire *while working*, ordered by impact, plus the dig list
> that is still alive. Rebuilt 2026-10-31 from [`_archive/2026-10-31/RESEARCH.md`](_archive/2026-10-31/RESEARCH.md) (948 KB, kept byte-identical).
> **When to read:** HANDOVER at run start, in full; every stage cites rule IDs from here. **Not here:** archived rules
> (end of file), closed or stale digs, per-run dig blocks, staged rule candidates — all in the archive (`A:Lnnn`).

**How impact was ranked (2026-10-31).** (a) the rule came from a measured failure (all kept ones did); (b) it was
actually cited in recent desk output — counts are raw ID mentions in `llm_outputs/2026-09-01…10-15/**.md`, 575 files,
excluding `_bak_*`/`_carry_*` copies (⚠ `C1–C5`, `S1–S6`, `D1–D6` share IDs with old contradictions/scenarios/digs,
so their counts are upper bounds); (c) it makes the desk **read earnings, guidance, competition and the financial
environment** — the new desk skeleton. Measured reason for (c), `module_lens` first learning over 165 legacy brackets:
filings/earnings/guidance evidence hit **6 of 8 (0.70)**, macro 0.38, price 0.43, news 0.41, **investor flow 5 of 32
(0.18)** (orchestra BRIEF 2026-10-31). ⇒ **Tier 1 = rules that make you read the business and the money environment;
flow evidence corroborates, it never carries a conclusion alone (D6).**

| Rank | Rule | Fires when | Cites 09-01→10-15 | Tier |
|---|---|---|---|---|
| 1 | **C2** | Both halves of a print | 237 | 1 · reads the business/money |
| 2 | **L1** | Read the second derivative in a price-cycle industry | 484 | 1 · reads the business/money |
| 3 | **L2** | The peak-margin / low-multiple trap | 283 | 1 · reads the business/money |
| 4 | **W4** | Name the customers of the node you are concluding on | 44 | 1 · reads the business/money |
| 5 | **W5** | State the dispersion inside the sector | 258 | 1 · reads the business/money |
| 6 | **W3** | Information being real is not the same as it being profitable | 55 | 1 · reads the business/money |
| 7 | **L3** | Grade branches by information content before the event | 140 | 1 · reads the business/money |
| 8 | **T23** | a term-burst / drift flag (*"`bankruptcy` spiked 4.7×"*) | 0 | 1 · reads the business/money |
| 9 | **U3** | ⚠ You are about to compare a news-body number to a filing. Ask first whether th… | no ID | 1 · reads the business/money |
| 10 | **D6** | Weight a signal by its measured grade, not by how visible the tool makes it | 485 | 2 · measurement hygiene |
| 11 | **C1** | Baseline and benchmark | 194 | 2 · measurement hygiene |
| 12 | **W1** | A signal's market of measurement is part of the signal | 271 | 2 · measurement hygiene |
| 13 | **C3** | Keep an "unknown" column | 681 | 2 · measurement hygiene |
| 14 | **C4** | Say "indistinguishable", not "rejected" | 195 | 2 · measurement hygiene |
| 15 | **C5** | Expose the arbitrary choice | 204 | 2 · measurement hygiene |
| 16 | **D1** | Check for a second listing venue before reading domestic flow | 202 | 2 · measurement hygiene |
| 17 | **S5** | Short samples invent structure | 175 | 2 · measurement hygiene |
| 18 | **S1** | Fold by date before trusting a t | 95 | 2 · measurement hygiene |
| 19 | **S6** | Tag any label that uses the future | 87 | 2 · measurement hygiene |
| 20 | **D5** | Cross-check providers before theorizing about a late series | 137 | 2 · measurement hygiene |
| 21 | **D2** | Verify the proxy's sign | 113 | 2 · measurement hygiene |
| 22 | **D3** | Signed and unsigned variables are different physics | 106 | 2 · measurement hygiene |
| 23 | **U6** | ⚠ You are about to write "N names confirm it". Check whether the N moves are da… | no ID | 2 · measurement hygiene |

---

# Part A · Tier 1 — read the business and the money environment

<!-- C2: verbatim from A:L54–L61 -->
### C2 · Both halves of a print
**Fires when** you cite a headline economic release (exports, CPI, shipments, orders).
**Check** you quoted **both** the YoY and the sequential figure, on a **like-for-like window**
(1–20th vs 1–20th, never a partial window against a full month).
**Measured failure** — KR semiconductor exports **+180.6% YoY** cited as a bullish catalyst on the
same day the like-for-like window printed **−11.3% MoM**. Half a print is not evidence.
**Source** retracted R2 (no lab precedent — this is a new failure class)


<!-- L1: verbatim from A:L310–L317 -->
### L1 · Read the second derivative in a price-cycle industry
Commodity-cycle equities track the **rate of change of price**, not the level. The two routinely
point opposite ways, producing the apparent paradox "shortage persists but the equity struggles".
Measured: server DRAM contract prices **+90~95% → +58~63% → +13~18% QoQ** across three quarters while
physical supply stayed short into 2027.
**Use** — for memory, steel, shipping, refining, chemicals, any commodity node: tabulate the **QoQ
change series**. Two consecutive declines in the *rate* is the signal; the level is the distraction.


<!-- L2: verbatim from A:L318–L339 -->
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


<!-- W4: verbatim from A:L263–L270 -->
### W4 · Name the customers of the node you are concluding on
**Fires when** you write a verdict on any supply-chain node.
**Check** who buys from it, and whether their **disclosed spend** confirms or contradicts. If their
prints are pending, say so **with the date** rather than concluding around them.
**Measured failure** — an entire memory-supply analysis was produced without examining hyperscaler
earnings, the buyers who set the demand. The omission was caught by the user, not the desk.
**Source** retracted R6 (new failure class)


<!-- W5: verbatim from A:L297–L307 -->
### W5 · State the dispersion inside the sector
**Fires when** you write a sector-level verdict.
**Check** the spread between sub-nodes. If it exceeds the sector's own move, the sector label is the
wrong unit of analysis and the file must say so.
**Measured failure** — 2026-07-21: memory/storage **+12~14%** while GPU/ASIC managed **+2.0~2.2%** —
a ~10pp spread inside "semiconductors" in one session. Calling that day a "semiconductor rebound"
describes something that did not happen.
**Source** this session (lens B5 merged here)

---


<!-- W3: verbatim from A:L254–L262 -->
### W3 · Information being real is not the same as it being profitable
**Fires when** you claim an edge, an alpha, or a tradable signal.
**Check** you reached the **enterable** window and subtracted round-trip cost.
**Measured failure** — unscheduled preliminary earnings disclosures produce a D+1 open gap of
**+50.6bp** (shuffle p = 0.0005) — real information, confirmed. But filings arrive after the close,
so the only enterable window (D+1 open→close) is **−5.3bp, p = 0.79**, and **−40.3bp net** of a
35bp round trip. The built-in placebo: scheduled periodic filings move **+4.0bp**.
**Source** PLAYGROUND §3 · §7-8


<!-- L3: verbatim from A:L340–L349 -->
### L3 · Grade branches by information content before the event
Outcomes are not symmetric: one branch may only confirm, while the other can falsify.
Measured framing — a hyperscaler capex **cut** breaks both the volume and the price leg of a memory
thesis; a **raise** confirms volume only, and cannot un-measure the contract-price series because the
same buyers signed the price caps.
**Use** — before bracketing a binary, write down which branch would change the conclusion. **If
neither would, the event is not worth waiting for.** Score the observable, not the price reaction.

---


### T23 · Credit beside every distress word (verbatim row, A:L2483)
| # | The moment you write… | …check this | Measured failure it closes |
|---|---|---|---|
| **T23** | **a term-burst / drift flag** (*"`bankruptcy` spiked 4.7×"*) | **(a) body-read every match, (b) cite `HY OAS` or `NFCI` in the same paragraph.** A word count is not a regime. | This run's DRIFT: **5 items at 4.7×** decomposed over all **39** day-1 foreign matches to **exactly 1** genuine new US distress datapoint (freight, outside every DEEP sector); the rest were foreign idiosyncratic filings, **one** story carried by 4 outlets, legacy estates, a *"`bankruptcy`-remote SPV"* structuring term, and risk-factor boilerplate. Meanwhile `HY OAS` **2.75** sat **12bp off its 365-day low** and **11bp tighter over 90 days**, `NFCI` **−0.559** within 1.2bp of the year's loosest. **Same shape as the 2026-07-21 narrative-only credit stack.** |

### U3 · A news-body number vs a filing (verbatim row, A:L2384; un-numbered in the archive, labelled U3 here)
| Group | Trigger | Measured failure |
|---|---|---|
| **D** | **⚠ You are about to compare a news-body number to a filing.** Ask **first** whether the number exists in the filing at all — then grade the two cases separately. | Measured 2026-08-17 on `S51-KR`. For the same event, the **denominator** (010950 2Q26 refining OP) reproduced from a news body to **0.0041%** against two primaries; the **numerator** (재고관련이익) **appears 0 times in the entire 3,977,008-character filing**, and the nearest filed line (재고자산평가손실 343,126, 102× the prior year) has the **opposite sign and a different meaning**. ⇒ **"News bodies are unreliable" is the wrong generalisation and would have thrown away an exact number.** The staged 2026-08-03 rule ("when a filing exists for the same event, the filing decides the magnitude — measured at 9.3× on KDDX") assumes a filing exists; **this is the branch where it does not**, and the honest output is an evidence grade, not a correction. |

# Part A · Tier 2 — measurement hygiene (keeps the Tier 1 reading honest)

<!-- D6: verbatim from A:L180–L219 -->
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


<!-- C1: verbatim from A:L44–L53 -->
### C1 · Baseline and benchmark
**Fires when** you write *excess*, *relative*, *outperformed*, *RS20/RS60*, or any conditional return.
**Check** (a) the benchmark is named **in the same sentence**; (b) you measured the window yourself —
including any baseline you were handed.
**Measured failure** — the same 20 days: 005930 is **−12.1% vs SPY** and **+10.1% vs `^KS11`**,
because the KOSPI fell ~26% in a month. Sign flips with the benchmark. Separately, a baseline passed
down in a brief was wrong and two experiments had to correct it: the "−1.72% over 5 days" window was
the news window only; the full year was **+0.95%**.
**Source** PLAYGROUND §7-1 · ECONOPHYSICS §V-3 · retracted R4


<!-- W1: verbatim from A:L232–L239 -->
### W1 · A signal's market of measurement is part of the signal
**Fires when** you cite a statistical result measured in a different market.
**Check** was it replicated **here**? Does the source document record a replication failure?
**Measured failure** — a KR-measured fear-gauge result (t −3.5) applied to VIX/US, while the source
document states the **US mirror failed to replicate**. The repo already enforces this for the news
feed (`--scope domestic|foreign`); it applies identically to statistical results.
**Source** retracted R3 · ECONOPHYSICS §IV-3


<!-- C3: verbatim from A:L62–L69 -->
### C3 · Keep an "unknown" column
**Fires when** you bucket anything into present/absent, hit/miss, news/quiet.
**Check** there is a **third bucket for unknown**. NaN merged into "absent" manufactures a difference.
**Measured failure** — news-z needs a 30-day baseline, so early-May events were all NaN; folding them
into "quiet" contaminated the quiet sample and produced a difference that did not exist (it happened
on the first run).
**Source** PLAYGROUND §7-3 · INFLECTION §2-⑤


<!-- C4: verbatim from A:L70–L77 -->
### C4 · Say "indistinguishable", not "rejected"
**Fires when** a test comes back not significant.
**Check** the write-up says **indistinguishable / no power**, not "no effect". A blank beats a
falsehood (P4).
**Measured failure** — 27 results logged as "rejected" in PLAY6–10 were re-classified as
"undetectable with this data" once power was computed. Nothing had actually been falsified.
**Source** ECONOPHYSICS §V-7 · PLAYGROUND §4


<!-- C5: verbatim from A:L78–L87 -->
### C5 · Expose the arbitrary choice
**Fires when** you pick a weighting, a smoothing, a group count, a scoring panel, or a prior.
**Check** the choice is stated **and** its alternative's effect is known.
**Measured failure** — choices that flipped conclusions: market weighting (R² **0.237 ↔ 0.315**),
filtering vs smoothing (**19.8%** of days disagreed), group-count matching, which residual panel
scores, and the prior (most-likely cause reversed on **41.4%**).
**Source** PLAYGROUND §7-7

---


<!-- D1: verbatim from A:L146–L156 -->
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


<!-- S5: verbatim from A:L128–L134 -->
### S5 · Short samples invent structure
**Fires when** your window is under ~1 year and you report a grouping, cluster, or regime.
**Check** stability separately from fit — they move in opposite directions on short windows.
**Measured failure** — cutting to 244 days dropped membership stability (ARI) to **0.093** while
**within-group correlation went up**. The structure looked better and was less real.
**Source** PLAYGROUND §7-9


<!-- S1: verbatim from A:L90–L98 -->
### S1 · Fold by date before trusting a t
**Fires when** you cite n ≥ ~20 pooled observations, or any panel t-statistic.
**Check** count the **distinct dates**. If n / distinct-dates > ~3, the effective sample is the date
count. (Long-short portfolios are already cross-sectional aggregates — harmless, SE inflation 0.92–1.11.)
**Measured failure** — the same data went from **t = +6.55 to t = −0.74** when folded by date:
233 shock events, 65 of them on one day (2026-06-08). Also 2026-07-21: 18/18 US semis green,
median +5.0% — that is **n≈1**, not n=18.
**Source** PLAYGROUND §7-2 · ECONOPHYSICS §V-2 · INFLECTION §2-③ · retracted (lens B3 merged here)


<!-- S6: verbatim from A:L135–L143 -->
### S6 · Tag any label that uses the future
**Fires when** you use pivot, regime, smoothed-state, or any variable defined with hindsight.
**Check** it is marked `[label]` and never used as a signal.
**Measured failure** — the pivot classifier uses **10 forward days**; its rows show +18~20% moves
that are pure circularity. Warnings are hardcoded into the code and output for this reason.
**Source** PLAYGROUND §7-6 · INFLECTION §2-③ note

---


<!-- D5: verbatim from A:L220–L229 -->
### D5 · Cross-check providers before theorizing about a late series
**Fires when** data looks missing or stale.
**Check** a second and third independent source before concluding the provider is lagging.
**Measured failure** — KIS, Naver, and KRX returned **identical** investor figures through the same
date and all three stopped there, proving the day was unpublished rather than one feed lagging.
One source cannot distinguish those two cases.
**Source** this session (lens B6 merged here)

---


<!-- D2: verbatim from A:L157–L164 -->
### D2 · Verify the proxy's sign
**Fires when** you substitute a proxy for an unavailable series.
**Check** the proxy's sign against a known case before using it directionally.
**Measured failure** — FINRA imbalance **inverts sign** through market-maker hedging; it is unusable
for direction. Conversely, KRX official investor data matched the Naver proxy at **corr 1.0000** —
so proxies are not all bad, they are all **unverified until checked**.
**Source** ECONOPHYSICS §V-5 · PLAY17 · PLAY21


<!-- D3: verbatim from A:L165–L171 -->
### D3 · Signed and unsigned variables are different physics
**Fires when** you model impact, flow, or pressure.
**Check** whether your variable carries a sign. Do not carry a result from one to the other.
**Measured failure** — unsigned volume is **linear** (exponent 1.0–1.6); signed net flow is
**concave** (δ = 0.33–0.38). Concavity is a property of *signed* flow only.
**Source** ECONOPHYSICS §V-4 · Law 1


### U6 · "N names confirm it" (verbatim row, A:L2408; labelled U6 here)
| Group | Trigger | Measured failure |
|---|---|---|
| **W** | **⚠ You are about to write "N names confirm it".** Check whether the N moves are **date-clustered on one driver** before counting them as N observations. | Measured 2026-08-17: `MPC` **+3.10z**, `PSX` **+3.15z**, `VLO` **+2.96z** — individually each clears an "exceptional" bar, and **all three landed in the same five sessions on the same named driver** ⇒ **n≈1, not n=3.** The desk holds two of the three, and a cycle-GAP flag was open on exactly that node the same day. |

# Part C · Open dig list — alive only

Kept: digs cited in desk output from 2026-09-20 on whose definition row is not marked closed, plus the two original
analytical digs (D1 LTA floors, D3 capex→memory lead-lag) that the new skeleton needs. Gist shortened; full row at `A:Lnnn`.
Count = mentions in `llm_outputs` 2026-09-20…10-15. Allocate new IDs with `python -X utf8 -m module_evidence next-id D`.

- **D3** (ID shared with rule) Hyperscaler capex → memory revenue lead-lag, tested the way W2 demands. · A:L359
- **D1** (ID shared with rule) Do LTA price floors actually hold margin? Pull Micron/Hynix/Samsung long-term-agreement language from filings + ca… · A:L357
- **D48** (82) - `D48`/§4c — fired twice on this run's own output and both were appended, not edited away: · A:L4778
- **D650** (51) - `D650` ★★★ — A one-day % change in a continuous futures series is cited only after the two closes are confirmed… · A:L5435
- **D93** (49) A KR sweep row's `last` field is a PRICE, so D79's own `asof ≠ last-date` detector cannot run in KR. Verified this… · A:L862
- **D642** (46) - `D642` ★★★ — Define "real hands" in `kr_live_shortlist` as daily continuity (institution or foreign net-positive… · A:L5280
- **D652** (31) - `D652` ★★★ — Split PREFLIGHT gate G1 into two legs that are scored separately — (a) *query* (the FTS probe answe… · A:L5494
- **D391-KR** (27) - `D391-KR` — KR catalysts do not come from `catalyst_calendar`; build them by hand. · A:L3426
- **D653** (27) - `D653` ★★ — Quote crude and Brent from the named front-month contract (`CLV26`/`CLX26`, `BZX26`/`BZZ26`) in the… · A:L5495
- **D621** (26) - `D621` ★★ — `reject_ledger due` prints a per-name summary (rows / legs met / legs failed) and a name enters the… · A:L5124
- **D584** (21) Give the exposure ledger a settled-bar re-accrual path. A cumulative built from unsettled bars is not a close-base… · A:L4764
- **D645** (16) - `D645` ★★★ — Define every bracket window as "N settled sessions from a printed base date" only, derive the calen… · A:L5392
- **D568** (16) `module_flow/_price_flow.py` 가 종목과 벤치에 위치 인덱스(`iloc[-1]`)를 써서, 벤치 봉이 하루 늦은 날 보드 전체가 낙관 편향된다. 처방: `close`·`bench_cl… · A:L4690
- **D343** (15) ⚠ Date-clustered brackets are ONE observation, not N. 2026-08-28 currently carries SEVEN pre-registered rows (`P67… · A:L2976
- **D628** (13) - `D628` ★★ — `exposure_rule` prints a `⚠repeat-value` warning when NAV% and invested% equal the previous row exac… · A:L5178
- **D657** (12) - `D657` ★★★ — When the benchmark's last bar is older than the constituents' last bar, `sector_flow` cuts every se… · A:L5575
- **D659** (11) - `D659` ★ — `kr_live_shortlist` prints "투자자 미측정" as its own verdict when the investor feed is n/a, separate from… · A:L5577
- **D651** (10) - `D651` ★★ — A ledger revival/entry condition that names a verdict of a scenario that has already settled, or a l… · A:L5440
- **D315** (10) 🚨 `module_flow --positioning` selects the NEAREST option expiry, not the first expiry that COVERS the event — so t… · A:L2748
- **D646** (9) - `D646` ★★★ — Slice the bench on `Close` validity (`dropna(subset=["Close"])`), stamp `asof` from that last valid… · A:L5393
- **D647** (9) - `D647` ★★ — Attach a minimum size to every "sign leg" in a macro proposition or bracket (e.g. |x| ≥ 2% of the na… · A:L5394
- **D649** (9) - `D649` ★★★ — A slope (curve) scenario measures `DGS10 − DGS2` (or the named tenor pair) from H.15, scored on the… · A:L5430
- **D596** (9) `module_valuation` 을 `stock.naver.com` 경로로 갈아타고, 리디렉트(3xx)·본문 0B 를 「미제공」이 아니라 「수집 실패」로 인쇄하라. · A:L4895
- **D528** (8) *A carry file large enough that a run cannot read it linearly must declare its READING METHOD at the head of the r… · A:L4503
- **D640** (7) - `D640` ★★★ — Add a 금융투자 (securities-firm proprietary/trust) daily net-buy series for KR large caps — from KRX in… · A:L5278
- **D8** (7) Does the equipment cycle actually lag the price cycle? The 042700 thesis assumes it. · A:L364
- **D10** (6) News body boilerplate. asiae/sedaily carry 100% page furniture in the first 400 chars; measured boilerplate share… · A:L367
- **D585** (6) Add a MAGNITUDE leg to `top1_flips_sign`: flag when `abs(wflow_ex_top1) < 0.25 × abs(wflow)`. Sign survival is a w… · A:L4765
- **D540** (6) ★★ *The calendar's EARNINGS block fails silently (`yfinance unavailable`) while the same library, called directly,… · A:L4515
- **D656** (6) - `D656` ★★ — On weekend and holiday runs, take each single name's settled close from the yfinance last bar, print… · A:L5534
- **D679** (6) - `D679` ★★ — `module_news_data thread` returns an empty-window report (header + "0 articles") instead of raising… · A:L5763
- **D677** (5) - `D677` — scenario VOID legs on policy need "report + denial" wording. `P168`'s VOID read "dated US product-expor… · A:L5740
- **D660** (4) - `D660` — No AI-exposure factor (beneficiary vs displaced) exists in the toolkit, yet it is the live cross-sectio… · A:L5597
- **D670** (3) - `D670` ★★★ — `sector_flow` aligns benchmark and constituent series on the intersection of their date indices bef… · A:L5667
- **D682** (3) - `D682` ★ — Write into the `SCENARIOS.md` legend that a row settling on "day X close" is scored by the day X+1 pr… · A:L5808
- **D662** (2) - `D662` — `catalyst_calendar` missed the Xi state visit twice (`P161` was registered on a wrong "≈09-21/22" date… · A:L5599
- **D663** (2) - `D663` ★★★ — `sector_flow` drops a benchmark row whose Close is NaN, cuts every constituent to the benchmark's l… · A:L5616
- **D673** (1) - `D673` — BET can double-record a name across the two ledgers or twice in one ledger — `META` was reject-ledgered… · A:L5692
- **D678** (1) - `D678` ★ — A weekend/holiday KR run quotes the prior-night US contract and FX bars with a `[provisional]` tag, a… · A:L5762
- **D680** (1) - `D680` — the G1 falsification probe decays to a structural zero. PREFLIGHT G1's protocol probe (`fts search 삼성전자… · A:L5786

---

**In the archive, not loaded (`_archive/2026-10-31/RESEARCH.md`):** 6 Part-A triggers (S2, S3, S4, D4, W2, W6 — A:L40–L307) · T22 · T24 · T25 (A:L2482–L2485) · 4 un-numbered triggers U1 U2 U4 U5 (A:L2353, L2354, L2406, L2407) · every staged rule candidate and per-run dig block · ~722 other dig IDs. Find one with `grep -n "<ID>" handoff/_archive/2026-10-31/RESEARCH.md` or `python -X utf8 -m module_evidence cite <words>`.

## Change log
- 2026-10-31 — thinned and re-ranked by impact by orchestra branch K3 (archive byte-identical).
