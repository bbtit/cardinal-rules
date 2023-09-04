N = int(input())
# i番目の社員の上司の番号をA[i]とする
A = [0] * 2 + list(map(int, input().split()))

# 隣接リストを作成する
# G[i]は社員iの部下のリスト
G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    G[A[i]].append(i)

# N番目の社員から順に部下の数を求める
# dp[i]は社員iの部下の数
dp = [0] * (N + 1)
for i in range(N, 0, -1):
    for subordinate in G[i]:
        dp[i] += dp[subordinate] + 1

# アンパックして出力
print(*dp[1:])
