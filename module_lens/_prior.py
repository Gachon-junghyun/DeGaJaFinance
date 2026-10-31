# -*- coding: utf-8 -*-
"""파급력 사전값 — `impact` 표를 실험 산출물에서 채운다 (권장 비중 = 파급력 × 신뢰도 의 앞쪽).

출처 두 갈래 (lab/NEWS3D_20261030.md E2):
  · 뉴스 단어 (kind='news', key=단어) — 장 전 기사 단어의 그날 |초과수익|÷평소 변동성 배수.
    🔴 200번 이상 나온 단어만 — 반으로 갈라 본 순위상관이 그 아래로 내려가면 0.15~0.29 라 못 믿는다.
    🔴 가격 묘사어는 뺀다 — «이미 움직인 것»을 보도하는 말이라 원인이 아니다(E1c 순환).
  · 거시 데이터 변화 (kind='macro') — 2000~2026 FRED 사건일의 S&P500 그날 |수익| 배수. 숫자는 E2 표 그대로.
값은 실험을 다시 돌리면 바뀐다 — 그때 `load` 를 다시 부른다(파생 표라 덮어써도 잃는 게 없다).
"""
from __future__ import annotations

import json
import sqlite3

from ._config import OUT_DIR

WORDIMPACT = OUT_DIR / "news3d" / "wordimpact_20261031.json"
MIN_N = 200
# 가격을 묘사하는 말 — 원인이 아니라 결과를 보도한다. 실측 상위에 올라온 것 + 같은 부류.
PRICE_WORDS = {
    "애프터마켓서", "급등", "급락", "특징주", "상승", "하락", "질주", "상한가", "하한가", "강세", "약세", "속보",
    "PREMARKET", "PRE", "MOVERS", "SOARS", "LIFTS", "LIFT", "TUMBLES", "SLIDING", "DIVE", "BELL", "JUMPS", "FALLS",
    "SURGES", "PLUNGES", "RISES", "DROPS", "GAINS", "STOCK", "SHARES",
}
# 거시: E2 «시장 층 — 데이터 변화» 표 (S&P500 그날 |수익| 배수, 사건 수)
MACRO = [
    ("dgs10_move_10bp", 1.98, 561), ("dgs10_move_15bp", 3.02, 129),
    ("wti_move_5pct", 2.08, 352), ("usd_broad_move_0_7pct", 2.21, 252),
]


def rows() -> list[tuple]:
    out = []
    if WORDIMPACT.exists():
        r = json.loads(WORDIMPACT.read_text(encoding="utf-8"))
        for mk, m in r.get("markets", {}).items():
            for w, v in m["stock"]["rows"].items():
                if v["n"] >= MIN_N and w not in PRICE_WORDS:
                    out.append(("news", w, round(v["day0"], 3), int(v["n"]), f"E2 {mk} stock-layer day0"))
    out += [("macro", k, m, n, "E2 FRED 2000-2026 S&P day0") for k, m, n in MACRO]
    return out


def load(con: sqlite3.Connection) -> dict:
    con.execute("CREATE TABLE IF NOT EXISTS impact (kind TEXT, key TEXT, mult REAL, n INTEGER, src TEXT, "
                "PRIMARY KEY(kind, key))")
    rs = rows()
    # 같은 단어가 두 시장에 다 있으면 표본이 큰 쪽
    best: dict[tuple, tuple] = {}
    for r in rs:
        k = (r[0], r[1])
        if k not in best or r[3] > best[k][3]:
            best[k] = r
    # 이 로더가 넣은 줄(src 가 «E2 …»)은 통째로 바꾼다 — 새 원자료에서 빠진 단어가 남아 advise 에 쓰이지 않게
    con.execute("DELETE FROM impact WHERE src LIKE 'E2 %'")
    con.executemany("INSERT OR REPLACE INTO impact VALUES(?,?,?,?,?)", list(best.values()))
    con.commit()
    return {"rows": len(best), "news": sum(k[0] == "news" for k in best), "macro": sum(k[0] == "macro" for k in best)}
