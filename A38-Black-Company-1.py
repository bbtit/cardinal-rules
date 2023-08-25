D, N = map(int, input().split())
L = [None] * (N + 1)
R = [None] * (N + 1)
H = [None] * (N + 1)

for i in range(1, N + 1):
    L[i], R[i], H[i] = map(int, input().split())

LIM = [24] * (D + 1)

for cond_num in range(1, N + 1):
    for day in range(L[cond_num], R[cond_num] + 1):
        LIM[day] = min(LIM[day], H[cond_num])

ans = 0
for i in range(1, D + 1):
    ans += LIM[i]

print(ans)
