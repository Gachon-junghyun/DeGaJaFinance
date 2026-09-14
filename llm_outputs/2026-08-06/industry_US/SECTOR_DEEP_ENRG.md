# SECTOR_DEEP_ENRG — Energy · industry_US · 2026-08-06 · **ROTATING slot, dived 08-05 ⇒ DELTA-LED**

> Value-chain names, segment coverage and the 08-04 adjudications are carried **by reference** to
> `llm_outputs/2026-08-05/industry_US/SECTOR_DEEP_ENRG.md` (which itself references 08-04). Unchanged
> structure is not re-printed. Benchmark **SPY**, inline (C1). **P4: analysis only — no positioning,
> no sizing, no order language.**
> ⚠⚠ **D74**: last settled US session = **2026-08-05**. The 08-06 bar is partial and appears **only**
> tagged 🟡live, carrying **no verdict**, in one place (§1).

---

## 0 · The mandate, answered in one line

**The 0.285 concentration gap is neither early nor a trap — it is arithmetic, and the fact it is
hiding is that the refining leg's 20-day relative strength COLLAPSED on the settled 08-05 bar
(MPC RS20 vs SPY **+14.2 → +2.8 in one session**, on a **−4.75%** day, **24 hours after a +219%
net-income print**) while its 60-day alpha and its revision book remain the only real ones in the
sector.** [measured, own calc `yfinance` settled + `SECTOR_FLOW_US.json` 08-05/08-06 files]
⇒ **The verdict must be written about REFINING, not about "Energy"** (§2 quantifies B5: sub-node
spread **~18pp** against a sector move of **−1.5pp vs SPY** — the label fails its own dispersion
test). ⇒ **On the refining leg the honest tag today is EARLY-ON-THE-BOOK / DE-RATING-ON-THE-TAPE,
which is `INDISTINGUISHABLE` this session (C4)** and resolves on one number: whether RS60 holds.
⇒ **The physical object is VERIFIED as to class and REFINED as to exclusivity** (§3): it is
conversion capacity, not a strait — corroborated by **XOM's CEO on the record** — but Russia is
**one of four** named capacity legs, and Kpler ranks China's export quota as comparable.
⇒ **S55: branch B is the live one on the running number and the conditional base rate flips in its
favour, but 75% of the mass is "neither"** (§7).

---

## 1 · The delta since 08-05 — five things, four of them new numbers

Yesterday's file (i) scored **S53 branch A** on MPC/PSX, (ii) found the refining tier monotonically
strongest on every flow column, (iii) rejected the Russian "lull" as `unknown`, (iv) registered the
crack's rate structure. **(i), (ii) and (iv) are carried; (iii) is now RESOLVED AGAINST the lull —
see §3.** New today:

| # | Delta | Number |
|---|---|---|
| **D-1** | 🚨 **The refining leg's RS20 broke, hard, in ONE session** | MPC **+14.2 → +2.8** · VLO **+12.8 → +3.6** · PSX **+12.0 → +4.6** vs XOM **+5.5 → +4.2** · CVX **+6.3 → +2.7**. Settled 08-05 moves: **MPC −4.75% · VLO −2.05% · PSX −1.62%** against **WTI −0.73% · SPY −0.20%** |
| **D-2** | ★ **Lens 3's "PSX sign flip" is a four-observation TREND, not a flip** | d21-60 (RS60−RS20): **−5.5 (07-31) → +1.4 (08-03) → +4.9 (08-04) → +9.1 (08-05)**, monotone. **But see §2b — it rose because RS20 fell, not because the base rose** |
| **D-3** | ★★★ **The crack's step-up is a JULY event and PSX's miss is an APRIL–JUNE number** | distillate crack **Q2-26 avg 64.47 → July-26 avg 84.09 (+30.4%)** [own calc, settled]. **The calendar refutes the mandate's premise on (iv) — §3b** |
| **D-4** | ★★ **The two 🟢 names' estimate breadth is net-DOWN; the three 🟡 names' is net-UP** | XOM CY 30d **4↑/12↓**, 7d **0↑/4↓** · CVX NQ 30d **2↑/11↓** vs MPC CY 30d **11↑/0↓** · VLO CY 30d **12↑/2↓** · PSX CY 30d **13↑/2↓**, 7d **5↑/0↓** [`module_fundamentals_us`] |
| **D-5** | ⚠ **XOM's short-volume printed a 🔴 spike on the same bar its green lit** | FINRA short% **65.1% vs 42.7% base, z +2.73** (≥+1.5 = spike). CVX **−1.34** (covering) · VLO +1.10 · MPC −0.02 · PSX −0.54 [`us_flow.py`, 08-05] |

🟡**live, no verdict (D74)**: at pull time the 08-06 partial bar reads WTI **75.20**, distillate crack
**84.799**, gasoline crack **36.617**, dist−gas **48.182**; MACRO §0 quoted the same bar minutes
earlier at WTI 76.41 / 83.131 / 35.033 / 48.098. **Two reads of one unsettled bar, both recorded, and
neither used below (C2/D74).**

---

## 2 · Flow, decomposed by sub-leg — where the gap actually comes from

### 2a · The sector aggregate is two mega-caps carrying fourteen names

