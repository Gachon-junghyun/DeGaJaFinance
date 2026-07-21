# -*- coding: utf-8 -*-
"""과거 유사국면 검색 — "이런 말이 나왔을 때, 그 다음엔 어떻게 흘렀나".

변곡 이벤트 하나 = 그 창(-3…+1일)의 기사 제목 묶음. 그 묶음의 **벡터 평균**을 이벤트의
지문으로 삼고, 새 상황(오늘의 제목들 또는 자유 질의문)과 코사인으로 맞춰 **가장 닮은 과거
이벤트 k개 + 그 이후 실제 수익 분포**를 돌려준다. 답을 지어내지 않고 전례를 꺼내온다.

⚠ **평균중심화 필수** (`_embed` 상단 실측과 같은 이유): 문장 임베딩은 한쪽으로 쏠려 있어
(anisotropy) 아무 상관 없는 기사쌍도 코사인이 높게 나온다. 코퍼스 평균을 빼지 않으면
'가장 닮은 과거'가 사실상 무작위가 된다. 중심화 기준은 **이 코퍼스 전체 평균**이며
`meta` 에 저장해 질의 때도 같은 벡터를 뺀다(기준이 다르면 비교가 성립하지 않는다).

⚠ **벡터는 새로 안 만든다**(P1). 226,081건 제목 임베딩은 이미 `news_vectors.db` 에 있다
(모델 `jhgan/ko-sroberta-multitask`, 768차원, float16). 이벤트 지문은 그걸 평균낼 뿐이다.
GPU 가 필요한 경우는 **자유 텍스트 질의를 인코딩할 때 하나뿐**이고, 그 import 는
함수 안에서만 한다(P6 — 최상단 torch import 는 수집 서버를 기동 불능으로 만든다).

⚠ **k개 전례의 평균수익은 예측이 아니다.** 표본이 수십 건이고 같은 날 시장 전체가 함께
움직인 것들이 섞여 있다(독립표본 아님). 분포와 표본수를 항상 함께 읽는다.
"""
from __future__ import annotations

import json
import sqlite3

import numpy as np

from ._config import VEC_DB

