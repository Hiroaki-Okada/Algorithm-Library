from heapq import *


# Dijkstra 法
def dijkstra(tree, ini_node, inf=1e18):
    '''
    Parameters
    ----------
    tree : list
        重み付き無向連結グラフの隣接リスト
    ini_node : int
        初期ノード

    Returns
    ----------
    dist : list
        ini_node から各頂点への距離が格納されたリスト
    prev : list
        最短経路において i 番目の頂点の 1 つ前に通る頂点が i 番目の要素に格納されたリスト
    '''

    # 距離計算用
    dist = [inf] * len(tree)
    dist[ini_node] = 0

    # 経路復元用
    prev = [-1 for i in range(len(tree))]

    # 初期ノードの情報を優先度付きキューに格納
    que = [(0, ini_node)]
    heapify(que)

    while que:
        weight, v_curr = heappop(que)

        # 今見ている頂点(v_curr)の重みより小さい
        if dist[v_curr] < weight:
            continue

        # v_curr から伸びる頂点の情報を優先度付きキューに追加
        for v_next, cost in tree[v_curr]:
            ncost = weight + cost
            if ncost < dist[v_next]:
                prev[v_next] = v_curr
                dist[v_next] = ncost
                heappush(que, (ncost, v_next))

    return dist, prev


# 経路復元 : 終点から逆に最短経路を辿っていく
def get_shortest_path(node, prev):
    shortest_path = []
    # 今の頂点を shortest_path に追加した後、今の頂点を 1 つ前の頂点に更新
    while node != -1:
        shortest_path.append(node)
        node = prev[node]

    shortest_path.reverse()

    return shortest_path


n = int(input())
k = 0

tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append([b, c])
    tree[b].append([a, c])

dist, prev = dijkstra(tree, ini_node=k)
path = prev[k]