`SECTOR_FLOW_US.json`, **asof 2026-08-05 settled**, n=16.
**wflow +0.230 (rank 3 of 11) · eqflow −0.055 · delta −0.129 (LAST of 11) · 🟢2 / 🔴5 / breadth 0.12.**

XOM (**$571B**) and CVX (**$346B**) are **~55% of the sector's measured cap** and are the only two
positives large enough to move a cap-weighted mean; the equal-weighted mean is negative. **The 0.285
gap is therefore not a timing signal — it is the mechanical difference between a cap-weighted and an
equal-weighted average over a 16-name set with two dominant members.** [measured, own calc on the
flow file's own `mcap` field]

**And the delta that ranks LAST is the refiners' own:**

| ticker | flow 08-04 → **08-05** | Δ | RS20 vs SPY | RS60 vs SPY | OBV | `vol_surge` | tag |
|---|---|---|---|---|---|---|---|
| **PSX** | 0.656 → **0.338** | **−0.318** | +12.0 → **+4.6** | 16.9 → **13.7** | **중립** | 1.09 | 🟡 |
| **VLO** | 0.628 → **0.351** | **−0.277** | +12.8 → **+3.6** | 25.2 → **21.1** | 매집 | 0.99 | 🟡 |
| **MPC** | 0.589 → **0.422** | **−0.167** | +14.2 → **+2.8** | 23.6 → **17.2** | 매집 | 0.95 | 🟡 |
| **XOM** | 0.496 → **0.569** | **+0.073** | +5.5 → +4.2 | −0.4 → **+0.5** | 매집 | **0.85** | **🟢 velocity-only** |
| **CVX** | 0.590 → **0.580** | −0.010 | +6.3 → +2.7 | −1.1 → **−1.7** | 매집 | **0.99** | **🟢 velocity-only** |

★★★ **The three largest negative deltas in the sector are the three refiners, and the only positive
delta is the velocity-lit mega-cap.** The sector's last-place delta is **the money leg de-rating**,
not the laggards deteriorating further. **This is the opposite of "early".**

### 2b · The `d21-60` re-tag is real but it is being manufactured by the wrong leg

**D-2's monotone series is arithmetically driven by the RS20 term, not the RS60 term** [measured,
five consecutive flow files]:

| | 07-31 | 08-03 | 08-04 | **08-05** | net |
|---|---|---|---|---|---|
| **PSX** RS20 / RS60 | 19.7 / 14.2 | 15.4 / 16.8 | 12.0 / 16.9 | **4.6 / 13.7** | RS20 **−15.1** · RS60 **−0.5** |
| **MPC** RS20 / RS60 | 18.5 / 18.3 | 13.3 / 21.7 | 14.2 / 23.6 | **2.8 / 17.2** | RS20 **−15.7** · RS60 **−1.1** |
| **VLO** RS20 / RS60 | 16.6 / 20.2 | 12.9 / 26.7 | 12.8 / 25.2 | **3.6 / 21.1** | RS20 **−13.0** · RS60 **+0.9** |

⇒ **`d21-60 = RS60 − RS20` is not sign-invariant to which leg moves.** All three refiners' segments
"improved" on a measure whose improvement came from **the near window collapsing**. **A name whose
20-day excess falls 15pp while its 60-day excess is flat is not building a base — it is spending
one.** ★ **This does not overturn Lens 3's tag; it re-specifies it**: `EXTENDED-BUT-LIVE` on
`d21-60` + revision book is **still satisfied on the KPI half** (§2c), but the price half is
carrying the opposite sign to the one the segment measure implies. **Registered as a method finding,
not smoothed.** ⚠ **C2, the other half**: SPY itself ran **+5.5% in 5 settled sessions**, which
inflates every RS denominator — but on the 08-05 bar alone SPY was **−0.20%** and MPC **−4.75%**, so
**the single-session RS20 destruction is name-specific, not a denominator artifact.**

### 2c · The revision axis says the exact opposite of the tag axis (D-4, resolving mandate (ii))

`module_fundamentals_us`, pulled today. **90d estimate change AND up:down breadth, both halves (B2):**

| | fwd P/E | CQ 90d | CY 90d | **CY 7d Δ** | CY breadth 30d | CY breadth 7d |
|---|---|---|---|---|---|---|
| **VLO** 🟡 | 10.77 | +76.7% | **+47.6%** | **41.25 vs 35.41 = +16.5%** | **12↑/2↓** | 4↑/1↓ |
| **MPC** 🟡 | 10.08 | +60.1% | +72.3% | ⚠ **39.08 vs 40.22 = −2.8%** | **11↑/0↓** | 9↑/1↓ |
| **PSX** 🟡 | 10.30 | +60.1% | +30.0% | +0.5% | **13↑/2↓** | **5↑/0↓** |
| **XOM** 🟢 | — | +10.6% | +9.0% | +5.6% | 🚨 **4↑/12↓** | 🚨 **0↑/4↓** |
| **CVX** 🟢 | — | +9.4% | +12.8% | +7.5% | 9↑/7↓ (NQ **2↑/11↓**) | 4↑/1↓ |

