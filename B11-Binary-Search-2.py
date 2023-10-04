import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = [None] * Q

for i in range(Q):
    X[i] = int(input())

A.sort()
for i in range(Q):
    idx = bisect.bisect_left(A, X[i])
    print(idx)
