"""Rebuildable evidence credit, capped advice and probability calibration.

Beta quantiles always use a continued fraction for regularized incomplete beta
and bisection (no normal approximation). n/hits/misses count rows without the
backfill discount; only wsum/contribution are discounted. Callers own commits.
"""
from __future__ import annotations

import math
from datetime import datetime, timezone

from module_lens._score import _branches, _ensure_schema, _number, _rows, brier


def _beta_fraction(a, b, x):
    """Modified Lentz continued fraction for incomplete beta."""
    tiny, eps = 1e-300, 3e-14
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) >= tiny else tiny)
    value = d
    for m in range(1, 1001):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        c = 1.0 + aa / c
        d = 1.0 / (d if abs(d) >= tiny else tiny)
        c = c if abs(c) >= tiny else tiny
        value *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        c = 1.0 + aa / c
        d = 1.0 / (d if abs(d) >= tiny else tiny)
        c = c if abs(c) >= tiny else tiny
        delta = d * c
        value *= delta
        if abs(delta - 1.0) < eps:
            break
    return value


def _beta_cdf(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    factor = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                      + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return factor * _beta_fraction(a, b, x) / a
    return 1.0 - factor * _beta_fraction(b, a, 1.0 - x) / b


def beta_interval(a, b, q) -> float | None:
    """Beta(a,b) quantile at q, to about 1e-14 absolute x accuracy."""
    a, b, q = _number(a), _number(b), _number(q)
    if a is None or b is None or q is None or min(a, b) <= 0 or not 0 <= q <= 1:
        return None
    if q in (0.0, 1.0):
        return q
    lo, hi = 0.0, 1.0
    for _ in range(64):
        mid = (lo + hi) / 2.0
        if _beta_cdf(a, b, mid) < q:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def learn(con) -> list[dict]:
    _ensure_schema(con)
    questions = {r["id"]: r for r in _rows(con, "SELECT id,branches FROM questions")}
    outcomes = {r["question"]: r["fired"] for r in _rows(con, "SELECT question,fired FROM outcomes")}
    aggregates = {}
    for e in _rows(con, "SELECT * FROM evidence WHERE dead IS NULL AND weight>0 AND supports!=''"):
        q = questions.get(e["question"])
        fired = outcomes.get(e["question"])
        if fired in (None, "VOID", "AMBIGUOUS") or q is None:
            continue
        if fired not in [branch.get("k") for branch in _branches(q["branches"])]:
            continue
        weight = _number(e["weight"])
        if weight is None:
            continue
        w = weight / 100.0 * (0.5 if e["backfilled"] else 1.0)
        hit = e["supports"] == fired
        for level in ("method", "kind", "key"):
            name = e[level]
            if not name:
                continue
            row = aggregates.setdefault((level, name),
                                        {"n": 0, "hits": 0, "misses": 0,
                                         "wsum": 0.0, "contrib": 0.0})
            row["n"] += 1
            row["hits" if hit else "misses"] += 1
            row["wsum"] += w
            row["contrib"] += w if hit else -w
    now = datetime.now(timezone.utc).isoformat()
    results = []
    for (level, name), values in sorted(aggregates.items()):
        row = dict(level=level, name=name, **values)
        row["cred"] = row.pop("contrib") / (row["wsum"] + 5.0)
        a, b = 1 + row["hits"], 1 + row["misses"]
        row.update(beta_mean=a / (a + b), lo80=beta_interval(a, b, 0.1),
                   hi80=beta_interval(a, b, 0.9), updated=now)
        results.append(row)
    # Savepoint avoids a partially rebuilt table without committing a caller's work.
    con.execute("SAVEPOINT lens_learn")
    try:
        con.execute("DELETE FROM credit")
        for row in results:
            con.execute("""INSERT INTO credit
                (level,name,n,hits,misses,wsum,cred,beta_mean,lo80,hi80,updated)
                VALUES (:level,:name,:n,:hits,:misses,:wsum,:cred,:beta_mean,:lo80,:hi80,:updated)""", row)
        con.execute("RELEASE lens_learn")
    except Exception:
        con.execute("ROLLBACK TO lens_learn")
        con.execute("RELEASE lens_learn")
        raise
    return results


def set_impact(con, rows):
    """Upsert {kind,key,mult,n,src} dicts. Invalid/missing rows are reported."""
    _ensure_schema(con)
    result = []
    for row in rows or []:
        mult = _number(row.get("mult"))
        n = _number(row.get("n", 0))
        if not row.get("kind") or not row.get("key") or mult is None or mult < 0 or n is None or n < 0:
            result.append(dict(row, reason="missing/invalid impact fields"))
            continue
        con.execute("""INSERT INTO impact(kind,key,mult,n,src) VALUES (?,?,?,?,?)
            ON CONFLICT(kind,key) DO UPDATE SET mult=excluded.mult,
            n=excluded.n,src=excluded.src""",
                    (row["kind"], row["key"], mult, int(n), row.get("src")))
        result.append(dict(row, mult=mult, n=int(n)))
    return result


def _weights(scores):
    count = len(scores)
    if count == 0:
        return []
    if count < 3:
        weights = [100.0 / count] * count
    else:
        weights, remaining, budget = [0.0] * count, list(range(count)), 100.0
        while remaining:
            total = sum(scores[i] for i in remaining)
            proposed = {i: (budget * scores[i] / total if total > 0 else budget / len(remaining))
                        for i in remaining}
            capped = [i for i in remaining if proposed[i] > 40.0]
            if not capped:
                for i in remaining:
                    weights[i] = proposed[i]
                break
            for i in capped:
                weights[i] = 40.0
                budget -= 40.0
                remaining.remove(i)
    largest = max(range(count), key=lambda i: weights[i])
    rounded = [round(w * 2.0) / 2.0 for w in weights]
    residual = 100.0 - sum(rounded)
    # Nearest-half ties use Python's ties-to-even rule. Repair only if the
    # positive residual would break a saturated largest item's 40% ceiling;
    # then put the final residual on the largest item, as the contract requires.
    if count >= 3:
        for i in sorted(range(count), key=lambda i: weights[i] - rounded[i], reverse=True):
            if i != largest and rounded[i] < 40 and rounded[largest] + residual > 40:
                rounded[i] += 0.5
                residual -= 0.5
        # With hundreds of tiny items nearest-half rounding can overshoot 100
        # by more than the largest weight. Keep the residual recipient nonnegative.
        for i in sorted(range(count), key=lambda i: rounded[i] - weights[i], reverse=True):
            if i != largest and rounded[i] >= 0.5 and rounded[largest] + residual < 0:
                rounded[i] -= 0.5
                residual += 0.5
    rounded[largest] += residual
    return rounded


def _flow_cap(items, weights):
    """수급·포지셔닝 항목의 합을 FLOW_CAP 안으로 — 넘친 몫은 나머지 항목에 비례해 나눈다(0.5 단위, 합 100 유지).
    나머지 항목이 없으면(전부 수급) 그대로 둔다 — 그런 물음은 think 가 거절한다."""
    from . import _config
    FLOW_CAP = getattr(_config, "FLOW_CAP", 30.0)          # 테스트가 끼워 넣는 가짜 _config 에는 없을 수 있다
    FLOW_KINDS = getattr(_config, "FLOW_KINDS", ("flow", "positioning"))
    fi = [i for i, it in enumerate(items) if it.get("kind") in FLOW_KINDS]
    oi = [i for i in range(len(items)) if i not in fi]
    fsum = sum(weights[i] for i in fi)
    if not fi or not oi or fsum <= FLOW_CAP:
        return weights
    w = list(weights)
    for i in fi:
        w[i] = round(weights[i] * FLOW_CAP / fsum * 2) / 2
    osum = sum(weights[i] for i in oi) or len(oi)
    rest = 100 - sum(w[i] for i in fi)
    for i in oi:
        w[i] = round(((weights[i] if sum(weights[j] for j in oi) else 1) / osum) * rest * 2) / 2
    big = max(oi, key=lambda i: w[i])
    w[big] += 100 - sum(w)
    return w


def advise(con, items) -> list[dict]:
    _ensure_schema(con)
    items = list(items or [])
    if not items:
        return []
    credits = {(r["level"], r["name"]): r for r in _rows(con, "SELECT * FROM credit")}
    impacts = {(r["kind"], r["key"]): r["mult"] for r in _rows(con, "SELECT * FROM impact")}
    histories, scores, reasons = [], [], []
    for item in items:
        history = [(level, credits[(level, item.get(level))])
                   for level in ("key", "method", "kind") if (level, item.get(level)) in credits]
        histories.extend(row.get("n") or 0 for _, row in history)
        level, row = history[0] if history else ("none", {})
        cred = _number(row.get("cred"))
        cred = max(cred if cred is not None else 0.05, 0.05)
        impact = _number(impacts.get((item.get("kind"), item.get("key")), 1.0))
        impact = impact if impact is not None and impact >= 0 else 1.0
        scores.append(impact * cred)
        reasons.append(f"{level} credit; n={row.get('n', 0)}; impact={impact:g}; floor=0.05")
    equal = not any(n >= 10 for n in histories)
    if equal:
        scores = [1.0] * len(items)
        reasons = ["equal: every available history has n<10"] * len(items)
    weights = _flow_cap(items, _weights(scores))
    result = []
    for item, weight, reason in zip(items, weights, reasons):
        if len(items) < 3:
            reason += "; equal: 40% cap infeasible with fewer than 3 items"
        elif not equal and weight == 40:
            reason += "; 40% cap with redistribution"
        result.append(dict(item, weight=weight, reason=reason))
    return result


def calib(con) -> dict:
    """Probability means/frequencies are fractions; bucket bounds are percent.

    Buckets are [0,20), ... [80,100]. Only genuine branch outcomes contribute.
    Missing probabilities skip that branch; missing Brier skips grouped means.
    Alive kinds include context/zero-weight evidence and count each question once.
    """
    _ensure_schema(con)
    buckets = [{"lo": lo, "hi": lo + 20, "count": 0,
                "predicted_mean": None, "observed_frequency": None} for lo in range(0, 100, 20)]
    sums = [[0.0, 0] for _ in buckets]
    kinds = {}
    for row in _rows(con, "SELECT DISTINCT question,kind FROM evidence WHERE dead IS NULL"):
        if row["kind"]:
            kinds.setdefault(row["question"], set()).add(row["kind"])
    desks, by_kind = {}, {}
    for row in _rows(con, """SELECT q.id,q.desk,q.branches,o.fired,o.brier
                            FROM questions q JOIN outcomes o ON o.question=q.id"""):
        branches = _branches(row["branches"])
        if row["fired"] in ("VOID", "AMBIGUOUS") or row["fired"] not in [x.get("k") for x in branches]:
            continue
        for branch in branches:
            p = _number(branch.get("p"))
            if p is None or not 0 <= p <= 100:
                continue
            i = min(int(p // 20), 4)
            buckets[i]["count"] += 1
            sums[i][0] += p / 100.0
            sums[i][1] += branch.get("k") == row["fired"]
        value = _number(row["brier"])
        if value is None:
            value = brier(branches, row["fired"])
        if value is None:
            continue
        desks.setdefault(row["desk"], []).append(value)
        for kind in kinds.get(row["id"], set()):
            by_kind.setdefault(kind, []).append(value)
    for bucket, (predicted, observed) in zip(buckets, sums):
        if bucket["count"]:
            bucket["predicted_mean"] = predicted / bucket["count"]
            bucket["observed_frequency"] = observed / bucket["count"]
    def groups(values, label):
        return [{label: name, "count": len(numbers), "mean_brier": sum(numbers) / len(numbers)}
                for name, numbers in sorted(values.items(), key=lambda pair: str(pair[0]))]
    return {"buckets": buckets, "by_desk": groups(desks, "desk"),
            "by_kind": groups(by_kind, "kind")}
