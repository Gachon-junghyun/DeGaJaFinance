# SECTOR_DEEP_HLTH — Health Care (HLTH) deep-dive · 2026-07-21 (Tue)

> **Stage 6 / L1·DEEP.** Runtime `--market us`, English-pure, news scope `foreign` on every call.
> **Inputs reread from disk:** `MACRO_REPORT.md` §4/§4x(d) · `SWEEP_READ.md` §1 · `EVENT_ALPHA.md`
> (HLTH mentioned only in the raw event feed, not a card) · `SECTOR_ROTATION.md` §2(b) · `BLINDSPOT_PREMORTEM.md`
> FINDING 0 (the correlation constraint) and LENS 1 LEG 3 (the RE/WELL finding). **Baseline: `llm_outputs/2026-07-19/industry_US/SECTOR_DEEP_HLTH.md`.**
>
> ★ **CONTINUOUS TRACK, third consecutive deep (07-17 → 07-19 → 07-21).** This file **leads with the
> DELTA**. The 07-19 map — the 8→7-node value-chain re-derivation, the 32-name player universe, the
> UNH/HUM 10-K anchors, the MLR-print discovery, the three committed verdicts (§6-A hedge/diversifier
> split, §6-B breadth, §6-C REIT reassignment withdrawn) — is **carried BY REFERENCE and NOT re-printed.**
> Only what MOVED, plus the two questions this run's mandate names explicitly, are re-derived below.
>
> ⚠ **asof = 2026-07-20 close** (the tape) / **2026-07-17** (FRED rates, one session behind — per MACRO).
> The 07-21 news pool is **14 articles → 0 events**; nothing below claims "today."
>
> **Zero buy/sell calls. Zero sizing.** (P4 — BET owns that.)

---

## §0 ★ DELTA since 2026-07-19 — lead with it

**Δ1 — ★★ MACRO reversed its OWN 07-19 promotion. HLTH moved OW → Neutral ("hedge role"), citing
evidence this file must adjudicate.** MACRO §4: *"Downgraded on its own evidence. XLV RS20 +7.2% and
accumulating — but it was the worst sector on 07-20 (−1.14%) on a +$550B risk-on day, and −1.34%/5d.
That is the definition of a hedge, confirming 07-19 DRIFT's β −0.16 finding."* ROTATION §2(b) put it
back to OW but relabeled it, and handed DEEP one line to answer: *"does this desk carry hedges as OW
allocations, or only orthogonal names?"* **§6 below answers it directly, with fresh numbers, not the
07-19 numbers re-quoted.**

**Δ2 — ★★ HUM's short interest INVERTED. The 07-19 verdict's sole orthogonal vehicle just became the
sector's single most crowded short.** FINRA Reg SHO, asof 07-20:

| | 07-19 (asof 07-17) | **07-21 (asof 07-20)** |
|---|---|---|
| HUM short% | 34.7% | **53.4%** |
| HUM base20 | — | 38.7% |
| HUM z | **−0.60** (lowest short intensity in the leg) | ★★ **+1.97 — 극단 (crowded-short, self-base-relative extreme)** |
| HUM 5v5 trend | +0.7▲ | +1.0▲ (still building) |

**This is the largest single measured change in the file.** 07-19's diversifier case for HUM rested
explicitly on *"shorts at z −0.60 and short% 34.7% — the lowest in the leg"* as evidence the +78.5%/60d
run was **not** crowded. Two trading days later the same metric reads **+1.97**, the most extreme
short-pressure reading of any name checked this run (UNH +0.83, ABT +0.70, LLY +0.24, VRTX −1.28,
ISRG −1.65). **The orthogonality thesis and the crowding-free thesis were two separate legs of the same
07-19 argument. One of them just broke.** §6 treats this as a first-class finding, not a footnote.

**Δ3 — UNH's chart-level signal flipped against its own flow tag.** `module_flow` still tags UNH
🟢가속/매집 (OBV accumulating, RS20 +5.8%, RS60 +14.9%, vol 1.20×). But `module_chart UNH --read`
(different window/method) shows: **OBV 분배(매도압력↑), 20d slope −19%; bearish divergence (price
higher-high, RSI lower-high); turn-verdict PULLBACK-TO-SUPPORT, not CONFIRMED-TURN.** ABT and CVS, by
contrast, both read **CONFIRMED-TURN** on the same tool. **Two independent flow methods now disagree
about UNH specifically — the name MACRO and 07-19 both used as the thesis's proof case.** Neither
overrides the other; both are reported, and the disagreement is itself the signal §6 uses.

