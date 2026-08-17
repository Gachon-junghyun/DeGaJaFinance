# PROMPT_MAP — full analysis of the prompt-style .md inventory (the L1 map)

> Every prompt/protocol .md of the old repo, read and decomposed through the lens
> "**one stage = one big part = one L1**". This is the map for reorganizing prompts into the
> layered folders of this repo. (Modules: [`../MODULE_MAP.md`](../MODULE_MAP.md); layer rules: [`README.md`](README.md).)

---

## 0. Big picture — 5 desk flows

The prompts form 5 families (desk flows); each flow is a **chain of L1 parts (stages/phases)**.

```
[all desks]  PREFLIGHT (stage −1 — verify the INSTRUMENTS before inheriting any number)
                 │ writes llm_outputs/{date}/preflight/PREFLIGHT.md = a claim-permission table
                 │ a FAILED gate removes a citation right for the run (not a warning)
                 ▼
[all desks]  HANDOVER (stage 0 — inherit the standing view before anything else)
                 │ reads/writes ../handoff/ : STANDING_VIEW · SCENARIOS · RESEARCH
                 ▼
[industry]   MACRO → SWEEP → ROTATION → (PRE-MORTEM) → DEEP → BET → ALPHA → DRIFT
   │ sector pick + name pick ↓
[company]    Phase1 business model → Phase2 earnings quality → Phase3 valuation → Phase4 technical setup → verdict
   │ verdict ↓                                     ↑ chart-analysis (11 branches) embedded
[strategy]   Phase0 cycle → Phase1 value chain → Phase2 names (calls company) → Phase3 port+cards → Phase4 verify
[real-alpha] STEP0 datapack → STEP0.5 self-grade revisit → block A ∥ block B (∥ block D) → block C set-difference → refute → verdict
   └ independent parallel track (READ-ONLY, reference-only). Writes back to the industry board via SECTOR_ALPHA_MAP
[chart]      §0 pre-checks → §1–§11 branches → conflict matrix (M1–M4) → single conclusion  (embedded in company Phase4)
[idle-probe] CENSUS → PAIR → PROBE → CONTROL → ADJUDICATE → SIZE → STAGE_ORDERS
   └ target is the INSTRUMENT and the OPEN QUESTION, not the market. Never writes to ../handoff/ (counter collision D137·D211)
```

**Meta 3 layers** (the reorganization axes): `PROTOCOL (design SPEC)` → `runtime canon (KR·US language-pure)` → `stages/ (on-disk execution chain, each = one L1)`.

### HANDOVER — the cross-desk stage 0 (repo-native, no mvp ancestor)

| Layer | Unit | Role |
|---|---|---|
| L1 | [handover](L1_stages/handover.md) | Inherit the standing view · score matured scenarios · stale-check · load the binding research rules · write the carry back at run end |
| L1 | [leak_audit](L1_stages/leak_audit.md) | **사후 감사** — 끝난 런이 지불하고 걷지 않은 것. 거부·커버리지소실·스쳐감·발굴부재 4클래스 × 선행검정(후행 동어반복 차단) × 창 레짐 라벨링 → 파일·줄 단위 프로토콜 처방 |
| L2 | [carryover](L2_modules/carryover.md) | Read `../handoff/` + reconcile it against the mechanical tag ledger (`module_report_tags`); re-pull anything whose suspension has cleared |
| L3 | [scenario_score](L3_functions/scenario_score.md) | One pre-registered scenario → one branch verdict, against the **frozen** threshold. `EXPIRED` is logged, never dropped |
| L3 | [reject_ledger](L3_functions/reject_ledger.md) | 거부(DROP/PASS/강등) 1건 → 사유클래스 + **부활조건** + 재확인일로 적립하고 사후 채점. `add` 가 두 필드를 강제 |
| L3 | [missed_ledger](L3_functions/missed_ledger.md) | ★ 위의 **대칭 짝**(2026-07-31) — "검토했으나 사지 않은 것" 1건 → **진입조건** + 재확인일로 적립·채점. **부호 반대**(`excess>0` = 놓쳐서 손해). 거부 원장과 같은 티커×날짜는 `add` 가 기계로 막는다 |
| L3 | [ic_ledger](L3_functions/ic_ledger.md) | ★ **이 데스크의 시계** — 신호 축의 횡단면 IC 를 런당 1행 적립. 11포지션 손익으로 배우면 수십 년, 828종목 랭킹으로 배우면 **3~5개월**. `필요n` 열이 축을 언제 죽일지 말한다. **겹침 보정(NW·n_eff<4 판정불가) + 다중비교(Bonferroni) 내장** |
| L3 | [axis_inflection](L3_functions/axis_inflection.md) | 패턴 발견기(`module_inflection`)의 신호를 IC 축 파일로 내보낸다. **눈금자 → 발견기 순서**를 만드는 배관 — 새 축은 파일만 떨구면 되고 원장 수정 0 |
| L3 | [exposure_state](L3_functions/exposure_state.md) | ★ 노출 규칙의 현재 상태(정상/방어/**복귀**/과열) + 목표 투자·**현금** 비중 읽기. 읽기 전용(적립은 타임폴리오 태스크 소유). **현금 타깃의 단일 원본**(F5) |

