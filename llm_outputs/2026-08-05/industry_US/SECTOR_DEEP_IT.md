# SECTOR_DEEP_IT — industry_US — 2026-08-05 (Wed) · **ROTATING → full fresh map**

> Last IT deep 2026-07-31. Flow `asof 2026-08-04 settled` (`SECTOR_FLOW_US.json`, trimmed per SWEEP D74
> — US market is OPEN this run; the live 2026-08-05 bar is excluded from every figure below, [measured]).
> Benchmark **SPY** inline on every relative number. No sizing / no buy-sell.

## §0 · The mandate, answered in one line

**Neither is "the sector."** XLK's +5.13pp is a 1-session, cap-weighted number carried by MSFT (RS20
+23.6; IT's wflow/eqflow gap is 10.3×, `SECTOR_ROTATION §2`); 0.05 breadth (3🟢/56, 17🔴) is the
20-session median-name reality, and it says **Semiconductors (med RS20 −7.7, 0🟢/8🔴) is the board's
worst sub-industry while Communications Equipment (+5.7) and Systems Software (+5.4, RS60 +50.4) carry
it.** The 13.4pp median-RS20 spread is **2.6× XLK's 5-day excess and ~12× its duration-matched 20-day
excess (+1.15pp).** **The label is the wrong unit (W5); "IT" is at least two sectors — software/
networking accumulating, semis being distributed — glued together by GICS.**

## §1 · Sub-industry dispersion — reproduced independently [measured]

| Sub-industry | n | med flow_score | med RS20 vs SPY | med RS60 vs SPY | 🟢 | 🔴 |
|---|---|---|---|---|---|---|
| **Communications Equipment** | 5 | **+0.532** | **+5.7** | −3.2 | 0 | 1 |
| Application Software | 12 | +0.281 | +4.2 | −10.4 | 1 | 3 |
| Systems Software | 5 | +0.264 | +5.4 | **+50.4** | 2 | 0 |
| Tech Hardware/Storage | 6 | +0.256 | −0.6 | +8.9 | 0 | 1 |
| Electronic Components | 3 | +0.085 | −0.1 | −4.0 | 0 | 1 |
| EMS | 2 | +0.060 | +4.6 | −5.2 | 0 | 0 |
| IT Consulting | 2 | −0.123 | −4.8 | −7.3 | 0 | 1 |
| Semi Materials & Equip. | 6 | −0.319 | −4.9 | +6.5 | 0 | 2 |
| **Semiconductors** | 14 | **−0.443** | **−7.7** | −9.2 | 0 | **8** |

(Electronic Equipment & Instruments dropped, n=1/KEYS only, no median.) Re-derived total: **3🟢/17🔴 of
56 ⇒ breadth 0.054** — matches the mandate figure exactly.

