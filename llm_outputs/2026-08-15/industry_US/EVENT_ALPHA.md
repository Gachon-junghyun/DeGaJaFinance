# EVENT_ALPHA — industry_US · 2026-08-15 · Stage 5/11 (L1·EVENT_ALPHA)

> Bottom-up complement to MACRO's top-down matrix. Scope **`--scope foreign`** on every call (verified
> on each command). Flow tags asof **2026-08-14 settled**, `flow_score` is **3-axis**. No sizing (P4).

## 🚨 0 · The stage's own instrument state, stated BEFORE any card

**`thread --days 7` was NOT run — it cannot be run on this client.** `thread` (and `brief`) are
parser-marked **client-only** and **refused by the server** (`'thread' 는 원격 실행 불가`), and this
repo owns no local `news_alert.db`. This is an **architecture fact, not today's outage** (`D268`).

**Substitute actually used, and it is weaker in one specific way:** per-day curves were rebuilt by
differencing successive `fts search <term> --days N --count --scope foreign` windows — a legitimate
per-day count, but it gives **article counts, not outlet counts**. ⇒ **This stage cannot apply the
"≤2 outlets and climbing" precursor test as written**; it applies "≤2 *articles* and climbing" and
**says so on every card**. Where the distinction decides a card, the outlets are counted by hand from
the body read.

✅ **The transport itself is alive** — `fts` and `chain-hop` run remotely (MACRO §0 measured the CLI
flap and its recovery). Every count below was fetched at **23:2x–23:4x KST**.

---

## 1 · Selection log — no silent truncation

**13 candidate terms curved. 6 selected. 7 not selected, counted and named.**

| Thread | Curve (articles/day, **old → new**, 7d) | Tag | Selected? |
|---|---|---|---|
| **Navy shipbuilding** | 0 · 0 · 1 · 0 · 0 · 0 · **4** | **PRECURSOR** | ✅ Card 1 |
| **Optical transceiver / co-packaged optics** | 2 · 0 · 0 · 4 · 6 · 6 · **6** (24 total) / 2 · 0 · 0 · 5 · 6 · 8 · **6** (27) | **BUILDING from zero** | ✅ Card 2 |
| **Russian refinery** | 6 · 3 · 1 · 7 · 11 · 7 · **17** | **BUILDING, accelerating** | ✅ Card 3 |
| **Strait of Hormuz** | 108 · 70 · 192 · 236 · 252 · 188 · **231** (1,277) | **BUILDING, high plateau** | ✅ Card 4 |
| **Consumer sentiment** | 13 · 4 · 20 · 17 · 15 · 21 · **85** | **REIGNITED, spike** | ✅ Card 5 |
| **Maia 300** | 0 · 0 · 3 · 7 · 4 · 2 · **2** | **FADING** | ✅ Card 6 — *FADING admitted **only** because the book holds both sides of it* |
| HBM4 | 5 · 1 · 8 · 10 · 7 · 1 · 8 | choppy, no trend | ✗ |
| ADNOC | 14 · 14 · 28 · 13 · 22 · 6 · 16 | choppy; subsumed by Card 4 | ✗ |
| Austal | 0 · 0 · 5 · 3 · 0 · 0 · 1 | faded; folded into Card 1 as evidence | ✗ |
| tanker rates | 2 · 1 · 1 · 2 · 2 · 0 · 1 | flat at n≈1/day | ✗ |
| custom AI silicon | 1 · 0 · 1 · 0 · 1 · 0 · 0 | dead (3 articles / 7d) | ✗ |
| sanctions Iran | 2 · 0 · 1 · 0 · 0 · 0 · 1 | dead (4 / 7d) | ✗ |
| CXMT | — (88 / 7d, pool-norm **0.62× decelerating**) | decelerating | ✗ — but see §4 |

⚠ **Denominator for every curve**: foreign pool **d1 9,705 · d7 38,115**; **pool ratio 1.782×**
(`D255`). A thread must beat the pool to be building, and Cards 1–3 do by construction (they start
near zero).