**Why it is stage 0 and not a closing step.** The ledger in `pipeline/handoff.md` answers *what was
covered*; nothing answered *what we believe, what we pre-committed to, and what we already retracted*.
Measured 2026-07-22: six judgments reversed **inside one session** — a cross-listing venue distortion
read as directional flow, a half-quoted export print, a KR-measured signal applied to a US index, an
unlabelled benchmark, an uncited lead-lag claim repeated on authority, and the demand side of the
thesis never examined. All six were carry failures, not data failures — so the fix belongs *before*
the first proposition is formed, not after the last.

**Where its rules are enforced** (loaded by HANDOVER, binding downstream):
MACRO — cite both halves of a print · name the benchmark · no cross-market signal transfer.
DEEP — second-derivative reading for price cycles · peak-margin vs low-multiple check · name the
node's customers · test or tag every lead/lag claim · state sub-sector dispersion.
PREMORTEM — grade branches by information content · freeze observable+threshold at registration ·
score the observable, not the tape · date-clustered moves are n≈1.
L2 indicators — check for a second listing venue before reading domestic flow · cross-check
providers before theorizing about a late series.

---

## 1. Industry (industry_us / industry_kr)

Purpose: rank "where the wind blows" from macro propositions, deep-dive only the OW 3–4 down to the
value chain. Zero buy/sell calls. Output root `REPORT/industry_{KR|US}/`; previous folder read-only.

| L1 | Phase | Calls | Input → output |
|---|---|---|---|
| **0** | MACRO | **both: `embed sync` → `brief`(events) → `thread --days 7`(trajectories)** · KR: `news_fts --kr --syn` · `news blindspot --domestic` / US: `module_macro_us`(FRED) · `us_flow --cot` · `catalyst_calendar` | events + trajectories + 7-bucket news + daily anchor → `MACRO_REPORT.md` (proposition table + ★transmission matrix + hit-rate) |
| **0.5** | SWEEP | `sector_flow --market {kr\|us}` · `{kr\|us}_live_shortlist` · (US) `cycle_exposure` | universe CSV → `SECTOR_FLOW.json` · `LIVE_SHORTLIST.json` · (US) `CYCLE_EXPOSURE.md` |
| **0.7** | EVENT_ALPHA | `thread --days 7`(scope market-locked) · `drill_detail` · `chain-hop`/`industry_map` · `module_flow`/`us_flow` · `report_tags` | building threads × money flow → `EVENT_ALPHA.md` (forward cards; CONFIRMED-EARLY → ROTATION/BET, ENDED-thread book flags) |
| **1** | ROTATION | `news_fts --count` (velocity) · `module_industry_map` | matrix + flow → `SECTOR_ROTATION.md` (11-sector OW/UW + 4 DEEP + DEEP_LOG) |
| **1.5** | PRE-MORTEM *(US only)* | 4 adversarial subagents (fan-out) | rotation draft → `BLINDSPOT_PREMORTEM.md` |
| **2** | DEEP | KR: `module_industry_map` · `module_business` · `module_disclosure` · `module_chart --read` / US: `module_business_us` · `module_disclosure_us` · `chain-hop` · `us_flow` | 4 targets → `SECTOR_DEEP_{code}.md` ×4 |
| **3** | BET | `module_valuation` · `module_math_check` · `module_flow` · (US) `us_setup_screener` · `module_fundamentals_us` | 4 DEEP → `BET_SHEET.md` (per-sector §A–§E) |
| **4** | ALPHA | `module_flow --positioning` · (US) `theme_age` · `action_bracket` · WebSearch | BET_SHEET → §B tags (🟢LIVE/🟡PARTIAL/🔴RESOLVED) · (US) `ACTION_TICKETS.md` |
| **post** | DRIFT *(US)* | `drift_watch` | +3–6h kill-switch burst → MACRO_REPORT §5 ADDENDUM |

