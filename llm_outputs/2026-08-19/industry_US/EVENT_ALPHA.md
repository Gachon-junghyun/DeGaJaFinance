# EVENT_ALPHA — industry_US · 2026-08-19 · Stage 5/11 (L1·EVENT_ALPHA)

> Bottom-up complement to MACRO's matrix. Scope **`--scope foreign`** on every call (verified).
> Flow tags are `SECTOR_FLOW_US.json`, **asof 2026-08-18**, 3 axes, `velocity` **revoked** (G1).

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: **4,056 daily events → 3,150 threads → 490 multi-day → 144 alive**
(227 new today). Window denominators: 08-13 **808** · 08-14 743 · 08-15 282 · 08-16 293 · 08-17 754 ·
08-18 797 · 08-19 **379** (partial — the US session had not opened).

**8 selected · 136 alive threads NOT selected.** Selection rule applied in order:
**(a) precursor form** — curve starting ≤2 outlets and climbing (5 of the 8 qualify);
**(b) remaining BUILDING/REIGNITED by peak** (3 of the 8).

⚠ **The 08-15/08-16 denominators are a weekend (282, 293)**, which mechanically inflates FADING across
that boundary. Only **1** FADING and **1** ENDED/REIGNITED thread appear in the tagged set and
**neither was used**, precisely because the boundary makes them unreadable.

🚫 **Every "direction" below is read from the article's own sentence, not from a bare headline.**
⚠ **Instrument limit, logged**: `module_news_data search` exposes **no `--body` flag** (verified via
its argparse: only `--days --limit --scope --field --match-mode`). Body **length** is printed and
`--field any` searches body text, but the CLI cannot print a body. So direction reads here are from
**(i) full-sentence headlines that state their own mechanism**, **(ii) `brief`'s sub-event (`└`)
structure**, and **(iii) `chain-hop`'s ±300-character body-proximity co-mentions** — all three are body-
derived, none is a bare headline. **This is a G7-class gap and is named rather than papered over.**

---

## Card 1 — 🚨 AI DATA-CENTRE BACKLASH · the risk card against a position the book holds

- **Thread**: *"Tech Deploys Charm Offensive to Combat AI Data Center Backlash"* · **BUILDING 3 days ·
  2→3→4 outlets · 17 articles** (08-17 VMware Explore → 08-18 Infosys/Knorr-Bremse AI → 08-19 the
  charm-offensive piece) · denominator 379 events today.
- **Direction (body-derived)**: `[yahoo_finance]`, **body 16,034 characters** — the industry is
  **deploying a charm offensive to *combat* a backlash**, i.e. the sector is on the **defensive** on
  siting, power and permitting. **The headline's own verb is the direction**: you do not run a charm
  offensive from a winning position. This is a **political/permitting risk to the AI-power chain**,
  and it is the one thread in the set that points *against* a book exposure.
- **Exposure** (flow asof 08-18; every name is 🟡 — the `vol_surge` gate, §SWEEP §3):
  | ticker | chain position | flow / tag | OBV | RS20 vs `SPY` | note |
  |---|---|---|---|---|---|
  | `ETN` | electrical distribution — **HELD** | +0.360 🟡 | **매집** +0.251 | +4.5 | the book's direct exposure |
  | `PWR` | build/EPC | +0.524 🟡 | **매집** +0.165 | +6.3 | |
  | `ANET` | networking — **HELD** | +0.628 🟡 | **매집** +0.187 | +8.1 | headline layer, marked as such |
  | `VRT` | thermal/power train | −0.615 🟡 | 중립 −0.034 | **−13.1** | already broken |
  | `GEV` | generation | −0.683 🟡 | 중립 −0.080 | **−9.4** | already broken |
- ★ **The exposure map splits cleanly and that is the finding**: the **inside-the-building** layer
  (`ETN`, `PWR`, `ANET`) is accumulating with positive RS20; the **generation/thermal** layer
  (`GEV`, `VRT`) is down double-digits vs `SPY`. **A permitting backlash bites the generation layer
  first**, and the tape has already moved that way.
