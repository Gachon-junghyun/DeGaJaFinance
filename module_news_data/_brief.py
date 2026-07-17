# -*- coding: utf-8 -*-
"""하루 뉴스 브리핑 — 파이썬이 전수를 읽고, LLM 이 읽을 수 있는 크기로 **계층화**해 넘긴다.

이 모듈이 푸는 문제는 하나다: **하루 4,279건을 LLM 이 다 읽을 수 없는데, 다 알아야 한다.**
  · 본문 전부 = 4,101k 토큰 (컨텍스트 20~28배 초과, 불가능)
  · 제목 전부 = 146k 토큰 (들어는 가지만 무의미 — 4,279줄을 나열해봐야 세지도 비교하지도 못한다)
  · 이 브리핑  = ~17k 토큰 (사건 단위 + 계층 + 분모)

해법은 "다 읽게 한다"가 아니라 **"다 읽었다고 말할 수 있게 한다"**. 파이썬이 100% 를 읽고,
LLM 에겐 (a)분모 (b)중요한 것의 근거 (c)나머지의 무작위 표본을 준다. 그러면 LLM 은 4,279건을
읽지 않고도 "오늘 시장 사건 396개 중 한화오션은 54건·9매체이고 근거는 이렇다"고 말할 수 있고,
그 문장의 모든 숫자가 검증 가능하다(P4).

계층 경계는 **매체수**다 — 몇 개 편집국이 독립적으로 "이건 뉴스다"라고 판정했나. 우리가 정한
규칙이 아니라 시장의 판정을 빌려온 것. 실측 분포(2026-07-07 국내 시장사건 396개):
    9매체 1 · 8매체 4 · 7매체 8 · 6매체 24 · 5매체 24 | 4매체 43 · 3매체 102 | 2매체 190
꼬리(2매체)의 절반은 부동산 실거래 자동기사·정례 지표표·시상식 포토라 읽어서 얻을 게 없다.

⚠ **꼬리를 자르지 않고 '표본+분모'로 준다.** 매체수는 중요도의 좋은 대리지표지 진실이 아니다 —
꼬리에도 "한-싱가포르 FTA 개선협상"·"롯데건설 성수4지구 시공사 선정" 같은 진짜가 섞여 있다.
그래서 "190개 있고 무작위 10개는 이렇다"고 말해준다. LLM 이 못 본 게 있다는 걸 알아야
드릴다운을 할 수 있다(`blindspot` 이 원래 하던 일과 같은 원리).

⚠ 판정하지 않는다(P4). 호재/악재를 여기서 안 정한다 — 실측으로 7/07 한화오션 [54건/9매체]는
**수주가 아니라 탈락**이었다. 방향은 본문을 읽어야 아는데, 그 본문이 지금 못 쓸 상태다
(아래 `LEDE_DEFAULT` 참조). 그래서 지금 브리핑은 "무슨 일이 몇 건/몇 매체로 있었나"까지만
말하고 **방향은 말하지 않는다**. 방향까지 주려면 스크래퍼 수정이 선행돼야 한다.

⚠ 클라이언트 전용(`_cluster` 가 GPU 벡터를 쓴다). 서버는 이 파일을 import 만 하고 실행 안 한다.

사용:
    python -m module_news_data brief --date 2026-07-07 --scope domestic
    python -m module_news_data brief --date 2026-07-07 --json      # LLM 에 먹일 형태
"""
from __future__ import annotations

import json
import random
from datetime import date as _date

from ._classify import applies_to, train
from ._cluster import cluster_day
from ._config import OUT_DIR, utf8_stdout
from ._export import ledes

BRIEF_OUT = OUT_DIR / "news_brief"

HEAD_SOURCES = 5    # 이 이상 = 머리(근거 3건). 실측 61개
BODY_SOURCES = 3    # 이 이상 = 몸통(제목 한 줄). 실측 145개
TAIL_SAMPLE = 10    # 꼬리는 세고 무작위 표본만 — 자르는 게 아니다(위 ⚠)

