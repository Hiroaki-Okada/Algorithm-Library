from heapq import *


# Prim 法
def prim(tree):
    '''
    Parameters
    ----------
    tree : list
        重み付き無向連結グラフの隣接リスト

    Returns
    ----------
    total_weight : int
        最小全域木を構成する辺の総コスト
    mst_edges : set
        最小全域木を構成する辺とその重みをまとめた集合
    '''

    # 初期化
    total_weight = 0
    mst_edges = set()

    # 最初の頂点を用意し、訪問済みとする
    ini_node = 0
    seen = [False] * len(tree)
    seen[ini_node] = True

    # 最初の頂点から伸びる辺の情報を優先度付きキューに格納
    que = [(cost, ini_node, v) for v, cost in tree[ini_node]]
    heapify(que)

    while que:
        weight, v_curr, v_next = heappop(que)

        # 次の頂点が訪問済みならスキップ
        if seen[v_next]:
            continue

        seen[v_next] = True

        # 最小全域木の情報を更新
        total_weight += weight
        mst_edges.add((v_curr, v_next, weight))

        # 今見ている頂点(v_next)から伸びる辺の情報を優先度付きキューに追加
        for nv, ncost in tree[v_next]:
            heappush(que, (ncost, v_next, nv))

    return total_weight, mst_edges


# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f
n, m = map(int, input().split())

tree = [[] for i in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    tree[u].append([v, c])
    tree[v].append([u, c])

total_weight, mst_edges = prim(tree)

print(total_weight)