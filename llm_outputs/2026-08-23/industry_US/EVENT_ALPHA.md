# EVENT_ALPHA — industry_US · 2026-08-23 (Sun) · Stage 5 / L1·EVENT_ALPHA

> Bottom-up complement to MACRO's transmission matrix: *which stories ARE building, and is money
> already following.* Scope **`--scope foreign`** on every call (market-locked; a card citing the KR
> feed is void). All flow tags read from `SECTOR_FLOW_US.json`, **asof 2026-08-21 settled close**.
> **`n_new_sessions_since_prior_run = 0`** — every flow number below is inherited, not new. **The
> news is the only thing that is new today, and that is the whole point of this stage.**

---

## 0 · 🚨 A tool defect found and isolated INSIDE this stage — it manufactures zeros

Four thread body-reads in this stage returned **0 hits** and were nearly written down as "no
coverage". They were not zero.

| Query as issued | Hits | Same query, each term quoted | Hits |
|---|---:|---|---:|
| `Micron AND CXMT` | **0** | `"Micron" AND "CXMT"` | **27** |
| `Anthropic AND OpenAI AND IPO` | **0** | `"Anthropic" AND "OpenAI" AND "IPO"` | **108** |
| `Canada AND tariffs AND lumber` | **0** | `"Canada" AND "tariffs" AND "lumber"` | **36** |
| `Broadcom AND Google` | 1 | `"Broadcom" AND "Marvell"` | **126** |

**Isolated to one line of behaviour**: the CLI wraps the *entire* user string in double quotes before
handing it to FTS5 (`MATCH: ("Micron AND CXMT")`), so **a bare boolean becomes a phrase search and
returns 0 silently.** Control: `Micron` alone returns **562**. ⇒ **Every term must be individually
quoted.** This is the `M68` class the MACRO EXIT CHECK names — *"no bucket's 0/near-0 hit count is
trusted until its terms were passed correctly"* — and today it fired **four times in one stage** and
would have produced four fabricated silences, one of them on a **held name** (`AVGO`). Registered as
a dig at run end. **All four queries were re-run and their real results are the cards below.**

---

## 1 · Selection — logged, not silently capped

`thread --days 7 --scope foreign`: **4,417 daily events → 3,391 threads → 536 multi-day → 49 alive**
(2,855 one-day, 92 new today). Per-day denominators **08-17 756 · 08-18 824 · 08-19 825 · 08-20 824 ·
08-21 766 · 08-22 280 · 08-23 142.**

**8 selected · 41 alive threads NOT selected** (no silent truncation). The 41 are dominated by
single-name buy/sell listicles (`Jim Cramer` ×4, `Reddit vs Rigetti`, `3 Top Dividend Stocks`),
non-market geopolitics with no US-listed exposure hop (West Bank settlements, Guatemala deportations),
and consumer/sport items.

🚨 **Selection rule overridden once, with the measurement that justifies it.** The tool labels this
run's **headline story FADING (7→2)** — *"Nvidia customers notified about AI-related price hikes"*.
A direct query contradicts the label: **8 distinct outlets, most recent Sun 2026-08-23.** The "2" is a
**142-article Sunday, 17% of a weekday's volume** (`M828`). ⇒ **Card 1 is selected against its own
tag**, and every FADING/ENDED label in this file is treated as unreadable for the same reason.

---

## 2 · Forward cards

### ★★★ Card 1 — Memory cost is being passed through the accelerator layer, four days before the print

- **Thread**: *"Nvidia customers notified about AI-related price hikes above 15%"* · tool tag **FADING
  7→2, REFUSED** (§1) · **8 outlets measured directly** (`fortune` · `scmp` · `cnbc` · `cna`×2 ·
  `straitstimes` · `yahoo_finance` · `investing_en` · `google_en`/Reuters) · latest **Sun 08-23** ·
  window denominator **08-22: 1,684 articles / 280 events**.
