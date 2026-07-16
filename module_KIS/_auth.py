# FILE: research_Mvp/module_kis/_auth.py
"""한국투자증권(KIS) Open API 설정 로딩 + OAuth2 접근토큰 발급/캐시.

KIS 접근토큰(access_token)은 발급 후 24시간 유효하지만, KIS가 토큰 재발급을
분당 1회 수준으로 제한한다. 너무 자주 /oauth2/tokenP 를 때리면
'EGW00133 접근토큰 발급 잠시 후 다시 시도' 류 에러로 막힌다.
→ 토큰은 반드시 디스크에 캐시하고 만료 직전까지 재사용한다.

환경변수:
    KIS_APP_KEY      (필수) 앱키
    KIS_APP_SECRET   (필수) 앱시크릿
    KIS_ENV          prod(실전, 기본) | vps(모의투자)
    KIS_CUST_TYPE    P(개인, 기본) | B(법인)
    KIS_TOKEN_CACHE  (옵션) 토큰 캐시 파일 경로. 기본 <프로젝트루트>/.kis_token_cache.json

발급: https://apiportal.koreainvestment.com 에서 앱키/시크릿 신청.
모의투자는 별도 모의 앱키가 필요하다(실전 키와 다름).
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests

# 도메인 — 실전과 모의가 호스트/포트 모두 다르다.
_BASE_PROD = "https://openapi.koreainvestment.com:9443"
_BASE_VPS = "https://openapivts.koreainvestment.com:29443"

# 만료 이 시간(초) 전이면 캐시를 버리고 재발급. 토큰 24h 유효 → 10분 여유.
_REFRESH_MARGIN = 600


class KisError(RuntimeError):
    """KIS API 호출의 사용자-친화 에러 (인증·요청 공통)."""


@dataclass
class KisConfig:
    app_key: str
    app_secret: str
    env: str           # "prod" | "vps"
    cust_type: str     # "P" | "B"
    base_url: str
    token_cache: Path
    account_no: str = ""   # "12345678-01" 형태(계좌엔드포인트 전용, 시세조회엔 불필요)

    @property
    def is_paper(self) -> bool:
        return self.env == "vps"

    @property
    def cano(self) -> str:
        """종합계좌번호 앞 8자리(CANO). 계좌번호의 숫자만 추려 앞 8자리."""
        digits = "".join(c for c in self.account_no if c.isdigit())
        return digits[:8]

    @property
    def acnt_prdt_cd(self) -> str:
        """계좌상품코드 뒤 2자리(ACNT_PRDT_CD). 없으면 기본 '01'."""
        digits = "".join(c for c in self.account_no if c.isdigit())
        return digits[8:10] if len(digits) >= 10 else "01"

    def require_account(self) -> None:
        """계좌 엔드포인트 호출 전 계좌번호 유효성 가드."""
        if len(self.cano) < 8:
            raise KisError(
                "KIS_ACCOUNT_NO 환경변수가 필요합니다(잔고/계좌 조회용). "
                "'12345678-01' 형태(종합계좌 8자리-상품코드 2자리)로 .env 에 설정하세요. "
                "한국투자 앱/HTS 계좌번호에서 확인 가능."
            )


def _project_root() -> Path:
    """module_kis 의 부모(=research_Mvp)를 프로젝트 루트로 본다."""
    return Path(__file__).resolve().parent.parent


def load_config() -> KisConfig:
    """환경변수에서 KIS 설정을 읽어 KisConfig 로 만든다.

    KIS_APP_KEY / KIS_APP_SECRET 가 없으면 친절한 안내와 함께 KisError.
    """
    app_key = os.environ.get("KIS_APP_KEY", "").strip()
    app_secret = os.environ.get("KIS_APP_SECRET", "").strip()
    if not app_key or not app_secret:
        raise KisError(
            "KIS_APP_KEY / KIS_APP_SECRET 환경변수가 필요합니다. "
            "https://apiportal.koreainvestment.com 에서 앱키/시크릿 발급 후 "
            ".env 또는 셸에 설정하세요. (모의투자는 모의용 키가 따로 필요)"
        )

    env = os.environ.get("KIS_ENV", "prod").strip().lower()
    if env not in ("prod", "vps"):
        raise KisError(f"KIS_ENV 는 prod 또는 vps 여야 합니다 (받은 값: {env!r}).")

    cust_type = os.environ.get("KIS_CUST_TYPE", "P").strip().upper()
    base_url = _BASE_VPS if env == "vps" else _BASE_PROD

    cache_override = os.environ.get("KIS_TOKEN_CACHE", "").strip()
    token_cache = (
        Path(cache_override)
        if cache_override
        else _project_root() / ".kis_token_cache.json"
    )

    account_no = os.environ.get("KIS_ACCOUNT_NO", "").strip()

    return KisConfig(
        app_key=app_key,
        app_secret=app_secret,
        env=env,
        cust_type=cust_type,
        base_url=base_url,
        token_cache=token_cache,
        account_no=account_no,
    )


# ── 토큰 캐시 ────────────────────────────────────────────────────────

def _cache_key(cfg: KisConfig) -> str:
    """앱키+환경 조합을 해시해 캐시 슬롯 키로 쓴다(실전/모의 토큰 분리)."""
    raw = f"{cfg.env}:{cfg.app_key}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


def _read_cache(cfg: KisConfig) -> Optional[dict]:
    p = cfg.token_cache
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None
    slot = data.get(_cache_key(cfg))
    if not slot:
        return None
    if float(slot.get("expires_at", 0)) - _REFRESH_MARGIN <= time.time():
        return None  # 만료(임박) → 무효
    return slot


def _write_cache(cfg: KisConfig, token: str, expires_at: float) -> None:
    p = cfg.token_cache
    data: dict = {}
    if p.exists():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            data = {}
    data[_cache_key(cfg)] = {
        "access_token": token,
        "expires_at": expires_at,
        "env": cfg.env,
        "issued_at": time.time(),
    }
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass  # 캐시 쓰기 실패는 치명적이지 않음 — 다음 호출에 재발급될 뿐.


def _parse_expiry(body: dict) -> float:
    """응답에서 만료 epoch(초)를 뽑는다.

    KIS는 access_token_token_expired('2026-06-25 23:59:59')와
    expires_in(초)을 함께 준다. expires_in 우선, 없으면 문자열 파싱, 둘 다 실패 시 23h.
    """
    exp_in = body.get("expires_in")
    if exp_in is not None:
        try:
            return time.time() + float(exp_in)
        except (TypeError, ValueError):
            pass
    exp_str = body.get("access_token_token_expired")
    if exp_str:
        try:
            dt = datetime.strptime(exp_str, "%Y-%m-%d %H:%M:%S")
            return dt.timestamp()
        except Exception:
            pass
    return time.time() + 23 * 3600


def get_access_token(cfg: Optional[KisConfig] = None, *, force: bool = False) -> str:
    """유효한 Bearer 접근토큰을 반환한다. 캐시 우선, 없으면 발급.

    Args:
        cfg: 설정. None 이면 load_config().
        force: True 면 캐시를 무시하고 강제 재발급(만료/오류 복구용).

    Raises:
        KisError: 발급 실패(잘못된 키, rate limit 등).
    """
    cfg = cfg or load_config()

    if not force:
        cached = _read_cache(cfg)
        if cached:
            return cached["access_token"]

    url = f"{cfg.base_url}/oauth2/tokenP"
    payload = {
        "grant_type": "client_credentials",
        "appkey": cfg.app_key,
        "appsecret": cfg.app_secret,
    }
    try:
        r = requests.post(url, json=payload, timeout=15)
    except requests.RequestException as e:
        raise KisError(f"토큰 발급 요청 실패: {type(e).__name__}: {e}") from e

    try:
        body = r.json()
    except ValueError:
        raise KisError(f"토큰 발급 응답이 JSON 아님 (HTTP {r.status_code}): {r.text[:200]}")

    token = body.get("access_token")
    if not token:
        # KIS는 에러 시 error_code/error_description 또는 msg_cd/msg1 을 준다.
        code = body.get("error_code") or body.get("msg_cd") or r.status_code
        msg = body.get("error_description") or body.get("msg1") or r.text[:200]
        raise KisError(f"토큰 발급 실패 [{code}]: {msg}")

    expires_at = _parse_expiry(body)
    _write_cache(cfg, token, expires_at)
    return token
