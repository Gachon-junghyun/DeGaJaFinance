# L1 · DEEP — sector deep-dive (stage)

> Phase 2. One agent per DEEP sector (parallel fan-out, one message): flow → players → IR →
> value chain → bottleneck/refutation. Calls L2. Output: `SECTOR_DEEP_{code}.md` × N.

## L2 called
- [deepdive](../L2_modules/deepdive.md) — `module_industry_map` (player union + value chain) ·
  `module_business(_us)` (⚠ `--json` on US: default markdown carries KR headers) ·
  `module_disclosure(_us)` · `module_chart --read`.
- [news](../L2_modules/news.md) — (US) `chain-hop` under-named-beneficiary candidates.
- [indicators](../L2_modules/indicators.md) — `module_flow`/`us_flow` flow cross-check
  (short-z ≥+1.5 spike / ≤−1.5 exit divergence vs narrative = the order-flow tell news can't see).

## What this stage does
- **Macro gate**: only OW-designated sectors (plus any pre-mortem-promoted leg). No Neutral/UW padding.
- Per sector: player extraction (**large-cap universe ∪ thematic small-caps**, bounded: named ≥2×
  in the sector's news window AND a real ticker AND mcap ≥ ~$2B — this union is where alpha leaks) →
  IR anchor (who does what, from primary filings) → value-chain node map 5–8 nodes left→right
  (bottleneck = *binding constraint*, strong demand ≠ bottleneck; mark cross-sector chains,
  e.g. AI→power→transformers→copper) → chain-hop candidates (body-proximate only, never
  headline-named; a news co-mention alone is NOT a candidate — flow cross-check before it may
  reach BET) → track-KPIs + anti-signals (what kills the thesis, stated as observables).
- **Continuous-track vs rotating** (from ROTATION's picks):
  a continuous sector was deep-dived very recently → **lead with the DELTA** (new print/contract/
  guide, thesis confirm-or-crack, kill-switch proximity) and carry unchanged structure by reference
  to the prior file. A rotating sector gets a full fresh map. Daily tracking compounds signal;
  it does not re-print the same map.
- Fan out all sector agents **in one message** (parallel) — wall-clock stays near a single deep.

### Carry rules from `handoff/RESEARCH.md` (loaded by HANDOVER; binding here)
- ⚠ **Price-cycle sectors are read on the second derivative, not the level** (lens B1). For memory,
  steel, shipping, refining, chemicals — any commodity node — tabulate the **QoQ change series**.
  Level and rate routinely point opposite ways, which produces the apparent paradox "shortage
  persists but the equity struggles". Measured: server DRAM contract prices ran
  **+90~95% → +58~63% → +13~18% QoQ** across three quarters while physical supply stayed short into
  2027. Two consecutive declines in the *rate* is the signal; the level is the distraction.
- ⚠ **Peak-margin / low-multiple trap** (lens B2). A cyclical at its earnings peak prints its
  *lowest* forward multiple because the denominator is peaking. Measured: Micron forward P/E
  **6.31×** at gross margin **84.6%**, against a prior-cycle peak of 59% and an FY2023 margin of
  **−9.1%**. **Put the forward multiple next to where margin sits in its own history** before calling
  anything cheap — a multiple without a margin percentile is not a valuation.
  ★ **And read the estimate-momentum table with it** (`module_fundamentals_us` §추정치 모멘텀,
  added 2026-07-22). It shows where the denominator has been *going*: MU's +1y EPS ran
  **100.53 → 150.91 in 90 days (+50.1%)** on **30 upgrades : 0 downgrades**. A low multiple whose
  estimates are being revised up that steeply is consensus **chasing**, not cheapness.
  🚨 **But do NOT write "revisions turn before price does" — that was tested and it did not hold**
  (2026-08-09, `scripts/measure_ic.py`, its first-ever invocation).
  · Two non-overlapping windows disagreed **in sign**: W1 **+0.403**, W2 **−0.299** — and **both
    cleared the |IC|<0.21 power floor while pointing opposite ways**, so the folded +0.052 is empty.
  · The control arm settles the cause: on **ex-IT 120 names** the same measurement gives
    **+0.074 / −0.064** and the Q5−Q1 spread goes **+9.4pp → −1.1pp**. ⇒ **the effect is an
    Information-Technology loading, not a revision axis.** (`RESEARCH.md` had it as *"indistinguishable
    — Q5 is 72% IT"*, an inference from composition; the control makes it a measurement.)
  ⇒ **Use the revision table as a description of the denominator's direction** — that part is
  arithmetic and still valid. **Do not use it as a leading indicator, and never as independent
  evidence on an IT name** (that is precisely where the confound lives). Sizing on it is barred:
  see SIZE's `--ic` note.
- 🚨 **Before calling a cyclical's margin unsustainable, read its CONTRACT terms from the filing —
  not the press** (added 2026-08-10; this is the L2 lens's own escape hatch and it fired).
  Lens L2 says a peaking denominator collapses. **Whether it can collapse is a contractual question**,
  and the answer is in the 10-Q, which the desk had never opened. Measured on MU's FY26Q3 10-Q
  (`module_disclosure_us` → SEC primary, **its first-ever call**): strategic customer agreements are
  **take-or-pay with binding multi-year volumes**, carry a **ceiling at ~the 2Q CY2026 market price**
  **and a floor for the term**, and management states that at **floor** pricing gross margin runs
  *above any prior cycle's peak*. The FY2025 10-K, nine months earlier, said the opposite
  (*customers reluctant to enter fixed-price contracts; terms periodically renegotiated*) —
  **the contracting regime changed between two filings and no desk file noticed.**
  ⇒ Two consequences, both binding here:
  (a) **L2's mechanism does not apply to contracted volume** — say which share is contracted, or
      mark it `unknown` (C3). Never assert the collapse without that share.
  (b) ⚠⚠ **A contractual ceiling flattens the very series L1 tells you to read.** The desk's evidence
      #1 for its regime call is the contract-price QoQ deceleration (+90~95% → +58~63% → +13~18%).
      If price is renegotiated **inside a floor/ceiling band** and the ceiling is pinned to a dated
      market price, that deceleration is **arithmetic hitting a cap, not demand weakening.**
      **Check for a band before reading a second derivative as a demand signal.**
  ★ **Generalized, and this is the transferable part**: the desk already ran the take-or-pay frame
  *well* — 21 files apply it to KMI's $35.67B RPO, LNG's tolling, VST's 20-year PPA floor, listed as
  *"things the Fed can't reach"*. **Zero of them applied it to memory**, where the same structure sat
  in the filing and where the desk's own §6 carried it as an open contradiction for three weeks.
  ⇒ **When a frame is load-bearing in one sector, ask which other position it should be pointed at.**
  The failure class is not a missing capability; it is a capability aimed at only one target.
- ⚠ **Name the node's customers and check their disclosed spend** (rule A6). A supply-chain verdict
  written without looking at the buyers' capex is missing the demand side of its own thesis. If their
  prints are pending, say so **with the date** rather than concluding around them.
- ⚠ **An inherited lead/lag claim is tested or tagged `[unverified]`** (rule A5). Measured: an
  uncited "EDA leads semis by 12–18 months" was carried between reports and repeated as fact; 199
  monthly observations (2010–2026) gave same-month **+0.63** vs lag-12 **+0.05** — coincident, not
  leading. Lead-lag is one correlation table to test and expensive to get wrong; it is the claim
  class most likely to be repeated on authority alone.
- ⚠ **State the dispersion inside the sector** (lens B5). Measured 2026-07-21: memory/storage
  +12~14% while GPU/ASIC managed +2.0~2.2% — a ~10pp spread inside "semiconductors" in one session.
  If the spread between sub-nodes exceeds the sector's own move, the sector label is the wrong unit
  of analysis and the file must say so.

## ✅ EXIT CHECK
- [ ] One `SECTOR_DEEP_{code}.md` per selected sector (incl. any promoted 5th), written via parallel agents.
- [ ] Each covers flow → players(∪ thematic) → IR → chain map(+chain-hop) → bottleneck/KPI/anti-signal.
- [ ] Continuous-track files LED with the delta; rotating files are full fresh.
- [ ] Any ROTATION-flagged matrix×flow divergence has an explicit resolution verdict in its sector file.
- [ ] **Commodity/price-cycle nodes carry a QoQ rate-of-change series, not just levels.**
- [ ] **Every "cheap on forward multiple" claim states where margin sits in that name's own history
      AND its estimate-revision trend** (`module_fundamentals_us` §추정치 모멘텀 — 90d change +
      up:down breadth). A low multiple whose estimates are being revised up steeply is consensus
      chasing, not cheapness. ⚠ The revision table describes the denominator's **direction**; it is
      **not** a leading indicator and carries **no independent weight on an IT name** (measured: the
      effect is an IT loading, ex-IT Q5−Q1 = −1.1pp).
- [ ] 🚨 **Every "the margin must mean-revert" claim names the contract terms it checked** —
      floor/ceiling bands, take-or-pay volumes, contracted share — read from the **filing**, or marks
      that share `unknown` (C3). And **before reading a QoQ rate-of-change as a demand signal, state
      whether a contractual ceiling could be producing it.**
- [ ] **One frame-transfer question answered**: name a frame this desk trusts elsewhere (take-or-pay
      floors, RPO lock-in, regulated-return) and say whether it applies to this node. *"Checked, does
      not apply"* is a pass; never having asked is not.
- [ ] **The node's customers are named and their disclosed spend checked** (or their print dates given).
- [ ] **Every lead/lag claim is either measured this run or tagged `[unverified]`** — none inherited as fact.
- [ ] **Linter run on this stage's own output** — `python -X utf8 scripts/report_lint.py <written file>`. Every finding is fixed or the paragraph carries its rule ID with a stated reason for exemption. ⚠ It checks form only (C1 benchmark · C2 both halves · S6 future label · D6 OBV-alone); a clean run is not a correct report.
- [ ] Sub-sector dispersion stated; if it exceeds the sector move, the file says the sector label is the wrong unit.