★★★ **Mandate (ii) resolves, and it resolves the same way on two independent axes.** The money map
(RS60 **+13.7 / +17.2 / +21.1** vs SPY) and the consensus-revision map (CY 30-day breadth
**13↑/2↓ · 11↑/0↓ · 12↑/2↓**) both point at the **refining** sub-leg. The tag map points at two
names whose **30-day estimate breadth is net-NEGATIVE on three of four lines (XOM) and on the
next-quarter line (CVX 2↑/11↓)** and whose green is **velocity-only at `vol_surge` 0.85 / 0.99**
(`SWEEP §2`, D6 grade: news-count ignition). **⇒ The sector's verdict is to be written about
MPC/VLO/PSX. The 🟢 filter is naming the wrong leg on both the price axis and the estimate axis.**

★ **(v) cross-checked and CONFIRMED exactly**: VLO's CY line is **41.25 today vs 35.41 seven days
ago = +16.49%** — Lens 3's "+16.5% in a single week" reproduces to the decimal on an independent
pull. PSX's d21-60 sign change reproduces (**−5.5 → +9.1**) with the D-2 refinement above.

### 2d · B2, stated where it hurts — the peak-margin / low-multiple test

**All three refiners are "cheap on forward multiple" (10.08 / 10.77 / 10.30) with estimates revised
up 30–77% in 90 days. B2 says that is consensus chasing until proven otherwise. Where the margin
sits in its own history:**
- **Node level [measured, own calc]**: distillate crack **84.220 = 92.1st percentile** of its own
  trailing 252 settled sessions; dist−gas **40.211 = 93.7th**. **Top decile.**
- **Company level [news, `nasdaq`/Zacks body 08-05 + `seekingalpha` 08-04]**: PSX worldwide realised
  **$24.08 vs $11.25 a year earlier (2.14×)**; MPC **$36.33 vs $17.58 (2.07×)**. **Both roughly
  doubled YoY.**
- ⚠ **VLO is UNMEASURABLE on the quarterly-XBRL margin route, as B2 anticipated**:
  `module_fundamentals_us VLO` returns **"XBRL 데이터 없음 또는 skip"** — the SEC cross-check block is
  empty. **No margin percentile is invented for VLO. `unknown` (C3).**

**Both halves (C2) — what argues AGAINST the trap reading:** a peak-margin trap requires consensus
to **extrapolate** the peak. It does not, on two of three names. **VLO's own consensus already models
CQ 14.90 → NQ 9.35 = −37.2% sequential; PSX 8.09 → 5.25 = −35.1%.** **MPC is the exception and is
therefore the name most exposed to B2**: **CQ 13.95 → NQ 15.50 = +11.1% sequential**, i.e. consensus
is still raising Q4 — and **MPC's annual lines ticked DOWN week-on-week while its near quarters ticked
up (CY 40.22→39.08, NY 29.19→27.77)**. **Consensus is moving earnings out of the out-years and into
the next two quarters. That is the late-cycle shape, named, on the desk's own held name.**
★ **This is exactly Lens 3's registered MPC flip condition** (*"a 2nd consecutive weekly cut to the CY
line"*) **and week 1 of it has now printed.**

---

## 3 · The physical object — verified, refined, and one attribution refuted

### 3a · R46's object: CONFIRMED as to class, by the operator itself

`module_news_data fts --scope foreign`, bodies read. **The strongest evidence is a primary operator
statement the desk did not have yesterday:**

> **ExxonMobil CEO Darren Woods, on the record to CNBC (Fri 07-31)**: *"I think this refining
> challenge is going to be with the world for a while… **Even after the Strait opens up**, we'll see
> more products start to flow through the Strait… But we've still got **the Russia capacity that's
> been lost**, and we'll have to see what the Chinese do with respect to exporting."*
> [`cnbc` 08-03, full body]

★★★ **The CEO of the sector's largest name separates the transit route from the lost conversion
capacity, unprompted, and states that opening the Strait does not resolve the product tightness.**
That is **R46 confirmed by the physical object's own operator**, and it is the class of evidence
S55's VOID condition names.

**The volumetric claims, verified by direct body-read** [`oilprice` 08-03, citing *The Moscow Times*
citing **Bloomberg analysis**]: Russian refineries processed **3.6 mbpd in July, the lowest monthly
level since May 2002**, ~⅓ below the **5.3–5.6 mbpd** 2020–25 seasonal norm · **18 Russian refineries
struck in July**, beating the prior record of 17 set in May · **Omsk, 440 kbpd, Russia's largest**,
>2,500 km from the border · **30 attacks on Russian oil infrastructure in July**, second-highest
month of the war · *"Last week, Russia extended its ban on most diesel and gasoline exports."*
⚠ **D5 cross-provider, stated honestly**: the headline volumetric number still traces to **one
analytic provider (Bloomberg)** through two republications. **MACRO §0-b's caveat stands unchanged.**

**Independent corroboration this stage adds, from three different providers:**
1. **Kpler** [`toi` 08-04, full body]: India exported **1.53 mbpd of refined fuels in July, a
   1-year high, +27% vs the 12-month average**, the highest July since Kpler's series began in 2017 —
   *"Exceptionally strong diesel margins, **following the ban on Russian diesel exports**,
   incentivised exports… **to fill the supply void**"*; Turkey now replacing Russian fuel with Indian
   cargoes; *"**Europe remains short on diesel supplies**… record-high diesel refining margins had
   encouraged higher export volumes to Europe."*
