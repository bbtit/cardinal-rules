# N:頂点数, M:辺数
N, M = map(int, input().split())
# i番目の辺は頂点A[i]と頂点B[i]を結ぶ
A = [None] * (M + 1)
B = [None] * (M + 1)

for i in range(1, M + 1):
    A[i], B[i] = map(int, input().split())

# グラフの隣接リスト表現
G = [[] for i in range(N + 1)]

for i in range(1, M + 1):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

for i in range(1, N + 1):
    print(f"{i}:  {{{', '.join(map(str, G[i]))}}}")
