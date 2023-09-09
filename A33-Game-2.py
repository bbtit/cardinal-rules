# ニム
N = int(input())  # 石の山の個数
A = list(map(int, input().split()))  # 各山の石の個数

xor_sum = A[0]
for i in range(1, N):
    xor_sum ^= A[i]

if xor_sum == 0:
    print("Second")
else:
    print("First")
