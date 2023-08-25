N = int(input())
A = []

for i in range(N):
    l, r = map(int, input().split())
    A.append([r, l])

A.sort()

current_time = 0
ans = 0

for i in range(N):
    # 現在時刻が、映画の開始時間A[i][1]よりも前なら
    if current_time <= A[i][1]:
        # 現在時刻を映画の終了時間A[i][0]に更新
        current_time = A[i][0]
        # 選んだ映画の数を1増やす
        ans += 1

print(ans)
