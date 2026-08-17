# L1 · BET — bet sheet (stage)

> Phase 3. Turn the DEEP sectors' candidates into numbers + business + flow, one file.
> Calls L2. Output: `BET_SHEET.md` — **a single file with per-sector sections** (§A–§E each);
> downstream desks read this exact filename, so never split it.

## L2 called
- [deepdive](../L2_modules/deepdive.md) — `module_valuation --peers` (KR) ·
  `module_fundamentals_us --json` (US XBRL numbers; ⚠ `--json` avoids KR scaffolding) ·
  `us_setup_screener --sector` (US wide-net setups) · `module_math_check` (verify arithmetic).
- [indicators](../L2_modules/indicators.md) — `module_flow --bench SPY|^KS11` per candidate
  (KR adds ⑦ per-investor actuals + ⑧ short balance; US adds `--positioning` for finalists only).

## What this stage does
- **Candidate set per DEEP sector = wide net, not the 3 names you already knew:**
  (deep-agent thesis leaders) ∪ (sector screener setups) ∪ (★LIVE_SHORTLIST names — this last
  one drags in cross-sector LIVE candidates beyond the DEEP sectors; they get their own section).
- Per candidate: §A numbers table (multiples, growth, margins — cross-check XBRL↔yfinance;
  state blanks as blanks) · §B narrative/thesis + freshness placeholder (ALPHA fills) ·
  §C flow/positioning cross-read · §D competition/peers · §E refutation + dated catalyst.
- Include the pre-mortem's **epicenter-starter module** if a cycle GAP was flagged: a partial core
  in the #1 cycle's epicenter exists on the sheet regardless of tape, tape gates only the remainder.
- Sizing language is *influence illustration* only — zero buy/sell recommendation.
- **Every name you set aside becomes a scored record** — L3 [reject_ledger](../L3_functions/reject_ledger.md).
  Write it with its **reason class**, its **`--revives-if` condition**, and its **`--recheck-date`** —
  **`add` will not run without both** (script-enforced since 2026-07-23, no bypass):
  ```bash
  python -X utf8 scripts/reject_ledger.py add --date <run date> --ticker <6자리> --name <종목> \
      --cls <클래스> --why "<한 줄 근거>" --stage BET \
      --revives-if "<부활 조건>" --recheck-date <YYYY-MM-DD>
  ```
  Measured 2026-07-23 (24 rejections): **67% changed nothing**, and the loss tail ran **2.2× the gain
  tail** (+83.8pp vs −38.4pp). Almost all of that loss tail (**+41.2pp + 26.9pp on one name**) traces
  to two rejections filed **without** a revival condition, never re-opened until a user forced a
  manual audit. **Do not file a rejection you cannot attach both fields to** — if you cannot state
  what would reverse it and by when, the rejection is not ready to be written yet; narrow the reason
  until it is. HANDOVER now runs `reject_ledger.py due` every run (`carryover.md` §3b) — a condition
  you set here **will** be re-examined without you having to remember it.
- **★ And the names you never got as far as rejecting — L3 [missed_ledger](../L3_functions/missed_ledger.md).**
  A name that surfaced in SWEEP/EVENT_ALPHA and simply **did not make this sheet** leaves no trace at
  all unless you write one. That gap (F2) is why "we were disciplined" and "we never saw it" produced
  identical evidence for months.
  ```bash
  python -X utf8 scripts/missed_ledger.py add --date <run date> --ticker <6자리> --name <종목> \
      --cls <클래스> --why "<한 줄 근거>" --stage BET \
      --enters-if "<진입 조건>" --recheck-date <YYYY-MM-DD>
  ```
  ⚠ **Do not file here what belongs in `reject_ledger`** — if you stated a reason and set it aside,
  that is a *rejection*. `missed_ledger add` refuses any ticker×date already in the rejection ledger
  (exit 1), so the boundary is machine-enforced, not a judgment call.
  ⚠ Sign is inverted vs the rejection ledger: `excess > 0` here means **missing it cost us**.
  ⚠ The `P.현금부족` class exists for names blocked by the exposure rule rather than by their own
  merits — file those there, so the cost lands on the **beta** decision where it belongs
  (L3 [exposure_state](../L3_functions/exposure_state.md)), not on stock selection.
- **When the flow gate still passes and only the story broke, RE-FILE the name — don't remove it.**
  A thread going FADING/ENDED, a catalyst going quiet, or a *secondary* thesis being refuted
  (e.g. "the squeeze premise died") is a reason to **restate the thesis and lower conviction**, not to
  delete a name whose money is still measurably arriving. Give it a new thesis line and a dated
  re-check. ★ Measured origin: 475150 was set aside twice on narrative grounds (07-16 "theme faded",
  07-20 "squeeze thesis refuted") while its foreign+institution net-buy never stopped — the two
  rejections cost **+41.2pp** and **+26.9pp**. Removal is for names the **measured** axes reject.

## ✅ EXIT CHECK
- [ ] Every DEEP sector has a section; cross-sector LIVE shortlist names included or explicitly dropped with reason.
- [ ] Numbers cross-checked (math_check on any derived figure); blanks are blanks, not guesses.
- [ ] Flow/positioning cross-read present per candidate; BET_SHEET.md written as ONE file.
- [ ] **Every set-aside name is in the ledger with a class AND a `--revives-if` condition**
      (`reject_ledger.py add`), and any name whose stored condition has come true is back in §A/§B.
      A rejection with an empty revival condition is a permanent ban — allowed, but say why.
- [ ] **No name was removed on narrative grounds alone while its measured flow still passed** — such
      names appear re-filed under a new thesis with a dated re-check, not absent.
- [ ] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** with a
      class AND an `--enters-if` condition. A sheet that produces zero rejections *and* zero missed
      entries from a multi-name sweep has not scored its own funnel — say why, or file the rows.
- [ ] **Sizing language is consistent with the exposure state carried by HANDOVER** (§3d). If the
      state is `복귀` the sheet must actually supply enough candidates to reach the target, or state
      plainly that it cannot — an unfillable target is how cash silently stays where it was.
- [ ] **Linter run on this stage's own output** — `python -X utf8 scripts/report_lint.py <written file>`. Every finding is fixed or the paragraph carries its rule ID with a stated reason for exemption. ⚠ It checks form only (C1 benchmark · C2 both halves · S6 future label · D6 OBV-alone); a clean run is not a correct report.
