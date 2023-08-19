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


a, b = map(int, input().split())
print(Power(a, b, 1000000007))
