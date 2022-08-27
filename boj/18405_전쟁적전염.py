import collections
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
virus = list()

for _ in range(n):
    virus.append(list(map(int, sys.stdin.readline().rstrip().split())))

time, s, g = map(int, sys.stdin.readline().rstrip().split())
ds = [-1, 1, 0, 0]
dg = [0, 0, -1, 1]

# dictionary 초기화
virusdict = collections.defaultdict(list)
for i in range(n):
    for j in range(n):
        if virus[i][j] > 0:
            virusdict[virus[i][j]].append([i, j])


def go(sero, garo, vstate):
    for j in range(4):
        ns = sero + ds[j]
        ng = garo + dg[j]
        if ns < 0 or ng < 0 or ns >= n or ng >= n or vstate[ns][ng] != 0:
            continue
        vstate[ns][ng] = vstate[sero][garo]
        virusdict[vstate[ns][ng]].append([ns, ng])


# 시간이 우선
tick = 0
while tick < time:
    vqueue = list()
    for i in range(1, k + 1):
        for _ in range(len(virusdict[i])):
            target = virusdict[i].pop(0)
            go(target[0], target[1], virus)
    tick += 1

print(virus[s - 1][g - 1])
