N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

Answer = 0

for a in A:
    Answer += a * M

Answer += B * M * N

for c in C:
    Answer += c * N

print(Answer)
