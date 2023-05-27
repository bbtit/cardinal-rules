N = input()  # 2進数
ans = 0

for i in range(len(N)):
    keta = len(N) - i - 1  # 右から何桁か
    num = int(N[keta])  # その桁の数字
    ans += num * (2 ** i)  # その桁の数字×2の乗数

print(ans)
