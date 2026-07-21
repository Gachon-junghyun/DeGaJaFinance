# -*- coding: utf-8 -*-
"""사건 궤적(thread) — 하루 스냅샷(`brief`)을 **여러 날의 흐름**으로 잇는다.

이 파일이 푸는 문제: `cluster`/`brief` 는 "오늘 무슨 일이 있었나"까지만 답한다.
그런데 매매에 필요한 건 그 다음 질문이다 — **"이 사건이 오늘 처음인가, 5일째 커지는
중인가, 식어가는 중인가."** 같은 [12건/6매체]라도 첫날이면 이르고, 닷새째 정점이면
이미 크라우디드다. 하루 뷰는 이 둘을 구분하지 못한다.

방법: 일별 사건(cluster_day, 일내 중심화)을 그대로 두고, 사건마다 **원공간 centroid**
(구성기사 벡터 평균)를 다시 계산 → 윈도우 전체 사건 모집단으로 평균중심화 →
average-link 응집으로 날짜를 가로질러 다시 묶는다 = 스레드(같은 사건의 여러 날).

⚠ **중심화 기준이 두 번 다르다 — 버그가 아니라 원칙이다.** 일내 클러스터는 '그날
모집단', 스레드 연결은 '윈도우 사건 모집단'으로 중심화한다(`_embed` 의 ⚠: 중심화는
무엇을 모아놓고 재느냐에 달렸다). 일내 중심화된 벡터끼리는 날이 다르면 **비교 자체가
불가능**하다(빼는 평균이 다르다) — 그래서 원공간에서 centroid 를 다시 만든다.

⚠ 판정하지 않는다(P4). BUILDING/FADING 은 매체수 곡선의 **모양**이지 호재/악재/중요도가
아니다. 방향은 여전히 근거를 읽어야 안다(`brief` 의 같은 ⚠ — 한화오션 [27건]은 탈락이었다).

⚠ 클라이언트 전용(GPU 벡터 파생물 사용) — `DB_READ_CMDS` 에 넣지 않는다(P6).
⚠ torch/sklearn 최상단 import 금지 — 서버가 `build_parser` 로 이 파일을 import 한다.

실측(2026-07-11→17 국내, 7일, 17.3초):
  · 일별 사건 2,480 → 스레드 1,876 · 다일(2일+) 352 = 살아있는 73(BUILDING 16 ·
    FADING 35 · REIGNITED 22) + ENDED 279 · 원데이 1,524
  · LINK_DISTANCE 스윕: 0.30 → 다일 225·6일+ 사가 4개뿐(환율 사가 등이 토막) /
    **0.40 → 다일 352·6일+ 12개, 사가 순수** / 0.50 → 다일 482인데 '폭염' 332건 블롭 +
    '오늘의 운세'까지 7일 스레드(반복 포맷 흡착) → **0.40 채택**
  · 검증: 한은 금리인상 사가 7일 [총 302건] — **7/11 [14건/2매체] "금리인상 초읽기" 꼬리
    → 7/16 [101건/8매체] 인상 발표**. 환율 1486원 사가 7일 [221건], 이란·호르무즈 7일.
    이런 전조형(2매체 시작 → 5매체+ 정점) 스레드가 이 윈도우에만 **12개** — 하루 뷰에선
    꼬리라 안 보이던 것이 궤적에선 미리 보인다. 이게 이 축의 알파다.
  · 크기: --json 전체 374KB(~262k 토큰 — **LLM 직접 소비 불가, 기계용 파일**). LLM 은
    텍스트 뷰를 읽는다(--top 25 기준 17.5KB ≈ 12k 토큰): 살아있는 시장 스레드 타임라인
    + 나머지 한 줄 + ENDED 상위 10 + 비시장·원데이 분모.

⚠ **윈도우 끝이 휴일/저물량이면 태그가 FADING 쪽으로 기계적으로 쏠린다.** 실측 7/17
(제헌절)은 기사 185건 vs 평일 450+ — 마지막 날 매체수가 물량 때문에 낮아져 BUILDING 이
과소, FADING 이 과대해진다. per-day 분모 줄을 먼저 읽고 태그를 해석하라.

⚠ **남은 한계(정직하게): 스레드에는 '같은 사건의 연속'과 '같은 주제의 나열'이 섞인다.**
`_cluster` 의 사건/주제 미분리 한계가 주간으로 증폭된 것. 실측: 한은 금리인상 스레드는
진짜 사가(초읽기→인상→후폭풍)지만, 'AI' 6일 BUILDING 스레드는 정부AI·FSN·휴넷·강연이
섞인 **테마 묶음**이었다. 테마 모멘텀 신호로는 여전히 유효하나 "한 사건이 6일 이어졌다"로
읽으면 오독이다 — 타임라인 제목들이 같은 주어를 공유하는지 눈으로 확인하라.

사용:
    python -m module_news_data thread --days 7 --scope domestic          # 오늘 기준 7일
    python -m module_news_data thread --date 2026-07-17 --days 7 --json
"""
from __future__ import annotations

