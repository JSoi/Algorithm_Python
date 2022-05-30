# p.201
import sys

cnt, length = map(int, sys.stdin.readline().split())
ddeok = list(map(int, sys.stdin.readline().split()))
ddeok.sort(reverse=True)
# print(ddeok)
longest_ddeok = max(ddeok)
start, end = 0, longest_ddeok
longest = 0
while start <= end:
    mid = (start + end) // 2
    cut = 0
    for d in ddeok:
        if d < mid:
            break
        if d > mid:
            cut += (d - mid)
    if cut == length:
        longest = mid
        start = mid + 1 # 값이 맞지만 덜 잘라보자
    elif cut < length:  # 더 잘라야 될 경우
        end = mid - 1
    else:
        start = mid + 1 # 덜 잘라보자
print(longest)
'''
4 6
19 15 10 17
'''
