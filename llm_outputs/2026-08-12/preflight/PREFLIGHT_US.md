# PREFLIGHT — 2026-08-12 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run time KST 2026-08-12 10:50–11:05 (US market closed; Wed 08-12 KST = pre-open Tue-night US) ·
> sweep data **asof 2026-08-11** (last US close, Tuesday).
>
> ⚠ **Filename deviation, logged (same as 2026-08-10):** the composition table names this
> `preflight/PREFLIGHT.md`, but an `industry_kr` run started in the same minute (10:50 KST) and its
> sweep is still in flight; `PREFLIGHT.md` is that desk's rights table. Overwriting a sibling desk's
> output is not a correction, so this US table is written as `PREFLIGHT_US.md` in the same folder.
> Human decision still pending on whether the path should be market-suffixed permanently.

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| G1 news axis alive | 🔴 **FAIL** | Coverage **11.3%** (34/300). Not silence — the remote news API is **unreachable** and the local FTS index is **0 bytes**, while the client-side article store holds **50,234** articles for 08-04→08-11 |
| G2 scoring-scale continuity | 🟢 **PASS** | 3-axis vs 3-axis (`nonews`↔`nonews`), baseline **2026-08-07**, **299/300 names (99.7%) carry Δ**. Caveat: Δ spans **2 trading sessions**, not one |
| G3 who owns the sector sign | 🟢 **PASS** | Flipper list printed — **3 of 11** sectors (Financials/BRK-B · Industrials/CAT · Materials/LIN) |
| G4 risk-unit stability | 🔴 **FAIL** | 250d **8 units** vs 500d/750d **7 units** — NVDA membership splits by window (identical to 08-10) |
| G5 does the universe cover the book | 🔴 **FAIL** | **2 of 8** US holdings outside `us_top300` (**LNG · TSM**, **12th consecutive run**) + universe **28 days** old (limit ≤8) |
| G6 estimate-snapshot accrual | 🔴 **FAIL** | Measured ETA **88 days** vs ideal 32 = **2.75×** (limit 1.5×) |
| G7 tool liveness | 🟡 **FAIL→probed** | 37 entry points, **36 exit 0**; `module_chart` exits 1 on `--help`, functional probe clean |

**PASS 2 / FAIL 5.** Today this desk cannot speak in **news velocity · theme freshness · "it's quiet" ·
single-number concentration · `--ic`-grounded size · flow reads on LNG/TSM**.
**Improvement vs 2026-08-10 (PASS 1 / FAIL 6): G2 recovered** — the Δ baseline is now a same-mode,
299-name, 2-session-old snapshot instead of an 18-day-old 5-ticker scratch run.

---

## G1 · News axis alive — 🔴 FAIL

**Command**
- `SECTOR_FLOW_US.json §scoring` → `{"vel_axis": false, "vel_coverage": 0.1133, "n_axes": 3, "scored": 300, "dropped_missing_axis": 0}`
- Falsification probe, actually executed:
  `python -X utf8 -m module_news_data fts search <q> --days 7 --count --scope foreign` (×5 queries, ×2 attempts)

**Numbers**

