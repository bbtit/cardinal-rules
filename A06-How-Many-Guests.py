N, Q = map(int, input().split()) # N日間、Q個のクエリ
A = list(map(int, input().split()))

L = [None] * Q
R = [None] * Q

for i in range(Q):
    L[i], R[i] = map(int, input().split())

S = [None] * (N + 1)
S[0] = 0

for i in range(N):
    S[i + 1] = S[i] + A[i]

for j in range(Q):
    print(S[R[j]] - S[L[j] - 1])
