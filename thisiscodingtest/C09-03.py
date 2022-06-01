import collections
import heapq
import sys

citycount, roadcount, sender = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e09)
conn = collections.defaultdict(dict)

for _ in range(roadcount):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    conn[a][b] = c
# print(conn)
dist = [INF] * (citycount + 1)
q = []
dist[sender] = 0
heapq.heappush(q, (0, sender))
while q:
    acc, cur = heapq.heappop(q)
    if acc > dist[cur]:
        continue
    for adj in conn[cur]:
        # print(conn[cur][adj])
        cost = conn[cur][adj] + acc
        if dist[adj] > cost:
            dist[adj] = cost
            heapq.heappush(q, (cost, adj))
ans_city = 0
ans_time = 0
# print(dist)
for c in dist[1:]:
    if c < INF:
        ans_city += 1
        ans_time = max(ans_time,c)
print(ans_city-1, ans_time)

'''
3 2 1
1 2 4
1 3 2
'''
