"""대상 종목과 동종 peer들의 멀티플을 한 표로 묶는다."""
from __future__ import annotations

import time
from typing import List, Optional

import pandas as pd

from ._naver_fetch import NaverSnapshot, fetch_naver_snapshot

_COLS = [
    ("code", "코드"),
    ("name", "종목명"),
    ("price", "현재가"),
    ("market_cap_eok", "시총(억)"),
    ("per_ttm", "PER(TTM)"),
    ("per_fwd", "PER(Fwd)"),
    ("pbr", "PBR"),
    ("eps_fwd", "추정EPS"),
    ("target_price", "목표주가"),
    ("upside_pct", "상승여력%"),
    ("foreign_pct", "외인%"),
    ("div_yield", "배당%"),
    ("industry_per", "업종PER"),
]


def _row(snap: NaverSnapshot) -> dict:
    return {
        "code": snap.code,
        "name": snap.name,
        "price": snap.price,
        "market_cap_eok": snap.market_cap_eok,
        "per_ttm": snap.per_ttm,
        "per_fwd": snap.per_fwd,
        "pbr": snap.pbr,
        "eps_fwd": snap.eps_fwd,
        "target_price": snap.target_price,
        "upside_pct": snap.upside_pct(),
        "foreign_pct": snap.foreign_pct,
        "div_yield": snap.div_yield,
        "industry_per": snap.industry_per,
    }


def build_peer_table(
    target: str,
    peers: List[str],
    sleep: float = 0.4,
) -> pd.DataFrame:
    """target 1개 + peers N개를 동시 비교. 첫 행이 target."""
    rows = []
    for code in [target, *peers]:
        try:
            snap = fetch_naver_snapshot(code)
        except Exception as e:  # 네트워크 실패한 종목만 빼고 계속
            rows.append({"code": str(code).zfill(6), "name": f"<err: {e}>"})
            continue
        rows.append(_row(snap))
        time.sleep(sleep)  # 네이버 부담 줄이기
    df = pd.DataFrame(rows)
    return df.rename(columns={k: v for k, v in _COLS})


def add_peer_avg(df: pd.DataFrame) -> pd.DataFrame:
    """target 행 빼고 peer 평균/중앙값을 마지막 두 행에 추가."""
    if len(df) <= 1:
        return df
    peers = df.iloc[1:]
    numeric_cols = peers.select_dtypes(include="number").columns
    avg = {c: peers[c].mean() for c in numeric_cols}
    med = {c: peers[c].median() for c in numeric_cols}
    avg.update({"코드": "—", "종목명": "Peer 평균"})
    med.update({"코드": "—", "종목명": "Peer 중앙값"})
    return pd.concat([df, pd.DataFrame([avg, med])], ignore_index=True)


def render_markdown(df: pd.DataFrame, target_code: Optional[str] = None) -> str:
    """리포트에 그대로 붙여 넣을 수 있는 markdown 표."""
    fmt = df.copy()
    for col in fmt.columns:
        if fmt[col].dtype.kind in "fi":
            if "%" in col or "PER" in col or "PBR" in col:
                fmt[col] = fmt[col].map(lambda v: f"{v:,.2f}" if pd.notna(v) else "—")
            else:
                fmt[col] = fmt[col].map(lambda v: f"{v:,.0f}" if pd.notna(v) else "—")
    return fmt.to_markdown(index=False)