2. **Standard Chartered** [`oilprice` 08-05, full body]: the **ICE gasoil–Brent crack (European
   diesel) exceeded $75/bbl on 31 July, close to a 20-year high** — a *different instrument, different
   geography, different analyst*, agreeing with this desk's NYMEX-based percentile.
3. **EIA** [via `hellenicshipping` 08-01, "Source: EIA"]: **record global inventory draws of 5.1 mbpd
   in 2Q26**; China's 2Q26 crude imports **8.1 mbpd, −32% QoQ**, below 8.0 mbpd in May and June for
   the first time since 2016. **A primary-agency datum, and it cuts both ways (C2) — record draws are
   tightness, a −32% Chinese import collapse is demand destruction.**

**My own D5 check on the core observable** [own calc, settled]: recomputing the distillate crack
against **Brent** instead of WTI gives **79.99, the 94.0th percentile** of its trailing year, 5d
**−12.814**, 21d **+15.479**, 63d **+20.592** — structurally identical to the WTI-based read
(84.220 / 92.1st / −14.864 / +15.989 / +17.222). **Two crude benchmarks, one answer.**

### 3a-2 · REFUTED: the exclusivity of the Russian attribution — it is FOUR legs, not one

[`oilprice` 07-30, full body, quoting **EIA** data and **Kpler**'s Matt Smith via Bloomberg]:
US refineries produced **17 mbpd of fuels last week, the highest since September 2019**, at
record margins, **and the world is still short**. The body names the constraint stack explicitly:
**(1)** the Gulf-state **product**-export disruption (*"the Gulf states were not only major exporters
of crude — they also exported quite a lot of refined products"*) · **(2)** **European refinery
closures** (structural) · **(3)** **China's fuel-export quota policy** — and **Kpler ranks this "not
less important than Russia's drop in refinery output"** · **(4)** Russia's capacity loss and export
ban. **A fifth, cyclical leg arrived 08-05**: **European heat/drought** derating refinery cooling and
constraining Rhine/Danube barge logistics [StanChart via `oilprice` 08-05].

⇒ **Verdict on (iii): the ATTRIBUTION IS CONFIRMED AS TO CLASS and PARTIALLY REFUTED AS TO
EXCLUSIVITY.** R46's rule holds completely — the spread is set by **facilities, not a transit route**,
and the operator says so. But **"the distillate leg is set by Russian refining capacity plus a Russian
export ban" is too narrow**: it is one of four named capacity legs, and the provider closest to the
data (Kpler) ranks China's quota as comparable. **The desk should carry the object as
"distillate-capable conversion capacity outside the US", with Russia as its largest single named
component.**

### 3a-3 · And yesterday's open `unknown` is now RESOLVED — against the "lull"

Yesterday's §4 left the 08-04 Bloomberg *"Lull in Drone Strikes Boosts Refining"* claim as
`unknown` on three grounds. **Two independent bodies now close it:**
- [`oilprice` 07-31, full body] **Ukraine struck Lukoil's Volgograd refinery (300 kbpd) on 07-31**,
  confirmed by **Ukraine's Security Service (Telegram)** *and* **Volgograd governor Andrei Bocharov**
  — *"The renewed drone attacks on refineries come **after several weeks of a lull**"*. **The lull
  ended on the day it was being reported.**
- [`oilprice` 08-03, full body, **Sergei Vakulenko, Carnegie Russia Eurasia Center**]: *"Refinery
  strikes resumed during the final week, with **three large plants hit during the last three days of
  July and four more attacked over the weekend**."*
⇒ **The "lull" was a mid-July operational window that had already closed before it was published.
`S55`'s VOID condition is NOT met, and the direction of the error was toward the desk's own thesis,
which is why it is stated plainly.** ★ Second-order: the same 07-31 body records Deputy PM **Novak**
saying the fuel crisis *"had started to ease"* — **and the export ban being extended anyway**, which
the body itself reads as *"a sign that the situation has not improved too much."*
⚠ **C2/C3 on the ban's end-date**: `oilprice` 07-31 says extended *"from July 31 **to the end of the
year**"*; the desk's 07-30 read said **"through January 2027."** **Direction agrees (EXTENDED);
the end-date does not. Both recorded; neither is resolved here.**

### 3b · ★★★ (iv) — PSX's Atlantic Basin miss: the calendar refutes the premise, and the 10-K kills the obvious explanation

**The mandate's premise is that Europe is closest to the Russian shortfall, so the miss is the
mechanism. Two measured facts break that chain.**

**(1) The shortfall's price expression postdates the reported quarter by a month.** [own calc,
settled bars] The distillate crack averaged **64.47 across Q2-26 (Apr–Jun, n=62 sessions)** and
**84.09 across July-26 (n=22) — a +30.4% step-up entirely OUTSIDE PSX's Apr–Jun window.** The
Brent-based crack does the same (**60.22 → 78.80, +30.9%**). **A Q2 realised margin cannot be caused
by a July price regime.** The ICE gasoil–Brent 20-year high is dated **07-31**; the Kpler Indian
export surge is **July**; the 18 refinery strikes are **July**; the ban extension is **07-31**.
**Every element of the Russian mechanism is post-quarter.**

**(2) The company's own 10-K kills the yield explanation.** [**PRIMARY: PSX 10-K, filed 2026-02-20,
accession 0001534701-26-000006, period 2025-12-31**, capacity table read directly]

