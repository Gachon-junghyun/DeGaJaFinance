# PREFLIGHT — 2026-08-21 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-21 22:09–22:26 = ET 2026-08-21 09:09–09:26, FRIDAY — US cash PRE-MARKET**
> (bell 09:30 ET = 22:30 KST). Terminal settled bar **2026-08-20 (Thursday close)**; sweep `asof`
> **2026-08-20**. Sweep was run fresh at **22:10–22:12 KST today** (no artifact reuse, unlike 08-20).

★ **Three things measured today.**

**① The news pipe is ALIVE at run time — and the sweep's news axis died anyway.** This is the cleanest
separation of the two facts this desk has recorded. At 22:09 KST, before the sweep, the CLI returned
`fts search Nvidia --days 7 --count --scope foreign` = **3523**. The sweep launched one minute later
and measured velocity on **50 of 299 names (16.72%)**, tripping its own 🚨 line. At 22:20 the same CLI
returned **3523 · 3523 · 3523** on three consecutive calls. ⇒ **The tunnel is up; the sweep's per-name
loop still only lands ~1 call in 6.** The failure is not "server down" — the server answered every
hand-issued call in this window. It is throughput/concurrency inside the sweep's own velocity loop.

**② The falsification probe is again unambiguous, and its cumulative record is now perfect over seven
runs.** The **first 40 names the sweep marked silent** came back **40 / 40 valid in 18.8 s** when
re-asked by hand through the identical `news_velocity()` entry point — including `COIN` (recent **234**
/ base **836**), `ABNB` (57/296), `COP` (46/219). Cumulative false-silence count across seven runs of
this probe: **0 of 280.** The sweep has never once been right that a US large cap had no news.

**③ The survivor count moved off its three-run plateau — and the shape says the same thing anyway.**
Runs 08-18/08-19/08-20 returned 51 / 49 / 50 survivors. Today: **50 survivors of 299**, but sitting at
indices **1 – 289** in **41 distinct success runs, longest 3, 33 singletons** — statistically identical
in *shape* to yesterday (40 runs, longest 4, 33 singletons). ⇒ **The membership is arbitrary and stable
in its arbitrariness; the count is quota-shaped.** A number that is invariant to whether the tunnel is
up (today) or down (this morning's KR run, also ~50) cannot be read as a measurement of news.

⚠ **Filename deviation, logged (12th consecutive run, same reason):** the composition table names this
`preflight/PREFLIGHT.md`, but the `industry_kr` desk wrote its rights table to that path this morning
(08:17–08:25 KST). Overwriting a sibling desk's output is not a correction, so the US table is written
as `PREFLIGHT_US.md` in the same folder — documented practice 08-10 through 08-20. Human decision on
permanent market-suffixing still pending (PROMPT_MAP §6).

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** *(3rd consecutive US pass)* | Terminal bar **2026-08-20** · Close **300/301** on each of the last three rows (08-18 · 08-19 · 08-20) · last-bar volume / prior-20d median **0.935** (q25 0.775 · q75 1.201, n=300) · `SPY` closes present through **08-20 762.60** ⇒ names and benchmark share one terminal date, **no RS-leg misalignment**. The one missing name in every column is `EA` (see G5) |
| **G1** news axis alive | 🔴 **FAIL** *(9th consecutive run)* | Sweep coverage **16.72% (50/299)**, `vel_axis=false`, `n_axes=3`, `dropped_missing_axis=0`. Falsification: the **first 40 silent names → 40/40 valid in 18.8 s**; CLI `fts search Nvidia --days 7 --count --scope foreign` → **3523 · 3523 · 3523**, and **3523 before the sweep too**. Cumulative **0 of 280** false-silences over seven runs |
| **G2** scoring-scale continuity | 🟢 **PASS** | **3-axis (`nonews`) vs 3-axis (`nonews`)** — prior history snapshot `2026-08-19._mode = nonews`. Subtraction is legal, and the Δ spans exactly **ONE session (08-19 → 08-20)**: 294/299 scores moved, median abs-Δ **0.067**, max **0.873** |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **1 of 11**: Communication Services / `GOOGL` **38.3%** (wflow **+0.090** → ex-top1 **−0.010**). Yesterday's flipper (Materials/`LIN`) has left the set; `LIN` today is +0.008 → +0.149, same sign |
| **G4** risk-unit stability | 🔴 **FAIL** *(12th consecutive run, identical numbers)* | 250d **11 units** · 500d **10** · 750d **10** — 500 and 750 agree name-for-name, **250 does not** |
| **G5** does the universe cover the book | 🔴 **FAIL** *(staleness + one hole)* | **11/11 US holdings inside `us_top300` AND scored ✅**. But `us_top300.csv` is **37 days old** (limit ≤8), and **`EA`** is still absent from the sweep (299 of 300) — **9th** consecutive run unmeasurable |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** *(but the daemon fired today, 3rd straight day)* | 13 files / **31 calendar days** = **0.42/day** ⇒ measured ETA **≈64 days** to the 40-day target vs ideal 27 = **2.4×** (limit 1.5×). ★ Last save = **today, 2026-08-21** |
| **G7** tool liveness | 🔴 **FAIL** *(12th consecutive, same two)* | **39 entry points** probed, **2** non-zero `--help`: `module_chart` · `scripts/margin_history.py`. Both pass a functional probe ⇒ citation retained **for those command lines only** |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate and it passed).
**Instrument state equals the 08-20 reading — the best this desk has recorded — with one genuinely new
datum: the news tunnel was verifiably UP while the sweep axis died anyway.** All five failures are
long-standing; none is new.

