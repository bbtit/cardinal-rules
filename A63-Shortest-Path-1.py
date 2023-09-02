from collections import deque

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

distances = [-1] * (N + 1)
distances[1] = 0

Q = deque()
Q.append(1)

while Q:
    pos = Q.popleft()
    for next_pos in graph[pos]:
        # 未到達な頂点の場合
        if distances[next_pos] == -1:
            distances[next_pos] = distances[pos] + 1
            Q.append(next_pos)

for i in range(1, N + 1):
    print(distances[i])