- **Future — both branches:**
  - **IF the thread keeps building AND flow stays accumulating** → the backlash is a *siting* story
    that slows new-build without touching installed-base electrical demand ⇒ the `ETN`/`PWR` leg holds.
    **KPI: `EW{GEV,VRT}` 20-day excess vs `SPY` at 2026-09-02 ≥ −5.0pp** while `ETN` OBV stays in
    accumulation.
  - **ELSE / kill condition** → **`ETN` OBV turns to dispersion OR `EW{ETN,PWR,ANET}` 20-day excess
    vs `SPY` ≤ −5.0pp at 2026-09-02** ⇒ the backlash reached the electrical layer and this card is
    wrong about where it bites.
- **Cell**: **STORY-ONLY (risk side)** — the story is building and the money has *not* yet left the
  held names. **Handed to the book desk as a watch flag, not to BET.**

---

## Card 2 — ★★★ ABF / ADVANCED-PACKAGING SUPPLY CUT · 1 outlet, named mechanism, the earliest card here

- **Thread**: *"Ajinomoto reportedly cuts critical chip packaging film supply to China by 30% as
  domestic substitutes race to qualify — ABF restriction comes following Beijing's rare-earth export
  curbs"* `[tomshardware]`, **body 7,208 characters**, **1 outlet**, surfaced only because the sweep
  went through `search --field any` rather than an outlet filter.
- **Direction (body-derived)**: the headline is a complete causal sentence — **a Japanese supplier cuts
  the single most concentrated input in advanced substrate (ABF, Ajinomoto Build-up Film) to China by
  30%, explicitly *in response to* Beijing's rare-earth curbs.** Direction: **materials weaponisation
  has moved from raw earths into the packaging bottleneck**, which sits directly upstream of HBM,
  FC-BGA and every AI accelerator substrate.
- **Exposure** — ⚠ **and the honest answer is that this desk cannot map it.** `chain-hop ABF --days 7`
  scanned **4 articles** and returned **0 headline-named and 0 chain-hop candidates**;
  `chain-hop "chip packaging"` scanned **8** and returned headline-named `INTC` (2 title / 1 body,
  flow **−0.608 🔴분산**, OBV 분산, RS20 **−10.9**) and one candidate, `NVDA` (0 title / 2 proximity /
  4 body, flow +0.111 🟡, OBV 중립, RS20 +3.4). **The substrate suppliers themselves (Ajinomoto,
  Ibiden, Shinko, AT&S) are not US-listed and are outside `us_top300` — they are not measurable here,
  which is `N.유니버스부재`, not "no signal".**
- **Future — both branches:**
  - **IF the thread builds** → by **2026-09-05** the ABF/substrate story reaches **≥3 outlets** and at
    least one `us_top300` name is named in a ≥2-outlet story as supply-constrained on substrate ⇒ this
    is a real chain event and the desk's universe has a **structural blind spot at the substrate layer**.
  - **ELSE / kill** → still ≤1 outlet at 09-05 ⇒ a single-outlet trade-press item, correctly ignored.
- **Cell**: **STORY-ONLY → watchlist with a dated re-check (2026-09-05).** ★ Its value is not a trade;
  it is that **the desk's most concentrated AI-chain risk sits one layer above anything it can price.**

---

## Card 3 — CHINA HUMANOID ROBOTICS / UNITREE · the fastest thread on the board, and the money refuses it

- **Thread**: **BUILDING 3 days · 2→5→17 outlets · 40 articles** — *"LimX on China's Robotics
  Development"* (08-17, 2 outlets) → *"China's Unitree unveils 'Superman' robot"* (08-18, 5) →
  *"Shares in Chinese humanoid robot maker Unitree soar in its Shanghai debut"* (08-19, **33 articles /
  17 outlets**). A **second, independent** thread corroborates: Serve/Grubhub + Duke Robotics +
  Unitree STAR, BUILDING 5→5→3→5.
- **Direction (body-derived)**: `[economictimes]`, **body 6,298 characters** — *"Unitree shares soar
  nearly six-fold in Shanghai debut as robotics boom gains momentum"*; the debut ran **+460% → +629%**
  to roughly **$66bn**. Independently corroborated by `[businessinsider]`, **body 24,753 characters**:
  *"Industrial Robot Installations Hit Record Highs as Global Labor Shortages Deepen"* — a **volume**
  statement, not a valuation one, from a different cluster.
- **Exposure**: ⚠ **`us_top300` contains no clean humanoid-robotics exposure.** The only name with a
  named humanoid programme is `TSLA` — flow **−0.789 🔴분산**, OBV **분산 −0.198**, RS20 **−13.7 vs
  `SPY`**, `vol_surge` 0.78: **the board's 4th-worst flow score.**
