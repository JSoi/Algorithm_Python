# https://www.acmicpc.net/problem/2606
import collections

cnt = int(input())
link_cnt = int(input())
global visit
visit = [False] * cnt
dict = collections.defaultdict(list)
for _ in range(link_cnt):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)


def infect(a):
    global visit
    visit[a - 1] = True
    for i in dict[a]:
        if not visit[i - 1]:
            infect(i)


infect(1)
print(visit.count(True)-1)
