import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split()))
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()
small, big = 0, array[-1]


def cut(array, cutlength):
    totalcut = 0
    for a in array:
        if cutlength < a:
            totalcut += (a - cutlength)
    return totalcut


while small <= big:
    mid = (small + big) // 2
    cutlen = cut(array, mid)
    if M == cutlen:
        print(mid)
        break
    elif M > cutlen:
        big = mid - 1
    else:
        small = mid + 1

'''
4 6
19 15 10 17
'''
