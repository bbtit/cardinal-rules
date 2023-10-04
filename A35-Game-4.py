N = int(input())
A = list(map(int, input().split()))

dp = [[None] * (N + 1) for _ in range(N + 1)]

# 最下段はすでに決定
for i in range(1, N + 1):
    dp[N][i] = A[i - 1]

# 下の行から順に決定していく
for row in reversed(range(1, N)):
    for col in range(1, row + 1):
        # もし行が奇数なら、スコアを最大化する
        if row % 2 == 1:
            dp[row][col] = max(dp[row + 1][col], dp[row + 1][col + 1])
        # もし行が偶数なら、スコアを最小化する
        if row % 2 == 0:
            dp[row][col] = min(dp[row + 1][col], dp[row + 1][col + 1])

print(dp[1][1])
