from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))  # 0-indexed

L = []  # L[i]: 長さi+1の増加部分列の最終要素のうち最小のもの 0-indexed

for i in range(N):
    pos = bisect_left(L, A[i])

    # 今までの増加部分列の最後の要素よりも大きい場合
    if pos >= len(L):
        L.append(A[i])  # 今までの増加部分列にA[i]が追加可能であるからLを増やす
    else:
        L[pos] = A[i]  # L[pos]を更新

print(len(L))
