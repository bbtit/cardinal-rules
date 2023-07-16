from collections import deque

Q = int(input())
queries = [input().split() for i in range(Q)]

T = deque()

for q in queries:
    if q[0] == "1":
        T.append(q[1])
    if q[0] == "2":
        print(T[0])
    if q[0] == "3":
        T.popleft()
