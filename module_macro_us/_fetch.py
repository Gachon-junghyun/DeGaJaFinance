"""FRED API wrapper.

fredapi가 설치돼 있으면 그걸 쓰고, 없으면 requests로 FRED REST API 직접 호출.
어느 쪽이든 결과는 동일한 dataclass 리스트로 정규화.

환경변수 FRED_API_KEY 필수. 없으면 친절한 안내 메시지로 SystemExit.
Rate limit: FRED 공식 120 req/min. 호출 사이 0.1s sleep 권장.
"""
from __future__ import annotations

import os
import sys
import time
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import Optional

import requests

from ._series import SERIES_CATALOG, SeriesSpec

FRED_OBS_URL = "https://api.stlouisfed.org/fred/series/observations"
RATE_LIMIT_SLEEP = 0.1  # 초


class MacroFetchError(RuntimeError):
    """fetch 단계의 사용자-친화 에러."""


@dataclass
class Observation:
    date: str   # YYYY-MM-DD
    value: float


@dataclass
class SeriesData:
    key: str
    spec: SeriesSpec
    observations: list[Observation] = field(default_factory=list)
    error: Optional[str] = None  # 시리즈별 fetch 실패 시 메시지

    @property
    def latest(self) -> Optional[Observation]:
        return self.observations[-1] if self.observations else None


def _require_api_key() -> str:
    key = os.environ.get("FRED_API_KEY", "").strip()
    if not key:
        raise MacroFetchError(
            "FRED_API_KEY 환경변수가 없음. "
            "https://fred.stlouisfed.org/docs/api/api_key.html 에서 "
            "무료 발급 후 .env 또는 셸 환경변수에 추가하라."
        )
    return key


def _parse_value(raw: str) -> Optional[float]:
    """FRED는 결측을 '.' 로 반환."""
    if raw is None:
        return None
    raw = raw.strip()
    if raw in ("", "."):
        return None
    try:
        return float(raw)
    except (ValueError, TypeError):
        return None


def _fetch_via_fredapi(spec: SeriesSpec, start: date, end: date, api_key: str) -> list[Observation]:
    """fredapi 패키지 경로. import 실패 시 ImportError 그대로 raise."""
    from fredapi import Fred  # type: ignore[import-not-found]

    fred = Fred(api_key=api_key)
    s = fred.get_series(
        spec["fred_id"],
        observation_start=start.isoformat(),
        observation_end=end.isoformat(),
    )
    obs: list[Observation] = []
    for ts, val in s.items():
        # pandas Timestamp → ISO date
        try:
            d = ts.date().isoformat() if hasattr(ts, "date") else str(ts)[:10]
        except Exception:
            d = str(ts)[:10]
        try:
            fval = float(val)
        except (ValueError, TypeError):
            continue
        if fval != fval:  # NaN check
            continue
        obs.append(Observation(date=d, value=fval))
    return obs


def _fetch_via_rest(spec: SeriesSpec, start: date, end: date, api_key: str) -> list[Observation]:
    """REST API fallback."""
    params = {
        "series_id": spec["fred_id"],
        "api_key": api_key,
        "file_type": "json",
        "observation_start": start.isoformat(),
        "observation_end": end.isoformat(),
    }
    r = requests.get(FRED_OBS_URL, params=params, timeout=30)
    if r.status_code != 200:
        # FRED는 400/422 + JSON 에러 메시지를 준다
        try:
            body = r.json()
            msg = body.get("error_message") or body.get("message") or r.text[:200]
        except Exception:
            msg = r.text[:200]
        raise MacroFetchError(
            f"FRED API {r.status_code} for {spec['fred_id']}: {msg}"
        )
    data = r.json()
    rows = data.get("observations", [])
    obs: list[Observation] = []
    for row in rows:
        val = _parse_value(row.get("value", ""))
        if val is None:
            continue
        d = row.get("date", "")[:10]
        if not d:
            continue
        obs.append(Observation(date=d, value=val))
    return obs


def _fetch_one(key: str, days: int, api_key: str, use_fredapi: bool) -> SeriesData:
    spec = SERIES_CATALOG[key]
    # 월별 시리즈 + yoy 계산을 위해 최소 400일은 끌어와야 12개월 전 값을 잡을 수 있음.
    lookback = max(days, 400) if spec["freq"] == "monthly" else max(days, 200)
    end = date.today()
    start = end - timedelta(days=lookback)

    sd = SeriesData(key=key, spec=spec)
    try:
        if use_fredapi:
            sd.observations = _fetch_via_fredapi(spec, start, end, api_key)
        else:
            sd.observations = _fetch_via_rest(spec, start, end, api_key)
    except MacroFetchError as e:
        sd.error = str(e)
    except Exception as e:  # noqa: BLE001 - 사용자 친화 메시지로 감싼다
        sd.error = f"{type(e).__name__}: {e}"
    return sd


def _has_fredapi() -> bool:
    try:
        import fredapi  # noqa: F401
        return True
    except ImportError:
        return False


def fetch_series(keys: list[str], days: int = 365) -> list[SeriesData]:
    """선택한 시리즈를 fetch.

    fredapi 설치 시 그걸 쓰고, 없으면 REST 폴백. 어느 쪽이든 동일 dataclass 반환.
    개별 시리즈 fetch 실패는 SeriesData.error에 기록하고 계속 진행
    (12종 중 1개가 죽어도 나머지는 살려둠).

    Raises:
        MacroFetchError: API key 부재 등 *전체* fetch 불가 사유.
    """
    api_key = _require_api_key()
    use_fredapi = _has_fredapi()

    if not use_fredapi:
        sys.stderr.write(
            "[macro_us] fredapi not installed — using requests REST fallback. "
            "`pip install fredapi` 하면 더 빠름.\n"
        )

    results: list[SeriesData] = []
    for i, key in enumerate(keys):
        sd = _fetch_one(key, days, api_key, use_fredapi)
        if sd.error:
            sys.stderr.write(f"[macro_us] {key} ({sd.spec['fred_id']}) failed: {sd.error}\n")
        else:
            sys.stderr.write(
                f"[macro_us] {key} ({sd.spec['fred_id']}): {len(sd.observations)} obs\n"
            )
        results.append(sd)
        if i < len(keys) - 1:
            time.sleep(RATE_LIMIT_SLEEP)
    return results
