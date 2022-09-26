import sys


def binary_search_iteration(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            return binary_search_iteration(array, target, mid + 1, end)
        else:
            return binary_search_iteration(array, target, start, mid - 1)
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search_iteration(array, target, 0, n - 1)
if not result:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)

'''
10 7
1 3 5 7 9 11 13 15 17 19
4
'''
