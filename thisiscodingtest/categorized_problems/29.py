import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
mylist = []
for _ in range(N):
    mylist.append(int(sys.stdin.readline().rstrip()))


def search(lst, cnt):
    lst.sort()
    minl = 1
    maxl = lst[-1] - lst[0]
    answer = 0
    while minl <= maxl:
        midl = (minl + maxl) // 2
        cur = lst[0]
        count = 1
        for i in range(1, len(lst)):
            if cur + midl <= lst[i]:
                cur = lst[i]
                count += 1
        if count >= cnt:
            answer = midl
            minl = midl + 1
        else:
            maxl = midl - 1
    print(answer)
    return answer


search(mylist, C)