---

## Card 1 — 🚨 **The US Navy opened warship construction to foreign yards, and it lands inside this desk's own OW−**

| | |
|---|---|
| **Thread** | `Navy shipbuilding` · **PRECURSOR** · 0·0·1·0·0·0·**4** · 5 articles / 7 days on a 38,115 pool |
| **Outlets (hand-counted)** | **3 independent** — `reuters` (via `cna`, `google_en`), `investing_en`, `upi` |

**Direction (body-read, not headline):**
> *"**Trump orders Navy shipbuilding overhaul and new shipyard**"* [`investing_en` **08-14**]
> *"**Hanwha, Fincantieri shares rise after Trump opens Navy shipbuilding to foreign yards**"*
> [`reuters`/`cna` **08-15**] · *"Hanwha makes bid to acquire **Austal USA**"* [`upi` 08-11]

The move is a **policy-set change to who may build US warships** — a category the desk's term table has
no bucket for and which no velocity screen can see at 5 articles. **The market has already voted on
one side of it**: the named beneficiaries that rose are **foreign yards** (Hanwha, Fincantieri), not
US primes.

**Exposure (chain position · flow tag asof 2026-08-14 · crowding):**

| Ticker | Chain position | flow (3-axis) | Tag | OBV | RS20 | RS60 | `vol_surge` |
|---|---|---|---|---|---|---|---|
| `GD` | **US shipbuilder** (Electric Boat, Bath Iron Works) — the most directly exposed US name | +0.188 | 🟡 | **+0.448 매집** | +2.9 | +10.6 | **0.52** |
| `LMT` | prime, indirect (Sikorsky/missiles, not hulls) | +0.544 | 🟡 | **+0.467 매집** | **+15.2** | +9.8 | 0.78 |
| `RTX` *(held)* | prime, missiles — no hull exposure | +0.467 | 🟡 | **+0.381 매집** | +10.8 | **+22.0** | 0.64 |
| `NOC` | prime, shipbuilding exited (Newport News → HII, 2011) | +0.429 | 🟡 | **+0.401 매집** | +7.9 | −0.5 | 0.58 |
| `HII` | **the pure-play US Navy shipbuilder** | — | **🚫 NOT IN UNIVERSE** | — | — | — | — |

🚨 **The single most exposed listed US name to this thread — `HII`, Huntington Ingalls — is not in
`us_top300` and therefore has no flow, RS, OBV or short reading on this desk at all.** That is the
`LNG`/`TSM` failure class (`M-univ`), reopened on a different name. **Not a signal; an inability to
measure.**
⚠ **All four measurable names are OBV-accumulating with positive RS20 and every one is 🟡 solely
because `vol_surge` < 1.2** — the artifact `SWEEP_READ §3` measured across 100 names.

**Future — both branches, dated:**
- **IF the thread keeps building (≥3 articles/day sustained) AND `GD` flow stays ≥ 0** → the policy is
  read as **capacity expansion** (more hulls, allied yards as overflow) ⇒ **track KPI: `GD` RS20 vs
  `SPY` at the 2026-08-21 close, currently +2.9.**
- **ELSE / KILL** → **if `GD` RS20 vs `SPY` falls below −3.0 by 08-21 while the thread is still
  building**, the market is reading the same policy as **margin compression for protected US yards**,
  and the "defense accumulation" reading of `M667` loses its shipbuilding leg.
- ⚠ **Anti-signal**: an unrelated defense-budget headline (CR, supplemental) inside the window
  confounds the read ⇒ VOID.

**Cell: STORY-ONLY → watchlist, dated re-check 2026-08-21.** *Money has not moved in the measurable
names (all 🟡, all sub-1.2 surge); the story is 24 hours old.* **Not handed to BET.**
**Handed to ROTATION and to DEEP-INDU**, which already owns `D249` (the INDU bracket measures `XLI`
while the position is defense) — this thread is a **third** object inside that same unresolved label.

