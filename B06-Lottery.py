N = int(input())
A = list(map(int, input().split()))

Q = int(input())
L = [None] * Q
R = [None] * Q

for i in range(Q):
    L[i], R[i] = map(int, input().split())

# 累積和:prefix sum, cumulative sum, inclusice scan
win_prefix_sum = [0] * (N + 1)
lose_prefix_sum = [0] * (N + 1)

for i in range(1, N+1):
    win_prefix_sum[i] = win_prefix_sum[i-1]
    lose_prefix_sum[i] = lose_prefix_sum[i-1]
    if A[i-1] == 1:
        win_prefix_sum[i] += 1
    elif A[i-1] == 0:
        lose_prefix_sum[i] += 1
    else:
        raise ValueError("累積和の計算に失敗")

for i in range(Q):
    win = win_prefix_sum[R[i]] - win_prefix_sum[L[i] - 1]
    lose = lose_prefix_sum[R[i]] - lose_prefix_sum[L[i] - 1]
    if win > lose:
        print("win")
    elif win < lose:
        print("lose")
    elif win == lose:
        print("draw")
    else:
        raise ValueError("クエリの出力に失敗")
