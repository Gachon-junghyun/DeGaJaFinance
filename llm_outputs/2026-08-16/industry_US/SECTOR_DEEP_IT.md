# SECTOR_DEEP_IT — industry_US · 2026-08-16 · **Rotating slot 1** (last covered 2026-08-13 = 3 runs)

> Full fresh map. Benchmark **`SPY`** named inline (C1). Settled **2026-08-14**,
> `yfinance auto_adjust=False`. No sizing (P4).
> ★ Given the rotating slot on the 08-15 DEEP_LOG's own written pre-commitment — honoured.

## §1 · ★★★ The finding that changes the sector read: the board's TOP flow score just round-tripped

`COHR` carries **`flow_score` +0.99 — the highest of all 299 names** — a 🟢가속 tag and `vol_surge`
**1.67**, the biggest surge in the universe. **Pull its actual closes:**

| | 08-05 | 08-06 | **08-07** | 08-10 | 08-11 | **08-12** | 08-13 | **08-14** |
|---|---|---|---|---|---|---|---|---|
| **`COHR`** | 328.22 | 334.22 | **379.13** | 325.15 | 328.57 | 355.64 | 327.23 | **325.83** |
| `LITE` | 826.26 | 838.06 | 890.17 | 813.51 | 820.59 | **932.47** | 880.41 | **926.14** |

| | 5-session | 20-session | 5d excess vs `SPY` | 20d excess vs `SPY` |
|---|---|---|---|---|
| **`COHR`** | **−14.06%** | +17.37% | **−14.457pp** | +12.927 |
| `LITE` | +4.04% | **+26.38%** | +3.642 | **+21.934** |
| `SPY` | +0.40% | +4.45% | — | — |

⇒ **`COHR` spiked to 379.13 on 08-07 and gave the entire move back — it closed 08-14 BELOW its 08-05
level.** Its `vol_surge` **1.67** is measuring **the round-trip's volume, not accumulation**, and its
🟢 is measuring a spike that has already failed.
★ **`LITE` is the opposite** — it made its high on 08-14 (926.14) and **held** the move.
⇒ **The desk has been carrying `COHR` and `LITE` as one pair ("the only two admissible 🟢 in IT") for
two runs. On the 5-session window they are 18.1pp apart and pointing in opposite directions.** `W5`
inside a two-name node.

**Corroborating structure** (`module_chart --read`, `asof 2026-08-14`):
- `COHR`: OBV **누적 (+57% 20d slope)** · no divergence · **MA 혼조, price above only 2 of 4 MAs** ·
  Bollinger expansion **52.2%** (the volatility is enormous) · RSI 58.5 · turn verdict
  **NEUTRAL/CHOP** · **ignition trigger `close > 332.48` — it closed 325.83, i.e. BELOW its own
  trigger** · swing-low stop 222.05.
⇒ **The OBV says accumulation and the price structure says chop below the trigger.** Under `D6` OBV is
C-grade and the price axis is A-grade ⇒ **the price axis wins: `COHR` has not ignited.**

## §2 · The sector verdict's own arithmetic — N+ rests on 0.021 flow points

| | value |
|---|---|
| `wflow` | **+0.023** — ⚠ **`NVDA` alone**; ex-top1 **−0.082** (G3 flipper, 19.4% weight) |
| `eqflow` | **+0.044** |
| The N+ basis | `eqflow` **>** `wflow` = a gap of **0.021 flow points** |
| Δ (day-over-day) | **+0.007** — a **95% decay** from the +0.152 that justified the 08-14 promotion |
| breadth | **0.05** (5🟢 / 6🔴 of 56) — and the 🟢 count fell to **3 of 56** admissible this run |
| Equal-weight vs cap-weight, price axis | `RSPT` exc5 **+2.030** · exc20 **+6.979** · exc60 **+9.800** vs `XLK` **+0.687 / +3.766 / +3.873** — **`RSPT` beats `XLK` on all three windows vs `SPY`** |

