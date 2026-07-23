# -*- coding: utf-8 -*-
"""사건 클러스터링 — 기사(article)가 아니라 **사건(event)** 을 단위로 만든다.

왜 단위가 바뀌어야 하나(실측 근거):
  · **중복**: 같은 일을 27번 낸다. 캐나다 잠수함 건이 기사 27건인데, 단어 단위로 보면
    `한화오션`·`잠수함`·`캐나다`·`TKMS`·`나토` 5줄로 **쪼개져** 나온다. 사건 단위면 1줄.
  · **누락**: 단어 급등(z)은 "새로운 것"을 재지 "큰 것"을 못 잰다. 7/07 코스피 8% 급락 +
    서킷브레이커 날, `코스피`는 평소 1.826%→2.300%(1.3배)라 후보에도 못 들었다(`영업이익`이
    23.6배로 1위). 사건 단위는 같은 날을 [30건/8매체]로 1위에 올린다.
  · **중요도**: 몇 개 매체가 다뤘나 = 편집자 여러 명이 **독립적으로** 내린 판정. 우리가 정한
    규칙이 아니라 시장의 판정을 빌려오는 것. 단독 보도는 시장이 안 중요하다고 말한 것이다.

⚠ **평균중심화 필수**(`_embed` 참조). 임베딩은 쏠려 있어 무작위 기사쌍도 코사인이 높다
(실측 ko-sroberta +0.148 / e5-base +0.772 — e5 는 그대로 쓰면 3,774건이 **한 덩어리**가 된다).
그날 모집단의 평균을 빼면 -0.003 으로 펴진다. 중심화 기준이 '그날'인 이유: 무엇을 모아놓고
재느냐에 따라 평균이 달라지므로, 비교 대상인 그날 기사들로 잡아야 한다.

⚠ **average-link 여야 한다.** single-link 는 A~B, B~C 만으로 A,C 를 잇는 연쇄 때문에
763~1,279건짜리 블롭을 만든다(실측). average 는 최대 클러스터가 23~125로 유지된다.

⚠ 판정하지 않는다(P4). 사건을 묶고 세기만 한다 — 호재/악재도, 시장/비시장도 여기서 안 정한다.
실제로 7/07 한화오션 [27건/9매체] 는 **수주가 아니라 탈락**이었다. 방향은 근거를 읽어야 안다.

⚠ 남은 한계(정직하게): 임베딩은 "같은 사건"과 "같은 주제"를 한 척도로 재서 완전히 못 가른다.
실측 임계 0.65 에서 삼성 관련 113건이 한 덩어리가 됐는데, 그 안엔 성과급·2분기실적·갤S27 AP·
DRAM 가격이 섞여 있었다(= 토픽 블롭). 임계를 올리면 파편화, 내리면 블롭 — 중간이 없다.
현재값은 그 트레이드오프의 타협점이지 정답이 아니다.
→ **전역 임계로는 못 고치니 큰 덩어리 안에서만 다시 자른다**(`SPLIT_*` / `subevents`).
  실측 2026-07-23: 8건+ 사건 21개 중 15개가 실은 복수 사건이었고, 25개 사건이 되살아났다.

⚠ **여기서 '버린' 것은 전부 세어서 돌려준다**(P4). 매체수 미달 덩어리는 `singles`,
번역중복·포토·자동기사는 `excluded_noise`. 실측 2026-07-23 국내 1,821건 중 638건(35%)이
1매체 덩어리였고 그 절반이 시장기사였다 — 조용히 사라지면 "오늘 조용했다"가 거짓이 된다.

⚠ torch/sklearn 을 모듈 최상단에서 import 하지 않는다 — 서버(GPU 없음)가 `build_parser`
로 이 파일을 import 한다(`_embed` 의 같은 ⚠).

사용:
    python -m module_news_data cluster --date 2026-07-07 --scope domestic
    python -m module_news_data cluster --date 2026-07-07 --min-sources 3 --json
"""
from __future__ import annotations

import json
import math
from collections import Counter
from datetime import date as _date

from ._config import FOREIGN_SOURCES, OUT_DIR, noise_class, utf8_stdout
from ._embed import load_vectors

CLUSTER_OUT = OUT_DIR / "news_events"

