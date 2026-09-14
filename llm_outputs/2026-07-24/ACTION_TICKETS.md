# ACTION_TICKETS — industry_US — 2026-07-24 (Fri)

> Stage 9/10 (ALPHA). **Pre-committed conditional brackets**: every binary in the window, both sides,
> with its frozen observable, its threshold, its date, and what it would change.
> Every relative figure names **SPY** inline. **Analytical only.**

---

## ⚠ Deviation logged — no sizing, no share counts, no `action_bracket.py` run

The L1 names `scripts/action_bracket.py` as the generator, which emits **DRY-RUN share counts** from a
live KIS account balance. **This run's standing instruction is analytical output only, zero buy/sell
recommendations**, and a share count is the mechanics of a recommendation. **The script was therefore
not run**, and this file delivers the part the protocol actually needs downstream — **the both-sides
brackets and their observables** — with no position sizing anywhere.
**Resolved this way deliberately; logged here and in the run summary.** *(Unattended-run rule: default
to documented practice and state which way it was resolved.)*

⚠ **A second reason this was the right call today**: the script's own `why core` string is dig **D32**
— it still ships PSX's *"cheapest large refiner on forward"* rationale, which **R8 retracted on
2026-07-22 and which this run re-measured false for a third consecutive time (MPC 10.71 < PSX 11.02 <
VLO 12.27)**. A ticket whose stated premises are stale strings is worse than no ticket.
**`core_pick` is human-locked; no stage may rewrite it.**

---

## 0 · No cycle-GAP starter is triggered — and why the ✅ is weaker than it reads

`CYCLE_EXPOSURE.json`: AI-compute **12.14% ≥ 12.0%** ✅ · Energy **11.33% ≥ 8.0%** ✅ · missile-defense
10.27% with **no threshold set**. **No 🚨, so no tape-independent core-starter module fires.**

⚠ PREMORTEM Lens 4 measured what the ✅ conceals: the AI-compute epicenter bucket spans **95.0pp of
RS60 vs SPY** (MU +85.6 → AVGO −9.4, median +21.4) and the book's held names rank **AVGO 10/10 and
NVDA 9/10 — the two worst**; Energy's ✅ is satisfied by **XOM, 5/6 in its own bucket**, the leg with
**+2.7pp** of 60-day excess vs SPY while the excluded refining leg carries **+22.9 to +34.2pp**.
**Refining, AI-security and memory/storage exposure are each 0%, and two of the three are invisible to
the guard because no registry row exists.** Seven registry edits are proposed to a human in
`BLINDSPOT_PREMORTEM.md` §5. **The ✅ means "no gap the registry can see."**

---

## 1 · The brackets, in date order

### ⓘ Implied-move status, measured twice today — **M47 reproduces for a THIRD run**

**Unusable (expiry 2026-07-24 = D0, i.e. they expire BEFORE their events):** META ±2.0/2.1% ·
MSFT ±1.5/1.8% · AMZN ±1.4% · AAPL ±1.2% · VLO ±2.3% · MA ±1.3% · XOM ±1.4/1.6% · UPS ±1.3/1.7%.
★ **Usable, and there are exactly two on the entire board:** **MPC ±11.2%** and **STNG ±10.0%**, both
expiry **2026-08-21 (D28)**.
⇒ **Every threshold below that is not taken from an options chain says so and is categorical instead.
None is invented.**

---

### T-1 · **UPS Q2 — 2026-07-28** `S20` · the window's first binary, and it is two tests at once