---

## Card 2 — ★★★ **Optics is the AI bottleneck story of the week — and this desk's two highest-scoring names are in it, POST-catalyst**

| | |
|---|---|
| **Thread** | `optical transceiver` **BUILDING 0→6/day** (24 / 7d) · `co-packaged optics` 0→6 (27 / 7d) |
| **Outlets (hand-counted)** | `tomshardware` ×2 · `marketwatch` ×2 · `yahoo_finance` ×4 · `nasdaq` · `fool` · `scmp` — ⚠ **the "8 Stocks to Play the Boom in Optics" item is ONE syndicated piece appearing on 3 outlets**; counted once |

**Direction (body-read) — two legs, and they are NOT the same trade:**

**Leg A, POLICY, forward-looking:**
> *"**FCC proposes import ban on Chinese optical transceivers** — blockade targets key AI interconnects
> as **China holds 56% global market share**"* [`tomshardware` **08-11**]
> *"How optical interconnects and silicon photonics emerged as AI's next hot commodity — **looming
> US-China summit puts photonics into the crosshairs**"* [`tomshardware` 08-12]

**Leg B, EARNINGS, already printed:**
> *"**Lumentum sees sales more than double** as AI demand swells"* [`marketwatch` **08-11**]
> *"**Lumentum Earnings Top Estimates** Amid Supply Chain Constraints"* [`yahoo_finance` 08-12]
> *"Lumentum's stock **surges**, giving a further boost to the optical-networking trade"* [`marketwatch` 08-12]
> *"Cisco, **Coherent** Are Earnings Movers Late After Nebius, Lumentum, CoreWeave Lead AI Rally"* [`yahoo_finance` 08-12]
> *"**Coherent Falls 12%, Lumentum Drops 7%** as AI Optics Stocks Cool **Ahead of** Earnings"* [`yahoo_finance` **08-10**]

🚨🚨 **This is the card's finding, and it corrects this run's own SWEEP reading.** `SWEEP_READ §3`
recorded `COHR` (+0.990, the **highest flow score on the 299-name board**) and `LITE` (+0.817) as the
two **admissible** IT greens — the two names that survive the `D261` velocity adjustment. **They
survive because their `vol_surge` is 1.67 and 1.27 — and this body read dates that volume to their
own earnings prints on 08-11/08-12.**

⇒ **The two cleanest greens on the board are earnings-reaction volume, not accumulation.**
Written here rather than edited into `SWEEP_READ` (D48 class; **this stage's 1st self-refutation**).

**Exposure:**

| Ticker | Chain position | flow | Tag | OBV | RS20 | **RS60** | `vol_surge` |
|---|---|---|---|---|---|---|---|
| `COHR` | transceivers/lasers — **headline layer** | **+0.990** | 🟢 | +0.155 매집 | +12.9 | **−13.7** | **1.67** |
| `LITE` | transceivers/photonics — **headline layer** | +0.817 | 🟢 | +0.275 매집 | **+21.9** | −1.8 | 1.27 |
| `CIEN` | optical systems — **one hop past the headlines** | +0.342 | 🟡 | +0.031 중립 | +10.1 | **−26.7** | 0.90 |
| `GLW` | optical fibre/glass — **two hops, and the desk cannot search its name** | −0.173 | 🟡 | −0.021 중립 | +2.9 | −11.4 | 0.55 |

⚠ **`GLW` carries `Δ +0.419`, the 6th largest on the board**, and is the only name here the desk
**cannot body-search**: `D262` measured that FTS stems `Corning` → `Corn` and returns agricultural
futures. **Its Δ is visible and its story is not readable.** Named, not inferred.
★ **Every name in this chain has a NEGATIVE RS60.** The whole node is a turn inside a drawdown — the
same shape the 08-13 carry recorded, unchanged after earnings.

**Future — both branches, dated:**
- **IF Leg A (policy) is the driver** → the move survives the earnings fade. **Track KPI:
  `EW{COHR, LITE, CIEN}` 5-session excess vs `SPY` at the **2026-08-21** close.** ⚠ **This is
  already `S86`'s registered observable** (branches **A ≥ +12.584 · B ≤ −5.948**, sd 8.998 = the
  widest estimator on the board) — **no new bracket is registered; the existing one is named.**
