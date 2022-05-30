import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))


def binarySearch():
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1
'''
5
-15 -6 1 3 7
'''

print(binarySearch())
