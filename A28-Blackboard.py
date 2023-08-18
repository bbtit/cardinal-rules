N = int(input())
T = [None] * N
A = [None] * N
for i in range(N):
    T[i], A[i] = input().split()
    A[i] = int(A[i])

Answer = 0
for i in range(N):
    if T[i] == "+":
        Answer += A[i]
    if T[i] == "-":
        Answer -= A[i]
    if T[i] == "*":
        Answer *= A[i]
    if Answer < 0:
        Answer += 10000
    Answer %= 10000
    print(Answer)
