# BET_SHEET — industry_US — 2026-07-31 (Fri)

> **ONE file, per-sector sections, §A–§E facets each** (downstream desks glob this exact filename —
> never split). Benchmark **SPY** inline on every relative number (**C1**). Flow/RS asof the
> **module_flow 2026-07-31 pull** (positioning tool, prev-close settled RS) unless noted; fundamentals
> cross-checked live 2026-08-01 clock via `module_fundamentals_us --json` (XBRL↔yfinance). **Sizing
> language is influence illustration only — zero buy/sell recommendation (P4).** §B freshness tags
> (🟢LIVE / 🟡PARTIAL / 🔴RESOLVED) filled by ALPHA (stage 9); `theme_age --scope foreign` run FIRST.

## ⚠ 0 · Five instrument caveats binding on every number below

1. **The Energy epicenter's fundamental CRACKED on the newest settled bar.** The distillate crack
   (HO×42−WTI, yfinance DAILY settled) fell **−5.879 on the 07-30 settled bar — the first negative
   increment since 07-24** — WHILE crude also fell (84.46→83.59), which is the demand-destruction
   anti-signal DEEP-ENRG registered, not a supply release (Russia diesel/gasoline ban *extended into
   2027*, so supply held). **The deterministic crack (fundamental) and the OBV flow now DISAGREE.**
   This sheet presents that as a **divergence**, not a branch-A confirmation.
2. **L2 margin percentiles are blank on the sheet's two most-cited refiners.** `margin_history.py`
   returns `연간 데이터 없음` on **VLO (7th run, D56)** and **XOM (2nd)**; regulated utilities and IPPs
   have **no comparable gross-margin series (C3)**. ⇒ **NO name here is called cheap or expensive** —
   a forward multiple without a margin percentile is not a valuation.
3. **The 🟢 tag is biased LOW in the small-cap tail.** SWEEP's news-velocity axis served only the
   **top-48 by mcap**; rank>48 ran OBV-only, so the refiner/CEG/tanker 🟡 tags are **news-velocity
   demotion artifacts** — the 07-31 positioning pull re-rates the refiners to 🟢가속 (DEEP-ENRG §3), but
   OBV is **grade-C (D6)** and never carries a verdict alone.
4. **27% of the real US book sits on NO measured axis.** **TSM (~$382) and LNG (~$780) are outside
   `us_top300` (M252)** ⇒ any exposure percentage carries an unstated error bar. LNG is the book's main
   touch on the Energy cycle (consequence-beta, not the engine).
5. **The exposure state is `복귀`, target 90%, but the book is 밴드이탈 −37.3pp (invested ~53.9%), and
   `TIMEFOLIO_EXECUTE=1` is ARMED 🚨🚨.** Per the BET EXIT CHECK, §6 below states plainly whether these
   candidates can fill that target. **They cannot, on merit-clean names — stated, not silently left.**

---

# §I · ENERGY (OW−, continuous DEEP ①) — the epicenter-starter, with its engine cracked

## §A Numbers `[module_fundamentals_us --json, live]`

| Name | Layer | Trailing P/E | Forward P/E | Fwd EPS | Mean target | Margin pctile | flow / OBV | RS20 vs SPY | RS60 vs SPY | short |
|---|---|---|---|---|---|---|---|---|---|---|
| **VLO** | refiner | 12.92 | **11.44** | $27.08 | $290.22 | ⚠ **BLANK, 7th run (D56)** | +0.48 / 매집 | **+15.9** | **+19.5** | 4.3% covering |
| **MPC** | refiner | 20.62 | **11.28** | $27.77 | $303.89 | ~37th (FY25 GM 10.0%, med 10.5) | +0.50 / 매집 | **+17.9** | **+17.7** | 2.5% covering |
| **PSX** | refiner | — | **11.07** | $18.98 | $205.47 | ~55th (FY25 GM 12.3%, med 12.1) | +0.48 / 매집 | **+19.4** | **+13.9** | 2.3% covering |
| **XOM** | integrated (control) | — | 14.4 est | — | ~$167 | ⚠ **BLANK (M233)** | 매집 | **+12.1** | **−3.6** | 1.1% covering |
| **CVX** | integrated | — | — | — | — | ⚠ blank | 매집 | +15.0 | **−1.9** | 1.0% covering |

