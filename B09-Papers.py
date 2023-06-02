# 面積を求める時に累積和を使う時は、座標+1をしてはいけない
# 正方形のラインを含めるか含まないか考えること
N = int(input())

A = [None] * N
B = [None] * N
C = [None] * N
D = [None] * N

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# print(A)
# print(B)
# print(C)
# print(D)
# print("")

T = [[0] * 1501 for _ in range(1501)]
for i in range(N):
    T[A[i]][B[i]] += 1
    T[A[i]][D[i]] -= 1
    T[C[i]][B[i]] -= 1
    T[C[i]][D[i]] += 1

# for y in range(10):
#     for x in range(10):
#         if T[y][x] >= 0 and T[y][x] <= 9:
#             print(T[y][x], end="  ")
#         else:
#             print(T[y][x], end=" ")
#     print("")
# print("")

for y in range(0, 1501):
    for x in range(1, 1501):
        T[y][x] += T[y][x-1]

for x in range(0, 1501):
    for y in range(1, 1501):
        T[y][x] += T[y-1][x]


# for y in range(10):
#     for x in range(10):
#         if T[y][x] >= 0 and T[y][x] <= 9:
#             print(T[y][x], end="  ")
#         else:
#             print(T[y][x], end=" ")
#     print("")
# print("")

ans = 0
for y in range(1501):
    for x in range(1501):
        if T[y][x] >= 1:
            ans += 1

print(ans)