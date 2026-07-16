"""yfinance wrapper — 단일 ticker 펀더멘털 스냅샷.

Ticker.info / analyst_price_targets / recommendations /
quarterly_income_stmt / quarterly_balance_sheet / calendar 한 번에 묶음.
한 호출이라도 실패하면 그 필드만 None 두고 진행.
"""
from __future__ import annotations

import sys
from dataclasses import asdict, dataclass, field
from datetime import date, datetime
from typing import Optional

import yfinance as yf


@dataclass
class FundamentalsSnapshot:
    ticker: str
    company_name: Optional[str] = None
    sector: Optional[str] = None
    industry: Optional[str] = None
    price: Optional[float] = None
    market_cap: Optional[int] = None
    # 밸류에이션
    trailing_pe: Optional[float] = None
    forward_pe: Optional[float] = None
    peg_ratio: Optional[float] = None
    price_to_sales: Optional[float] = None
    price_to_book: Optional[float] = None
    # EPS
    trailing_eps: Optional[float] = None
    forward_eps: Optional[float] = None
    # 52주
    fifty_two_week_high: Optional[float] = None
    fifty_two_week_low: Optional[float] = None
    # 컨센서스
    target_low: Optional[float] = None
    target_mean: Optional[float] = None
    target_high: Optional[float] = None
    target_median: Optional[float] = None
    # 추천
    recommendations: list[dict] = field(default_factory=list)
    # 분기 매출 (yfinance) — [(quarter_end_date_str, revenue_float), ...]
    quarterly_revenue: list[tuple[str, float]] = field(default_factory=list)
    # 분기 매출 (SEC XBRL, 교차 검증)
    quarterly_revenue_xbrl: list[tuple[str, float]] = field(default_factory=list)
    # 사업 요약 (long)
    business_summary: Optional[str] = None
    # 메타
    next_earnings_date: Optional[str] = None
    beta: Optional[float] = None
    dividend_yield: Optional[float] = None


def _safe_get(d: dict, key: str) -> Optional[object]:
    if not isinstance(d, dict):
        return None
    v = d.get(key)
    if v is None or v == "":
        return None
    return v


def _to_float(v) -> Optional[float]:
    if v is None:
        return None
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    # NaN guard
    if f != f:
        return None
    return f


def _extract_quarterly_revenue(qis) -> list[tuple[str, float]]:
    """quarterly_income_stmt DataFrame → [(date_str, revenue), ...] 최신순."""
    if qis is None:
        return []
    try:
        if qis.empty:
            return []
    except Exception:
        return []
    # 매출 행: Total Revenue 우선, 없으면 Operating Revenue
    row = None
    for candidate in ("Total Revenue", "Operating Revenue", "TotalRevenue"):
        if candidate in qis.index:
            row = qis.loc[candidate]
            break
    if row is None:
        return []
    out: list[tuple[str, float]] = []
    for col in qis.columns:
        try:
            v = row[col]
        except Exception:
            continue
        f = _to_float(v)
        if f is None:
            continue
        # col 보통 Timestamp
        try:
            ds = col.strftime("%Y-%m-%d")
        except Exception:
            ds = str(col)[:10]
        out.append((ds, f))
    # 최신순 정렬 (이미 그렇지만 명시)
    out.sort(key=lambda x: x[0], reverse=True)
    return out


def _extract_next_earnings(calendar) -> Optional[str]:
    if not calendar:
        return None
    try:
        ed = calendar.get("Earnings Date")
    except Exception:
        return None
    if not ed:
        return None
    # ed: list of date | single date
    if isinstance(ed, (list, tuple)):
        if not ed:
            return None
        d0 = ed[0]
    else:
        d0 = ed
    if isinstance(d0, (date, datetime)):
        return d0.strftime("%Y-%m-%d") if isinstance(d0, date) else d0.date().isoformat()
    return str(d0)[:10]


def _extract_recommendations(rec_df) -> list[dict]:
    """recommendations DataFrame → list of dict."""
    if rec_df is None:
        return []
    try:
        if rec_df.empty:
            return []
    except Exception:
        return []
    out: list[dict] = []
    for _, row in rec_df.iterrows():
        d: dict = {}
        for col in rec_df.columns:
            v = row[col]
            if col == "period":
                d["period"] = str(v)
            else:
                f = _to_float(v)
                d[str(col)] = int(f) if (f is not None and f == int(f)) else f
        out.append(d)
    return out