| PSX segment | refineries | net crude throughput kbpd | gasolines / distillates (clean-product capability) | **% of company** | Q2 realised $/bbl vs 4-analyst est |
|---|---|---|---|---|---|
| **Atlantic Basin/Europe** | **Bayway** (Linden NJ 258) · **Humber** (N. Lincolnshire UK 221) · **MiRO** (Karlsruhe DE, 18.75% JV, 58) | **537** | 277 / 272 = **50.4% gasoline** | **27.6%** | 🚨 **14.44 vs 19.77 = −27.0%** |
| Central Corridor | Ponca City · Billings · Wood River · Borger | 777 | 433 / 315 = **57.9% gasoline** | 39.9% | 29.56 vs 26.35 = **+12.2%** |
| Gulf Coast | Lake Charles · Sweeny | 529 | 263 / 247 = 51.6% | 27.2% | 24.25 vs 22.42 = **+8.2%** |
| West Coast (= "Western/Pacific") | **Ferndale WA only** | **105** | 65 / 39 = **62.5% gasoline** | **5.4%** | **29.65 vs 19.93 = +48.8%** |

★ **Capacity-weighting these four realised margins reproduces the reported worldwide number to
within 0.5%** (23.96 computed vs **24.08 reported**) — **which validates the weights and lets the
miss be sized**: had Atlantic Basin merely hit its estimate, worldwide margin would have been
**$25.43 vs the $23.15 estimate = a +9.9% beat instead of +4.0%.** **The one regional miss removed
~$1.47/bbl of worldwide margin — roughly 60% of the potential beat — because it sits on 27.6% of the
company's crude capacity while the +48.8% beat sits on 5.4%.**
★★ **And the yield hypothesis is refuted, not asserted**: the **most** gasoline-weighted segments
(**Central Corridor 57.9%**, **West Coast 62.5%**) **BEAT**; the balanced one (50.4%) **missed**.
**It is not a gasoline-mix artifact.**
★ **The feedstock hypothesis is weak too**: Brent−WTI averaged **4.25 in Q2-26** against a trailing-
252-day mean of **4.62** — **narrower than normal**, so a "European refiners paid up for Brent-linked
crude" story is not supported. [own calc, settled]

⇒ **Answer to (iv): the Q2 miss is NOT the Russian mechanism — the calendar forbids it. What survives
is narrower and more useful: Atlantic Basin/Europe is PSX's structurally weakest capture node, it is
52% European by capacity (Humber + MiRO = 279 of 537 kbpd), and it is the segment where the two
July/August forces land in OPPOSITE directions** — the European gasoil crack at a 20-year high
(positive) against heat/drought cooling derate and barge constraints plus record Indian import
cargoes (negative). **C4: the two candidate explanations are INDISTINGUISHABLE on Q2 data alone.**
**The discriminator is dated and it is the single highest-information number the refining leg will
produce: PSX's Q3 Atlantic Basin realised margin.** If the "timing lag" reading is right, that line
should be the largest positive surprise of the print; if the "structurally contested basin" reading is
right, it misses again — **which is precisely Lens 3's registered PSX flip condition (*"a 2nd
Atlantic-Basin margin miss"*), and this section is why that condition is well-chosen.**

---

## 4 · Value chain, left → right — 8 nodes, binding constraint marked

> **Strong demand is not a bottleneck.** The binding node is the one that is running flat out and
> still failing to clear.

