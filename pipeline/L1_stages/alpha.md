# L1 · ALPHA — is it still bettable now? freshness, tickets, book flags (stage)

> Big stage, last analytical stage. Separates «interesting» from «bettable now»: the pipeline reads lagging data,
> so by thesis time the catalyst may already have fired.
> **Reads**: `BET_SHEET.md §B`, theme age, the catalyst's primary source (release, 8-K, 공시), positioning for
> finalists. **Output**: `BET_SHEET §B` tags (🟢LIVE / 🟡PARTIAL / 🔴RESOLVED) + (US) `ACTION_TICKETS.md` — **cap 6 KB
> of additions**. **Next**: HANDOVER close-out carries every tag; paper_desk/미러링 read the tags.

## L2 called
- [schedule](../L2_modules/schedule.md) — `theme_age` first (token-0): 🟢FRESH / 🟡ACCELERATING / ⚪ECHO / 🔴FADING.
- [web_errand](../L2_modules/web_errand.md) — has the catalyst fired? read the release/공시 itself.
- [lens](../L2_modules/lens.md) — every ticket is a registered question.

## What this stage does
- **Check the pipe before reading a zero.** `theme_age` stands on the news index, which was measured failing
  silently (tunnel drops; a dead pipe and a quiet theme return the same value; the KR sweep once queried the
  foreign pool). Run `python -X utf8 -m module_news_data fts search 삼성전자 --days 7 --count` — a known-loud name
  must come back loud. If preflight G1 failed or the probe is quiet, issue **no** freshness verdict and say so.
  (🟢LIVE fired 0 times in 8 runs, later 18 KR runs, while nobody checked the counter.)
- **Per bet**: has the catalyst fired (primary source, not a WebSearch summary)? has the move been made (price vs
  the dated catalyst)? is the thesis already consensus (estimate trend from EARNINGS)?
  Tag 🟢LIVE / 🟡PARTIAL (state the residual) / 🔴RESOLVED.
- 🔴 is dropped from the bettable list **as a ledger row** — `reject_ledger.py add … --revives-if … --recheck-date …`
  (measured: 475150's kill condition reversed three runs later while a prose ban stayed on).
- 🟡 is a dated appointment: give a re-check date and hand it to HANDOVER close-out (475150 was 🟡 «돌파 後» and broke
  out unattended). A name carried into ALPHA that gets no tag is a `missed_ledger` row with `--enters-if`.
- **Tags follow the name, not the sector's slot**; list every tagged name for carry-forward.
- **Momentum-only flag**: price/volume green but earnings direction flat or down = tape trade → stamp «hard-stop
  required». Grade any accumulation read first (D6 table in indicators): KIS investor actuals B (confirmation) · **OBV alone C**
  (r≈0.49 vs real flow, t=1.00); a C-grade disagreement downgrades to 🟡 and is reported, it does not convert a bet.
- **Positioning is read last and as context** (US `module_flow <TKR> --positioning` implied move for finalists;
  KR futures basis/OI — no KR implied move exists, never fabricate a KR threshold from basis). US ⚡crowded-short is
  turn-conditional fuel, never a standalone buy. KR investor actuals may lower conviction one notch with the
  reason written; they do not demote a name alone.
- **Book flags**: any open position whose thesis rides a thread that ENDED, or a guide that was cut, is flagged to
  paper_desk/미러링 in the last section.
- **(US) `ACTION_TICKETS.md`** via `action_bracket`: PREMORTEM's both-sides brackets + any cycle-GAP core-starter,
  DRY-RUN share counts (a human executes separately). **An earnings or macro event ticket carries at least one
  earnings/macro observable** (guide vs threshold, GM guide, `fred:` series) beside any price observable — measured:
  22 of 22 recent tickets were scored on price only, 0 on an earnings figure. Register each ticket in the lens
  ledger (`ask → ev → think --weights`) with its frozen threshold; `action_bracket` failing (KIS) ⇒ write the
  placeholder line and still register the questions.

## ✅ EXIT CHECK
- [ ] Pipe probe run before any freshness verdict; G1-fail ⇒ no freshness verdict issued.
- [ ] Every §B tag has evidence label + date; catalyst status read from a primary source.
- [ ] 🔴 logged as `reject_ledger` rows with condition + recheck date; 🟡 have re-check dates; untagged carried
      names are `missed_ledger` rows; tagged names listed for carry-forward regardless of sector slot.
- [ ] Momentum-only and positioning notes graded (D6) and stamped where they apply.
- [ ] (US) ACTION_TICKETS written; earnings/macro events carry a non-price observable; each ticket has a lens Q ID.
- [ ] Book flags emitted.
