import copy
import sys
from itertools import combinations

sero, garo = map(int, sys.stdin.readline().rstrip().split())
total = garo * sero
virusmap = list()
for _ in range(sero):
    virusmap.append(list(map(int, sys.stdin.readline().rstrip().split())))
# print(virusmap)
# 0 빈칸
# 1 벽
# 2 바이러스
# 후보 거르기

dg = [1, 0, -1, 0]
ds = [0, 1, 0, -1]
comb = list()


def bfs(vmap, se, ga):
    queue = list()
    queue.append([se, ga])
    while len(queue) > 0:
        s, g = queue.pop(0)
        for j in range(4):
            ng, ns = g + dg[j], s + ds[j]
            if ng < 0 or ns < 0 or ng >= len(vmap[0]) or ns >= len(vmap) or vmap[ns][ng] != 0:
                continue
            queue.append([ns, ng])
            vmap[ns][ng] = 2
    # print(vmap)

vloc = list()

for i in range(total):
    smallsero = i // garo
    smallgaro = i - smallsero * garo
    smalltarget = virusmap[smallsero][smallgaro]
    if smalltarget == 0:
        comb.append(i)
    if smalltarget == 2:
        vloc.append([smallsero, smallgaro])

ans = 0
for a, b, c in list(combinations(comb, 3)):
    temp = copy.deepcopy(virusmap)
    temp[a // garo][a - (a // garo) * garo] = temp[b // garo][b - (b // garo) * garo] \
        = temp[c // garo][c - (c // garo) * garo] = 1
    for v in vloc:
        bfs(temp, v[0], v[1])
    cnt = 0
    for t in temp:
        cnt += t.count(0)
    ans = max(ans, cnt)
print(ans)