Today this desk **cannot** speak with the sweep's news-velocity axis, the 50 survivors as a set, theme
freshness, "it went quiet", `breadth` as a news-informed reading, a single concentration number, an
`--ic`-derived size, the Communication Services `wflow` sign, or `EA`. It **can** speak with settled
prices through the **2026-08-20** close, a **one-session Δ**, RS, OBV, `eqflow`, `vol_surge`, the full
`module_chart --read` panel, FINRA short pressure, CFTC COT positioning, FRED series, primary filings,
and **hand-probed per-name news velocity, which measured 40/40 at 22:18 KST.**

---

## G0 · Bar completeness · date alignment — 🟢 **PASS**

Not one of the seven. Carried because the KR desk measured it into existence on 08-12.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-21.pkl`
(85 rows × 1806 columns = 301 tickers × 6 fields) + `SECTOR_FLOW_US.json §scoring`.

### (a) The three most recent rows, field by field — **[measured]**

| Field | 2026-08-18 | 2026-08-19 | **2026-08-20 (terminal)** |
|---|---|---|---|
| Open | 300 / 301 | 300 / 301 | **300 / 301** |
| High | 300 / 301 | 300 / 301 | **300 / 301** |
| Low | 300 / 301 | 300 / 301 | **300 / 301** |
| Close | 300 / 301 | 300 / 301 | **300 / 301** |
| Volume | 300 / 301 | 300 / 301 | **300 / 301** |

The single missing name in every cell is `EA` — a separate, older hole (G5), not a bar defect.

★ **The "three-quarters bar" defect class (full volume, NaN close, invisible to volume heuristics) has
now been absent for three consecutive runs.** It is not retired as a *class*: the only test that ever
caught it — **non-null close count** — remains this gate's primary test, permanently, regardless of
clean readings.

### (b) Completeness of the terminal bar — **[measured]**

| Test | Reading on the 08-20 row | Conclusion |
|---|---|---|
| Row present in frame? | yes, index ends **2026-08-20** | Thursday is here |
| **Non-null closes on the last row** | **300 / 301** | primary test fires clean |
| Last-bar volume / prior-20d median | **median 0.935** · q25 **0.775** · q75 **1.201** (n=300) | settled full session (a live partial bar reads far below this at pre-market) |
| Benchmark alignment | `SPY` closes **08-14 776.34 · 08-17 772.67 · 08-18 767.45 · 08-19 769.06 · 08-20 762.60** | names and bench end on the **same date** |

The last item is the KR desk's standing failure mode (names one session ahead of `^KS11`, RS legs
misaligned — its G0 failed again this morning, 3rd straight). **It does not occur here.**

### (c) Sessions gained — **[measured]**

Prior usable snapshot **2026-08-19**; today's **2026-08-20** ⇒
**`n_new_sessions_since_prior_run = 1`.** Written by hand, because nothing writes it automatically
(D280). Three consecutive runs now advance one clean session each.

**✅ Rights retained today**: settled prices, closes, returns, RS, OBV, `vol_surge` through the
**2026-08-20** close · the full `module_chart --read` panel · benchmark-relative statistics.

**🚫 Rights revoked today**
1. **No 08-21 price of any kind.** The US cash session for 08-21 opens at 22:30 KST, after this table.
   The desk has Thursday, not Friday.
2. **No stage may re-pull prices after 22:30 KST and treat the result as comparable to the sweep** —
   after the bell the feed hands back a live partial bar. If a stage needs an intraday quote it must
   label it intraday and must not mix it into any 08-20-based statistic.

---

## G1 · News axis alive — 🔴 **FAIL** (9th consecutive run)

**Command** `SECTOR_FLOW_US.json §scoring` + falsification probe
(`module_flow._news_velocity.news_velocity(name, 7, 28, kr=False)` on the silent set;
`python -X utf8 -m module_news_data fts search Nvidia --days 7 --count --scope foreign`).

### (a) What the instrument reports about itself — **[measured]**

```
"scoring": {"vel_axis": false, "vel_coverage": 0.1672, "n_axes": 3,
            "scored": 299, "dropped_missing_axis": 0}
