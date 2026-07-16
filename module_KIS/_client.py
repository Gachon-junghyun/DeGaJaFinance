# FILE: research_Mvp/module_kis/_client.py
"""KIS Open API 조회(GET) 공통 래퍼.

엔드포인트마다 다른 tr_id(거래ID)와 공통 인증헤더(appkey/appsecret/Bearer)를
조립해 GET 호출하고, KIS 응답 규약(rt_cd=='0' 성공)에 따라 정규화한다.

토큰 만료(EGW00123 등)로 401/거부가 나면 한 번 강제 재발급 후 재시도한다.
조회 계열만 다루므로 hashkey(주문 서명)는 필요 없다.
"""
from __future__ import annotations

import time
from typing import Optional

import requests

from ._auth import KisConfig, KisError, get_access_token, load_config

# 조회 rate limit 여유 — 모의는 초당 2건, 실전은 초당 약 20건. 보수적으로 약간 sleep.
RATE_LIMIT_SLEEP = 0.06

# 토큰 만료로 보이는 KIS 메시지 코드(이 경우 강제 재발급 후 1회 재시도).
_TOKEN_EXPIRED_CODES = {"EGW00121", "EGW00123", "EGW00201"}


def _headers(cfg: KisConfig, tr_id: str, token: str, extra: Optional[dict]) -> dict:
    h = {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"Bearer {token}",
        "appkey": cfg.app_key,
        "appsecret": cfg.app_secret,
        "tr_id": tr_id,
        "custtype": cfg.cust_type,
    }
    if extra:
        h.update(extra)
    return h


def kis_get(
    path: str,
    tr_id: str,
    params: dict,
    cfg: Optional[KisConfig] = None,
    *,
    timeout: int = 15,
    extra_headers: Optional[dict] = None,
    return_headers: bool = False,
):
    """KIS 조회 GET 호출. 성공 시 전체 JSON(body) dict 를 반환.

    Args:
        path: '/uapi/...' 로 시작하는 엔드포인트 경로.
        tr_id: 거래ID (엔드포인트별 상수).
        params: FID_* 쿼리 파라미터.
        cfg: 설정. None 이면 load_config().
        extra_headers: 연속조회(tr_cont) 등 추가 헤더.
        return_headers: True 면 (body, 응답헤더 dict) 튜플 반환(연속조회용).

    Raises:
        KisError: 인증/네트워크 실패 또는 rt_cd != '0'.
    """
    cfg = cfg or load_config()
    token = get_access_token(cfg)
    url = f"{cfg.base_url}{path}"

    def _do(tok: str) -> requests.Response:
        return requests.get(
            url,
            headers=_headers(cfg, tr_id, tok, extra_headers),
            params=params,
            timeout=timeout,
        )

    try:
        r = _do(token)
    except requests.RequestException as e:
        raise KisError(f"{tr_id} 요청 실패: {type(e).__name__}: {e}") from e

    body = _safe_json(r)

    # 토큰 만료/거부면 강제 재발급 후 1회 재시도.
    if r.status_code in (401, 403) or body.get("msg_cd") in _TOKEN_EXPIRED_CODES:
        token = get_access_token(cfg, force=True)
        try:
            r = _do(token)
        except requests.RequestException as e:
            raise KisError(f"{tr_id} 재시도 실패: {type(e).__name__}: {e}") from e
        body = _safe_json(r)

    if r.status_code != 200:
        raise KisError(
            f"{tr_id} HTTP {r.status_code}: {body.get('msg1') or r.text[:200]}"
        )

    rt_cd = body.get("rt_cd")
    if rt_cd not in (None, "0"):
        raise KisError(
            f"{tr_id} 실패 [rt_cd={rt_cd} msg_cd={body.get('msg_cd')}]: {body.get('msg1')}"
        )

    time.sleep(RATE_LIMIT_SLEEP)
    if return_headers:
        return body, dict(r.headers)
    return body


def kis_post(
    path: str,
    tr_id: str,
    body: dict,
    cfg: Optional[KisConfig] = None,
    *,
    hashkey: Optional[str] = None,
    timeout: int = 15,
) -> dict:
    """KIS POST 호출(주문/정정/취소 등). 성공 시 JSON body dict.

    주문 계열은 hashkey 서명 헤더가 필요하다(호출부에서 make_hashkey 로 계산해 전달).

    Raises:
        KisError: 인증/네트워크 실패 또는 rt_cd != '0'.
    """
    cfg = cfg or load_config()
    token = get_access_token(cfg)
    url = f"{cfg.base_url}{path}"

    def _do(tok: str) -> requests.Response:
        headers = _headers(cfg, tr_id, tok, None)
        if hashkey:
            headers["hashkey"] = hashkey
        return requests.post(url, headers=headers, json=body, timeout=timeout)

    try:
        r = _do(token)
    except requests.RequestException as e:
        raise KisError(f"{tr_id} POST 실패: {type(e).__name__}: {e}") from e

    resp = _safe_json(r)
    if r.status_code in (401, 403) or resp.get("msg_cd") in _TOKEN_EXPIRED_CODES:
        token = get_access_token(cfg, force=True)
        try:
            r = _do(token)
        except requests.RequestException as e:
            raise KisError(f"{tr_id} 재시도 실패: {type(e).__name__}: {e}") from e
        resp = _safe_json(r)

    if r.status_code != 200:
        raise KisError(f"{tr_id} HTTP {r.status_code}: {resp.get('msg1') or r.text[:200]}")
    if resp.get("rt_cd") not in (None, "0"):
        raise KisError(
            f"{tr_id} 실패 [rt_cd={resp.get('rt_cd')} msg_cd={resp.get('msg_cd')}]: "
            f"{resp.get('msg1')}"
        )
    time.sleep(RATE_LIMIT_SLEEP)
    return resp


def make_hashkey(body: dict, cfg: Optional[KisConfig] = None) -> str:
    """주문 body 를 /uapi/hashkey 로 서명해 hashkey 문자열 반환.

    hashkey 는 요청값 위변조 방지용 서명일 뿐, 호출 자체로 주문이 나가지 않는다.
    """
    cfg = cfg or load_config()
    url = f"{cfg.base_url}/uapi/hashkey"
    headers = {
        "content-type": "application/json; charset=utf-8",
        "appkey": cfg.app_key,
        "appsecret": cfg.app_secret,
    }
    try:
        r = requests.post(url, headers=headers, json=body, timeout=10)
    except requests.RequestException as e:
        raise KisError(f"hashkey 발급 실패: {type(e).__name__}: {e}") from e
    data = _safe_json(r)
    h = data.get("HASH") or data.get("hash")
    if not h:
        raise KisError(f"hashkey 응답에 HASH 없음 (HTTP {r.status_code}): {data}")
    return h


def _safe_json(r: requests.Response) -> dict:
    try:
        out = r.json()
        return out if isinstance(out, dict) else {"_raw": out}
    except ValueError:
        return {"msg1": r.text[:200]}
