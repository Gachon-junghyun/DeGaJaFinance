# PREFLIGHT — 2026-08-20 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-20 22:10–22:30 = ET 2026-08-20 09:10–09:30, THURSDAY — US cash PRE-MARKET**
> (bell 09:30 ET = 22:30 KST). Terminal settled bar **2026-08-19 (Wednesday close)**; sweep `asof`
> **2026-08-19**.
>
> ★ **Three things measured today.**
>
> ① **G0 passes for the second consecutive run, and the Δ baseline is finally one session.** Yesterday's
> table had to stamp every `delta` field "TWO-session (08-14 → 08-18)". Today the prior history snapshot
> is **2026-08-18** and the current is **2026-08-19** ⇒ **`n_new_sessions_since_prior_run = 1`.** The
> six-run price freeze that ran 08-13 → 08-18 is fully behind this desk; the feed has now advanced on
> two consecutive days.
>
> ② **G1 fails for the 8th consecutive run, and the shape reproduces yesterday's US shape, not KR's.**
> Sweep coverage **16.39% (49/299)**. Survivors sit at indices **0 – 297**, **40 distinct success runs,
> longest 4, 33 singletons**. Yesterday's US run: 51 survivors, 44 runs, longest 3, 40 singletons,
> indices 16–295. This morning's KR run: 50 survivors scattered 45–775 (KR itself retracted its
> "contiguous prefix" finding today). ⇒ **The count is quota-shaped (~50/sweep) and stable across three
> consecutive measurements on two markets; the membership is arbitrary and stable in its arbitrariness.**
>
> ③ **The falsification probe is unambiguous: it is the pipe, not silence.** The same 40 names the sweep
> returned `None` for came back **40 / 40 valid in 18.4 s** when re-asked by hand, and the CLI returned
> `3651` three times for `Nvidia --days 7 --count --scope foreign`. Cumulative false-silence count
> across six runs of this probe: **0 of 240**. The sweep has never once been right that a US large cap
> had no news.
>
> ⚠ **Sweep artifact reused, logged.** `SECTOR_FLOW_US.json` in this run folder was written at
> **07:22 KST today** (2 h after the 08-19 US close), and its terminal bar is **08-19** — the newest
> settled US bar in existence at preflight time. Re-running the sweep now would download the same
> terminal bar and re-roll only the broken news axis. The artifact is measured as-is and SWEEP inherits
> it. Stated so no downstream stage reads a 22:10 timestamp into it.
>
> ⚠ **Filename deviation, logged (11th consecutive run, same reason):** the composition table names this
> `preflight/PREFLIGHT.md`, but the `industry_kr` desk wrote its rights table to that path this morning
> (08:17–08:26 KST). Overwriting a sibling desk's output is not a correction, so the US table is written
> as `PREFLIGHT_US.md` in the same folder — documented practice on 08-10 through 08-19. Human decision
> on permanent market-suffixing still pending (PROMPT_MAP §6).

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** *(2nd consecutive US pass)* | Terminal bar **2026-08-19** · Close **300/301** on each of the last three rows (08-17 · 08-18 · 08-19) · last-bar volume / prior-20d median **0.879** (q25 0.757 · q75 1.089, n=300) · `SPY` closes present through **08-19 769.06** ⇒ names and benchmark share one terminal date, **no RS-leg misalignment**. The one missing name in every column is `EA` (see G5) |
| **G1** news axis alive | 🔴 **FAIL** *(8th consecutive run)* | Sweep coverage **16.39% (49/299)**, `vel_axis=false`, `n_axes=3`. Falsification: the **same 40 silent names → 40/40 valid in 18.4 s**; CLI `fts search Nvidia --days 7 --count --scope foreign` → **3651 · 3651 · 3651**. Cumulative **0 of 240** false-silences over six runs |
| **G2** scoring-scale continuity | 🟢 **PASS** | **3-axis (`nonews`) vs 3-axis (`nonews`)** — prior history snapshot `2026-08-18._mode = nonews`. Subtraction is legal. ★ **And for the first time since 08-12 the Δ spans exactly ONE session (08-18 → 08-19)**: 295/299 scores moved, median \|Δ\| **0.095**, max **0.943** |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **1 of 11**: Materials / `LIN` **24.7%** (wflow **−0.099** → ex-top1 **+0.063**). Down from 3 yesterday (`BRK-B`, `CAT` both left the set) |
| **G4** risk-unit stability | 🔴 **FAIL** *(11th consecutive run, identical numbers)* | 250d **11 units** · 500d **10** · 750d **10** — 500 and 750 agree exactly, **250 does not** |
| **G5** does the universe cover the book | 🔴 **FAIL** *(staleness + one hole)* | **11/11 US holdings inside `us_top300` AND scored ✅**. But `us_top300.csv` is **36 days old** (limit ≤8), and **`EA`** is still absent from the sweep (299 of 300) — **8th** consecutive run unmeasurable |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** *(but the daemon fired today)* | 12 files / **30 calendar days** = **0.40/day** ⇒ measured ETA **≈70 days** to the 40-day target vs ideal 28 = **2.5×** (limit 1.5×). ★ Last save = **today, 2026-08-20**, second consecutive day |
| **G7** tool liveness | 🔴 **FAIL** *(11th consecutive, same two)* | **41 entry points** probed, **2** non-zero `--help`: `module_chart` · `scripts/margin_history.py`. Both pass a functional probe ⇒ citation retained **for those command lines only** |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate and it passed).
**Instrument state equals yesterday's — the best this desk has recorded — with one improvement: the Δ is
now a clean single session.** All five failures are long-standing; none is new.

