N = int(input())
# 1つ前からの移動コスト 2~ 1-indexed
A = [0, 0] + list(map(int, input().split()))
# 2つ前からの移動コスト 3~ 1-indexed
B = [0, 0, 0] + list(map(int, input().split()))

# 1-indexed
dp = [None] * (N+1)
dp[0] = 0
dp[1] = 0
dp[2] = A[2]

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])

print(dp[N])
