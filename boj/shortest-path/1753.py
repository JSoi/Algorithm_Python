import collections
import heapq
import sys

V, E = map(int, sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())
conn = collections.defaultdict(list)
INF = int(1e09)
dist = [INF] * (V + 1)
for _ in range(E):
    u, v, e = map(int, sys.stdin.readline().rstrip().split())
    conn[u].append((v, e))
q = [(0, start)]
dist[start] = 0
while q:
    acc, cur = heapq.heappop(q)
    if dist[cur] < acc:
        continue
    for adj, co in conn[cur]:
        cost = acc + co
        if dist[adj] > cost:
            dist[adj] = cost
            heapq.heappush(q, (cost, adj))
# print(dist)
for d in dist[1:]:
    if d < INF:
        print(d)
    else:
        print('INF')
'''
5 6
2
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''
