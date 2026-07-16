"""국내주식 순위 조회 — 등락률 상승/하락 + 거래량(인기) 상위.

읽기 전용. 주문 아님(발사 경로 없음).
엔드포인트:
  - 등락률 순위 : GET /uapi/domestic-stock/v1/ranking/fluctuation      (tr FHPST01700000)
  - 거래량 순위 : GET /uapi/domestic-stock/v1/quotations/volume-rank   (tr FHPST01710000)
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List, Optional

from ._auth import KisConfig, load_config
from ._client import kis_get

_FLUCT_PATH = "/uapi/domestic-stock/v1/ranking/fluctuation"
_FLUCT_TR = "FHPST01700000"
_VOL_PATH = "/uapi/domestic-stock/v1/quotations/volume-rank"
_VOL_TR = "FHPST01710000"

# 응답마다 종목코드 키가 다름(엔드포인트별) — 순서대로 시도
_CODE_KEYS = ("stck_shrn_iscd", "mksc_shrn_iscd", "mksc_shrn_iscd", "stck_shrn_iscd")


@dataclass
class RankRow:
    code: str                       # 6자리 종목코드
    name: str                       # 한글 종목명
    price: Optional[float]          # 현재가(원)
    change_pct: Optional[float]     # 전일대비 등락률(%)
    volume: Optional[int] = None    # 누적 거래량(주)

    def to_dict(self) -> dict:
        return asdict(self)


def _f(v) -> Optional[float]:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _i(v) -> Optional[int]:
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


# ETF/ETN 이름 휴리스틱(개별종목 뷰에서 제외)
_ETF_PREFIX = ("KODEX", "TIGER", "SOL", "ACE", "1Q", "KBSTAR", "ARIRANG",
               "HANARO", "KOSEF", "PLUS", "RISE", "TIMEFOLIO", "WON", "BNK",
               "KIWOOM", "히어로즈", "마이다스", "파워", "TREX")
_ETF_KEYWORD = ("레버리지", "인버스", "선물", "2X", "ETN", "채권", "국고채", "리츠")


def _is_etf(name: str) -> bool:
    n = (name or "").upper()
    if any(n.startswith(p) for p in _ETF_PREFIX):
        return True
    return any(k.upper() in n for k in _ETF_KEYWORD)


def _code_of(r: dict) -> str:
    for k in ("stck_shrn_iscd", "mksc_shrn_iscd"):
        v = r.get(k)
        if v:
            return str(v).strip()
    return ""


def fetch_fluctuation(rising: bool = True, top: int = 5,
                      cfg: Optional[KisConfig] = None,
                      exclude_etf: bool = True) -> List[RankRow]:
    """등락률 순위. rising=True 상승률 상위 / False 하락률 상위.
    exclude_etf=True(기본) 면 레버리지/인버스/ETN 등 제외(개별종목 뷰)."""
    cfg = cfg or load_config()
    params = {
        "fid_cond_mrkt_div_code": "J",
        "fid_cond_scr_div_code": "20170",
        "fid_input_iscd": "0000",           # 0000 전체
        "fid_rank_sort_cls_code": "0" if rising else "1",  # 0 상승률 / 1 하락률
        "fid_input_cnt_1": "0",
        "fid_prc_cls_code": "0",
        "fid_input_price_1": "",
        "fid_input_price_2": "",
        "fid_vol_cnt": "",
        "fid_trgt_cls_code": "0",
        "fid_trgt_exls_cls_code": "0",
        "fid_div_cls_code": "0",
        "fid_rsfl_rate1": "",
        "fid_rsfl_rate2": "",
    }
    body = kis_get(_FLUCT_PATH, _FLUCT_TR, params, cfg=cfg)
    out = body.get("output") or []
    rows = [
        RankRow(code=_code_of(r), name=(r.get("hts_kor_isnm") or "").strip(),
                price=_f(r.get("stck_prpr")), change_pct=_f(r.get("prdy_ctrt")),
                volume=_i(r.get("acml_vol")))
        for r in out
    ]
    # API 정렬 quirk 방지 — 등락률로 클라이언트 재정렬 후 top 절단
    rows = [r for r in rows if r.code and r.change_pct is not None]
    if exclude_etf:
        rows = [r for r in rows if not _is_etf(r.name)]
    rows.sort(key=lambda r: r.change_pct, reverse=rising)
    return rows[:top]


def fetch_volume_rank(top: int = 5, cfg: Optional[KisConfig] = None) -> List[RankRow]:
    """거래량 상위(인기). 주의: 레버리지/인버스 ETF가 상위 점유하는 경향."""
    cfg = cfg or load_config()
    params = {
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_COND_SCR_DIV_CODE": "20171",
        "FID_INPUT_ISCD": "0000",
        "FID_DIV_CLS_CODE": "0",
        "FID_BLNG_CLS_CODE": "0",          # 0 평균거래량
        "FID_TRGT_CLS_CODE": "111111111",
        "FID_TRGT_EXLS_CLS_CODE": "0000000000",
        "FID_INPUT_PRICE_1": "0",
        "FID_INPUT_PRICE_2": "0",
        "FID_VOL_CNT": "0",
        "FID_INPUT_DATE_1": "",
    }
    body = kis_get(_VOL_PATH, _VOL_TR, params, cfg=cfg)
    out = body.get("output") or []
    rows = [
        RankRow(code=_code_of(r), name=(r.get("hts_kor_isnm") or "").strip(),
                price=_f(r.get("stck_prpr")), change_pct=_f(r.get("prdy_ctrt")),
                volume=_i(r.get("acml_vol")))
        for r in out
    ]
    return [r for r in rows if r.code][:top]


if __name__ == "__main__":  # 간이 self-test
    import os
    from pathlib import Path
    here = Path(__file__).resolve().parent.parent
    for env_file in (here / ".env",):
        if env_file.exists():
            for ln in env_file.read_text(encoding="utf-8").splitlines():
                ln = ln.strip()
                if ln and not ln.startswith("#") and "=" in ln:
                    k, _, v = ln.partition("=")
                    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    c = load_config()
    print("── 상승 top5 ──")
    for r in fetch_fluctuation(True, 5, c):
        print(f"  {r.name}({r.code}) {r.price:,.0f}원 {r.change_pct:+.2f}%")
    print("── 하락 top5 ──")
    for r in fetch_fluctuation(False, 5, c):
        print(f"  {r.name}({r.code}) {r.price:,.0f}원 {r.change_pct:+.2f}%")
    print("── 거래량(인기) top5 ──")
    for r in fetch_volume_rank(5, c):
        print(f"  {r.name}({r.code}) {r.price:,.0f}원 {r.change_pct:+.2f}% vol={r.volume:,}")