**Arithmetic cross-check (math)**: forward EPS ÷ trailing EPS = **MPC 27.77/15.20 = 1.827 (+82.7%)**,
**VLO 27.08/23.97 = 1.130 (+13.0% yfinance trailing)** — the 90-day +1y EPS revision path DEEP measured
(MPC 20.55→27.77 = **+35.1%**, VLO 18.87→25.21 = **+33.6%**, PSX 15.17→18.98 = **+25.1%**) reproduces
independently as "estimates climbing 25–35% in 90 days on an ~11× multiple" = consensus **chasing**, not
cheapness (M234, 4th replication). ✅

## §B Thesis + freshness `theme_age --scope foreign`

**Theme age (07-31/foreign):** `diesel crunch` **🟡ACCELERATING 25.71× accel, age 80, 9 total** (the
precursor ≤2-outlet climbing form) · `refining margins` **🟡ACCEL 2.91×, 104** · `Russia sanctions`
**🟡ACCEL 3.43×, 88**. The supply narrative is accelerating, NOT fading.

- **VLO · MPC · PSX — 🟡PARTIAL (downgraded from a 🟢-flow read; disagreement stamped).** The refiner
  layer is the clean cycle epicenter — **the only Energy layer with a positive RS60 vs SPY base (+13.9
  to +19.5), shorts covering, uncrowded** — and the margin thesis (S49 branch A) is *supply-supported*
  (Russia ban into 2027). **BUT the margin engine just cracked**: the distillate crack rolled −5.879 on
  the 07-30 settled bar while crude also fell — DEEP-ENRG's registered demand-destruction anti-signal.
  **The OBV flow (매집, RS20 +15.9/+17.9/+19.4 vs SPY) and the deterministic crack now DISAGREE**; per
  **D6** the OBV is grade-C and does **not** carry the verdict against the crack. ⇒ **🟡PARTIAL, residual
  = the 5-session settled crack change must hold > 0; re-check S49 → 08-06 (MPC prints 08-04, PSX
  08-05).** `[measured]`
- **XOM — 🟡PARTIAL leaning against us (S31).** Integrated control, **RS60 −3.6 vs SPY negative base**
  (crude-beta laggard); RS20 +12.1 vs SPY > +10 is a war-premium decoupling — **S31 branch A tracking
  against the desk to 08-05.** XOM **missed Q2** on refinery maintenance (07-31). Not a buy candidate;
  it is the S31 control. Re-check 08-05.
- **CVX — 🔴RESOLVED (logged).** Integrated, one risk-unit with XOM (crude-beta not crack), **RS60 −1.9
  vs SPY negative base**; **beat** on refining margins soaring (07-31) but the base axis fails. Dropped
  from bettable; `reject_ledger E.상관가드`, revives-if RS60 vs SPY > 0, recheck 08-05.

## §C Flow / positioning `[module_flow --positioning, 2026-07-31]`

Sector flow **#1 on both wflow (+0.471) and eqflow (+0.358)**, breadth 0.19 (best on the board) — money
is accumulating Energy **broadly** on the prev-close series, which **has not yet repriced the 07-30/07-31
crack roll** (SWEEP CONTRADICT flag). Refiner short covering: VLO 4.3% / MPC 2.5% / PSX 2.3% float, all
covering. Implied moves: **MPC ±8.5% (expiry 08-21, D21 — COVERS its 08-04 print, usable)**; **PSX ±2.4%
(expiry 07-31 — EXPIRES BEFORE its 08-05 print, NOT event-priced, M89)**.

★ **Tanker sub-layer (Hormuz-closure leg, 0% book — PREMORTEM Lens-4 blind spot).** DISPERSED, not
uniformly dead: **INSW 🟢가속 매집 RS20 +17.7 / RS60 +7.2 vs SPY with a BUILDING 6.2%-float short (DTC
3.4) = squeeze fuel**, **FRO 🟢가속 매집 RS60 +1.9 vs SPY** — both positive-base; **STNG (RS60 −12.3 vs
SPY) / DHT (−4.0 vs SPY) 🟡중립** negative-base. INSW/FRO flow PASSES but **chain-hop is DOWN (300s
timeout)** so no body-proximity confirmation → **not promoted to a buy candidate; filed to
`missed_ledger U.발굴부재` (INSW/FRO), enters-if body-confirm + RS60 vs SPY holds > 0, recheck 08-13.**
STNG carried on ledger since 07-23; **DHT → `reject_ledger A.flow미도착`, recheck 08-13.**

