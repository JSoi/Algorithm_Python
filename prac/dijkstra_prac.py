import heapq
import sys

with open('dijkstra_testcase.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(n, m)
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    print(graph)

INF = int(1e9)


def djikstra_plain(graph, start):
    def smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N):
            if dist[i] < min_value and not visit[i]:
                min_value = dist[i]
                idx = i
        return idx

    N = len(graph)
    dist = [INF] * N
    visit = [False] * N

    dist[start] = 0
    visit[start] = True

    for adj, d in graph[start]:
        dist[adj] = d

    for _ in range(N - 1):
        cur = smallest_node()
        visit[cur] = True
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if dist[adj] > cost:
                dist[adj] = cost

    return dist


def dijkstra_pq(graph, start):
    N = len(graph)
    dist = [INF] * N

    q = []

    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        acc, cur = heapq.heappop(q)
        print(acc, cur)
        if acc > dist[cur]:
            continue

        for adj, d in graph[cur]:
            cost = d + acc
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

print(dijkstra_pq(graph, start))