N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

grundy = [None] * 100001  # grundy[i] : 石がi個のときのGrundy数
for i in range(100001):
    Transit = [False, False, False]  # Transit[i] : Grundy数がiとなるような遷移が可能か
    if i >= X:
        Transit[grundy[i - X]] = True
    if i >= Y:
        Transit[grundy[i - Y]] = True

    if Transit[0] is False:
        grundy[i] = 0
    elif Transit[1] is False:
        grundy[i] = 1
    else:
        grundy[i] = 2

XOR_sum = 0
for i in range(N):
    XOR_sum ^= grundy[A[i]]
if XOR_sum >= 1:
    print("First")
else:
    print("Second")
