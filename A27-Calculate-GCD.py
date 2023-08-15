def GCD(a, b):
    # 片方が0になるまで操作
    while a >= 1 and b >= 1:
        if a >= b:
            a = a % b
        else:
            b = b % a
    if a >= 1:
        return a
    return b


A, B = map(int, input().split())
print(GCD(A, B))
