# -*- coding: utf-8 -*-
"""제목 벌크 반출 — 서버(수집) → 클라이언트(임베딩·클러스터)의 증분 동기화 통로.

왜 있나: 임베딩·사건 클러스터링은 GPU 가 필요해 **클라이언트(고사양 PC)** 에서 돌고,
뉴스 DB 는 **서버(24시간 수집, 저사양)** 가 소유한다. 그런데 기존 조회 서브커맨드는
'검색 결과 몇 건'을 사람이 읽는 텍스트로 돌려줄 뿐이라, 하루 4천건·30일 12만건을
기계가 받아 벡터로 만드는 용도엔 맞지 않는다. 이 명령이 그 통로다.

전송은 새 엔드포인트를 만들지 않는다(P1) — `DB_READ_CMDS` 에 등록돼 있으므로
`DEGAJA_NEWS_API` 만 켜면 `__main__` 이 argv 를 서버 `/exec` 로 넘기고 서버가 자기 DB 로
실행해 stdout(JSON)을 돌려준다. 서버 코드 추가 0.

⚠ 커서는 **`fetched_at`**(서버가 받은 시각)이지 `published_at`(발행시각)이 아니다.
발행시각은 소급 기사(며칠 전 것이 지금 들어옴) 때문에 단조증가가 아니라서, 그걸 커서로
쓰면 밀린 기사를 영영 못 받는다. 수집순서만 단조증가한다.
  · 클라이언트는 받은 것 중 max(fetched_at)을 저장 → 다음엔 `--since <그 값>`.
  · 경계는 배타(`>`)라 같은 건 두 번 안 받는다. 그래도 소비 측은 url_hash 로 멱등해야 한다
    (같은 초에 여러 건이 들어오면 잘릴 수 있다 — 그래서 `--since` 는 초 단위가 아니라
    저장된 원본 문자열 그대로 넘긴다).

⚠ 크기: 30일 전량이면 ~12만행(약 13MB) → `/exec` 의 JSON 문자열 안에 들어가 더 커진다.
반드시 `--count` 로 먼저 크기를 보고, 처음 한 번만 통째로 받고 그 뒤엔 증분(하루 ~430KB)으로.

사용:
    python -m module_news_data export --count --since 2026-07-01           # 몇 건인지만
    python -m module_news_data export --since 2026-07-16T09:00:00.000000   # 증분 반출
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys

from ._config import NEWS_API_BASE, NEWS_DB, utf8_stdout

PULL_TIMEOUT = 600   # 대량 반출 — `__main__.REMOTE_TIMEOUT` 과 같은 뜻(그쪽은 CLI 라우팅용)

# 전송량을 줄이려고 짧은 키를 쓴다(12만행 × 키 길이가 그대로 MB 가 된다).
#   h=url_hash · p=published_at · s=source · t=title · u=url · f=fetched_at(커서용, 행엔 없음)
# url 을 싣는 이유 둘: ①근거 링크(LLM/사람에게 url_hash 는 아무 쓸모가 없다) ②섹션 라벨
# (`mt.co.kr/politics/`·`chosun.com/entertainment/` — 분류기 학습셋이 여기서 공짜로 나온다).
# 비용은 행당 ~60B(전량 +14MB, 하루 +260KB) — 그만한 값을 한다.
_SQL = (
    "SELECT url_hash, published_at, source, title, url, fetched_at FROM seen_news "
    "WHERE title IS NOT NULL AND title != ''"
)


LEDE_CHARS = 220   # 본문 앞머리만. 뒤쪽은 스크래퍼가 사이드바를 섞어놨다(asiae 55.6%) — `_burst` ⚠

# ⚠ **앞머리도 안전하지 않다.** "리드는 사이드바 오염 전 구간"이라 여겼다가 실측에 깨졌다 —
# asiae·sedaily 는 본문 앞 400자가 **100%** 페이지 가구('함께 보면 좋은 기사' 목록, '뉴스 듣기
# 글자 크기 기사 공유' 툴바)로 시작한다(나머지 신문은 0% — 두 곳의 스크래퍼 셀렉터 문제).
# 그대로 두면 서킷브레이커 사건의 근거로 엉뚱한 기사 제목이 붙어 **LLM 이 오독한다**(실측 오염률 22%).
# 근본 수정은 스크래퍼 쪽이고, 여기선 가구를 잘라내고 **못 자르면 리드를 안 준다**(빈칸이 거짓보다 낫다).
_FURNITURE = re.compile(
    r"^.*?(?:함께\s*보면\s*좋은\s*기사|뉴스\s*듣기|글자\s*크기|기사\s*공유)\s*", re.S)
_FURNITURE_MARK = ("함께 보면 좋은 기사", "뉴스 듣기", "글자 크기", "기사 공유")


def _clean_lede(body: str | None) -> str | None:
    """페이지 가구를 잘라낸 리드. 잘라도 가구가 남거나 너무 짧으면 **None**(지어내지 않는다)."""
    if not body:
        return None
    txt = " ".join(body.split())
    if any(k in txt[:200] for k in _FURNITURE_MARK):
        txt = _FURNITURE.sub("", txt, count=1)
        # 가구 목록이 여러 겹인 경우가 있어 한 번 더
        if any(k in txt[:200] for k in _FURNITURE_MARK):
            txt = _FURNITURE.sub("", txt, count=1)
    txt = txt.strip()
    if len(txt) < 60 or any(k in txt[:120] for k in _FURNITURE_MARK):
        return None
    return txt[:LEDE_CHARS]


def _where(since: str | None, params: list) -> str:
    if since:
        params.append(since)
        return _SQL + " AND fetched_at > ?"      # 배타 — 같은 건 두 번 안 받는다
    return _SQL


def ledes(hashes: list[str]) -> dict[str, str]:
    """**지목한 기사만** 본문 리드를 준다. 브리핑이 머리 층에만 붙이는 용도(~180건).

    전량 반출에 본문을 실으면 60MB 가 되지만, 실제로 필요한 건 보여줄 사건의 근거뿐이다.
    ⚠ 앞 220자만 — 그 뒤는 사이트 사이드바가 섞여 있다(다른 기사 제목이 본문인 척한다).
    """
    if not hashes:
        return {}
    if NEWS_API_BASE:
        out: dict[str, str] = {}
        for i in range(0, len(hashes), 50):     # URL 길이 제한 — 나눠 부른다
            chunk = hashes[i:i + 50]
            from ._api_client import exec_remote
            res = exec_remote(NEWS_API_BASE, ["export", "--hashes", ",".join(chunk)],
                              timeout=PULL_TIMEOUT)
            if res.get("error"):
                raise RuntimeError(f"원격 리드 반출 실패: {res['error']}")
            out.update(json.loads(res.get("stdout", "{}").strip()))
        return out
    return _ledes_local(hashes)


def _ledes_local(hashes: list[str]) -> dict[str, str]:
    con = sqlite3.connect(f"file:{NEWS_DB}?mode=ro", uri=True)
    ph = ",".join("?" * len(hashes))
    # 가구를 잘라내려면 원문을 넉넉히 읽어야 한다(자른 뒤 220자를 남긴다).
    rows = con.execute(
        f"SELECT url_hash, substr(body,1,1200) FROM article_contents "
        f"WHERE url_hash IN ({ph})", hashes).fetchall()
    con.close()
    out = {}
    for h, b in rows:
        cl = _clean_lede(b)
        if cl:
            out[h] = cl
    return out


def query(since: str | None, limit: int | None = None) -> dict:
    """**로컬 DB** 에서 직접 읽는다(= 서버 자신이 실행하는 몸통). 전송은 모른다."""
    con = sqlite3.connect(f"file:{NEWS_DB}?mode=ro", uri=True)
    p: list = []
    q = _where(since, p) + " ORDER BY fetched_at"
    if limit:
        q += f" LIMIT {int(limit)}"
    rows = []
    mx = since
    for h, pub, src, title, url, fx in con.execute(q, p):
        rows.append({"h": h, "p": pub, "s": src, "t": title, "u": url})
        if fx and (mx is None or fx > mx):
            mx = fx
    con.close()
    return {"rows": rows, "max_fetched": mx, "n": len(rows)}


def pull(since: str | None, limit: int | None = None) -> dict:
    """**클라이언트가 부르는 입구** — 로컬이든 원격이든 같은 결과를 준다.

    `DEGAJA_NEWS_API` 가 켜져 있으면 서버 `/exec` 로 이 CLI 를 실행시켜 그 stdout(JSON)을
    파싱하고, 아니면 로컬 DB 를 직접 읽는다. 소비자(_embed 등)는 이 함수만 부르면 되고
    전송 방식을 몰라도 된다 — 이 분기를 소비자마다 다시 짜면 P1 위반이다.
    """
    if not NEWS_API_BASE:
        return query(since, limit)
    from ._api_client import exec_remote
    argv = ["export"]
    if since:
        argv += ["--since", since]
    if limit:
        argv += ["--limit", str(limit)]
    res = exec_remote(NEWS_API_BASE, argv, timeout=PULL_TIMEOUT)
    if res.get("error"):
        raise RuntimeError(f"원격 반출 실패: {res['error']}")
    try:
        return json.loads(res.get("stdout", "").strip())
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"원격 반출 응답이 JSON 이 아님({exc}) — 서버 코드가 낡았을 수 있다"
                           f"(export 는 서버에도 git pull 필요). 앞부분: "
                           f"{res.get('stdout','')[:200]!r}") from exc


def run(since: str | None, limit: int | None, count_only: bool,
        hashes: str | None = None) -> None:
    utf8_stdout()
    if hashes:
        json.dump(_ledes_local([h for h in hashes.split(",") if h]),
                  sys.stdout, ensure_ascii=False, separators=(",", ":"))
        sys.stdout.write("\n")
        return
    con = sqlite3.connect(f"file:{NEWS_DB}?mode=ro", uri=True)

    if count_only:
        p: list = []
        q = _where(since, p).replace(
            "SELECT url_hash, published_at, source, title, url, fetched_at",
            "SELECT COUNT(*), SUM(LENGTH(title))")
        n, chars = con.execute(q, p).fetchone()
        con.close()
        print(json.dumps({"count": n or 0, "title_chars": chars or 0,
                          "approx_bytes": (chars or 0) + (n or 0) * 90, "since": since},
                         ensure_ascii=False))
        return

    con.close()
    # compact — indent 를 넣으면 12만행에서 수 MB 가 그냥 공백이 된다.
    json.dump(query(since, limit), sys.stdout, ensure_ascii=False, separators=(",", ":"))
    sys.stdout.write("\n")


def cli_register(sub) -> None:
    p = sub.add_parser("export", help="제목 벌크 반출(증분) — 임베딩/클러스터용 기계 소비 전용")
    p.add_argument("--since", default=None,
                   help="이 fetched_at **초과**만(배타). 클라이언트가 저장한 max_fetched 를 그대로 넘겨라")
    p.add_argument("--limit", type=int, default=None, help="안전장치 — 처음 받을 땐 크기 보고 나눠 받기")
    p.add_argument("--count", action="store_true", dest="count_only",
                   help="건수/예상크기만(먼저 이걸로 확인)")
    p.add_argument("--hashes", default=None,
                   help="url_hash 쉼표목록 → 그 기사들의 본문 리드만(브리핑 머리층용)")
    p.set_defaults(func=lambda a: run(a.since, a.limit, a.count_only, a.hashes))
