N, Q = map(int, input().split())

# 反転をすることを考えて両端に番兵(None)を置く
E = [None] * (N + 2)
for i in range(1, N + 1):
    E[i] = i

# 反転を管理する変数(1:反転なし, 2:反転あり)
State = 1

for _ in range(Q):
    Q = input().split()
    if Q[0] == "1":
        x = int(Q[1])
        y = int(Q[2])
        if State == 1:
            E[x] = int(Q[2])
        if State == 2:
            E[N - x + 1] = int(Q[2])

    if Q[0] == "2":
        State = 2 if State == 1 else 1

    if Q[0] == "3":
        x = int(Q[1])
        if State == 1:
            print(E[x])
        if State == 2:
            print(E[N - x + 1])
