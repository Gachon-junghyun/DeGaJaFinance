# -*- coding: utf-8 -*-
"""정량 검증 — "뉴스와 변곡이 실제로 붙어 있나, 붙었다면 어느 쪽이 먼저인가".

여기서 내는 건 전부 **관측값**이다(P4). 해석·판단은 상위(리포트/에이전트)가 한다.

세 가지를 잰다.
  ① **리드/래그 상관** corr(뉴스z[t+k], |수익z[t]|), k = -5…+5 거래일.
     k<0 = 뉴스가 먼저, k>0 = 가격이 먼저. 뉴스가 늘 후행이면 이 축은 진입엔 못 쓴다.
  ② **리프트** P(|수익z|≥2 | 뉴스z≥2) ÷ P(|수익z|≥2). 1.0 이면 아무 정보가 없다는 뜻.
  ③ **순열검정** 종목 안에서 뉴스 계열을 무작위로 섞어 ①을 다시 잰다 — 표본이 크면
     아무 관계 없어도 상관이 0.02 쯤은 나오므로, 그 잡음 분포와 비교해야 실측이 된다.

⚠ **거래일 정렬**: 뉴스는 달력일(토·일 포함), 가격은 거래일이다. 그대로 붙이면 금요일
저녁~일요일 기사가 통째로 사라진다. 그래서 각 거래일의 언급수는 **직전 거래일 다음날부터
그 거래일까지의 달력일 합**으로 접는다(월요일 = 토+일+월). 그러지 않으면 주말 재료가
반영된 월요일 갭이 '뉴스 없는 변곡'으로 오분류된다.

⚠ 상관의 분모는 종목·날의 곱이라 커 보인다. 유효표본은 종목수 × 거래일수지 독립표본이
아니다(같은 날 시장 전체가 같이 움직인다) — 순열검정도 그 종속을 완전히 지우진 못한다.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def fold_to_trading_days(mentions: pd.DataFrame, trading_days: list[str]) -> pd.DataFrame:
    """달력일 언급 행렬 → 거래일 행렬(직전 거래일 이후 달력일 전부를 그 거래일에 접는다)."""
    if mentions.empty:
        return mentions
    idx = pd.to_datetime(mentions.index)
    m = mentions.copy()
    m.index = idx
    td = pd.to_datetime(pd.Index(trading_days))
    bins = pd.cut(idx, bins=[td[0] - pd.Timedelta(days=7)] + list(td),
                  labels=td, right=True)
    folded = m.groupby(bins, observed=False).sum()
    folded.index = [str(d)[:10] for d in folded.index]
    return folded.reindex(trading_days).fillna(0.0)


def lead_lag(retz: pd.DataFrame, newsz: pd.DataFrame,
             lags: range = range(-5, 6)) -> list[dict]:
    """|수익z| 와 뉴스z 의 리드/래그 상관(종목·날 풀링)."""
    a = retz.abs()
    out = []
    for k in lags:
        b = newsz.shift(-k)          # k<0 → 뉴스가 과거로 = 뉴스 선행
        x = a.to_numpy().ravel()
        y = b.reindex_like(a).to_numpy().ravel()
        ok = np.isfinite(x) & np.isfinite(y)
        n = int(ok.sum())
        r = float(np.corrcoef(x[ok], y[ok])[0, 1]) if n > 100 else float("nan")
        out.append({"lag": k, "corr": round(r, 4), "n": n,
                    "meaning": "뉴스 선행" if k < 0 else ("동일일" if k == 0 else "가격 선행")})
    return out


def lift_table(retz: pd.DataFrame, newsz: pd.DataFrame,
               ret_thr: float = 2.0, news_thr: float = 2.0) -> dict:
    x = retz.abs().to_numpy().ravel()
    y = newsz.to_numpy().ravel()
    ok = np.isfinite(x) & np.isfinite(y)
    x, y = x[ok], y[ok]
    if len(x) < 100:
        return {"n": int(len(x)), "error": "표본 부족"}
    big = x >= ret_thr
    hot = y >= news_thr
    base = float(big.mean())
    cond = float(big[hot].mean()) if hot.sum() else float("nan")
    rev = float(hot[big].mean()) if big.sum() else float("nan")
    return {
        "n": int(len(x)),
        "P(|retz|>=%.1f)" % ret_thr: round(base, 4),
        "P(|retz|>=%.1f | newsz>=%.1f)" % (ret_thr, news_thr): round(cond, 4),
        "lift": round(cond / base, 3) if base else None,
        "P(newsz>=%.1f | |retz|>=%.1f)" % (news_thr, ret_thr): round(rev, 4),
        "n_hot": int(hot.sum()), "n_big": int(big.sum()),
    }


def permutation_null(retz: pd.DataFrame, newsz: pd.DataFrame,
                     iters: int = 200, seed: int = 7, mode: str = "per_ticker") -> dict:
    """뉴스 계열을 순환이동(circular shift)해 만든 귀무분포. 자기상관은 보존하고 정렬만 깬다.

    ⚠ **귀무를 두 개 써야 한다.** 어느 걸 쓰느냐가 결론을 바꾼다.
      · `per_ticker` — 종목마다 다른 만큼 민다. 종목별 정렬은 깨지지만 **'시장이 시끄러운 날'
        구조까지 같이 깨진다.** 그래서 "뉴스 많은 날 = 많이 움직이는 날"이라는 시장 수준의
        동시성만으로도 유의가 나온다 — 종목 고유 정보라는 증거가 못 된다.
      · `common`  — 모든 종목을 **같은 만큼** 민다. 날짜의 시장 구조(어느 날이 시끄러웠나)를
        그대로 둔 채 뉴스와 가격의 날짜 정렬만 어긋낸다. 이걸 통과해야 '종목 단위 정보'다.
    """
    rng = np.random.default_rng(seed)
    a = retz.abs()
    x = a.to_numpy().ravel()
    obs_y = newsz.reindex_like(a).to_numpy()
    ok0 = np.isfinite(x) & np.isfinite(obs_y.ravel())
    obs = float(np.corrcoef(x[ok0], obs_y.ravel()[ok0])[0, 1])
    nrow = obs_y.shape[0]
    null = []
    for _ in range(iters):
        if mode == "common":
            sh = np.roll(obs_y, int(rng.integers(1, nrow)), axis=0)
        else:
            sh = np.empty_like(obs_y)
            for j in range(obs_y.shape[1]):
                sh[:, j] = np.roll(obs_y[:, j], int(rng.integers(1, nrow)))
        y = sh.ravel()
        ok = np.isfinite(x) & np.isfinite(y)
        if ok.sum() > 100:
            null.append(float(np.corrcoef(x[ok], y[ok])[0, 1]))
    null_arr = np.array(null)
    p = float((np.abs(null_arr) >= abs(obs)).mean()) if len(null_arr) else float("nan")
    return {"mode": mode, "observed_corr": round(obs, 4),
            "null_mean": round(float(null_arr.mean()), 4),
            "null_sd": round(float(null_arr.std()), 4), "iters": len(null_arr),
            "p_two_sided": round(p, 4)}


def baseline_forward(panel_returns: pd.DataFrame) -> dict:
    """**무조건부 기준선** — 같은 창의 아무 종목·아무 날의 5·20일 선행수익.

    이게 없으면 "급등 뒤 5일 -1.9%"가 되돌림인지 그냥 그 기간 시장이 빠진 건지 구분이
    안 된다. 조건부 수익은 반드시 이 기준선과 **차이로** 읽는다.
    """
    out = {}
    for n in (5, 20):
        fwd = panel_returns.rolling(n).sum().shift(-n)
        v = fwd.to_numpy().ravel()
        v = v[np.isfinite(v)]
        out[f"fwd{n}"] = {
            "n": int(len(v)),
            "mean_pct": round(float(v.mean()) * 100, 3),
            "median_pct": round(float(np.median(v)) * 100, 3),
            "win_rate": round(float((v > 0).mean()), 3),
        }
    return out


def day_clustered(events: list[dict], key: str = "fwd5") -> dict:
    """**날짜로 묶은** 이벤트 통계 — 이 모듈에서 가장 중요한 함수다.

    왜: 변곡은 종목마다 독립적으로 일어나지 않는다. 실측 2026-06-08 하루에 급락충격
    **65건/233건**이 몰렸다. 그걸 233개 독립표본으로 세면 "급락 뒤 5일 +3.05%, t=6.55"
    라는 압도적 결과가 나오는데, 실제로는 **'6/8 에 시장이 빠졌다가 되돌았다'는 관측 하나**를
    65번 센 것이다. 하루를 한 표본으로 접으면 같은 데이터가 −1.03% ± 1.39pp(=효과 없음)가 된다.

    그래서 이 모듈은 **날짜 단위(clustered)를 기본 보고 단위**로 삼는다. pooled 값은
    비교용으로만 함께 낸다 — 둘이 크게 다르면 그 결과는 소수의 시장 사건이 만든 것이다.
    """
    from collections import defaultdict
    by_kind: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for e in events:
        v = e.get(key)
        if v is None or not np.isfinite(v):
            continue
        by_kind[e["kind"]][e["date"]].append(float(v))
    out = {}
    for kind, per_day in sorted(by_kind.items()):
        flat = np.array([v for vs in per_day.values() for v in vs], dtype=float)
        daily = np.array([float(np.mean(vs)) for vs in per_day.values()], dtype=float)
        top = max(len(vs) for vs in per_day.values())
        se = float(daily.std(ddof=1)) / np.sqrt(len(daily)) if len(daily) > 1 else float("nan")
        out[kind] = {
            "n_events": int(len(flat)), "n_days": int(len(daily)),
            "largest_day_share": round(top / len(flat), 3),
            "pooled_mean_pct": round(float(flat.mean()) * 100, 2),
            "day_mean_pct": round(float(daily.mean()) * 100, 2),
            "day_se_pp": round(se * 100, 2),
            "day_t": round(float(daily.mean()) / (se or np.nan), 2),
        }
    return out


def split_by_news(events: list[dict], newsz_lookup, thr: float = 1.5,
                  baseline: dict | None = None) -> dict:
    """변곡을 '뉴스 동반 / 조용 / 측정불가'로 갈라 이후 수익 분포를 비교.

    이게 이 실험의 핵심 질문이다 — **재료 있는 변곡이 더 오래가나**.

    ⚠ 세 번째 칸(unknown)이 있는 이유: 뉴스z 는 30일 baseline 이 필요해 창 초반(5월 초)
    이벤트는 **NaN** 이다. NaN 을 'quiet' 에 넣으면 '뉴스 없는 변곡' 표본이 5월 초 이벤트로
    오염된다 — 모른다와 없다는 다르다(P4).
    """
    groups: dict[str, dict[str, list]] = {}
    for e in events:
        z = newsz_lookup(e["ticker"], e["date"])
        if z is None or not np.isfinite(z):
            tag = "unknown"
        else:
            tag = "news" if z >= thr else "quiet"
        g = groups.setdefault(e["kind"], {"news": [], "quiet": [], "unknown": []})
        if e.get("fwd5") is not None:
            g[tag].append((e["fwd5"], e.get("fwd20"), e["z"]))
    out = {}
    for kind, g in sorted(groups.items()):
        row = {}
        for tag, vals in g.items():
            if not vals:
                row[tag] = {"n": 0}
                continue
            f5 = np.array([v[0] for v in vals], dtype=float)
            f20 = np.array([v[1] for v in vals if v[1] is not None], dtype=float)
            b5 = (baseline or {}).get("fwd5", {}).get("mean_pct")
            b20 = (baseline or {}).get("fwd20", {}).get("mean_pct")
            m5 = float(f5.mean()) * 100
            m20 = float(f20.mean()) * 100 if len(f20) else None
            row[tag] = {
                "n": len(f5),
                "fwd5_mean_pct": round(m5, 3),
                "fwd5_median_pct": round(float(np.median(f5)) * 100, 3),
                "fwd5_win_rate": round(float((f5 > 0).mean()), 3),
                # 초과 = 같은 창의 무조건부 평균을 뺀 값. 시장 드리프트가 상쇄된다.
                "fwd5_excess_pp": round(m5 - b5, 3) if b5 is not None else None,
                "fwd20_mean_pct": round(m20, 3) if m20 is not None else None,
                "fwd20_excess_pp": round(m20 - b20, 3) if (m20 is not None and b20 is not None) else None,
                "n20": int(len(f20)),
            }
        out[kind] = row
    return out