import json
from datetime import date as _date, datetime, timedelta

from ._classify import applies_to, train
from ._cluster import DISTANCE, MIN_SOURCES, cluster_day
from ._config import OUT_DIR, utf8_stdout
from ._embed import load_vectors

THREAD_OUT = OUT_DIR / "news_threads"

WINDOW_DAYS = 7      # 기본 회고 폭 — "최소 일주일의 흐름"
LINK_DISTANCE = 0.40  # 스레드 연결 임계(윈도우 중심화 코사인 거리). 실측 스윕은 헤더 참조.


def _day_list(end_day: str, days: int) -> list[str]:
    end = datetime.strptime(end_day, "%Y-%m-%d").date()
    return [(end - timedelta(days=i)).isoformat() for i in range(days - 1, -1, -1)]


def _shape_tag(day_sources: dict[str, int], end_day: str) -> str:
    """매체수 곡선의 모양 — 중요도 판정이 아니다(P4). 숫자로 재현 가능한 서술만.

    NEW        마지막 날 처음 등장
    BUILDING   마지막 날 살아있고, 마지막 날 매체수 = 윈도우 정점
    FADING     마지막 날 살아있는데 정점은 이전(피크를 지났다)
    REIGNITED  2일+ 공백 후 마지막 날 재등장
    ENDED      마지막 날 이전에 끊김(정점·지속일은 timeline 으로)
    """
    seen = sorted(day_sources)
    first, last = seen[0], seen[-1]
    alive = last == end_day
    if not alive:
        return "ENDED"
    if first == last:
        return "NEW"
    prev = datetime.strptime(seen[-2], "%Y-%m-%d").date()
    cur = datetime.strptime(last, "%Y-%m-%d").date()
    if (cur - prev).days >= 2:
        return "REIGNITED"
    peak = max(day_sources.values())
    return "BUILDING" if day_sources[last] >= peak else "FADING"