| # | Node | State, with receipt | Binding? |
|---|---|---|---|
| 1 | **Crude production / OPEC+ spare** | Record **global inventory draws 5.1 mbpd in 2Q26** [EIA via `hellenicshipping` 08-01]; WTI nonetheless **−21.2% / 60 settled sessions** [own calc] | **No** — tight but repricing DOWN |
| 2 | **Crude transit** (Hormuz · Black Sea · Novorossiysk) | Hormuz narrative **decaying 20→4 outlets** [`EVENT_ALPHA` Card 1]; Novorossiysk loadings **4 tankers w/e 07-26 vs 7 and 8 prior** [Bloomberg via `oilprice` 08-03] | **No — and this is R46's whole point.** *"Even after the Strait opens up… we've still got the Russia capacity that's been lost"* — **XOM CEO, on the record** |
| 3 | 🔒 **DISTILLATE-CAPABLE CONVERSION CAPACITY (ex-US)** | **US refineries at 17 mbpd, highest since Sept 2019, at record margins — and the world is still short ~8% of global diesel demand** [EIA + Lipow Oil Associates via `oilprice` 07-30 / `cnbc` 08-03]. Four named legs: Russia **3.6 vs 5.3–5.6 mbpd** · Gulf **product** exports disrupted · European closures **+ heat derate** · **China's export quota** (Kpler: "not less important than Russia") | 🔒 **BINDING.** Running at maximum and not clearing = the definition |
| 4 | **Product logistics / freight** | India→Europe/Turkey at a **1-year high, 1.53 mbpd, +27%** [Kpler via `toi` 08-04]; Rhine/Danube **barges carrying smaller loads** [StanChart via `oilprice` 08-05]; war-risk freight **S61** running against the leg (STNG RS20 −7.51, FRO −4.55) | **No** — cost-adding, and it is the leg **competing away** the Atlantic Basin's capture (§3b) |
| 5 | **US refiner realised capture** — MPC · VLO · PSX | The rent-collecting node. Q2: MPC **$36.33/bbl vs $17.58 y/y**, capture **112%** of benchmark; PSX **$24.08 vs $11.25**. Revision books **11↑/0↓ · 12↑/2↓ · 13↑/2↓** (CY, 30d) | **No** — but it is where node 3's scarcity rent lands |
| 6 | **Marketing / retail** | AAA: US average diesel **$5.36/gal**; **California $6.92, up from $5.10 pre-war (+35.7%)** [`cnbc` 08-03] | **No** — pass-through is happening |
| 7 | **End customers (A6)** | ~**⅓ of US containership imports/exports** move through San Pedro Bay and are hauled at California fuel prices; *"these prices influence freight costs, transportation margins, and ultimately the delivered cost of goods nationwide"* [**JPMorgan, Natasha Kaneva**, June note, via `cnbc`]. **Disclosed spend: next prints are OCTOBER — rails and airlines all reported Q2 in July.** Tape now: **DAL RS60 +22.7 (OBV 매집) · UAL +29.0 · CSX +9.7 · NSC +5.2 · UNP +7.3** vs **ODFL 🔴 · FDX 🔴** [flow file] | **No.** ⚠ **C2: the customer is NOT visibly breaking** — airlines carry the best RS60 in transport. **That is evidence against a demand-destruction end to the cycle, and it is quoted because it cuts the desk's way** |
| 8 | **Demand destruction / substitution** — the release valve | **China 2Q26 crude imports −32% QoQ, below 8.0 mbpd for the first time since 2016** [EIA]; NH winter **heating-oil restock** still ahead [`oilprice` 07-30] | **No, not yet** — the one node that could end the cycle without any facility being repaired |

⇒ **B5 fires, quantified.** 60-session excess vs SPY: **VLO +21.1 · MPC +17.2 · PSX +13.7** against
**XOM +0.5 · CVX −1.7 · XLE −1.5 · XOP −4.3** — a **~18pp** sub-node spread against a **−1.5pp**
sector move. **"Energy" is not the unit; "refining" is, and even that splits by geography inside one
company by 2.05× (§3b).**

---

## 5 · Chain-hop candidates — body-proximate only, each with a flow cross-check. **ZERO reach BET.**

`module_news_data chain-hop "distillate" diesel --days 7` (397 articles scanned) and
`chain-hop "Russian refinery" gasoil --days 7` (**29 articles scanned**).

| Candidate | proximity / body | Flow cross-check (08-05 settled) | Disposition |
|---|---|---|---|
| **BKR** | **16 / 18** — the only energy-chain candidate with real body proximity | flow **+0.364 🟡**, OBV 매집, RS20 **+3.8**, **RS60 −7.8**, `vol_surge` **0.77**, **delta −0.347** | ⛔ **REJECTED on the object, not the flow.** Its proximate article is *"Crude Prices Pressured by Growing Optimism the Strait of Hormuz to Soon Reopen"* — **proximate to node 2 (transit), which §3a establishes is not the binding constraint. R46 disqualifies it** |
| **WMB** | 2 / 8 | flow **−0.253 🟡**, OBV **중립**, RS20 **−7.9**, RS60 −4.6 | ⛔ **REJECTED.** Proximate article is *"Petrol prices 'highly likely' to hit 160p"* — **UK retail petrol has no mechanical link to a US gas-pipeline operator.** ★ **This is the desk's registered 2026-07-14 WMB mis-labelling repeating in the same tool** |
| NDAQ · SPGI · SCHW · JPM · MSFT · META | 2–6 each | — | ⛔ **Exchange/data/bank furniture** — surfaced by articles that merely *contain* an inventory or price number. Not chain candidates |

🚨 **The finding is the emptiness, and it is measurable.** The **"Russian refinery / gasoil"**
chain-hop — the desk's *correct* object under R46 — scanned **29 articles in 7 days and returned
ZERO body-proximate candidates**, with only XOM/CVX/VLO appearing at all and all of them
**headline-named**. The **"distillate / diesel"** hop scanned 397 and returned **XOM (21 title / 41
body) and CVX (17/36) at the top of the headline-named list**. ⇒ **The desk's own news surface is
object-confused in exactly the direction MACRO §0-b warns about: it names the crude majors on a
distillate story, and it cannot see a single US ticker adjacent to the physical object.** **No
candidate is handed forward.**

---

## 6 · Track KPIs and anti-signals, as dated observables

