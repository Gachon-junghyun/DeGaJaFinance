# FILE: research_Mvp/module_kis/_investor.py
"""국내주식 투자자별 매매동향(개인/외국인/기관 순매수).

엔드포인트: GET /uapi/domestic-stock/v1/quotations/inquire-investor
tr_id:      FHKST01010900 (실전/모의 동일)

수급 주체(외국인·기관)의 순매수 방향은 공격적 트레이딩의 핵심 신호 —
현재 프로젝트엔 깨끗한 수급 채널이 없어 KIS로 보강한다.
응답은 최근 약 30영업일 일별 순매수(수량/대금)를 최신순으로 준다.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Optional

from ._auth import KisConfig
from ._client import kis_get
from ._parse import norm_code, to_int

_PATH = "/uapi/domestic-stock/v1/quotations/inquire-investor"
_TR_ID = "FHKST01010900"


@dataclass
class InvestorDay:
    date: str                       # YYYY-MM-DD
    close: Optional[int] = None     # 종가
    change: Optional[int] = None    # 전일 대비
    individual_qty: Optional[int] = None    # 개인 순매수 수량(주)
    foreign_qty: Optional[int] = None       # 외국인 순매수 수량(주)
    institution_qty: Optional[int] = None   # 기관계 순매수 수량(주)
    individual_value: Optional[int] = None    # 개인 순매수 대금(원)
    foreign_value: Optional[int] = None       # 외국인 순매수 대금(원)
    institution_value: Optional[int] = None   # 기관계 순매수 대금(원)


def fetch_investor_trend(
    code: str,
    days: int = 20,
    cfg: Optional[KisConfig] = None,
) -> list[InvestorDay]:
    """투자자별 일별 순매수 동향을 날짜 오름차순으로 반환(최근 days영업일)."""
    code = norm_code(code)
    body = kis_get(
        _PATH,
        _TR_ID,
        {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": code},
        cfg=cfg,
    )
    rows = body.get("output") or []
    out: list[InvestorDay] = []
    for row in rows:
        d = (row.get("stck_bsop_date") or "").strip()
        if len(d) != 8:
            continue
        out.append(
            InvestorDay(
                date=f"{d[:4]}-{d[4:6]}-{d[6:8]}",
                close=to_int(row.get("stck_clpr")),
                change=to_int(row.get("prdy_vrss")),
                individual_qty=to_int(row.get("prsn_ntby_qty")),
                foreign_qty=to_int(row.get("frgn_ntby_qty")),
                institution_qty=to_int(row.get("orgn_ntby_qty")),
                individual_value=to_int(row.get("prsn_ntby_tr_pbmn")),
                foreign_value=to_int(row.get("frgn_ntby_tr_pbmn")),
                institution_value=to_int(row.get("orgn_ntby_tr_pbmn")),
            )
        )
    out.sort(key=lambda r: r.date)
    if days and len(out) > days:
        out = out[-days:]
    return out


def net_summary(rows: list[InvestorDay]) -> dict:
    """기간 누적 순매수 수량 합계 — {foreign, institution, individual}."""
    def _sum(attr: str) -> int:
        return sum(getattr(r, attr) or 0 for r in rows)

    return {
        "foreign": _sum("foreign_qty"),
        "institution": _sum("institution_qty"),
        "individual": _sum("individual_qty"),
        "days": len(rows),
    }


def to_dicts(rows: list[InvestorDay]) -> list[dict]:
    return [asdict(r) for r in rows]
