# 答えが x秒 以下かを判定し、Yes であれば true、No であれば false を返す関数
def check(x, N, K, A):
    sum = 0

    for i in range(N):
        sum += x // A[i]

    if K <= sum:
        return True
    return False

N, K = map(int, input().split())

A = list(map(int, input().split()))

L = 0
R = 10 ** 9

while L < R:
    M = (L+R) // 2
    Ans = check(M, N, K, A)
    if Ans:
        R = M
    if Ans == False:
        L = M+1

print(L)
