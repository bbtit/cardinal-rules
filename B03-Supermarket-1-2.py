import itertools
N = int(input())
A = list(map(int, input().split()))
ans = False

for i in itertools.combinations(A, 3):
    if sum(i) == 1000:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")