## §D Competition / peers

MPC/VLO/PSX are **one risk unit (ρ +0.878, M147)** — may NOT be counted as three positions. **XOM/CVX
are one-layer-off** (integrated, RS60 negative vs SPY = crude-beta), the control not a peer — "add
refiners, not integrateds" (PREMORTEM Lens 4). The intra-"Energy" RS60-vs-SPY spread runs **STNG −12.3
to VLO +19.5 = ~32pp**, dwarfing the ~2pp sector move (XLE 5-day −1.99pp vs SPY) ⇒ **"Energy" is the
wrong analytical unit; refiner / integrated / tanker are three trades (B5/W5).**

## §E Refutation + dated catalyst

- ⚠⚠ **The epicenter-starter's engine cracked the same week the cycle-GAP opened.** SWEEP's −1.135pp
  Energy epicenter hole is real and the tape is 🟢 (gate open), so a **core** refiner starter exists on
  this sheet regardless of tape (§ ACTION_TICKETS) — **but the ADD beyond core is now under a fundamental
  headwind** (crack roll), so the under-exposure is *less* clearly a hole than on 07-30.
- **First 7-day DOWNGRADES appeared in the refiner revision breadth** coincident with the crack roll:
  +1y `down7` = **MPC 2 · VLO 3** (PSX 0) — revisions turn before price, tracked (n small).
- **Kill (S49 branch B):** 5-session settled distillate crack change **≤ −5.0 by 08-06** — now **+3.0
  with the daily increment already −5.879**, so **one further settled roll breaches it.** **Dated: MPC
  08-04 · PSX 08-05 · S49 → 08-06.**

---

# §II · FINANCIALS (OW−, DEEP ④) — the OW re-carried on money-center bank NIM, not breadth

## §A Numbers `[module_fundamentals_us --json, live]`

| Name | Node | Trailing P/E | Forward P/E | Fwd EPS | P/B | Mean target | flow / OBV | RS20 vs SPY | RS60 vs SPY |
|---|---|---|---|---|---|---|---|---|---|
| **BAC** | money-center (most asset-sensitive) | 14.33 | **11.76** | $5.28 | 1.58 | $68.68 | +0.57 / 매집 | **+5.8** | +13.9 |
| **JPM** | money-center | — | **14.26** | — | — | $371.85 | +0.53 / 매집 | **+5.6** | +11.3 |
| USB·PNC·FITB | regionals (purest NIM) | — | — | — | — | — | USB🟢/PNC·FITB🟡 매집 | +2.0/+0.0/−1.2 | +10.3/+9.7/+9.3 |

**BAC estimate momentum (B2):** +1y EPS **5.03 → 5.27 in 90d (+4.8%) on 4↑:0↓ (30d)** — the FRONT edge
of repricing the NIM tailwind (shallow, not the 30↑:0↓ consensus-chasing MU shows). fwd P/E 11.76 on a
*rising* E ⇒ NOT called cheap (C3); **the first downgrade in that 4:0 breadth is the anti-signal.**

## §B Thesis + freshness

**Theme age (07-31/foreign):** `credibility shock` **🟢FRESH, age 2, 7 total** (golden zone) — the
bear-steepener mechanism is fresh; `bank earnings` **⚪ECHO 0.96×** (the prints are consumed — no fresh
bank catalyst lands in-window until Q3 ~mid-Oct).

