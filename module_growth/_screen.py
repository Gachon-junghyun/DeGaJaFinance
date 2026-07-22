"""이익 성장 스크리너 — 유니버스를 훑어 GrowthMetrics 로 랭킹.

재무 fetch 는 **재구현하지 않는다**(P1):
  · US → module_fundamentals_us.fetch_fundamentals (yfinance 분기 손익 + 컨센)
  · KR → module_valuation.fetch_naver_snapshot (선행 EPS 성장만 — 실현 히스토리 부재, 아래 한계 참조)
둘 다 함수 안에서 lazy import — US 만 쓸 때 bs4/lxml, KR 만 쓸 때 yfinance 를 강제하지 않는다.

⚠️ 시장별 데이터 한계(P4, 정직하게):
  · US: yfinance 분기 손익 = 실현 순이익/매출/EPS 히스토리(보통 4~5분기, 최대 8). YoY 는 5분기+ 필요.
  · KR: 네이버는 **스냅샷만**(PER·EPS TTM/추정). 실현 분기 이익 히스토리가 없어 '선행 EPS 성장(컨센)'만.
        실현 KR 이익 성장은 DART 재무제표 API(fnlttSinglAcnt) 붙인 뒤 가능 — MODULE_MAP '다음 후보'.
"""
from __future__ import annotations

import sys
import time
from dataclasses import dataclass, field
from typing import Optional

from ._metrics import GrowthMetrics, compute_metrics
from ._universe import load_universe


@dataclass
class ScreenResult:
    rows: list[GrowthMetrics] = field(default_factory=list)
    market: str = ""
    n_requested: int = 0
    n_fetched: int = 0            # 재무 하나라도 받은 종목
    n_scored: int = 0            # 성장 점수를 낸 종목
    latest_quarter_seen: Optional[str] = None
    asof: str = ""               # 실행 시각(신선도)
    notes: list[str] = field(default_factory=list)


def _sleep(sec: float) -> None:
    if sec > 0:
        time.sleep(sec)


def _fetch_us(ticker: str, retries: int, backoff: float):
    """(revenue, net_income, diluted_eps, trailing_eps, forward_eps, peg) 또는 None(빈응답)."""
    from module_fundamentals_us import fetch_fundamentals  # lazy: yfinance

    last = None
    for attempt in range(retries + 1):
        snap = fetch_fundamentals(ticker)
        last = snap
        got = snap.quarterly_net_income or snap.quarterly_revenue or snap.trailing_eps
        if got:
            return (
                snap.quarterly_revenue,
                snap.quarterly_net_income,
                snap.quarterly_diluted_eps,
                snap.trailing_eps,
                snap.forward_eps,
                snap.peg_ratio,
            )
        if attempt < retries:
            _sleep(backoff * (2 ** attempt))  # 429 지수 백오프
    return None


def _fetch_kr(ticker: str, retries: int, backoff: float):
    """네이버 스냅샷 → 선행 성장용 스칼라. 실현 시계열은 없음(빈 리스트)."""
    from module_valuation._naver_fetch import fetch_naver_snapshot  # lazy: bs4/lxml

    code = ticker.split(".")[0]  # 005930.KS → 005930
    for attempt in range(retries + 1):
        try:
            snap = fetch_naver_snapshot(code)
        except Exception as e:  # noqa: BLE001
            if attempt >= retries:
                sys.stderr.write(f"[{ticker}] naver 실패: {e}\n")
                return None
            _sleep(backoff * (2 ** attempt))
            continue
        if snap.eps_ttm or snap.per_ttm:
            # KR PEG 근사 = PER(TTM) / 선행성장%  (실현 성장이 없어 컨센 선행으로)
            peg = None
            if snap.per_ttm and snap.eps_ttm and snap.eps_fwd and snap.eps_ttm > 0:
                g = (snap.eps_fwd / snap.eps_ttm - 1) * 100
                if g > 0:
                    peg = round(snap.per_ttm / g, 3)
            return ([], [], [], snap.eps_ttm, snap.eps_fwd, peg)
        if attempt < retries:
            _sleep(backoff * (2 ** attempt))
    return None


def screen(
    market: str = "us",
    *,
    limit: Optional[int] = 30,
    sector: Optional[str] = None,
    min_market_cap: Optional[float] = None,
    sleep: float = 0.4,
    retries: int = 2,
    backoff: float = 1.5,
    asof: str = "",
    progress: bool = True,
) -> ScreenResult:
    """유니버스를 훑어 이익 성장 랭킹을 낸다. asof 는 호출자가 넘긴다(결정론)."""
    market = market.lower()
    universe = load_universe(
        market, limit=limit, sector=sector, min_market_cap=min_market_cap
    )
    res = ScreenResult(market=market, n_requested=len(universe), asof=asof)
    if market == "kr":
        res.notes.append(
            "KR = 선행 EPS 성장(컨센)만 — 네이버 스냅샷엔 실현 분기 이익 히스토리 없음. "
            "실현 성장은 DART 재무제표 API 도입 후."
        )

    for i, row in enumerate(universe, 1):
        if progress:
            sys.stderr.write(f"[{i}/{len(universe)}] {row.ticker} {row.name} ...\n")
        fetched = _fetch_us(row.ticker, retries, backoff) if market == "us" \
            else _fetch_kr(row.ticker, retries, backoff)
        if fetched is None:
            m = GrowthMetrics(ticker=row.ticker, name=row.name, sector=row.sector)
            m.flags.append("fetch 실패(빈 응답/429)")
            m.grade = "?"
            res.rows.append(m)
            _sleep(sleep)
            continue
        rev, ni, eps, te, fe, peg = fetched
        m = compute_metrics(
            row.ticker, revenue=rev, net_income=ni, diluted_eps=eps,
            trailing_eps=te, forward_eps=fe, peg=peg,
        )
        m.name, m.sector = row.name, row.sector
        res.rows.append(m)
        res.n_fetched += 1
        if m.score is not None:
            res.n_scored += 1
        if m.latest_quarter and (
            res.latest_quarter_seen is None or m.latest_quarter > res.latest_quarter_seen
        ):
            res.latest_quarter_seen = m.latest_quarter
        _sleep(sleep)

    # 점수순 랭킹(관측불가는 뒤로)
    res.rows.sort(key=lambda x: (x.score is not None, x.score or -1e18), reverse=True)
    return res
