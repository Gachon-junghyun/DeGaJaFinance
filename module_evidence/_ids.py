# -*- coding: utf-8 -*-
"""ID 브로커 — `M1039`–`M1051` 을 발급한다. 손으로 치던 3-grep 의 대체물.

현행 규약은 WRITE 시점에 사람이 *"ID 3-grep: `M1026`–`M1038` 0 hits"* 를 손으로 돌리는 것이다.
그게 실패하면 같은 번호가 두 뜻을 갖는다(`D76` 충돌 클래스). 여기선 산수로 막는다.

⚠️ **기본은 라이브 스캔이다** — DB 를 믿지 않는다. 색인을 마지막으로 만든 뒤 다른 런이
`llm_outputs/` 에 번호를 적었을 수 있고, 그 한 번이 충돌이다. `--fast` 는 DB 를 읽지만
그때는 「색인 시각 이후는 못 본다」를 출력에 박는다.
"""
from __future__ import annotations

from pathlib import Path

from ._config import (EVIDENCE_DB, FAMILIES, HANDOFF_DIR, REPORT_DIR, RUNS_DIR, iter_md)
from ._harvest import harvest_refs_and_ids


def scan_occupancy() -> dict[str, list[dict]]:
    """리포 전체 md 라이브 스캔 → family -> [{num, cid, file, line}]."""
    out: dict[str, list[dict]] = {f: [] for f in FAMILIES}
    for root in (HANDOFF_DIR, REPORT_DIR, RUNS_DIR):
        for p in iter_md(root):
            _, ids = harvest_refs_and_ids(p)
            for i in ids:
                out.setdefault(i["family"], []).append(i)
    return out


def _max_from_db(family: str, db: Path) -> tuple[int, str]:
    from ._store import connect
    con = connect(db)
    row = con.execute("SELECT max(num), (SELECT v FROM meta WHERE k='built_at') "
                      "FROM occupancy WHERE family = ?", (family,)).fetchone()
    con.close()
    return (row[0] or 0), (row[1] or "")


def next_id(family: str, count: int = 1, market: str = "", fast: bool = False,
            db: Path = EVIDENCE_DB) -> dict:
    """다음 ID 를 count 개 발급. 발급만 하고 **파일에 쓰지는 않는다** — 쓰는 건 사람/스테이지."""
    fam = family.strip().upper()[:1]
    if fam not in FAMILIES:
        raise ValueError(f"모르는 계열 {family!r} — {'/'.join(FAMILIES)}")
    if fast:
        top, built = _max_from_db(fam, db)
        src = f"DB(색인 {built or '없음'}) — 그 이후 추가된 번호는 못 본다"
        holder = ""
    else:
        occ = scan_occupancy().get(fam, [])
        top = max((i["num"] for i in occ), default=0)
        holder = next((f"{i['file']}:{i['line']}" for i in occ if i["num"] == top), "")
        src = "라이브 스캔(handoff + REPORT + llm_outputs)"
    suffix = f"-{market.upper()}" if market else ""
    ids = [f"{fam}{n}{suffix}" for n in range(top + 1, top + 1 + max(1, count))]
    return {"family": fam, "meaning": FAMILIES[fam], "highest": f"{fam}{top}" if top else "(없음)",
            "highest_at": holder, "ids": ids, "scanned": src}
