# PROMPT_MAP — full analysis of the prompt-style .md inventory (the L1 map)

> Every prompt/protocol .md of the old repo, read and decomposed through the lens
> "**one stage = one big part = one L1**". This is the map for reorganizing prompts into the
> layered folders of this repo. (Modules: [`../MODULE_MAP.md`](../MODULE_MAP.md); layer rules: [`README.md`](README.md).)

---

## 0. Big picture — 5 desk flows

The prompts form 5 families (desk flows); each flow is a **chain of L1 parts (stages/phases)**.

```
[industry]   MACRO → SWEEP → ROTATION → (PRE-MORTEM) → DEEP → BET → ALPHA → DRIFT
   │ sector pick + name pick ↓
[company]    Phase1 business model → Phase2 earnings quality → Phase3 valuation → Phase4 technical setup → verdict
   │ verdict ↓                                     ↑ chart-analysis (11 branches) embedded
[strategy]   Phase0 cycle → Phase1 value chain → Phase2 names (calls company) → Phase3 port+cards → Phase4 verify
[real-alpha] STEP0 datapack → STEP0.5 self-grade revisit → block A ∥ block B (∥ block D) → block C set-difference → refute → verdict
   └ independent parallel track (READ-ONLY, reference-only). Writes back to the industry board via SECTOR_ALPHA_MAP
[chart]      §0 pre-checks → §1–§11 branches → conflict matrix (M1–M4) → single conclusion  (embedded in company Phase4)
```

**Meta 3 layers** (the reorganization axes): `PROTOCOL (design SPEC)` → `runtime canon (KR·US language-pure)` → `stages/ (on-disk execution chain, each = one L1)`.

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

## 7. Open reorganization decisions (unresolved — a human locks these)

- **Folder axes**: (a) meta layer (spec/runtime/stage) × (b) Phase L1 × (c) runtime KR/US — how to fold 3 axes into folders.
- **Name substitution**: prompts call `module_kis` · `module_text_chart` → this repo has `module_KIS` · `module_chart`. Batch-substitute during migration.
- **Dead references**: remove `module_scenario_scan` / scenario.db call sites (retired).
- **KR/US asymmetry**: keep the common-skeleton + runtime-delta pattern (the US anti-tunnel five don't exist in KR).
- **Unported dependencies**: strategy needs `trading_engine` · `alert_bot` (not in this repo yet); real-alpha needs `real_alpha_datapack{_kr}.py` (unported) — migration order to be decided.