Today this desk **cannot** speak with the sweep's news-velocity axis, the 49 survivors as a set, theme
freshness, "it went quiet", `breadth` as a news-independent reading, a single concentration number, an
`--ic`-derived size, the Materials `wflow` sign, or `EA`. It **can** speak with settled prices through
the **2026-08-19** close, a **one-session Δ**, RS, OBV, `eqflow`, `vol_surge`, the full
`module_chart --read` panel, FINRA short pressure, CFTC COT positioning, FRED series, primary filings,
and **hand-probed per-name news velocity, which measured 40/40 at 22:14 KST.**

---

## G0 · Bar completeness · date alignment — 🟢 **PASS**

Not one of the seven. Carried because the KR desk measured it into existence on 08-12.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-20.pkl`
(85 rows × 1806 columns = 301 tickers × 6 fields) + `SECTOR_FLOW_US.json §scoring`.

### (a) The three most recent rows, field by field — **[measured]**

| Field | 2026-08-17 | 2026-08-18 | **2026-08-19 (terminal)** |
|---|---|---|---|
| Open | 300 / 301 | 300 / 301 | **300 / 301** |
| High | 300 / 301 | 300 / 301 | **300 / 301** |
| Low | 300 / 301 | 300 / 301 | **300 / 301** |
| Close | 300 / 301 | 300 / 301 | **300 / 301** |
| Volume | 300 / 301 | 300 / 301 | **300 / 301** |

The single missing name in every cell is `EA` — a separate, older hole (G5), not a bar defect.

★ **The "three-quarters bar" defect class (full volume, NaN close, invisible to volume heuristics) has
now been absent for two consecutive runs.** It is not retired as a *class*: the only test that ever
caught it — **non-null close count** — remains this gate's primary test, permanently, regardless of
clean readings.

### (b) Completeness of the terminal bar — **[measured]**

| Test | Reading on the 08-19 row | Conclusion |
|---|---|---|
| Row present in frame? | yes, index ends **2026-08-19** | Wednesday is here |
| **Non-null closes on the last row** | **300 / 301** | primary test fires clean |
| Last-bar volume / prior-20d median | **median 0.879** · q25 **0.757** · q75 **1.089** (n=300) | settled full session (a live partial bar reads far below this at pre-market) |
| Benchmark alignment | `SPY` closes **08-13 777.88 · 08-14 776.34 · 08-17 772.67 · 08-18 767.45 · 08-19 769.06** | names and bench end on the **same date** |

The last item is the KR desk's standing failure mode (names 08-19, bench `^KS11` 08-18, RS legs one
session apart — its G0 failed again this morning). **It does not occur here.** The gate is checked, not
assumed.

### (c) Sessions gained — **[measured]**

Prior usable snapshot **2026-08-18**; today's **2026-08-19** ⇒
**`n_new_sessions_since_prior_run = 1`.** Written by hand, because nothing writes it automatically
(D280).

**✅ Rights retained today**: settled prices, closes, returns, RS, OBV, `vol_surge` through the
**2026-08-19** close · the full `module_chart --read` panel · benchmark-relative statistics.

**🚫 Rights revoked today**
1. **No 08-20 price of any kind.** The US cash session for 08-20 opens at 22:30 KST, after this table.
   The desk has Wednesday, not Thursday.
2. **No stage may re-pull prices after 22:30 KST and treat the result as comparable to the sweep** —
   after the bell the feed hands back a live partial bar. If a stage needs an intraday quote it must
   label it intraday and must not mix it into any 08-19-based statistic.

---

## G1 · News axis alive — 🔴 FAIL *(8th consecutive run)*

**Command**
- `SECTOR_FLOW_US.json §scoring` → `vel_axis false · vel_coverage 0.1639 · n_axes 3 · scored 299 · dropped_missing_axis 0`
- Probe A (falsification): `flow_read.news_velocity(q, 7, 30, kr=False)` over **40 names the sweep called silent**
- Probe B (CLI): `module_news_data fts search Nvidia --days 7 --count --scope foreign` ×3

### (a) The probes — **[measured]**

| Clock (KST) | Path | Calls | Valid | Reading |
|---|---|---|---|---|
| 07:20–07:22 | sweep (library) | 299 | **49** | coverage **16.39%** |
| 22:12 | CLI `fts search Nvidia --days 7 --count --scope foreign` | 3 | **3** | **3651 · 3651 · 3651** (via NEWS API tunnel) |
| 22:14 | **library, the 40 sweep-silent names, re-run** | 40 | **40** | **100% valid in 18.4 s** |

⇒ **The sweep's `None` is a pipe failure, not an absence of articles.** Cumulative across six runs of
Probe A: **0 of 240** silences survived falsification.

### (b) Survivor shape — **[measured]**

| | KR sweep 08-20 (08:18) | US sweep 08-19 (21:52) | **US sweep 08-20 (07:22)** |
|---|---|---|---|
| Survivors | **50** / 806 | **51** / 299 | **49** / 299 |
| Distinct success runs | scattered | **44** | **40** |
| Longest success run | — | **3** | **4** |
| Singleton successes | — | **40** | **33** |
| Index span of survivors | **45 – 775** | **16 – 295** | **0 – 297** |

**Stated positively and now measured three times on two markets:** the bridge grants **on the order of
50 successful calls per sweep**, and *where* those calls land is **arbitrary**. The count is the
reliable part; the membership is not — and it is arbitrary in both markets, so no market's survivor set
may be read as a selection (this morning's KR table retracted exactly that reading for KR).

### (c) Rights

🚫 **Cannot cite today, in every stage (SWEEP · EVENT_ALPHA · ROTATION · PREMORTEM · DEEP · BET · ALPHA):**
1. **The sweep's news-velocity axis** — it is not in the score (`n_axes=3`) and its 49 present values
   are an arbitrary sample.
2. **Theme freshness / news velocity as a ranked quantity.**
3. **"It went quiet" / "the story cooled" for any name or sector** — the desk cannot distinguish silence
   from the pipe. Probe A says the pipe is the answer 240 times out of 240.
4. **`breadth` as a news-independent reading** — it is computed off tags, and tags consumed velocity.

✅ **Retained**: **hand-probed per-name news velocity** and any article read directly through
`fts search` / `brief` / `thread`, because those are **event observations**, not the broken axis. Any
stage using them must name the probe and its clock.

---

## G2 · Scoring-scale continuity — 🟢 **PASS**

**Command** `SECTOR_FLOW_US.json §scoring` vs `llm_outputs/sector_flow/history.json` prior snapshot.

- Today: `n_axes = 3`, `vel_axis = false` ⇒ mode `nonews`.
- Prior snapshot in history: **`2026-08-18`**, `_mode = nonews`, 300 names.
- Same axis count ⇒ **subtraction between the two snapshots is legal.**

★ **And the baseline is one session, not two.** History now runs `… 08-13 · 08-14 · 08-18 · 08-19`.
Yesterday every `delta` field silently meant a two-session move (08-14 → 08-18) and that table had to
say so. Today `delta` means what it looks like it means.

**Measured Δ**: **295 of 299** scores moved · median |Δ| **0.095** · max |Δ| **0.943** ·
**4** names newly tagged 🟢. Tag distribution today: **🟢 7 · 🟡 229 · 🔴 63** (universe `wflow` **−0.162**).

**✅ Rights**: `delta` may be cited as **a single-session move, 2026-08-18 → 2026-08-19.**
**🚫 Rights**: no stage may describe today's Δ as multi-day, and no stage may compare today's scores to
any snapshot older than 08-18 without re-checking `_mode` for that date.

---

## G3 · Who owns the sector sign — 🟢 **PASS** — flipper list in full, **1 of 11**

**Command** `SECTOR_FLOW_US.json §sector_rotation[].top1_flips_sign`.

| Sector | top1 | top1_w | wflow | wflow_ex_top1 | swing |
|---|---|---:|---:|---:|---:|
| **Materials** | `LIN` | **24.7%** | **−0.099** | **+0.063** | 0.162 |

**The other ten sectors: zero flippers.** Yesterday there were three (`BRK-B` Financials, `CAT`
Industrials, `LIN` Materials); `BRK-B` and `CAT` both left the set on today's bar. `LIN` has flipped
Materials' sign on every run this desk has measured.

🚫 **Cannot do today**: **promote or demote Materials on its `wflow` sign** (ROTATION §2). One name at
24.7% weight is manufacturing the negative. Use `eqflow` (+0.063 ex-top1 direction) or hold.
✅ The remaining ten sectors' `wflow` signs are **not** owned by a single name and may be used.

---

## G4 · Risk-unit stability — 🔴 **FAIL** *(11th consecutive run)*

**Command** `scripts/risk_units.py --book --days {250,500,750}`.

| Window | Units | U0 |
|---|---|---|
| **250d** | **11** | `028050, 316140` (two book theme labels in one measured unit) |
| **500d** | **10** | `ANET, ETN` |
| **750d** | **10** | `ANET, ETN` |

500d and 750d agree **exactly**, unit for unit. 250d does not: it splits `AVGO`/`NVDA` (one unit at
500/750) and merges the two KR holdings (separate at 500/750). **The same 13 positions group
differently depending on the window.**

🚫 **Cannot do today**: cite a concentration guard **as a single number**. Any concentration statement
must carry the `--days` it came from **on the same line**.

---

## G5 · Does the universe cover the book — 🔴 **FAIL** *(staleness + one hole)*

**Command** `data/us_universe/us_top300.csv` × book holdings × `SECTOR_FLOW_US.json` scored set.

- **US book holdings (11): `ANET · AVGO · ETN · HPE · MET · MPC · NDAQ · NUE · NVDA · PSX · RTX`.**
  **Missing from universe: 0. Missing from the scored set: 0.** ✅ The cover leg passes.
- ⚠ **`us_top300.csv` is dated 2026-07-15 — 36 days old** (PASS limit ≤8). Market-cap weights used by
  every `wflow` in this run are **36-day-old weights**.
- ⚠ **`EA` is in the universe and not in the sweep** (299 scored of 300 requested) — no close in the
  price frame on any of the last three bars. 8th consecutive run.

🚫 **Cannot do today**
1. **Describe any `wflow` as "current market-cap weighted"** — it is weighted as of 2026-07-15.
2. **Make any flow / RS / OBV / short call on `EA`** — the desk is not measuring it as absent; the desk
   **cannot measure it**. Those are different sentences and only the second one is true.

---

## G6 · Estimate-snapshot accrual — 🔴 **FAIL**

**Command** `scripts/snapshot_estimates.py --status`.

- **12 files / 30 calendar days** (2026-07-22 → 2026-08-20) = **0.40 files/day**.
- 28 more days needed to reach the 40-day target: ideal **28 days**, measured **≈70 days** = **2.5×**
  the 1.5× limit.
- Gaps (days): `[6, 3, 1, 2, 1, 1, 5, 1]` · median 2 · max 6.
- ★ Last save is **today, 2026-08-20**, the second consecutive day. The daemon is firing; it is the
  30-day history that is thin, and **thin history cannot be back-filled.**

🚫 **Cannot do today**: report `kelly_size --ic` output **as an evidence-backed size**. If it is used at
all it must be labelled **"mechanical quarter-Kelly, IC sample below threshold."**

---

## G7 · Tool liveness — 🔴 **FAIL** *(11th consecutive, same two)*

**Command** `--help` on all 41 entry points this run may touch (16 modules + 25 scripts).

- **Exit 0 — 39 of 41.** All 16 modules except `module_chart`; all 25 scripts except `margin_history`.
- **Exit 1 — 2:**
  - `module_chart --help` → prints a bare usage line and exits 1 (`usage: python -m module_text_chart <ticker> [--read]`). **Functional probe: `module_chart NVDA --read` returns a full panel** — OBV distribution (20d slope −114%), no divergence, bull stack 5>20>60>120, Bollinger expansion 21.5%, RSI 71.9, turn verdict NEUTRAL/CHOP, trigger `close>222.55`, stop 190.01. **The tool is alive; only its `--help` is not.**
    ⚠ **RULE D6 — EXEMPTION CLAIMED, with its reason.** The OBV figure above is quoted as **evidence that a TOOL PRODUCED OUTPUT**, not as evidence about `NVDA`. This gate makes no market claim of any kind (P4), so the C-grade-signal rule has nothing to bind here — and the panel is quoted in full precisely so that a reader can see the tool returned every field, not one.
  - `scripts/margin_history.py --help` → exit 1 (argparse `%` escaping bug in a help string). **Functional probe: `margin_history NVDA` returns FY2009–FY2026 gross margin in full** (max FY2025 75.0% · min FY2009 34.3% · median 56.9%). **Alive.**

🚫 **Cannot do today**: nothing is revoked outright — **but any citation of `module_chart` or
`margin_history` must state "`--help` is dead; output verified by direct functional probe."**
The other 39 entry points keep full citation rights.

⚠ Standing note (measured 08-19 KR, re-confirmed here): **`--help` exit code is a proxy for tool
liveness and it is a leaky one.** Both of today's failures are help-rendering bugs sitting on top of
working code. Repair is a human-approval item, not this stage's job (rule 1).

---

## Rights revoked today — one-page summary

1. **No news-velocity axis, no theme freshness, no "it went quiet", no `breadth`** (G1). Hand probes and
   directly-read articles are allowed **with their clock stated**.
2. **No promotion/demotion of Materials on its `wflow` sign** (G3) — `LIN` at 24.7% owns it.
3. **No concentration number without its `--days`** (G4).
4. **No `wflow` described as "current" market-cap weighting** (G5 — weights are 36 days old).
5. **No flow/RS/OBV/short call on `EA`** (G5) — unmeasurable, not absent.
6. **No `--ic`-derived size reported as evidence-backed** (G6) — "mechanical quarter-Kelly" only.
7. **`module_chart` / `margin_history` citations must carry "`--help` dead, output probed"** (G7).
8. **No 08-20 price of any kind; nothing re-pulled after 22:30 KST may be mixed with sweep statistics**
   (G0).

**Rights explicitly granted today (stated positively so stages use them):** settled prices and every
price-derived statistic through the **2026-08-19** close · a **one-session Δ (08-18 → 08-19)** ·
`eqflow` and the ten non-flipper sector signs · FINRA short pressure · CFTC COT percentiles · FRED
series · primary filings · the full `module_chart --read` panel · hand-probed per-name news velocity.

> ⚠ This document is not written into the carry (`handoff/`) — instrument state is not a market view.
> HANDOVER reads it; nothing else inherits it.