- **Direction (body-read, title verbatim)**: `yahoo_finance` 08-22 — ***"Nvidia customers face over 15%
  server price hikes AS MEMORY COSTS SOAR"***. **The mechanism is named and it is cost, not demand.**
  Corroborating layer: `tomshardware` 08-19 — *"Samsung raises advanced foundry prices by up to 15% as
  AI demand fills its 4nm lines."* **Two ~15% increases at two chain layers in four days.**
- **Exposure** (flow asof 08-21):

  | Ticker | Chain position | Flow | Crowding note |
  |---|---|---|---|
  | `NVDA` **held** | the layer raising the price | **−0.181 🟡**, OBV 중립 −0.024, rs20 +0.2, rs60 −1.0, surge 0.75 | FINRA z **+0.41**, normal. **Headline layer — crowded by construction** |
  | `MU` | the cost | **−0.278 🟡**, OBV 중립, rs60 +2.1, surge 0.63 · **delta +0.300 = rank 16 of 299** | not held; not in any card until today |
  | `SNDK` | the cost (NAND) | **+0.144 🟡**, OBV 중립 · **delta +0.416 = rank 7 of 299** | not held |
  | `AVGO` **held** | co-designs the accelerators being repriced | **−0.221 🟡**, rs60 **−14.7** | see Card 3 — its problem is not memory |
- **Future — both branches, settle 2026-08-26 (`NVDA` print, D-3):**
  - **IF the pass-through is binding** → guided next-quarter gross margin **≤** the reported quarter's,
    and the reported quarter beats the prior by **≤50bp**. KPI: `theme-age "memory prices"` and whether
    the 8-outlet cluster survives Monday's session.
  - **ELSE (kill)** → guided GM **≥ +100bp** above the reported quarter ⇒ this was pricing power, the
    card's premise is wrong, and the desk's *"level stays tight"* reading loses its only buy-side
    corroboration.
- **Cell**: **CONFIRMED-EARLY on the story axis, UNCONFIRMED on the money axis** — the story is 8
  outlets and one day old; `NVDA`'s own flow is −0.181 with `vol_surge` 0.75. ⇒ **handed to ROTATION as
  IT cross-evidence and to PREMORTEM as `P90`'s object. NOT handed to BET as a name.**
- ⚠ **`L2` (peak-margin trap) is the binding lens**, not `L1`: a cost pass-through defends a margin, it
  does not expand one.

### ★★★ Card 2 — The memory complex's flow SECOND DERIVATIVE turned while its LEVEL stayed negative

- **Thread**: *"Nvidia vs. Micron: One Sells AI Chips, One Sells the Memory"* (08-18, 17 articles/5
  outlets) → *"Can Micron Beat the Memory Cycle As CXMT Scales Up?"* (08-21) → *"Micron vs. Sandisk:
  Which AI Memory Stock Should You Own"* (08-23) · **REIGNITED 5→3→3, 34 articles.**
- **Direction (body-read)**: two forces named in the same week and they oppose. **Supply threat**:
  `CXMT` is scaling — and `tomshardware`/`digitimes` 08-20 report in court testimony that *"CXMT planned
  to use stolen Samsung IP to develop its DRAM"*, with a follow-on that `YMTC` filed for a **$4.6–4.9bn
  Shanghai STAR IPO** (`bloomberg`/`google_en`, 08-19 & **08-23**). **Chinese memory is capitalising at
  scale.** **Price support**: Card 1's pass-through.
