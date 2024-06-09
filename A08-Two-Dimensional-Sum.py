# 高さと幅
H, W = map(int, input().split())

# 入力行列
input_matrix = [None] * H
for i in range(H):
    input_matrix[i] = list(map(int, input().split()))

# クエリ数
Q = int(input())

A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q

for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 累積和用行列
sum_matrix = [[0] * (W + 1) for _ in range(H + 1)]

# 横方向の累積和
for y in range(1, H + 1):
    for x in range(1, W + 1):
        sum_matrix[y][x] = sum_matrix[y][x - 1] + input_matrix[y - 1][x - 1]


# 縦方向の累積和
for x in range(1, W + 1):
    for y in range(1, H + 1):
        sum_matrix[y][x] += sum_matrix[y - 1][x]


for i in range(Q):
    ans = sum_matrix[C[i]][D[i]] + sum_matrix[A[i] - 1][B[i] - 1] - sum_matrix[A[i] - 1][D[i]] - sum_matrix[C[i]][B[i] - 1]
    print(ans)
