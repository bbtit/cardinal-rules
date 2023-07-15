N, K = map(int, input().split())

A = list(map(int, input().split()))

# i番目はP94の赤いところを意味する
# i番目の要素は、条件を満たす要素のうち、右端のインデックスを意味する
R = [None] * N

# iはP94の赤いところ
for i in range(0, N-1):
    # スタート地点
    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i-1]

    # 端まで行くか、１つ右の要素が条件を満たさなくなるまで右に進む
    while R[i] < N-1 and A[R[i]+1] - A[i] <= K:
        R[i] += 1

    answer = 0
    for i in range(0, N-1):
        # 右端のインデックスから、自分のインデックスを引くことで、条件を満たす要素の数がわかる
        answer += R[i] - i