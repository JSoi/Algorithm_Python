# p.197
import sys


def binarySearch(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return
        elif arr[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def search():
    for c in customer:
        if binarySearch(customer, c) == -1:
            print('No')
            return
    print('Yes')
    return


N = int(sys.stdin.readline().rstrip())
store = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
customer = list(map(int, sys.stdin.readline().rstrip().split()))
search()
