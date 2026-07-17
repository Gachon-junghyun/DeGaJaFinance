# -*- coding: utf-8 -*-
"""시장 뉴스 분류 — 제목만 보고 "이게 시장 얘긴가"를 가른다. 의존성 0(표준 라이브러리).

왜 필요한가(실측): 뉴스 풀은 금융 코퍼스가 아니다 — 국내 기사의 **62%가 종합지**
(yonhap 17.7k · chosun 13.7k · google_kr 11.2k · donga 2.8k vs 경제지 전부 합쳐 28k).
그래서 걸러내지 않으면 폭우·송파구·아이들·호날두가 반도체·수주를 이긴다.

왜 '상장사 이름이 나오나'로는 안 되는가(폐기한 방법): 그건 정밀하지만 **재현율이 처참**하다.
실측 — 섹션이 `economy` 인 기사 3,646건 중 제목에 상장사명이 있는 건 **10.6%뿐**이라 89%가
탈락한다. 결정적으로 7/07 그날 최대 사건인 "코스피 급락에 매도 사이드카 발동"의 상장사
관련도는 **7%** 였다(제목에 회사 이름이 없으니까). 매크로·지수·정책 뉴스가 통째로 날아간다.

왜 트랜스포머가 아닌가: 라벨이 URL 에서 공짜로 나오므로(아래) 트랜스포머를 써도 **같은 라벨**을
쓴다 — 그 라벨 품질이 상한이다. 실측 나이브베이즈가 홀드아웃 95.7%(정밀도 94.6·재현율 96.5),
학습 안 한 신문에도 85.6~89.7%(LOSO). 5~8%p 더 맞자고 torch 2GB + **감사 불가**를 사는 건
남는 장사가 아니다. NB 는 "코스피(+5.71)·환율(+5.14) 때문에 시장이라 봤다"를 그대로 보여준다
(`explain()`), 트랜스포머는 0.87 만 뱉는다. 판정 근거가 보여야 상위(LLM)가 반증할 수 있다(P4).

라벨은 URL 섹션에서 **공짜로** 나온다 — mt/donga/chosun/mk 는 경로에 섹션이 박혀 있다
(`mt.co.kr/politics/`·`chosun.com/entertainment/`). 실측 22,923건이 사람 손 0으로 라벨링된다.
그리고 학습 특징(제목)과 라벨(URL 경로)이 **서로 다른 신호**라, 섹션이 URL 에 없는 신문
(yonhap·asiae·hankyung·sedaily·google_kr = 국내의 62%)에도 그대로 일반화된다.

⚠ 애매한 섹션(`world`·`politics`·`real_estate`)은 **학습에서 뺀다**(POS 도 NEG 도 아님).
  · real_estate 를 POS 에 넣으면 `단지`(아파트 단지)가 시장 근거어 상위에 낀다 — 실측.
  · world/politics 엔 관세·호르무즈 같은 매크로와 정쟁이 섞여 있어 라벨이 시끄럽다.
  빼도 추론은 된다 — 그 기사들은 자기 어휘로 점수가 매겨진다(관세→시장, 정쟁→비시장).

⚠ 판정을 강제하지 않는다(P4). 점수와 근거어를 낼 뿐, 자르는 임계는 호출부가 정한다.
  틀린 10~14%(LOSO 기준)는 상위 LLM 이 근거를 읽고 버리면 된다 — false positive 는 싸고
  false negative(놓친 테마)는 영영 안 보인다.

사용:
    python -m module_news_data classify --title "코스피 급락에 매도 사이드카 발동"
    python -m module_news_data classify --eval          # 홀드아웃 + LOSO 성능
    python -m module_news_data classify --words         # 근거어 top (감사용)
"""
from __future__ import annotations

import math
import re
import sqlite3
from collections import Counter

from ._config import FOREIGN_SOURCES, origin_tag, utf8_stdout
from ._embed import VEC_DB
from ._tokenize import tokens

# URL 경로에 섹션이 박힌 신문만. 나머지(yonhap·asiae·hankyung·sedaily)는 불투명 ID 라 학습셋에
# 못 들어가지만, 바로 그 62% 를 맞히는 게 이 분류기의 목적이다.
_SEC = re.compile(r"(?:mt\.co\.kr|donga\.com/news|chosun\.com|mk\.co\.kr/news)/([A-Za-z_]+)/", re.I)

POS_SECTIONS = {"economy", "stock", "industry", "policy"}      # 시장
NEG_SECTIONS = {"sports", "entertainment", "society"}          # 비시장
# 나머지(world·politics·real_estate·jp·topics…)는 의도적으로 학습 제외(위 ⚠)