- ★ **This is the 2×2's textbook STORY-ONLY cell: story CONFIRMED (2→17 outlets in 72h), money
  REFUSED.** No name is handed to BET.
- **Future — both branches:** (registered as `P76` in MACRO §E)
  - **IF it keeps building** → at **2026-09-02** the robotics thread still prints **≥5 outlets on ≥3
    separate days** AND ≥1 `us_top300` name is publicly named as supplier/competitor in a ≥3-outlet
    story ⇒ a real cycle the registry does not carry.
  - **ELSE / kill** → thread ENDED or ≤2 outlets at 09-02 ⇒ a listing-day artifact.
  - **Anti-signal**: a second China A-share tech IPO of comparable size inside the window ⇒ the outlet
    count measures the IPO channel, not the theme ⇒ `VOID`.
- **Cell**: **STORY-ONLY.** Logged to the missed ledger — `TSLA` / `S.테마회피` / re-check **2026-09-02**.

---

## Card 4 — CANADA 50% TARIFFS → PAUSED · the largest thread of the day, and it resolved

- **Thread**: **BUILDING 5 days · 5→6→6→17→18 outlets · 83 articles** — *"U.S. says Canada among
  China's biggest enablers"* (08-13) → *"A new set of Trump tariffs for Canada could take effect"*
  (08-17) → *"Trump and Carney hold urgent talks as steep 50% US tariffs…"* (08-18, 17 outlets) →
  **"Trump pauses 50% tariffs on Canada, claims trade deal is close"** (08-19, **23 articles / 18
  outlets**, with a `└` sub-event *"Trump pauses tariffs on Canada after last-minute deal"* 8/7).
