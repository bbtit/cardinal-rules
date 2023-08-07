N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j] : i番目までのカードを使ってj円になるか
dp = [[None] * (S+1) for _ in range(N+1)]

# カード0枚のときにj円になるか
dp[0][0] = True
for j in range(1, S+1):
    dp[0][j] = False

# カードの枚数iが1~N枚のときにjが作れるか
for i in range(1, N+1):
    for j in range(S+1):
        # 作りたい数字が追加候補のカードの数未満のとき
        # (この条件を入れないとdp[i-1]"""[j-A[i-1]""""]が範囲外になる)
        if j < A[i-1]:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
        # 作りたい数字が追加候補のカードの数以上のとき
        if j >= A[i-1]:
            if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

# 出力
if dp[N][S] == True:
    print("Yes")
else:
    print("No")
