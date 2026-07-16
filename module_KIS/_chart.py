# FILE: research_Mvp/module_kis/_chart.py
"""국내주식 기간별 시세(OHLCV) — 일/주/월/년봉.

엔드포인트: GET /uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice
tr_id:      FHKST03010100 (실전/모의 동일)

한 번 호출에 최대 100봉(가장 최근 100개)을 [start, end] 구간에서 돌려준다.
100봉을 넘기는 요청은 end 날짜를 과거로 밀며 창(window)을 이어붙여 페이지네이션.

terminal/prices.py 의 yfinance .KS/.KQ 해석은 접미사 추정이 불안정하다 —
KIS는 6자리 코드를 그대로 받으므로 더 안정적인 OHLCV 소스.
출력은 terminal 차트 파이프라인이 쓰기 좋게 날짜 오름차순 dict 리스트로 정규화.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta
from typing import Optional

from ._auth import KisConfig
from ._client import kis_get
from ._parse import norm_code, to_float, to_int

_PATH = "/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice"
_TR_ID = "FHKST03010100"

_PERIOD_CODES = {"D": "일", "W": "주", "M": "월", "Y": "년"}
# 한 호출당 과거로 얼마나 끌어올지(달력일). 100봉을 충분히 채우게 넉넉히.
_WINDOW_DAYS = {"D": 200, "W": 760, "M": 3200, "Y": 38000}
_MAX_PAGES = 12  # 페이지네이션 무한루프 방지.


@dataclass
class KisBar:
    date: str        # YYYY-MM-DD
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    volume: Optional[int]
    value: Optional[int] = None  # 거래대금(원)


def _parse_rows(output2: list) -> list[KisBar]:
    bars: list[KisBar] = []
    for row in output2 or []:
        d = (row.get("stck_bsop_date") or "").strip()
        if len(d) != 8:
            continue
        bars.append(
            KisBar(
                date=f"{d[:4]}-{d[4:6]}-{d[6:8]}",
                open=to_float(row.get("stck_oprc")),
                high=to_float(row.get("stck_hgpr")),
                low=to_float(row.get("stck_lwpr")),
                close=to_float(row.get("stck_clpr")),
                volume=to_int(row.get("acml_vol")),
                value=to_int(row.get("acml_tr_pbmn")),
            )
        )
    return bars


def fetch_ohlcv(
    code: str,
    period: str = "D",
    count: int = 100,
    *,
    adjusted: bool = True,
    end_date: Optional[str] = None,
    cfg: Optional[KisConfig] = None,
) -> tuple[list[KisBar], Optional[str]]:
    """기간별 OHLCV 를 날짜 오름차순으로 반환.

    Args:
        code: 6자리 종목코드.
        period: D(일)/W(주)/M(월)/Y(년).
        count: 받아올 봉 개수(100 초과 시 자동 페이지네이션).
        adjusted: True=수정주가(권리락 반영), False=원주가.
        end_date: 기준 종료일 YYYYMMDD(기본 오늘). 과거 시점 조회용.

    Returns:
        (bars, name) — bars 는 날짜 오름차순 KisBar 리스트, name 은 종목명(output1).
    """
    code = norm_code(code)
    period = period.upper()
    if period not in _PERIOD_CODES:
        raise ValueError(f"period 는 D/W/M/Y 중 하나여야 합니다 (받음: {period!r}).")

    end = datetime.strptime(end_date, "%Y%m%d").date() if end_date else date.today()
    window = timedelta(days=_WINDOW_DAYS[period])
    adj = "0" if adjusted else "1"  # KIS: 0=수정주가, 1=원주가

    by_date: dict[str, KisBar] = {}
    name: Optional[str] = None
    cur_end = end

    for _ in range(_MAX_PAGES):
        start = cur_end - window
        body = kis_get(
            _PATH,
            _TR_ID,
            {
                "FID_COND_MRKT_DIV_CODE": "J",
                "FID_INPUT_ISCD": code,
                "FID_INPUT_DATE_1": start.strftime("%Y%m%d"),
                "FID_INPUT_DATE_2": cur_end.strftime("%Y%m%d"),
                "FID_PERIOD_DIV_CODE": period,
                "FID_ORG_ADJ_PRC": adj,
            },
            cfg=cfg,
        )
        if name is None:
            o1 = body.get("output1") or {}
            name = (o1.get("hts_kor_isnm") or "").strip() or None

        rows = _parse_rows(body.get("output2") or [])
        if not rows:
            break
        for b in rows:
            by_date.setdefault(b.date, b)

        if len(by_date) >= count:
            break

        oldest = min(b.date for b in rows)  # YYYY-MM-DD
        oldest_d = datetime.strptime(oldest, "%Y-%m-%d").date()
        next_end = oldest_d - timedelta(days=1)
        if next_end >= cur_end:  # 진척 없음 → 종료
            break
        cur_end = next_end

    bars = sorted(by_date.values(), key=lambda b: b.date)
    if len(bars) > count:
        bars = bars[-count:]  # 최근 count 개만.
    return bars, name


def to_dicts(bars: list[KisBar]) -> list[dict]:
    return [asdict(b) for b in bars]
