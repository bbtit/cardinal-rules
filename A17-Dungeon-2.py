N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None] * (N+1)
dp[0] = 0
dp[1] = 0
dp[2] = dp[1] + A[2-2]

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

# dpを求めている段階では、その地点を最終的に通るか分からない
# ゴールから逆算しながらコースを求める
Answer = []
Place = N
while True:
    Answer.append(Place)
    if Place == 1:
        break

    if dp[Place] == dp[Place-1] + A[Place-2]:
        Place = Place-1
    else:
        Place = Place-2
Answer.reverse()
Answer2 = [str(i) for i in Answer]

print(len(Answer))
print(" ".join(Answer2))
