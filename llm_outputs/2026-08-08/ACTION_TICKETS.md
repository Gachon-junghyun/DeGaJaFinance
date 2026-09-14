# ACTION_BRACKET — 2026-08-08  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,025,332원 · fx 1419 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** July CPI (D-4, axis=inflation) — both-sides armed below.

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF July CPI (D-4) prints toward cool
- **size:** 10 sh @ ~$223.96 (≈$2,239.6 notional, risk $158.85 = 1.5% )
- **stop:** $208.28 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF July CPI (D-4) prints toward hot
- **size:** 4 sh @ ~$298.2 (≈$1,192.8 notional, risk $84.72 = 0.8% )
- **stop:** $277.33 (−7.0%) · exch NYSE

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

## §0 · ALPHA-stage commentary — read this BEFORE the tickets above (industry_US, 2026-08-08)

**✅ D155/D188 did NOT reproduce.** The script's silent-false-negative on runs crossing local midnight
did not fire: it correctly identified **July CPI at D-4** and armed a genuine both-sides conditional.
**Recorded as a null result on a known defect, not as a fix.**

🚨 **D204's SECOND half DID reproduce, and it is the material one.** The soft/strong → asset mapping is
**hard-coded to a CUT-cycle Fed** — `cool ⇒ NVDA`, `hot ⇒ an energy name` — while **this Fed is
debating a HIKE**: September hike odds moved **55% → 44%** on the 08-07 payroll print and the
**December hike probability HELD at 77%** `[economictimes bodies 08-07/08-08]`. ⇒ **the reaction
function the mapping assumes may be inverted**, and **the ticket pair above is therefore carried as a
SCHEDULING artifact, not as an expression of this desk's view.**

⚠ **A second, independent reason not to read the pair as the desk's view**: this run's PREMORTEM Lens 2
established that the **against-us branch of a COOL CPI hits FOUR tilts at once — INDU, FIN, MATR and
UTIL** — because they share one exposure (the rate-expectations path) under four GICS labels. **The
script brackets one asset per side; the measured correlated exposure is four-wide.** That is what
**`S72`** was registered today to test, and **`S71`** to test the CPI→PPI reversal the pair cannot see.

⚠ **On the `hot` leg's chosen name**: the script selected **MPC**, which is independently the strongest
revision-breadth name on this run's sheet (**FY 30d 13↑/0↓, FY EPS +84.3%/90d**). **That agreement is a
coincidence of a hard-coded mapping, not a derivation** — stated so the ticket is not read as
corroboration of the DEEP's finding.

**Nothing in this file is an order. `TIMEFOLIO_EXECUTE=1` is set for a 6th consecutive run and this run
touched nothing executable (P4).**