- **★★ The measurement this card exists for.** Ranking all **299** names by one-session flow delta:
  **`SNDK` #7 (+0.416) · `LRCX` #10 (+0.370) · `MU` #16 (+0.300) · `ADI` #18 (+0.296) · `TER` #36
  (+0.197) · `STX` #42 (+0.177) · `AVGO` #43 (+0.176) · `INTC` #45 (+0.153)** — **8 memory / memory-
  equipment names inside the top 45**, against a universe median delta of **+0.011**.
  ⚠ **And their LEVELS are all negative**: `MU` −0.278 · `LRCX` −0.294 · `ADI` −0.322 · `TER` −0.364 ·
  `INTC` −0.503 · `AMAT` −0.766 · `WDC` −0.781. **OBV is 중립 or 분산 on seven of eight — only `STX`
  is 매집.** ⇒ **This is a rate-of-change inflection off a bad level, not accumulation.**
  ★ **Which is the desk's own regime sentence applied to its own tape**: *the equity tracks the second
  derivative, not the level.* The spine wrote that about memory **prices**; here it is in memory
  **flows**.
- **Exposure**: `MU` · `SNDK` · `LRCX` · `STX` — **none held, none previously carded.** ⚠ `TSM` is
  **not in the universe** and therefore unmeasurable on every axis (`G5`).
- **Future — both branches, horizon 2026-09-03 (10 settled sessions from 08-21):**
  - **IF the inflection is real** → at least **4 of the 8** carry `flow_score` above **0** *and* OBV to
    **매집**, with `MU` rs20 vs `SPY` **> 0**.
  - **ELSE (kill)** → **≥6 of the 8** still print `flow_score` < 0 on 09-03 ⇒ the delta was a
    one-session artifact and `D293`'s roll-off warning was the whole signal.
- **Cell**: **STORY-ONLY → watchlist with a dated re-check (2026-09-03).** The money axis is a
  **delta**, not a level, and one session is not a tape. **Not handed to BET.**
- ⚠ **Filed to the miss ledger** (`Q.확신부족`) rather than dropped, per this stage's rule: the thread
  cleared the money axis on rate-of-change and never became a candidate.

### ★★★ Card 3 — `AVGO` (HELD) lost share of its single most important custom-silicon customer, and the desk has no thesis line for it

- **Thread**: *"Google pits Marvell against Broadcom as it chases AI crown"* (`theregister` 08-19) ·
  *"Broadcom Falls 5% as Marvell Lands Google Custom Chip Deal"* (`yahoo_finance` 08-19) · *"Broadcom
  Gets Fresh Google Warning"* (08-19) · *"Where we stand on Broadcom after Marvell muscles in on its key
  customer Google"* (`cnbc` 08-19) · *"Google Is Getting Paid in Marvell Stock Warrants"* (08-22 body
  tier) · **126 hits on `"Broadcom" AND "Marvell"` over 5 days.**
  ⚠ **This thread was one of the four the broken query in §0 nearly zeroed.**
- **Direction (body-read)**: unambiguous and **negative for the held name** — Google dual-sourced its
  custom accelerator to `MRVL`, and is taking **warrants in `MRVL`** as part of the arrangement, i.e.
  the customer now has equity-linked incentive in the competitor.
- **★ The money already moved and the desk did not:**

  | | `AVGO` (**held, 1 share**) | `MRVL` (not held) | spread |
  |---|---:|---:|---:|
  | `flow_score` | **−0.221** | **+0.583** | 0.80 |
  | `obv_state` | 중립 (+0.038) | **매집** (+0.183) | — |
  | rs20 vs `SPY` | **−7.2** | **+18.4** | **25.6pp** |
  | rs60 vs `SPY` | **−14.7** | **+17.3** | **32.0pp** |
  | FINRA short z | **−2.53 🟢 covering** (5v5 −6.0▼) | — | — |

  ⚠⚠ **And `MRVL` is one of the six `R96` tag-contaminated names** — a partial-coverage sweep marked it
  **🟢가속** on news velocity, and *this story is that velocity*. **The contamination and the substance
  point at the same ticker**, which is why `R96`'s rule is "re-derive from the score column", not
  "discount the greens": `MRVL`'s **score** (+0.583, OBV 매집, rs20 +18.4) is clean and says the same
  thing the news does.