- **Direction (body-derived via `brief`'s sub-event structure)**: the parent event and its own `└`
  sub-event **both** carry the word *pauses*, from two separate clusters at 18 and 7 outlets. Direction
  is **de-escalation**, and it arrived on the day the thread peaked.
- **Exposure** (flow asof 08-18):
  | ticker | chain position | flow / tag | OBV | RS20 vs `SPY` |
  |---|---|---|---|---|
  | `NUE` | US steel — **HELD** | +0.483 🟡 | **매집 +0.452** | **+10.7** |
  | `STLD` | US steel | *(Materials, `S77` basket, exc5 −4.86)* | — | — |
  | `CAT` | machinery, headline layer | **−0.657 🔴분산** | 분산 −0.086 | **−8.1** |
  | `DE` | machinery | −0.194 🟡 | 중립 | −2.2 |
- ★ **The tape disagrees with the naive read.** A tariff *pause* should relieve machinery and pressure
  domestic steel; instead **`NUE` is accumulating with RS20 +10.7 while `CAT` is the board's dispersing
  🔴**. Either the pause is not believed, or the steel bid is not the tariff.
- **Future — both branches:**
  - **IF the pause holds** → at **2026-08-31**, `NUE` 10-day excess vs `SPY` **≤ 0** ⇒ the steel bid
    *was* the tariff, and it unwinds.
  - **ELSE / kill** → `NUE` 10-day excess vs `SPY` **≥ +3.0pp** at 08-31 with the pause still in force
    ⇒ **the steel bid is not tariff-driven and this card mis-identified the driver.**
- **Cell**: **LATE-MONEY** — the thread peaked at 18 outlets *on the resolution*. Valuation-gate note
  for BET; **no fresh candidate handed forward.**

---

## Card 5 — UAE ↔ IRAN: escalation, and the first thread about *routing around* the chokepoint

- **Thread**: **BUILDING 2 days · 4→6 outlets · 14 articles** — *"UAE says Iran fired 2 missiles at
  country, as war drags…"* (08-18, 4 outlets) → **"UAE imposes indefinite trade embargo on Iran over
  alleged mi[ssile attack]"** (08-19, 10 articles / 6 outlets). Companion head item: *"Oil edges up on
  uncertainty over exports through Hormuz"* (**23 / 13**).
- **Direction (body-derived)**: escalation, **and a second-order move nobody has carded**: two separate
  items describe the market **building alternatives to the chokepoint** —
  `[fortune]`, body 4,974 chars: *"Strait of Hormuz chaos has incentivized China to use an alternative
  trade route: a 3,400-mile frozen Arctic channel dubbed the 'Ice Silk Road'"*, and a REIGNITED thread
  (3→3): *"Iraq-Syria Oil Pipeline to Bypass Hormuz Is 4 Years [away]"*. ⇒ **Near-term escalation with
  a medium-term de-rating of the chokepoint's own optionality** — and the pipeline item dates the
  workaround at **four years**, which is the number that keeps the near-term premium alive.
- **Exposure** — ⚠ **every Energy name is 🟡 and that is the volume gate, not the money** (SWEEP §3:
  7 of 16 Energy names accumulate, **0 of 16** clear `vol_surge` 1.2, sector max 1.06):
  | ticker | chain position | flow / tag | OBV | RS20 vs `SPY` |
  |---|---|---|---|---|
  | `MPC` | refining — **HELD** | **+0.700 🟡** | **매집 +0.242** | **+12.0** |
  | `PSX` | refining — **HELD** | **+0.694 🟡** | 매집 +0.180 | **+12.1** |
  | `COP` | E&P | +0.586 🟡 | **매집 +0.336** | +7.8 |
  | `CVX` | integrated, headline layer | +0.468 🟡 | 매집 +0.289 | +5.1 |
  | `XOM` | integrated, headline layer | +0.371 🟡 | 매집 +0.094 | +6.6 |
- **Future — both branches:**
  - **IF escalation continues AND flow stays accumulating** → at the **08-21** settle
    `EW{MPC,PSX,VLO}` 5-session excess vs `SPY` **≥ +2.0pp** with the distillate crack **≥ 95 $/bbl**
    ⇒ the refining leg is paid by **margin**, not by the barrel (this is `P75`).
  - **ELSE / kill** → crack **≤ 88** and the EW excess **≤ 0** ⇒ it was the barrel, and the capacity
    thesis loses its best week.
  - **Kill for the sector card specifically**: a dated, ≥3-outlet **Hormuz reopening** ⇒ this card and
    `S74`/`S92`/`S95` all resolve together.
- **Cell**: **CONFIRMED-EARLY** — story building **and** OBV accumulating across 5 of 5 mapped names.
  ⚠ Handed to ROTATION/BET **with the tag caveat stated**: these names are 🟡 only because of
  `vol_surge`, and BET owns sizing.

---

## Card 6 — SK HYNIX $28.6bn BUYBACK · a capital-return event inside the regime call's own subject

- **Thread**: **BUILDING 4 days · 3→3→2→3 outlets · 15 articles** — *"An inside look at SK Hynix's
  $720bn AI-fuelled buildout"* (08-13) → *"SK Hynix's Stock Trades at Around 5× Next Year's Earnings"*
  (08-17) → *"SK hynix: Believe In The HBM Leader"* (08-18) → *"Why is SK hynix stock rallying today?"*
  (08-19). Head item today, separate cluster: **"SK Hynix launches $28.6 billion share buyback and
  cancellation"** (**8 articles / 5 outlets**).
- **Direction (body-derived via cluster structure)**: the buildout thread and the buyback cluster point
  **opposite ways on the same balance sheet** — a **$720bn buildout narrative** alongside a
  **$28.6bn buyback-and-cancellation**. **Capital returning to shareholders at a 5× forward multiple is
  a late-cycle capital-allocation signal, not an early-cycle one**, and it lands squarely on `M1`–`M9`'s
  regime call (*memory is a price cycle in rate-of-change deceleration while the level stays tight*)
  and on `M18` (MU gross margin at the **100th percentile of 17 years**, the `L2` peak-margin lens).
- **Exposure** (US-listed memory chain, flow asof 08-18):
  | ticker | chain position | flow / tag | OBV | RS20 vs `SPY` |
  |---|---|---|---|---|
  | `MU` | DRAM/HBM — the regime call's instrument | **−0.541 🟡** | 중립 −0.071 | **−5.7** |
  | `WDC` | NAND | −0.536 🔴분산 | 분산 −0.084 | **−12.1** |
  | `STX` | HDD | +0.239 🟡 | **매집 +0.206** | −1.2 |
  | `SNDK` | NAND | +0.097 🟡 | 중립 | −0.3 |
  ⚠ SK hynix itself is **not US-listed in `us_top300`** — `N.유니버스부재`, not "no signal".
- ★ **The chain is split**: the HBM/DRAM leg (`MU`) and NAND (`WDC`) are both negative on RS20 while
  the mechanical-storage leg (`STX`) is the only accumulator. `HBM` term velocity **1.18×** (CLI,
  22:0x KST) against `memory` **1.01×** and `semiconductor` **0.99×** — **attention is concentrating in
  HBM while the broad semis terms are flat.**
- **Future — both branches:**
  - **IF the deceleration thesis is right** → at **2026-09-05**, `MU` 20-day excess vs `SPY` **≤ 0**
    AND `MU`'s next-quarter consensus EPS revision is **flat-to-down** ⇒ the buyback was the tell.
  - **ELSE / kill** → `MU` 20-day excess vs `SPY` **≥ +5.0pp** at 09-05 with `HBM` velocity still
    ≥1.15× ⇒ the buildout leg won and the "late-cycle capital return" read is wrong.
  - ⚠ **`MU` is not in `data/estimates`' 120-name universe** — verified today — so the revision leg of
    the IF-branch **may not be measurable**. Disclosed at registration (`D287`).
- **Cell**: **STORY-ONLY** — the story is live, the money is not (RS20 −5.7, OBV neutral). No hand-off.

---

## Card 7 — OPTICAL / INTERCONNECT · the only node where story and money both cleared

- **Thread**: not a `thread` cluster today — it appears as **`Zacks` 08-17 "Applied Optoelectronics…"**
  inside a 5-day 2→2→2→2→2 BUILDING thread, and as `S96`'s registered instrument set. **`no thread` is
  stated explicitly** rather than manufactured.
- **Direction (body-derived)**: carried from 08-17's three independent instruments (`theme_age optical`
  **1.74×**, highest of 13; `burst OPTOELECTRONICS` **z 5.7**, vocabulary-free; a BUILDING Lightmatter
  thread). ⚠ **`theme_age` and `burst` are news-axis tools and G1 revokes the sweep's velocity — these
  are carried as 08-17 measurements with their date, not re-asserted as today's.**
