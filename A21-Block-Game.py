N = int(input())
P = [None] * (N + 1)
A = [None] * (N + 1)
for i in range(1, N + 1):
    P[i], A[i] = map(int, input().split())

dp = [[None] * (N + 1) for _ in range(N + 1)]
dp[1][N] = 0

for LEN in reversed(range(0, N - 1)):
    for left in range(1, N - LEN + 1):
        right = left + LEN
        # dp[left][right]のときの最大点数を考える

        # 左を取り除いてdp[left][right]になったとき
        score1 = 0
        if left >= 2 and left <= P[left - 1] and P[left - 1] <= right:
            score1 = A[left - 1]

        # 右を取り除いてdp[left][right]になったとき
        score2 = 0
        if right <= N - 1 and left <= P[right + 1] and P[right + 1] <= right:
            score2 = A[right + 1]

        # dp[left][right]を決定
        # left == 1のときは右を削った点数
        if left == 1:
            dp[left][right] = dp[left][right + 1] + score2
        # right == Nのときは左を削った点数
        elif right == N:
            dp[left][right] = dp[left - 1][right] + score1
        # 右を削った場合と左を削った場合の最大値を選択
        else:
            dp[left][right] = max(
                dp[left - 1][right] + score1, dp[left][right + 1] + score2
            )

Answer = 0
for i in range(1, N + 1):
    Answer = max(Answer, dp[i][i])
print(Answer)
