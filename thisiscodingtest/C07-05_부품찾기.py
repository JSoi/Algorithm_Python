import sys


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


N = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()
M = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().rstrip().split()))

for xx in X:
    if binary_search(array, xx, 0, N - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''
5
8 3 7 9 2
3
5 7 9
'''