**News has two axes** (L2 `news`): **term** (`news_fts`·`blindspot`·`chain-hop` — "is my theme hot?")
and **event** (L3 `daily_events` → `brief` — "what happened today, all of it"; L3 `event_threads` →
`thread --days 7` — "how each event moved across the week", BUILDING/FADING curves). Not substitutes —
measured on the KOSPI −8% circuit-breaker day the term `코스피` ran at 1.3× normal and ranked
**nowhere**, while the event view had it at [39 articles/8 outlets]. Terms spike when *new*; events
rank when *big*; and a snapshot cannot show runway — the BOK rate-hike saga sat at 2 outlets 5 days
before the hike (`2→7→6→7→5→8`), visible only as a trajectory. ⚠ Event axis is **client-only** (GPU,
CLAUDE.md P6); market/non-market filtering is
**KR-only** (Korean-trained classifier — foreign feeds are 82% finance already, so nothing is filtered).

**KR/US asymmetry (core)**: KR = 6 stages (no PRE-MORTEM/DRIFT), no macro primary module (cross-reads
US MACRO §A), but has **KIS per-investor net-buy actuals** (real-hands/weak-hands) that the US lacks.
US = 7+ stages with the anti-tunnel five (catalyst injection · cycle_exposure · premortem ·
action_bracket · drift — all born from the 2026-07-14 postmortem).
**Gates**: macro gate (only OW enters DEEP) · EXIT-CHECK chain · 4-DEEP selection (2 continuous + 2 rotating)
· Phase-4 bettable (🔴 dropped) · momentum-only hard-stop.

---

## 2. Company (company_analysis US/KR/PROTOCOL)

Purpose: dissect ONE name the industry desk picked, trader's lens → a **"do we bet"** trading verdict.
Input: one 🟢LIVE BET_SHEET name + THESIS_SEED + HORIZON. Output: `{date}/company_{ticker}/COMPANY_ANALYSIS.md`.

| L1 | Phase | KR | US |
|---|---|---|---|
| **1** | Business model | `module_business --include-ir --include-dart` + domestic search | `module_business_us --full` + foreign search |
| **2** | Earnings quality | `module_disclosure` + DART fnlttSinglAcntAll | `module_fundamentals_us` + SEC XBRL CompanyFacts |
| **3** | Valuation/catalyst | `module_valuation --peers` (+ global-peer WebSearch) | `module_fundamentals_us` + yfinance multiples |
| **4** | Technical setup | `module_chart` + **chart-analysis 11 branches** · `module_flow .KS --bench ^KS11` | `module_chart` + SMA200/MACD/ATR · `module_flow --bench SPY --positioning` |
| verify | | `module_math_check` + adversarial self-review | same |

**Gates**: above-SMA200 gate · MACD/flow confirmation (no OBV-alone) · catalyst mandatory (else
value-trap discard) · upside/|downside| ≥ 1.5 · opinion-anchoring block · double verification.
**PROTOCOL = master SPEC; US/KR = runtime stamps.**

---

## 3. Strategy (strategy_protocol)

Purpose: the synthesis layer above industry→company → **"how do we run the book"** (port, sizing, exits).
Input: BET_SHEET · COMPANY_VERDICT · MACRO · CARDS · HORIZON. Output: `strategy_{KR|US}/STRATEGY.md`
(FULL) / `TRACK.md` + alert_bot mechanization.