MIN_TRAIN = 2000    # 이보다 적으면 학습셋이 부족 — 조용히 엉터리 모델을 쓰느니 알린다

# ⚠ **이 분류기는 국내(한글) 전용이다.** 해외에 쓰면 안 된다:
#   · 학습이 한글 제목이라 영어는 거의 전부 미등록어 → 점수가 0 근처에 뭉친다. 실측으로
#     "Oil Surges as US Strikes Targets in Iran"(-0.5)·"Stocks ease despite upbeat Samsung
#     forecast"(-0.1)·"Deutsche Bank flags disconnect between inflation, Fed"(-0.1)가 전부
#     **비시장으로 잘렸다**. 신호가 없는 게 아니라 모델이 그 언어를 모르는 것이다.
#   · 애초에 필요도 없다 — 해외 피드는 **82%가 금융**(yahoo_finance·seekingalpha·bloomberg·
#     sec_edgar…)이라 소스 선택 단계에서 이미 걸러져 있다. 국내가 종합지 62%인 것과 정반대.
# 그래서 `applies_to()` 로 게이트한다. 영어 분류가 필요해지면 영어 라벨(섹션이 URL 에 있는
# 영문 매체)로 **별도 모델**을 학습해야 한다 — 이 모델을 쓰면 안 된다.
KR_ONLY = True


def applies_to(sources) -> bool:
    """이 사건에 분류기를 써도 되나 = **국내 기사인가**.

    ⚠ scope 가 아니라 **소스**로 판정한다. `scope='all'` 은 국내+해외가 섞이므로 scope 로
    게이트하면 그 안의 영어 기사가 통째로 잘린다. 국적 판정은 `origin_tag` 재사용(P1).
    """
    srcs = [sources] if isinstance(sources, str) else list(sources or [])
    if not srcs:
        return False
    return all(origin_tag(s) == "KR" for s in srcs)


def section_of(url: str | None) -> str | None:
    """URL 에서 섹션 라벨 추출. 없으면 None(= 학습에 못 쓰는 신문)."""
    if not url:
        return None
    m = _SEC.search(url)
    return m.group(1).lower() if m else None


class Model:
    """나이브베이즈(add-1). 학습 2초라 **모델 파일을 두지 않는다** — 부를 때마다 새로 학습하면
    버전 관리할 아티팩트도, 낡을 일도 없다(코퍼스가 자라면 자동으로 따라간다)."""

    def __init__(self, cnt, docs, vocab, tot, prior):
        self.cnt, self.docs, self.vocab, self.tot, self.prior = cnt, docs, vocab, tot, prior

    def score(self, title: str) -> float:
        """로그우도비. >0 = 시장. 크기는 확신의 세기(부호만 쓰는 게 안전하다)."""
        s = [self.prior[0], self.prior[1]]
        for w in tokens(title):
            if w not in self.vocab:
                continue
            for y in (0, 1):
                s[y] += math.log((self.cnt[y][w] + 1) / (self.tot[y] + len(self.vocab)))
        return s[1] - s[0]

    def is_market(self, title: str) -> bool:
        return self.score(title) > 0

    def explain(self, top: int = 8) -> list[tuple[str, float]]:
        """단어별 로그비 — **왜 그렇게 판정했는지의 감사 근거**(NB 를 고른 이유)."""
        out = {}
        for w in self.vocab:
            if self.cnt[0][w] + self.cnt[1][w] < 40:
                continue
            out[w] = (math.log((self.cnt[1][w] + 1) / (self.tot[1] + len(self.vocab)))
                      - math.log((self.cnt[0][w] + 1) / (self.tot[0] + len(self.vocab))))
        return sorted(out.items(), key=lambda x: -x[1])[:top]


def _labeled_rows() -> list[tuple[str, int, str]]:
    """(source, y, title) — URL 섹션으로 라벨된 것만. 국내만(해외는 섹션 규칙이 다르다).
    DB 를 한 번만 읽는다 — LOSO 가 신문 수만큼 이걸 부르므로."""
    con = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    rows = con.execute("SELECT source, url, title FROM articles "
                       "WHERE url IS NOT NULL AND title != ''").fetchall()
    con.close()
    out = []
    for src, url, title in rows:
        if (src or "") in FOREIGN_SOURCES:
            continue
        sec = section_of(url)
        if sec in POS_SECTIONS:
            out.append((src, 1, title))
        elif sec in NEG_SECTIONS:
            out.append((src, 0, title))
    return out


def _labeled(exclude_source: str | None = None) -> list[tuple[int, str]]:
    """URL 섹션으로 라벨된 (y, title) — 사람 손 0."""
    return [(y, t) for s, y, t in _labeled_rows() if s != exclude_source]


