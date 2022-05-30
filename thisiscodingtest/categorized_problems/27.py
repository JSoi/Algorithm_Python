import bisect
import sys

N, x = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
# print(N, x)
# print(arr)
left = bisect.bisect_left(arr, x)
if left < len(arr) and arr[left] == x:
    right = bisect.bisect_right(arr, x)
    print(right - left)
else:
    print(-1)
'''
7 4
1 1 2 2 2 2 3
'''