| L1 | Phase (FULL mode) | Calls |
|---|---|---|
| **0** | Cycle read + risk budget | `trading_engine dashboard` · `module_macro_us` |
| **1** | Value-chain selection | `module_industry_map` (KR) |
| **2** | Per-name company analysis | **calls the COMPANY_ANALYSIS_{KR|US} subroutine** |
| **3** | Portfolio + viewpoint cards | `trading_engine size/exits` · `alert_bot` (card mechanization) |
| **4** | Verify | `trading_engine enforce/checklist` |

**Modes**: weekday split (FULL Mon·Thu / TRACK Tue·Wed·Fri / skip weekends). **KR/US asymmetry (§9)**:
US = full execution machine (all trading_engine commands), KR = surveillance layer (alert_bot alarms +
reports only). **Gates**: hard block on live writes · self-financing · stops move UP only · sizing caps ·
catalyst D-1 freeze · alpha freshness (🔴 disqualified).

---

## 4. Real-alpha (real_alpha_company_research US/KR)

Purpose: one company per day, forensic — **"is it REAL"**. News = the defendant's testimony;
verification = primary sources (EDGAR/DART) + actual money movement. **Reference-only (non-binding)**,
a different axis from company-analysis "do we bet".
Output: `real_alpha{_kr}/{date}/{T}/REPORT.md` · `verdict.json` · `ledger.json` + `SECTOR_ALPHA_MAP{_KR}.md` · `SECTOR_BEAT_HANDOFF{_KR}.md`.

**BUILT** as `protocols/real_alpha_kr.md` (8 L1 blocks, compile-verified) — reuses our modules, no mvp
`real_alpha_datapack.py` dependency. Run stage-by-stage via `run_protocol.py real_alpha_kr` (context-loss guard).

| # | L1 stage | Content · calls |
|---|---|---|
| 0 | PULSE (opt-lead) | same-day tape sanity if the name is moving hard today |
| 1 | FORENSIC_PACK | STEP-0 datapack frozen before reasoning — `module_valuation`(컨센/PER) · `module_business`(DART 사업보고서) · `module_disclosure`(공시 digest) · `money_trail` · `module_chart --read` · `filing_diff` · news velocity |
| 2 | SELF_SCORE | grade prior observation points hit/refuted/pending (skip if first research) |
| 3 | **CHAIN_ALPHA** (Block A+) | analyst-grade value-chain, 7 lenses: 마진포착 노드지도 · 세그먼트 단위이코노믹스 · 계약 book-to-bill(`contract_alpha`) · 고객/공급 의존그래프 · 경쟁 스펙표 · 가격전가력 · 미스프라이싱 노드 |
| 4 | MONEY_FORENSIC (Block B) | is the money real — `money_trail`(외/기/개 수급·insider·treasury·short) + `accruals_check`(NI↔OCF·재고/채권·one-off) + 말vs행동 괴리표 |
| 5 | SET_DIFF (Block C) | `set_difference`: ②실측 − ①선반영 = alpha, ①−② = risk unseen (valuation veto) |
| 6 | FALSIFY | strongest bear case first → reject/uphold with A/B evidence + one PLAY43 refutation hammer |
| 7 | VERDICT | **4-tier** REAL / REAL-but-PRICED / INFLATED / BROKEN + delta line + dated observation points + ledger merge |

**KR data axes**: DART(rcept 원문) · KIS per-investor 일별 순매수 · KRX shorts · yfinance 재무제표(NI/OCF/capex/재고,
`.KS/.KQ`). Gaps: insider trade price 미상 · single-stock options 없음 · procurement needs `DATA_GO_KR_KEY`.
Output: `llm_outputs/{date}/real_alpha_kr/{code}/REPORT.md · verdict.json` + `real_alpha_kr/ledger.json`. binding:false.

---

## 5. Chart analysis (technical_analysis.md · 11 branches + M1–M4)

Purpose: one ASCII chart → all 11 branches without omission → conflicts resolved by meta-rules →
a single trading conclusion. **Embedded in company Phase 4.**
Input: `module_chart` CHART_READ .txt (yfinance fallback when API off). Output: direction · entry ·
stop · target + ONE deciding variable.

