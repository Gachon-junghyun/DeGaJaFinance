# -*- coding: utf-8 -*-
"""시간축 정규화 — published_at(발행시각) → UTC 의 **단일 원본** (CLAUDE.md P1).

수집시각(fetched_at)은 '언제 내 DB에 들어왔나'지 '언제 일어났나'가 아니다. 수집이
밀렸다 몰리면(밤 공백 → 아침 catch-up) 사흘치 기사가 한 시각에 뭉쳐 들어와, 그대로
일별 비닝하면 **수집 공백이 가짜 뉴스 스파이크로 둔갑**한다. 서사의 시계열을 재려면
축은 반드시 published_at 이어야 한다.

published_at 은 소스마다 포맷이 다르다(실측 5계열):
  ① RFC2822 + 숫자 오프셋   'Tue, 02 Jun 2026 00:28:00 +0900'   (대다수 · 1자리 일자도 있음)
  ② RFC2822 + GMT           'Tue, 02 Jun 2026 00:14:00 GMT'     (google_kr·bloomberg)
  ③ RFC2822 + Z             'Tue, 02 Jun 2026 00:53:46 Z'       (fxstreet — RFC2822 비표준)
  ④ RFC2822 + 콜론 오프셋   'Mon, 01 Jun 2026 04:00:00 +09:00'  (mk — RFC2822 비표준)
  ⑤ ISO8601                 '2026-05-26T10:07:41-04:00'         (sec_edgar)

⚠ ④가 이 파일이 존재하는 이유다. stdlib `parsedate_to_datetime` 은 콜론 오프셋에서
**예외를 안 내고 tzinfo=None 인 naive datetime 을 조용히 돌려준다**(오프셋을 통째로 버림).
그걸 UTC로 간주하면 mk 기사가 9시간 밀린 채 소리없이 섞인다. 그래서 콜론을 먼저 지운다.

⚠ 시각을 **지어내지 않는다**(P4). 파싱 실패·타임존 불명이면 None — 호출부가 '빈칸'으로
처리하고 분모에서 빼야지, 그럴듯한 값으로 채우면 안 된다.

⚠ published_at 은 2026-05 이전 수집분에 없다(실측: 2026-03 100% 빈값, 2026-04 95%,
2026-05부터 0%). 즉 이 축의 실질 시작점은 **2026-05-01**. 그 이전 구간의 baseline 을
published_at 으로 잡으면 표본이 통째로 비니, 윈도우를 그 뒤로 두거나 fetched_at 로
명시적으로 폴백해야 한다(`PUBLISHED_AT_SINCE` 참조).
"""
from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

from ._config import origin_tag

# published_at 이 신뢰 가능한 최초 시점(실측). 이 앞 구간은 축으로 쓸 수 없다.
PUBLISHED_AT_SINCE = "2026-05-01"

# 국내 기사의 일자 기준. KST 는 서머타임이 없어 고정 오프셋으로 정확하다.
KST = timezone(timedelta(hours=9))

# 'DD:DD:DD +09:00' → 'DD:DD:DD +0900' (RFC2822 는 콜론 없는 4자리 오프셋만 안다)
_COLON_OFFSET = re.compile(r"([+-]\d{2}):(\d{2})\s*$")

# 'DD:DD:DD Z' → 'DD:DD:DD +0000' (RFC2822 에 Z 는 없다 — fxstreet 방언)
_TRAILING_Z = re.compile(r"\s+Z\s*$")


def parse_published(raw: str | None) -> datetime | None:
    """발행시각 문자열 → **tz-aware UTC** datetime. 못 믿으면 None.

    None 을 돌려주는 경우(전부 '모른다'는 뜻 — 추측값으로 메우지 않는다):
      · 빈 값 (2026-05 이전 수집분)
      · 어떤 계열로도 파싱 실패
      · 파싱은 됐지만 타임존이 없어 절대시각을 확정할 수 없음
    """
    if not raw:
        return None
    s = raw.strip()
    if not s:
        return None

    # ④ 콜론 오프셋을 먼저 정규화 — 안 하면 stdlib 가 조용히 naive 로 떨군다.
    s = _COLON_OFFSET.sub(r"\1\2", s)
    # ③ 비표준 트레일링 Z → 명시적 +0000.
    s = _TRAILING_Z.sub(" +0000", s)

    dt: datetime | None = None

    # ①②③④ RFC2822 계열 (쉼표+요일이 있으면 이쪽)
    if "," in s:
        try:
            dt = parsedate_to_datetime(s)
        except (TypeError, ValueError):
            dt = None

    # ⑤ ISO8601 계열
    if dt is None:
        try:
            dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            dt = None

    if dt is None:
        return None

    # 타임존을 확정 못 했으면 절대시각을 모르는 것 — 지어내지 않는다.
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        return None

    return dt.astimezone(timezone.utc)


def utc_day(raw: str | None) -> str | None:
    """발행시각 → UTC 일자 'YYYY-MM-DD' (일별 비닝의 단일 원본). 못 믿으면 None."""
    dt = parse_published(raw)
    return dt.strftime("%Y-%m-%d") if dt else None


def utc_hour(raw: str | None) -> str | None:
    """발행시각 → UTC 시각 'YYYY-MM-DDTHH' (시간별 비닝). 못 믿으면 None."""
    dt = parse_published(raw)
    return dt.strftime("%Y-%m-%dT%H") if dt else None


def market_day(raw: str | None, source: str | None) -> str | None:
    """발행시각 → **그 기사 시장의 현지 일자** 'YYYY-MM-DD'. 일별 비닝은 이걸 쓴다.

    왜 UTC 가 아닌가: 한국 기사 아침 08:00 KST 는 UTC 로 전날 23:00 이라, UTC 일자로
    세면 **아침 뉴스가 통째로 전날 칸에 쌓인다**(실측: 국내 73,506건 중 16,174건 = 22.0%).
    서사를 거래일과 붙여 읽는 게 목적이므로 일자는 시장 현지 기준이어야 한다.

    타임존은 `scope` 가 아니라 **기사 소스별**로 정한다 — scope=foreign 은 BBC(영국)·
    SCMP(홍콩)·bloomberg(글로벌)가 섞인 잡탕이라 단일 현지시각이 없다. 소스 국적 판정은
    `_config.origin_tag` 재사용(P1 — 여기서 다시 정의하지 않는다):
      · KR 소스 → KST(+9). 서머타임 없음 → 고정 오프셋으로 정확.
      · EN 소스 → UTC. 여러 나라가 섞여 단일 현지시각이 없으니 절대축을 쓴다.
        (US 전용 분석에 ET 일자가 필요해지면 그때 소스별 tz 표를 여기 추가한다.)
    """
    dt = parse_published(raw)
    if dt is None:
        return None
    if origin_tag(source) == "KR":
        return dt.astimezone(KST).strftime("%Y-%m-%d")
    return dt.strftime("%Y-%m-%d")
