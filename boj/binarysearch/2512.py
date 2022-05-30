import sys

cnt = int(sys.stdin.readline().rstrip())
moneys = list(map(int, sys.stdin.readline().rstrip().split()))
limit = int(sys.stdin.readline().rstrip())


def cal():
    low, high = 0, max(moneys)
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        lilmoney = 0
        for m in moneys:
            if mid <= m:
                lilmoney += mid
            else:
                lilmoney += m
        if lilmoney <= limit:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return answer


print(cal())