```

The sweep's own 🚨 line fired verbatim: *the news axis died in this run (measured 16.7%) — "there is no
article" is probably really "it could not be counted."* `dropped_missing_axis = 0` confirms the D225
fix is holding — **all 299 names were scored on the same 3 axes**, so no name received the +0.305
phantom bonus that the 2026-08-09 defect produced. The scale is wrong-but-uniform, which is what makes
G2 legal.

### (b) The falsification probe — is it silence, or is it the pipe? — **[measured]**

The 40 names at the head of the silent set, re-asked by hand through the same function the sweep calls:

**40 valid / 40 asked, in 18.8 seconds.** Not one returned "no articles."

| Ticker | Name | recent(7d) | base(28d) | velocity |
|---|---|---|---|---|
| MSTR | MicroStrategy | 27 | 88 | 1.23 |
| TGT | Target Corporation | 28 | 45 | **2.49** |
| MSI | Motorola Solutions | 3 | 72 | 0.17 |
| PSX | Phillips 66 | 38 | 130 | 1.17 |
| MPC | Marathon Petroleum | 29 | 116 | 1.00 |
| TRI | Thomson Reuters | 32 | 114 | 1.12 |
| DASH | DoorDash | 47 | 200 | 0.94 |
| ABNB | Airbnb | 57 | 296 | 0.77 |
| COIN | Coinbase | **234** | **836** | 1.12 |
| CVNA | Carvana | 31 | 101 | 1.23 |
| KKR | KKR & Co. | 17 | 74 | 0.92 |
| COP | ConocoPhillips | 46 | 219 | 0.84 |

(full 40 in `llm_outputs/2026-08-21/industry_US/_silent_names.json`)

**Cumulative record of this probe: 0 false silences in 280 hand-checks over seven runs.**

### (c) The new datum — the tunnel was UP the whole time — **[measured]**

| Clock (KST) | Probe | Result |
|---|---|---|
| 22:09 | `fts search Nvidia --days 7 --count --scope foreign` | **3523** |
| 22:10–22:12 | sweep's own velocity loop, 299 names | **50 answered (16.72%)** |
| 22:18 | 40 silent names, hand-issued | **40 / 40 in 18.8 s** |
| 22:20 | same CLI ×3 | **3523 · 3523 · 3523** |

This morning's KR run recorded the opposite condition — a genuine **TLS outage** (`curl` exit 35,
http_code 000) with the local fallback DBs at 0 bytes — and its coverage was **6.05% (50/806)**.
**Same ~50 answered names under a dead tunnel and under a live one.** ⇒ the survivor count is not a
function of news availability *or* of server health. It is a property of the sweep's own loop.

### (d) Shape of the survivors — **[measured]**

| Run | Survivors | Index span | Distinct runs | Longest run | Singletons |
|---|---|---|---|---|---|
| 08-19 (US) | 51 | 16 – 295 | 44 | 3 | 40 |
| 08-20 (US) | 49 | 0 – 297 | 40 | 4 | 33 |
| **08-21 (US)** | **50** | **1 – 289** | **41** | **3** | **33** |

Scattered singletons across the whole universe, never a contiguous prefix. **Not a quota exhausted at
call N; a ~1-in-6 success rate spread over the whole loop.**

**🚫 Rights revoked today (every stage, no exceptions)**
1. **No stage may cite news velocity, theme freshness, or news acceleration from `SECTOR_FLOW_US.json`.**
   The axis is `false` and the field is `null` for 249 of 299 names.
2. **No stage may write "it went quiet", "no news flow", "the narrative faded", or any absence-claim
   sourced from the sweep.** Measured 0-for-280: this instrument's silence has never once been real.
3. **`breadth`, `green`, `red` counts remain citable** (they derive from the 3 surviving axes) **but may
   not be described as news-informed.**
4. **The 50 survivors may not be used as a set** — not as a shortlist, not as a "names with live news"
   group, not as a ranking input. Membership is arbitrary (41 disjoint runs, 33 of them singletons).
5. ✅ **Per-name news velocity IS citable when hand-probed** and labelled as such with its clock time.
   That path measured 40/40 today and 3523 three times.

---

## G2 · Scoring-scale continuity — 🟢 **PASS**

**Command** `SECTOR_FLOW_US.json §scoring.n_axes` vs `llm_outputs/sector_flow/history.json` prior
snapshot `_mode`.

| Snapshot | `_mode` | axes | names |
|---|---|---|---|
| 2026-08-14 | `nonews` | 3 | 299 |
| 2026-08-18 | `nonews` | 3 | 299 |
| 2026-08-19 (**prior run**) | `nonews` | 3 | 299 |
| **2026-08-20 (this run)** | **`nonews`** | **3** | **299** |

Both sides of every `delta` field are 3-axis. **Subtraction is legal today.**

★ **And the Δ baseline is one clean session for the third consecutive run** (08-19 → 08-20):
**294 of 299** scores moved, median abs-Δ **0.067**, max **0.873**. Compare 08-20's reading (295 moved,
median 0.095, max 0.943) — today's tape moved slightly less. The six-run price freeze of 08-13 → 08-18
remains fully behind this desk.

⚠ **Standing caveat, unchanged**: `nonews`-mode scores are *comparable to each other* but are **not**
on the same scale as any 4-axis snapshot before 08-13. Cross-mode subtraction stays forbidden.

**✅ Rights retained**: `delta` fields, new-🟢 ignition calls, Δflow ranking — **all on a one-session
basis**, which must be stated on the same line.

---

## G3 · Who owns the sector sign — 🟢 **PASS**

**Command** `SECTOR_FLOW_US.json §sector_rotation[].top1_flips_sign` — **printed in full, all 11**.

| Sector | n | wflow | ex-top1 | top1 | top1 weight | **flips?** |
|---|---|---|---|---|---|---|
| Energy | 16 | +0.169 | +0.235 | XOM | 30.5% | no |
| Health Care | 32 | +0.150 | +0.152 | LLY | 19.4% | no |
| **Communication Services** | 12 | **+0.090** | **−0.010** | **GOOGL** | **38.3%** | **🚨 YES** |
| Consumer Staples | 19 | +0.050 | +0.135 | WMT | 28.9% | no |
| Consumer Discretionary | 28 | +0.010 | +0.075 | AMZN | 40.2% | no |
| Materials | 12 | +0.008 | +0.149 | LIN | 24.7% | no |
| Financials | 47 | −0.020 | −0.031 | BRK-B | 13.9% | no |
| Industrials | 50 | −0.247 | −0.197 | CAT | 8.7% | no |
| Information Technology | 56 | −0.279 | −0.298 | NVDA | 19.4% | no |
| Real Estate | 12 | −0.335 | −0.240 | WELL | 16.9% | no |
| Utilities | 15 | −0.647 | −0.648 | NEE | 17.7% | no |

**Flipper count: 1 of 11.** Yesterday's flipper (Materials / `LIN`) has left the set — `LIN` today
keeps the sign (+0.008 → +0.149). Today's is **Communication Services**, where `GOOGL` alone carries
38.3% of the sector weight and is the entire reason the sector prints positive.

**🚫 Rights revoked today**
- **Communication Services may not be promoted or demoted on its `wflow` sign.** The sector is one
  company. ROTATION §2 must use `eqflow` (**+0.151**) or `breadth` (**0.00 — zero green of 12**) for
  it, or hold it. Note those two disagree with each other as well; that disagreement is the finding.
- ✅ The other **10 sectors' `wflow` signs are owner-verified** and may be cited as sector-level facts.

---

## G4 · Risk-unit stability — 🔴 **FAIL** (12th consecutive run)

**Command** `python -X utf8 scripts/risk_units.py --book --days {250,500,750}` — **all three actually
run**, 22:13–22:16 KST.

| Window | Units | Grouping |
|---|---|---|
| **250d** | **11** | `U0: 028050 + 316140` merged (a KR E&C name with a KR bank holding); **AI-compute split three ways** — ANET / AVGO / NVDA each alone; ETN alone |
| **500d** | **10** | `U0: ANET + ETN` · `U1: AVGO + NVDA` · `U2: MPC + PSX` · 028050 and 316140 **separate** |
| **750d** | **10** | **identical to 500d, name for name** |

500d and 750d agree exactly. **250d does not** — and it disagrees in the way that matters most: it
splits the three AI-compute names into three units while merging two unrelated Korean names into one.
Threshold sweeps: 250d selects dist 0.65 → 11 units (intra +0.6045); 500d dist 0.65 → 10 (+0.5243);
750d dist 0.65 → 10 (+0.5150).

**🚫 Rights revoked today**
1. **No concentration guard may be quoted as a single number.** "AI-compute is N% of the book" is
   window-dependent: at 250d it is three units, at 500/750d it is two (ANET travels with ETN, AVGO with
   NVDA).
2. **Any stage citing a risk-unit count must print `--days` on the same line as the conclusion.**
3. ✅ **`MPC + PSX` is one unit in all three windows** and may be treated as a single risk unit without
   a window caveat — the only grouping in the book that is window-invariant.

---

## G5 · Does the universe cover the book — 🔴 **FAIL** (staleness + one hole)

**Command** `data/us_universe/us_top300.csv` (300 rows) × `module_paper_book status` holdings ×
`SECTOR_FLOW_US.json §names`.

### (a) Coverage leg — **PASS** — **[measured]**

**11 / 11 US holdings are inside `us_top300` and carry a score in today's sweep:**

| Ticker | tag | flow_score | Ticker | tag | flow_score |
|---|---|---|---|---|---|
| ANET | 🟡중립 | +0.033 | NDAQ | 🟡중립 | −0.021 |
| AVGO | 🟡중립 | −0.397 | NUE | 🟡중립 | +0.224 |
| ETN | 🟡중립 | −0.075 | NVDA | 🟡중립 | −0.199 |
| HPE | 🟡중립 | +0.487 | PSX | 🟡중립 | +0.733 |
| MET | 🟡중립 | −0.175 | RTX | 🟡중립 | +0.182 |
| MPC | 🟡중립 | +0.700 | | | |

★ Note for downstream: **all 11 are 🟡 — not one green, not one red.** The two KR holdings
(`028050`, `316140`) are out of scope for the US universe by construction, not a hole.

### (b) Staleness leg — **FAIL** — **[measured]**

`us_top300.csv` mtime **2026-07-15** ⇒ **37 days old**, limit ≤8. The sweep logs its own warning
(universe 37 days elapsed, market caps stale).

### (c) The `EA` hole — **FAIL** — **[measured]**

`EA` is row-present in `us_top300.csv` but **absent from the sweep's 299 scored names and NaN in every
price column of the frame** — 9th consecutive run. Cause unchanged and undiagnosed at this stage
(diagnosis is `idle_probe`'s job, not this stage's).

**🚫 Rights revoked today**
1. **No flow / RS / OBV / short judgment on `EA`.** It is not *quiet*; it is **unmeasured**. Any stage
   that reaches for it writes "unmeasurable, 9th run" — never "no signal."
2. **Market-cap ranks and sector labels from `us_top300` are 37 days stale.** Sector *membership* is
   citable (GICS does not churn in 5 weeks); **rank ordering and cap weights are not** — and `wflow` is
   cap-weighted, so `wflow` inherits a 37-day-old weighting. State this wherever `wflow` decides a call.
3. ✅ The **11 book names are fully measurable today** — no per-name caveat needed for them.

---

## G6 · Estimate-snapshot accrual — 🔴 **FAIL** (2.4× slow — but the daemon fired today)

**Command** `python -X utf8 scripts/snapshot_estimates.py --status`.

| Quantity | Reading |
|---|---|
| Files accrued | **13** (120 tickers each, ~148 KB) |
| Calendar span | **31 days** (2026-07-22 → 2026-08-21) |
| Measured rate | **0.42 / day** (ideal 1.00) |
| Remaining to the 40-day target | **27 more** ⇒ ideal 27 days, **measured ≈64 days** |
| Ratio to ideal | **2.4×** (limit 1.5×) |
| Gap distribution (days) | `[3, 1, 2, 1, 1, 5, 1, 1]` · median 2 · max 6 |
| **Last save** | **2026-08-21 — today.** Third consecutive day (08-19, 08-20, 08-21) |

★ **This is the D16 trap by construction**: counting *files* (13) reads as healthy; counting *days*
(31) is what makes it 2.4× slow. The status tool now prints both, which is why this is catchable.
The recent run of three consecutive daily saves is the best stretch in the ledger, but three days do
not move a 31-day rate.

**🚫 Rights revoked today**
1. **`kelly_size --ic` output may not be presented as an evidence-backed size.** Any stage using it
   labels it **"mechanical ¼-Kelly, IC unmeasured"** on the same line.
2. **No stage may claim an IC-informed edge for any axis.** With n_eff < 4 the `ic_ledger` rule is
   explicit: **no verdict.**
3. ⚠ **Retroactive recovery is impossible.** Days not accrued are gone; the ETA cannot be caught up by
   working harder later.

---

## G7 · Tool liveness — 🔴 **FAIL** (12th consecutive, same two)

**Command** `--help` on every entry point this run will touch — **39 probed**, exit code recorded.

**37 of 39 returned exit 0.** The two failures, unchanged since 08-10:

| Entry point | `--help` exit | Functional probe | Verdict |
|---|---|---|---|
| `python -m module_chart` | **1** | `module_chart NVDA --read` → full CHART_READ panel (OBV 분배 −103% · MA 강세스택 · RSI 67.4 · turn NEUTRAL/CHOP · trigger 220.86 / stop 190.01) | **argparse defect only** |
| `python scripts/margin_history.py` | **1** | `margin_history.py NVDA` → SEC XBRL **FY2008–FY2026, 19 years**, no gaps | **argparse defect only** |

Both are the known argparse `%`-format bug in the help string, not a runtime failure.

**🚫 Rights revoked today**
1. **Neither tool's `--help` may be cited as documentation of its interface.** Argument names must be
   read from source, not from help output.
2. ✅ **Citation is RETAINED for the two command lines proved above** — `module_chart <TICKER> --read`
   and `scripts/margin_history.py <TICKER>` — and **only** those. Any *other* flag combination on
   either tool is unprobed and may not be assumed to work.
3. ✅ All other **37 entry points** are cleared for use, including the ones this run depends on:
   `module_macro_us` · `module_news_data` · `module_flow` · `module_fundamentals_us` ·
   `module_business_us` · `module_disclosure_us` · `scripts/sector_flow.py` ·
   `scripts/us_live_shortlist.py` · `scripts/us_flow.py` · `scripts/cycle_exposure.py` ·
   `scripts/catalyst_calendar.py` · `scripts/drift_watch.py` · `scripts/risk_units.py` ·
   `scripts/kelly_size.py` · `scripts/report_lint.py`.

---

## Consolidated rights table — what this run may and may not say

**🚫 FORBIDDEN today**

| # | Claim class | Source gate |
|---|---|---|
| 1 | News velocity / theme freshness / acceleration **from the sweep** | G1 |
| 2 | Any absence-claim ("quiet", "narrative faded", "no flow") sourced from the sweep | G1 |
| 3 | The 50 velocity survivors **as a set** | G1 |
| 4 | Communication Services promoted/demoted on its `wflow` sign (GOOGL = 38.3%) | G3 |
| 5 | Any concentration figure as a single window-free number | G4 |
| 6 | `wflow` cap-weights or `us_top300` rank order treated as current (37 days stale) | G5 |
| 7 | Any flow/RS/OBV/short judgment on **`EA`** | G5 |
| 8 | `kelly_size --ic` as an evidence-backed size; any IC-informed edge claim | G6 |
| 9 | `module_chart` / `margin_history` **`--help`** as interface documentation | G7 |
| 10 | Any **2026-08-21** price, or post-22:30-KST intraday quotes mixed into 08-20 statistics | G0 |

**✅ PERMITTED today**

| # | Claim class | Source gate |
|---|---|---|
| 1 | Settled prices / returns / RS / OBV / `vol_surge` through the **2026-08-20** close | G0 |
| 2 | `delta` / Δflow / new-🟢 ignitions — **on a one-session (08-19→08-20) basis, stated** | G0 · G2 |
| 3 | `wflow` **signs** for the 10 non-flipper sectors; `eqflow` and `breadth` for all 11 | G3 |
| 4 | `MPC + PSX` as one risk unit, window-invariant | G4 |
| 5 | Full flow/RS/OBV panel on all **11 US book names** | G5 |
| 6 | `module_chart <T> --read` and `margin_history <T>` outputs | G7 |
| 7 | **Hand-probed** per-name news velocity, labelled with its clock time | G1(c) |
| 8 | FRED series, FINRA short pressure, CFTC COT positioning, SEC primary filings | G7 |

---

## Run log

- Sweep run **fresh today at 22:10–22:12 KST** (301 tickers, 4mo, yfinance batch) — no artifact reuse.
- Output filename `PREFLIGHT_US.md` (not `PREFLIGHT.md`) — sibling KR desk owns that path today. 12th
  consecutive run; human decision pending (PROMPT_MAP §6).
- Nothing in this stage is written to `handoff/` — instrument state is not a market view.
- No failed lookups in this stage. Every command listed returned.