- **`W4` fires — name the customers.** The standing view carries `AVGO` as *"AI-compute-EPICENTER"*
  with **no customer named**. Its customer is Alphabet, and Alphabet dual-sourced on **2026-08-19**.
- **Future — both branches, settle 2026-09-02 (`AVGO` print, D-10, a calendar binary):**
  - **IF the share loss is material** → `AVGO` guides next-quarter AI revenue **below** the prior
    quarter's sequential growth rate, **OR** `AVGO`'s rs60 vs `SPY` is still **≤ −10** on the first
    settled close after 09-02.
  - **ELSE (kill)** → `AVGO` rs60 vs `SPY` recovers **above −5** by that close **AND** the print names
    a replacement custom-silicon win. Then this is a one-customer scare, not a franchise event.
- **Cell**: **LATE-MONEY on `MRVL`** (rs60 already +17.3; the desk would be buying after a 32pp spread)
  → **valuation gate note, not a candidate.** **Book flag on `AVGO`** — see §3.
- ⚠ **`AVGO`'s FINRA z −2.53 (shorts covering) into a −14.7 rs60 is the `M804` shape for a THIRD
  instance this run** (after `RTX` z −2.15 into delta −0.304, and `LHX` on 08-21). **Shorts covering
  into decline is not a bottom signal; it is the removal of one class of future buyer.**

### ★★ Card 4 — The `NVDA` earnings thread peaks on a Sunday, three days before the print

- **Thread**: **BUILDING 7 days · outlets 3→5→5→5→6→4→7 · 103 articles** — *"History Says Nvidia Is
  Going to Disappoint Wall Street"* (08-18) → *"Why Is Nvidia Stock So Cheap?"* (08-19, 30 articles) →
  *"Nvidia Earnings Preview"* (08-21) → *"Prediction: Nvidia Will Be a $6 Trillion Company"* (**08-23,
  7 outlets — the thread's peak, on a 142-article day**).
- **Direction (body-read)**: the thread is **two-sided and its skew flipped**. 08-18/08-19 carried
  *disappointment* and *cheapness* framings; 08-21–08-23 carry previews and a **$6tn** target, plus
  `Oppenheimer`'s *"blunt Nvidia stock message ahead of earnings"* (08-22, 4 outlets). ⇒ **The
  narrative is at maximum outlet count with the print not yet delivered.**
- **Exposure**: `NVDA` **held** (−0.181 🟡, OBV 중립, surge 0.75, FINRA z +0.41 normal). Second-order:
  `MRVL` +0.583, `AMD` **−0.683 🟡** (rs20 −13.0), `MU` (Card 2).
- **Future — both branches, settle 2026-08-26:**
  - **IF the story is priced** → `NVDA` 1-session excess vs `SPY` on 08-27 is within **±3.0pp**
    (a maximum-attention print that moves nothing is the definition of priced).
  - **ELSE (kill)** → **|excess| ≥ 3.0pp** ⇒ attention did not equal pricing and the thread was
    information, not noise.
- **Cell**: **STORY-ONLY.** Peak attention + neutral flow + `surge` 0.75 is the crowded-narrative shape.
  ⚠ **`S103` brackets this print and its bands are still HAND-SET for a fourth run (`D295`/`D315`)** —
  ALPHA's obligation today.

### ★★ Card 5 — The US–Canada 50% tariff is LIVE, not looming, since 2026-08-22

- **Thread**: **60 articles / 24 outlets on 08-22** — the day's largest cluster by 3×. Tool tag
  **FADING (11→24→11), REFUSED** (§1, weekend denominator).
- **Direction (body-read, dated sequence recovered by the corrected query)**:
  **08-18** *"US-Canada tariff clock ticks: last-minute talks to avert Trump's 50% tariffs"* (`toi`) →
  **08-19** *"Trump announces 3-day pause on Canada tariffs as deadline neared"* (`upi`) →
  **08-22** ***"US-Canada trade standoff: 50% tariff kicks in as Ottawa vows 'dollar-for-dollar'
  response"*** (`toi`), with `bloomberg`/`scmp`/`fortune` carrying the Canadian retaliation.
  ⇒ **The pause expired. The tariff is in force. This is a state change, not an escalation risk.**
- **Exposure — and this is where the desk's instrument gap bites** (flow asof 08-21, i.e. **before** the
  tariff took effect):

  | Ticker | Chain position | Flow | Note |
  |---|---|---|---|
  | `NUE` **held** | US steel — a tariff beneficiary | **+0.319 🟡**, OBV 매집 +0.148, surge **1.41**, rs20 −5.2 | fails 🟢 on rs20 only; `S114` (09-03) already brackets it |
  | `STLD` | US steel | −0.105 🟡, surge 1.31, **delta +0.189** | not held |
  | `CAT` · `DE` | machinery, Canadian input cost | `CAT` **−0.692 🔴** · `DE` +0.337 🟡 (surge **1.61**) | `CAT` is Industrials' `top1` at 8.7% |
  | `F` · `GM` | autos, integrated NA supply chain | `F` −0.284 🟡 · `GM` +0.261 🟡 OBV 매집 | — |
  | ⚠ `X` · `WY` · `CNI` · `CP` | steel, lumber, Canadian rail — the **most** exposed layer | **NOT IN UNIVERSE** | **unmeasurable, not neutral** (`G5`) |