- **ELSE / KILL** → **if `vol_surge` on both `COHR` and `LITE` falls below 1.2 by 08-21 and both
  lose the 🟢 tag**, the tag was the earnings print and nothing else, and this node returns to being
  a drawdown.
- ⚠ **Anti-signal**: if the FCC proposal is **withdrawn or deferred** at the US–China summit, Leg A
  is removed while Leg B has already printed ⇒ VOID the policy reading, keep the earnings one.

**Cell: LATE-MONEY, not CONFIRMED-EARLY.** *The money moved on the print, the print has happened, and
the price is still below where it was 60 days ago.* **A valuation/timing gate applies at BET; this
card does not hand `COHR`/`LITE` forward as fresh candidates.**
🚨 **Handed to ROTATION with one structural flag: `cycle_registry.json` has NO entry for
optical/interconnect** (28 days stale, `D250`) — **the desk's registry does not contain the cycle that
owns its two best-scoring names**, so PREMORTEM's Lens-4 GAP check is structurally blind to it.

---

## Card 3 — ★★★ **The distillate crunch has a named physical mechanism, and it is accelerating**

| | |
|---|---|
| **Thread** | `Russian refinery` · **BUILDING, accelerating** · 6·3·1·7·11·7·**17** (52 / 7d; 24 in the last 2 days) |
| **Outlets** | `oilprice` ×4 · `AP` (via `google_en`) · `aljazeera` · `yahoo_finance` — **4 independent** |

**Direction (body-read):**
> *"**Ukraine Strikes Gazprom's 200,000-Bpd Salavat Refinery** in the Urals"* [`oilprice` **08-13**]
> *"Ukraine's drones hit a major Russian refinery **800 miles from the border**, sparking a fire"* [`AP` 08-13]
> *"**Drone Strike Sparks Blaze at Key Russian Oil and Fuel Terminal**"* [`oilprice` **08-14**]
> *"**Russia's Diesel Exports Crash to Multiyear-Low** amid Tight Global Market"* [`oilprice`·`yahoo_finance` 08-13]
> *"**Refinery Attacks Deepen Global Diesel Supply Crunch**"* [`oilprice` 08-12]

⇒ **Unambiguously distillate-supply-destructive.** This is the **physical mechanism** behind `P62`
(MACRO §E), which was argued from futures alone: `HO=F` **+5.37% / 20d** while `CL=F` is **−0.11%**
and `RB=F` **−6.15%**. **Narrative and price agree on the same leg, from independent instruments.**

**Exposure:**

| Ticker | Chain position | flow | Tag | OBV | RS20 | **RS60** | `vol_surge` |
|---|---|---|---|---|---|---|---|
| `MPC` *(held)* | refiner — highest distillate leverage of the three | **+0.806** | 🟢 | +0.220 매집 | +9.3 | **+29.3** | 1.25 |
| `PSX` *(held)* | refiner | +0.628 | 🟡 | +0.139 매집 | +8.5 | **+22.3** | **1.01** |
| `VLO` | refiner — **not held** | +0.490 | 🟡 | +0.188 매집 | +5.9 | **+24.3** | 0.84 |
| `XOM` | integrated — **the name that owns Energy's `wflow`** | +0.244 | 🟡 | +0.073 중립 | +4.2 | **−7.3** | 0.85 |
| `CVX` | integrated | +0.401 | 🟢🚫 | +0.283 매집 | +2.3 | **−4.4** | 0.95 |

