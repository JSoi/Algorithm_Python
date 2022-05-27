arr = [3, 2, 1, 5, 3, 2, 3]


def merge(arr1, arr2):
    result = []
    i1 = i2 = 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            result.append(arr1[i1])
            i1 += 1
        else:
            result.append(arr2[i2])
            i2 += 1
    while i1 < len(arr1):
        result.append(arr1[i1])
        i1 += 1
    while i2 < len(arr2):
        result.append(arr2[i2])
        i2 += 1
    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    L = mergeSort(arr[:mid])
    R = mergeSort(arr[mid:])
    return merge(L, R)


print(mergeSort(arr))
