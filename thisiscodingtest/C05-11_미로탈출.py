import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    string = sys.stdin.readline().rstrip()
    graph.append([int(string[i]) for i in range(len(string))])

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(graph, sr, sc):
    queue = deque()
    queue.append((sr, sc, 1))
    count = 0
    while queue:
        row, col, cost = queue.popleft()
        if row == N - 1 and col == M - 1:
            return cost
        for i in range(4):
            tr, tc = row + dr[i], col + dc[i]
            if tr not in range(N) or tc not in range(M):
                continue
            if graph[tr][tc] == 1:
                graph[tr][tc] = 0
                queue.append((tr, tc, cost + 1))


print(bfs(graph, 0, 0))
'''
5 6
101010
111111
000001
111111
111111

'''