# ⚠ **리드는 기본 OFF**(`--lede` 로만 켠다). 머리층에 본문 앞머리를 붙이면 방향(호재/악재)이
# 보여서 원래 이 브리핑의 핵심이었는데, 본문이 못 쓸 상태다:
#   · asiae·sedaily 는 본문 앞 400자가 **100%** 페이지 가구('함께 보면 좋은 기사' 목록 등)
#   · 그 결과 리드의 **22%가 그 사건과 무관한 기사**였다(실측). 서킷브레이커 사건의 근거로
#     "푸드나무 200억 유상증자"가 붙는 식 — LLM 이 사건을 통째로 오독한다.
#   · 가구 제거 규칙을 넣어봤으나 오히려 멀쩡한 리드를 떨어뜨려 오염률이 27%로 올랐다.
# 틀린 리드는 없는 리드보다 나쁘다(P4: 지어내지 않는다). 스크래퍼가 고쳐지면 기본 ON 으로.
LEDE_DEFAULT = False


def build(day: str, scope: str = "domestic", head_min: int = HEAD_SOURCES,
          body_min: int = BODY_SOURCES, tail_sample: int = TAIL_SAMPLE,
          with_lede: bool = LEDE_DEFAULT) -> dict:
    """하루 → 계층 브리핑. 판정 없음 — 세고 묶고 근거만 붙인다."""
    cl = cluster_day(day, scope)
    events = cl.get("events", [])
    model = train()

    # ⚠ 분류기는 **국내 기사에만** 쓴다(사건별 판정 — scope 로 게이트하면 `all` 안의 영어가
    # 통째로 잘린다). 해외 사건은 그냥 통과시킨다: 한글로 학습한 모델이라 영어는 점수가 0
    # 근처에 뭉쳐 무의미하고("Oil Surges as US Strikes Iran" 이 -0.5 로 잘렸다), 애초에
    # 해외 피드는 82% 가 금융이라(yahoo_finance·seekingalpha·bloomberg…) 걸러줄 게 없다.
    market, nonmarket = [], []
    for e in events:
        e = dict(e)
        if applies_to(e.get("sources") or []):
            e["nb"] = round(model.score(e["title"]), 1)
            (market if e["nb"] > 0 else nonmarket).append(e)
        else:
            e["nb"] = None          # 판정 안 함 — 0 이나 점수로 채우면 거짓말이 된다(P4)
            market.append(e)

    head = [e for e in market if e["n_sources"] >= head_min]
    body = [e for e in market if body_min <= e["n_sources"] < head_min]
    tail = [e for e in market if e["n_sources"] < body_min]

    # 머리층에만 본문 리드 — 방향(호재/악재)이 거기 있다. 필요한 것만 지목해 받는다.
    if with_lede and head:
        want = [x["url_hash"] for e in head for x in e["evidence"]]
        try:
            got = ledes(want)
        except RuntimeError:
            got = {}     # 리드 못 받아도 브리핑은 낸다 — 없으면 없다고 표시(지어내지 않는다)
        for e in head:
            for x in e["evidence"]:
                x["lede"] = got.get(x["url_hash"])

    rng = random.Random(day)   # 일내 재현, 일별 회전
    sample = rng.sample(tail, min(tail_sample, len(tail))) if tail else []

    return {
        "date": day, "scope": scope,
        "denominator": {
            "articles": cl.get("n_articles", 0),
            "clusters": cl.get("n_clusters", 0),
            "events_2src_plus": len(events),
            "market_events": len(market),
            "nonmarket_events": len(nonmarket),
        },
        "tiers": {"head_min_sources": head_min, "body_min_sources": body_min},
        "head": head,
        "body": [{"title": e["title"], "n_articles": e["n_articles"],
                  "n_sources": e["n_sources"], "nb": e["nb"]} for e in body],
        "tail": {"count": len(tail), "shown": len(sample),
                 "note": "매체 2개 이하 — 세기만 하고 무작위 표본만 보여준다(자른 게 아니다)",
                 "sample": [{"title": e["title"], "n_articles": e["n_articles"]}
                            for e in sample]},
        "excluded_nonmarket": {
            "count": len(nonmarket),
            "note": "분류기가 비시장으로 본 사건(스포츠·연예·날씨 등). 오분류 10~14%(LOSO 기준)",
            "sample": [{"title": e["title"], "n_sources": e["n_sources"], "nb": e["nb"]}
                       for e in nonmarket[:5]],
        },
    }


