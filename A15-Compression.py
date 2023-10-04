import bisect

N = int(input())
A = list(map(int, input().split()))
B = [None] * N

T = list(set(A))
T.sort()
for i in range(N):
    # A[i] が T の何番目に小さいかを求める
    B[i] = bisect.bisect_left(T, A[i])
    B[i] += 1  # 1-indexed にする

Answer = [str(b) for b in B]
print(" ".join(Answer))
