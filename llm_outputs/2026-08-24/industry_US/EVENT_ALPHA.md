# EVENT_ALPHA — industry_US · 2026-08-24 (Mon) · Stage 5 / L1·EVENT_ALPHA

> Bottom-up complement to MACRO's top-down matrix. **All news `--scope foreign`, all calls made
> outside a sweep window.** All flow tags are the **08-21 settle** (`SECTOR_FLOW_US.json`), unchanged
> for three runs — every tag below carries that `asof`. **This stage never sizes (P4).**

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: **4,175 daily events → 3,225 threads → 512 multi-day → 129 ALIVE.**
**8 selected · 121 not selected**, of which **109 were only ever seen as one-line summaries** because
`--top 20` prints 20 (`D335-KR`, reproduced).
Per-day denominators **08-18 824 · 08-19 826 · 08-20 827 · 08-21 771 · 08-22 288 · 08-23 303 ·
08-24 336 (partial)** ⇒ the last three days run at **35 / 37 / 41%** of the weekday median.
🚫 **No thread was selected or excluded by a FADING/ENDED label this run** — every such label in this
window is unreadable (`D328(b)`).
⚠ Also unseen at the event tier: **265 of 280 single-outlet foreign events (94.6%)**, shown as a random
15 because the classifier is Korean-only (`D339`).

★ **Selection deliberately overrode the tool's ranking once**: Card 1 sits **outside `thread`'s top-20**
and is tagged FADING, while `brief` ranked it the **#1 event of 08-23**. It was taken on the `brief`
ranking. **That override is the single most consequential choice in this stage.**

## 0-a · 🚨 A universe hole that pre-empts three of these cards

`us_top300` membership checked for every exposure name below (`M868`). **Absent, and therefore
untaggable by any flow / RS / OBV / short axis:**

| Missing | Why it matters here |
|---|---|
| **`AA`** (aluminium) · **`X`** (steel) · **`WY`** (lumber) | The three most direct US names in the **Canada tariff** transmission — Card 1, the run's #1 object |
| **`LYB`** · **`DOW`** | The two named US chemicals counterparties in the **Shell $8bn sale** — Card 8 |
| **`BABA`** | The issuer in the **$10.2bn HK placement** — Card 5 |

⇒ **On the run's largest story the desk can produce no flow-tagged exposure name at all.** This is the
`SWEEP` invariant *"the desk must be able to tag what it holds"* extended one step: **it cannot tag what
its own discovery layer surfaces.** ⇒ **`D341`.** Every affected card below is marked **UNTAGGABLE**
rather than given a substitute name — substituting a taggable neighbour for an untaggable principal is
how a card gets built on the wrong company.

---

## Card 1 — ★★★ US–Canada trade war: talks COLLAPSED, tariffs are IMPOSED, retaliation is DATED

