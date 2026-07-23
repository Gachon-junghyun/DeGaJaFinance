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

⚠ **그 원칙을 꼬리에만 적용했던 게 이 파일의 오래된 버그였다**(2026-07-23 실측으로 수정).
20% 무작위 표본 대조 — 그날 국내기사의 **45.6%가 브리핑 어디에도 안 나왔다.** 꼬리는 `--body 2`
로 이미 비웠는데도. 새던 곳은 꼬리가 아니라 **아무 표시 없이 사라지던 두 곳**이었다:
  · 1매체 덩어리 638건(35%) — `_cluster` 가 '사건 아님'으로 통째로 버렸다. 그중 330건이
    분류기 기준 시장기사였고, 그날 환율·국고채·한은 코멘트가 전부 거기 있었다 → `single_source`
  · 비시장 66개 중 61개 — `nonmarket[:5]` 가 매체수 상위만 떠서 경계선이 100% 숨었다.
    「이란 핵시설 타격, 美→이스라엘 공습계획 통보」[3매체, nb=−1.2]가 그렇게 잘렸다. 같은 날
    머리엔 "뉴욕증시, 美-이란 긴장에 하락…유가 한 달 최고"가 있었다 → `excluded_nonmarket.band`
셋째로 **한 사건 안에 다른 사건이 숨어 있었다**(토픽 블롭) — 「美 301조 강제노동 관세」44건
안에 국내 「무역위 중국산 부틸아크릴레이트 반덤핑」4건이 삼켜져 한 줄로 붕괴 → `subevents`(`└`).
합쳐서 회수 53.9% → 63.2%, 토큰 14.9k → 22.2k. 남은 것은 전부 **개수로 보고**된다.

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
from ._config import NONMARKET_BAND, OUT_DIR, utf8_stdout
from ._export import ledes

BRIEF_OUT = OUT_DIR / "news_brief"

HEAD_SOURCES = 5    # 이 이상 = 머리(근거 3건). 실측 61개
BODY_SOURCES = 3    # 이 이상 = 몸통(제목 한 줄). 실측 145개
TAIL_SAMPLE = 10    # 꼬리는 세고 무작위 표본만 — 자르는 게 아니다(위 ⚠)

# ── 비시장 경계밴드 (값의 단일 원본은 `_config.NONMARKET_BAND` — 여기는 근거) ────────────
# 예전엔 `nonmarket[:5]` 였다. 사건이 **매체수 내림차순**이라 그 5개는 늘 nb −5~−13,
# 즉 **가장 확실한 사건사고**(화재·조폭·판결)였고, 오분류 위험이 최대인 경계선(nb 0~−3)은
# 100% 숨었다 — 표본으로서 정확히 거꾸로다. 실측 2026-07-23: 그 컷에서 3칸 밀려 잘린 것이
#   「"이란 곡괭이산 비밀 핵시설 타격"…美, 이스라엘에 공습 계획 통보」[3매체/5건, nb=−1.2]
# 이었다. 같은 날 머리에 "뉴욕증시, 美-이란 긴장에 하락…국제유가 한 달 만에 최고"가 있었으니
# **결과는 보여주고 원인을 잘라낸 것**이다. 그래서 컷을 개수가 아니라 **점수 밴드**로 바꾼다.
# 실측 개방폭: nb>−1 → 8개 / nb>−3 → 17개 / nb>−5 → 23개 (전체 비시장 66개). +828 토큰.
# ⚠ `_thread`(주간)도 같은 밴드를 쓴다 — 같은 층의 형제라 서로 import 하지 않고 둘 다
#   `_config` 를 본다(pipeline README: calls go one way, never sideways).