- **BAC · JPM — 🟢LIVE.** The FIN OW− survives WITHOUT the retracted R32 breadth reason, carried by
  **asset-sensitive money-center bank NIM**: the FRED-verified bear steepener (DGS2 −4bp to 4.22, DGS10
  +6bp to 4.67, **derived 2s10s +0.35→+0.45 on 07-29**) is the exact configuration that expands NIM, and
  **banks greened this run — BAC 🟢가속 매집 RS20 +5.8 / RS60 +13.9 vs SPY, JPM 🟢가속 매집 RS20 +5.6 /
  RS60 +11.3 vs SPY** (OBV paired with the RS pair, D6), XLF eqflow turned positive (+0.121). The
  mechanism is a same-tick rate-transmission, not an inherited lag (W2). `[measured]` **Hard kill 6–7
  days out: S51 NFP 08-07 (2s10s ≤ +0.20) / S23 → 08-05 / HY OAS ≥ 2.90% (9bp of buffer via IG 0.90%).**
- **Regionals (USB/PNC/FITB) — 🟡PARTIAL.** The *purest* NIM node and the deepest RS60 vs SPY base
  (+9–10), but **RS20 vs SPY flat (only USB green)** and offsetting CRE-credit risk — mechanism yes,
  tape no. Residual = RS20 vs SPY crossing > 0; re-check 08-07 (NFP duration read).

## §C Flow / positioning

XLF **wflow +0.163 AND eqflow +0.121 (both halves positive)** but **Δ−0.222 fading d/d** (money still on
it, decelerating). eqflow−wflow gap **still −0.042 (mega-cap-led) ⇒ R32 breadth reason has NOT returned.**
JPM shortlist **✅clean-rise** (short z −2.14, covering); BAC short 55.2 z +1.0 covering. **Insurers (TRV
RS60 +22.5 vs SPY) carry the deepest base but on a long-end reinvestment-yield mechanism, NOT NIM** — the
07-30 file's mislabelled carrier; carried as context (TRV recheck 08-06), not re-argued as the NIM leg.

## §D Competition / peers

Money-center BAC/JPM (NIM) ≠ insurers TRV/CB (reinvestment yield) ≠ exchanges ICE/CME (rate volatility,
RS60 −3.5/−8.9 vs SPY) ≠ payments MA/V (consumer spend, zero NIM). **The steepener helps deposit-funded
lenders specifically** — "Financials OW" resolves to money-center banks, not the sector (W5). BAC is the
cleaner pick (most asset-sensitive; JPM diluted by markets-NII, M138).

## §E Refutation + dated catalyst

- The 25bp buffer to the flattener line is an **07-29 reading, 2 sessions stale (D103)** — the mechanism
  is trackable only on the curve + flow until Q3 prints, so **S51 NFP 08-07 is the live binary that can
  break this OW in one print** (a hot print reprices cuts out → front sells harder → bear FLATTENER
  through +0.20 → NIM breaks, and R32 already killed the only other leg).
- **Credit override:** HY OAS ≥ 2.90% (2.84% now) OR IG OAS ≥ 0.90% (0.81%, 9bp) ⇒ banks de-rate
  regardless of NIM, hit first via JPM's 0.932 shared beta (M147). **Dated: S51 08-07 · S23 08-05 ·
  S26/S41 → 08-12.**

---

# §III · INFO TECH (N, split unresolved, DEEP ③) — the genuine early leg is STORAGE, not the mega-caps

## §A Numbers `[module_fundamentals_us --json, live]`

| Node | Name | Fwd P/E | Fwd EPS | Margin pctile (own history) | +1y breadth (30d/7d) | flow / OBV | RS20 vs SPY | RS60 vs SPY |
|---|---|---|---|---|---|---|---|---|---|
| **Storage** | **STX** | 15.68 | $54.71 | FY25 GM 35.2% = **MAX of 17-yr series (R23 +3.8pp l-f-l)** | 4–5↑:0↓ | +0.71 / 매집 | **+5.7** | +9.6 |
| | **WDC** | **29.16** | $18.75 | — | rising | +0.19 / 매집 | **+1.7** | +14.9 |
| **Networking** | **ANET** | 39.64 | — | — | — | +0.48 / 매집 | **+11.5** | +2.0 |
| | **CSCO** | — | — | — | — | +0.28 / 매집 | +2.6 | +19.6 |
| **DRAM (dropped)** | MU | **5.53** | $153.74 | **GM 84.6% = 100th pctile, +25.7pp over FY18 peak** | 30↑:0↓ / 28↑:1↓ | −0.25 / 분산 | **−13.0** | +29.4 |