- **Thread**: *"Canada announces retaliatory tariffs on U.S. goods"* · tag **FADING (unreadable,
  §0)** · curve **19→23→9→11→24→20→14 outlets** · `brief` 08-23 rank **#1, 38 articles / 20 outlets,
  3.2× the next cluster` · `theme-age "Canada tariff"` **🟡ACCELERATING 9.86×** (base 69) vs
  `theme-age tariff` ⚪ECHO 1.14× (base 9,876).
- **Direction (body-read, ≥5 outlet bodies — this is NOT a headline card):**
  **The US imposed 50% tariffs on $20bn of Canadian goods after talks failed** (`aljazeera` 08-22:
  *"US imposes 50 percent tariffs on $20bn in Canadian goods after talks fail"*; `cnbc` 08-22:
  *"U.S.-Canada trade talks collapse, ushering in wave of new tariffs"*; `bbc`, `dw`, `euronews` same
  day). **Carney: Canada will match "dollar for dollar"** and calls the move a **"miscalculation"**.
  ★★ **Canada's retaliation has a NAMED EFFECTIVE DATE — 2026-09-08** (`aljazeera` 08-23) — and
  **targets steel, dairy, appliances, agricultural goods** (`dw` 08-22) (`M869`).
- **Exposure**: 🚨 **UNTAGGABLE at the epicentre** — `AA`, `X`, `WY` are outside the universe (§0-a).
  Measurable second ring, all `asof 2026-08-21`:
  `NUE` steel · flow **+0.319** 🟡 · OBV 매집 · rs20 **−5.2** · surge 1.41 — *held name; Canada's list
  names steel* · `STLD` steel · −0.105 🟡 · 중립 · rs20 **−11.1** ·
  `HD` home-improvement (lumber pass-through) · **−0.378 🔴분산** · rs20 −2.8 — *headline-named by
  `chain-hop`, i.e. crowded layer* · `UNP` **−0.347 🔴분산** and `CSX` −0.535 🟡 (cross-border rail) ·
  `GM` +0.261 🟡 매집 / `F` −0.284 🟡 (auto content crosses the border repeatedly).
  ⚠ `chain-hop "Canada tariff"` returned **`FCX`** (Copper, 3 proximity / 3 body) as its cleanest
  one-hop — `FCX` flow **+0.739 🟡 매집 rs20 +18.8 rs60 +18.4**, and **`Copper` COT sits at the 100th
  percentile long** (§A-5). **That is a crowded long on the one metal the chain-hop surfaced**, and it
  is named as a risk, not a candidate.
- **Future — both branches, dated:**
  **IF** the object keeps building **AND** money follows → by **2026-08-28 close** the equal-weight
  Industrials basket's 5-session excess vs **`SPY`** reaches ≤ **−3.10pp** (−2.0σ; **`P93` branch A**).
  **KPI:** `theme-age "Canada tariff"` (today **9.86×**) and the outlet curve.
  **ELSE / KILL** → Industrials excess ≥ **−0.50pp** while `SPY` itself falls ≤ −1.00% (**`P93`
  branch B**) ⇒ the trade war is an index-level risk premium, not a sector transmission, and this card
  is void as a *sector* object.
- ★★ **Construction finding handed to PREMORTEM (`M869`):** **both `P92` (settles 08-28) and `P93`
  (08-28) close ELEVEN DAYS BEFORE Canada's retaliation takes effect on 09-08.** They can only measure
  the **announcement**, never the **implementation**. **A successor bracket keyed to 2026-09-08 does
  not exist on this board.** ⇒ **`D342`.**
- **Cell**: **STORY-ONLY at the epicentre (untaggable) / CONFIRMED-EARLY on the second ring is NOT
  claimed** — `NUE`'s OBV is accumulating but its rs20 is **−5.2**, so the money leg fails. ⇒
  **watchlist with a dated re-check: 2026-09-08.** No name handed to BET.

## Card 2 — ★★★ Hormuz: the Strait hardened and partially reopened in the same 72 hours

- **Thread**: Hormuz · **REIGNITED**, curve **14→2→2 outlets** (08-18 → 08-24) · `theme-age
  "Strait of Hormuz"` ⚪ECHO **0.73×** on a **8,059** base — **unreadable width** (`D340`);
  the narrow terms are **`economic D-Day` 🟢FRESH age 4 (base 141)** and **`Iraqi tankers` 🟢FRESH
  age 2 (base 3, too thin to rate)**.
- **Direction (body-read, and it cuts BOTH ways — this is why the card exists):**
  **Hardening**: `MINOAN DIGNITY` (IMO 9294484), a Liberia-flagged bulk carrier, **struck in its engine
  room while transiting outbound, chief engineer killed, 08-17→18, UKMTO-confirmed**; `AMARA` (IMO
  9333280), a products tanker, **seized near Qeshm 08-17** — the first confirmed Iranian seizure since
  06-22; IRGC high-speed-craft readings **338 (08-09→16) vs 209** prior. **The US announces its
  strictest-ever sanctions today** — Bessent's FT op-ed, *"economic D-Day"*, presser **14:00 ET 08-24**.
  **Softening**: **Iran granted special transit permits to some Iraqi tankers** (IRNA via Reuters
  08-22; `aljazeera`, `hellenicshipping` ×2 bodies), **on repeated Iraqi diplomatic requests** — with
  **neither of the IRGC's two named conditions mentioned anywhere in the chain**.
- ★★ **This is the `S74` settlement (HANDOVER §2b): `FIRED-C`, with its own anti-signal (a) partially
  fired.** The Strait now has a **third channel — bilateral exception-granting** — that neither the
  retired Oman frame nor the two-conditions frame covers.
- **Exposure** (`asof 2026-08-21`, all 🟡 because none clears `vol_surge ≥ 1.2` — §SWEEP §3):
  `PSX` **+0.728** 매집 rs60 **+37.0** (surge 1.11) · `MPC` **+0.700** 매집 rs60 **+44.0** (1.06) —
  *both held* · `VLO` +0.506 매집 rs60 **+43.1** (0.71) · `COP` +0.694 매집 rs60 +15.1 ·
  `CVX` +0.369 매집 · `XOM` **−0.183, OBV 분산** — *the control, and it is dispersing while its sector
  accumulates*. ⚠ Tankers (`FRO`, `STNG`, `DHT`, `TNK`) are **not in the universe** — untaggable.
- **Future — both branches, dated:**
  **IF** hardening dominates → by **2026-08-28** (`FRO` earnings, and `P89`'s settle) the Energy basket
  holds 5-session excess vs `SPY` ≥ **+2.00pp** (today **+3.519**) **and** the refining rs60 spread
  persists. **KPI:** `theme-age "economic D-Day"` (today FRESH, age 4) and vessel-incident counts.
  **ELSE / KILL** → **the exception channel widens**: ≥2 further counterparties receive named transit
  permits by **2026-09-08**, in ≥2 outlet bodies each ⇒ a de-facto reopening occurs **without either
  named condition being met**, the war-premium leg of the ENRG OW deflates, and this card is void.
- ⚠ **LIVE INTRADAY PRINT, not in the 08-21 frame:** Brent **−1.3% to $93.16**, WTI **−1.9% to $85.42**
  (04:32 ET 08-24), attributed in-body to the Iraqi permits. **The tape's first vote went to the
  softening leg.**
- **Cell**: **CONFIRMED-EARLY, two-sided.** `MPC`/`PSX` are held and accumulating; the card's value is
  that it now carries a **named kill condition** the desk did not have before. Handed to ROTATION as
  ENRG cross-evidence and to BET §B as **re-justification, not as a new candidate.**

## Card 3 — ★★ The Treasury tried to fix the long end on 08-19, and the long end did not move

- **Thread**: `Treasury buyback` · **🟢FRESH, age 5 days, base 201** — the board's only FRESH theme ·
  paired with `national debt` **🟡ACCELERATING 7.82×** (base 278).
- **Direction (body-read — and the headline direction is the OPPOSITE of the naive read):**
  **Bessent DOUBLED long-bond buybacks "in the face of surging yields"** (`yahoo_finance` 08-19;
  `seekingalpha` 08-19 *"U.S. Treasury Ups Its Buying Of Long-Dated Treasuries"*). **The sell side does
  not believe it**: *"Bessent Doubling The Treasury Buyback Program Is Just A Deck Chair Trade"*
  (`seekingalpha` 08-23) · *"Treasury buybacks raise fiscal questions"* (BBH via `fxstreet` 08-20) ·
  *"analysts cast doubts over long-term impact"* (`fxstreet` 08-21) · ING: *"buybacks favor pro-risk FX,
  not the Dollar"*.
  ★★ **And the tape agrees with the skeptics: `DGS30` sits at the 96.4th percentile of its own year
  (5.23) on 08-20, the day AFTER the doubling was announced** (`M870`). The intervention is dated and
  the long end did not fall.
- **Exposure**: 🚨 the honest answer is **there is no clean equity exposure**, and saying so is the
  card. `chain-hop "Treasury buyback"` returned `NDAQ` (headline-named, 6 title / 12 body — *held*,
  flow −0.025 🟡), and its proximity candidates were **`COIN` (8/20)**, **`META` (7/44)**, `BLK` (3/9),
  `GS` (2/5) — the `COIN`/`META` proximity comes from *bitcoin* articles (*"How a Treasury buyback tweak
  helped bitcoin surge 25%"*), **not from a Treasury-exposure chain**. ⚠ **Flagged as chain-hop noise,
  not carried as exposure.** Measurable: `BLK` +0.385 🟡 매집 · `GS` **−0.524 🔴분산** ·
  `SCHW` +0.454 🟡 매집 rs60 **+29.1**.
- **Future — both branches, dated:** **`P94` carries this card.** **IF** supply owns the long end →
  at the first close covering **2026-08-27** `[FRED]`, `DGS30` ≥ **5.31** (its 365-day max) **AND**
  `T10YIE` ≤ 2.38. **ELSE / KILL** → `DGS30` ≤ **5.10** with `T10YIE` in 2.28–2.40 ⇒ the buyback
  worked, the $40tn narrative is a headline, and this card is void.
- ★ **Self-correction to `MACRO §D` recorded here rather than edited away**: `P94`'s VOID leg names
  *"an announced buyback-size change inside the window."* **The doubling was announced 2026-08-19 —
  BEFORE the 08-21→08-27 window opens.** It is therefore the row's **prior, not its voider**, and P94
  is *strengthened* by that, not voided. The MACRO sentence is left standing with this correction
  appended (`D48` discipline).
- **Cell**: **STORY-ONLY** — a genuine macro object with **no clean equity handle in this universe**.
  Watchlist, dated re-check **2026-08-28** (July PCE).

## Card 4 — ★★ Jackson Hole: Warsh's first speech as Chair, and the instrument only sees it when narrowed

- **Thread**: `Jackson Hole` **🟡ACCELERATING 14.9×** (base 296) — the board's **second-fastest** ratio ·
  `theme-age Warsh` ⚪ECHO **0.85×** on a **3,628** base ⇒ **17.5× ratio difference on one event, from
  term width alone** (`M861`, `D340`) · thread one-liner: *"Kevin Warsh to Make First Jackson Hole
  Speech as Fed Chair"* curve **4→6→5**.
- **Direction (body-read)**: the calendar is the fact — **Jackson Hole opens 2026-08-27**, and
  `catalyst_calendar --days 10` **still does not carry it** (its only entries are July PCE 08-28 and the
  undated Hormuz row) — **3rd consecutive run of that miss.** The event is confirmed from news bodies,
  not from the calendar tool.
- **Exposure**: the desk's measured rate betas say the duration underweight has **no rate beta**
  (`XLU` +0.0049 · `XLRE` −0.0072 · `XLP` +0.0224 · `XLV` +0.0185 per bp of Δ10y) while **`XLE` has
  +0.1534**. ⇒ **the desk's only rate-exposed tilt is its ENERGY OVERWEIGHT, with a positive sign.**
  Measurable names: `NEE` **−0.600 🔴분산** · `CEG` −0.625 🔴 · `VST` −0.689 🔴 (Utilities is 0.0%
  participation — SWEEP §3) vs `MPC`/`PSX` above.
- **Future — both branches, dated:** **IF** Warsh delivers a hawkish-supply message → `DGS2` breaks its
  four-session **4.19** print and closes ≥ **4.30** at the first observation covering **2026-08-27**
  (**`S102` branch A**, thresholds frozen). **ELSE / KILL** → `DGS2` ≤ 4.08 with `30y−10y` ≥ 0.59
  (**branch B**) — or, the disclosed favourite, neither (branch C).
- ⚠ **`S102` remains UNSETTLED for a 5th run because `DGS2` publishes late** (§HANDOVER 2c): the H.15
  family ends **08-20** while `T10YIE` and `SOFR` carry **08-21**. **The next settle attempt is
  2026-08-25.**
- **Cell**: **STORY-ONLY** (macro, no clean single-name handle). Dated re-check **2026-08-27**.

## Card 5 — ★ Hong Kong equity raises: two in 48 hours, and the fast one does NOT qualify

- **Thread**: `Shein` HK IPO **BUILDING 2→4→16 outlets** · `Alibaba` placement **BUILDING 7→9** ·
  `theme-age "Hong Kong IPO"` ⚪ECHO **1.28×** on a 134 base — **the instrument does not see a cluster
  the event tier plainly shows.**
- **Direction (body-read — and it KILLS half the card):**
  **Shein is a down-round, not IPO fever.** *"Shein Launches $27 Billion IPO, **Down 70% From Its Peak
  Valuation**"* (`forbes` 08-24) · seeking **$1.77bn** (`seekingalpha` 08-24) · *"postpones Hong Kong
  debut to September"* (08-20) · *"PE backers may have to hold on a little longer"* (08-21) · and
  **`US launches national security probe into the Shein–Everlane deal`** (`bloomberg` + `yahoo_finance`
  08-24). ⚠ **`brief`'s head framed the cluster as "IPO Fever Heats Up"; the bodies say a 70% down-round
  under a fresh US national-security review.** A headline-only card here would have been wrong (`M871`).
  **Alibaba is the qualifying leg**: **$10.2bn HK placement to fund AI**, and **`BABA` shares slid on it**
  (LIVE INTRADAY PRINT, 08-24 wire).
- **Exposure**: 🚨 **`BABA` is not in `us_top300`** (§0-a) — **UNTAGGABLE.** `PDD` (+0.404 🟡 매집,
  rs60 **+0.0**) is the nearest measurable China-ADR proxy and is **not** the issuer. **No substitute is
  carried as exposure.**
- **Future — both branches, dated:** **`P95`.** **IF** an AI-financing rotation → **≥2 further** HK
  raises ≥$1bn by **2026-09-05** whose reported use of proceeds names AI/data-centre/compute, ≥2 outlet
  bodies each. **ELSE / KILL** → zero such raises by 09-05 **and** `theme-age "Hong Kong IPO"` ≤ 1.5×.
  ★ **Shein does not count toward the observable** — fast fashion, no AI use of proceeds. **The two
  legs of this thread are one cluster and two different objects, and the card says so.**
- **Cell**: **Shein → DEAD as an AI-financing object** (re-filed as a separate down-round/probe story
  with a dated re-check **2026-09-05**, per the "DEAD is a money verdict" rule — its money axis was
  never measured because the name is untaggable). **Alibaba → STORY-ONLY, untaggable.**

## Card 6 — ★★ `NVDA` prints in two sessions, and the options market says the information is about MEMORY

- **Thread**: `theme-age "Nvidia earnings"` **🟡ACCELERATING 14.11×** (base 118) — the board's
  **fastest** narrow-term ratio · `catalyst_calendar` confirms **NVDA 2026-08-26 (D-2), 🔀binary**.
- **Direction (inherited `[measured]`, not re-derived — HANDOVER §1)**: `M818` — **NVDA notified
  customers of >15% server price increases with MEMORY COSTS named as the cause** (8 outlets), three
  days before the print, alongside Samsung's up-to-15% foundry increase. `S117` registered the sharper
  fact: **`MU` carries a HIGHER ATM IV than `NVDA` on the identical 08-28 expiry (0.650 vs 0.606) with
  no `MU` print until 09-24** ⇒ the options market prices NVDA's print as being about **memory**.
- **Exposure** (`asof 2026-08-21`): `NVDA` **−0.181 🟡 중립** surge 0.75 — *held* ·
  `MRVL` **+0.583 🟡 매집 rs20 +18.4 rs60 +17.3** (prints **08-27**) · `AVGO` −0.221 🟡 중립 rs60
  **−14.7** — *held*, prints 09-02 · `MU` −0.278 🟡 중립 · `WDC` **−0.781 🔴분산 rs20 −15.2** ·
  `SNDK` +0.144 🟡 · `HPE` **+0.489 🟡 매집 rs60 +41.6** — *held* · `DELL` **−0.478 🔴분산** but rs60
  **+42.8**.
  ★ **The memory leg is the weakest tape on the board while the narrative says memory is the cause** —
  `MU` 중립, `WDC` 🔴분산. **That is a contradiction the print resolves, and it is stated rather than
  smoothed.**
- **Future — both branches, dated:** **`P90` (08-26) carries it.** **IF** the >15% increase is margin
  expansion → the print guides gross margin up and `MU`/`SNDK` follow. **ELSE / KILL** → it is a cost
  pass-through: NVDA's margin guide is flat-to-down while memory names rally ⇒ the AI-compute epicentre
  re-rates **downward** relative to its own supply chain.
- ⚠ **`S103`'s hand-set ±5.0pp band sits INSIDE the implied move (`NVDA` ±6.11%, 08-28 expiry) and is
  pre-declared NO-INFORMATION** (`D242`, not re-banded). `S115` was written outside it.
- **Cell**: **LATE-MONEY.** Two of three names are held; the thread is at 14.11× two sessions before a
  binary. **No new candidate is handed to BET** — a card that arrives D-2 into a 🔀binary is a
  valuation/timing note, not an entry.

## Card 7 — ★ Health Care is the board's best sector on three instruments and has no story

- **Thread**: **none.** ★ **That is the card.** `theme-age` has no HC bucket in this desk's term table;
  `brief`'s 08-23 head carried no HC cluster; `thread`'s top-20 carried none.
- **Direction**: unmeasured — and stated as unmeasured, not as "quiet" (the sweep's silence is the pipe,
  and 265 single-outlet events went unseen).
- **Exposure**: `MRK` **+0.978 🟢가속** OBV 매집 rs20 **+12.8** rs60 **+24.8** surge **1.56** — one of
  only six greens on the board, and the **only** 🟢 in the shortlist that also sits in an OW sector.
  Sector: `wflow` **+0.196** (rank 1) · `eqflow` **+0.229** (rank 1) · **participation 59.4% (rank 2)** ·
  `exc5` **+3.889 vs SPY (rank 1)**.
- **Future — both branches, dated:** **IF** the sector's leadership is real → by **2026-09-03** the HC
  basket holds `exc5` ≥ **+1.00pp** vs `SPY` **and** participation stays ≥ 50%.
  **ELSE / KILL** → `exc5` ≤ **0.00pp** by 09-03 ⇒ the 08-21 reading was a one-week rotation artifact.
  **KPI:** register an HC term in the living table before the next run and read its age.
- **Cell**: 🚨 **CONFIRMED-EARLY on money, ZERO on narrative — the board's largest coverage gap.**
  Handed to ROTATION as the one sector where flow and grade agree but **no proposition exists**
  (MACRO §E flagged the same hole). **Filed to the miss ledger** (§9) rather than converted to a
  candidate, because a card with no direction body-read may not become one.

## Card 8 — ★★ Shell's $8bn US chemicals exit, with `XOM` bidding — found only by the blind-spot pass

- **Thread**: **not in `thread` at all.** Surfaced by `burst`: **`CHEMICALS` z 13.2**, the highest on
  the board, 6 articles / 4 outlets, **100% market relevance**, against a term table with no chemicals
  bucket. `theme-age chemicals`-adjacent narrow terms are ≤1 day old.
- **Direction (body-read, ≥5 sources):** **Shell is selling its US chemicals business — ~$8bn, four
  Louisiana sites — and the named interested parties are `XOM`, LyondellBasell and Apollo** (FT 08-24,
  via `yahoo_finance`, `seekingalpha`, `oilprice`, `investing_en` bodies + a `bloomberg` title).
  `chain-hop chemicals` independently surfaced **`APO`** as a one-hop candidate (4 proximity / 5 body,
  example article = the Shell story itself) while `XOM` was **headline-named 22 times** — i.e. the tool
  correctly separated the crowded layer from the one-hop.
- **Exposure**: 🚨 **`LYB` and `DOW` are outside the universe — UNTAGGABLE** (§0-a). Measurable:
  `XOM` **−0.183 🟡, OBV 분산**, rs60 +9.6 · `APO` +0.255 🟡 중립 rs20 +4.6 · `CVX` +0.369 🟡 매집 ·
  `APD` +0.194 🟡 매집 (industrial gases, adjacent) · `PSX` +0.700 🟡 매집 (chemicals JV exposure).
- ★ **The finding that makes this a card and not a headline**: **`XOM` is carried in this desk's
  standing view as a 🔴RESOLVED *control* for crack-spread attribution — explicitly "a control, not a
  bet."** A control that bids **$8bn** for a downstream asset is doing something a control does not do,
  and **its own OBV is dispersing (−0.101) while its sector accumulates.** Combined with `brief`'s
  08-23 head item *"One of Exxon's Biggest Oil Fields Is Running Out of Room"* (11 articles / 7
  outlets), the **capital-allocation** story on `XOM` is now two-sided and unowned.
- **Future — both branches, dated:** **IF** the sale proceeds with `XOM` as buyer → a definitive
  agreement naming the buyer and a price, in ≥2 outlet bodies, by **2026-09-30** ⇒ `XOM`'s
  🔴RESOLVED control status must be re-argued or retracted. **ELSE / KILL** → no definitive agreement
  by 09-30, or a non-`XOM` buyer ⇒ the item is Shell portfolio news with no US read-through and this
  card is void.
- **Cell**: **STORY-ONLY**, with a **dated ledger consequence** rather than a candidate: `XOM`'s
  standing 🔴RESOLVED row (ledger `A.flow미도착` → 09-16) now has a **competing, dated observable.**
  Handed to ROTATION as Materials/Energy cross-evidence.

---

## 9 · Ledger entries filed by this stage

**Rejections (`reject_ledger`) — 0.** No card was dropped on a money verdict; the two DEAD/void legs
(Shein-as-AI-financing; the `COIN`/`META` chain-hop proximity) were killed on **direction body-reads
and tool-noise diagnosis**, not on flow, and both are re-filed with dated re-checks inside their cards
rather than dropped.

**Misses (`missed_ledger`) — 4 filed**, all `prospective`:

| Ticker | Class | Why | `--enters-if` | Recheck |
|---|---|---|---|---|
| `MRK` | `Q.확신부족` | Card 7 — board's only 🟢 inside an OW sector, and this stage could not produce a direction body-read for it (no HC thread exists) | an HC term registered in the living table reads 🟡ACCEL or 🟢FRESH **∧** `MRK` holds OBV 매집 with rs20 > 0 | 2026-09-03 |
| `MRVL` | `M.숏리스트탈락` | Card 6 — flow **+0.583**, OBV 매집, rs20 +18.4, rs60 +17.3, **fails the 🟢 gate on `vol_surge` 0.85 alone** | post-print (08-27) `vol_surge` ≥ 1.2 **∧** OBV still 매집 | 2026-08-28 |
| `MSTR` | `Q.확신부족` | The shortlist's only clean-rise name (FINRA z **−1.23**), flow +1.000, rs20 +26.5 — **but rs60 −24.7**, i.e. a 20-day spike on a losing 60-day base (the `D306` exhaustion-geometry class) | rs60 turns ≥ 0 **∧** OBV stays 매집 | 2026-09-08 |
| `FCX` | `S.테마회피` | Card 1's cleanest chain-hop (flow +0.739, OBV 매집, rs20 +18.8) — **avoided because `Copper` COT sits at the 100th percentile long**, not because the name failed | `Copper` COT 1y percentile ≤ 80 **∧** `FCX` OBV still 매집 | 2026-09-08 |

⚠ **Sign hygiene**: the miss ledger's `excess` is **inverted** relative to the rejection ledger and the
two are not summed.

## 10 · Book cross-check — ENDED threads under open positions

🚫 **No `ENDED` label is actionable this run** (§0 — weekend denominators). **Nothing is flagged to the
book desk on a label.** Flagged on **content** instead, and only where a body-read supports it:
- **`XOM`** — Card 8. Its standing role (🔴RESOLVED *control*) is contradicted by an $8bn bid. **Not a
  thesis change; a request that the role be re-argued or retracted at BET.**
- **`NUE`** — Card 1. **Canada's retaliation list names steel** and `S114` (settles 09-03) is the
  steel/tariff bracket already pointed at this held name. **The card supplies its object; the bracket
  is unchanged.**
- **`NVDA` / `AVGO` / `HPE`** — Card 6. **D-2 into a 🔀binary.** No action from this stage (P4).

## 11 · Instrument observations (dig candidates for `RESEARCH.md` Part C at run end)

> 3-grep at WRITE time across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`: `D341`, `D342`,
> `M868`–`M871` **0 hit** in all three.

