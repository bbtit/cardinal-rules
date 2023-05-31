
N = int(input())

X = [None] * N
Y = [None] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

Q = int(input())

A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q

for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 各座標の点を数える
S = [[0] * 1501 for _ in range(1501)]
for i in range(N):
    # ここのY,Xの順番で座標軸の向きが変わる
    # クエリの順番と一致させること
    S[Y[i]][X[i]] += 1

# 累積和
T = [[0] * 1501 for _ in range(1501)]
for y in range(1, 1501):
    for x in range(1, 1501):
        T[y][x] = T[y][x-1] + S[y][x]

for x in range(1, 1501):
    for y in range(1, 1501):
        T[y][x] += T[y-1][x]

for i in range(Q):
    ans = T[D[i]][C[i]] + T[B[i]-1][A[i]-1] - T[D[i]][A[i]-1] - T[B[i]-1][C[i]]
    print(ans)