## §B Thesis + freshness

**Theme age (07-31/foreign):** `memory shortage` **⚪ECHO, 1.59×, 297 total, age 75** — the theme is now
LOUD-but-CONSUMED (was 🟡ACCEL 2.07× two runs ago). Per the ALPHA rule, an ECHO theme needs *stronger*
live evidence — which storage has on flow, DRAM does not.

- **STX — 🟡PARTIAL (hard-stop required, ⚡crowded-short + no-info band).** The one ignited memory name
  (beat+guided, 🟢가속 매집 RS20 +5.7 / RS60 +9.6 vs SPY, crossed RS20 vs SPY > 0), BUT **ring-fenced by
  R23**: HANDOVER pre-committed to read STX as **no-info inside its own ±14.6% band**, and it carries a
  **⚡crowded-short (z +1.75, squeeze fuel — never a standalone buy, hard-stop stamped).** Residual =
  S30 median settles 08-05; a green here is squeeze fuel, not a clean signal. Re-check 08-05.
- **WDC — 🟡PARTIAL.** Cleaner storage expression — 🟢가속 매집 RS20 +1.7 / RS60 +14.9 vs SPY, short 7.6%
  covering — but **fwd P/E 29.16 with no margin percentile (C3)** and the settlement is S30 (08-05).
  Residual = S30 median {STX,MU,WDC} RS20 vs SPY holding > 0 on the 08-05 settled close.
- **ANET · CSCO — 🟡PARTIAL.** Networking pick-and-shovel, both 🟢가속 매집 (ANET RS20 +11.5 / RS60 +2.0,
  CSCO RS20 +2.6 / RS60 +19.6 vs SPY). ⚠ EVENT_ALPHA walled ANET as story-only pending a green; the
  07-31 flow pull now reads 🟢가속. **ANET prints 08-04 (S50) — the AI-capex-guidance binary; residual =
  the guide direction. Re-check S50 → 08-06.**
- **MU — 🔴RESOLVED (dropped + logged).** DRAM core, textbook L2 peak-margin trap (fwd P/E 5.53× on a
  100th-percentile GM with 30↑:0↓ revisions = consensus chasing a peaking denominator), flow **🔴분산,
  RS20 −13.0 vs SPY, has NOT turned** (OBV 분산 with the RS pair, D6). `reject_ledger H.밸류소진`,
  revives-if S30 median RS20 vs SPY > 0 on 08-05 AND MU OBV → 매집, recheck 08-05.

## §C Flow / positioning

`SECTOR_FLOW_US.json`: **wflow +0.199 (rank 2) ≫ eqflow −0.113, 4🟢/56/26🔴, breadth negative.** The
wflow is MSFT (+0.80)/NVDA re-rating on their **own** prints (narrow); the negative breadth is a genuine
sub-node rotation — **storage igniting UP while DRAM (MU) + semicap (AMAT/LRCX/KLAC 🔴) + exhausted
security (CRWD/PANW 🔴) distribute.** RS20 vs SPY spans **+17.0 (MSFT) to −28.6 (SNDK) = 45.6pp**, ~18×
XLK's own 5-day move ⇒ the sector label is arithmetically the wrong unit (B5). **Storage-vs-equipment
RS20-vs-SPY spread ~20pp inside "semiconductors."**

## §D Competition / peers

**S30 control pair DELL (+4.0/+86.4 vs SPY) / HPE (+16.4/+56.8 vs SPY) stayed positive throughout while
equipment stayed deeply negative** ⇒ the memory turn is **storage-specific, not IT-beta** (a beta turn
would lift equipment). Storage (STX/WDC) wants the OPPOSITE verdict from the node one step to its left
(semicap). MU (DRAM) and STX (HDD/near-line) sit on **different demand curves** — STX is not the
decelerating DRAM contract-price series (M1).

## §E Refutation + dated catalyst

- **The whole IT candidate set is either ring-fenced or binary-gated:** STX is no-info-band +
  squeeze-fuel, WDC/ANET settle on 08-04/08-05 prints, MU is dropped. **There is no un-gated IT buy
  candidate on this sheet** — IT stays N and the sheet says so.
