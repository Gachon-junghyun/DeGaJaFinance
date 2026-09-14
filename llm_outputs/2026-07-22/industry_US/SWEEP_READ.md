# SWEEP_READ — industry_US — 2026-07-22

> Stage 2/10 (SWEEP). **The reading, not a second copy of the data.** Sector rows live in
> `SECTOR_FLOW_US.json §sector_rotation`; per-name rows in `§names` and `US_LIVE_SHORTLIST.json`.
> Nothing already in those files is reprinted here. Benchmark for every RS figure below: **SPY** (C1).
> ⚠ Sweep **asof 2026-07-21 close** — today's oil re-escalation, the 200% pharma-tariff headline and
> the Saudi nuclear approval are **NOT in these numbers**. Cross-checks are read with that lag.

## 1. Universe headline

**n=300 · wflow −0.051 · 🟢 11 / 🔴 83.** Distribution outnumbers accumulation **7.5 : 1** on a tape
whose mega-cap-weighted flow is essentially flat. NaN audit (the 2026-07-15 bulk-download trap):
**0% NaN on `last`, `rs20`, `rs60`, `flow_score`** across all 300 — rankings are trustworthy this run.

## 2. Cross-checks against the MACRO matrix — where money agrees and where it does not

**CONFIRMS · Financials (matrix OW).** The only sector where **eqflow > wflow** (+0.357 vs +0.212) —
**breadth-led, not mega-cap-narrow**, and it carries 5 of the board's 11 greens, the most of any
sector. This is the highest-quality confirm on the board. ⚠ But the confirm is *not* in the
investment banks: GS, MS and C are all 🔴분산. The money is in insurers/custody/payments
(TRV, CB, STT, USB, PYPL). **The MACRO steepening logic points at banks; the flow points at
non-bank financials.** ROTATION should carry the sector OW with the sub-node named.

**CONFIRMS with a correction · Energy (matrix OW+).** wflow **+0.248 = #2**, and **delta +0.218 = the
single largest day-over-day improvement of the 11 sectors** — the money turned toward Energy on
07-21, *before* today's re-escalation. But eqflow is only +0.125: **mega-cap-led, breadth thin**.
The correction MACRO could not see: **the flow is concentrated in refining, not E&P or services.**
VLO/MPC/PSX run RS20 **+25 to +29** and RS60 **+27 to +39** (vs SPY) with OBV accumulating, while
SLB is −3.4/−20.5 and the midstream names (KMI, WMB) are flat. The cycle registry calls this cycle
"oil-refining (Hormuz + Russia crack)" — **the tape agrees with the registry's node, not with a
generic energy long.**

**CONTRADICTS · Health Care (matrix UW).** Health Care is the **#1 sector on wflow (+0.453)** with the
board's best green:red balance and 2 of 11 greens (ABT, UNH); JNJ, MRK, ABBV, LLY, TMO all carry
positive flow and OBV accumulation. **The matrix is UW; the money was buying.** ★ Resolution: this is
a *timing* contradiction, not a factual one — the sweep closes 07-21, and the **up-to-200% pharma
tariff was announced 07-22 [11 articles / 7 outlets]**, landing on top of freshly-built defensive
positioning. That combination (crowded-fresh长 + a same-day policy shock) is the highest-information
cell on the board, which is why HLTH goes to DEEP as a **falsification target**, not as a long.
Note the internal split even pre-news: PFE (−0.390, 🔴 OBV distributing, RS60 −12.1) and ISRG
(−13.6/−32.5) were already being sold — this was never a whole-sector bid.

**CONFIRMS the refusal to tilt · Information Technology (matrix N, held flat into the binary).**
**0 greens of 56 · 29 reds · eqflow −0.289 — the worst breadth on the board.** MACRO declined to tilt
IT long into tonight's print; the flow says the same thing far more bluntly.
★ **And it exposes the sector label as the wrong unit (W5).** Inside IT, over 20 days vs SPY:
**MU −20.4, SNDK −30.6, WDC −25.7, INTC −25.7, LRCX −21.9, KLAC −19.7** (all 🔴분산, OBV distributing)
against **AAPL +9.8, MSFT +7.8**. That is a **~40pp intra-sector spread vs the same benchmark**, and
the memory/equipment complex sits on the wrong side of it — *while its own RS60 is still +30 to +96*.
**Level high, 20-day rate rolling over, OBV distributing: the tape is already doing to memory what
the standing view says the margin cycle will do.** The 07-21 "+12–14% memory rally" was a bounce
inside a 20-day drawdown vs SPY, not a trend — anyone citing it as a turn is quoting one day (S1).