11 branches: §0 pre-checks · §1 patterns · §2 trend · §3 momentum/mean-reversion · §4 volatility
(TTM squeeze) · §5 volume/money-flow (+KR investor decomposition) · §6 support-resistance/structure ·
§7 theory (Dow·Elliott·Wyckoff) · §8 quant/stats (HMM·DTW) · §9 sentiment/positioning · §10 breadth ·
§11 relative strength/RRG.
Meta-rules: **M1** academic-alpha weighting (TS-momentum > mean-reversion > volatility > volume) ·
**M2** horizon priority · **M3** uncorrelated-branch confluence ("3 uncorrelated > 100 of one") ·
**M4** axiom violation (events) → invalidate & rerun.

---

## 6. Wrap account (wrap_account) — repo-native, no mvp ancestor

Purpose: run the **same** paper book as a **discretionary mandate** instead of one undifferentiated pile.
Sector target weights are declared, and the book is managed against them: drift bands, single-name and
correlated-theme caps, and a portfolio beta band. This desk has no old-repo prompt — it was built here
(`protocols/wrap_account.md`, 8 L1 blocks, compile-verified). Engine = `module_paper_book._allocate`
(mandate tables live inside `data/paper_book.db`). Output `llm_outputs/{date}/wrap_account/`.

| # | L1 stage | Content · calls |
|---|---|---|
| 1 | MARK *(reused)* | `module_paper_book status`/`mark` — equity, cash sleeves, P&L, stop-hits |
| 2 | MANDATE_SET | `mandate --set` per market (KRX / GICS sector names) + `--band` + `--map` for unmapped ADRs + `--target-beta/--beta-band`; cash target = 100 − Σ targets |
| 3 | DRIFT_CHECK | `drift` — target vs current weight in pp, band breach, cash vs cash target, book beta (L3 `portfolio_beta`, KR `^KS11` / US `SPY`) |
| 4 | INTAKE *(reused)* | reports → candidates, **read after the drift** so only the short sectors are shopped |
| 5 | DECIDE *(reused)* | trade the breach or carry it; which 🟢LIVE name fills each `NEEDS_CANDIDATE` gap |
| 6 | REBALANCE_PLAN | `rebalance [--to target\|band]` — deterministic trims (weakest = smallest stop-distance first) / adds (strongest first), `MAX_POS_PCT` ceiling + post-plan `MAX_THEME_PCT` re-check |
| 7 | SIMULATE *(reused)* | fills, DRY-RUN unless a human passes `--commit` (paper ledger only) |
| 8 | REVIEW *(reused)* | journal + track record + mandate-compliance note |

**Judgment boundary (P4)**: the module owns everything with one right answer (drift pp · the amount to move ·
which *held* name absorbs it · the caps). It refuses to pick a **new** name for an underweight sector — that
returns `NEEDS_CANDIDATE` + the amount, and DECIDE fills it from the research desks' ledger.
**Gates**: bands as the anti-churn device · 🔴RESOLVED cannot fill a gap (freshness veto outranks the mandate) ·
correlated basket capped as ONE risk unit · per-currency cash sleeve (KRW cash cannot fund a US add) ·
`--commit` human-only, no scheduler.

---

## 8. Morning brief (morning_brief) — repo-native, no mvp ancestor

Purpose: **publish**, not research. Turn the previous desk run + the overnight foreign session +
today's calendar into one pre-open file a person reads on a phone at 08:30 KST. No new number, no
view, no recommendation. Output `llm_outputs/{date}/morning_brief/`.

| # | L1 stage | Content · calls |
|---|---|---|
| 1 | BRIEF_GATHER | candidate facts + **origin** + asof *session* + 08:30 availability — L2 report_read(prev run) · news(**`--scope domestic` on the PREVIOUS trading day = the spine**, plus `--scope foreign` overnight; both incl. the 1-outlet + non-market boundary sections) · schedule(10-day) · bookkeeping(prior-session marks, read-only) |
| 2 | BRIEF_RANK | 5-tier consequence order (resolves ≤48h → moved overnight → confirmed yesterday → dated this week → standing) · **domestic-first fill, foreign rows admitted on the domestic-print test (W6)** · ~15 cap **with a counted cut list + the domestic/foreign split** · bias check |
| 3 | BRIEF_RENDER | Korean plain text, fact-first, `출처:` per item (**Korean outlet cited for foreign items too**) — L3 `public_source` ban list swept by grep |