# 실측 스윕에서 고른 타협점(ko-sroberta + 평균중심화 + average-link):
#   0.75 → 사건 499 · 폭락 3덩어리 · 최대 125 (블롭 쪽)
#   0.65 → 사건 1,022 · 2매체+ 512 · 폭락 5 · 잠수함 7 · 최대 113   ← 채택
#   0.60 → 사건 1,333 · 폭락 8 (파편 쪽)
DISTANCE = 0.65
MIN_SOURCES = 2   # 1개 매체만 다룬 건 '사건'으로 안 센다 — 시장이 안 중요하다고 판정한 것

# ── 블롭 해체(하위사건) ───────────────────────────────────────────────────
# 임계 0.65 는 파편화를 막는 대신 **다른 사건을 삼킨다**. 실측 2026-07-23: 8건 이상 사건
# 21개 중 **15개가 실제로는 2개 이상**이었고, 최악은 [44건/5매체] "美 301조 강제노동 관세"
# 안에 국내 **무역위 중국산 부틸아크릴레이트 반덤핑 관세[4건/3매체]**와 트럼프 캐나다 50%
# 추가관세가 통째로 들어가 한 줄로 붕괴한 것이다 — 브리핑만 읽으면 그 둘은 존재하지 않는다.
# 임계를 낮춰 전역 해결하면 반대편(파편화)이 터지므로, **큰 덩어리 안에서만** 다시 자른다.
# 하위사건 자격은 부모와 같은 논리(매체 2개 이상) — 한 매체가 여러 각도로 쓴 건 사건이 아니다.
SPLIT_MIN_ARTICLES = 8      # 이보다 작은 사건은 안 쪼갠다(실측: 그 아래는 거의 단일사건)
SPLIT_DISTANCE = 0.45       # 내부 재분할 임계. 실측 25개 숨은 사건 회수 / +1.8k 토큰


def _norm_entropy(counts: list[int]) -> float:
    """소스 분포의 정규화 엔트로피 0~1. 1=여러 매체에 고르게, 0=한 매체 독점(메아리)."""
    n = sum(counts)
    if n <= 0 or len(counts) <= 1:
        return 0.0
    h = -sum((c / n) * math.log(c / n) for c in counts if c > 0)
    return h / math.log(len(counts))


def _subevents(sub, members, meta, np, AgglomerativeClustering) -> list[dict]:
    """큰 사건 하나를 내부에서 다시 잘라 '숨은 하위사건'을 찾는다(위 ⚠ SPLIT_*).

    돌려주는 건 하위사건이 **2개 이상일 때만** — 1개면 쪼갤 게 없었다는 뜻이고,
    있지도 않은 분열을 보고하면 상위 LLM 이 없는 사건을 읽는다(P4).
    """
    lab = AgglomerativeClustering(n_clusters=None, distance_threshold=SPLIT_DISTANCE,
                                  metric="cosine", linkage="average").fit_predict(sub)
    groups: dict[int, list[int]] = {}
    for i, l in enumerate(lab):
        groups.setdefault(int(l), []).append(i)

    out = []
    for g in groups.values():
        srcs = {meta[members[i]]["source"] or "?" for i in g}
        if len(g) < 2 or len(srcs) < MIN_SOURCES:
            continue                       # 부모와 같은 자격 — 1매체짜리 각도는 사건이 아니다
        c = sub[g].mean(axis=0)
        c = c / (np.linalg.norm(c) or 1.0)
        rep = g[int(np.argmax(sub[g] @ c))]
        out.append({"n_articles": len(g), "n_sources": len(srcs),
                    "title": meta[members[rep]]["title"]})
    out.sort(key=lambda s: (-s["n_articles"], -s["n_sources"]))
    return out if len(out) >= 2 else []


