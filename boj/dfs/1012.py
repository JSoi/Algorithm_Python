import sys

sys.getrecursionlimit()
cnt = int(sys.stdin.readline().rstrip())
answer = ''
for _ in range(cnt):
    garo, sero, cabbage = map(int, sys.stdin.readline().rstrip().split())
    mymap = [[0 for _ in range(garo)] for _ in range(sero)]
    for _ in range(cabbage):
        g, s = map(int, sys.stdin.readline().rstrip().split())
        mymap[s][g] = 1
    ds = [1, -1, 0, 0]
    dg = [0, 0, -1, 1]


    def dfs(x, y):
        mymap[x][y] = 0
        for k in range(4):
            ns = x + ds[k]
            ng = y + dg[k]
            if ns < 0 or ns >= sero or ng < 0 or ng >= garo or mymap[ns][ng] == 0:
                continue
            dfs(ns, ng)


    count = 0
    for i in range(sero):
        for j in range(garo):
            if mymap[i][j] == 1:
                count += 1
                dfs(i, j)

    answer += str(count) + '\n'
print(answer)