| | |
|---|---|
| **Frozen observable (categorical)** | Does the Q2 call **quantify fuel expense YoY**, and is any FY guidance cut attributed to **fuel** or to **volume**? |
| **Implied move** | ±1.3–1.7%, **expiry 07-24 = D0 — NOT event-priced. Declared unusable; no magnitude threshold taken.** |
| **Measured prior** | UPS is priced at **+0.6% to mean target** — the Street expects nothing. Flow +0.563, RS20 **+6.8** / RS60 **+2.2 vs SPY**, OBV accumulating, short **3.1% float covering** |
| **Branch A** — fuel quantified up materially YoY, guidance cut attributed to fuel | **W4 closes at 5 of 5.** DAL/UAL/FDX/LUV already disclosed **+66% to +84% YoY**; the "paper crack" objection dies at the largest US distillate buyer |
| **Branch B** — fuel is a **non-event** in the call | **Against us.** The distillate bottleneck is absent from the P&L of the buyer most exposed to it ⇒ contradicts §A's Leg 3 directly |
| **Branch C** — guidance cut on **VOLUME** | **Against the promoted rail node.** Cass shipments are already **−4.1% YoY / −3.1% MoM**; a volume-led cut falsifies the freight read. Read-across CSX, UNP, NSC |
| ⚠ **Scoring discipline** | **Branch C is scored on the rails' own dwell/volume KPI, NOT on UPS's price reaction** — **D28** (never put a price reaction inside an observable's branch) |

---

### T-2 · **FOMC — 2026-07-29** `S19` ★★ the branch no prior scenario contained

| | |
|---|---|
| **Frozen observable** | (i) the **target-range decision** (raised / held / cut); (ii) **DGS2**, quoted **with DFII10 alongside T10YIE** (S9's own rule) |
| **State at registration** | CME FedWatch hike odds **10.7% (07-15) → 34.7% (07-22)** · DGS2 **4.31% = 120-day high** · DFII10 **2.39% = 120-day high** with T10YIE **2.28%, flat** · 2s10s **+0.36, flattening a 2nd session** |
| **No options instrument exists** for an FOMC decision here — thresholds **reuse P1's already-registered levels** rather than being invented, and that is stated |
| **Branch H** — raised, **or** held with **DGS2 closing > 4.45% by 2026-08-05** | **Against OW Health Care first** — it went to OW on flow that is mega-cap-shaped (**top-5 = 50.6% of cap but 77% of sector wflow**), so a discount-rate shock hits that leg first. ⚠ **Qualified by measurement**: XLV's residual sensitivity to Δ^TNX is **−0.198**, *behind* XLRE **−0.293** and XLU **−0.220** — so "hit first" rests on the **concentration** leg, not on rate beta. And the relationship is **entirely same-session** (±1/±2 day ≤ 0.075): **no advance warning** |
| **Branch D** — held with dovish language and **DGS2 closes < 4.15% by 2026-08-05** (= P1's registered anti-signal) | ★★ **FOUR tilts lose together**: OW Energy **+** N− Utilities **+** N− Real Estate **+** N− Cons. Staples — measured, not asserted: **XLE–^TNX +0.326** against **XLU/XLRE/XLP–^TNX −0.227 / −0.302 / −0.194**, with **XLU–XLRE +0.538** and **XLRE–XLP +0.565** both clearing R10's own 0.35 threshold. ★ **And §0 of BET_SHEET adds a fifth: the rail node is ~8/12ths fuel surcharge, i.e. the Energy bet again** |
| **Branch M** — held, DGS2 stays 4.15–4.45% | No conclusion changes |
| **Bracket invalidation** | **HY OAS > 3.10% on a close** (P2's line) — then it is a credit event and the rate attribution is void |
| ⚠ **n≈1 warning, pre-registered** | FOMC 07-29 and June PCE 07-30 **share one driver (oil), one day apart. They are not two observations** |

---

### T-3 · **MSFT + META capex — 2026-07-29 (date disputed, D47)** `S13` · the highest-information bracket carried

| | |
|---|---|
| **Frozen observable (cross-condition, unchanged)** | (1) the **capex guide** at MSFT and META · (2) the **spenders'** NTM P/E change · (3) the **suppliers'** median **RS20 vs SPY** (MU, AMAT, LRCX, KLAC), over the 10 sessions to ≈**2026-08-12** |
| **⚠ Date disputed** | `catalyst_calendar` and news bodies say META **07-29**; `yfinance` says **07-30** for both, and **MSFT is absent from the calendar entirely (D18, 5th consecutive run)**. **Registered dates are NOT rewritten on one disagreeing provider (D5)** |
| **Branch A** — capex raised **AND** spender NTM P/E compresses **AND** supplier median RS20 vs SPY turns positive | **Info Tech's single label is wrong on BOTH halves at once** ⇒ IT must be split, as R7 split Real Estate and M26/M36 split Industrials |
| **Branch B** — raised and the spenders hold their multiple | The raise is read as demand; low information by the pre-registered asymmetry |
| **Branch C** — capex **cut** at either | **High information.** Breaks the volume leg and the price leg together and extends past memory into AVGO/NVDA/TSM. ⚠ Its narrative frequency is **literally zero** (`capex cut` d1 = 0 for a third measurement) — **watch the line item, not the feed (C6)** |
| ★ **What changed this run, and it weakens the branch-A prior** | The 07-23 "supplier over spender" spread of 6.07pp is **a spender event, not a rotation**, once normalized: **GOOGL −3.44σ · AMZN −2.81σ** against **MU +0.50σ · KLAC +0.31σ · AMAT +0.26σ · LRCX +0.03σ**. **The suppliers did not rally; they failed to fall.** Branch A has **n≈0** observations on its supplier half, not n≈1. And the sweep's 20-day window runs the other way (suppliers' RS20 all negative, AAPL/MSFT 🟢) |
| ★ **C6 refined** | The branch **is** now narrated — under different words. `free cash flow` **1.41×** and `capex` **1.40×** are the two fastest terms on the board (pool-normalized), while `capex cut` and `margin drag` are both **0**. **Track the economic content, not the frozen phrase** |

---

### T-4 · **VLO Q2 — 2026-07-30** · the refining node's own falsifier

| | |
|---|---|
| **Frozen observable** | **VLO's reported gross margin.** Consensus **EPS $10.127 on revenue $38.429B** implies gross margin going **6.30% → ~12.6%** — a doubling, where **6.30% (Q1'26) is VLO's own 5-quarter maximum** |
| **Implied move** | ±2.3%, **expiry 07-24 = D0, six days before the print — unusable.** Bracket is categorical and says so |
| **Branch ≥12.0%** | Consensus is met; the crack is converting to reported margin and §A's "margin not premium" verdict is confirmed on a US income statement |
| **Branch 10–12%** | Partial; the extrapolation was heroic but directionally right |
| **Branch < 10.0%** | ★ **This file's own falsifier fires.** The crack did not convert, and the peak-denominator reading takes over |
| ⚠ **The measured warning attached to it** | **VLO is the ONLY refiner with analysts cutting its current quarter — 6↑/5↓ (7d), 7↑/5↓ (30d)** — and it prints first. Its current-quarter consensus increment has been **exactly 0.00 for two consecutive runs** while the *next* quarter still rises: **consensus has stopped marking the quarter VLO is about to report** |

---

### T-5 · **STNG Q2 — 2026-07-30** `S21` ★ one of only two usable straddles on the board

| | |
|---|---|
| **Frozen observable** | Q2 **TCE $/day** and the **% of Q3 days already booked** |
| **Implied move** | ★ **±10.0%, expiry 2026-08-21 (D28) — USABLE** |
| **State** | 🟡, **RS20 +5.8 / RS60 −4.8 vs SPY**, news velocity **0.00×**, short **5.4% of float, BUILDING**, P/C 1.06. On the reject ledger as `A.flow미도착` since 07-23, recheck 08-06 |
| **Branch A** — TCE flat-or-down and Q3 booked days below Q2 | **Against us: S8 branch A arrives with no Hormuz statement.** The Red Sea rerouting rent has peaked and the OW's war-premium half is confirmed as the driver |
| **Branch B** — TCE up, Q3 bookings ≥ Q2, **and the move is outside ±10.0%** | The blockade is being paid in cash, and **M45**'s "the literal beneficiaries are not being bought" becomes a dislocation rather than a correct market judgment |
| **Branch C** — inside ±10.0% either way | **No information — already priced.** Pre-committed so an in-band reaction cannot later be read as confirmation |
| **Cross-check** | The settled 3-2-1 crack (frozen **66.49**) holding **≥ 65** through 2026-08-06 invalidates branch A's read-across to refining |

---

### T-6 · **MA Q2 — 2026-07-30** `S14` + `S14-ANNEX` · the contaminated observable

| | |
|---|---|
| **S14 stays frozen as written and will be scored as written on 2026-08-06** — moving a registered observable after the fact is what L3 `scenario_score` forbids |
| **Pre-registered alongside it (before the event)** | the **{MA, V}-only** reading, because **PYPL's +31.2 RS20 vs SPY is a live merger-arb spread** (Stripe bid **$53B on 07-15**; PayPal's board **held out for more on 07-20**; unaccepted), corroborated by PYPL's estimates being **cut 0↑:4↓ next-quarter and 0↑:3↓ CY** while it trades **5.5% above** target |
| **If the two readings disagree, the disagreement IS the finding** — it measures how much of "Financials breadth" was a takeover spread |
| **Baseline, from the filing rather than sell-side** | MA FY2025 **cross-border volume +15% local currency**, GDV $10.6T +9%, switched transactions 175.5B +10% |
| **Branch B (against us)** | cross-border decelerates from +15% **and** {MA, V} RS20 vs SPY flips negative within 5 sessions, to **2026-08-06** |
| ⚠ | Implied move ±1.3%, **D0 — unusable, and not used** |

---

### T-7 · **June PCE — 2026-07-30** `S15` · and **The undated one**

**S15**: frozen observable **core PCE MoM**, read against core CPI's printed **−0.02% MoM**.
Branch A **> +0.3%** ⇒ P1's "reaction-function, not inflation" framing collapses. Branch B **≤ +0.3%**
⇒ P1 stands. ⚠ The numeric line is **judgement and is flagged as such** — no options threshold exists.
⚠ **Shares its driver with T-2. Not an independent observation.**

**S8 — the Hormuz "Strait open" statement: still `[blank]`, deliberately not guessed.**
★ **But it acquired its first dated proxy this run**: **the Russian diesel export ban expires
2026-07-31** (imposed 07-08; the 2023 precedent was partially lifted after two weeks). If it lapses
un-renewed, the middle-distillate bottleneck loses its largest single contributor **three days after
VLO prints and one day after STNG prints.** Carried as an **observable**, not folded into the war narrative.

---

### Dropped for lack of information content — stated, not silently skipped

- **AAPL 07-31** — neither branch moves a tilt; it enters only as one third of S16's `{MSFT, AMZN, AAPL}`
  equal-weight **denominator**, so a beat and a miss both move the comparator.
- **AMZN 07-30/31 as a standalone** — S2 branch B **pre-declares** its outcome as *"Partial; wait for
  AMZN + AAPL."* A bracket designed to resolve to "partial" cannot change a conclusion.
- **META 07-29 and MSFT 07-29/30 as two brackets** — they are **one** cross-condition (T-3). Scoring
  them separately manufactures n=2 from one date and one driver.

---

## 2 · Freshness gate — `theme_age`, `--scope foreign`, token-0 novelty

| Theme | Verdict | Age (d) | 7d avg | Accel | Total | Note |
|---|---|---|---|---|---|---|
| **Red Sea** | 🟡ACCELERATING | ≥90 | 88.9 | ★ **42.31×** | 727 | the board's fastest |
| **surcharge** | 🟡ACCELERATING | ≥90 | 11.4 | **12.24×** | 147 | ★ the rail node's actual driver |
| **intermodal** | 🟡ACCELERATING | 80 | 4.4 | **10.22×** | 62 | small n |
| **diesel** | 🟡ACCELERATING | ≥90 | 36.6 | **8.71×** | 545 | |
| **GLP-1** | 🟡ACCELERATING | 77 | 24.6 | 8.10× | 374 | |
| **capex** | 🟡ACCELERATING | ≥90 | 119.9 | 5.88× | 2,035 | |
| **payments** | 🟡ACCELERATING | ≥90 | 218.7 | 5.87× | 3,754 | |
| **insurance** | 🟡ACCELERATING | ≥90 | 146.0 | 5.15× | 2,686 | |
| **refining** | 🟡ACCELERATING | ≥90 | 87.4 | 4.68× | 1,859 | |
| **rail** | 🟡ACCELERATING | ≥90 | 32.3 | 4.50× | 672 | ⚠ **poisoned token — ~40% fintech "payment rails"** |
| **rate hike** | 🟡ACCELERATING | ≥90 | 91.4 | 2.07× | 3,399 | |
| **crack spread** | 🟡ACCELERATING | 78 | 4.7 | 20.20× | **45** | ⚠ **n=45 over 90 days — the accel ratio is not usable at this sample** |

★ **Not one theme in this run is 🟢FRESH, and not one is 🔴FADING. Every bet is on an OLD theme that
re-ignited.** By the L1's own rule that is the weaker of the two live states — **ECHO/FADING theses
need stronger live evidence to survive, and 🟡 is one notch above that.** The strongest live evidence
this run produced is precisely the non-narrative kind: **settled weekly cracks, a supermajor's realized
margin marker, EIA utilization, primary 8-K filing dates, and revision breadth.**
⚠ **Two tool defects carried (D36 family)**: `rail` is a poisoned FTS token (entity-qualify before
use), and `crack spread` is a two-token phrase whose 45 total hits make its 20.2× ratio unusable —
**query themes as single tokens, and say which was used.**

---

## 3 · Post-run kill-switch check (the DRIFT substitute — **D17 is unfixed for a 3rd run**)

`scripts/drift_watch.py --report …/MACRO_REPORT.md` → **`'drift' 는 원격 실행 불가(조회 전용)`**.
**The client-side `DB_READ_CMDS` edit was never deployed to the running server** — this is a one-command
fix for a human (server `git pull` + API restart, **P6**), not a code change. The measured substitute
(pool-normalized `fts --count` over this run's own anti-signal terms) is executed in stage 10 and is
now effectively the permanent path.

---

**Every bracket above names both branches, its observable, its threshold and its date. There is no
one-way bracket in this file, and no share count anywhere in it.**
