import bisect
import sys

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# 配列Pを作成
P = []
for x in range(N):
    for y in range(N):
        P.append(A[x] + B[y])

# 配列Qを作成
q = []
for z in range(N):
    for w in range(N):
        q.append(C[z] + D[w])

# 配列Qを二分探索のためにソート
q.sort()

# 二分探索
for i in range(len(P)):
    position = bisect.bisect_left(q, K - P[i])
    if position < N*N and q[position] == K - P[i]:
        print("Yes")
        sys.exit()

print("No")