**Why it needed its own L3** (`public_source`): the 2026-07-23 draft cited **our own filenames** as
sources on 4 of 8 items. Every one had a public origin it walked past. The unit's rule is one line —
*cite where the fact entered the world, not where we wrote it down* — plus a translation table so
desk tags (🟢가속 매집 · BUILDING · RS60 · D-0) become plain Korean instead of being deleted.
**★ Whose morning is it — wired 2026-07-24 as trigger W6** (`handoff/RESEARCH.md`, and into the
protocol header + all three stage EXIT CHECKs): **the reader is in Korea, so the domestic pool is the
spine and each foreign row earns its place by having been printed for domestic readers.**
The measured reason it has to be said out loud: the overnight foreign pool held **810 market events
off 5,576 articles** against the prior domestic session's **357 off 3,093** — **the foreign pool is
larger by construction every day**, so ranking by event size hands the editorial line to the wrong
market *by default*, not by mistake. That run's first draft did exactly that and the user corrected it
(*"너무 외국 중심이야 한국 풀에서 놀아야 해"*). Rebuilt domestic-first: **8 of 15 published items
domestic-origin · the other 7 foreign-origin but all 7 already printed by Korean outlets (7/7) ·
the separate foreign event pass contributed 5 candidate rows of 810 (0.6%) · zero coverage lost**.
★ The finding: the overnight facts a KR reader needs **reach the domestic pool by 08:30 anyway**, so
the domestic-print test loses nothing and simultaneously doubles as a date check and picks up figures
the English wires drop (두바이유 90달러선 · 원·엔 900원선 existed only in the Korean copy).

**Gates**: no mid-session number in a pre-open file · every `출처:` checkable without this repo ·
zero recommendation · cut count published so the reader knows it is a selection ·
**domestic/foreign split published in both the rank file and the reader-facing closing note**.

---

## 10. Preflight (preflight) — repo-native, no mvp ancestor · **stage −1 of every desk**

**한 줄**: 데스크가 오늘 쓸 **계기가 작동하는지**를 몇 분 안에 검사하고, 실패한 게이트마다
**오늘 이 런이 주장할 수 없는 것**을 확정한다. 산출은 보고서가 아니라 **권한표**다.

| Layer | Unit | Role |
|---|---|---|
| L1 | [instrument_check](L1_stages/instrument_check.md) | 게이트 7개 × (명령 · PASS 조건 · **FAIL 시 박탈되는 주장 권한**). UNKNOWN = FAIL |
| L1 | [census](L1_stages/census.md) *(idle_probe 와 공유, 주1회)* | 실행표면 인구조사 — 완전유휴 / 배선안됨 / shim |

**게이트**: G1 뉴스축 생사 · G2 채점 척도 연속성 · G3 섹터 부호의 주인 · G4 위험단위 안정성 ·
G5 유니버스가 보유를 덮나 · G6 계측 적립 속도 · G7 도구 생사.

**측정된 기원 (2026-08-09~10).** 하루에 **계기 결함 12개**가 나왔고 **하나도 예외를 던지지 않았다** —
전부 그럴듯한 숫자를 줬다. 뉴스축이 죽으면 축이 드롭돼 **전 종목 점수가 +0.305 부풀었고**,
`clip(nan)=+1.0` 이라 **결측이 최대 양수**를 받았고, KR 스윕이 한국 기업명을 **해외 영문 풀**에
조회했고, 섹터 26개 중 **10개**의 부호가 한 이름에서 나왔고, 책이 **보유한** 두 종목이 유니버스
밖이었다. ⇒ 문제는 데이터 부재가 아니라 **「측정했다고 믿은 자리에서 계기가 값을 지어낸 것」** 이었다.

**`idle_probe` 와의 분업**: 발견은 idle_probe(느리고 창의적), **재발 방지는 preflight**(빠르고 지루).
섞으면 매일 도는 것이 무거워지고, **안 도는 검사는 없는 검사다** — `measure_ic` 가 툴킷 표에 등재된
채 3주간 호출 0 이었던 것이 그 증거다.

---

## 9. Idle probe (idle_probe) — repo-native, no mvp ancestor

**한 줄**: 이 리포가 **소유했으나 부른 적 없는 실행표면**을 데스크가 **이미 등록해 둔 미해결 질문**과
교차시켜 가설로 만들고, 통제군까지 돌려 닫는다. 대상은 시장이 아니라 **계기와 질문**이다.