def run(day: str | None, scope: str, head_min: int, body_min: int, as_json: bool,
        with_lede: bool = LEDE_DEFAULT) -> None:
    utf8_stdout()
    day = day or _date.today().strftime("%Y-%m-%d")
    b = build(day, scope, head_min, body_min, with_lede=with_lede)
    d = b["denominator"]

    if as_json:
        BRIEF_OUT.mkdir(parents=True, exist_ok=True)
        fp = BRIEF_OUT / f"{day}_{scope}.json"
        txt = json.dumps(b, ensure_ascii=False, separators=(",", ":"))
        fp.write_text(txt, encoding="utf-8")
        print(json.dumps({"date": b["date"], "scope": b["scope"], "denominator": d,
                          "head": len(b["head"]), "body": len(b["body"]),
                          "tail": b["tail"]["count"], "bytes": len(txt),
                          "approx_tokens": int(len(txt) * 0.7)},
                         ensure_ascii=False, indent=2))
        print(f"\n(전체 → {fp})")
        return

    sc = {"all": "국내+해외", "foreign": "해외만", "domestic": "국내만"}[scope]
    print(f"\n# 뉴스 브리핑 — {day} [{sc}]")
    print(f"  기사 {d['articles']:,}건 → 사건 {d['events_2src_plus']}개 "
          f"→ 시장 {d['market_events']}개 (비시장 {d['nonmarket_events']}개 제외)")

    print(f"\n  ══ 머리 ({head_min}개 매체 이상) — {len(b['head'])}개. 오늘의 뉴스 ══")
    for e in b["head"]:
        print(f"\n  [{e['n_articles']:>3}건/{e['n_sources']}매체 분산{e['src_entropy']:.2f}] {e['title'][:60]}")
        lede = next((x.get("lede") for x in e["evidence"] if x.get("lede")), None)
        if lede:
            print(f"      {lede[:110]}")

    print(f"\n  ══ 몸통 ({body_min}~{head_min-1}개 매체) — {len(b['body'])}개 ══")
    for e in b["body"][:30]:
        print(f"   [{e['n_articles']:>3}건/{e['n_sources']}매체] {e['title'][:62]}")
    if len(b["body"]) > 30:
        print(f"   … 외 {len(b['body'])-30}개 (--json 에 전부)")

    t = b["tail"]
    print(f"\n  ══ 꼬리 (2매체) — {t['count']}개. 세기만 하고 표본만 ══")
    for e in t["sample"]:
        print(f"   [{e['n_articles']:>3}건] {e['title'][:62]}")
    print(f"\n  ⚠ 꼬리 {t['count']}개는 자른 게 아니라 표본만 보여준 것 — 진짜가 섞여 있을 수 있다.")
    print(f"  ⚠ 비시장 {d['nonmarket_events']}개 제외 — 분류기 오분류 10~14%(LOSO).")
    print(f"  ⚠ 판정 아님 — 호재/악재는 리드를 읽어야 안다.")


def cli_register(sub) -> None:
    p = sub.add_parser("brief", help="하루 → 계층 브리핑(머리/몸통/꼬리+분모). 클라 전용")
    p.add_argument("--date", default=None, help="market_day YYYY-MM-DD (기본: 오늘)")
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="domestic")
    p.add_argument("--head", type=int, default=HEAD_SOURCES, dest="head_min",
                   help=f"머리층 최소 매체수(기본 {HEAD_SOURCES})")
    p.add_argument("--body", type=int, default=BODY_SOURCES, dest="body_min",
                   help=f"몸통층 최소 매체수(기본 {BODY_SOURCES})")
    p.add_argument("--lede", action="store_true", dest="with_lede",
                   help="머리층에 본문 리드 (⚠ 기본 OFF — 본문 22%%가 사건과 무관, 스크래퍼 버그)")
    p.add_argument("--json", action="store_true", help="LLM 에 먹일 형태(compact)")
    p.set_defaults(func=lambda a: run(a.date, a.scope, a.head_min, a.body_min, a.json,
                                      a.with_lede))
