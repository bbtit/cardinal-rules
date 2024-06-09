N = int(input())

for i in reversed(range(10)):
    # 割る数:divisor 割られる数:dividend
    divisor = 2**i
    print((N // divisor) % 2, end="")

print("")
