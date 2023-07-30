N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None] * (N+1)
dp[0] = 0
dp[1] = 0
dp[2] = dp[1] + A[2-2]

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

print(dp[N])
