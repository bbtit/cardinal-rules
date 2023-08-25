N = int(input())
A = list(map(int, input().split()))

# 個数をカウント
cnt = [0] * 101
for a in A:
    cnt[a] += 1

ans = 0
for i in range(1, 101):
    ans += (cnt[i] * (cnt[i] - 1) * (cnt[i] - 2)) // 6

print(ans)