- **Future — both branches, settle 2026-08-28 (`P92`):**
  - **IF it prices** → `XLI` 5-session excess vs `SPY` ≤ **−2.50pp** **OR** `XLB` ≤ **−1.00pp**.
  - **ELSE (kill)** → **both** `XLI` ≥ −0.50pp **and** `XLB` ≥ +2.00pp ⇒ headline, not macro object.
- **Cell**: **CONFIRMED-EARLY on the story axis, UNMEASURED on the money axis** — the flow frame
  predates the event by one session and **the four most-exposed names are outside the universe.**
  ⇒ Handed to ROTATION as a **caveat on Industrials/Materials**, not as a candidate.
- 🚨 **Three independent instruments failed on this same story**: `drift_watch`'s kill-switch term set
  has no trade term (`D316`); `theme-age tariff` reads **⚪ECHO 1.11×** because its base is **9,712**
  articles (`M830`); and the universe cannot price the four names that matter most. **A desk can be
  blind to one event in three different ways at once.**

### ★★ Card 6 — A named 38-gigawatt power gap, and every measurable power name is 🔴

- **Thread**: *"Nvidia Chip-Filled Data Centers Need More Power Than A[nything]"* (3→5→4→2) plus, from
  the corrected query (**1,306 hits**): ***"Morgan Stanley Says AI Data Centers Face a 38-Gigawatt Power
  Gap. These Industrial Stocks Fill It."*** (`yahoo_finance` + `fool`, **08-20**) · *"Nvidia investing
  $1.5B in SoftBank data center developer behind OpenAI project"* (`techcrunch` 08-17) · *"TerraPower's
  nuclear reactor has a secret weapon for powering AI data centers"* (08-19) · *"Pennsylvania dangles
  permitting carrot for data centers that bring their own power"* (08-19).
- **Direction (body-read)**: the constraint is being **quantified and named by a sell-side house**, and
  capital is being committed to it (`NVDA`'s **$105bn** OpenAI Ohio lease guarantee, `M802`; `NVDA`'s
  $1.5bn into a SoftBank DC developer).