**Dispersion vs the sector's own move**: best sub-industry (Comms Equip, RS20 +5.7) minus worst (Semis,
−7.7) = **13.4pp**. XLK exc5 **+5.13pp**, duration-matched exc20 **+1.15pp** (`MACRO §B`) — the 13.4pp
exceeds both (2.6× / ~12×); RS60 spread is worse (Systems Software +50.4 vs Semis −9.2 = **59.6pp**).
⇒ **By this desk's own rule (spread > sector move ⇒ wrong unit), "IT" fails as a unit on two windows.**
Semiconductors (n=14, the sector's largest group) is the worst-performing sub-industry of any size on
the board.

## §2 · S30 and what the control pair pre-commits

**S30's frozen observable** (median RS20 vs SPY of {STX, MU, WDC}): **STX −1.0 · MU −8.0 · WDC −0.1 ⇒
median −1.0** on the 08-04 settled bar — **branch B (≤0) by a 1.0pp margin**, reproduced independently,
matching `MACRO §D-2`. **Not re-scored**: S30's actual settle is tonight's close, unseen this run.

**What the control pair pre-commits.** Registration text: *"if the memory median turns while DELL/HPE
do not, it is a memory event; if both turn, it is an IT-beta event."* Measured: **DELL RS20 +8.8 / RS60
+97.5**, **HPE RS20 +17.4 / RS60 +71.0** vs SPY — both positive on both windows, and have been since at
least 07-31 (+4.0/+86.4, +16.4/+56.8). ⇒ **the disqualifying condition ("controls do NOT turn") is
already false, and has been false for the bracket's entire life.** **If S30 flips to branch A tonight,
the registration's own logic pre-commits that flip to read as an IT-beta event, not a memory event** —
the disambiguator that would license "the memory median turned" never held. A flip proves less than
S30's authors intended.

## §3 · Value chain — 7 nodes, 2 primary anchors

```
① memory        ② foundry/logic   ③ accelerators    ④ interconnect/optics  ⑤ networking systems  ⑥ systems SW   ⑦ hyperscaler
MU STX WDC   →   TSM (untracked) → NVDA AMD AVGO  →  LITE COHR CIEN      →  ANET CSCO           →  MSFT PANW NOW → MSFT (dual-role)
🔴 🟡 🟡          [absent, M252]     🟡 🟡 🟡           🟡 🟡 🔴              🟡 🟡                🟢 🟡 🟡        🟢 (= node ⑥)
```

**Primary anchors**: LITE's 10-K (filed 2025-08-19) — Cloud & Networking supplies "optical and photonic
chips, components, modules, and subsystems ... enabling high-capacity optical links for cloud
computing, AI/ML workloads, and DCI" — node ④ is load-bearing infrastructure by primary text. ANET's
fresh 8-K (filed 2026-08-04, Items 2.02/9.01) is the primary for the first-$3bn-quarter cited in the
mandate.

**Binding constraint, layered honestly**: the standing finding (D1, since 07-28) is node ① binds on the
**LTA price term**, not volume — but this run has **no fresh second-derivative source** for DRAM QoQ
(TrendForce); the 07-31 carried 1Q26 +90~95%→2Q26 +58~63%→3Q26 +13~18% is **not re-pulled or
re-asserted** [inferred/carried, unverified this stage]. Fresh this run: node ② is **structurally
invisible** (TSM absent from `us_top300`; M252's gap grew 2→4 names per PREMORTEM Lens 4) — the desk
cannot see whether foundry binds at all. Of visible nodes, ⑤ carries the cleanest money (ANET FINRA z
**−1.45**, primary-confirmed record quarter) while ④ splits (LITE accumulating, CIEN broken RS60
−29.1). **Call**: node ① remains the plausible standing constraint by prior evidence; this run can only
show node ② is unmeasurable and node ⑤ has the cleanest fresh demand — a gap, not a resolved answer.

## §4 · The optical node — Card 1 re-graded

EVENT_ALPHA Card 1 called LITE **CONFIRMED-EARLY** on OBV 매집 + RS20 +18.4 vs SPY against COHR's RS20
−0.1 on an equally headline-named name — "the story named two suppliers and the money picked one." That
split reproduces here. But PREMORTEM Lens 3 measured LITE's days-21-to-60 segment (the 60-day excess
earned *before* the last 20 sessions) at **−23.9pp, the worst in its scanned set** — RS20 +18.4 sits
atop a 40-day hole nearly 24pp deep, not a level base. Card 1's own KPI for a theme is **RS60 crossing
above 0**; RS60 is **−10.3**, still negative — **unmet.** ⇒ **CONFIRMED-EARLY overstates the evidence.**
Re-grade: the money did pick LITE over COHR (real, worth carrying), but the shape is a turn-off-a-hole
repair, not a confirmed run — should read **"EARLY, NOT YET CONFIRMED"** until RS60 clears 0 **and** a
named instrument (Federal Register notice, BIS rule, EO number) appears, both due by 2026-08-19. CIEN
remains broken (RS60 −29.1, 🔴분산); COHR remains money-absent — the ban-talk story names three
suppliers, only one has real accumulation, and the shape is not yet a trend.

## §5 · Valuation / estimate momentum — LITE, ANET

**`margin_history` is not a field `module_fundamentals_us` returns for either name** — confirmed on the
raw `--json` (no such key). Per the stated ~61% failure rate (M233), **no cheapness/richness claim is
made for either name — no percentile exists to place the multiple against.**

Measured instead: **LITE** fwd P/E **46.59×**, PEG **0.63**, cleanest revision table on the board —
every horizon 100% up/0% down at 7d and 30d, +1y EPS +10.4% over 90 days. Not the low-multiple trap
shape (46.6× isn't a trough multiple) — priced for continued acceleration, a different risk (miss vs.
steep consensus, not de-rate off a cheap base). **ANET** fwd P/E **40.13×**, PEG **2.30** (richer
growth-adjusted), much softer momentum — current-quarter revisions 0 up/1 down over 7d, 90-day EPS
+2.6%/+3.3%, an order of magnitude below LITE's. ANET has run further ahead of its own revisions —
matching Lens 3's finding that ANET's days-21-60 segment is **genuinely positive (+15.2)**: one of four
names (with VLO, MPC, PSX) whose momentum is real, excluded from green only by `vol_surge` (1.11,
misses 1.2 by 0.09) — not a repair.

## §6 · AMD / S50 — a beat-and-sell-off breaks the bracket's asymmetry, not the thesis

AMD beat with record data-centre revenue and an upbeat outlook and sold off; flow says money left
**before**, not after, the print: fs **−0.103**, OBV **중립**, RS20 **−2.7** / RS60 **+21.5** vs SPY,
segment **+24.2** ⇒ **DECAYING-STOCK**. Fwd P/E 35.34×, PEG 1.14, revisions net-positive (11↑/2↓ 30d)
but far less lopsided than LITE's.

**S50 was written asymmetric — "only the CUT branch changes a conclusion."** This event exposes the
blind spot: guidance was not cut, so by S50's own test the bracket's conclusion is formally
**UNCHANGED** — the thesis it was built to falsify did not happen. But price acted as if something did
change, and flow independently re-filed AMD as decaying. **The bracket and the flow tag now read
differently on the same print, by construction, not error**: S50 only watched guidance content, never
price reaction to content that beat. A beat-and-sell-off is exactly what "only CUT moves the needle"
under-reads — it resolves "no change" while the tape prices something else. Not a flaw to patch (S50
not re-scored); the honest limit of what it was built to see, stated at its 2026-08-06 settle.

## §7 · Track KPIs + anti-signals, dated

| KPI | Value `08-04` | Test / settle | Anti-signal |
|---|---|---|---|
| S30 median RS20 {STX,MU,WDC} | **−1.0**, branch B | **08-05** close (unseen) | DELL/HPE already turned ⇒ flip reads IT-beta, not memory |
| S48 optical (LITE) | RS20 +18.4, RS60 **−10.3**, seg −23.9 | RS60>0 + named instrument, **08-19** | LITE OBV → 분산 ⇒ kill |
| S50 (AMD/ANET) | AMD DECAYING (−2.7/+24.2); ANET clean (z −1.45, seg +15.2) | **08-06** | AMD OBV → 매집 in 5 sessions ⇒ flush, not decay |
| Sub-industry dispersion | 13.4pp vs XLK exc5 +5.13/exc20 +1.15 | ongoing | spread < XLK's 5d move ⇒ label re-converges |
| Breadth vs wflow | 3🟢/56; wflow +0.175 vs eqflow +0.017, 10.3× | ongoing | eqflow > wflow ⇒ genuinely broadening |
| Memory 2nd-derivative | source absent this run | flag only | — |

**Carried anti-signals**: HY OAS ≥3.10% (reclass to credit); IG OAS ≥0.90% (now 0.78%); CXMT Entity
List action (settles 09-30, feeds S37).
