# L1 · BRIEF_RANK — order by consequence, cap at ~15, count what was cut (stage)

> Stage 2 of `morning_brief`. Turn the gathered pool into an ordered short list. Calls L3.
> Output: `BRIEF_RANK.md` (ordered rows + the cut list with its count).

## The ordering rule
A morning brief is read once, on a phone, before the open. Order by **when the reader has to care**,
not by how interesting the desk finds it.

1. **Resolves today or tomorrow** — a dated binary the reader will see land within 48h (a tariff
   announcement, a decision, a print). These go first even if the number is small.
2. **Moved overnight** — what the US session did and why, plus oil / FX, because that is what the KR
   open reacts to.
3. **Confirmed yesterday, still standing** — prints and filings from the prior session whose effect
   has not been consumed yet.
4. **Slow but dated** — this week's calendar, ARMED items with a specific date.
5. **Standing conditions** — a stress or trend still in place with no new print. One line, not more,
   and only if it changed enough to matter.

⚠ **Domestic structural events outrank foreign earnings.** Measured 2026-07-23: the first draft's
  calendar line carried three US macro dates and omitted both 07-29 domestic items (an ADR conversion
  opening on a name the desk had suspended its own flow read for, and a financial-holdco governance
  package). For a KR reader those two are the ones with a mechanism, not the US earnings.

⚠ **The 5-tier order has a known blind spot: undated domestic policy.** Because tier 1 rewards "a
  date attached", a domestic event with real transmission but no resolution date falls to tier 5 and
  gets cut. Measured 2026-07-23 by a random 10% audit of the day's 246 market events against the
  17-item draft: **6 of 25 covered (24%)** — most of the misses were correctly dropped (broker notes,
  regional items, a contributed column), but **three should have been in**: the presidential
  real-estate policy roundtable [20 articles/6 outlets, the day's #2 domestic event, with 보유세·
  양도세 on the table], Samsung's foldable launch [9/6], and POSCO's collapsed wage talks going to
  arbitration [4/3]. None had a resolution date; all three move banks, construction, handsets, steel.
  **Give undated domestic policy/corporate events their own slot at tier 2**, judged by transmission
  breadth rather than by whether a date happens to be attached.

⚠ **Bucket by occurrence, not by topic.** The gather stage hands over 간밤 발생 / 누적·진행 중 /
  오늘 예정. Rank inside each bucket and keep them visibly separate in the output — a reader must
  never have to guess whether item 9 already happened. Measured: mixing a 4-day-old escalation into
  the overnight block made a continuing war read as a fresh shock.

## The cap: **15 news items, hard.** Calendar sections are separate and not counted.
Fifteen is a reading budget, not a coverage claim. A day holds ~539 knowable events; the brief keeps
the fifteen a reader must not miss and **publishes the number it dropped**.

**Merge before you cut.** Most of the pressure on the cap is fake — it comes from one event written
as three items. Merge anything sharing a *mechanism*; never merge on a shared keyword.
Measured 2026-07-23: a 29-item news list collapsed to 15 with nothing lost —
- tariff announcement + the June 12.5% proposal + the 15% cap + LG's $28bn delay = **one** item
  (they are one policy with a history, and the history is what makes the announcement readable);
- Iran fighting + Trump's bridge/power-plant threat + Red Sea tanker diversions = **one**;
- Alphabet capex + revenue + first-ever negative FCF + the 5% drop = **one** (one earnings release).

**Slot discipline** — decide by consequence class, not by how interesting the item reads:
| Class | Slots | Rule |
|---|---|---|
| Resolves ≤48h | 1–2 | Automatic. A dated binary always outranks a bigger undated story |
| The open's reference points | 3 | Index close · FX · oil. Fixed cost; the reader needs the baseline |
| New structural facts | 4–6 | Ratings actions · policy approvals · capacity · price setting — things that change a forward number |
| Value-chain single names | 2–4 | Only where the read-through is nameable (a foundry price rise, a panel maker's loss). Not "a company did a thing" |
| Continuing conditions | 1–2 | Geopolitics, credit stress. One line each, only if the state changed |
| PR · awards · MOUs · regional · broker notes | **0** | Never. Measured: these were ~46% of a day's domestic events |

**The cut list is published**, as a count plus reason classes — the reader must know the brief is a
selection, not the day. Silent truncation would make fifteen items look like fifteen events happened.

## L3 called
- [public_source](../L3_functions/public_source.md) — run the **DROP test early**, at ranking, not at
  render: an item with no reader-checkable origin cannot be ranked into a slot it will later vacate.

## What this stage does
- Apply the order above; assign each surviving item its rank and its "why now" in one clause.
- Drop, and count: `origin: none` · `not knowable at 08:30` · `duplicate of #n` · `position language`.
- **Bias check before freezing the order**: if the desk holds or wants a position in a name, that
  name's item must earn its rank on the same test as everything else. A brief is not a pitch. If an
  item survives only because we are long it, cut it and count it.

## ✅ EXIT CHECK
- [ ] **News items = 15, after merging by mechanism.** Calendar sections are separate. If 15 feels
      tight, check for unmerged duplicates before cutting anything real — that is where the room is.
- [ ] Items ordered by the 5-tier consequence rule; each carries a one-clause "why now".
- [ ] Cut list written **with counts and reason classes** — no silent truncation.
- [ ] No item appears twice under different wording; merged items share a mechanism, not a keyword.
- [ ] Domestic dated/structural items were ranked against foreign ones, not appended after them.
- [ ] Bias check stated: no item is present because the book is positioned in it.
