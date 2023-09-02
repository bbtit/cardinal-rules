import sys

sys.setrecursionlimit(1200000)


def dfs(pos, G, visited):
    visited[pos] = True
    for to in G[pos]:
        if not visited[to]:
            dfs(to, G, visited)


N, M = map(int, input().split())
Edge = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N + 1)]
for a, b in Edge:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)
dfs(1, G, visited)

# すべての頂点を訪問できたかどうかチェック
answer = True
for i in range(1, N + 1):
    if not visited[i]:
        answer = False

print("The graph is connected." if answer else "The graph is not connected.")
