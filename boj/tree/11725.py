import collections
import sys

sys.setrecursionlimit(10 ** 6)
cnt = int(input())
line = []
dic = collections.defaultdict(list)
answer = dict()
for _ in range(cnt - 1):
    a, b = list(map(int, input().split()))
    dic[a].append(b)
    dic[b].append(a)
visited = [False] * (cnt + 1)


# print(dic)
def go(x):
    for ele in dic[x]:
        if not visited[ele]:
            visited[ele] = True
            answer[ele] = x
            go(ele)


go(1)
for i in range(2, len(answer) + 1):
    print(answer[i])