def thread_window(end_day: str, days: int = WINDOW_DAYS, scope: str = "domestic",
                  distance: float = DISTANCE, link_distance: float = LINK_DISTANCE,
                  min_sources: int = MIN_SOURCES) -> dict:
    """윈도우의 일별 사건 → 스레드(같은 사건의 여러 날). 묶고 세고 근거만."""
    import numpy as np                                   # 무거운 import 는 함수 안에서만
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.preprocessing import normalize

    day_events: list[dict] = []          # 사건 + day
    centroids: list = []
    per_day: list[dict] = []
    for day in _day_list(end_day, days):
        cl = cluster_day(day, scope, distance, min_sources, with_members=True)
        per_day.append({"date": day, "articles": cl.get("n_articles", 0),
                        "events": cl.get("n_events", 0)})
        if not cl.get("events"):
            continue
        # 원공간 벡터로 centroid — 일내 중심화 공간은 날짜 간 비교 불가(헤더 ⚠)
        hashes, _, Z = load_vectors(day=day)
        idx = {h: i for i, h in enumerate(hashes)}
        for e in cl["events"]:
            rows = [idx[h] for h in e["members"] if h in idx]
            if not rows:
                continue
            c = Z[rows].mean(axis=0)
            centroids.append(c / (np.linalg.norm(c) or 1.0))
            day_events.append({"day": day, **{k: v for k, v in e.items() if k != "members"}})

    if len(day_events) < 2:
        return {"window": {"end": end_day, "days": days}, "scope": scope,
                "per_day": per_day, "threads": [],
                "note": "윈도우에 사건이 2개 미만 — 스레드 불가(빈칸이지 '조용함'이 아니다)"}

    C = np.vstack(centroids)
    Cc = normalize(C - C.mean(axis=0))                   # ★ 윈도우 사건 모집단 기준 중심화
    lab = AgglomerativeClustering(n_clusters=None, distance_threshold=link_distance,
                                  metric="cosine", linkage="average").fit_predict(Cc)

    groups: dict[int, list[int]] = {}
    for i, l in enumerate(lab):
        groups.setdefault(int(l), []).append(i)

    model = train()
    threads = []
    for members in groups.values():
        # 같은 날 사건 여러 개가 한 스레드에 들어오면 그날 칸에서 합산
        by_day: dict[str, dict] = {}
        for i in members:
            e = day_events[i]
            d = by_day.setdefault(e["day"], {"date": e["day"], "n_articles": 0,
                                             "n_sources": 0, "title": None, "_ev": None})
            d["n_articles"] += e["n_articles"]
            if e["n_sources"] > d["n_sources"]:
                d["n_sources"], d["title"], d["_ev"] = e["n_sources"], e["title"], e
        timeline = sorted(by_day.values(), key=lambda x: x["date"])
        day_sources = {t["date"]: t["n_sources"] for t in timeline}
        peak = max(timeline, key=lambda t: t["n_sources"])
        rep = peak["_ev"]
        # 시장/비시장은 brief 와 같은 규칙(국내 소스만 판정, 아니면 None) — 정점 사건 기준
        nb = round(model.score(rep["title"]), 1) if applies_to(rep.get("sources") or []) else None
        threads.append({
            "tag": _shape_tag(day_sources, end_day),
            "days_seen": len(timeline),
            "first": timeline[0]["date"], "last": timeline[-1]["date"],
            "total_articles": sum(t["n_articles"] for t in timeline),
            "peak_sources": peak["n_sources"], "peak_date": peak["date"],
            "title": rep["title"], "nb": nb,
            "curve": "→".join(str(t["n_sources"]) for t in timeline),
            "timeline": [{k: t[k] for k in ("date", "n_articles", "n_sources", "title")}
                         for t in timeline],
            "evidence": rep.get("evidence", [])[:3],
        })

    multi = [t for t in threads if t["days_seen"] >= 2]
    # 살아있는(BUILDING→REIGNITED→FADING) 순 — 데스크가 먼저 봐야 하는 건 커지는 쪽이다.
    tag_rank = {"BUILDING": 0, "REIGNITED": 1, "FADING": 2, "ENDED": 3}
    multi.sort(key=lambda t: (tag_rank.get(t["tag"], 9), -t["peak_sources"],
                              -t["days_seen"], -t["total_articles"]))
    oneday = [t for t in threads if t["days_seen"] == 1]
    new_today = sum(1 for t in oneday if t["last"] == end_day)

    return {
        "window": {"start": _day_list(end_day, days)[0], "end": end_day, "days": days},
        "scope": scope,
        "params": {"distance": distance, "link_distance": link_distance,
                   "min_sources": min_sources, "centered": "window-events"},
        "per_day": per_day,
        "denominator": {"day_events": len(day_events), "threads": len(threads),
                        "multiday": len(multi),
                        "alive": sum(1 for t in multi if t["tag"] != "ENDED"),
                        "oneday": len(oneday), "oneday_new_today": new_today},
        "threads": multi,
        "oneday": {"count": len(oneday), "new_today": new_today,
                   "note": "1일 스레드 — 오늘 처음(NEW)을 포함해 하루 뷰(brief)의 몫. 세기만 한다"},
    }


