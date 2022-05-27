arr = [1, 6, 2, 9, 4]


def partition(arr, start, end):
    # pivot이 중요!
    if len(arr) == 1:
        return arr

    if start >= end:
        return arr

    p = len(arr) - 1
    i = start - 1
    for j in range(start, end + 1):
        if arr[j] < arr[p]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    print('index', i)
    print(arr)
    return i + 1


def quicksort(arr, start, end):  # 배열을 쪼개지 않고 인덱스로 접근하자.. ㅎㅎ
    part = partition(arr, start, end)
    quicksort(arr, start, part - 1)  # 작은값들만
    quicksort(arr, part + 1, end)  # 큰 값들만
    return arr