def cluster_day(day: str, scope: str = "domestic", distance: float = DISTANCE,
                min_sources: int = MIN_SOURCES, with_members: bool = False,
                split_big: bool = True) -> dict:
    """하루치 기사 → 사건 목록. 판정 없음 — 묶고 세고 근거만 붙인다.

    with_members=True 면 사건마다 전체 구성기사 url_hash 목록(`members`)을 붙인다 —
    `_thread`(주간 궤적)가 사건 centroid 를 원공간에서 다시 계산할 때 쓴다.
    기본 OFF: brief 산출물이 머리사건 하나에 50+ 해시로 부풀지 않게.

    split_big=True 면 큰 사건에 `subevents`(숨은 하위사건)를 붙인다 — `_thread` 는 궤적만
    보므로 꺼서 부른다.

    ⚠ 매체수 미달 덩어리는 **버리지 않고 `singles` 로 돌려준다**. 예전엔 여기서 조용히
      사라졌는데, 실측 2026-07-23 그 풀에 국내기사의 35%(638건)가 있었고 그중 절반이
      분류기 기준 시장기사였다(환율·국고채·한은 코멘트가 전부 여기 있었다).
      '사건이 아니다'와 '없었다'는 다른 말이다 — 등급을 낮출 뿐 지우지 않는다.
    """
    import numpy as np                                   # 무거운 import 는 함수 안에서만
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.preprocessing import normalize

    hashes, meta, Z = load_vectors(day=day)
    keep = [i for i, m in enumerate(meta)
            if scope == "all"
            or ((m["source"] or "") in FOREIGN_SOURCES) == (scope == "foreign")]

    # ★ 분모 정정 — 번역중복·포토·자동기사를 모집단에서 뺀다. **세어서 돌려준다**(P4).
    noise = Counter()
    kept = []
    for i in keep:
        nc = noise_class(meta[i]["title"], meta[i].get("url"))
        if nc:
            noise[nc] += 1
        else:
            kept.append(i)
    keep = kept

    if len(keep) < 2:
        return {"date": day, "scope": scope, "n_articles": len(keep), "events": [],
                "singles": [], "excluded_noise": dict(noise),
                "note": "기사가 2건 미만 — 클러스터 불가(빈칸이지 '조용함'이 아니다)"}
    meta = [meta[i] for i in keep]
    hashes = [hashes[i] for i in keep]
    Z = Z[keep]

    # ★ 그날 모집단 기준 평균중심화 → 재정규화 (위 ⚠)
    base_cos = float(np.mean(np.sum(Z[:500] * Z[500:1000], axis=1))) if len(Z) >= 1000 else None
    Zc = normalize(Z - Z.mean(axis=0))

    lab = AgglomerativeClustering(n_clusters=None, distance_threshold=distance,
                                  metric="cosine", linkage="average").fit_predict(Zc)

    groups: dict[int, list[int]] = {}
    for i, l in enumerate(lab):
        groups.setdefault(int(l), []).append(i)

    events, singles = [], []
    for members in groups.values():
        srcs = Counter(meta[i]["source"] or "?" for i in members)
        # 대표기사 = 중심(medoid). 제일 긴 제목을 고르면 재배포판('- YTN','- v.daum.net')이
        # 뽑힌다 — 실측으로 확인. 중심에 가까운 게 그 사건의 전형적 서술이다.
        sub = Zc[members]
        centroid = sub.mean(axis=0)
        # 중심에 가까운 순 — 1등이 대표. ⚠ 근거를 그냥 `members[:3]` 로 주면 **제목과 근거가
        # 따로 논다**(대표는 medoid 인데 근거는 아무거나). 실측으로 서킷브레이커 사건의 근거가
        # 같은 덩어리에 섞인 공시목록 기사로 나왔다 — LLM 이 엉뚱한 기사를 그 사건의 증거로 읽는다.
        order = [members[j] for j in np.argsort(-(sub @ centroid))]
        rep = order[0]

        if len(srcs) < min_sources:
            # 사건 자격 미달 — 그래도 **제목은 남긴다**(위 ⚠). 상위가 nb 로 다시 거른다.
            singles.append({"n_articles": len(members), "source": meta[rep]["source"],
                            "title": meta[rep]["title"], "url_hash": hashes[rep]})
            continue

        ev = {
            "n_articles": len(members),
            "n_sources": len(srcs),
            "src_entropy": round(_norm_entropy(list(srcs.values())), 2),
            "title": meta[rep]["title"],
            "sources": sorted(srcs),
            "evidence": [{"source": meta[i]["source"], "title": meta[i]["title"],
                          "url_hash": hashes[i], "url": meta[i].get("url")}
                         for i in order[:3]],
        }
        if split_big and len(members) >= SPLIT_MIN_ARTICLES:
            subs = _subevents(sub, members, meta, np, AgglomerativeClustering)
            if subs:
                ev["subevents"] = subs
        if with_members:
            ev["members"] = [hashes[i] for i in order]
        events.append(ev)
    events.sort(key=lambda e: (e["n_sources"], e["n_articles"]), reverse=True)
    singles.sort(key=lambda s: -s["n_articles"])

    return {
        "date": day, "scope": scope, "n_articles": len(meta),
        "n_clusters": len(groups), "n_events": len(events),
        "singletons": sum(1 for g in groups.values() if len(g) == 1),
        "n_singles": len(singles),
        "n_subevents": sum(len(e.get("subevents", [])) for e in events),
        "excluded_noise": dict(noise),
        "params": {"distance": distance, "min_sources": min_sources,
                   "linkage": "average", "centered": True,
                   "split_distance": SPLIT_DISTANCE if split_big else None},
        "baseline_cos_raw": round(base_cos, 3) if base_cos is not None else None,
        "events": events,
        "singles": singles,
    }