def train(data: list[tuple[int, str]] | None = None) -> Model:
    data = _labeled() if data is None else data
    if len(data) < MIN_TRAIN:
        raise RuntimeError(
            f"학습셋 {len(data)}건 < {MIN_TRAIN} — URL 섹션이 있는 기사가 부족하다. "
            f"`embed sync` 로 articles 를 채웠는지, url 컬럼이 백필됐는지 확인하라.")
    cnt = [Counter(), Counter()]
    docs = [0, 0]
    for y, t in data:
        docs[y] += 1
        for w in tokens(t):
            cnt[y][w] += 1
    vocab = set(cnt[0]) | set(cnt[1])
    tot = [sum(cnt[0].values()), sum(cnt[1].values())]
    prior = [math.log(max(docs[i], 1) / len(data)) for i in (0, 1)]
    return Model(cnt, docs, vocab, tot, prior)


def evaluate() -> dict:
    """홀드아웃(같은 신문 안) + LOSO(처음 보는 신문). 실사용은 LOSO 쪽에 가깝다."""
    import random
    data = _labeled()
    random.Random(42).shuffle(data)
    cut = int(len(data) * 0.8)
    m = train(data[:cut])
    tp = tn = fp = fn = 0
    for y, t in data[cut:]:
        p = 1 if m.score(t) > 0 else 0
        tp += (y == 1 and p == 1); tn += (y == 0 and p == 0)
        fp += (y == 0 and p == 1); fn += (y == 1 and p == 0)
    n = len(data) - cut
    hold = {"n": n, "acc": (tp + tn) / max(n, 1),
            "prec": tp / max(tp + fp, 1), "rec": tp / max(tp + fn, 1)}

    # LOSO — 그 신문을 통째로 빼고 학습해서 맞힌다. 실사용(라벨 없는 yonhap·asiae)에 가깝다.
    rows = _labeled_rows()
    loso = []
    for s in sorted({r[0] for r in rows}):
        tr = [(y, t) for src, y, t in rows if src != s]
        te = [(y, t) for src, y, t in rows if src == s]
        if len(tr) < MIN_TRAIN or len(te) < 200:
            continue
        mm = train(tr)
        ok = sum(1 for y, t in te if (1 if mm.score(t) > 0 else 0) == y)
        loso.append({"source": s, "n": len(te), "acc": ok / len(te)})
    return {"holdout": hold, "loso": loso, "train_size": len(data)}


def run(title: str | None, do_eval: bool, do_words: bool) -> None:
    utf8_stdout()
    if do_eval:
        r = evaluate()
        h = r["holdout"]
        print(f"\n# classify 성능 (학습셋 {r['train_size']:,}건 · URL 섹션 라벨 · 사람 손 0)")
        print(f"  홀드아웃(같은 신문 안) : 정확도 {100*h['acc']:.1f}%  정밀도 {100*h['prec']:.1f}%  "
              f"재현율 {100*h['rec']:.1f}%   (n={h['n']:,})")
        print(f"\n  LOSO — 그 신문을 한 번도 학습 안 하고 맞히기(실사용에 가까움):")
        for x in r["loso"]:
            print(f"     {x['source']:<10} {x['acc']*100:>5.1f}%  (n={x['n']:,})")
        print(f"\n  ⚠ 상장사이름 방식의 경제기사 재현율은 10.6% 였다 — 그걸 대체한 것.")
        return
    m = train()
    if do_words:
        print(f"\n# 시장 근거어 top12 (감사 — 왜 그렇게 판정하나)")
        for w, v in m.explain(12):
            print(f"   +{v:.2f}  {w}")
        print(f"\n# 비시장 근거어 top8")
        for w, v in sorted(m.explain(len(m.vocab)), key=lambda x: x[1])[:8]:
            print(f"   {v:.2f}  {w}")
        return
    if title:
        s = m.score(title)
        print(f"\n  {'시장' if s > 0 else '비시장'}  (점수 {s:+.1f})   {title}")
        return
    print("  --title / --eval / --words 중 하나를 주라.")


def cli_register(sub) -> None:
    p = sub.add_parser("classify", help="제목 → 시장/비시장 (NB·의존성0·URL 라벨 자가학습)")
    p.add_argument("--title", default=None, help="이 제목 한 건을 판정")
    p.add_argument("--eval", action="store_true", dest="do_eval", help="홀드아웃+LOSO 성능")
    p.add_argument("--words", action="store_true", dest="do_words", help="근거어(감사)")
    p.set_defaults(func=lambda a: run(a.title, a.do_eval, a.do_words))