★★ **The refiner/integrated split is the cleanest sector-internal separation on the board**: three
refiners at RS60 **+22 to +29 vs `SPY`**; two integrateds at **−4 to −7**. A **36-point** spread inside
one GICS sector.
🚫 **`CVX`'s 🟢 is velocity-lit and inadmissible** (`D261`) — so the sector's only admissible green is
`MPC`, a refiner, exactly where the mechanism points.
⚠ **`PSX` and `VLO` are 🟡 on `vol_surge` 1.01 / 0.84 alone** — the two names carrying the second- and
third-best RS60 in Energy are filtered out of the desk's own shortlist by the volume leg
(`D251`, reproduced).

**Future — both branches, dated:**
- **IF the strikes continue AND the crack holds** → this is `P62` direction A. **Track KPI:
  `HO=F` 20-day return minus `CL=F` 20-day return at the **2026-08-21** close, currently **+5.48pp**;
  A holds while the gap stays **> +4pp**.**
- **ELSE / KILL** → **gap ≤ 0pp by 08-21** ⇒ it was a barrel move and the distillate framing dies.
- ⚠ **Anti-signal (as registered in `P62`)**: a **US** refinery outage or a PADD3 hurricane inside the
  window makes distillate strength domestic-supply, not Russia/Hormuz ⇒ VOID.

**Cell: CONFIRMED-EARLY** — narrative building **and** money already in the specific names
(`MPC` 🟢 admissible, `PSX`/`VLO` OBV-accumulating with top-of-sector RS60).
★ **Handed to ROTATION and BET §B as the run's strongest cross-evidence**, and it is the same node
`CYCLE_EXPOSURE` flagged: **rank-2 cycle, epicenter 7.10% vs 8.0% required, GAP −0.898pp.**

---

## Card 4 — ★★ **Hormuz escalated to a territorial claim while its coverage DECELERATED**

| | |
|---|---|
| **Thread** | `Strait of Hormuz` · **BUILDING, high plateau** · 108·70·192·236·252·188·**231** (1,277 / 7d) |
| ⚠ **Pool-normalised** | `Hormuz` **0.68× — DECELERATING** against a 1.782× pool |

**Direction (body-read):**
> *"**Trump vows to make Hormuz US territory 'pretty soon'**"* [`aljazeera` **08-15**] ·
> *"Trump says he'll soon declare Strait of Hormuz to be US territory"* [`scmp` 08-14]
> *"**UAE accuses Iran of attacks on two ADNOC vessels**"* [`aljazeera` 08-14]
> *"Ship traffic **near three-month low**"* [`cnbc` 08-12] · *"'Hormuz remains blocked'"* [`cnbc` 08-13]
> *"Iran's military rejects Trump's claims … as **'lies'**"* [`euronews` 08-13]
> *"**Hormuz Shock 'Manifesting Itself In Cracks, Not Crude,' Jefferies Says**"* [`zerohedge` 08-13]
> *"**Hormuz Stalemate Raises Risk of $120 Oil**"* [`oilprice` 08-13]

★★ **The card's finding is the divergence**: **coverage is decelerating (0.68×) while the tape pays
`XLE` +7.271 excess vs `SPY`, the best of eleven.** The desk's own term-velocity screen **did not find
this run's largest sector move** — the `M196` failure mode, reproduced on the US desk. ⇒ **term
velocity is not a discovery instrument for a story already at plateau.**

**Exposure:** the same refiner chain as Card 3 (Jefferies routes the shock to **cracks**, not crude),
plus the **`WTI` spec position at the 18th percentile SHORT** (COT 08-11) — the most asymmetric cell
on the positioning board.