**CONTRADICTS · Industrials (matrix N+, on nuclear/defense order flow).** wflow **−0.167 (#9)** with
**17 reds of 50**. The two greens (CTAS, TRI) are business services, not defense. Among the defense
names only GD (+0.508) and RTX (+0.444) carry positive flow; NOC is RS60 −18.4 and the electrical/
power-equipment node is outright negative (ETN −0.506, GEV −0.322). **The matrix's N+ rests on
narrative order flow that the tape does not yet show.** ROTATION should either cut Industrials to N-
or require DEEP to prove the defense sub-node on its own numbers.

**CONFIRMS · Materials (UW, worst on both axes) · Real Estate (UW, 0 green / 5 red of 12) ·
Utilities (N-, delta −0.183, the worst day-over-day deterioration on the board; CEG 🔴).** The three
duration/late-cycle UWs are confirmed by flow with no dissent.

**INVERTED, worth one line · Consumer Staples.** wflow −0.131 but **eqflow +0.129** — breadth positive
while mega-caps are sold. Same inversion shape as Comm Services (wflow −0.271, eqflow +0.003,
**delta +0.145 = 2nd-best improvement**), where the negative wflow *is* GOOGL (−0.428) being de-risked
into its own print while META (+0.578) is bid. GOOGL's A-grade axes carry the claim — **RS20 −1.2 and
RS60 −3.2 vs SPY, both negative** — with OBV distributing only as agreement, not as the finding (D6).
**Comm Services' sector number is one pre-earnings name.**

## 3. Shortlist composition — the absences, diagnosed

Shortlist = 11 names (`US_LIVE_SHORTLIST.json`), and the composition is the finding: **6 Financials,
2 Health Care, 2 Industrials(services), 1 Comm Services. Zero Energy. Zero Info Tech.**

**The Energy zero is a mechanism artifact, and this run measured the mechanism.** The 🟢 gate is
`green≥3 AND has_conviction`, over four axes: OBV 매집 · RS20>0 · vol_surge≥1.2 · news velocity≥1.2.
**On the US path news velocity is always `None`** (`vel=None` on all 300 rows — there is no US news
axis wired into `module_flow`). So a four-axis majority silently becomes a **three-axis unanimity**:
a US name must fire OBV **and** RS20 **and** a volume surge to be tagged 🟢.

Measured consequence: **99 of 300 names pass OBV-accumulating **and** RS20>0 and are blocked solely by
`vol_surge < 1.2`** — Financials 23, Health Care 18, IT 13, Industrials 10, Staples 10, **Energy 4**.
The Energy 4 are exactly **XOM, VLO, MPC, PSX** — the refining complex the sector read above is built
on. Their volume was ordinary; their relative strength was not.

The distortion this produces is concrete: **T (AT&T) is tagged 🟢 on RS20 +0.2 with a 1.53 volume
surge, while VLO is 🟡 on RS20 +28.6 with a 1.04 surge.** The tag is preferring a one-day volume spike
over a 20-day relative-strength reading — i.e. **a C-grade axis is outranking an A-grade one**
(`handoff/RESEARCH.md` D6; open code defect **D11**). Per the interpretation-layer rule this run:

- **Every US 🟢 on this board is OBV-gated** (all 11 carry `obv_state=매집`; `has_conviction` cannot be
  satisfied any other way when `vel` is None). They are therefore read as **🟡 with a stated
  agreement/disagreement from RS**, not as 🟢.
- **Agreement (RS20 and RS60 both positive):** PYPL, CTAS, TRV, ABT, CB, USB, UNH, STT — these survive
  the downgrade as genuine.
- **Disagreement — do not carry:** **T** (RS20 +0.2, **RS60 −22.0**) and EA (RS60 −2.4); TRI is mixed
  (RS20 +18.0, RS60 −5.0). AT&T is a volume-surge tag on a name that has underperformed SPY by 22%
  over 60 days; it is not a flow signal.
- **The IT zero is real, not an artifact** — 0 of 56 pass even OBV+RS20 with a surge, and 29 are 🔴.

Short-pressure axis (FINRA z, the only US flow proxy): one clean-rise name (**TRV**, z −2.00,
low-short/covering) and one crowded-short (**CB**, z +1.61 — squeeze fuel conditional on a turn,
never a reason on its own). Everything else is 정상숏. The axis added nothing this run and is
reported as such rather than dressed up.

## 4. Cycle-exposure GAP → handed to ALPHA

`CYCLE_EXPOSURE.json` (book asof today, KIS read-only): **🚨 GAP on rank-2 "Energy / oil-refining
(Hormuz + Russia crack)" — epicenter exposure 0.0% vs 8.0% required (−8.00pp).** The book touches the
cycle only through adjacent/fuel names (KMI, LNG): beta to the consequence, none to the engine.
Rank-1 AI-compute is compliant (12.25% vs 12.0% required, via AVGO/NVDA/TSM); rank-3 rearmament has
no threshold set (RTX 9.49%).

**This GAP and this stage's flow read point at the same node from two directions** — the registry says
the book has no refining epicenter; the tape says refining is where 07-21's money went (RS20 +25~29
vs SPY, OBV accumulating) and the 🟢 filter structurally cannot surface it. Handed to ALPHA's action
bracket. ⚠ A 🚨 GAP is a *coverage* statement about the book, **not** a buy signal, and today's
run has an unresolved oil oscillation (MACRO P4 both branches) sitting on top of it.

---

### Deltas this stage found that the JSONs cannot state
1. Energy money is **refining-specific**, and the 🟢 filter is structurally blind to it (99-name
   `vol_surge` block measured, Energy's 4 named).
2. Health Care flow **contradicts** the matrix — and the contradiction is dated: flow closes 07-21,
   the tariff headline is 07-22.
3. Financials confirm **breadth-led**, but in insurers/custody/payments, **not** in GS/MS/C.
4. IT's ~40pp intra-sector RS20 spread vs SPY makes "semiconductors" an unusable unit of analysis.
5. Industrials' N+ has **no flow support**; the defense sub-node must be proven separately.
6. On the US path the 🟢 tag is a **volume-surge count**, not a flow count — a US 🟢 count is not
   comparable to a KR 🟢 count, and neither is a "green ignition" claim built from it.
