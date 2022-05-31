import collections
import sys

company, route = map(int, sys.stdin.readline().rstrip().split())
conn = collections.defaultdict(list)

INF = int(1e9)
graph = [[INF] * (company + 1) for _ in range(company + 1)]

for _ in range(route):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

visitc, date = map(int, sys.stdin.readline().rstrip().split())

for i in range(company + 1):
    for j in range(company + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, len(graph)):
    for a in range(1, len(graph)):
        for b in range(1, len(graph)):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

distance = graph[1][date] + graph[date][visitc]
if distance >= INF:
    print('-1')
else:
    print(distance)

'''
4 2
1 3
2 4
3 4
'''
'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''