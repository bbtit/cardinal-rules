# TLE
D = int(input())
N = int(input())

L = [None] * N
R = [None] * N

for i in range(N):
    L[i], R[i] = map(int, input().split())

ans = [0] * (D + 1)

for l, r in zip(L, R):
    for i in range(l, r+1):
        ans[i] += 1

for j in range(1, D+1):
    print(ans[j])