N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [-(10**9)] * (N + 1)
dp[1] = 0
for i in range(1, N):
    # dp[A[i-1]]の値は既存のdp[A[i-1]]と新たな値を比較して大きい方を採用
    dp[A[i - 1]] = max(dp[A[i - 1]], dp[i] + 100)
    # dp[B[i-1]]の値は既存のdp[B[i-1]]と新たな値を比較して大きい方を採用
    dp[B[i - 1]] = max(dp[B[i - 1]], dp[i] + 150)

print(dp[N])
