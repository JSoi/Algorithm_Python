import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    string = sys.stdin.readline().rstrip()
    graph.append([int(string[i]) for i in range(len(string))])

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def dfs(graph, row, col):
    graph[row][col] = 1
    for i in range(4):
        tr, tc = row + dr[i], col + dc[i]
        if tr not in range(N) or tc not in range(M):
            continue
        if graph[tr][tc] == 0:
            graph[tr][tc] = 1
            dfs(graph, tr, tc)


answer = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 0:
            dfs(graph, i, j)
            answer += 1
print(answer)
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

'''
