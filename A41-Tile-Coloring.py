N = int(input())
S = input()

ans = False
for i in range(0, N - 2):
    if S[i : i + 3] == "RRR":
        ans = True
    if S[i : i + 3] == "BBB":
        ans = True

print("Yes" if ans else "No")