# ── 1매체 층(F2) ─────────────────────────────────────────────────────────
# 매체 2개 미만 덩어리는 `_cluster` 가 '사건 아님'으로 등급을 낮춘다. 맞는 판정이지만
# **안 보여주는 건 다른 문제였다** — 실측 2026-07-23 국내기사의 35%(638건)가 여기 있었고,
# 잡동사니(번역중복·포토·자동기사)를 걷어낸 뒤에도 **330건이 분류기 기준 시장기사**였다.
# 그 안에 그날의 환율·금리 1차 재료가 통째로 있었다:
#   nb=21.8 [외환] 'GDP 서프라이즈·亞통화 강세'에 1,470원선 아래로 급락(상보)
#   nb=23.1 한은 "워시 연준 체제 출범 후 불확실성 확대…장기금리 상승 가능성"
#   nb=13.8 국고채 금리 대체로 상승…3년물 장중 연 3.919%
# 단독보도라 매체수로는 못 거르니 **점수로 거른다**. 실측 비용: nb>15 → 24건/1.7k tok ·
# nb>10 → 68건/4.6k tok · nb>5 → 184건/12k tok. 기본은 10.0 — 매크로 단독기사를 사면서
# 지역행사·인사·홍보는 안 사는 지점.
SINGLES_NB = 10.0
SINGLES_UNSCORED_SAMPLE = 15   # 점수를 못 매기는 층(해외)은 꼬리와 같은 규칙 — 무작위 표본+분모

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
          with_lede: bool = LEDE_DEFAULT, nonmarket_band: float = NONMARKET_BAND,
          singles_nb: float = SINGLES_NB) -> dict:
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

    # ── 비시장: 개수 컷이 아니라 **경계밴드**로 연다(위 NONMARKET_BAND ⚠) ──────
    # 0 에 가까운 순 = 분류기가 가장 덜 확신한 순 = 오분류일 확률이 가장 높은 순.
    band = sorted([e for e in nonmarket if e["nb"] > nonmarket_band],
                  key=lambda e: -e["nb"])

    # ── 1매체 층: 점수로 거른다(위 SINGLES_NB ⚠) ─────────────────────────────
    # ⚠ 분류기는 국내(한글) 전용이다(`_classify.KR_ONLY`). 해외 기사는 점수가 **없지** 낮은 게
    #   아니다 — 그걸 "nb 미달이라 안 보여준다"고 쓰면 US 데스크가 162건을 잡동사니로 읽는다.
    #   점수를 못 매기는 층은 꼬리와 같은 규칙(무작위 표본+분모)으로 준다.
    singles_all = cl.get("singles", [])
    scored, unscored = [], []
    for s in singles_all:
        nb = round(model.score(s["title"]), 1) if applies_to(s.get("source")) else None
        row = {"title": s["title"], "n_articles": s["n_articles"],
               "source": s["source"], "nb": nb}
        if nb is None:
            unscored.append(row)
        elif nb > singles_nb:
            scored.append(row)
    scored.sort(key=lambda s: -s["nb"])
    unscored_sample = (random.Random(day + "|singles")
                       .sample(unscored, min(SINGLES_UNSCORED_SAMPLE, len(unscored)))
                       if unscored else [])

    return {
        "date": day, "scope": scope,
        "denominator": {
            "articles": cl.get("n_articles", 0),
            "clusters": cl.get("n_clusters", 0),
            "events_2src_plus": len(events),
            "market_events": len(market),
            "nonmarket_events": len(nonmarket),
            "subevents_recovered": cl.get("n_subevents", 0),
            "single_source_clusters": cl.get("n_singles", 0),
            # ⚠ 아래는 **모집단에서 뺀 것**이라 위 articles 에 안 들어 있다(분모 정정).
            "excluded_not_news": cl.get("excluded_noise", {}),
        },
        "tiers": {"head_min_sources": head_min, "body_min_sources": body_min,
                  "nonmarket_band": nonmarket_band, "singles_min_nb": singles_nb},
        "head": head,
        "body": [{"title": e["title"], "n_articles": e["n_articles"],
                  "n_sources": e["n_sources"], "nb": e["nb"],
                  **({"subevents": e["subevents"]} if e.get("subevents") else {})}
                 for e in body],
        "tail": {"count": len(tail), "shown": len(sample),
                 "note": "매체 2개 이하 — 세기만 하고 무작위 표본만 보여준다(자른 게 아니다)",
                 "sample": [{"title": e["title"], "n_articles": e["n_articles"]}
                            for e in sample]},
        "single_source": {
            "count": len(singles_all), "shown": len(scored) + len(unscored_sample),
            "min_nb": singles_nb,
            "scored": len(scored), "scorable": len(singles_all) - len(unscored),
            "unscored": len(unscored), "unscored_shown": len(unscored_sample),
            "note": "1개 매체만 다룬 덩어리. 매체수로는 못 걸러지는 환율·금리·채권 단독기사가 "
                    "여기 산다 → 국내는 분류기 점수 상위, 해외는 **점수가 없어**(분류기 한글 전용) "
                    "무작위 표본. 나머지는 개수로만 존재(자른 게 아니다)",
            "sample": scored + unscored_sample,
        },
        "excluded_nonmarket": {
            "count": len(nonmarket), "shown": len(band), "band": nonmarket_band,
            "note": f"분류기가 비시장으로 본 사건(스포츠·연예·날씨 등). 오분류 10~14%(LOSO 기준)"
                    f" — 그래서 경계선(nb>{nonmarket_band})은 전부 보여준다. 0 에 가까울수록 "
                    f"분류기가 덜 확신한 것 = 되짚어야 할 것",
            "sample": [{"title": e["title"], "n_sources": e["n_sources"],
                        "n_articles": e["n_articles"], "nb": e["nb"]} for e in band],
        },
    }