| id | Finding | Positive-form remedy |
|---|---|---|
| **`D341`** | 🚨🚨 **The desk cannot tag the names its own discovery layer surfaces.** `AA`/`X`/`WY` (the Canada-tariff epicentre — the run's **#1** object), `LYB`/`DOW` (the named counterparties in the $8bn chemicals sale), and `BABA` (the issuer in the $10.2bn placement) are **all outside `us_top300`**. **Three of eight cards therefore carry no flow-tagged principal** (`M868`). This is the 2026-08-10 `TSM`/`LNG` invariant extended one step: not "what it holds", but "what it finds" | **Rebuild the universe with `--include AA,X,WY,LYB,DOW,BABA` (and re-examine the tanker set `FRO,STNG,DHT,TNK` already flagged) — the builder supports the union today. ★ And add a standing step to EVENT_ALPHA: run the membership check BEFORE writing cards, so an untaggable principal is declared rather than quietly replaced by a taggable neighbour.** Also fixes the 40-day staleness that decides news-bucket membership (`D336` neighbourhood) |
| **`D342`** | ★★ **The desk's two trade-war brackets both settle ELEVEN DAYS BEFORE the tariffs they measure take effect.** `P92` and `P93` close **2026-08-28**; **Canada's retaliation begins 2026-09-08** (`aljazeera` 08-23, named date) (`M869`). They can only measure the **announcement**, never the **implementation**, and **no row on this board is keyed to 09-08** | **Register a successor bracket at PREMORTEM keyed to 2026-09-08** with the sector observable measured across the effective date, not before it. **And add to the registration checklist: when a bracket's object has a named effective date, the settle date is compared to it and the gap is written into the row** |

---
*Analytical output only — forward cards, no buy/sell recommendation and no sizing (P4).*