- **Anti-signals:** a capex CUT at **AMD 08-04 (S50 branch B)** breaks volume + price together and flips
  NVDA's EXTENDED-BUT-LIVE tag toward EXHAUSTED · CXMT Entity-List designation implemented · HY OAS ≥
  3.10% (then it is S26, not IT). **Dated: AMD/ANET 08-04 (S50) · S30 settles 08-05 · MU FQ4 ~09 (S4).**

---

# §IV · UTILITIES (UW−, DEEP ②) — UW correct in aggregate, masking one nuclear accumulator (CEG)

## §A Numbers `[module_fundamentals_us --json, live]`

| Leg | Name | Fwd P/E | Fwd EPS (vs trailing) | flow / OBV | RS20 vs SPY | RS60 vs SPY | prints |
|---|---|---|---|---|---|---|---|
| **AI-power** | **CEG** (nuclear/PPA) | 19.56 | $13.38 (▲ vs 11.52) | +0.49 / 매집 | **+10.6** | **−20.2** | **08-06** |
| | VST (merchant/IPP) | 14.3 | $10.33 (▲ vs 5.97) | +0.07 / mild-매집 | −1.3 | −9.9 | 08-07 |
| | GEV / VRT (GICS Indu) | — | — | 분산 / 분산 | −10.9 / **−21.2** | −12.4 / −33.4 | 10-28 / 10-21 (OUT) |
| **Regulated** | D · PCG | — | — | 매집 / 매집 | −0.1 / +3.9 | +7.7 / +5.6 | 07-31 / 10-22 |
| | WEC·AEP·ETR·SO·XEL·EXC | — | — | 분산 | median **−3.8** | negative | passed |

## §B Thesis + freshness

**Theme age (07-31/foreign):** `nuclear power` **⚪ECHO 1.89×, 665** · `data center power` **⚪ECHO
1.58×, 368** — CEG's narrative is loud but CONSUMED; its accumulation is a **flow** move (into the 08-06
print), NOT an estimate-momentum or fresh-narrative move (+1y EPS revised −1.6%/90d, current quarter
1↑:4↓).

- **CEG — 🟡PARTIAL (watch, not a candidate — DEEP explicit).** Accumulating IN a drawdown: OBV 매집 with
  **RS20 +10.6 but RS60 −20.2 vs SPY** (the RS pair carries the read, not OBV alone, D6). Its measured
  flow PASSES, so per the re-file rule it is **not removed on narrative grounds** — but the base is a
  60-day drawdown and the estimates are flat-to-down, so it is a positioning move into the print, not a
  breakout. **Residual = OBV stays 매집 AND RS20 vs SPY > 0 through the 08-06 print. Carry-forward
  independent of UTIL's DEEP slot; re-check 08-06.** `[measured]`
- **Regulated leg — 🔴 (UW vindicated, no candidate).** Median RS20 vs SPY **worsened to −3.8** on the
  bear steepener (duration-negative); D/PCG are idiosyncratic accumulators (OBV 매집 with RS20 −0.1/+3.9,
  RS60 +7.7/+5.6 vs SPY) carrying NO thesis — PCG prints 10-22 (out of window, no cheapness claim, C3).
- **VST — 🔴RESOLVED (logged).** Estimates moving (0y EPS +11.3%/90d) but **flow flat +0.07, RS20 −1.3 /
  RS60 −9.9 vs SPY — money is not following the estimates.** `reject_ledger B.모멘텀only`, revives-if OBV
  re-accumulate 매집 + RS20 vs SPY > 0, recheck 08-07. **GEV/VRT — 🔴 EXHAUSTED, out of window** (long
  liquidation: VRT estimates fine +5.2%/90d while RS20 −21.2 vs SPY collapses; carried on ledger).

## §C Flow / positioning