DIM = 768
_SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
    id       TEXT PRIMARY KEY,          -- ticker|date|kind
    ticker   TEXT, name TEXT, sector TEXT,
    date     TEXT, kind TEXT,
    z        REAL, ret REAL,
    fwd1     REAL, fwd5 REAL, fwd20 REAL, prior5 REAL, prior20 REAL,
    n_arts   INTEGER,
    titles   TEXT,                      -- JSON: 창 안 제목(근거)
    vec      BLOB                       -- 중심화+L2정규화된 float32 지문
);
CREATE INDEX IF NOT EXISTS ix_ev_ticker ON events(ticker);
CREATE TABLE IF NOT EXISTS analog_meta (k TEXT PRIMARY KEY, v BLOB);
"""


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript(_SCHEMA)


def _vec_ro() -> sqlite3.Connection:
    return sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)


def corpus_mean(sample: int = 60000) -> np.ndarray:
    """코퍼스 평균벡터(중심화 기준). 표본으로 충분 — 평균은 빨리 수렴한다."""
    src = _vec_ro()
    rows = src.execute("SELECT vec FROM vectors LIMIT ?", (sample,)).fetchall()
    src.close()
    acc = np.zeros(DIM, dtype=np.float64)
    for (blob,) in rows:
        acc += np.frombuffer(blob, dtype=np.float16).astype(np.float64)
    return (acc / max(1, len(rows))).astype(np.float32)


def fetch_vectors(hashes: list[str]) -> np.ndarray:
    """url_hash 목록 → (n,768) float32. 없는 건 조용히 빠진다."""
    if not hashes:
        return np.zeros((0, DIM), dtype=np.float32)
    src = _vec_ro()
    out = []
    for i in range(0, len(hashes), 900):          # sqlite 변수 상한
        part = hashes[i:i + 900]
        q = f"SELECT vec FROM vectors WHERE url_hash IN ({','.join('?' * len(part))})"
        out += [np.frombuffer(b, dtype=np.float16).astype(np.float32)
                for (b,) in src.execute(q, part)]
    src.close()
    return np.vstack(out) if out else np.zeros((0, DIM), dtype=np.float32)


def fingerprint(vecs: np.ndarray, mean: np.ndarray) -> np.ndarray | None:
    """기사 벡터들 → 이벤트 지문(중심화 후 평균, L2정규화). 기사 0건이면 None."""
    if vecs.shape[0] == 0:
        return None
    v = (vecs - mean).mean(axis=0)
    n = np.linalg.norm(v)
    if n == 0:
        return None
    return (v / n).astype(np.float32)


def save_mean(con: sqlite3.Connection, mean: np.ndarray) -> None:
    con.execute("INSERT OR REPLACE INTO analog_meta(k,v) VALUES('corpus_mean',?)",
                (mean.astype(np.float32).tobytes(),))
    con.commit()


def load_mean(con: sqlite3.Connection) -> np.ndarray | None:
    row = con.execute("SELECT v FROM analog_meta WHERE k='corpus_mean'").fetchone()
    return np.frombuffer(row[0], dtype=np.float32).copy() if row else None


def store_event(con: sqlite3.Connection, ev: dict, titles: list[dict],
                vec: np.ndarray | None) -> None:
    con.execute(
        "INSERT OR REPLACE INTO events(id,ticker,name,sector,date,kind,z,ret,"
        "fwd1,fwd5,fwd20,prior5,prior20,n_arts,titles,vec) "
        "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (f"{ev['ticker']}|{ev['date']}|{ev['kind']}", ev["ticker"], ev.get("name"),
         ev.get("sector"), ev["date"], ev["kind"], ev["z"], ev["ret"],
         ev.get("fwd1"), ev.get("fwd5"), ev.get("fwd20"), ev.get("prior5"),
         ev.get("prior20"), len(titles),
         json.dumps(titles, ensure_ascii=False),
         vec.tobytes() if vec is not None else None))


def load_index(con: sqlite3.Connection) -> tuple[list[dict], np.ndarray]:
    rows = con.execute(
        "SELECT id,ticker,name,sector,date,kind,z,fwd1,fwd5,fwd20,n_arts,titles,vec "
        "FROM events WHERE vec IS NOT NULL").fetchall()
    metas, vecs = [], []
    for r in rows:
        metas.append({"id": r[0], "ticker": r[1], "name": r[2], "sector": r[3],
                      "date": r[4], "kind": r[5], "z": r[6], "fwd1": r[7],
                      "fwd5": r[8], "fwd20": r[9], "n_arts": r[10],
                      "titles": json.loads(r[11] or "[]")})
        vecs.append(np.frombuffer(r[12], dtype=np.float32))
    return metas, (np.vstack(vecs) if vecs else np.zeros((0, DIM), dtype=np.float32))


def encode_query(text: str, mean: np.ndarray) -> np.ndarray:
    """자유 텍스트 → 지문. **여기서만 GPU 모델이 필요**하다(lazy import, P6)."""
    from sentence_transformers import SentenceTransformer   # noqa: PLC0415 (의도적)
    from module_news_data._embed import MODEL_NAME

    model = SentenceTransformer(MODEL_NAME)
    v = model.encode([text], normalize_embeddings=True)[0].astype(np.float32)
    v = v - mean
    return (v / np.linalg.norm(v)).astype(np.float32)


def search(con: sqlite3.Connection, query_vec: np.ndarray, k: int = 10,
           exclude_ticker: str | None = None, before: str | None = None) -> dict:
    metas, mat = load_index(con)
    if mat.shape[0] == 0:
        return {"error": "인덱스가 비었다 — `build` 먼저"}
    sims = mat @ query_vec
    order = np.argsort(-sims)
    hits = []
    for i in order:
        m = metas[i]
        if exclude_ticker and m["ticker"] == exclude_ticker:
            continue
        if before and m["date"] >= before:
            continue                       # 미래 전례를 끌어오면 그건 컨닝이다
        hits.append({**m, "sim": round(float(sims[i]), 4),
                     "titles": m["titles"][:6]})
        if len(hits) >= k:
            break
    f5 = np.array([h["fwd5"] for h in hits if h["fwd5"] is not None], dtype=float)
    f20 = np.array([h["fwd20"] for h in hits if h["fwd20"] is not None], dtype=float)
    summary = {
        "k": len(hits),
        "fwd5_mean_pct": round(float(f5.mean()) * 100, 2) if len(f5) else None,
        "fwd5_median_pct": round(float(np.median(f5)) * 100, 2) if len(f5) else None,
        "fwd5_win_rate": round(float((f5 > 0).mean()), 3) if len(f5) else None,
        "fwd20_mean_pct": round(float(f20.mean()) * 100, 2) if len(f20) else None,
        "n_fwd5": int(len(f5)), "n_fwd20": int(len(f20)),
    }
    return {"summary": summary, "hits": hits}