⇒ **The breadth leg is real on the PRICE axis** (`RSPT` > `XLK` on three windows) even though it is
paper-thin on the flow axis. **That is the honest split: N+ survives on equal-weight price, not on
flow.** `S85` (`RSPT − XLK`, settle **08-21**) reads **+1.343 = branch C**.

## §3 · The narrative delta — Microsoft is building its way off Nvidia

EVENT_ALPHA Card 2, body-read, **REIGNITED 6 days, outlet curve 6→7→5→10→4→5, 132 articles**:
- **08-10** *"Microsoft to unveil **Maia 300** AI chip this fall, **targets 300,000 units**"*
- **08-10** *"Microsoft Plans to Ramp Up Homegrown AI Chip Production **Next Year**"*
- **08-11** *"Microsoft could unveil Maia 300 as early as **September**"* [`economictimes`]
- ★ **08-10 — *"Microsoft Rethinks Its Nvidia Reliance"*** — the direction stated outright
- ★ **08-11 — *"Marvell Could Be Next Winner in Microsoft AI Bet"*** — the named beneficiary

🚨 **The DEEP mandate was to find or fail to find a primary source. Result: FAILED TO FIND.**
Every item in the cluster traces to *"The Information, Report Says"* / *"Market Chatter"*. **No
Microsoft filing, 8-K, or press release is in the corpus.** ⇒ **`[news]`-grade only, and `W4` is half
met**: the *customer* is named, **no supplier contract is**. **This may not be cited as evidence for a
new proposition** — it is a dated watch item, nothing more.

## §4 · Value chain — 8 nodes, bottleneck marked

`Hyperscaler capex budget (MSFT·GOOGL·AMZN·META)` → `Merchant GPU (NVDA)` ∥ **`Custom ASIC design (AVGO · MRVL)`** →
`Foundry (TSM — outside us_top300)` → `HBM / memory (MU · SNDK · WDC)` →
**`🔴 OPTICAL INTERCONNECT + ADVANCED PACKAGING — the binding constraint`** → `Networking (ANET · CSCO)` →
`Rack power & thermal (VRT · ETN)` *(cross-sector → INDU/UTIL)* → `Data-centre shell (DLR · EQIX · IRM)` *(cross-sector → RE)*.

- **Bottleneck justification**: GPU supply is being *added* (Maia 300 is 300k units of **new**
  capacity, not a substitution for scarce silicon). What does not scale with either merchant or custom
  silicon is **optical interconnect and packaging** — and it is the one node where the desk's own flow
  data puts the **only two admissible 🟢 in the sector** (`COHR`, `LITE`).
- ⚠ **Substitution does NOT shrink the bottleneck node — it grows it.** Both merchant and custom parts
  need the same optics. That is the structural reason the optical node is the interesting one, and it
  is **`[inferred]`** — no filing was pulled to confirm it this run.

## §5 · 🚨 `D250` — the anti-tunnel instrument cannot see this sector's own cycle

`data_build/cycles/cycle_registry.json` is **29 days stale**, rank-3 floor **0.0** (check OFF), and has
**NO ENTRY** for either cycle this DEEP just mapped:

| Cycle | Where it shows up | Registry | Book exposure |
|---|---|---|---|
| **Optical / interconnect** | The node this DEEP marks as the bottleneck; the sector's only two admissible 🟢 | **NONE** | **ZERO** |
| **Custom AI silicon** | §3's whole narrative; `MRVL` named as beneficiary | **NONE** | indirect (`AVGO` held) |

⇒ **PREMORTEM Lens 4 returns ✅ on AI-compute (16.54% vs a 12.0% floor) while being structurally unable
to flag zero exposure to the bottleneck node.** Registered as **`S94`** (PREMORTEM §5). **The remedy is
human (P5) and this DEEP does not promote either name** — §1 is precisely why not.

## §6 · Instrument events this sector must not mistake for market events

