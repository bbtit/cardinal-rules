def binary_search(A, x):
    L = 0
    R = N - 1

    while L <= R:
        M = (L + R) // 2
        if x < A[M]:
            R = M -1
        elif x > A[M]:
            L = M + 1
        else:
            return M
    return -1

N, X = map(int, input().split())

A = list(map(int, input().split()))

ans = binary_search(A, X)

print(ans + 1)