def fetch_fundamentals(ticker: str) -> FundamentalsSnapshot:
    """yfinance 호출 묶음. 개별 호출 실패는 None 으로 두고 progress."""
    snap = FundamentalsSnapshot(ticker=ticker.upper())
    try:
        t = yf.Ticker(ticker)
    except Exception as e:
        sys.stderr.write(f"[warn] yf.Ticker init failed: {e}\n")
        return snap

    # info
    info: dict = {}
    try:
        info = t.info or {}
    except Exception as e:
        sys.stderr.write(f"[warn] info fetch failed: {e}\n")

    # Unknown ticker detection: info 가 거의 비어있고 symbol 도 없으면 알 수 없음.
    if isinstance(info, dict) and len(info) <= 2 and not info.get("symbol") and not info.get("shortName"):
        # 비어있는 snap 반환 — 호출자가 판단
        return snap

    snap.company_name = _safe_get(info, "longName") or _safe_get(info, "shortName")
    snap.sector = _safe_get(info, "sector")
    snap.industry = _safe_get(info, "industry")
    snap.price = _to_float(_safe_get(info, "currentPrice") or _safe_get(info, "regularMarketPrice"))
    mc = _safe_get(info, "marketCap")
    if mc is not None:
        try:
            snap.market_cap = int(mc)
        except Exception:
            snap.market_cap = None
    snap.trailing_pe = _to_float(_safe_get(info, "trailingPE"))
    snap.forward_pe = _to_float(_safe_get(info, "forwardPE"))
    snap.peg_ratio = _to_float(_safe_get(info, "pegRatio") or _safe_get(info, "trailingPegRatio"))
    snap.price_to_sales = _to_float(_safe_get(info, "priceToSalesTrailing12Months"))
    snap.price_to_book = _to_float(_safe_get(info, "priceToBook"))
    snap.trailing_eps = _to_float(_safe_get(info, "trailingEps"))
    snap.forward_eps = _to_float(_safe_get(info, "forwardEps"))
    snap.fifty_two_week_high = _to_float(_safe_get(info, "fiftyTwoWeekHigh"))
    snap.fifty_two_week_low = _to_float(_safe_get(info, "fiftyTwoWeekLow"))
    snap.beta = _to_float(_safe_get(info, "beta"))
    snap.dividend_yield = _to_float(_safe_get(info, "dividendYield"))
    bs = _safe_get(info, "longBusinessSummary")
    if isinstance(bs, str):
        snap.business_summary = bs

    # analyst_price_targets
    try:
        tp = t.analyst_price_targets or {}
    except Exception as e:
        sys.stderr.write(f"[warn] analyst_price_targets failed: {e}\n")
        tp = {}
    if isinstance(tp, dict):
        snap.target_low = _to_float(tp.get("low"))
        snap.target_mean = _to_float(tp.get("mean"))
        snap.target_high = _to_float(tp.get("high"))
        snap.target_median = _to_float(tp.get("median"))

    # recommendations
    try:
        rec = t.recommendations
    except Exception as e:
        sys.stderr.write(f"[warn] recommendations failed: {e}\n")
        rec = None
    snap.recommendations = _extract_recommendations(rec)

    # quarterly_income_stmt
    try:
        qis = t.quarterly_income_stmt
    except Exception as e:
        sys.stderr.write(f"[warn] quarterly_income_stmt failed: {e}\n")
        qis = None
    snap.quarterly_revenue = _extract_quarterly_revenue(qis)[:8]

    # quarterly_balance_sheet — 현재는 출력 표에서 안 쓰지만 호출 자체는 시도 (warm cache, 향후 확장)
    try:
        _ = t.quarterly_balance_sheet
    except Exception:
        pass

    # calendar
    try:
        cal = t.calendar
    except Exception as e:
        sys.stderr.write(f"[warn] calendar failed: {e}\n")
        cal = None
    snap.next_earnings_date = _extract_next_earnings(cal)

    return snap


def to_dict(snap: FundamentalsSnapshot) -> dict:
    return asdict(snap)