def run(end_day: str | None, days: int, scope: str, link_distance: float,
        top: int, tag_filter: str | None, as_json: bool) -> None:
    utf8_stdout()
    end_day = end_day or _date.today().strftime("%Y-%m-%d")
    rep = thread_window(end_day, days, scope, link_distance=link_distance)

    if as_json:
        THREAD_OUT.mkdir(parents=True, exist_ok=True)
        fp = THREAD_OUT / f"{end_day}_{days}d_{scope}.json"
        txt = json.dumps(rep, ensure_ascii=False, separators=(",", ":"))
        fp.write_text(txt, encoding="utf-8")
        print(json.dumps({"window": rep["window"], "scope": scope,
                          "denominator": rep.get("denominator"),
                          "bytes": len(txt), "approx_tokens": int(len(txt) * 0.7)},
                         ensure_ascii=False, indent=2))
        print(f"\n(스레드 전체 + 근거 → {fp})")
        return

    sc = {"all": "국내+해외", "foreign": "해외만", "domestic": "국내만"}[scope]
    w = rep["window"]
    print(f"\n# 사건 궤적 — {w['start']} → {w['end']} ({w['days']}일) [{sc}]")
    if not rep.get("threads"):
        print(f"  {rep.get('note', '다일 스레드 0개')}")
        return
    d = rep["denominator"]
    print("  " + " · ".join(f"{p['date'][5:]} {p['events']}건" for p in rep["per_day"]))
    print(f"  일별 사건 {d['day_events']:,} → 스레드 {d['threads']:,} "
          f"(다일 {d['multiday']} — 살아있는 {d['alive']} · 원데이 {d['oneday']}, "
          f"그중 오늘 신규 {d['oneday_new_today']})")

    pool = [t for t in rep["threads"] if (not tag_filter or t["tag"] == tag_filter)]
    # brief 와 같은 규칙: nb>0 또는 판정불가(None)=시장. 게이트가 아니라 정렬 힌트 —
    # 비시장도 자르지 않고 분모+표본으로 남긴다(오분류 10~14%, LOSO).
    mkt = [t for t in pool if t["nb"] is None or t["nb"] > 0]
    nonmkt = [t for t in pool if not (t["nb"] is None or t["nb"] > 0)]
    alive = [t for t in mkt if t["tag"] != "ENDED"]
    ended = [t for t in mkt if t["tag"] == "ENDED"]

    # ══ 살아있는 스레드: top 개는 타임라인 전부, 나머지는 한 줄 — 자르지 않는다 ══
    for t in alive[:top]:
        nb = f" nb={t['nb']}" if t["nb"] is not None else ""
        print(f"\n  [{t['tag']:<9}] {t['days_seen']}일 · 매체 {t['curve']} · "
              f"총 {t['total_articles']}건{nb}")
        for row in t["timeline"]:
            print(f"     {row['date'][5:]} [{row['n_articles']:>3}건/{row['n_sources']}매체] "
                  f"{row['title'][:56]}")
    if len(alive) > top:
        print(f"\n  ── 살아있는 나머지 {len(alive)-top}개 (한 줄씩) ──")
        for t in alive[top:]:
            print(f"   [{t['tag'][:5]}] {t['curve']:>12} {t['title'][:54]}")

    # ══ ENDED: 끊긴 사가 — 관심 회전의 흔적. 정점 큰 순 10개 + 분모 ══
    if ended and not tag_filter:
        ended.sort(key=lambda t: -t["peak_sources"])
        print(f"\n  ── 끊긴 스레드(ENDED) {len(ended)}개 — 정점 큰 10개만, 나머진 분모 ──")
        for t in ended[:10]:
            print(f"   [{t['first'][5:]}~{t['last'][5:]}] {t['curve']:>10} "
                  f"피크{t['peak_sources']}매체 {t['title'][:48]}")
    if nonmkt and not tag_filter:
        print(f"\n  ── 비시장 스레드 {len(nonmkt)}개 — 분류기 판정(오분류 10~14%). 표본 5개 ──")
        for t in nonmkt[:5]:
            print(f"   [{t['tag'][:5]}] {t['curve']:>10} nb={t['nb']} {t['title'][:48]}")
    print(f"\n  ⚠ 태그는 매체수 곡선의 모양이지 중요도·방향이 아니다 — 근거를 읽어야 안다(P4).")
    print(f"  ⚠ 윈도우 끝이 휴일/저물량이면 FADING 이 과대해진다 — 위 per-day 분모 먼저.")
    print(f"  ⚠ 원데이 {d['oneday']}개(오늘 신규 {d['oneday_new_today']})는 하루 뷰(brief)가 담당.")


def cli_register(sub) -> None:
    p = sub.add_parser("thread", help="여러 날 사건 궤적(스레드) — BUILDING/FADING. 클라 전용")
    p.add_argument("--date", default=None, help="윈도우 끝 market_day (기본: 오늘)")
    p.add_argument("--days", type=int, default=WINDOW_DAYS, help=f"회고 폭(기본 {WINDOW_DAYS}일)")
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="domestic")
    p.add_argument("--link-distance", type=float, default=LINK_DISTANCE, dest="link_distance",
                   help=f"스레드 연결 임계(기본 {LINK_DISTANCE}; 낮추면 사가 토막, 올리면 토픽블롭)")
    p.add_argument("--top", type=int, default=25, help="텍스트 출력 스레드 수")
    p.add_argument("--tag", choices=["NEW", "BUILDING", "FADING", "REIGNITED", "ENDED"],
                   default=None, help="이 모양만 출력")
    p.add_argument("--json", action="store_true", help="LLM 에 먹일 형태(전체)")
    p.set_defaults(func=lambda a: run(a.date, a.days, a.scope, a.link_distance,
                                      a.top, a.tag, a.json))
