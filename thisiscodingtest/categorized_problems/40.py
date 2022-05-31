import collections
import heapq
import sys

barn, route = map(int, sys.stdin.readline().rstrip().split())
conn = collections.defaultdict(list)

for _ in range(route):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    conn[a].append(b)
    conn[b].append(a)

INF = int(1e9)
# print(conn)


def go(conn):
    dist = [INF] * (barn + 1)
    q = []
    dist[0] = dist[1] = 0
    heapq.heappush(q, (0, 1))  # 1부터 시작

    while q:
        acc, cur = heapq.heappop(q)
        if dist[cur] < acc:
            continue
        for adj in conn[cur]:
            cost = acc + 1
            if dist[adj] > cost:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))
    maxdist = max(dist)
    print(dist.index(maxdist), maxdist, dist.count(maxdist))

    return dist


go(conn)

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
