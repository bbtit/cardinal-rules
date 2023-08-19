# aのb乗をmで割ったあまりを返す関数
def Power(a, b, m):
    # pはa^1 -> a^2 -> a^4 -> a^8 ...
    p = a
    Answer = 1
    # iは2のi乗の位を表す
    for i in range(30):
        wari = 2**i
        # 2^iの位のビットが1のとき
        if (b // wari) % 2 == 1:
            Answer = (Answer * p) % m
        p = (p * p) % m
    return Answer


n, r = map(int, input().split())
M = 1000000007

# 分子 n! の余りaを求める
a = 1
for i in range(1, n + 1):
    a = (a * i) % M

# 分母 r! * (n-r)! の余りbを求める(階乗を展開した形で求める)
b = 1
for i in range(1, r + 1):
    b = (b * i) % M
for i in range(1, n - r + 1):
    b = (b * i) % M

# a * b^(m-2)をMで割った余りを求める
# (a%M) * (b^(m-2)%M)をする
# aは既にMの余りだから%Mの必要なし
print((a * Power(b, M - 2, M)) % M)
