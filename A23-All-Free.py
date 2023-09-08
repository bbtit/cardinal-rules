# ビットDP
# N:商品数, M:クーポン枚数
N, M = map(int, input().split())
A = [None] * M
for i in range(M):
    A[i] = list(map(int, input().split()))

# 全ての商品で0・1が必要だから2**N列必要
# クーポン0からMまでを使うからM+1行必要
# dp[i][j]: i番目までのクーポンでj(ビットで商品を指定)の商品を全てタダで買う時のクーポン必要枚数
dp = [[10**9] * (2**N) for _ in range(M + 1)]
dp[0][0] = 0  # dp[0][1]~dp[0][2**N-1]まではクーポン0では購入できないからINF

# 行
for i in range(1, M + 1):
    # 列
    for j in range(0, 2**N):
        # already[k] == 1: k番目の商品はj列の商品セットに含まれる
        already = [None] * N
        # j列の商品セットに含まれるなら1, そうでないなら0
        for k in range(N):
            if (j // (2**k) % 2) == 1:
                already[k] = 1
            else:
                already[k] = 0

        # クーポンiを使用する場合のインデックスを計算する
        v = 0
        for k in range(0, N):
            # 商品kがj列の商品セットまたはクーポンiの対象なら加算して列のインデックスを計算
            if already[k] == 1 or A[i - 1][k] == 1:
                v += 2**k

        # クーポンiを使わない場合
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        # クーポンiを使う場合
        dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1)

# 出力
if dp[M][2**N - 1] == 1000000000:
    print("-1")
else:
    print(dp[M][2**N - 1])