def run(day: str | None, scope: str, distance: float, min_sources: int,
        top: int, as_json: bool) -> None:
    utf8_stdout()
    day = day or _date.today().strftime("%Y-%m-%d")
    rep = cluster_day(day, scope, distance, min_sources)

    if as_json:
        CLUSTER_OUT.mkdir(parents=True, exist_ok=True)
        fp = CLUSTER_OUT / f"{day}_{scope}.json"
        fp.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({k: v for k, v in rep.items() if k not in ("events", "singles")},
                         ensure_ascii=False, indent=2))
        print(f"\n(사건 {len(rep['events'])}개 + 근거 + 1매체 {len(rep['singles'])}개 → {fp})")
        return

    sc = {"all": "국내+해외", "foreign": "해외만", "domestic": "국내만"}[scope]
    print(f"\n# 사건 — {rep['date']} [{sc}]")
    if not rep["events"]:
        print(f"  {rep.get('note', '사건 0개')}")
        return
    nz = rep.get("excluded_noise") or {}
    nz_txt = (" · 뉴스아님 " + "+".join(f"{k} {v}" for k, v in sorted(nz.items()))) if nz else ""
    print(f"  기사 {rep['n_articles']:,}건 → 덩어리 {rep['n_clusters']:,}개 "
          f"→ 사건 {rep['n_events']}개({min_sources}개 매체 이상){nz_txt}")
    print(f"\n  {'건수':>4} {'매체':>4} {'분산':>5}  제목")
    print("  " + "─" * 74)
    for e in rep["events"][:top]:
        print(f"  {e['n_articles']:>4} {e['n_sources']:>4} {e['src_entropy']:>5.2f}  {e['title'][:62]}")
        for s in e.get("subevents", [])[1:]:
            print(f"       └ [{s['n_articles']}건/{s['n_sources']}매체] {s['title'][:58]}")
    print(f"\n  분산=매체 고르기(1=고르게 퍼짐, 0=한 매체 독점) · 근거기사는 --json")
    print(f"  ⚠ 판정 아님 — 호재/악재도 시장/비시장도 여기선 안 정한다. 근거를 읽어야 안다.")
    print(f"  └ = 그 사건 안에 묻혀 있던 별개 사건({rep['n_subevents']}개) — 임계 {DISTANCE}가 삼킨 것.")
    print(f"  ⚠ 1매체 덩어리 {rep['n_singles']:,}개는 여기 안 뜬다(--json 의 `singles`) — "
          f"버린 게 아니라 등급이 낮은 것.")


def cli_register(sub) -> None:
    p = sub.add_parser("cluster", help="하루 기사 → 사건(중복 압축·매체수 랭킹). 클라 전용")
    p.add_argument("--date", default=None, help="market_day YYYY-MM-DD (기본: 오늘)")
    p.add_argument("--scope", choices=["all", "foreign", "domestic"], default="domestic")
    p.add_argument("--distance", type=float, default=DISTANCE,
                   help=f"응집 거리 임계(기본 {DISTANCE}; 낮추면 파편화, 올리면 토픽 블롭)")
    p.add_argument("--min-sources", type=int, default=MIN_SOURCES, dest="min_sources",
                   help=f"사건 자격 최소 매체수(기본 {MIN_SOURCES})")
    p.add_argument("--top", type=int, default=25)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=lambda a: run(a.date, a.scope, a.distance, a.min_sources,
                                      a.top, a.json))
