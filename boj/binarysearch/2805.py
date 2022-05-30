'''
4 7
20 15 10 17
'''
import sys

treecnt, length = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))


def cal():
    short, long, answer = 0, max(trees), 0
    while short <= long:
        mid = (short + long) // 2
        tcut = 0
        for t in trees:
            if mid < t:
                tcut += (t - mid)
        if tcut >= length:  # 너무 많이잘랐나
            answer = mid
            short = mid + 1
        else:
            long = mid - 1
    print(answer)


cal()
