import sys
from collections import deque


def bfs(mymap, s, g):
    ds = [0, 0, -1, 1, 1, 1, -1, -1]
    dg = [1, -1, 0, 0, -1, 1, -1, 1]
    cnt = 0
    queue = deque([(s, g)])
    while queue:
        nns, nng = queue.popleft()
        cnt += 1
        # print('pop', pop)
        for i in range(8):
            ns = nns + ds[i]
            ng = nng + dg[i]
            if ns < 0 or ns >= len(mymap) or ng < 0 or ng >= len(mymap[0]) or mymap[ns][ng] == 0:
                continue
            mymap[ns][ng] = 0
            queue.append((ns, ng))
    return cnt


answer = ""
while True:
    numline = list(map(int, sys.stdin.readline().split()))
    garo, sero = numline[0], numline[1]
    if garo == 0 and sero == 0:
        break
    mymap = list()
    for _ in range(sero):
        line = sys.stdin.readline().strip()
        mylist = list(map(int, list(line.split())))
        mymap.append(mylist)
    count = 0
    for i in range(len(mymap)):
        for j in range(len(mymap[0])):
            if mymap[i][j] == 1:
                count += 1
                mymap[i][j] = 0
                bfs(mymap, i, j)
    answer += str(count) + '\n'
print(answer)