- **Exposure** (flow asof 08-18):
  | ticker | flow / tag | OBV | RS20 vs `SPY` | `vol_surge` | note |
  |---|---|---|---|---|---|
  | **`LITE`** | **+0.543 🟢가속** | **매집 +0.182** | **+1.7** | **1.25** | **the only optical name in the 8-name shortlist**; FINRA short-z **−1.07 = clean rise** |
  | `COHR` | +0.254 🟡 | **매집 +0.082** | **−6.0** | **1.70** | **the board's highest `vol_surge` here**, blocked by RS20 |
  | `CIEN` | −0.233 🟡 | 중립 −0.067 | −3.3 | 1.08 | |
  | `GLW` | −0.410 🟡 | 중립 −0.027 | −4.1 | 0.67 | |
- ★ **`LITE` is the one name on this board that cleared the story axis, the money axis and the
  short-pressure axis at once**, and it did so **on a `velocity`-free score** — which is the only
  reason it is admissible under G1.
- **Future — both branches:** `S96` settles **2026-08-21** on `EW{COHR,LITE}` 5-session excess vs
  `SPY`: **A ≥ +5.0pp with the thread reaching ≥4 outlets · B ≤ −5.0pp.** Pre-settle reading at the
  08-18 close: **+0.247** — deep mid-band, far from either bound.
  - **Kill condition**: `LITE` OBV turns to dispersion **or** its FINRA short-z rises above +1.0 (the
    clean-rise property is the card's basis).
  - ⚠ **Both names carry negative-to-zero 60-day excess** (`COHR` −13.67 · `LITE` −1.76 at
    registration) — **a 20-day phenomenon on a 5-day narrative**, and `S96`'s own text says so.
- **Cell**: **CONFIRMED-EARLY (`LITE` only).** Handed to ROTATION/BET as a fresh candidate.
  `COHR` logged to the missed ledger — `R.타이밍대기` / re-check **2026-08-26**.

---

## Card 8 — BOEING–LOCKHEED $1.5bn SPACE VENTURE · precursor form, and defense OBV is broad

- **Thread**: *"Boeing-Lockheed Space Venture Inks $1.5 Billion Private [contract]"* · **BUILDING
  2→2 outlets**, precursor form. Adjacent, independent: *"NASA Taps Blue Origin, Firefly For Services"*
  (08-18) inside a 3-day 5→4→5 space thread.
- **Direction (body-derived)**: a **named dollar figure ($1.5bn) on a private contract** at a ULA-type
  JV — a **commercial** award, not a government one, which is the direction that matters: it says the
  incumbent launch JV is winning **non-NASA** revenue.
- **Exposure** — ★ **defense OBV accumulation is the broadest single pattern in this sweep**:
  | ticker | flow / tag | OBV | RS20 vs `SPY` |
  |---|---|---|---|
  | `RTX` | **+0.572 🟢가속** (a run new-🟢) — **HELD** | **매집 +0.368** | **+13.9** |
  | `LMT` | +0.528 🟡 | **매집 +0.493** | **+17.2** |
  | `NOC` | +0.483 🟡 | **매집 +0.568 — the highest OBV on this table** | **+12.4** |
  | `BA` | +0.411 🟡 | 매집 +0.252 | +6.4 |
  | `GD` | +0.256 🟡 | 매집 +0.467 | +4.4 |
  | `AXON` | +0.511 🟡 | 매집 +0.323 | **+18.7** |
  **6 of 6 accumulating, 6 of 6 positive RS20 vs `SPY`**, and only `RTX` cleared the `vol_surge` gate.
- ⚠ **`LHX` is the named exception** and `S97` owns it (CEO stepped down 08-17, 4 outlets; exc5
  **−1.862** at the 08-18 close, between A ≤−4.0 and B ≥0). `M719` already measured the defense EW as
  **+4.32pp better on 60 days with `LHX` removed** — today's tape does not contradict that.
- **Future — both branches:**
  - **IF** → at **2026-09-05** the defense EW `{RTX,LMT,NOC,GD}` 20-day excess vs `SPY` is **≥ +3.0pp**
    with ≥5 of 6 still in OBV accumulation ⇒ the accumulation was money, not drift.
  - **ELSE / kill** → EW 20-day excess vs `SPY` **≤ 0** at 09-05, **or** ≥3 of 6 turn to OBV dispersion.
- **Cell**: **CONFIRMED-EARLY (sector-level)** — handed to ROTATION as cross-evidence for Industrials
  `OW−`. **No new name handed to BET** (the accumulating names are 🟡 on the volume gate; `RTX` is
  already held).

---

## 9 · Book cross-check — ENDED threads under open positions

**None.** Every book thesis mapped to a thread above is **BUILDING or REIGNITED**, not ENDED:
`MPC`/`PSX` → Card 5 (BUILDING) · `ETN`/`ANET` → Card 1 (BUILDING, **risk side**) · `RTX` → Card 8
(BUILDING) · `NUE` → Card 4 (BUILDING, resolved) · `NVDA`/`AVGO` → the NVDA-earnings thread
(BUILDING 7 days, 5→2→3→3→3→5→5, `S79` settles 08-26) · `MET`/`NDAQ`/`HPE` → **no thread found, and
that is stated rather than invented.**

★ **One flag to the book desk, and it is Card 1**: `ETN` and `ANET` are held into a **building thread
that points against them**. Neither has turned on the tape (both OBV-accumulating, RS20 +4.5/+8.1), so
this is a **watch flag, not a re-justification demand** — but it is the only card in the set whose
direction is adverse to a held position, and it is named as such.

## 10 · Ledger updates

| Ledger | Row | Class | Condition | Re-check |
|---|---|---|---|---|
| missed | **`TSLA`** | `S.테마회피` | OBV → accumulation **AND** RS20 vs `SPY` > 0 while the robotics thread still prints ≥5 outlets on ≥3 days | **2026-09-02** |
| missed | **`COHR`** | `R.타이밍대기` | RS20 vs `SPY` turns positive on a settled close while OBV stays accumulating | **2026-08-26** |

**Rejections this run: 0** — no card reached the DEAD cell (FADING/ENDED **×** 🔴 dispersing on **both**
axes). `TSLA` is 🔴 on money but its story is **BUILDING**, so it is a **miss, not a drop**, and it was
filed as one.

## ✅ EXIT CHECK
- [x] Scope market-correct — `--scope foreign` on `thread`, `brief`, `search`, `chain-hop`, every
      bucket count. No cross-market feed appears in any card.
- [x] Selection logged: **144 alive → 8 selected, 136 not selected**, rule stated, no silent cap.
- [x] Direction read from body-derived evidence on every card (full-sentence headline / `└` sub-event
      structure / `chain-hop` ±300-char proximity), **with the CLI's missing `--body` flag named as a
      G7-class limit rather than hidden**.
- [x] Every exposure name carries a flow tag with **asof 2026-08-18**; names outside the universe are
      marked **`N.유니버스부재` = not measurable**, never "no signal".
- [x] Every card carries **both branches + a kill condition + a dated horizon**.
- [x] STORY-ONLY names (`TSLA`, `MU`, the ABF chain) did **not** leak into the candidate hand-off.
      **Handed forward: `LITE` (CONFIRMED-EARLY, BET §B) · Energy refining complex and the defense EW
      (CONFIRMED-EARLY, ROTATION cross-evidence).**
- [x] ENDED-thread book flags emitted (**none**), plus one adverse-direction flag on `ETN`/`ANET`.
- [x] Missed ledger updated (2 rows, both `prospective`).

---

## 11 · APPEND-ONLY CORRECTIONS from the DEEP stage (same run)

*(Cards 1–8 are left exactly as written. §4c forbids editing them away.)*

### 11a · 🚨 Card 4's driver attribution is REFUTED by dating, and its own KPI cannot separate its hypotheses

Card 4 read `NUE`'s accumulation against the Canada-tariff thread and asked whether *"the steel bid is
the tariff."* **DEEP-MATR dated the move: `NUE`'s entire +10.7 RS20 vs `SPY` was earned 07-22 → 07-28,
around its 2026-07-27 print (+6.94% EPS surprise) — twelve sessions BEFORE the tariff thread began on
08-13.** ⇒ **The tariff was never the driver, in either direction.** Card 4's framing ("either the pause
is not believed, or the steel bid is not the tariff") is resolved on the second horn, and it was
resolvable from the calendar alone.
⚠ Worse for the card's construction: **its KPI is already satisfied** — `NUE` 10-day excess vs `SPY`
reads **−3.09**, which the card set as the IF-branch condition (**≤ 0 at 08-31**) ⇒ **the KPI fires
regardless of which hypothesis is true and therefore separates nothing.** Recorded as a card-level
construction defect; **the card is not rewritten**, and the 08-31 date stands so the failure is visible
when it settles.

### 11b · Card 8's `RTX` tag is struck; the card's evidence survives without it

`RTX` is **🟡, not 🟢** — its green came from `velocity 1.55` on a `vol_surge` of **0.83** (the axis G1
revoked; full audit in `SWEEP_READ` §correction). Card 8's substance is unaffected: the defense group
still reads **9 of 10 accumulating and 8 of 10 positive RS20 vs `SPY`** (DEEP-INDU's wider A&D set),
and `M719` **strengthened to +5.11pp** (from +4.32) for the defense EW vs `XLI` with `LHX` removed.
⚠ But **"6 of 6 accumulating" was 5 of 6** — the failure is `RTX` itself, whose OBV reads
**매집 +0.368 in the sweep** and **분배 −25% in `module_chart --read`**.

### 11c · An open contradiction between two DEEP files, carried rather than resolved

**DEEP-INDU and Lens 3** report the sweep's `obv_state` and `module_chart --read`'s 20-day OBV slope
**disagreeing in sign on 5–6 of 22 names** (`ANET`, `NUE`, `RTX`, `PYPL`, `CRWD`). **DEEP-MATR
reconstructed OBV from settled bars and agrees with the sweep on 12 of 12 Materials names**, calling
the `NUE` flip a **clock artifact** (`module_chart` pulls its own live data; this run's readings were
taken after the 22:30 KST bell). **Both measurements stand and they are not yet reconciled** — the
likely resolution is that the conflict is a *timestamp* difference rather than a *method* difference,
but that has not been measured. ⇒ **Standing constraint until it is: no name-level claim may rest on
OBV alone (rule D6), and any OBV citation must name which instrument produced it and at what clock.**

### 11d · Card 7 (`LITE`) — the "clean rise" label is half-wrong

`US_LIVE_SHORTLIST` labels `LITE` **`✅저숏/숏커버 (청정 상승)`** on a FINRA short-**volume** z of −1.07,
while `module_flow --positioning` reads **12.2% of float short, DTC 2.0, 🔥크라우디드**. **Both are
true and they measure different objects** — a large short *stock* being *covered*. **`LITE` may be
moving on a squeeze rather than on accumulation**, which changes what `S96` (08-21) is testing.
Dig **`D289`**. ⚠ `LITE` is also **the real book's #2 position (12.01% of invested)** — see the
`PREFLIGHT_US.md` G5 correction.
