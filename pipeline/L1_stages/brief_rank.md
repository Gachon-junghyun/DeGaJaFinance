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

★ **Fill the spine from the domestic pool, and let each foreign item earn its slot by being one a
Korean outlet already printed for Korean readers** (trigger **W6**). Measured 2026-07-24:
**8 of 15 published items were domestic-origin**, and the other **7 were foreign-origin — all 7 of
which had already been printed by Korean outlets (7/7 passed the test)**. Those seven were the
tariff decision, oil through $100, the US close, an earnings surprise, a chip roadmap, a Treasury
currency report and the Middle East campaign.

★ **The most useful thing that count revealed**: nearly every foreign fact a KR reader needed
**arrived through the domestic pass, not the foreign one.** Korean outlets had already carried them
pre-open. The separate foreign event pass contributed only **5 candidate rows out of 810 (0.6%)**,
and of those only two added anything the domestic pass had not already delivered. **The domestic
pool is not a narrower window on the world — for this reader it is a better-curated one.**

**Why the rule is a fill order rather than a quota**: the overnight foreign pool is **bigger every
day** (2026-07-24: 810 foreign market events vs 357 domestic), so any ranking that starts from
"biggest events first" produces a foreign brief on a domestic desk **without anyone choosing that** —
measured on this run's own first draft, which the user corrected with
*"너무 외국 중심이야 한국 풀에서 놀아야 해."* Set the spine first and the arithmetic stops deciding.
**A run with a higher foreign share is publishable — it just carries a line in the cut list naming
what made that morning genuinely foreign-driven**, so the frame stays a choice rather than a default.

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

⚠ **15 is a ceiling AND a target — under-filling it is over-cutting, and it has a measured cost.**
Measured 2026-07-25: the run published **12** and treated the gap as fine, but the three empty slots
were exactly where the recovered single-outlet material belonged — 「HMM 8조 투자증액」, 「조선3사
1,500억달러 조선동맹」, 「삼성전자 3Q 반도체 가격 中 보이콧」, all tier-2 domestic structural, all cut
by stopping short. **If fewer than 15 survive, each empty slot is defended in the cut list by name**
(what tier-2 domestic item was considered and why it lost), not left as a silent shortfall. "Nothing
else cleared the bar" is a claim that has to be shown against the recovered pool, not assumed.

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

★ **Every class above is filled domestic-first (W6).** The three fixed "reference point" slots are
where this bites hardest and where it is easiest to get right: **the KR index close, the won, and oil
in won-relevant terms** are the reader's baseline — measured 2026-07-24, the FX item was only readable
because it paired the **prior domestic close (1,466.8원)** with the **pre-open level (1,470원대)** and
named the domestic mechanism behind the move (an ADR proceeds conversion), none of which exists in the
foreign pool at all.

**The cut list is published**, as a count plus reason classes — the reader must know the brief is a
selection, not the day. Silent truncation would make fifteen items look like fifteen events happened.
★ **Publish the domestic/foreign split with it**, as two numbers: how many of the fifteen are domestic,
and how many foreign rows passed the domestic-print test out of how many existed. Measured 2026-07-24:
**8 of 15 domestic-origin · 7 foreign-origin, all 7 domestic-printed · foreign event pass contributed 5 candidate rows of 810 (0.6%)**. That line is what lets the next run see
the frame at a glance instead of re-deriving it.

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
      **If fewer than 15, each empty slot is named in the cut list** with the tier-2 domestic candidate
      it beat — a bare "12 items" is an over-cut, not a light day (measured 2026-07-25).
- [ ] Items ordered by the 5-tier consequence rule; each carries a one-clause "why now".
- [ ] Cut list written **with counts and reason classes** — no silent truncation.
- [ ] No item appears twice under different wording; merged items share a mechanism, not a keyword.
- [ ] Domestic dated/structural items were ranked against foreign ones, not appended after them.
- [ ] **Spine is domestic (W6) and the split is published**: N of 15 domestic, and M of the available
      foreign rows admitted on the domestic-print test. Measured reference 2026-07-24: **8/15 domestic-origin · 7/7 foreign-origin
      domestic-printed**. A lower domestic share is publishable — it just carries its own line
      in the cut list explaining what made that morning genuinely foreign-driven.
- [ ] Bias check stated: no item is present because the book is positioned in it.
