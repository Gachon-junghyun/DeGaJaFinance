# -*- coding: utf-8 -*-
"""제목 → 문장 임베딩 (클라이언트 전용, GPU). 사건 클러스터링의 재료.

왜 임베딩인가 — 실측으로 다른 길을 전부 소진했다. 어휘 기반(자카드/코사인/오버랩)은
같은 사건을 못 묶는다: 임계를 낮추면 763~1,279건짜리 블롭이 생기고(single-link 연쇄),
average-link 로 연쇄를 막으면 폭락 기사 54건이 18~24 덩어리로 파편화됐다. LSA(200차원)는
`[포토]` 81건·`AI` 71건 처럼 **토픽**으로 뭉쳐 더 나빴다. "코스피 4%대 급락…삼전 6%↓" 와
"[속보] 코스피 급락에 매도 사이드카 발동" 이 같은 사건이라는 건 문장 의미로만 알 수 있다.
문장 임베딩으로 바꾸니 2매체+ 사건이 240 → 512개, 폭락 파편이 18 → 5 덩어리가 됐다.

⚠ **평균중심화(mean-centering)가 필수다.** 임베딩은 한쪽으로 쏠려 있어(anisotropy) 무작위
기사쌍끼리도 코사인이 높다 — 실측 e5-base +0.772 / ko-sroberta +0.148. 그대로 쓰면 e5 는
**3,774건 전부를 한 덩어리**로 만든다. 평균을 빼면 -0.003 으로 펴진다. 다만 중심화는
'무엇을 모아놓고 재느냐'에 달렸으므로 여기서 하지 않고 **클러스터 단계**(그날 모집단 기준)가
한다. 이 파일은 L2 정규화된 원본 벡터만 저장한다.

⚠ **torch/sentence-transformers 를 모듈 최상단에서 import 하지 않는다.** 서버(수집 전용,
저사양·GPU 없음)가 `__main__.build_parser` 를 부르면서 이 파일을 import 하는데, 최상단에
torch 가 있으면 **서버가 기동 못 한다**. 무거운 import 는 실제 인코딩 함수 안에서만.
같은 이유로 `embed` 는 `DB_READ_CMDS` 에 넣지 않는다 — 원격 실행 대상이 아니라 GPU 가 있는
클라이언트에서만 도는 명령이다.

⚠ 운영 전제: 서버는 24시간 수집, 이 PC 는 **켤 때만**. 그래서 증분 '따라잡기' 구조다 —
켤 때마다 못 받은 만큼만 받아 임베딩한다(실측 GPU 2,082건/초: 하루치 2초 · 한 달치 61초).

사용:
    python -m module_news_data embed sync        # 서버에서 새 기사 받아 → 임베딩
    python -m module_news_data embed status      # 현황(커서·건수·모델)
"""
from __future__ import annotations

import sqlite3
from datetime import datetime

from ._config import DATA_DIR, utf8_stdout
from ._export import pull
from ._timeaxis import market_day

VEC_DB = DATA_DIR / "news_vectors.db"   # 클라이언트 소유 파생물 — 서버 DB 는 안 건드린다

MODEL_NAME = "jhgan/ko-sroberta-multitask"   # 한국어 STS 학습. 실측: e5-base 보다 파편화 적음
MODEL_DIM = 768
BATCH = 256                                   # 3080 기준 VRAM 2.7GB
_DTYPE = "float16"                            # 건당 1.5KB — 1년 2.4GB. 코사인은 float32 로 올려 계산


