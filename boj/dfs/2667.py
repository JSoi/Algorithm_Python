import sys

cnt = int(input())
map = []
ds = [0, 0, -1, 1]
dg = [-1, 1, 0, 0]

for _ in range(cnt):
    map.append(list(sys.stdin.readline().strip()))

G = len(map[0])
S = len(map)
global minicount
minicount = 0


def go(s, g):
    global minicount
    minicount+=1
    map[s][g] = '0'
    for k in range(4):
        ns = s + ds[k]
        ng = g + dg[k]
        if ns < 0 or ns >= S or ng < 0 or ng >= S or int(map[ns][ng]) == 0:
            continue
        go(ns, ng)

count = 0
countarr = []
for i in range(S):
    for j in range(G):
        if int(map[i][j]) == 1:
            count += 1
            go(i, j)
            countarr.append(minicount)
print(count)
print(countarr)
