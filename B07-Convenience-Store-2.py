T = int(input())  # 閉店時間
N = int(input())  # 従業員数

L = [None] * N  # 従業員の出勤時間
R = [None] * N  # 従業員の退勤時間
for i in range(N):
    L[i], R[i] = map(int, input().split())

# 前の時刻との人数差
diff = [0] * (T + 1)  # 0時からT時までのT+1個の要素
for i in range(N):
    begin, end = L[i], R[i]
    diff[begin] += 1
    diff[end] -= 1

# 特定の時刻にいる従業員数→変化量の累積和
prefix_sum = [0] * (T + 1)  # 0時からT時までのT+1個の要素
prefix_sum[0] = diff[0]  # 0時の従業員数
for i in range(T):
    # i時の従業員数 = i-1時の従業員数 + i時の変化量
    prefix_sum[i] = prefix_sum[i-1] + diff[i]

for i in range(T):
    print(prefix_sum[i])