| Layer | Unit | Role |
|---|---|---|
| L1 | [census](L1_stages/census.md) | 실행표면 인구조사 — **CLI 호출문 기준**(언급 기준은 3~15배 부풀려진다). 완전유휴 / 배선안됨 / shim 3분류 |
| L1 | [pair](L1_stages/pair.md) | 유휴 능력 × 등록된 질문(dig · §6 열린 모순 · 관측값 빈 브래킷) 교차 → 가설. 분기 정보량(L3)·검정력(S3) 사전판정 |
| L1 | [probe](L1_stages/probe.md) | v번호 사슬로 실행. 외부 호스트가 막으면 **재구현 말고 소유 모듈 import**(P1). 숫자마다 `[1차]`/`[2차]`/`[추론]` |
| L1 | [control](L1_stages/control.md) | 통제군 + **아무도 안 고른 기본값 스윕**(최소 3점) + 계기 자기평가 검증 + **이 런 자기주장 재검**(D48) |
| L1 | [adjudicate](L1_stages/adjudicate.md) | 축 충돌을 `module_epistemics` 로 구조화. LR 은 **축 등급에서 유도**(D6), C급 단독 명제 금지, 잔여충돌 명시 |
| L1 | [size](L1_stages/size.md) *(재사용)* | 크기를 **고르지 않고 묻는다** — `kelly_size --ic` 스윕으로 "거래가 열리려면 IC 가 얼마여야 하나" |
| L1 | [stage_orders](L1_stages/stage_orders.md) *(재사용)* | 조건부 intent 카드 → `kis_stack.json`. **사람이 [체결]로 발사**(P5) |

**측정된 기원 (2026-08-09).** `handoff/README.md` 는 자기 도구표 서문에 *"아무도 안 부르는 능력은
존재하지 않는 능력"* 이라 적어놓고 **그 표 안에 호출 0 인 명령을 3주간 담고 있었다**
(`scripts/measure_ic.py`). 인구조사를 처음 돌리자 완전유휴 6개가 나왔고, 그중 하나를 3주 묵은 열린
모순(**C1**)과 등록 dig(**D1**)에 이었더니 최상단 레짐 콜의 증거 1번을 다시 쓰게 만드는 1차 출처가
나왔다. **새 데이터도 새 모델도 아니고, 이미 산 도구를 처음 겨눈 것이다.**

**종결 규칙** — 모든 가설은 `ic_ledger` 축 · 스택 카드 · 등록 dig · 철회 후보 중 **하나 이상**으로
착지해야 한다. 산문으로 끝나면 그 사이클은 실패로 적는다.

---

## 7. Open reorganization decisions (unresolved — a human locks these)

- **Folder axes**: (a) meta layer (spec/runtime/stage) × (b) Phase L1 × (c) runtime KR/US — how to fold 3 axes into folders.
- ~~**Name substitution**~~ ✅ **CLOSED 2026-08-10** — verified by grep: `module_kis` / `module_text_chart`
  appear **zero** times in `pipeline/`. Remaining hits are historical `llm_outputs/` files (not edited) and
  one `handoff/` asof entry that *records* a DEEP brief having emitted the dead name — kept as the receipt.
- ~~**Dead references**~~ ✅ **CLOSED 2026-08-10** — the last live call site was
  `module_industry_map/_renderer.py:55`, which printed *"(c) use `module_scenario_scan` + `search_news_alert`"*
  as an instruction to the reader. Replaced with existing modules.
  ★ **Why this mattered more than a stale comment**: the renderer *tells an agent what to run next*.
  A directive to a module this repo does not have is silently dropped or substituted — measured on
  2026-08-06, when a DEEP brief ordered `module_text_chart` and the agent quietly swapped in
  `module_chart`. **An instruction that cannot execute does not fail loudly; it just stops happening.**
- **KR/US asymmetry**: keep the common-skeleton + runtime-delta pattern (the US anti-tunnel five don't exist in KR).
- **Unported dependencies**: strategy needs `trading_engine` · `alert_bot` (not in this repo yet); real-alpha needs `real_alpha_datapack{_kr}.py` (unported) — migration order to be decided.
