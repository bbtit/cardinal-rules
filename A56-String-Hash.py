N, Q = map(int, input().split())
S = input()
queries = [list(map(int, input().split())) for _ in range(Q)]

# 文字列の各文字のASCIIコード
T = list(map(lambda c: ord(c) - ord('a') + 1, S))

MOD = 2147483647
power100 = [None] * (N + 1)
power100[0] = 1
for i in range(N):
    power100[i+1] = power100[i] * 100 % MOD

# H[i]はs[1,i]のハッシュ値
H = [None] * (N+1)
H[0] = 0
for i in range(N):
    H[i+1] = (H[i] * 100 + T[i]) % MOD


def hash_value(left, right):
    return (H[right] - H[left-1] * power100[right - left + 1]) % MOD


for a, b, c, d in queries:
    hash1 = hash_value(a, b)
    hash2 = hash_value(c, d)
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")
