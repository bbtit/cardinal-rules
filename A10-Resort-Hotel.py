N = int(input())

# i番目の部屋の収容人数(1-indexed)
A = [None] + list(map(int, input().split()))

# 工事日数
D = int(input())

# 使用不可な部屋の範囲
L = [None] * (D + 1)
R = [None] * (D + 1)
for i in range(1, D + 1):
    L[i], R[i] = map(int, input().split())

# 1~i番目の部屋の最大収容人数
P = [None] * (N + 1)
P[1] = A[1]
# 右隣が今までの最大収容人数より大きければ更新
for i in range(2, N + 1):
    P[i] = max(P[i - 1], A[i])

# i~N番目の部屋の最大収容人数
Q = [None] * (N + 1)
Q[N] = A[N]
# 左隣が今までの最大収容人数より大きければ更新
for i in range(N - 1, 0, -1):
    Q[i] = max(Q[i + 1], A[i])

# 1~D日目までの最大収容人数をそれぞれ求める
for i in range(1, D + 1):
    # L[i]~R[i]の部屋は使用不可にする
    # 1~L[i]-1, R[i]+1~N番目の部屋の最大収容人数を求める
    # 1~L[i]-1の最大収容人数はP[L[i]-1]
    # R[i]+1~Nの最大収容人数はQ[R[i]+1]
    print(max(P[L[i] - 1], Q[R[i] + 1]))
