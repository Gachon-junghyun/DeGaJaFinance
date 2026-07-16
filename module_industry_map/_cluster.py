"""corp pool ticker 리스트 → cosine 유사도 매트릭스 → 가치사슬 노드 클러스터.

corp_embeddings.db 의 사업보고서 임베딩 (3072d) 으로 cosine 매트릭스 계산.
agglomerative clustering 으로 N 개 노드 후보로 묶음.
다른 module_X 직접 import 0 — 자체 numpy / scipy 사용.
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np


DB_PATH = Path(__file__).resolve().parent.parent / "data" / "corp_embeddings.db"


@dataclass
class Cluster:
    cluster_id: int
    members: list[tuple[str, str]]  # [(ticker, corp_name), ...]
    centroid_pairs: list[tuple[int, int]]  # 각 멤버의 인덱스


def _connect() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"corp_embeddings.db 가 없습니다: {DB_PATH}")
    return sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)


def _load_embeddings(tickers: list[str]) -> tuple[list[str], list[str], np.ndarray]:
    """tickers → (valid_tickers, names, embedding matrix [N, D])."""
    valid: list[str] = []
    names: list[str] = []
    embs: list[np.ndarray] = []
    with _connect() as conn:
        for t in tickers:
            cur = conn.execute(
                "SELECT corp_name, embedding FROM corp_descriptions WHERE ticker=? AND embedding IS NOT NULL",
                (t,),
            )
            row = cur.fetchone()
            if not row or not row[1]:
                continue
            valid.append(t)
            names.append(row[0] or "")
            embs.append(np.frombuffer(row[1], dtype=np.float32))
    if not embs:
        return [], [], np.zeros((0, 0))
    matrix = np.vstack(embs)
    # L2 normalize (cosine ↔ dot product)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    matrix = matrix / norms
    return valid, names, matrix


def cosine_matrix(matrix: np.ndarray) -> np.ndarray:
    """L2-normalized [N, D] → [N, N] cosine 유사도."""
    return matrix @ matrix.T


def cluster_tickers(
    tickers: list[str],
    *,
    n_clusters: int = 6,
) -> list[Cluster]:
    """corp pool ticker → N 개 cluster.

    scipy linkage 기반 agglomerative clustering (단일 의존성).
    cosine 유사도가 높은 종목끼리 같은 cluster.
    """
    if len(tickers) < 2:
        return []

    valid_tickers, names, matrix = _load_embeddings(tickers)
    if len(valid_tickers) < 2:
        return []

    # cosine distance = 1 - cosine_similarity
    sim = cosine_matrix(matrix)
    dist = 1.0 - sim
    np.fill_diagonal(dist, 0.0)

    # scipy linkage 사용 — 외부 의존성 최소
    try:
        from scipy.cluster.hierarchy import linkage, fcluster
        from scipy.spatial.distance import squareform
    except ImportError:
        # fallback: 단순 그리디 클러스터링
        return _greedy_cluster(valid_tickers, names, sim, n_clusters)

    # condensed distance matrix
    condensed = squareform(dist, checks=False)
    Z = linkage(condensed, method="average")
    n_eff = min(n_clusters, len(valid_tickers))
    labels = fcluster(Z, t=n_eff, criterion="maxclust")

    clusters: dict[int, Cluster] = {}
    for idx, label in enumerate(labels):
        c = clusters.setdefault(int(label), Cluster(cluster_id=int(label), members=[], centroid_pairs=[]))
        c.members.append((valid_tickers[idx], names[idx]))
        c.centroid_pairs.append((idx, idx))

    # 클러스터를 멤버 수 내림차순
    return sorted(clusters.values(), key=lambda c: -len(c.members))


def _greedy_cluster(
    tickers: list[str], names: list[str], sim: np.ndarray, n_clusters: int,
) -> list[Cluster]:
    """scipy 없을 때 fallback — 그리디 클러스터링."""
    n = len(tickers)
    labels = [-1] * n
    cluster_id = 0
    while -1 in labels and cluster_id < n_clusters:
        # 아직 미할당 idx 중 첫 번째
        seed = labels.index(-1)
        # seed 와 cosine ≥ 0.85 인 모든 idx 같은 클러스터
        for j in range(n):
            if labels[j] == -1 and sim[seed, j] >= 0.85:
                labels[j] = cluster_id
        cluster_id += 1
    # 나머지는 마지막 클러스터로
    for i in range(n):
        if labels[i] == -1:
            labels[i] = cluster_id - 1

    clusters: dict[int, Cluster] = {}
    for idx, label in enumerate(labels):
        c = clusters.setdefault(label, Cluster(cluster_id=label, members=[], centroid_pairs=[]))
        c.members.append((tickers[idx], names[idx]))
        c.centroid_pairs.append((idx, idx))
    return sorted(clusters.values(), key=lambda c: -len(c.members))