1. **`NVDA` and `MRVL` both lost their 🟢 this run with ZERO price change** — velocity 1.20 → 1.16 and
   1.20 → 1.10 crossing the 1.2 gate, every other input identical to the digit. Both carry `vol_surge`
   **0.73 / 0.48** ⇒ **neither could ever have been green on the 3-axis path.** **No fundamental read
   may rest on that transition.**
2. **`NVDA`'s news velocity was measured three times today at three values** — sweep **1.16×**
   (~20:1x KST), `module_flow` **1.09×** (~22:5x KST), yesterday **1.20×** — **on a frozen tape**
   (`D271`).
3. **`CSCO` is 🟢 on RS20 −4.7 — negative — for a third consecutive run**, and its 🟢 is
   velocity-produced (velocity 2.48). **Not admissible.**
4. **`NVDA`'s straddle expires 2026-08-17 and it prints 2026-08-26** ⇒ its **±1.5%** implied move is
   **not event-priced** and no threshold may be taken from it (`M47`, PREMORTEM §6).

## §7 · Estimate-momentum / valuation note — and the rule that stops it being over-read

The carry rule is explicit: 🚨 **do NOT write "revisions turn before price does" — it was tested and it
did not hold** (`measure_ic.py`: W1 **+0.403** vs W2 **−0.299**, opposite signs, both above the power
floor; on the ex-IT 120-name control the Q5−Q1 spread collapses **+9.4pp → −1.1pp** ⇒ **an IT loading,
not a revision axis**). ⇒ **No revision-based claim is made in this file.**
⚠ **And `G6` binds any sizing downstream**: the estimate-snapshot series is accruing at **0.42
files/day vs an ideal 1.0** (**ETA ≈72 days vs 30**), so `kelly_size --ic` output is **not** an
evidence-backed size and must be labelled **"mechanical ¼"**.

## §8 · Track KPIs and anti-signals

| Track KPI | Current (08-14) | Kill / anti-signal |
|---|---|---|
| **`COHR` vs `LITE` 5-session excess spread vs `SPY`** | **−14.457 vs +3.642 = 18.1pp apart** | they re-converge ⇒ the "one node" read was right after all |
| `COHR` ignition trigger | close **325.83 vs a 332.48 trigger — BELOW** | `close > 332.48` **with** `vol_surge ≥ 1.0` ⇒ genuine ignition |
| `RSPT` − `XLK` vs `SPY` (`S85`) | **+1.343 = branch C**, settles **08-21** | goes negative ⇒ the N+'s only surviving leg fails |
| `eqflow` − `wflow` | **+0.021** | flips negative ⇒ N+ has no basis at all |
| Maia 300 primary source | **none exists** | a Microsoft filing / partner 8-K by **2026-09-30** ⇒ the story becomes evidence |
| `NVDA` print | **2026-08-26** | ⚠ its straddle does **not** cover the event |

**🚨 VOID**: a change in Microsoft's own **capex guide** inside the window — substitution and demand
would move together and the sector cannot be read (§4 asymmetry: a capex **cut** breaks both legs of
the memory thesis; a **raise** confirms volume only).

## §9 · Verdict handed forward

**Hold N+, and the basis is now explicitly named as the equal-weight PRICE leg, not the flow leg.**
- ⚠ **To BET: nothing is handed forward.** The two names that would have been candidates fail on the
  measurement: **`COHR` round-tripped −14.06% in five sessions and sits below its own trigger**, and
  **`LITE`'s green is dated to its own 08-11/08-12 earnings print** (reaction volume, not
  accumulation). **Re-read both after the print volume rolls off, ≈08-25.**
- ★ **To the dig list**: the sector's bottleneck node **has no registry entry** (`S94`), and the desk
  holds **zero** exposure to it — the 2026-07-14 postmortem's failure mode reproduced *structurally*.
- 🚫 `CSCO`'s 🟢 (velocity 2.48, RS20 −4.7) is **not admissible**, third run running.
