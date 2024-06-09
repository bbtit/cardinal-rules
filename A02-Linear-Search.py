N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = False

for i in A:
    if i == X:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")