- **★ And the tape says the exact opposite**, every name, one session, asof 08-21:

  | Ticker | Flow | OBV | rs20 | Tag |
  |---|---:|---|---:|---|
  | `TT` (cooling) | **−0.812** | 분산 | −9.4 | 🔴 |
  | `GEV` | **−0.741** | 분산 | −9.3 | 🔴 |
  | `VST` | **−0.689** | 분산 −0.340 | **−20.3** | 🔴 |
  | `CEG` | **−0.625** | 분산 | −4.2 | 🔴 |
  | `NEE` | **−0.600** | 분산 | −10.5 | 🔴 |
  | `PWR` | −0.073 | 중립 | −1.5 | 🟡 |
  | **`ETN` (held)** | **+0.210** | **매집 +0.172** | +0.1 | 🟡 |
  | `EMR` | +0.268 | **매집 +0.342** | +2.7 | 🟡 |

  **Five of eight are 🔴분산 — and the verdict does not rest on OBV** (`RULE D6`): each of the five
  also prints `flow_score` ≤ −0.600 **and** rs20 vs `SPY` ≤ −4.2, so the OBV leg is the third
  agreeing axis, not the claim. **Utilities is 🔴 on 13 of 15 names with `eqflow` −0.621, the worst
  sector on the board.** ⚠ `BE` (Bloom Energy) is **not in the universe** — unmeasurable.
  ⚠ Likewise `ETN`/`EMR`: their **OBV 매집 is cited only beside `flow_score` +0.210 / +0.268 and
  rs20 +0.1 / +2.7** — a grade-C signal is never the load-bearing one here.
- **Future — both branches, horizon 2026-09-03:**
  - **IF the capital commitment reaches the equities** → **≥3 of {`GEV`,`VST`,`CEG`,`NEE`,`TT`}** move
    OBV to 매집 **and** `flow_score` above **−0.20**.
  - **ELSE (kill)** → **≥4 of the 5** still print 🔴분산 on 09-03 ⇒ **the AI-power thesis is a capex
    story with no equity transmission**, and the desk should stop treating power as an AI-cycle layer.
- **Cell**: **DEAD is NOT the verdict** — this stage's rule is that DEAD requires *both* axes, and this
  thread is **BUILDING with a quantified number** while the money disperses. ⇒ **Re-filed with a new
  thesis line and a dated re-check (09-03)** rather than dropped, and `M802`'s contradiction is carried
  into `handoff` unresolved for a second run.
- ⚠ `ETN` is held and is one of only two names on this list with OBV 매집 — **but `M778` measured
  `ETN`'s beta to `XLI` at +1.402 (t +6.12)**, i.e. its move belongs to Industrials, **not** to the
  AI-power basket. **The book's power exposure is not measurably an AI-power exposure.**

### ★ Card 7 — A mega-IPO pipeline is forming, and it is an equity-SUPPLY event for the AI complex

- **Thread**: **REIGNITED 4 days · outlets 5→4→5→5 · 34 articles**, latest **08-23 at 5 outlets**:
  *"Anthropic's pre-IPO credit facility set to exceed $10 billion"* (08-18) · *"Bill Ackman Is Launching
  a New Way to Invest in Pre-IPO"* (08-21) · *"IPO Fever Heats Up for OpenAI and Anthropic"* (08-22 →
  **08-23**, `fool`/`nasdaq`/`yahoo_finance`, 40k-character bodies). **108 hits** on the corrected query.
- **Direction (body-read, dated)**: *"Anthropic could publicly file IPO paperwork **as soon as this
  month**"* (`yahoo_finance` 08-20) · *"Anthropic's IPO could come sooner than you think — **likely
  beating OpenAI to the punch**"* (08-21) · *"Anthropic market debut could **break the SpaceX IPO
  record**"* (08-22). Parallel: `YMTC` filing for **$4.6–4.9bn** in Shanghai (08-19, **08-23**).
- **★ Why this is a macro card and not a private-market curiosity**: a record-breaking AI IPO is
  **new supply of AI equity**, and it arrives while the desk's own IT sector is **`exc5` −2.158
  (rank 11 of 11)** and **🔴15 of 56**. Supply into weak breadth is a different object from supply into
  strength.
