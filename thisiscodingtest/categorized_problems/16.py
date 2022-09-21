import copy
import itertools
import sys

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

R, C = map(int, sys.stdin.readline().rstrip().split())

virus_map = []
blank_set = []
virus_set = set()
for r in range(R):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for mc in range(C):
        if line[mc] == 0:
            blank_set.append((r, mc))
        elif line[mc] == 2:
            virus_set.add((r, mc))
    virus_map.append(line)


def dfs(graph, r, c):
    stack = list()
    stack.append((r, c))
    while stack:
        a, b = stack.pop()
        for i in range(4):
            tr, tc = a + dr[i], b + dc[i]
            if tr not in range(R) or tc not in range(C) or graph[tr][tc] != 0:
                continue
            graph[tr][tc] = 2
            stack.append((tr, tc))


answer = 0
for a, b, c in list(itertools.combinations(blank_set, 3)):
    virus_map_temp = copy.deepcopy(virus_map)
    virus_map_temp[a[0]][a[1]] = virus_map_temp[b[0]][b[1]] = virus_map_temp[c[0]][c[1]] = 1
    for rv, cv in virus_set:
        dfs(virus_map_temp, rv, cv)
    safecount = 0
    for gg in virus_map_temp:
        safecount += gg.count(0)
    answer = max(answer, safecount)
print(answer)
'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