**Future — both branches, dated:**
🚨 **This is the `CATALYST_WATCH` binary and it is UNDATED** (*"Iran 'Strait of Hormuz open' statement
(TACO trigger)"*, `🔀binary`, `"undated": true`). **The mandatory both-sides bracket is `S84`,
already registered and settling 2026-08-21**: `[XLE exc5] − [EW{XLU,XLRE} exc5]` vs `SPY`,
**A ≤ −3.174 · B ≥ +5.544**.
★ **Live state: +7.271 − (+1.207 + 0.246)/2 = +6.545 — ALREADY 1.00pp ABOVE branch B**, four sessions
before settle. **Reported, not scored** (D242 — terminal-date settlement, no improvised early read).
- **Kill condition**: an Iranian or US statement that the Strait is open ⇒ branch A's tick, and it
  would hit **`XLE` and four underweights simultaneously** — which is precisely why `S84` was made
  mandatory.

**Cell: LATE-MONEY** — the story is at plateau and 1,277 articles deep; **the crowded layer is the
headline layer.** The tradeable residue is the **distillate leg (Card 3)**, not Hormuz itself.
**PREMORTEM owns the both-sides discipline.**

---

## Card 5 — ★★ **The US consumer print is the week's real regime event, and the desk's most-exposed sector was the worst performer on it**

| | |
|---|---|
| **Thread** | `consumer sentiment` · **REIGNITED, spike** · 13·4·20·17·15·21·**85** (175 / 7d) |
| **Outlets** | `seekingalpha`, `nasdaq`, `yahoo_finance`, `investing_en`, `bloomberg` — **5 independent** |

**Direction (body-read):**
> *"**Fed rate hike odds sink further as retail sales, consumer sentiment fall**"* [`seekingalpha` 08-14]
> *"U.S. Consumer Sentiment Slumps **Much More Than Expected** In August"* [`nasdaq` 08-14]
> *"**Treasuries Rise as Weak Retail Sales Dampen Fed Rate-Hike Expectations**"* [`bloomberg` 08-14]
> *"Dow, S&P 500, Nasdaq **slip after stocks hit record high**, consumer sentiment declines"* [`yahoo_finance` 08-14]

**Exposure — and the flow reading is the opposite of the story's usual reflex:**

| Ticker | Position | flow | Tag | OBV | RS20 | RS60 |
|---|---|---|---|---|---|---|
| `AMZN` | 40.2% of Consumer Discretionary cap | −0.391 | 🟡 | **−0.117 분산** | +1.8 | −4.5 |
| `HD` | big-ticket discretionary | **−0.683** | 🔴 | **−0.230 분산** | −4.4 | +6.2 |
| `ABNB` | discretionary services — **the sector's only admissible 🟢** | **+0.881** | 🟢 | +0.116 매집 | **+21.6** | **+34.5** |
| `TGT` | staples/discretionary crossover | +0.503 | 🟡 | +0.115 매집 | +6.2 | +15.6 |

★ **`XLY` posted `exc5` −1.783 vs `SPY`, the worst of eleven**, in the same five sessions — the sector
that owns the consumer read was the worst performer on the consumer news. **Story and money agree, in
the negative direction.**
⚠ **But not uniformly**: `ABNB` is accumulating with **RS60 +34.5, the best in the exposure set**.
**Services ≠ goods** (**W5**): a weak-goods, firm-services split is exactly what this label collapses.

**Future — both branches, dated:**
- **IF the consumer read keeps deteriorating** → `P61` direction A (the front end trades on demand
  data). **Track KPI: `DGS2` ≤ 4.05% at the 2026-08-21 close** (currently 4.15) — already registered
  in `P61`, **not re-registered here**.
- **ELSE / KILL** → **if `XLY` exc5 vs `SPY` turns positive by 08-21 while `DGS2` is unchanged**, the
  08-14 move was a one-print reaction and the sector reading dies with it.
- ⚠ **Anti-signal**: a September-FOMC-dated headline or an inflation print inside the window
  confounds the rate leg ⇒ VOID (same anti-signal as `P61`).

**Cell: CONFIRMED-EARLY on the NEGATIVE side.** *This is a card about an underweight's mechanism, not
a candidate.* **Handed to ROTATION** — Consumer Discretionary's neutral wind now has a dated,
body-read driver it did not have on 08-14.

---

## Card 6 — ⚠ **Maia 300 is FADING, and the book still cannot express it**

| | |
|---|---|
| **Thread** | `Maia 300` · **FADING** · 0·0·3·7·4·2·**2** — peaked 08-11, now at 2/day |
| **Admitted because** | the rule permits FADING **only** where the book already holds exposure. The book holds **`NVDA` and `AVGO`** |

**Direction (body-read):**
> *"Microsoft plans Maia 300 chip reveal in **September**"* [`yahoo_finance` 08-10, citing The Information]
> *"Microsoft's Maia 300 Could Be a Win for **Marvell and TSMC**"* [`yahoo_finance` 08-11]
> *"**Microsoft Rethinks Its Nvidia Reliance**"* [`yahoo_finance` 08-10]

**Exposure and the carried problem, re-measured today:**

| Ticker | Side of the displacement | flow | Tag | RS20 | **RS60** | Δ |
|---|---|---|---|---|---|---|
| `MRVL` | **named beneficiary** | +0.378 | 🟢🚫 velocity-lit | +13.2 | **+20.1** | 0.000 |
| `NVDA` *(held)* | **displaced** | +0.458 | 🟢🚫 velocity-lit | +6.6 | **−3.7** | +0.050 |
| `AVGO` *(held)* | custom-silicon incumbent — **the other side** | +0.207 | 🟡 | +1.5 | **−10.2** | **−0.199** |

★ **The carried `§3a` row holds on a second date**: `MRVL` **RS60 +20.1** against `NVDA` **−3.7** and
`AVGO` **−10.2**. **The book is long both sides of the displacement and can express neither
direction.**
🚨 **And both greens here are velocity-lit** (`D261`) — so the 08-15 board gives **no admissible flow
evidence at all** on the AI-compute epicenter the desk is 16.54% exposed to.

**Future — both branches, dated:**
- **IF the September reveal happens as reported** → the displacement is confirmed at product level.
  **Track KPI: `MRVL` RS60 minus `NVDA` RS60 vs `SPY`, currently +23.8pp**, at the **2026-08-27**
  close (NVDA's own print).
- **ELSE / KILL** → **spread ≤ +10pp by 08-27**, or a Microsoft statement deferring Maia 300 ⇒ the
  card dies and `NVDA`'s 08-13 downgrade loses its named substitute.
- ⚠ **Anti-signal**: NVDA's 08-26/27 earnings are inside the window and will move both legs for
  reasons unrelated to Maia ⇒ if the print lands first, the spread is read **as of 08-26 close**.

**Cell: STORY-ONLY, re-filed rather than dropped.** ⚠ **The thread is FADING but `MRVL` is
accumulating (OBV +0.168) with the node's best RS60** ⇒ by the stage's own rule, **DEAD requires BOTH
axes** and the money axis is not dispersing. **Re-filed with a dated re-check of 2026-08-27, not
dropped.**

---

## 2 · Ledger writebacks

### 2a · Rejections (`reject_ledger`) — every drop carries a revival condition

| Name/thread | Why dropped | `--revives-if` |
|---|---|---|
| `custom AI silicon` (thread) | **3 articles / 7 days** — below any measurable threshold; not a thread | ≥10 articles in a 7-day foreign window |
| `sanctions Iran` (thread) | **4 / 7d**, and the substance is inside Card 4 | ≥15 / 7d **and** a dated sanctions action |
| `tanker rates` (thread) | flat at ~1/day; **`D258` already recorded that the name-string route is defective here** — the correct observable is a **RATE (Baltic VLCC TCE)**, which this desk does not pull | a Baltic VLCC TCE print, or ≥5 articles/day |

### 2b · Misses (`missed_ledger`) — threads that cleared the money axis and did NOT become cards

| Name | Class | Why it is a miss, not a drop | `--enters-if` |
|---|---|---|---|
| **`HBM4`** | `Q.확신부족` | 40 articles / 7d with a real curve, and it sits on the desk's **stated regime call** (memory RoC deceleration). Not carded because the curve is **choppy (5·1·8·10·7·1·8)** and no single direction body-read was done — **an admission of insufficient work, not a judgement** | a 3-day rising curve **or** an issuer filing with an HBM4 price/volume term |
| **`CXMT`** | `M.숏리스트탈락` | pool-norm **0.62×, decelerating**, so it failed the screen — but `P43` has carried *"CXMT is an uncovered supply-side axis"* for **6 runs with the filing leg still unread** | any **filing** (Apple qualification, CXMT prospectus) or ≥2.0× pool-normalised |
| **`GLW`** | `Q.확신부족` | **Δ +0.419, the 6th largest on the 299-name board**, and it sits inside Card 2's chain — **but `D262` makes its name unsearchable** (`Corning` → `Corn`). Carried as unmeasurable rather than judged | a ticker-resolved search path, or `GLW` entering the 🟢 set on an admissible axis |

⚠ **The `GLW` row is the honest one**: it is not that the desk decided against it, it is that the
desk's search layer **cannot read it**, and that has been true since `D262` was registered on 08-14.

## 3 · Book cross-check — ENDED threads under open positions

**No ENDED thread sits under an open position.** One **FADING** thread does — **Card 6 (Maia 300),
under `NVDA` and `AVGO`, 16.54% of the book's AI-compute epicenter exposure.** Flagged to the book
desk: **the position's thesis rides a thread that peaked five days ago, and the book holds both sides
of the displacement it describes.** Re-justification date **2026-08-27** (NVDA print).

## 4 · Hand-off

| To | What |
|---|---|
| **ROTATION** | **Card 3 CONFIRMED-EARLY** (Energy/refining — narrative + money + a `CYCLE_EXPOSURE` GAP on the same node) · **Card 5 CONFIRMED-EARLY-negative** (DISC now has a body-read driver) · **Card 2 LATE-MONEY** (IT's admissible greens are earnings volume — do **not** read them as accumulation) · **Card 1 STORY-ONLY** (a third unmeasured object inside `D249`'s Industrials label) |
| **BET §B** | **Card 3 only.** Cards 1, 2, 4, 6 are STORY-ONLY or LATE-MONEY and **do not** enter the candidate hand-off |
| **PREMORTEM** | **Card 4** — the undated Hormuz binary, bracketed by `S84` (live state already above branch B) |
| **DEEP-INDU** | **Card 1** — `HII` is unmeasurable, `GD`/`LMT`/`NOC`/`RTX` are all accumulating-but-volume-blocked |

## ✅ EXIT CHECK
- [x] **Scope market-correct** — `--scope foreign` on every one of the ~60 remote calls. No
      cross-market feed is cited in any card.
- [x] **Selection logged** — 13 candidates curved → **6 selected, 7 not selected and named with their
      curves.** No silent cap.
- [x] **Every card has a direction body-read**, with the quoted evidence line and its outlet+date.
      ★ Two body reads **changed** the card: Card 2's earnings dating turned a CONFIRMED-EARLY into a
      **LATE-MONEY**, and Card 4's pool normalisation turned a 1,277-article thread into
      **decelerating**.
- [x] **Every exposure name carries a flow tag with asof (2026-08-14)**; `D261`-disqualified greens are
      marked 🚫 wherever they appear. **STORY-ONLY names did not leak into the BET hand-off** — only
      Card 3 is handed forward.
- [x] **Every card has both branches, a kill condition and a dated horizon.** Where an existing
      bracket already owns the observable (`S84`, `S86`, `P61`, `P62`) it is **named rather than
      duplicated** — no new bracket was minted to look productive.
- [x] **Ledger writebacks specified** — 3 rejections with `--revives-if`, **3 misses with
      `--enters-if`** (the funnel's widest stage has a scoreboard).
- [x] **Book flag emitted** — Card 6, FADING under `NVDA`/`AVGO`, re-justification 2026-08-27.
- [ ] ⚠ **`thread --days 7` NOT run** — structurally impossible on this client (§0). The substitute is
      declared, its specific weakness (articles, not outlets) is stated, and outlets were hand-counted
      on every card. **Left unticked rather than ticked on a substitute.**