| Item | Value |
|---|---|
| velocity measured | **34 / 300 = 11.3%** (threshold 80%) |
| Axis decision | velocity axis **excluded** → all 300 names scored on **3 axes**, uniformly |
| Names unscored (axis missing) | **0** — the D225-KR fix held: no per-name axis-count mixing this run |
| Probe result (all 5 queries, both attempts) | `뉴스 API 접속 실패 … URLError(FileNotFoundError(2))` — **the remote tunnel is down** |
| News API endpoint | `https://impolite-coherent-props.ngrok-free.dev/exec` — **unreachable** |
| Local fallback index `data/news_fts.db` | **0 bytes** (created empty at 10:51 by this run's own call) |
| Local fallback index `data/news_fts_kr.db` | **0 bytes** |

**★ This is the point of the gate — is it the market or the instrument?** Measured answer: **the
instrument**, and this time both halves of the ambiguity are closed by direct evidence.

The client-owned article derivative `data/news_vectors.db` (388,245 articles, sync cursor
`2026-08-11T08:00`) was queried as a substitute probe:

| Window 2026-08-04 → 08-11 | Articles |
|---|---|
| **Total** | **50,234** |
| title contains `Nvidia` | 361 |
| title contains `tariff` | 167 |
| title contains `Broadcom` | 60 |
| title contains `Federal Reserve` | 42 |
| title contains `natural gas` | 26 |
| Per-day | 08-04 **8,973** · 08-05 **9,169** · 08-06 **8,842** · 08-07 **8,013** · 08-08 3,424 · 08-09 3,566 · 08-10 **7,788** · 08-11 459 (partial — cursor stops 08:00 KST) |

So: **the pool is full and the search path is dead.** Collection on the server side was alive through
08-11 08:00 KST; what is broken is every *query* route this desk owns — remote `/exec` unreachable
**and** the local FTS index empty. Writing "US names had no news" today would fail EXIT.

⚠ **Unexplained residue, recorded not resolved:** 34 of 300 names *did* return a velocity while every
manual probe failed. A path that answers for 11% of names while the documented routes return
`URLError` is **non-deterministic**, which is itself a reason not to trust the 34. (Diagnosis is
`idle_probe`'s job — rule 1.)

**Second-order contamination.** The `flow_read` tag still consults news, so the 🟢/🔴 buckets inherit
the same defect. This run: **🟢 17 · 🟡 202 · 🔴 81**. On 2026-08-10 two sweeps twelve minutes apart on
identical prices produced 🟢 23 then 🟢 15 — an ±8-name instability with zero price change. Only one
sweep was run today, so today's 🟢 17 has **no measured error bar**; it must be quoted with its run,
not treated as a stable object.

**🚫 Rights revoked today**
1. **No citation of news velocity (`vel`)** — every stage (SWEEP · EVENT_ALPHA · ROTATION · PREMORTEM · DEEP · BET).
2. **No "this theme is fresh / this theme has gone cold" call.** The freshness axis does not exist today.
3. **No "it's quiet" as evidence.** Today's silence is the instrument's, not the market's.
4. `flow_score` is cited **as a 3-axis score**, and that fact goes **on the same line** as the conclusion.
5. **No 🟢/🔴 headcount or bucket-membership claim treated as stable to ±8 names** — quote it with the run.
6. **No `theme_age` / `chain_hop` / `brief` / `thread` output** — all ride the same dead query path.

*Repair is not this stage's job (rule 1) → `idle_probe` or a human-approved item.*

---

## G2 · Scoring-scale continuity — 🟢 PASS

**Command** `§scoring.n_axes` vs `llm_outputs/sector_flow/history.json` previous same-mode snapshot.

| Item | Value |
|---|---|
| This run `_mode` / `n_axes` | **`nonews` / 3** |
| Matched baseline | **2026-08-07** (`nonews`, **299** tickers) |
| Baseline age | **4 calendar days · 2 trading sessions** (08-07 Fri → 08-11 Tue) |
| Names carrying Δ | **299 / 300 = 99.7%** |
| Ticker overlap baseline∩today | **299 / 299 = 100%** |

Full US history ledger now 19 snapshots; the `nonews` entries are 2026-07-20 (5 tickers, the scratch
run), 2026-08-07 (299), 2026-08-11 (300, this run). `prev_snapshot()` correctly walked past the
thirteen 300-name `news` snapshots **and** past the 5-ticker scratch entry to land on 08-07.

This is the gate that failed on 2026-08-10 and it has **recovered on its own** — not by repair, but
because a second full-scale `nonews` snapshot now exists to compare against. The failure mode is
therefore **dormant, not fixed**: the missing recency+completeness guard on the matched snapshot is
still missing, and it will bite again the next time the news axis dies after a long `news` streak.

**✅ Rights retained, with one condition**
1. Δflow **is** citable this run (SWEEP · ROTATION), including the sector Δ column and the
   `new_green` list (11 names: ABNB · AXON · DASH · KKR · UBER · CVX · ORCL · BRK-B · JPM · CSCO · NVDA).
2. **Condition:** every Δ is labeled **"2 sessions (08-07→08-11)"**, never "today" or "day-over-day".
   A 2-session Δ described as daily is the same class of error this gate exists to catch.
3. Δ is a change in a **3-axis** score. It may not be compared to any Δ printed on or before 08-06.

---

## G3 · Who owns the sector sign — 🟢 PASS

**Command** `§sector_rotation[].top1_flips_sign` — does a list print (0 is a valid list).

**3 of 11 sectors** flip sign when their largest name is removed. Recorded in full:

| Sector | wflow | ex-top1 | top1 | top1_w | n |
|---|---|---|---|---|---|
| Financials | **+0.004** | **−0.060** | BRK-B (Berkshire Hathaway) | 13.9% | 47 |
| Industrials | **−0.015** | **+0.059** | CAT (Caterpillar) | 8.7% | 50 |
| Materials | **−0.069** | **+0.168** | LIN (Linde plc) | 24.7% | 12 |

The other eight sectors keep their sign ex-top1. Largest non-flipping ex-top1 moves, for the record:
Consumer Discretionary (−0.180 → **−0.294**, AMZN 40.2%), Energy (+0.360 → +0.257, XOM 30.5%),
IT (−0.151 → −0.220, NVDA 19.4%), Communication Services (−0.474 → −0.439, GOOGL 38.2%).

Gate **PASSES** (the list printed). Its content still binds ROTATION:
**Financials · Industrials · Materials may not be promoted or demoted on `wflow` today** — use
eqflow / breadth / ex-top1, or hold. Note all three pairs disagree in sign, which is the whole point.
Flippers went **1 → 3** vs 2026-08-10; on a mega-cap-narrow tape this count is itself a breadth reading.

*Caveat carried from G5: every `top1_w` above is computed off a **28-day-old** market-cap column.*

---

## G4 · Risk-unit stability — 🔴 FAIL

**Command** `python -X utf8 scripts/risk_units.py --book --days {250,500,750}` — **all three actually run.**

| --days | units | within-group residual corr | between-group | ARI (first half vs second) |
|---|---|---|---|---|
| 250 | **8** | +0.4346 | — | 0.6565 |
| 500 | **7** | +0.4489 | −0.0002 | 0.5424 |
| 750 | **7** | +0.4388 | −0.0114 | 1.0 |

**The split is at exactly one name — `NVDA`** (unchanged from 2026-08-10):
- 250d: `U0 = {AVGO, TSM}` · `U5 = {NVDA}` (**separate**)
- 500d · 750d: `U0 = {AVGO, NVDA, TSM}` (**merged**)

The other six units (`{KMI,LNG}` · `{009150}` · `{096770}` · `{MA}` · `{RTX}` · `{VST}`) are identical
across all three windows. ⇒ grouping **disagrees** → FAIL. Threshold sensitivity confirms the choice
sits on a boundary: at 250d, `dist 0.75` collapses 8 → 7; at 500d, `dist 0.60` expands 7 → 8. ARI
swings 0.54 → 1.0 across windows, i.e. the fit metric and the stability metric point opposite ways (S5).

**🚫 Rights revoked today**
1. **No single-number concentration guard** (SIZE · BET).
2. Whenever concentration is stated, the `--days` used goes **on the same line** as the conclusion.
3. **Whether `AVGO/NVDA/TSM` is one unit or two is decided by the window** — neither may be asserted today.

*Side observation (not a verdict): the tool warns at each window that the benchmark is `SPY` while the
two KR positions are KRW local returns, so a common FX factor may be injected.*

---

## G5 · Does the universe cover the book — 🔴 FAIL

**Command** builder invariant recomputed (`data/us_universe/*.csv` × `python -m module_paper_book status`).

| Item | Value |
|---|---|
| Book positions | 10 (US 8 · KR 2) |
| **US holdings outside `us_top300`** | **2 🚨 `LNG` · `TSM`** — logged, not fixed, for **12 consecutive runs** |
| US holdings outside `us_all_v2_candidate.csv` (1,522 names, built 2026-08-10 00:53) | **0** — the fix exists; it is not the file the sweep reads |
| `us_top300.csv` age | **28 days** (mtime 2026-07-15 18:04; limit **≤8**) → 🔴 |
| Sweep scale | 300 requested / **300 scored** (0 dropped) |
| KR holdings in `kr_all` | 2/2 ✅ (out of scope for this desk) |

The sweep logged it itself on line 1: `[warn] 유니버스 us_top300.csv 28일 경과 — 시총 stale.`

The character of this failure is unchanged from 08-10 and worth restating precisely: a **1,522-name
candidate universe containing both LNG and TSM exists on disk**. The book's blind spot is not a data
gap — it is a **wiring gap** between `us_all_v2_candidate.csv` and what `sector_flow --market us`
loads. Naming it is this stage's job; changing the wiring is not (rule 1). Note the aging is now
compounding: the market-cap column is 28 days stale, so `wflow` weights and every `top1_w` in G3 are
weights from mid-July.

**🚫 Rights revoked today**
1. **No flow / RS / OBV / short-pressure verdict on `LNG` or `TSM`** (SWEEP · BET · DEEP). Where they
   come up, the line reads **"not measured,"** never "no signal."
2. **`wflow` may not be described as "current market cap"** — the weights are 28 days old.

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL

**Command** `python -X utf8 scripts/snapshot_estimates.py --status`

| Item | Value |
|---|---|
| Accrued | **8 files / 22 calendar days** (2026-07-22 → 2026-08-12), 120 names each |
| Measured rate | **0.36 files/day** (ideal 1.0) |
| To the 40-day target | ideal **32 days** vs measured **≈88 days** = **2.75×** (limit 1.5×) |
| Gaps (days) | [2, 3, 4, 6, 3, 1, 2] · median 3 · max 6 |

Today's file **did** accrue (2026-08-12 present), and the largest gap did not grow — but the rate is
still 2.75× off ideal, which is a FAIL by the gate's own threshold. The tool printed its own trap
warning: *"counted as 'number of files' this instrument looks healthy (D16)."* Not recoverable
retroactively — days not accrued are gone.

**🚫 Rights revoked today**
1. **`kelly_size --ic` output may not be reported as a grounded size** (SIZE).
2. Any size written today is labeled **"mechanical 1/4"**. Calling it IC-based fails EXIT.

---

## G7 · Tool liveness — 🟡 FAIL on 1 of 37, probed back

**Command** `--help` on every entry point this run will use; exit code checked.

**exit 0 — 36 entry points**
Scripts (23): `sector_flow` · `us_live_shortlist` · `us_flow` · `flow_read` · `cycle_exposure` ·
`catalyst_calendar` · `drift_watch` · `action_bracket` · `exposure_rule` · `risk_units` · `kelly_size` ·
`report_lint` · `missed_ledger` · `reject_ledger` · `us_setup_screener` · `axis_window_flow` ·
`axis_inflection` · `snapshot_estimates` · `ic_ledger` · `measure_ic` · `brief_recall` ·
`handoff_compact` · `leak_scan`
Modules (13): `module_macro_us` · `module_news_data` · `module_paper_book` · `module_watchlist` ·
`module_report_tags` · `module_business_us` · `module_disclosure_us` · `module_fundamentals_us` ·
`module_valuation` · `module_flow` · `module_industry_map` · `module_epistemics` · `module_inflection`

**exit 1 — 1 entry point**

| Tool | Why `--help` failed | Functional probe (rule 3: don't manufacture UNKNOWN — measure) |
|---|---|---|
| `module_chart` | **CLI does not implement `--help`** — prints `usage: python -m module_text_chart <ticker> [--read]` then exits 1 | `module_chart NVDA --read` → **exit 0, clean**: OBV accumulating (20d slope **+68%**), no divergence, MA mixed / price above 3 of 4, Bollinger expanding 17.6% at midline, RSI 54.3, momentum20d +2.4%, turn verdict **PULLBACK-TO-SUPPORT**, trigger close>219.44, stop 190.01 |

**🚫 / ✅ Rights**
- By the gate's letter, `module_chart` output would be uncitable. **Under rule 3 the functional probe
  was actually run and returned clean output ⇒ citation right retained**, but the warrant is the probe
  above, not `--help`. Cite it that way.
- The right holds **only for this command form** (`<ticker> --read`). No other argument was measured.
- ⚠ `module_news_data --help` exits 0 — **tool liveness is not data liveness.** The binary is fine;
  its data path is dead (G1). G7 PASS never launders a G1 FAIL.
- ⚠ A dead `--help` means a human cannot discover the tool. Repair is out of scope (rule 1).

Not measured this run (not on the US path): `margin_history.py` (KR fundamentals), `module_KIS`,
`module_disclosure`, `module_fundamentals_kr`, `module_business`, `kr_live_shortlist.py`,
`module_order_desk`, `module_timefolio`, `module_webctl`.

---

## What this table binds in today's run (handed to HANDOVER)

| Stage | May not be used today |
|---|---|
| SWEEP | news velocity · stale market cap described as "current" · LNG/TSM flow tags · 🟢 headcount as stable · any Δ labeled "today" |
| EVENT_ALPHA | "theme is cooling / fresh" · velocity-based forward cards · thread-age arguments · `chain_hop` / `theme_age` output |
| ROTATION | promotion/demotion of **Financials · Industrials · Materials** on `wflow` (flippers) · Δ described as day-over-day |
| PREMORTEM | "the news went quiet on X" as evidence of anything |
| DEEP | news velocity · "it's quiet" · any estimate-revision leg leaning on `--ic` |
| BET / SIZE | single-number concentration · `--ic`-grounded size (→ "mechanical 1/4") · LNG/TSM flow verdicts |

**What remains, stated positively.** This desk today may speak with: **3-axis flow levels** (OBV
accumulation · RS20/RS60 · volume surge), **Δflow against a same-mode 299-name 08-07 baseline** (labeled
2-session), **eqflow · breadth · ex-top1 decomposition**, **FRED macro series** (`module_macro_us`,
untouched by any gate), **FINRA short-volume and CFTC COT positioning percentiles**, **primary filings
and fundamentals** (`module_disclosure_us` · `module_fundamentals_us` · `module_business_us`), and
**chart structure via the probed `module_chart <ticker> --read` form**.
**Speak with price, positioning, Δ, and primary sources. Do not speak with velocity or with freshness.**

*Instrument state is not a market view — this document is not written into `handoff/` (HANDOVER only reads it).*

---
---

# ═══ RUN-2 · PREFLIGHT (same day, second run) — 2026-08-12 22:10–22:45 KST ═══

> **This is an APPEND. Nothing above is rewritten.** The block above is RUN-1's rights table
> (10:50–11:05 KST); this block is RUN-2's. Where they disagree, **the disagreement is the finding.**
>
> **Why a second run exists today.** RUN-1 finished at 11:45 KST and its own headline was:
> *"July CPI prints 2026-08-12 08:30 ET — ~10 hours from this clock. It is the ≤48h binary."*
> That print has now **fired** (08:30 ET = 21:30 KST, ~40 min before this table was opened), and the
> US cash session for 08-12 **opened at 22:30 KST, mid-way through this stage.**
> Clock: **2026-08-12 22:10 KST = 2026-08-12 09:10 ET** (RUN-1's clock was 08-11 22:40 ET).

## Verdict summary — RUN-2

| Gate | RUN-1 | **RUN-2** | One line |
|---|---|---|---|
| G1 news axis alive | 🔴 FAIL | 🟢 **PASS** ⬆ | **The news path came back.** Direct probe **20/20 names (100%)** carry a velocity; API answers (`CPI` 7d **545**, `inflation` 1d **998**) |
| G2 scoring-scale continuity | 🟢 PASS | 🟡 **PASS-with-new-condition** | No new sweep this run ⇒ no new Δ. **New revocation:** RUN-2's 4-axis direct reads may **not** be differenced against RUN-1's 3-axis sweep |
| G3 who owns the sector sign | 🟢 PASS | 🟢 **PASS (inherited, re-read from JSON)** | Same file, list re-printed from source: **3 of 11** flip (Financials/BRK-B · Industrials/CAT · Materials/LIN) |
| G4 risk-unit stability | 🔴 FAIL | 🔴 **FAIL (reproduced, all 3 windows re-run)** | 250d **8** vs 500d/750d **7** — splits at **NVDA**, identical to RUN-1 and to 08-10 |
| G5 universe covers the book | 🔴 FAIL | 🔴 **FAIL — but partially repaired by a different route** | **LNG · TSM** still outside `us_top300` (**13th run**), universe **28d** old. ★ Both were nonetheless **measured directly** this run (see below) |
| G6 estimate-snapshot accrual | 🔴 FAIL | 🔴 **FAIL (unchanged)** | 8 files / 22 days = **0.36/day**; ETA **88d** vs ideal 32 = **2.75×** (limit 1.5×) |
| G7 tool liveness | 🟡 FAIL→probed | 🟡 **FAIL→probed (unchanged)** | **37 of 38** exit 0; `module_chart` exits 1 on `--help`, functional probe clean |

**RUN-2: PASS 3 / FAIL 4** (RUN-1: PASS 2 / FAIL 5). **The single change is G1, and it is a large one** —
it restores the axis that RUN-1 had to run blind on for its entire chain.

---

## G1 · News axis alive — 🟢 **PASS** (was 🔴 FAIL nine hours ago)

**Commands actually executed (RUN-2)**

| Probe | Result |
|---|---|
| `module_news_data fts search "CPI" --days 7 --count --scope foreign` | **545** · `(via NEWS API @ …ngrok-free.dev)` |
| `... fts search "inflation" --days 1 --count --scope foreign` | **998** |
| `... search "consumer price index" --days 1 --scope foreign` | **25** matches (foreign 25 / domestic 0), bodies present |
| `... fts search "CPI inflation" --days 1 --scope foreign --syn` | **29** |
| ★ **Axis-coverage probe** `module_flow <20 names> --bench SPY --json` | **20 / 20 = 100%** carry a news-velocity value |

**★ The 20-name coverage probe is the gate's actual measurement this run**, and it is a *direct* one:
every name returned a velocity multiple (range **0.40× KMI → 2.21× VST**), so the axis is not merely
"reachable", it is **populated per name**.

⚠ **The 11.3% in `SECTOR_FLOW_US.json §scoring` is RUN-1's number and must not be quoted as RUN-2's.**
That file was written at 10:52 KST while the tunnel was down; it is a **frozen artifact of the outage**,
not a measurement of the pool. RUN-2 did not re-run the sweep (see G2 for why), so **the JSON on disk
still says `vel_axis: false, vel_coverage: 0.1133, n_axes: 3` and that remains true of the file.**

**✅ Rights RESTORED for RUN-2 — but only along the route that was probed**
1. **News velocity is citable** when it comes from a **RUN-2 direct call** (`module_flow` / `fts` /
   `search`), quoted **with the call that produced it**.
2. **Theme freshness / "cooling" calls are permitted** on the same condition.
3. ⛔ **Still forbidden: quoting the sweep's `vel` column or its 🟢/🔴 buckets as news-informed.**
   Those 300 names were scored on **3 axes with the news axis dropped**. A sweep bucket and a RUN-2
   direct read are **different instruments** and may not be mixed in one sentence.
4. ⛔ **"It was quiet during RUN-1" is still forbidden** — RUN-1's silence was the tunnel's.
5. The **unexplained residue from RUN-1 is not resolved, only overtaken**: 34/300 names answered while
   every manual probe failed. A path that heals itself in nine hours without an operator is
   **non-deterministic on both ends**. Diagnosis remains `idle_probe`'s job (rule 1).

---

## G2 · Scoring-scale continuity — 🟡 PASS, with a **new** condition RUN-1 could not have written

**RUN-2 produced no new sweep snapshot, deliberately.** The reasoning is recorded because it is a
judgment, not an omission:

1. **There is no new settled US price bar.** The 08-12 cash session opened at 22:30 KST and is *in
   progress*; the last settled bar is still **08-11**. Three of the sweep's axes (OBV · RS · volume
   surge) would be **byte-identical** to RUN-1's.
2. **Re-running would overwrite two records that RUN-1's own reports cite** — `SECTOR_FLOW_US.json`
   and the **`2026-08-11` key in `llm_outputs/sector_flow/history.json`** (the ledger is keyed by data
   date, not run time, so a second run today **replaces** rather than appends). RUN-1's SWEEP_READ,
   ROTATION, PREMORTEM, 5 DEEPs and BET_SHEET all quote that snapshot. Overwriting it would leave the
   day's chain citing a file that no longer says what they say it says.
3. **The one axis that *would* change cannot be mixed anyway.** With the news path alive, a fresh sweep
   would score in **`news` mode (4 axes)**. Differencing a 4-axis score against RUN-1's 3-axis score is
   precisely the arithmetic this gate exists to forbid.

| Item | Value |
|---|---|
| RUN-1 snapshot on disk | `_mode` **`nonews`** · `n_axes` **3** · **300** scored · `asof` **2026-08-11** |
| RUN-1's matched baseline | **2026-08-07** (`nonews`, 299 names), Δ spanning **2 sessions** |
| RUN-2 new snapshot | **none written** (by decision, above) |
| RUN-2 direct reads | **4-axis** (`module_flow` with velocity restored) — **a different scale** |

**Rights**
1. Δflow **from RUN-1's snapshot** stays citable on RUN-1's condition: labeled **"2 sessions
   (08-07→08-11)"**, never "today".
2. ⛔ **NEW:** a RUN-2 4-axis direct read may **not** be subtracted from, ranked against, or described
   as "improved/deteriorated versus" any RUN-1 3-axis sweep score. Where both appear, **each carries
   its axis count on the same line.**
3. ⛔ No Δ may be computed against an intraday 08-12 bar — that bar does not exist yet.

---

## G3 · Who owns the sector sign — 🟢 PASS (list re-read from the JSON, not from RUN-1's prose)

**3 of 11** sectors flip sign when their largest name is removed — re-printed in full from
`SECTOR_FLOW_US.json §sector_rotation`:

| Sector | wflow | eqflow | ex-top1 | top1 | top1_w | breadth | n |
|---|---|---|---|---|---|---|---|
| **Financials** | **+0.004** | −0.043 | **−0.060** | BRK-B | 13.9% | 0.09 | 47 |
| **Industrials** | **−0.015** | +0.048 | **+0.059** | CAT | 8.7% | 0.08 | 50 |
| **Materials** | **−0.069** | +0.018 | **+0.168** | LIN | 24.7% | 0.0 | 12 |

Non-flippers, for the record: Energy +0.360 (ex-top1 +0.257, XOM 30.5%) · Health Care +0.230 (+0.169) ·
IT −0.151 (−0.220, NVDA 19.4%) · Cons Disc −0.180 (−0.294, AMZN 40.2%) · Real Estate −0.222 (−0.127) ·
Staples −0.223 (−0.216) · Comm Svcs −0.474 (−0.439, GOOGL 38.2%) · Utilities −0.475 (−0.446).

⚠ **Note what the breadth column says**: **7 of 11 sectors have breadth ≤ 0.06 and four are exactly
0.00.** The gate passes, but the object it is measuring is a tape where sector signs are owned by very
few names. Binding on ROTATION: **Financials · Industrials · Materials may not be promoted or demoted
on `wflow`** — use eqflow / breadth / ex-top1, or hold.
⚠ Every `top1_w` is computed off a **28-day-old** market-cap column (G5).

---

## G4 · Risk-unit stability — 🔴 FAIL (all three windows re-run this stage)

| `--days` | units | within-group resid corr | between-group | ARI (1st half vs 2nd) |
|---|---|---|---|---|
| **250** | **8** | +0.4346 | −0.0061 | 0.6565 |
| **500** | **7** | +0.4489 | — | — |
| **750** | **7** | +0.4388 | — | — |

**The disagreement is one name — `NVDA`**, exactly as in RUN-1 and on 08-10:
- 250d → `U0 = {AVGO, TSM}` · `U5 = {NVDA}` (**separate**)
- 500d · 750d → `U0 = {AVGO, NVDA, TSM}` (**merged**)

Six units identical across all three windows: `{KMI,LNG}` · `{009150}` · `{096770}` · `{MA}` · `{RTX}` ·
`{VST}`. Threshold sweep at 250d shows the choice sits on a boundary (`dist 0.75` collapses 8→7;
`dist 0.55–0.60` expands to 9; `dist 0.40–0.50` gives 10). Max residual correlation **+0.4935**.

**🚫 Rights revoked (unchanged)**
1. No single-number concentration guard (SIZE · BET).
2. Any concentration statement carries its `--days` **on the same line**.
3. Whether `AVGO/NVDA/TSM` is **one unit or two is decided by the window** — neither may be asserted.
   ⚠ This matters more than usual today: **NVDA earnings 08-26** is the un-bracketed binary RUN-1
   handed forward, and whether that print hits one unit or two is exactly what this gate cannot say.

---

## G5 · Does the universe cover the book — 🔴 FAIL, **with a route-specific repair**

| Item | Value |
|---|---|
| Book positions | **10** (US 8 · KR 2) — 009150 · 096770 · AVGO · KMI · LNG · MA · NVDA · RTX · TSM · VST |
| US holdings **outside** `us_top300.csv` | **2 🚨 `LNG` · `TSM`** — **13th consecutive run** |
| `us_top300.csv` | **300 rows**, mtime **2026-07-15 18:04** = **28 days** old (limit ≤8) 🔴 |
| Book equity | KRW **13,097,977** total · cash KRW **3,559,022** · USD cash **0** |

**★ The new fact, and it is the useful one:** the revocation RUN-1 wrote ("no flow / RS / OBV verdict on
LNG or TSM") is a property of **the sweep's universe file**, not of the instruments. A **direct**
`module_flow` call takes tickers, not a universe, and both names answered:

| Name | flow | vel | OBV | RS20 | RS60 | vol surge |
|---|---|---|---|---|---|---|
| `LNG` | 🔴 distributing | 1.18× | **distribution** | −2.3% | **+7.1%** | 0.88× |
| `TSM` | 🔴 distributing | 0.87× | **distribution** | −2.1% | −2.0% | 0.75× |

**Rights**
1. ✅ **RUN-2 may state flow / OBV / RS for LNG and TSM**, with the warrant named as **"direct
   `module_flow` call, 4-axis, 2026-08-12 22:4x KST"** — never as a sweep output, because they are
   still absent from the sweep and always will be until the universe file is rewired.
2. ⛔ They may **not** be ranked inside any sector table built from the sweep — different denominator.
3. ⛔ `wflow` may not be called "current market cap": the weights are **28 days** old.
4. The wiring gap is unchanged and now **13 runs old**: `us_all_v2_candidate.csv` (1,522 names, built
   08-10) contains both names; `sector_flow --market us` does not read it. Naming it is this stage's
   job; rewiring is not (rule 1).

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL (unchanged)

| Item | Value |
|---|---|
| Accrued | **8 files / 22 calendar days** (2026-07-22 → 2026-08-12), 120 names each |
| Measured rate | **0.36 files/day** (ideal 1.0) |
| ETA to 40-day target | ideal **32 days** · measured **≈88 days** = **2.75×** (limit 1.5×) |
| Gaps (days) | [2, 3, 4, 6, 3, 1, 2] · median **3** · max **6** |

The tool prints its own trap warning (D16): *counted as "number of files" this instrument looks
healthy.* Today's file did accrue; the **rate** is the failure. Not retroactively recoverable.

**🚫 Rights revoked (unchanged):** `kelly_size --ic` output may not be reported as a grounded size; any
size written today is labeled **"mechanical 1/4"**.

---

## G7 · Tool liveness — 🟡 FAIL on 1 of 38, probed back

**38 entry points checked with `--help`; 37 exit 0.**
Scripts (24): `sector_flow` · `us_live_shortlist` · `us_flow` · `flow_read` · `cycle_exposure` ·
`catalyst_calendar` · `drift_watch` · `action_bracket` · `exposure_rule` · `risk_units` · `kelly_size` ·
`report_lint` · `missed_ledger` · `reject_ledger` · `us_setup_screener` · `axis_window_flow` ·
`axis_inflection` · `snapshot_estimates` · `ic_ledger` · `measure_ic` · `brief_recall` ·
`handoff_compact` · `leak_scan` · `handoff_id_audit`
Modules (13): `module_macro_us` · `module_news_data` · `module_paper_book` · `module_watchlist` ·
`module_report_tags` · `module_business_us` · `module_disclosure_us` · `module_fundamentals_us` ·
`module_valuation` · `module_flow` · `module_industry_map` · `module_epistemics` · `module_inflection`

| exit 1 | Why | Functional probe (rule 3 — measure, don't manufacture UNKNOWN) |
|---|---|---|
| `module_chart` | CLI implements no `--help`; prints usage then exits 1 | `module_chart NVDA --read` -> **exit 0, clean**: OBV accumulating (20d slope **+67%**), no divergence, MA mixed / price above 3 of 4, Bollinger expanding 17.6% at midline, RSI **54.3**, momentum20d **+2.4%**, turn verdict **PULLBACK-TO-SUPPORT**, trigger `close>219.44`, stop `190.01` |

**Rights**: `module_chart` citation right **retained via the probe**, warrant = the probe, and **only for
the `<ticker> --read` form**. ⚠ G7 PASS never launders a data-path failure — that was RUN-1's G1 lesson
and it survives the recovery.

---

## What this table binds in RUN-2 (handed to HANDOVER)

**Restored, stated positively.** RUN-2 may speak with **news velocity and theme freshness from its own
direct calls**, **FRED macro** (`module_macro_us`), **FINRA/CFTC positioning**, **primary filings and
fundamentals**, **chart structure via the probed `--read` form**, **3-axis flow levels and the
08-07→08-11 Δ from RUN-1's snapshot (labeled as such)**, and — newly — **direct 4-axis flow reads on
`LNG` and `TSM`.**

**Still forbidden.** Mixing 3-axis sweep scores with 4-axis direct reads in one comparison · quoting
`vel_coverage 11.3%` as RUN-2's · promoting or demoting Financials/Industrials/Materials on `wflow` ·
single-number concentration · `--ic`-grounded size · calling the 28-day-old cap column "current" ·
any Δ against an 08-12 bar that has not settled.

*Instrument state is not a market view — not written into `handoff/` (HANDOVER only reads it).*

---

## §CLOCK-CORRECTION — appended at 22:25 KST (D48 applied to this stage's own output)

⚠ **The RUN-2 header above says *"the US cash session for 08-12 **opened at 22:30 KST, mid-way through
this stage**."* That was written forward-looking and it is WRONG as a statement of fact. It is left
visible and corrected here rather than rewritten.**

Measured, not assumed (`datetime` + `zoneinfo`, run at the time of writing):

| Item | Value |
|---|---|
| Clock at correction | **2026-08-12 22:23:25 KST = 2026-08-12 09:23:25 ET** |
| US cash open | **09:30 ET** ⇒ **NOT YET OPEN — 7 minutes away** |
| July CPI release | **08:30 ET** ⇒ **fired 53 minutes ago** |

⇒ **RUN-2's true position is POST-PRINT, PRE-OPEN.** Not "mid-session". This is not a cosmetic fix:
every settlement statement in this run depends on it, and the corrected clock is what makes
§HANDOVER's central finding (*the binary fired and no settled instrument covers it*) exact rather
than approximate.

**Provider state at 09:23 ET, measured on three routes (this is the evidence for that finding):**

| Route | Latest data | Covers 08-12? |
|---|---|---|
| `[FRED]` `module_macro_us` | CPI index **332.568 @ 2026-06-01**; daily H.15 through **08-10** | ❌ **No** |
| news `--scope foreign` | pool answers, but every CPI article is **pre-print** ("ahead of", "due", "futures rise before") | ❌ **No** |
| `yfinance` daily | last bar **2026-08-11** | ❌ **No** |
| `yfinance` 5-minute | last bar **2026-08-11 15:55 ET** — **no 08-12 rows at all** | ❌ **No** |

**Rights consequence:** ⛔ **No stage in RUN-2 may report any 08-12 price, excess, or settle.**
The 08-12 bar does not exist on any route this desk owns. Where a scenario settles on it, the correct
entry is **"binary fired, observable not yet settled"** — never a provisional number promoted to a score.