**Δ4 — The correlation constraint PREMORTEM's FINDING 0 raised is CONFIRMED at 90d and WORSE at 20d.**
`yfinance`, computed fresh this run (§6-B has the full table): 90d sector-ETF pairwise correlations
match PREMORTEM's within noise (XLV–XLRE 0.63 vs their 0.65). **But the 20d window — the freshest,
decision-relevant one — shows every pair at 0.67–0.80**, materially tighter than the 90d average of
≈0.57. **The "one bet" PREMORTEM flagged is currently MORE concentrated than its own headline number
says**, at the exact moment MACRO's hike-branch kill-switch (2s10s <+30bp, now +37bp) is 7bp away.

**Δ5 — Sub-industry breadth held and grew.** Sweep: HLTH wflow **+0.478** (was +0.429), eqflow
**+0.361** (was +0.314), day/day Δ **+0.049**, rank **#1 of 11, unchanged**, breadth 0.06, **2 of the
market's 12 universe-wide 🟢 names are here** (ABT, UNH — both on the LIVE shortlist). **This is the
third independent confirmation of the same fact** (SWEEP: *"the third independent confirmation of
MACRO's P7 downgrade"*): flow and price disagree by construction, because flow measures accumulation
and price measures the trade already having happened.

**Δ6 — Five runs, zero HLTH narrative thread — now stated by MACRO as evidence, not just an absence.**
MACRO §3: *"P7-HLTH has no thread at all — five runs in, health care has never generated a multi-day
narrative, which is itself evidence for the 'hedge, not destination' read."* This deep concurs and
extends it in §6: **an accumulation with no story attached is the textbook shape of a positioning move,
not a conviction trade** — the news axis (chain-hop, fts) finds nothing to attach it to below, again.

**Δ7 — Ignition names re-sorted. ABT and CVS both confirmed the turn; ISRG deepened, then a short-cover
signal appeared under it.** ABT: RS20 +15.6% (was +13.4%), OBV +89%/20d slope, CONFIRMED-TURN.
CVS: RS20 +10.1% (module_flow) / +8.1%→ now higher, OBV +66%/20d, **also CONFIRMED-TURN**, still at
0% off its YTD high, short z **1.34** (was 1.40 — essentially unchanged, still elevated). ISRG: RS20
−12.6% to −14.9% depending on tool (worse), vol surge 2.27× (was 2.06×, still the highest in the
bucket), **but short-vol z flipped to −1.65 (🟢 공매도급감 — shorts covering)** — the first sign the
short side of §4's bottleneck mechanism may be nearing exhaustion, not yet a reversal.

### What is CARRIED UNCHANGED, by reference (NOT re-printed)
- The **7-node value chain** with providers/facilities as the binding bottleneck — `SECTOR_DEEP_HLTH.md`
  (07-19) §4. Re-touched only where the bottleneck's confirming names moved (Δ7 above; HCA below).
- **IR anchors** UNH 10-K (0000731766-26-000062) and HUM 10-K (0000049071-26-000009) — 07-19 §3.
  Unchanged; not re-pulled this run (no new filing in window).
- The **MFN drug-pricing story** and the **MLR print's thin denominator** — 07-19 §3. Re-verified below
  (§5): the denominator has **not** expanded in two days.
- The **WELL/VTR REIT reassignment WITHDRAWN** verdict — 07-19 §6-C. Not re-litigated in full; PREMORTEM
  LENS 1 LEG 3 independently reached the same structural conclusion from a different method (WELL/SPG
  duration money, not a datacenter-REIT story) and folded RE into the same duration sleeve this file's
  §6-B treats as one bet — **convergent confirmation, cited not re-derived.**
- The 07-19 negative chain-hop findings and the CNC/MOH sub-threshold naming — §2/§5 below re-confirm
  rather than re-argue.

---

## §1 Flow — sub-leg split, this run's numbers

`module_flow` + `scripts/us_flow.py`, **asof 2026-07-20 close** (short-vol data), tape 07-20:

| Ticker | Sub-leg | Flow tag | OBV | RS20 | RS60 | Vol surge | Short z | 5v5 |
|---|---|---|---|---|---|---|---|---|
| **UNH** | Managed care | 🟢가속 (flow) / PULLBACK (chart) | 매집(flow)/**분배**(chart) | +5.8% | +14.9% | 1.20× | +0.83 | −5.3▼ |
| **HUM** | Managed care | 🟡중립 | 매집, CONFIRMED-TURN-adjacent | +11.0% | +78.8% | 0.98× | ★★ **+1.97 극단** | +1.0▲ |
| **CVS** | Managed care | 🟡중립 | 매집, **CONFIRMED-TURN** | +10.1% | +36.5% | 0.99× | +1.34 | +7.4▲ |
| ELV | Managed care | 🟡중립 | 매집 | −1.0% | +12.1% | 1.38× | +0.22 (was **−2.37** 🟢) | +3.2▲ |
| CI | Managed care | 🟡중립 | 중립 | +2.3% | −1.0% | 1.26× | −0.16 | −2.0▼ |
| **ABT** | Med-tech | 🟢가속, **CONFIRMED-TURN** | 매집 | +15.6% | +6.5% | 1.40× | +0.70 | −8.7▼ |
| **ISRG** | Med-tech | 🟡중립 | 중립 | −12.6% | −31.3% | ★2.27× | ★ **−1.65 🟢공매도급감** | −8.3▼ |
| BSX | Med-tech | 🔴분산 | 분산 | −2.7% | **−36.9%** | 0.77× | +1.12 | +1.2▲ |
| HCA | Providers/facilities | 🟡중립 | 중립 | −0.6% | −25.8% | 1.29× | **−1.54 🟢** | −6.7▼ |
| JNJ | Pharma | 🟡중립 | 매집 | +9.6% | +5.7% | 1.16× | — | — |
| MRK | Pharma | 🟡중립 | 매집 | +9.9% | +5.9% | 1.01× | — | — |
| PFE | Pharma | 🟡중립 | **분산** | −1.2% | −12.0% | 0.99× | — | — |
| LLY | Pharma | 🟡중립 | 매집 | +5.0% | +20.1% | 0.81× | +0.24 | +8.7▲ |
| VRTX | Biotech | 🟡중립 | 매집 | +7.0% | +5.4% | 0.79× | −1.28 | −4.7▼ |
| TMO | Tools | 🟡중립 | 매집 | +13.9% | −2.0% | 0.76× | — | — |
| DHR | Tools | 🟡중립 | 매집 | +14.1% | +4.9% | 1.09× | — | — |
| AMGN | Biotech | 🟡중립 | 매집 | +8.5% | +0.9% | 0.80× | — | — |
| GILD | Biotech | 🟡중립 | 매집 | +8.3% | −4.1% | 0.73× | — | — |
| BMY | Biotech | 🟡중립 | 매집 | +12.0% | −2.0% | 0.96× | — | — |
| WELL | *(REIT, §6-B cross-ref)* | 🟡중립 | 매집 | +19.1% | +18.3% | ⚠0.74× | ⚠**+1.34** (was +0.08) | −1.4▼ |
| VTR | *(REIT, §6-B cross-ref)* | 🟡중립 | 매집 | +18.6% | +15.8% | ⚠0.66× | +0.22 (was +1.12) | +0.8▲ |
| XLV | sector | 🟡중립 | 매집 | +7.2% | +4.5% | 0.92× | — | — |

**Read, stated against the narrative rather than around it (07-19's discipline, continued):**
- **The clean-positioning read (UNH — lowest crowding, shorts leaving) still holds on FINRA, but the
  chart method now disagrees about the same name (Δ3).** Two tools, two answers — reported both.
- **The crowded-defensive read has swapped names.** 07-19 found it at CVS/VTR/DOC. This run it is
  **HUM**, and by a wide margin (+1.97 is the most extreme z measured in this file, in either run).
  ELV's short-covering signal from 07-19 (z −2.37) also reverted to normal (+0.22) — the "shorts
  fleeing the sector" read is narrowing, not broadening.
- **ISRG's short-cover (z −1.65) against continuing price/RS weakness (−14.9% RS60, 2.27× volume) is
  the classic late-stage-decline signature** — worth a dated track KPI (§7), not yet a reversal call.
- **HCA's short-cover (z −1.54) is new this run** and sits at the bottleneck node §4 identifies —
  tracked, not yet interpreted (§7).

---

## §2 Players — carried by reference

Universe = the 32-name `us_top300` HLTH set, unchanged bound, `SECTOR_DEEP_HLTH.md` (07-19) §2. Not
re-printed in full; the flow board's **ordering** moved (ABT/CVS both now CONFIRMED-TURN on chart,
Δ7), the **membership and bound rule** did not.

Sub-threshold small-caps carried forward unchanged: **CNC (Centene), MOH (Molina)** — still surfacing
only inside index-move quote-table recaps (`economictimes` 07-20 European-shares wraps listing
*"Centene 66.44 (+3.99%)" / "Humana 400.00 (+3.50%)"*, checked this run via `fts search Humana short`),
**not independent article subjects.** Still logged sub-threshold, not cleared, two runs running.

Cross-sector REIT set carried for §6 adjudication only: **WELL, VTR** (flow-checked above); DOC, CTRE,
OHI, NHI, SBRA not re-pulled this run (PREMORTEM LENS 1 LEG 3 already re-verified the WELL/SPG-not-AI
reading independently — §0 Δ-carry note).

---

## §3 IR anchor — carried, with the one open flag re-checked

**UNH 10-K** (0000731766-26-000062) and **HUM 10-K** (0000049071-26-000009) — unchanged, `SECTOR_DEEP_HLTH.md`
(07-19) §3. No new filing in window; not re-pulled.

**The MLR print's denominator — re-checked, not assumed stale:**
`fts search "medical loss ratio" MLR --days 7 --mode or` → **2 matches**, same count as 07-19: the
SeekingAlpha 07-18 UNH piece (*"Medical Loss Ratio decreased by 270 bps to 86.7%"*) and one unrelated
BBC hit on "MLRS" (multiple launch rocket systems — a term-collision, not health care). **The real
denominator is still ONE article, unchanged after two days.** ★ The thesis remains un-crowded by the
news axis's own measure — consistent with Δ6's "no narrative thread in five runs" finding, now
cross-confirmed by a second tool.

**The CFO "stark warning" flag — still unresolved, re-checked:**
`fts search UnitedHealth CFO warning --days 7 --mode and` → still **2 matches**: TheStreet 07-19,
**title-only** (body still not retrievable), and an unrelated CNBC "Morning Squawk" digest that merely
mentions UnitedHealth in passing. **Logged `[blank]` a second run** — not resolved, not escalated,
carried exactly as 07-19 left it.

**New body-read this run, from the prompt's 07-20 headline list — checked, not just quoted:**
- *"Novartis faces drug pipeline test with valuation premium in focus"* [yahoo_finance 07-20] — the
  retrieved body is **the headline restated**, no incremental fact beyond the title (checked via `fts
  search Novartis pipeline valuation`, 1 match, body = title). **Not a HLTH-universe name; not promotable.**
- *"Why Vertex Pharmaceuticals (VRTX) Dipped More Than Broader Market Today"* — same pattern, body =
  title, **no cause given**. VRTX's own flow (§1) shows nothing unusual (매집, RS20 +7.0%, short z
  −1.28 normal) — **the headline is a name-level noise item, not a signal**, and is reported as such
  rather than assigned a cause the source doesn't provide.
- Samsung Biologics/PolyPeptide ($1.81bn) and Bristol-Myers/Nvidia (AI computing purchase) are both
  **outside `us_top300` or not HLTH-chain-relevant** (Samsung Biologics is a KR-listed CDMO; the Nvidia
  purchase is a BMY R&D-tooling capex item, not a chain-node event) — noted, not chased.

---

## §4 Value-chain map — carried, bottleneck re-confirmed with fresh numbers

Map unchanged from 07-19 §4 (7 nodes, providers/facilities = binding bottleneck because volume is
absent, not because demand is weak). Re-verified at the bottleneck node this run:

```
 ... upstream nodes (tailwinds, unchanged) ...  →   PAYERS/PBM (winner)   →   providers/facilities (★BOTTLENECK)
                                                     UNH RS60 +14.9%           HCA RS60 −25.8%, z −1.54🟢(new)
                                                     HUM RS60 +78.8%, z+1.97★  ISRG RS60 −31.3%, vol 2.27×, z −1.65🟢(new)
                                                     CVS RS60 +36.5%           BSX RS60 −36.9% (deepened), z +1.12
```

**The mechanism 07-19 named — MLR down = fewer claims paid = the providers/procedure-vendors' volume
loss, one utilization cycle, two P&Ls, opposite signs — still holds and is now confirmed by a THIRD
independent name.** BSX's RS60 deepened to −36.9% (was −31.6%) on the same read. **New this run: both
bottleneck-side names (HCA, ISRG) show short-covering (z −1.54, −1.65) even as their relative
strength stays negative or worsens.** That is not yet a reversal signal — short-covering into continued
RS weakness is as consistent with "the short thesis already got paid and is de-risking" as with "a
bottom is forming." **Flagged as a dated track KPI (§7), not resolved as either.**

---

## §5 Chain-hop candidates — re-run, still empty

`module_news_data chain-hop "managed care" "medical loss ratio" "drug pricing" --days 14 --scope foreign`
→ **26 articles scanned, headline-named top-9 only** (UNH, LLY, ABBV, PFE, CVS, BMY, ELV, JNJ, SO — all
already-crowded names). **Candidate section: EMPTY.** Zero names clear the "title 0× + body proximity
≥2×" bar. **Third consecutive run with zero promotable chain-hop candidates.**

★ **The tool-floor limitation named in 07-19 still applies and is re-stated, not re-argued:** `us_top300`
has no small-cap slot for CNC/MOH, so they remain structurally invisible to this instrument regardless
of how the news window moves. **The absence is partly the instrument's, not only the sector's — but two
runs of zero real candidates from a 32-name universe with the market's #1 flow ranking is itself a
data point for §6's hedge-vs-destination read: there is no unexplored corner of this thesis waiting to
be chain-hopped into. It is fully mapped and thin.**

---

## §6 ★★ ANSWERS — the two questions this run's mandate requires

### §6-Q1 — HEDGE OR DESTINATION? Named per ticker.

**The honest answer is unchanged in shape from 07-19 (both, split by name) but the split has moved, and
one name's status is now worse than 07-19 knew.**

**Sector level (XLV) = HEDGE, more clearly than on 07-19.** The evidence MACRO used to downgrade is a
*price* fact, not a correlation-math fact, and it is a stronger falsification method than 07-19 had
available: **XLV was the worst-performing sector on 07-20, a session that added $550B of US market cap
on ceasefire hopes, while its own flow tag stayed 매집/RS20 +7.2%.** Accumulating money that gives back
the hardest on the single best risk-on day of the window **is the live version of the β −0.16 / up-day
excess −0.74% finding 07-19 only had in backtest form.** Recomputed this run (§6-Q2 table): **XLV's
beta to SPY is −0.86 in the 20-day window** (vs −0.17 at 60d) — **the hedge behavior is intensifying in
the freshest data, not fading.** ★ **Compounding this: five runs and zero multi-day narrative thread
(Δ6).** Sustained accumulation with no story attached is what a positioning hedge looks like from the
outside — a destination trade generates coverage; a portfolio-construction trade does not.

**Named as HEDGE:** **XLV (the vehicle), WELL, VTR** (duration-flavored, β −0.73/−0.79 per 07-19,
short-z now rising at WELL specifically — z +1.34 this run vs +0.08 on 07-19, i.e. **crowding is now
building on the hedge leg too**), and, newly this run, **UNH is reclassified from "split" toward
HEDGE.** 07-19 called UNH's *thesis* independent but its *flow* hedge-shaped. This run's chart read
(Δ3: OBV distributing, bearish divergence, PULLBACK not CONFIRMED-TURN) and its correlation profile
(§6-Q2: corr to XLRE risen to 0.60 at 20d, up from a lower base) both move the same direction — **UNH
is trading more like the duration sleeve, not less, two days later.**

**Named as DESTINATION:** **ABT** — unchanged from 07-19's finding that the ignition is a broken-name
rebound (still −21% off its own YTD high per 07-19's ATR read, still unrelated to the MLR cycle) but
now **CONFIRMED-TURN on the chart tool**, a genuine technical event, not MLR-adjacent. **CVS**, newly
confirmed this run — also flipped to CONFIRMED-TURN, but sits at its exact YTD high with an unchanged
elevated short-z (1.34) — a destination trade the market is already fighting over, not an early one.

**Named as DESTINATION-BUT-NOW-CROWDED: HUM, and this is the file's central finding.** 07-19 built the
entire diversifier case on HUM being both orthogonal (correlation) AND uncrowded (short interest). The
correlation leg still holds (§6-Q2). **The uncrowded leg broke in two trading days** — short z went
from −0.60 (cleanest in the sector) to **+1.97 (most extreme reading in this file)**. This does not
kill HUM as an independent driver — it may mean the market is now betting *against* the MLR cycle at
HUM specifically, which is a different and testable claim, not a refutation of the correlation math.
**But it means "quiet, uncrowded accumulation" is no longer an accurate description of HUM, and any
downstream stage citing 07-19's "shorts have simply abandoned it" line is citing a dead number** —
the same discipline 07-19 applied to ISRG on 07-17's numbers.

> **Verdict: HLTH is both, split as: HEDGE (XLV, WELL, VTR, and now UNH) vs. DESTINATION (ABT — clean;
> CVS — confirmed but extended/crowded; HUM — the cycle's real vehicle, but no longer the clean,
> uncrowded position 07-19 described).** The desk's OW, if carried at the sector level, is carrying a
> hedge. If carried at the name level, the destination names have all either extended (CVS, ABT) or
> become newly crowded (HUM) since 07-19 — **there is no clean, early, uncrowded destination expression
> left in this universe that this run can point to.**

### §6-Q2 — ★★ THE CORRELATION CONSTRAINT — verified, with per-name numbers

`yfinance`, computed fresh (not reused from PREMORTEM), 6-month history, three windows:

**Sector-ETF pairwise correlation — confirms FINDING 0 and shows it tightening in the fresh window:**

| Pair | 90d (PREMORTEM cited) | 90d (this run) | 60d | **20d** |
|---|---|---|---|---|
| XLV–XLRE | 0.65 | 0.626 | 0.666 | ★ **0.801** |
| XLU–XLRE | 0.65 | 0.661 | 0.667 | 0.673 |
| XLP–XLRE | 0.63 | 0.620 | 0.648 | ★ **0.742** |
| XLV–XLP | 0.57 | 0.546 | 0.578 | ★ **0.716** |
| XLU–XLP | 0.49 | 0.488 | 0.491 | 0.677 |
| XLU–XLV | 0.46 | 0.406 | 0.458 | ★ **0.694** |
| **avg** | ≈0.57 | ≈0.56 | ≈0.58 | ★ **≈0.72** |

**The 90d/60d numbers match PREMORTEM within noise — the constraint is real, not an artifact of their
window choice. The 20d number is the finding this file adds: the average pairwise correlation has
risen from ≈0.57 to ≈0.72 in the most recent month.** The four "independent" verdicts (HLTH OW, RE
Neutral, UTIL Neutral, STPL Neutral) are **currently trading MORE like one position than the 90-day
average would suggest**, at the exact moment the kill-switch (2s10s <+30bp, now +37bp) is 7bp away.

**Per-name correlation to SPY, XLRE, TLT — the answer to "which names break the constraint":**

| Name | corr SPY 60d | corr SPY 20d | corr **XLRE** 60d | corr **XLRE** 20d | β(SPY) 60d | β(SPY) 20d | Up-day excess 60d | Down-day excess 60d |
|---|---|---|---|---|---|---|---|---|
| **XLV** | −0.12 | −0.43 | 0.67 | ★0.80 | −0.17 | −0.86 | −0.75% | +1.02% |
| **UNH** | −0.11 | −0.53 | 0.39 | ★**0.60** | −0.21 | −1.23 | −0.60% | +1.19% |
| ★ **HUM** | **0.06** | **−0.03** | ★★ **−0.13** | ★★ **−0.33** | 0.19 | −0.10 | **+0.49%** | +1.54% |
| ABT | −0.18 | −0.40 | 0.41 | 0.58 | −0.49 | −1.70 | −0.97% | +1.38% |
| CVS | −0.05 | −0.45 | 0.31 | 0.39 | −0.11 | −0.88 | −0.35% | +1.52% |
| ELV | −0.10 | −0.26 | 0.16 | 0.11 | −0.31 | −1.20 | −0.86% | +1.44% |
| CI | −0.21 | −0.26 | 0.33 | 0.12 | −0.49 | −0.73 | −1.04% | +1.19% |
| ISRG | 0.17 | 0.15 | 0.34 | 0.32 | 0.59 | 0.91 | −1.20% | +0.17% |
| VRTX | 0.06 | −0.02 | 0.35 | 0.49 | 0.14 | −0.06 | −0.63% | +0.92% |
| JNJ | −0.35 | −0.51 | 0.60 | 0.67 | −0.68 | −1.49 | −1.02% | +1.38% |
| MRK | −0.20 | −0.35 | 0.45 | 0.66 | −0.48 | −1.14 | −0.74% | +1.08% |

**Answer: exactly ONE name breaks the constraint — HUM, and by a wide margin.** Every other name in the
11-name scan carries a **positive** correlation to XLRE (0.11 to 0.80). **HUM alone is negative in both
windows (−0.13 at 60d, −0.33 at 20d) — it is the only HLTH name in this file that moves opposite the
duration sleeve, not merely uncorrelated with it.** Its beta and SPY-correlation are also the closest
to zero of any name tested, and it retains a positive up-day excess (+0.49%/60d) that every other name
in the table lacks. **On the correlation math alone, HUM can still be OW'd as an independent position.**

**But §6-Q1's finding travels with this answer and cannot be dropped from it: the same name that clears
the correlation bar is the name whose short interest just went from cleanest-in-sector to most-crowded-
in-file (Δ2).** A name can be statistically independent of the correlated sleeve and simultaneously be
a crowded, two-sided bet on its own idiosyncratic driver (the MLR cycle). Those are different risks,
and both are true of HUM at once.

**ABT and UNH — the two names carrying most of this file's flow signal — do NOT break the constraint.**
ABT's XLRE correlation (0.41/0.58) is actually **higher than XLV's own 60d reading**, despite being a
name-specific technical rebound with no duration-rate logic behind it at all — a reminder that
correlation in a risk-off tape can rise for reasons unrelated to the named mechanism. UNH's XLRE
correlation **rose from an implicitly lower 07-19 base to 0.60 at 20d** — consistent with §6-Q1's
finding that UNH is moving toward the hedge/duration sleeve, not away from it.

> **Verdict: the correlation constraint holds and has tightened. If this desk wants an HLTH position that
> is genuinely NOT the same bet as its RE/UTIL/STPL exposure, the correlation math names exactly one
> vehicle — HUM — and that same vehicle now carries a crowding risk (z +1.97) that did not exist two
> runs ago. There is no free lunch here: independence and cleanliness used to both point to HUM; now only
> independence does.**

---

## §7 Track KPIs + anti-signals — dated observables

**Track:**
1. ★★ **HUM short-vol z: +1.97 now. If it keeps rising (>+2.5) while price keeps running, this is a
   short-squeeze setup, not a diversifier holding steady. If it reverts toward 07-19's −0.60 within a
   week, the crowding was transient and the 07-19 read stands.** No date guessed; watch next 3-5 sessions.
2. ★ **UNH chart-vs-flow disagreement (Δ3): watch for `module_chart UNH --read` to either confirm
   CONFIRMED-TURN (bull case resolves) or for `module_flow`'s OBV to flip to 분산 (bear case resolves).
   Currently split — this is the file's most direct near-term falsifier of §6-Q1's UNH reclassification.**
3. **The correlation constraint's 20d reading (≈0.72 avg pairwise) vs 90d (≈0.56): if it reverts toward
   the 90d average next run, FINDING 0's urgency eases. If it holds >0.70, the "one bet" framing should
   govern sizing regardless of HLTH's own sector-level performance.**
4. **HCA and ISRG short-covering (z −1.54 / −1.65) against continuing RS weakness (−25.8% / −31.3%):
   either the bottleneck's short side is exhausting (watch for RS to stabilize) or shorts are just
   taking profit mid-decline (watch for RS to keep falling with volume). Unresolved, dated next run.**
5. **MLR news denominator: still 1 real article after 2 days (§3).** Expansion = the trade is being
   discovered publicly; continued silence = still-un-crowded-by-narrative, consistent with Δ6.
6. **CFO "stark warning" [TheStreet 07-19] — still `[blank]`, body unretrievable a second run.** Retrieve
   before the next UNH print or drop the flag as unresolvable.
7. **XLV's 20d beta to SPY: −0.86 now vs −0.17 at 60d.** If this reverts toward zero, the hedge-intensity
   finding weakens. If it deepens further negative, §6-Q1's HEDGE case strengthens further.
8. **The Managed Health Care sub-industry average (07-19: +0.440, from a 0.201 base): not independently
   re-pulled this run at the sub-industry-average level** — logged as a gap, re-check next run.

**Anti-signals:**
- ⚑ **HUM short z >+2.5 with price still rising** — squeeze-fuel-into-distribution risk, not a clean
  diversifier; would demand re-labeling HUM as crowded-momentum rather than orthogonal-quiet.
- ⚑ **UNH's chart OBV confirms 분산 (not just PULLBACK) on rising volume** — would settle Δ3 toward the
  bear case and strengthen §6-Q1's hedge reclassification.
- ⚑ **MLR print reverses (rises) at the next payer earnings** — the direct kill on the whole cycle,
  unchanged from 07-19.
- ⚑ **20d sector-ETF correlations stay >0.70 for a third run** — would mean FINDING 0's constraint is a
  regime feature, not a transient tightening, and should govern position sizing as such.
- ⚑ **WELL short z keeps rising from 1.34** (was 0.08 on 07-19) — the "nobody is defending this level"
  read from 07-19 §6-C would gain a second confirming metric beyond low volume.
- ⚑ **A chain-hop or fts pass finally returns a real HLTH candidate** — would break Δ6/§5's "fully
  mapped and thin" finding and require re-opening the small-cap search.

---

**EXIT CHECK:** ✅ **Delta-led**, seven measured changes (MACRO's own reversal on XLV price action; HUM's
short-z inversion +1.97; UNH chart/flow disagreement; the correlation constraint's 20d tightening;
breadth growth; ABT/CVS chart-confirmed turns with ISRG/HCA short-cover; the MLR-denominator and
zero-thread findings re-verified unchanged) · ✅ **§1 flow measured fresh**, sub-leg split, short-z
divergence stated against the narrative (HUM now the crowded name, not CVS/VTR) · ✅ **§2/§3 carried by
reference** with the two open flags (CNC/MOH sub-threshold, CFO-warning `[blank]`) re-checked rather than
assumed stale · ✅ **§4 bottleneck re-confirmed** with a third name (BSX deepened) and two new
short-cover readings flagged as unresolved · ✅ **§5 chain-hop re-run, third consecutive empty result,
tool-floor limitation re-stated** · ✅ **§6-Q1 answered by name**: HEDGE = XLV/WELL/VTR/UNH(newly);
DESTINATION = ABT(clean)/CVS(confirmed-but-crowded)/HUM(the real vehicle, no longer clean) · ✅ **§6-Q2
answered with computed numbers**: 90d/60d correlations confirm PREMORTEM, 20d shows tightening to ≈0.72
avg; **exactly one name (HUM) carries negative XLRE correlation and near-zero SPY correlation/beta**,
and that finding is reported alongside its new crowding risk rather than in isolation · ✅ **§7 eight
track-KPIs + six anti-signals as dated/falsifiable observables** · ✅ asof stated (07-20 tape / 07-17
rates / 07-21 news empty) and honored throughout · ✅ **Zero buy/sell calls, zero sizing.**
