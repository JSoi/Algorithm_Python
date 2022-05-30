import sys

has, need = map(int, sys.stdin.readline().rstrip().split())
timbers = list()
for _ in range(has):
    timbers.append(int(sys.stdin.readline().rstrip()))


# print(timbers)
def cal():
    answer = 0
    short, long = 1, max(timbers)
    while short <= long:
        mid = (short + long) // 2
        timbercount = 0
        for t in timbers:
            if t >= mid:
                timbercount += (t // mid)
        if timbercount >= need:
            # 개수가 더 많이 나왔으면 크게 잘라도 됨
            answer = mid
            short = mid + 1
        else:
            long = mid - 1
    print(answer)


cal()
'''
4 11
802
743
457
539
'''