| KPI | State, **settled 2026-08-05** | Anti-signal (what would break §0) | Date |
|---|---|---|---|
| ★★★ **S55** HO%−CL% from the 08-04 anchor | **+1.407pp after 1 of 5 sessions** | **A ≤ −3.0** = release real · **B ≥ +6.5** = premium rebuilds. Base rates measured: **A 15.5% · B 9.5% · neither 75.0%** (n=252) | **08-11** |
| ★★★ **Refining RS60 vs SPY** — the one number that decides §0 | **VLO +21.1 · MPC +17.2 · PSX +13.7**, all three **DOWN** for the first time in the series (from 25.2 / 23.6 / 16.9) | **any of the three going negative**, or a second consecutive session of RS60 declines on all three | rolling |
| ★★ **Refining RS20 vs SPY** | **+3.6 / +2.8 / +4.6** after a 13–16pp one-session collapse | RS20 < 0 on two of three ⇒ the de-rate is not a single bar | rolling |
| **B1 — distillate crack, level / 5d / 21d / 63d / %ile** | **84.220 / −14.864 / +15.989 / +17.222 / 92.1st** | **level out of the top quartile** (< ~55th pctile) while gasoline stays broken | rolling |
| **B1 — second derivative of the 5d rate** | **−9.733 → −4.912 → −2.377** (08-03/04/05): the rate is still falling but **its own decline has shrunk three sessions running** | the second derivative turning negative again for two consecutive sessions ⇒ the give-back is re-accelerating | rolling |
| **dist−gas spread, level AND 5d rate** | level **40.211** (93.7th pctile), widened 4/4 sessions — ⚠ **but the 5-session RATE just flipped negative for the first time: +5.300 → +4.280 → −0.626** | **level compressing on two consecutive settled closes** ⇒ the release is real and §0 is withdrawn | rolling |
| **Gasoline crack, all windows** | **−14.238 / −9.614 / −5.786** — still the leg doing the damage | turning positive on the 21-day window | rolling |
| ★★ **MPC CY estimate line** | **39.08 vs 40.22 w/w = −2.8%, first weekly cut** (NY −4.9%) while CQ/NQ rose | **a SECOND consecutive weekly cut** ⇒ Lens 3's MPC flip fires and B2's trap reading wins | **weekly** |
| ★★ **VLO CY estimate line** | **41.25, +16.5% in 7 days**, 30d breadth 12↑/2↓ | **two consecutive weekly declines**, or OBV → 분산 | **weekly** |
| ★★★ **PSX Atlantic Basin realised margin** | **$14.44 vs $19.77 est (−27.0%)**, on 27.6% of company capacity | **a 2nd Atlantic-Basin miss** ⇒ the basin is structurally contested, not lagging (§3b) | **PSX Q3 print, late Oct** (VLO's is **2026-10-22**) |
| **XOM / CVX estimate breadth** | **XOM CY 30d 4↑/12↓, 7d 0↑/4↓ · CVX NQ 30d 2↑/11↓** | **breadth turning net-positive on both** ⇒ the 🟢 tag stops being purely velocity and (ii) reopens | **weekly** |
| ⚠ **XOM short-vol z** | **+2.73 🔴 spike** (short% 65.1 vs 42.7 base) on the bar its green lit | z falling back < +1.5, or CVX's −1.34 covering reversing | daily |
| **§3a-3 Russian regime VOID** | **RESOLVED — NOT MET.** The "lull" ended 07-31; ban **extended** | a dated **named** regime change loosening exports, primary or two independent outlets on one primary | rolling |
| **Object exclusivity (new, from §3a-2)** | **Four capacity legs, not one.** Kpler ranks China's quota comparable to Russia | **China raising fuel-export quotas** — an un-bracketed, un-instrumented channel this desk cannot currently see | ⚠ `[blank]` — **no date exists and none is invented** |
| **A6 customer print dates** | Rails/airlines reported Q2 in July; **DAL RS60 +22.7, UAL +29.0** | **airline/rail RS60 rolling negative together** ⇒ node 8 (demand destruction) starts to bind | **October prints** |
| **S61** tanker war-risk | −5.56pp at registration, past its branch-B line | **A ≥ +6.80pp** at settle | **08-12** |

**⚠ What I could NOT measure, stated rather than guessed:**
1. **ICE gasoil futures** — `GAS=F`, `MFF=F`, `LGO=F` all return "no data" from the provider. **The
   $75/bbl European gasoil crack is `[news, StanChart via oilprice, single provider]` and could not be
   independently verified. `unknown` on the level (C3).**
2. **VLO's margin history via quarterly XBRL** — the SEC cross-check block is empty (B2's known
   limitation, reproduced). **No VLO margin percentile is stated.**
3. **PSX's segment-level explanation** — the 08-05 8-K (Item 2.02) is a results release; **no call
   transcript naming a cause for the Atlantic Basin figure was recovered at this stage.** §3b's two
   readings are therefore left as C4-indistinguishable rather than adjudicated.
4. **Russian export volumes from a primary agency (EIA/IEA/Argus)** — **still not read.** MACRO P26's
   KPI remains open; the corroboration added here is Kpler/StanChart/Carnegie, not a regulator.

---

## 7 · Verdicts

### 7a · (i) The ROTATION divergence — **it is a MIS-SPECIFIED question, and forced to choose: TRAP-side, but not for the reason offered**

