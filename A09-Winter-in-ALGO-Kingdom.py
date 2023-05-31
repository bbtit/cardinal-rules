# REの場合は配列外参照の場合が多い
H, W, N = map(int, input().split())
A = [None] * N
B = [None] * N
C = [None] * N
D = [None] * N

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

M = [[0] * (W+2) for i in range(H+2)]

for i in range(N):
    # 左上
    M[A[i]][B[i]] += 1
    # 右上
    M[A[i]][D[i]+1] -= 1
    # 左下
    M[C[i]+1][B[i]] -= 1
    # 右下
    M[C[i]+1][D[i]+1] += 1

# 累積和
Z = [[0] * (W+2) for _ in range(H+2)]
for y in range(1, H+1):
    for x in range(1, W+1):
        Z[y][x] = Z[y][x-1] + M[y][x]

for x in range(1, W+1):
    for y in range(1, H+1):
        Z[y][x] = Z[y-1][x] + Z[y][x]

for y in range(1, H+1):
    for x in range(1, W+1):
        if x >= 2:
            print(" ", end="")
        print(Z[y][x], end="")
    print("")
