N, K = map(int, input().split())

way = 0

for r in range(1, N+1):
    for b in range(1, N+1):
        w = K - r - b
        if w >= 1 and w <= N:
            way += 1

print(way)
