N, L = map(int, input().split())
A = [None] * (N + 1)
B = [None] * (N + 1)

for i in range(1, N + 1):
    A[i], B[i] = input().split()
    A[i] = int(A[i])

ans = 0
for i in range(1, N + 1):
    if B[i] == "E":
        ans = max(ans, L - A[i])
    if B[i] == "W":
        ans = max(ans, A[i])

print(ans)
