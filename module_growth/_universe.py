"""유니버스 로더 — data/us_universe·kr_universe CSV 를 읽어 (ticker, name, sector, mktcap).

기존 스냅샷 CSV(P5: 읽기전용 참조)를 그대로 쓴다. 시장별 파일 미러 복제 없이 --market 로 분기(P3).
"""
from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

_REPO = Path(__file__).resolve().parent.parent


def _data_dir() -> Path:
    return Path(os.environ.get("DEGAJA_DATA_DIR", str(_REPO / "data")))


@dataclass
class UniverseRow:
    ticker: str
    name: str
    sector: str
    market_cap: Optional[float]  # USD(us) / KRW(kr)
    market: str                  # 'us' | 'kr'


def load_universe(
    market: str,
    *,
    limit: Optional[int] = None,
    sector: Optional[str] = None,
    min_market_cap: Optional[float] = None,
) -> list[UniverseRow]:
    market = market.lower()
    if market == "us":
        # US 는 gics_sector(대분류)·gics_industry(세부) 둘 다 — "Semiconductors"는 industry 쪽
        path, tcol, ncol, scols, mcol = (
            _data_dir() / "us_universe" / "us_top300.csv",
            "ticker", "name", ("gics_sector", "gics_industry"), "market_cap_usd",
        )
    elif market == "kr":
        path, tcol, ncol, scols, mcol = (
            _data_dir() / "kr_universe" / "kr_all.csv",
            "ticker", "name", ("sector",), "market_cap_krw",
        )
    else:
        raise ValueError(f"unknown market: {market!r} (us|kr)")

    if not path.exists():
        raise FileNotFoundError(f"유니버스 파일 없음: {path}")

    rows: list[UniverseRow] = []
    with path.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            mc: Optional[float]
            try:
                mc = float(r.get(mcol) or 0) or None
            except ValueError:
                mc = None
            if min_market_cap is not None and (mc is None or mc < min_market_cap):
                continue
            sec_parts = [(r.get(c) or "").strip() for c in scols]
            sec = " · ".join(p for p in sec_parts if p)
            if sector and sector.lower() not in sec.lower():
                continue
            rows.append(UniverseRow(
                ticker=(r.get(tcol) or "").strip(),
                name=(r.get(ncol) or "").strip(),
                sector=sec,
                market_cap=mc,
                market=market,
            ))
    # 이미 시총 내림차순(rank) 이지만 명시적으로 정렬 유지
    if limit is not None:
        rows = rows[:limit]
    return rows