Sector flow **wflow −0.332 ≈ eqflow −0.329, 0🟢, both halves negative** — evenly sold, NOT a mega-cap
artifact ⇒ the aggregate UW is honest. But the **intra-AI-power CEG−VRT spread = 31.8pp vs SPY** (CEG
+10.6 − VRT −21.2), **14× the inter-leg spread (+2.3pp) and an order of magnitude wider than the
sector's own 20-day move (−2.84pp vs SPY)** ⇒ the sector label AND the two-leg split are both the wrong
unit (W5, the desk's 3rd instance after R7 and M26/M174).

## §D Competition / peers

CEG (contracted nuclear/PPA, hyperscaler counterparties Microsoft/Meta 20-yr PPAs) is a **different
object** from GEV/VRT (DC-equipment cyclicals, GICS Industrials) and from VST (merchant/IPP). The
regulated selloff is a **duration** verdict; CEG's build is a **contracted-capex** verdict — R7/R10
non-repeat: do not cross the two.

## §E Refutation + dated catalyst

- CEG's last-90-day EDGAR carries **NO new PPA/contract filing** (the 수주/계약 section is empty) — a
  demand update would land on the 08-06 print; stated as an omission with its date, not concluded around.
- **Anti-signals to "CEG is different":** a datacenter-PPA cancel or hyperscaler capex CUT at 08-06, OR
  CEG OBV → 분산 with RS20 < 0 vs SPY. **Anti-signal to the whole-sector UW:** regulated median RS20 vs
  SPY crossing > 0 by 08-07 (S35 branch A). **Dated: CEG 08-06 · VST 08-07 · S24/S47 → 08-07/08-12.**

---

# §V · CROSS-SECTOR LIVE SHORTLIST — names outside the four DEEP sectors

`US_LIVE_SHORTLIST.json` (asof 07-30 prev close). Named so nothing surfaces untracked; each is placed or
dropped-with-reason.

| Ticker | Sector | shortlist verdict | RS20/RS60 vs SPY | Disposition |
|---|---|---|---|---|
| **NVDA** | IT (held epicenter) | ✅clean-rise (short z −2.19 covering) | +1.5 / −2.3 | **🟢 held/crowded, not fresh** — EXTENDED-BUT-LIVE (capex RAISED); add-on-dip per PREMORTEM Lens 3, not a fresh BET candidate |
| **MSFT** | IT (spender) | 🟢가속, velo 2.12 | +18.1 / +9.3 | **🟢 held/crowded/most-printed** — the wflow head; not a fresh alpha layer |
| **JPM** | Financials | ✅clean-rise (short z −2.14) | +5.7 / +11.3 | **placed in §II** (money-center NIM leg) |
| **CSCO** | IT | 🟢가속 new-green | +2.6 / +19.6 | **placed in §III** (networking node) |
| **STX** | IT | ⚡squeeze-fuel (NOT clean) | +4.4 / +8.1 | **placed in §III** (🟡, hard-stop, no-info band) |
| **BKR** | Energy | △정상숏, RS60 −13.2 vs SPY | +15.1 / −13.2 | one-layer-off oil-services, negative base — **carried on reject_ledger** (not the crack epicenter) |
| **MA** | Financials | ⚡squeeze-fuel (z +2.73) | +6.5 / +12.6 | payments, zero-NIM — **dropped, `reject_ledger B.모멘텀only`** (squeeze fuel ≠ standalone buy, hard-stop), recheck 08-14 |
| **GRMN** | Cons Disc | ✅clean-rise, #1 flow of 300 | +22.5 / +22.4 | 🟢가속 clean-rise but **NO thesis anywhere in the desk's files** — **`missed_ledger U.발굴부재`**, enters-if a thesis/catalyst attaches, recheck 08-14 |
| **TRI · ITW** | Industrials (UW−) | 🟢가속 | +10.0/−0.0 · +4.4/+8.9 | sector UW−, no thesis — **`reject_ledger G.섹터중립`**, recheck 08-12 |
| **EA** | Comm Svc (N) | 🟢가속 OBV +0.44 매집 | +2.8 / +1.8 | no thesis (OBV 매집 with RS20 +2.8 vs SPY, D6) — **`reject_ledger G.섹터중립`**, recheck 08-14 |
| **SBUX** | Cons Disc (N) | 🟢가속 new-green | +3.2 / −0.4 | no thesis, RS60 −0.4 vs SPY — **`reject_ledger G.섹터중립`**, recheck 08-14 |

**Carried (already on ledger/scenarios, not re-filed):** AAPL (🟡 fade-watch, S46 → 08-13), QCOM (🔴,
K.본문반증 → 08-13), CRWD/PANW, STNG, GEV/VRT, AEP/EXC — all carried; HANDOVER `reject_ledger due`
re-surfaces them on schedule.

---

# §6 · Can these candidates fill the 90% `복귀` target? — NO, and this is stated, not left silent

**Book (CYCLE_EXPOSURE.json, 07-31):** total **$10,641**, invested **$5,731 = 53.9%**, cash **$3,921**;
target **90%** ⇒ **~$3,841 to deploy** (band −37.3pp). The cash roughly equals the deployment need, so
the constraint is **not cash — it is the absence of merit-clean candidates to absorb it.**

- **ENERGY** — the epicenter-starter fills the −1.135pp cycle hole (**~$121 to the 8.0% floor**) and
  that core exists on the sheet regardless of tape. **But the margin engine cracked (−5.879, one settled
  session from the S49-B kill), so the ADD beyond core is under a fundamental headwind** — this is not a
  place to responsibly push $3.8k.
- **FINANCIALS (BAC/JPM)** — the single cleanest OW (fresh, measured NIM mechanism, real base), but it
  carries a **hard binary kill 6–7 days out (S51 NFP 08-07)** — it can absorb a *measured* tranche, not
  a beta-sized push into a known binary.
- **IT** — every candidate is ring-fenced (STX no-info band + squeeze) or binary-gated (WDC/ANET on
  08-04/08-05); **no un-gated buy.** **UTIL** — CEG is a watch, not a candidate; the rest is UW.
- **Cross-sector** — GRMN has flow but no thesis; MA/STX are squeeze-fuel.

⇒ **The OW candidate set cannot responsibly fill a 90% target.** Deploying to 90% here means buying the
ENERGY crack-rollover and the STX no-info band to hit a number — the exact failure the EXIT CHECK warns
against. **The −37.3pp band gap is a beta/exposure decision (P.현금부족 class), flagged to the exposure
layer, NOT a stock-selection instruction (P4).** The responsible fills this sheet supports: the **refiner
core-starter (~$121, tape-gated ADD deferred on the crack)** + a **measured FIN money-center tranche
(kill-dated S51 08-07)**. Everything beyond that waits on 08-04/08-05/08-06/08-07 settlements. 🚨
`TIMEFOLIO_EXECUTE=1` is ARMED — a human confirms every order; the desk sends none.

---

## ✅ EXIT CHECK (BET)

- [x] Every DEEP sector has a section (ENRG/FIN/IT/UTIL) + a cross-sector LIVE shortlist section (§V);
      every shortlist name placed or dropped-with-reason.
- [x] Numbers cross-checked XBRL↔yfinance (`--json`); math_check on the fwd/trailing EPS ratios; blanks
      stated as blanks (VLO/XOM margin D56/M233; PSX/JPM trailing).
- [x] Flow/positioning cross-read per candidate; **written as ONE file.**
- [x] Every set-aside name in a ledger with a class + `--revives-if` + `--recheck-date` (14 reject rows
      + 3 missed rows this stage; carried names not re-filed).
- [x] **No name removed on narrative grounds while its measured flow still passed** — refiners re-filed
      as 🟡PARTIAL (not deleted) under the crack-vs-flow divergence; CEG kept as a 🟡 watch (flow passes);
      INSW/FRO filed missed (flow passes, body unconfirmed), not rejected.
- [x] Sizing consistent with the `복귀` exposure state — §6 states plainly the target **cannot** be
      filled on merit-clean candidates rather than pretending it can.
- [x] **Linter — `report_lint.py` → ✅ 0 findings** across C1 (benchmark inline) · C2 (both halves) ·
      S6 (future/live label) · D6 (OBV-alone). No exemptions claimed. ⚠ Form check only — it cannot see
      that §I's refiner thesis rests on a flow series that has NOT repriced the crack roll (stated in §A/§B).

*asof 2026-07-31 · industry_US BET_SHEET · no buy/sell language, sizing = illustration only (P4).*
