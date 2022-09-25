import collections
import sys

N, K = map(int, list(sys.stdin.readline().rstrip().split()))
A = list(map(int, list(sys.stdin.readline().rstrip().split())))
B = list(map(int, list(sys.stdin.readline().rstrip().split())))
A.sort()
B.sort(reverse=True)
for k in range(K):
    if A[k] < B[k]:
        A[k], B[k] = B[k], A[k]
    else:
        break
print(A)
'''
5 3
1 2 5 4 3
5 5 6 6 5
'''