def _connect() -> sqlite3.Connection:
    """스키마 보증 + 마이그레이션. `market_day` 는 **저장 시점에 계산해 둔다**(비정규화).

    ⚠ `published_at` 은 소스마다 포맷이 5종(RFC2822 ±오프셋/GMT/Z/콜론오프셋/ISO)이라
    **SQL 로 날짜 범위 조회가 불가능**하다. 그대로 두면 하루치를 뽑을 때마다 20만행을 전부
    읽어 파싱해야 한다. 그래서 `_timeaxis.market_day` 로 미리 정규화해 색인한다.
    """
    VEC_DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(VEC_DB))
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS articles (
            url_hash TEXT PRIMARY KEY, published_at TEXT, source TEXT, title TEXT);
        CREATE TABLE IF NOT EXISTS vectors (
            url_hash TEXT PRIMARY KEY, vec BLOB, model TEXT, dim INTEGER, embedded_at TEXT);
        CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
        """
    )
    cols = {r[1] for r in con.execute("PRAGMA table_info(articles)")}
    if "market_day" not in cols:
        con.execute("ALTER TABLE articles ADD COLUMN market_day TEXT")
    if "url" not in cols:
        # url 은 ①근거 링크 ②섹션 라벨(분류기 학습셋)에 쓴다. 나중에 추가했으므로 마이그레이션.
        con.execute("ALTER TABLE articles ADD COLUMN url TEXT")
    con.execute("CREATE INDEX IF NOT EXISTS ix_articles_mday ON articles(market_day)")

    # 옛 행 채우기(컬럼을 나중에 넣었으므로). 한 번만 돌고 그 뒤론 0건.
    todo = con.execute("SELECT url_hash, published_at, source FROM articles "
                       "WHERE market_day IS NULL").fetchall()
    if todo:
        con.executemany("UPDATE articles SET market_day=? WHERE url_hash=?",
                        [(market_day(p, s), h) for h, p, s in todo])
        con.commit()
    return con


def _meta_get(con, key, default=None):
    r = con.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
    return r[0] if r else default


def _meta_set(con, key, value):
    con.execute("INSERT INTO meta(key,value) VALUES(?,?) "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, str(value)))


def _encode(titles: list[str], device: str | None = None):
    """제목 → L2 정규화 벡터. **무거운 import 는 여기 안에서만**(위 ⚠ 참조)."""
    import numpy as np
    from sentence_transformers import SentenceTransformer

    if device is None:
        try:
            import torch
            device = "cuda" if torch.cuda.is_available() else "cpu"
        except ImportError:
            device = "cpu"
    model = SentenceTransformer(MODEL_NAME, device=device)
    vecs = model.encode(titles, batch_size=BATCH, normalize_embeddings=True,
                        show_progress_bar=False, convert_to_numpy=True)
    return np.asarray(vecs, dtype=np.float32), device


def sync(limit: int | None = None, device: str | None = None) -> dict:
    """서버에서 새 기사를 당겨(articles) 아직 벡터 없는 것만 임베딩(vectors). 멱등."""
    con = _connect()

    # ── ① 기사 따라잡기 (커서=fetched_at, 서버 수집순서만 단조증가) ─────────
    cursor = _meta_get(con, "cursor")
    data = pull(cursor, limit)
    rows = data.get("rows", [])
    # ⚠ 발행시각 없는 기사는 **버린다**(임베딩도 안 한다). 사건 클러스터는 '그날'을 모집단으로
    # 잡는데 날짜축에 못 올리는 기사는 어느 날에도 속하지 못한다. 실측: 2026-05-01 이전
    # 35,021건이 published_at 빈값(스크래퍼가 5월부터 받기 시작) — `_timeaxis.PUBLISHED_AT_SINCE`.
    # 커서는 그래도 전진시킨다(다시 안 받으려고).
    keep = [r for r in rows if r.get("p")]
    # UPSERT 다 — `INSERT OR IGNORE` 로 두면 나중에 추가한 컬럼(url)이 기존 행에서 영영 빈다.
    # 커서를 되감아 다시 받아도 채워지게 하려면 갱신이어야 한다(벡터는 url_hash 로 유지되니
    # 재임베딩은 안 일어난다).
    con.executemany(
        "INSERT INTO articles(url_hash,published_at,source,title,market_day,url) "
        "VALUES(?,?,?,?,?,?) "
        "ON CONFLICT(url_hash) DO UPDATE SET url=excluded.url, market_day=excluded.market_day",
        [(r["h"], r["p"], r["s"], r["t"], market_day(r["p"], r["s"]), r.get("u"))
         for r in keep])
    if data.get("max_fetched"):
        _meta_set(con, "cursor", data["max_fetched"])
    con.commit()

    # ── ② 모델이 바뀌면 옛 벡터는 비교 불가(공간이 다르다) ─────────────────
    prev = _meta_get(con, "model")
    if prev and prev != MODEL_NAME:
        con.close()
        raise RuntimeError(
            f"모델이 바뀌었다({prev} → {MODEL_NAME}). 벡터는 모델마다 다른 공간이라 섞으면"
            f" 클러스터가 망가진다. {VEC_DB.name} 의 vectors 를 비우고 다시 만들어라.")
    _meta_set(con, "model", MODEL_NAME)

    # ── ③ 벡터 없는 것만 인코딩 ────────────────────────────────────────────
    todo = con.execute(
        "SELECT a.url_hash, a.title FROM articles a "
        "LEFT JOIN vectors v ON v.url_hash = a.url_hash "
        "WHERE v.url_hash IS NULL AND a.title IS NOT NULL AND a.title != ''").fetchall()
    dev = None
    if todo:
        import numpy as np
        vecs, dev = _encode([t for _, t in todo], device)
        now = datetime.now().isoformat()
        con.executemany(
            "INSERT OR REPLACE INTO vectors(url_hash,vec,model,dim,embedded_at) VALUES(?,?,?,?,?)",
            [(h, np.asarray(v, dtype=np.float16).tobytes(), MODEL_NAME, MODEL_DIM, now)
             for (h, _), v in zip(todo, vecs)])
        con.commit()

    n_a = con.execute("SELECT COUNT(*) FROM articles").fetchone()[0]
    n_v = con.execute("SELECT COUNT(*) FROM vectors").fetchone()[0]
    con.close()
    return {"pulled": len(rows), "kept": len(keep), "skipped_no_pub": len(rows) - len(keep),
            "embedded": len(todo), "device": dev,
            "articles": n_a, "vectors": n_v, "cursor": data.get("max_fetched")}


def load_vectors(day: str | None = None, url_hashes: list[str] | None = None):
    """저장된 벡터 로드 → (hashes, meta[], np.ndarray[float32]). `day`=market_day(색인).

    ⚠ 여기서 평균중심화를 하지 않는다 — 중심화 기준은 '무엇을 모아놓고 재느냐'라서
    클러스터 단계가 그날 모집단으로 해야 한다(위 ⚠).
    """
    import numpy as np
    con = _connect()
    q = ("SELECT a.url_hash, a.published_at, a.source, a.title, a.market_day, v.vec, a.url "
         "FROM articles a JOIN vectors v ON v.url_hash = a.url_hash")
    where, p = [], []
    if day:
        where.append("a.market_day = ?"); p.append(day)
    if url_hashes:
        where.append(f"a.url_hash IN ({','.join('?' * len(url_hashes))})")
        p += list(url_hashes)
    if where:
        q += " WHERE " + " AND ".join(where)
    rows = con.execute(q, p).fetchall()
    con.close()
    hashes = [r[0] for r in rows]
    meta = [{"published_at": r[1], "source": r[2], "title": r[3], "market_day": r[4],
             "url": r[6]} for r in rows]
    Z = (np.frombuffer(b"".join(r[5] for r in rows), dtype=np.float16)
         .reshape(len(rows), MODEL_DIM).astype(np.float32)) if rows else np.zeros((0, MODEL_DIM), np.float32)
    return hashes, meta, Z


def status() -> dict:
    con = _connect()
    n_a = con.execute("SELECT COUNT(*) FROM articles").fetchone()[0]
    n_v = con.execute("SELECT COUNT(*) FROM vectors").fetchone()[0]
    out = {"db": str(VEC_DB), "articles": n_a, "vectors": n_v, "missing": n_a - n_v,
           "cursor": _meta_get(con, "cursor"), "model": _meta_get(con, "model")}
    con.close()
    return out


def run(cmd: str, limit: int | None, device: str | None) -> None:
    utf8_stdout()
    if cmd == "status":
        s = status()
        print(f"\n# 임베딩 현황 — {s['db']}")
        print(f"  기사   {s['articles']:>8,}")
        print(f"  벡터   {s['vectors']:>8,}   (미완 {s['missing']:,})")
        print(f"  모델   {s['model']}")
        print(f"  커서   {s['cursor']}  ← 다음 sync 는 이 이후만 받는다")
        return
    r = sync(limit, device)
    dev = f"  [{r['device']}]" if r["device"] else ""
    skip = f" · 발행시각없어 제외 {r['skipped_no_pub']:,}건" if r["skipped_no_pub"] else ""
    print("\n# embed sync")
    print(f"  서버에서 받음 {r['pulled']:,}건{skip} · 새로 임베딩 {r['embedded']:,}건{dev}")
    print(f"  누적 기사 {r['articles']:,} · 벡터 {r['vectors']:,}")
    print(f"  커서 {r['cursor']}")


def cli_register(sub) -> None:
    p = sub.add_parser("embed", help="제목 → 벡터 (클라 전용·GPU). sync=따라잡기 / status=현황")
    p.add_argument("cmd", nargs="?", choices=["sync", "status"], default="sync")
    p.add_argument("--limit", type=int, default=None, help="한 번에 받을 최대 기사수(첫 백필 분할용)")
    p.add_argument("--device", choices=["cuda", "cpu"], default=None, help="기본: 자동감지")
    p.set_defaults(func=lambda a: run(a.cmd, a.limit, a.device))
