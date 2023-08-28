def get_player_num(a, b, A, B, K):
    count = 0
    for i in range(1, len(A)):
        if a <= A[i] and b <= B[i] and a + K >= A[i] and b + K >= B[i]:
            count += 1
    return count


N, K = map(int, input().split())
A = [None] * (N + 1)
B = [None] * (N + 1)

for i in range(1, N + 1):
    A[i], B[i] = map(int, input().split())

ans = 0
for a in range(101):
    for b in range(101):
        ans = max(ans, get_player_num(a, b, A, B, K))

print(ans)
