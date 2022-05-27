import sys

cnt = int(sys.stdin.readline())
alldots = []
ans = []
for _ in range(cnt):
    a, b = map(int, sys.stdin.readline().split())
    alldots.append([a, b])


def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        one = [arr1[i][0], arr1[i][1]]
        two = [arr2[j][0], arr2[j][1]]
        if arr1[i][1] < arr2[j][1]:
            result.append(one)
            i += 1
        elif arr1[i][1] == arr2[j][1]:
            if arr1[i][0] < arr2[j][0]:
                result.append(one)
                i += 1
            else:
                result.append(two)
                j += 1
        else:
            result.append(two)
            j += 1
    while i < len(arr1):
        one = [arr1[i][0], arr1[i][1]]
        result.append(one)
        i += 1
    while j < len(arr2):
        two = [arr2[j][0], arr2[j][1]]
        result.append(two)
        j += 1

    return result


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    return merge(mergesort(L), mergesort(R))


ans = mergesort(alldots)
for dot in ans:
    print(dot[0], dot[1])
