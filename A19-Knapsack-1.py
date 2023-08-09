N, W = map(int, input().split())
w = [None] * (N + 1)
v = [None] * (N + 1)
for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

# 初期化
dp = [[-(10**15)] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(0, W + 1):
        # 追加する可能性のある品目の重さがjより大きい時
        if j < w[i]:
            # 追加できないから価格は1行上から変わらない
            dp[i][j] = dp[i - 1][j]
        # 追加する可能性のある品目の重さがjより小さい時
        if j >= w[i]:
            # 1行上から追加しない場合の価格と、1行上の追加品物の重さ分左の価格に追加品物を追加した時の価格を比較
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

# N行目の最大値を出力
print(max(dp[N]))
