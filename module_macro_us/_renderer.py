"""SeriesData 리스트 → markdown.

요약 헤더 (파생 지표: 2y/10y spread, CPI yoy 등) + 시리즈별 최근 값/추세/range.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

from ._fetch import Observation, SeriesData


# ---- 포맷 헬퍼 ---------------------------------------------------------------


def _fmt(v: Optional[float], unit: str = "") -> str:
    if v is None:
        return "—"
    if unit == "%":
        return f"{v:.2f}%"
    if unit == "$ billions":
        # M2 같은 큰 숫자
        return f"{v:,.1f}"
    # 일반 인덱스(VIX, CPI, DXY) — 소수 둘째 자리
    return f"{v:,.2f}"


def _fmt_delta(v: Optional[float], unit: str = "") -> str:
    if v is None:
        return "—"
    sign = "+" if v >= 0 else ""
    if unit == "%":
        return f"{sign}{v:.2f}%p"  # % point delta
    return f"{sign}{v:,.2f}"


def _parse_date(s: str) -> Optional[date]:
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").date()
    except Exception:
        return None


# ---- 시계열 분석 헬퍼 -------------------------------------------------------


def _obs_before(observations: list[Observation], days_ago: int) -> Optional[Observation]:
    """latest로부터 days_ago일 전(이전)의 가장 가까운 관측치."""
    if not observations:
        return None
    latest = observations[-1]
    latest_d = _parse_date(latest.date)
    if latest_d is None:
        return None
    from datetime import timedelta as _td
    target = latest_d - _td(days=days_ago)
    # observations는 날짜 오름차순 가정. target 이하 마지막 obs.
    best: Optional[Observation] = None
    for o in observations:
        od = _parse_date(o.date)
        if od is None:
            continue
        if od <= target:
            best = o
        else:
            break
    return best


def _high_low(observations: list[Observation]) -> tuple[Optional[float], Optional[float]]:
    if not observations:
        return None, None
    vals = [o.value for o in observations]
    return max(vals), min(vals)


def _value_at(sd: SeriesData, days_ago: int) -> Optional[float]:
    o = _obs_before(sd.observations, days_ago)
    return o.value if o else None


def _delta(sd: SeriesData, days_ago: int) -> Optional[float]:
    if not sd.observations:
        return None
    latest = sd.observations[-1].value
    past = _value_at(sd, days_ago)
    if past is None:
        return None
    return latest - past


def _yoy_pct(sd: SeriesData) -> Optional[float]:
    """월별 시리즈의 yoy 변동률 (%). 12개월 전 같은 달 값과 비교."""
    if not sd.observations:
        return None
    latest = sd.observations[-1]
    latest_d = _parse_date(latest.date)
    if latest_d is None:
        return None
    # 12개월 전 = 약 365일 전
    past = _obs_before(sd.observations, 365)
    if past is None or past.value == 0:
        return None
    return (latest.value - past.value) / past.value * 100.0


def _avg(observations: list[Observation], window: int) -> Optional[float]:
    """최근 window 개 관측치의 평균."""
    if not observations:
        return None
    pick = observations[-window:]
    if not pick:
        return None
    return sum(o.value for o in pick) / len(pick)


# ---- 요약 헤더 (파생 지표) ---------------------------------------------------


def _by_key(rows: list[SeriesData]) -> dict[str, SeriesData]:
    return {r.key: r for r in rows}


def _summary_section(rows: list[SeriesData]) -> str:
    by = _by_key(rows)
    lines: list[str] = ["## 요약"]

    def latest_of(key: str) -> Optional[float]:
        sd = by.get(key)
        if not sd or not sd.observations:
            return None
        return sd.observations[-1].value

    # 10y yield
    if "us_10y" in by and by["us_10y"].observations:
        sd = by["us_10y"]
        cur = sd.observations[-1].value
        m1 = _value_at(sd, 30)
        recent_180: list[Observation] = []
        for o in sd.observations:
            od = _parse_date(o.date)
            if od is not None and (date.today() - od).days <= 180:
                recent_180.append(o)
        hi6m, _lo6m = _high_low(recent_180)
        extras: list[str] = []
        if m1 is not None:
            extras.append(f"전월 {_fmt(m1, '%')}")
        if hi6m is not None:
            extras.append(f"6m high {_fmt(hi6m, '%')}")
        if extras:
            lines.append(f"- **10y yield**: {_fmt(cur, '%')} ({', '.join(extras)})")
        else:
            lines.append(f"- **10y yield**: {_fmt(cur, '%')}")

    # 2y/10y spread
    if "us_2y" in by and "us_10y" in by and by["us_2y"].observations and by["us_10y"].observations:
        sp = by["us_10y"].observations[-1].value - by["us_2y"].observations[-1].value
        note = "역전 지속" if sp < 0 else "정상"
        lines.append(f"- **2y/10y spread**: {_fmt(sp, '%')} ({note})")

    # CPI yoy
    if "cpi" in by:
        yoy = _yoy_pct(by["cpi"])
        # 직전 yoy (한 달 전)
        sd = by["cpi"]
        prev_yoy: Optional[float] = None
        if sd.observations and len(sd.observations) >= 14:
            # latest 한 달 전 시점 기준 yoy 다시 계산
            from datetime import timedelta as _td
            latest_d = _parse_date(sd.observations[-1].date)
            if latest_d:
                cutoff = latest_d - _td(days=28)
                prev_obs = [o for o in sd.observations if _parse_date(o.date) and _parse_date(o.date) <= cutoff]
                if prev_obs:
                    prev_latest = prev_obs[-1]
                    # 12m 전
                    target = _parse_date(prev_latest.date)
                    if target:
                        past_target = target - _td(days=365)
                        past_obs_candidates = [o for o in sd.observations
                                               if _parse_date(o.date) and _parse_date(o.date) <= past_target]
                        if past_obs_candidates and past_obs_candidates[-1].value != 0:
                            prev_yoy = (prev_latest.value - past_obs_candidates[-1].value) \
                                       / past_obs_candidates[-1].value * 100.0
        if yoy is not None:
            extra = f" (직전 {prev_yoy:+.1f}%)" if prev_yoy is not None else ""
            lines.append(f"- **CPI yoy**: {yoy:+.1f}%{extra}")

    # Core CPI yoy
    if "core_cpi" in by:
        yoy = _yoy_pct(by["core_cpi"])
        if yoy is not None:
            lines.append(f"- **Core CPI yoy**: {yoy:+.1f}%")

    # Fed Funds
    ff = latest_of("fed_funds")
    if ff is not None:
        lines.append(f"- **Fed Funds**: {_fmt(ff, '%')}")

    # Unemployment
    u = latest_of("unemployment")
    if u is not None:
        lines.append(f"- **실업률**: {_fmt(u, '%')}")

    # VIX
    if "vix" in by and by["vix"].observations:
        sd = by["vix"]
        cur = sd.observations[-1].value
        avg90 = _avg(sd.observations, 90)
        if avg90 is not None:
            lines.append(f"- **VIX**: {_fmt(cur)} (90일 평균 {_fmt(avg90)})")
        else:
            lines.append(f"- **VIX**: {_fmt(cur)}")

    # Dollar Index
    if "dxy" in by and by["dxy"].observations:
        sd = by["dxy"]
        cur = sd.observations[-1].value
        past3m = _value_at(sd, 90)
        if past3m and past3m != 0:
            pct = (cur - past3m) / past3m * 100.0
            lines.append(f"- **Dollar Index**: {_fmt(cur)} (3m {pct:+.1f}%)")
        else:
            lines.append(f"- **Dollar Index**: {_fmt(cur)}")

    # Real 10y
    r10 = latest_of("real_10y")
    if r10 is not None:
        lines.append(f"- **10y 실질금리(TIPS)**: {_fmt(r10, '%')}")

    # M2 yoy
    if "m2" in by:
        yoy = _yoy_pct(by["m2"])
        if yoy is not None:
            lines.append(f"- **M2 yoy**: {yoy:+.1f}%")

    lines.append("")
    return "\n".join(lines) + "\n"


# ---- 시리즈별 상세 ----------------------------------------------------------


def _series_section(sd: SeriesData) -> str:
    spec = sd.spec
    head = f"### {spec['label_en']} ({spec['fred_id']})"
    if sd.error:
        return f"{head}\n_fetch 실패: {sd.error}_\n\n"
    if not sd.observations:
        return f"{head}\n_관측치 없음._\n\n"

    latest = sd.observations[-1]
    unit = spec["unit"]
    lines = [head]
    lines.append(f"- 최근: {_fmt(latest.value, unit)} ({latest.date})")
    d30 = _delta(sd, 30)
    d90 = _delta(sd, 90)
    lines.append(f"- 30d 변화: {_fmt_delta(d30, unit)}")
    lines.append(f"- 90d 변화: {_fmt_delta(d90, unit)}")
    hi, lo = _high_low(sd.observations)
    if hi is not None and lo is not None:
        lines.append(f"- 365d high/low: {_fmt(hi, unit)} / {_fmt(lo, unit)}")
    if spec["freq"] == "monthly":
        yoy = _yoy_pct(sd)
        if yoy is not None:
            lines.append(f"- yoy: {yoy:+.2f}%")
    _lag = {"daily": "최근 영업일", "weekly": "주간 — 최대 7일 지연",
            "monthly": "월간 — 최대 ~1개월 지연"}.get(spec["freq"], spec["freq"])
    lines.append(f"- 빈도: {spec['freq']} ({_lag}) | 단위: {spec['unit']} | KR: {spec['label_ko']}")
    return "\n".join(lines) + "\n\n"


# ---- 진입점 -----------------------------------------------------------------


def render_markdown(rows: list[SeriesData], as_of: Optional[date] = None) -> str:
    as_of = as_of or date.today()
    title = f"# 미국 매크로 ({as_of.isoformat()} 기준)\n\n"
    parts = [title, _summary_section(rows), "## 시리즈별 최근 값\n\n"]
    for sd in rows:
        parts.append(_series_section(sd))
    parts.append("## 데이터 source\n")
    parts.append("FRED (Federal Reserve Bank of St. Louis), https://fred.stlouisfed.org\n")
    return "".join(parts)
