from heapq import heappush, heappop

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

nodes = [[] for _ in range(N + 1)]
for a, b, c in edges:
    nodes[a].append((b, c))
    nodes[b].append((a, c))

# Dijkstra
INFINITY = 10**10  # 無限長を表す値
confirmed_node = [False] * (N + 1)  # 確定したノードかどうか
cur = [INFINITY] * (N + 1)  # 暫定最短距離
cur[1] = 0

Q = []  # プライオリティキュー
heappush(Q, (0, 1))  # 第一引数が小さい順に取り出せるため(距離, 頂点番号)を格納

while Q:
    position = heappop(Q)[1]  # 頂点番号

    # 確定していたらスキップ
    if confirmed_node[position]:
        continue

    # cur[x] の値を更新
    confirmed_node[position] = True
    for next_position, distance in nodes[position]:
        if cur[next_position] > cur[position] + distance:  # 確定ノードはこの条件を満たさない
            cur[next_position] = cur[position] + distance  # 暫定最短距離を更新
            heappush(Q, (cur[next_position], next_position))

for i in range(1, N + 1):
    if cur[i] == INFINITY:
        print("-1")
    else:
        print(cur[i])