**The 0.285 gap between wflow +0.230 and eqflow −0.055 is arithmetic**: two names are ~55% of the
sector's measured cap, so a cap-weighted mean can be positive while an equal-weighted mean over 16
names is negative. **A gap of that construction carries no timing information at all** — it is the
same object the desk keeps re-discovering as "mega-cap-narrow", and calling it "early" would be
reading a weighting scheme as a signal.

**What DOES carry information is the delta of −0.129, and it is the refiners':** **PSX −0.318 ·
VLO −0.277 · MPC −0.167** are the three largest negative deltas in the sector, and the only positive
delta belongs to the velocity-lit mega-cap. **The sector ranks last on change because its money leg
de-rated, not because its laggards got worse. That is trap-shaped, not early-shaped.**

**But the trap is in the TAG, not in the LEG** — and this is the distinction ROTATION's downgrade
blurs. Three independent axes agree the refining sub-leg is where the substance is: **RS60 +13.7 to
+21.1 vs SPY** (money), **CY revision breadth 11↑/0↓ · 12↑/2↓ · 13↑/2↓** (consensus), and **capture
at 112% of benchmark with margins ~2× y/y** (accounting). **One axis — the 20-day tape — just went
violently the other way in a single session.** **C4: on one settled bar those cannot be separated.
`INDISTINGUISHABLE`, and the discriminator is registered: RS60.**

★ **What I would say plainly to ROTATION**: **N+ is defensible as a level and mis-argued as a
reason.** The downgrade cites eqflow −0.055 and delta −0.129 — **both of which are dominated by the
three names whose revision books are the strongest in the sector.** ⚠ **And the notch-back is being
taken on the same bar the desk's own segment measure was reading the refiners as its strongest
`EXTENDED-BUT-LIVE` names (Lens 3 §3, finding 2). Both readings are in this run, from the same file,
pointing opposite ways. Recorded as the disagreement it is, not averaged.**

### 7b · (ii) Which sub-leg the verdict is written about — **REFINING. Settled, on two axes.**

Not a close call. The 🟢 filter names **XOM and CVX**, whose greens are **velocity-only**
(`vol_surge` 0.85 / 0.99), whose narrative is measured **decaying 20→4 outlets** and ⚪ECHO 1.95×,
whose **60-day excess is +0.5 and −1.7 vs SPY**, and whose **30-day estimate breadth is net-negative
on three of four lines (XOM) and on the next-quarter line (CVX)**. **XOM additionally printed a
🔴 short-volume spike (z +2.73) on the very bar its green lit.** **The money map and the revision map
agree with each other and disagree with the tag map. The tag map loses.**

### 7c · (vi) S55's live branch — **B, on the running number and on the conditional base rate; but "neither" is still the modal outcome**

**Running, measured** [own calc, settled, anchor 08-04]: 08-05 gave **HO +0.682% vs CL −0.726% ⇒
+1.407pp**, one session of five. 🟡live 08-06 partial: **+0.48pp — quoted for the record, no verdict.**

**Base rates on the trailing 252 settled sessions (n=252, sd 4.90):** branch **A (≤ −3.0) = 15.5%** ·
branch **B (≥ +6.5) = 9.5%** · **neither = 75.0%.** ⇒ **Unconditionally A is 1.6× more likely than B,
and the bracket is honest: both branches are reachable, which is the P23 lesson satisfied.**
**Conditionally, after the first session, the odds invert**: B now needs **+5.1pp over 4 sessions
(base rate 13.1%)** while A needs **−4.4pp over 4 (10.3%)**. **The first session moved B from
9.5% to 13.1% and A from 15.5% to 10.3%.**

**Which branch the evidence favours, plainly: B.** The distillate level **rose two consecutive
sessions**; dist−gas widened **4/4**; the 5-day rate's own decline has **shrunk three sessions
running** (−9.733 → −4.912 → −2.377); the physical object is **verified as to class by the operator**
and its strike tempo **resumed, it did not lull**; and US runs at a **7-year high still fail to
clear an ~8% global diesel shortfall.**

**What would flip it to A, in order of how fast it could arrive:**
1. **dist−gas compressing on two consecutive settled closes** — the registered anti-signal, and
   ⚠ **its 5-session rate has ALREADY flipped negative (+5.300 → +4.280 → −0.626), which is the first
   evidence on A's side this file found.**
2. **A dated, named Russian regime change loosening exports** — §3a-3 says the opposite is on file.
3. **China raising fuel-export quotas** — the leg Kpler ranks as comparable to Russia's and for which
   **this desk has no instrument, no bracket and no date.** ⚠ **That is the largest un-guarded hole in
   §0's reasoning and it is named rather than left implicit.**
4. **Node 8 binding**: China's 2Q26 crude imports are **already −32% QoQ**. **Demand destruction is
   the one path that ends this cycle with no facility repaired, and it is the path the desk's KPIs
   watch least.**

**⚠ S1 throughout**: n = 1 settled session for D-1 and D-5, n = 1 company/1 quarter/4 regions for
§3b, n = 1 print for the MPC weekly cut. **None of these is four observations, and none is treated
as one.**