SUB_LINES_SHOWN = 6      # 텍스트 뷰에서 한 사건당 보여줄 하위사건 수. --json 엔 전부


def _sub_lines(e: dict, indent: str) -> None:
    """사건 안에 묻혀 있던 별개 사건. 첫 하위사건은 부모 제목이 이미 대표하므로 건너뛴다.

    ⚠ 텍스트 뷰만 자른다 — 그리고 **자른 개수를 말한다**(이 파일이 꼬리에 쓰는 규칙과 같다).
      실측 2026-07-21 해외: 유가 사건 [79건/18매체] 하나가 하위사건 13개였다(사탕수수·연준·IEA
      비축유가 전부 그 안에 있었다). 기계가 먹는 `--json` 은 전부 실린다.
    """
    subs = e.get("subevents", [])[1:]
    for s in subs[:SUB_LINES_SHOWN]:
        print(f"{indent}└ [{s['n_articles']}건/{s['n_sources']}매체] {s['title'][:58]}")
    if len(subs) > SUB_LINES_SHOWN:
        print(f"{indent}└ … 외 {len(subs)-SUB_LINES_SHOWN}개 (--json 에 전부)")


def run(day: str | None, scope: str, head_min: int, body_min: int, as_json: bool,
        with_lede: bool = LEDE_DEFAULT, nonmarket_band: float = NONMARKET_BAND,
        singles_nb: float = SINGLES_NB) -> None:
    utf8_stdout()
    day = day or _date.today().strftime("%Y-%m-%d")
    b = build(day, scope, head_min, body_min, with_lede=with_lede,
              nonmarket_band=nonmarket_band, singles_nb=singles_nb)
    d = b["denominator"]

    if as_json:
        BRIEF_OUT.mkdir(parents=True, exist_ok=True)
        fp = BRIEF_OUT / f"{day}_{scope}.json"
        txt = json.dumps(b, ensure_ascii=False, separators=(",", ":"))
        fp.write_text(txt, encoding="utf-8")
        print(json.dumps({"date": b["date"], "scope": b["scope"], "denominator": d,
                          "head": len(b["head"]), "body": len(b["body"]),
                          "tail": b["tail"]["count"],
                          "single_source_shown": b["single_source"]["shown"],
                          "nonmarket_shown": b["excluded_nonmarket"]["shown"],
                          "bytes": len(txt),
                          "approx_tokens": int(len(txt) * 0.7)},
                         ensure_ascii=False, indent=2))
        print(f"\n(전체 → {fp})")
        return

    sc = {"all": "국내+해외", "foreign": "해외만", "domestic": "국내만"}[scope]
    nz = d.get("excluded_not_news") or {}
    print(f"\n# 뉴스 브리핑 — {day} [{sc}]")
    print(f"  기사 {d['articles']:,}건 → 사건 {d['events_2src_plus']}개 "
          f"→ 시장 {d['market_events']}개 (비시장 {d['nonmarket_events']}개)")
    if nz:
        print(f"  분모 정정 — 뉴스아님 {sum(nz.values())}건 제외: "
              + " · ".join(f"{k} {v}" for k, v in sorted(nz.items())))

    print(f"\n  ══ 머리 ({head_min}개 매체 이상) — {len(b['head'])}개. 오늘의 뉴스 ══")
    for e in b["head"]:
        print(f"\n  [{e['n_articles']:>3}건/{e['n_sources']}매체 분산{e['src_entropy']:.2f}] {e['title'][:60]}")
        lede = next((x.get("lede") for x in e["evidence"] if x.get("lede")), None)
        if lede:
            print(f"      {lede[:110]}")
        _sub_lines(e, "      ")

    print(f"\n  ══ 몸통 ({body_min}~{head_min-1}개 매체) — {len(b['body'])}개 ══")
    for e in b["body"][:30]:
        print(f"   [{e['n_articles']:>3}건/{e['n_sources']}매체] {e['title'][:62]}")
        _sub_lines(e, "       ")
    if len(b["body"]) > 30:
        print(f"   … 외 {len(b['body'])-30}개 (--json 에 전부)")

    t = b["tail"]
    print(f"\n  ══ 꼬리 (2매체) — {t['count']}개. 세기만 하고 표본만 ══")
    for e in t["sample"]:
        print(f"   [{e['n_articles']:>3}건] {e['title'][:62]}")

    s = b["single_source"]
    print(f"\n  ══ 1매체 — {s['shown']}개 / 전체 {s['count']}개 ══")
    print(f"     단독보도라 매체수로는 못 걸러진다 — 환율·금리·채권 1차 재료가 여기 산다")
    for x in s["sample"][:40]:
        sc = f"nb={x['nb']:>5}" if x["nb"] is not None else "  무작위"
        print(f"   {sc} [{(x['source'] or '?')[:10]:<10}] {x['title'][:58]}")
    if s["shown"] > 40:
        print(f"   … 외 {s['shown']-40}개 (--json 에 전부)")

    nm = b["excluded_nonmarket"]
    print(f"\n  ══ 비시장 경계선 (nb>{nm['band']}) — {nm['shown']}개 / 전체 {nm['count']}개 ══")
    print(f"     0 에 가까울수록 분류기가 덜 확신한 것 = 오분류 후보")
    for e in nm["sample"]:
        print(f"   nb={e['nb']:>5} [{e['n_articles']:>2}건/{e['n_sources']}매체] {e['title'][:58]}")

    print(f"\n  ⚠ 꼬리 {t['count']}개는 자른 게 아니라 표본만 보여준 것 — 진짜가 섞여 있을 수 있다.")
    print(f"  ⚠ 비시장 {nm['count'] - nm['shown']}개는 nb≤{nm['band']} 라 안 보여준다 — 분류기 오분류 10~14%(LOSO).")
    if s["scorable"]:
        print(f"  ⚠ 1매체 중 국내 {s['scorable'] - s['scored']}개는 nb≤{s['min_nb']} 라 안 보여준다 "
              f"— `--singles-nb` 로 더 열 수 있다.")
    if s["unscored"]:
        print(f"  ⚠ 1매체 중 {s['unscored']}개는 **점수가 없다**(분류기는 한글 전용) — 낮은 게 아니라 "
              f"못 잰 것. 무작위 {s['unscored_shown']}개만 보여준다.")
    print(f"  └ = 사건 안에 묻혀 있던 별개 사건 {d['subevents_recovered']}개(임계 0.65 가 삼킨 것).")
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
    p.add_argument("--singles-nb", type=float, default=SINGLES_NB, dest="singles_nb",
                   help=f"1매체층에 띄울 최소 분류기 점수(기본 {SINGLES_NB}; 낮출수록 더 많이. "
                        f"실측 15→24건·10→68건·5→184건)")
    p.add_argument("--nonmarket-band", type=float, default=NONMARKET_BAND,
                   dest="nonmarket_band",
                   help=f"비시장 중 이 점수 위는 전부 보여준다(기본 {NONMARKET_BAND}; "
                        f"0 에 가까울수록 분류기가 덜 확신한 것)")
    p.add_argument("--json", action="store_true", help="LLM 에 먹일 형태(compact)")
    p.set_defaults(func=lambda a: run(a.date, a.scope, a.head_min, a.body_min, a.json,
                                      a.with_lede, a.nonmarket_band, a.singles_nb))
