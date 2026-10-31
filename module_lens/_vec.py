# -*- coding: utf-8 -*-
"""물음의 의미 검색 — `find` 가 낱말만으로 놓치는 «다른 말로 쓴 같은 물음»을 잡는다.

벡터 = 물음 제목 + 그 물음 근거들의 방법 이름을 한 문장으로 이은 것의 임베딩. 모델은 뉴스와 같은
`module_news_data._embed.MODEL_NAME` (단일 원본 — 여기서 모델을 다시 정하지 않는다).
`q_vec` 는 파생 색인이라 언제든 지우고 `embed` 로 다시 짓는다.

⚠ P6: torch·sentence_transformers 는 `_embed._encode` 안에서만 import 된다. 훅(`hook-prompt`)은 이 파일을
쓰지 않는다 — 모델을 올리는 데 몇 초가 걸려 훅 제한을 넘는다. `find` 를 손으로 부를 때만.
⚠ 모델이 한국어 학습이라 영어 제목(백필 168건은 영어다)의 의미 품질은 재지 않았다(lab/NEWS3D_20261030.md E1).
"""
from __future__ import annotations

import sqlite3


def _text(con: sqlite3.Connection, qid: str) -> str:
    title = (con.execute("SELECT title FROM questions WHERE id=?", (qid,)).fetchone() or [""])[0] or ""
    methods = [m for (m,) in con.execute(
        "SELECT DISTINCT method FROM evidence WHERE question=? AND method IS NOT NULL", (qid,))]
    return title + (" | " + "; ".join(methods) if methods else "")


def embed(con: sqlite3.Connection, all_rows: bool = False) -> dict:
    """q_vec 에 없는(또는 전부) 물음을 인코딩해 넣는다."""
    import numpy as np
    from module_news_data._embed import MODEL_NAME, _encode

    con.execute("CREATE TABLE IF NOT EXISTS q_vec (qid TEXT PRIMARY KEY, vec BLOB, model TEXT)")
    if all_rows:
        con.execute("DELETE FROM q_vec")
    todo = [q for (q,) in con.execute(
        "SELECT id FROM questions WHERE id NOT IN (SELECT qid FROM q_vec WHERE model=?)", (MODEL_NAME,))]
    if not todo:
        return {"embedded": 0}
    vecs, device = _encode([_text(con, q) for q in todo])
    con.executemany("INSERT OR REPLACE INTO q_vec VALUES(?,?,?)",
                    [(q, v.astype(np.float16).tobytes(), MODEL_NAME) for q, v in zip(todo, vecs)])
    con.commit()
    return {"embedded": len(todo), "device": device}


def scores(con: sqlite3.Connection, text: str, top: int = 300) -> dict[str, float]:
    """질의문 → {qid: 코사인}. 상위 top 개만. 벡터가 없으면 빈 dict(=낱말 검색만)."""
    import numpy as np
    from module_news_data._embed import MODEL_NAME, _encode

    rows = con.execute("SELECT qid, vec FROM q_vec WHERE model=?", (MODEL_NAME,)).fetchall()
    if not rows:
        return {}
    M = np.vstack([np.frombuffer(b, dtype=np.float16).astype(np.float32) for _, b in rows])
    q, _ = _encode([text])
    sim = M @ q[0]
    order = np.argsort(-sim)[:top]
    return {rows[i][0]: float(sim[i]) for i in order}