- **Exposure**: **no clean listed instrument** — which is the finding. Second-order: `MSFT`/`GOOGL`
  (holders of stakes), `COIN` **+1.000 🟢** and `MSTR` **+1.000 🟢** as the two names carrying the
  risk-appetite factor (**2 of the universe's 6 greens are bitcoin beta**).
- **Future — both branches, horizon 2026-09-30:**
  - **IF the pipeline lands** → an S-1 becomes **public** for Anthropic by 09-30, and `XLK` 20-session
    excess vs `SPY` on that date is **≤ 0**.
  - **ELSE (kill)** → **no public S-1 by 09-30** ⇒ this was pre-IPO chatter, and the card retires.
- **Cell**: **STORY-ONLY → watchlist, dated re-check 09-30.** ⚠ **`D311` applied**: *"as soon as this
  month"* is a body phrase, **not a date**, so no dated catalyst is registered from it.

### ★ Card 8 — `Treasury buyback` is the board's only FRESH theme, and it is 4 days old

- **Thread**: `theme-age "Treasury buyback"` **🟢FRESH · age 4 days · 178 articles** — the **only**
  FRESH theme of seven probed. Thread form: *"US debt tops $40 trillion threshold"* 6→18→19→4→5→3 ·
  *"The U.S. Treasury's Bond Market Intervention Is a Nightmare…"* (7/6, 08-22) · *"The Real Cost Of
  $40 Trillion In Debt"* (5/5) · *"How a Treasury buyback tweak helped bitcoin surge 25%"* (6/4).
- **Direction (body-read, inherited and re-checked)**: `M797`/`M798` recorded that the operation's own
  predicted effect was a **flattener** while the realised 20 sessions **steepened ~24bp**. ★ **Today's
  decomposition sharpens it (`M820`): the steepening is `DGS2` −18bp against `DGS30` +6bp — a
  front-end rally, not a long-end selloff.** The operation targets the long end; the long end moved
  **6bp** and the front end moved **18bp**.
- **Exposure**: `[FRED]` levels, not equities — `DGS30` **5.23 (96.4 %ile)** · `30y−10y` **0.54 (22.6
  %ile)** · `IG OAS` **0.82 (77.9 %ile)** vs `HY OAS` **2.75 (23.3 %ile)**. Equity second-order:
  `COIN`/`MSTR` (the bitcoin-surge transmission the 08-22 body tier names explicitly).
- **Future — both branches: `P85` (settles 08-28) and `P91` (assigned to the first business-day run on
  or after 08-31, per `D309`).**
- **Cell**: **CONFIRMED-EARLY on the macro axis** — a FRESH theme with a `[FRED]`-measurable object and
  two live brackets. **No equity candidate is derived from it** (P4).

---

## 3 · Book cross-check — positions whose thesis rides on a thread that changed

| Held name | Carried thesis | What changed | Action for the book desk |
|---|---|---|---|
| 🚨 **`AVGO`** | *"AI-compute-EPICENTER"*, **customer unnamed** | **2026-08-19: Alphabet dual-sourced custom silicon to `MRVL` and took `MRVL` warrants.** rs60 spread `AVGO` −14.7 vs `MRVL` +17.3 = **32.0pp**. FINRA z **−2.53**, shorts covering into the decline | **Re-justify on something still alive, before the 09-02 print.** The thesis line has no customer in it, and the customer is the event (`W4`) |
| ⚠ **`ETN`** | *"AI-power/electrical"* | The AI-power thread is **BUILDING with a named 38 GW gap**, while 5 of 8 measurable power names are 🔴분산 and **`M778` assigns `ETN`'s move to `XLI` (β +1.402, t +6.12)** | **The label and the measured driver disagree.** Carried, not resolved — `C14`-class, US instance |
| ⚠ **`NVDA`** | AI-compute epicenter | Card 1 changes the **question** at the 08-26 print from demand to cost pass-through | No thesis change; `P90` brackets it both ways |
| ⚠ **`NUE`** | Post-earnings re-rate | The **50% Canada tariff is now in force (08-22)**, after the flow frame | `S114` (09-03) already brackets it; the tariff makes its steel leg **more** live, not less |
| ✅ `MPC` · `PSX` | Refining capacity destruction | `P66` **corroborated inside the window** — `bloomberg` 08-22, 1 outlet: *"Ukraine Drones Strike Samara Oil Refinery"* | No change; the 1-outlet tier carried it again |

**ENDED-thread flags**: none of the five open theses above rides on a thread this run can honestly call
ENDED — **because this run refuses every ENDED/FADING label** (`M828`, weekend denominators). That
refusal is itself the flag: **the book cross-check is degraded this run and the next weekday run must
re-run it.**

---

## 4 · Hand-off

- **To ROTATION** — Card 1 & 3 (IT: the sector is rank 11 on price while its epicenter reprices and its
  #2 name loses a customer) · Card 5 (Industrials/Materials caveat: the tariff is live and post-dates
  the flow frame) · Card 6 (Utilities: a quantified demand story against the board's worst tape —
  `eqflow` −0.621 and 🔴 13 of 15, with OBV 분산 as the third agreeing axis, never alone; `RULE D6`).
- **To PREMORTEM** — `P90` (Card 1) is the run's binary-adjacent object; **`NVDA` 08-26 is D-3 and
  becomes D-2 for the next run.** Card 3's 09-02 `AVGO` print is a **second** calendar binary.
- **To BET** — **nothing.** No card reached CONFIRMED-EARLY on **both** axes. Stated plainly rather
  than promoting a story-only name to fill the slot.
- **To ALPHA** — `D295`/`S103`'s `NVDA` bands, **fourth run, print in three days.**
- **Ledgers** — Card 2's names (`MU`, `SNDK`, `LRCX`, `STX`) filed to the **miss** ledger
  (`Q.확신부족`, `--enters-if` = flow above 0 with OBV 매집, recheck **2026-09-03**); `MRVL` filed as
  **LATE-MONEY** with `--enters-if` on a pullback that holds OBV 매집. No rejections filed this run.

---

## ✅ EXIT CHECK

- [x] **Scope market-correct** — `--scope foreign` on every `brief`, `thread`, `theme-age`, `fts` and
      `search` call in this stage. No KR-feed citation appears in any card.
- [x] **Selection logged** — 49 alive → **8 selected, 41 not selected**, with the non-selected
      characterised. No silent cap. One selection made **against** the tool's own tag, with the
      measurement that overrode it (§1).
- [x] **Direction body-read on every card** — each card quotes a dated title or body line. 🚨 **Four of
      them only exist because a broken query was caught and re-run** (§0).
- [x] **Every exposure name carries a flow tag with its asof** (2026-08-21 settled), and names that are
      **outside the universe** (`TSM`, `X`, `WY`, `CNI`, `CP`, `BE`) are marked **unmeasurable, not
      neutral**.
- [x] **Every card has both branches, a kill condition and a dated horizon** — 08-26 · 08-28 · 09-02 ·
      09-03 · 09-30.
- [x] **STORY-ONLY names did not leak into the candidate hand-off** — **BET receives nothing this run**,
      stated explicitly rather than backfilled.
- [x] **DEAD used as a MONEY verdict, not a story verdict** — Card 6 is BUILDING × 🔴 and is therefore
      **re-filed with a new thesis line and a dated re-check**, not dropped.
- [x] **Threads read but not carded go to the miss ledger, not to nothing** — Card 2's four names and
      `MRVL` filed with `--enters-if` conditions.
- [x] **Book cross-check emitted** (§3), with the honest note that it is **degraded** this run because
      every ENDED/FADING label is unreadable on a weekend window.
