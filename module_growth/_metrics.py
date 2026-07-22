"""이익 성장 지표 — 분기 시계열에서 결정론 계산. 순수 함수, 네트워크 의존 0.

입력 시계열은 **최신순** `[(quarter_end_str, value), ...]` (yfinance/DART 공통 형태).
이 파일은 판단(사라/팔라)을 하지 않는다 — 관측값만 낸다(P4). 무엇을 살지는 상위(에이전트)가.

성장 점수(`score_growth`)는 튜닝용이라 가중치·임계값을 **모듈 상수**로 노출한다 — 실험자가 만진다.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Sequence

Series = Sequence[tuple[str, float]]

# ── 튜닝 파라미터 (실험자가 만지는 곳) ──────────────────────────────────
# 성장 점수는 '연 성장 % 근사' 단위. 실현 이익 성장이 1순위, 없으면 매출·선행으로 강등.
QUALITY_MIN_QUARTERS = 4        # 실현 지표를 신뢰할 최소 분기 수
ACCEL_WEIGHT = 0.5             # 가속(최신 YoY − 직전 YoY) 반영 비율
ACCEL_CLAMP = 0.5             # 가속 보정 상·하한 (±50%p)
REVENUE_UNBACKED_HAIRCUT = 0.5  # 이익성장이 매출 뒷받침 없을 때 base 를 깎는 비율
# 등급 임계값 (점수 %, 대략 연 YoY 기준)
GRADE_THRESHOLDS = [("A", 0.30), ("B", 0.15), ("C", 0.05), ("D", -1e9)]
# PEG 밸류 태그
PEG_TAGS = [(1.0, "저평가성장"), (2.0, "적정"), (3.0, "다소고평가"), (1e9, "고평가")]


@dataclass
class GrowthMetrics:
    ticker: str
    name: str = ""
    sector: str = ""
    # 실현 성장 (분기 YoY, 최신 분기)
    revenue_yoy: Optional[float] = None
    earnings_yoy: Optional[float] = None       # 순이익 YoY
    eps_yoy: Optional[float] = None
    # TTM (계절성 제거, 8분기 필요)
    revenue_ttm_yoy: Optional[float] = None
    earnings_ttm_yoy: Optional[float] = None
    # 가속 (최신 YoY − 직전 YoY, 6분기 필요)
    earnings_accel: Optional[float] = None
    revenue_accel: Optional[float] = None
    # 선행 (컨센)
    fwd_eps_growth: Optional[float] = None     # forward/trailing − 1
    peg: Optional[float] = None
    # 품질
    profitable_quarters: Optional[int] = None  # 최근 관측분기 중 순이익>0 개수
    n_quarters: int = 0
    latest_quarter: Optional[str] = None       # 신선도(P4)
    # 종합
    score: Optional[float] = None
    score_source: str = ""                     # 점수의 1순위 신호가 무엇이었나
    grade: str = "?"                           # A/B/C/D/?(관측불가)
    value_tag: str = ""                        # PEG 기반
    flags: list[str] = field(default_factory=list)  # 데이터 한계·품질 경고

    def to_dict(self) -> dict:
        from dataclasses import asdict
        return asdict(self)


def _f(v) -> Optional[float]:
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    if f != f:  # NaN
        return None
    return f


def yoy_growth(series: Series, index: int = 0, lag: int = 4) -> Optional[float]:
    """series[index] 대비 series[index+lag] 의 성장률. 최신순 시계열 가정.

    분모(과거값)가 <=0 이면 성장률 부호가 무의미 → None (호출자가 flag).
    """
    if series is None:
        return None
    if index + lag >= len(series):
        return None
    cur = _f(series[index][1])
    base = _f(series[index + lag][1])
    if cur is None or base is None or base <= 0:
        return None
    return cur / base - 1.0


def ttm_sum(series: Series, start: int = 0) -> Optional[float]:
    """start 부터 4분기 합(TTM). 4분기 미만이면 None."""
    if series is None or start + 4 > len(series):
        return None
    vals = [_f(series[i][1]) for i in range(start, start + 4)]
    if any(v is None for v in vals):
        return None
    return sum(vals)  # type: ignore[arg-type]


def ttm_yoy(series: Series) -> Optional[float]:
    """최근 TTM 대 직전 TTM(8분기 필요). 계절성 제거된 성장률."""
    cur = ttm_sum(series, 0)
    base = ttm_sum(series, 4)
    if cur is None or base is None or base <= 0:
        return None
    return cur / base - 1.0


def acceleration(series: Series, lag: int = 4) -> Optional[float]:
    """최신 분기 YoY − 직전 분기 YoY. 양수면 성장 가속. (lag+2 분기 필요)"""
    now = yoy_growth(series, index=0, lag=lag)
    prev = yoy_growth(series, index=1, lag=lag)
    if now is None or prev is None:
        return None
    return now - prev


def count_positive(series: Series) -> int:
    return sum(1 for _, v in series if (_f(v) or 0) > 0)


def compute_metrics(
    ticker: str,
    *,
    revenue: Optional[Series] = None,
    net_income: Optional[Series] = None,
    diluted_eps: Optional[Series] = None,
    trailing_eps: Optional[float] = None,
    forward_eps: Optional[float] = None,
    peg: Optional[float] = None,
) -> GrowthMetrics:
    """분기 시계열 + 스칼라 → GrowthMetrics. 계산 가능한 것만 채우고 나머진 None + flag."""
    revenue = revenue or []
    net_income = net_income or []
    diluted_eps = diluted_eps or []
    m = GrowthMetrics(ticker=ticker)
    m.n_quarters = len(net_income) or len(revenue)
    if net_income:
        m.latest_quarter = net_income[0][0]
    elif revenue:
        m.latest_quarter = revenue[0][0]

    m.revenue_yoy = yoy_growth(revenue)
    m.earnings_yoy = yoy_growth(net_income)
    m.eps_yoy = yoy_growth(diluted_eps)
    m.revenue_ttm_yoy = ttm_yoy(revenue)
    m.earnings_ttm_yoy = ttm_yoy(net_income)
    m.earnings_accel = acceleration(net_income)
    m.revenue_accel = acceleration(revenue)
    m.peg = _f(peg)

    te, fe = _f(trailing_eps), _f(forward_eps)
    if te is not None and fe is not None and te > 0:
        m.fwd_eps_growth = fe / te - 1.0

    if net_income:
        m.profitable_quarters = count_positive(net_income)
        if m.profitable_quarters < len(net_income):
            m.flags.append(f"적자분기 {len(net_income) - m.profitable_quarters}/{len(net_income)}")

    # 실현 이익 YoY 를 못 낸 이유를 밝힌다(부재 vs 적자기저) — P4
    if net_income and m.earnings_yoy is None:
        if len(net_income) <= QUALITY_MIN_QUARTERS:
            m.flags.append(f"YoY 불가: 분기 {len(net_income)}개(5개+ 필요)")
        else:
            m.flags.append("YoY 불가: 전년 기저 순이익 <=0")

    _score(m)
    return m


def _score(m: GrowthMetrics) -> None:
    """실현 이익 성장을 1순위로, 없으면 매출·선행으로 강등해 성장 점수를 낸다.

    점수 단위 = 대략 '연 YoY %'. 가속 보정 + 매출 뒷받침 감점.
    """
    base: Optional[float] = None
    src = ""
    for value, label in (
        (m.earnings_ttm_yoy, "순이익 TTM YoY"),
        (m.earnings_yoy, "순이익 분기 YoY"),
        (m.eps_yoy, "EPS 분기 YoY"),
        (m.fwd_eps_growth, "선행 EPS 성장(컨센)"),
        (m.revenue_ttm_yoy, "매출 TTM YoY"),
        (m.revenue_yoy, "매출 분기 YoY"),
    ):
        if value is not None:
            base, src = value, label
            break

    if base is None:
        m.score = None
        m.grade = "?"
        m.flags.append("성장 관측 불가(재무 시계열 없음)")
        _value_tag(m)
        return

    score = base
    # 가속 보정
    if m.earnings_accel is not None:
        adj = max(-ACCEL_CLAMP, min(ACCEL_CLAMP, m.earnings_accel)) * ACCEL_WEIGHT
        score += adj
    # 이익 성장이 매출 뒷받침 없이 나오면(원가절감·일회성 의심) 감점
    if (
        src.startswith("순이익")
        and base > 0
        and m.revenue_yoy is not None
        and m.revenue_yoy < 0
    ):
        score *= REVENUE_UNBACKED_HAIRCUT
        m.flags.append("이익성장 매출 뒷받침 약함(매출 YoY 음수)")

    m.score = round(score, 4)
    m.score_source = src
    for grade, thr in GRADE_THRESHOLDS:
        if score >= thr:
            m.grade = grade
            break
    _value_tag(m)


def _value_tag(m: GrowthMetrics) -> None:
    if m.peg is None or m.peg <= 0:
        m.value_tag = ""
        return
    for hi, tag in PEG_TAGS:
        if m.peg < hi:
            m.value_tag = f"{tag}(PEG {m.peg:.2f})"
            return
