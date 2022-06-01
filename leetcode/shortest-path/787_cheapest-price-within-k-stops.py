# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, K + 1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w + dw, y, k - 1))
        return -1

    def findCheapestPrice_TLE(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        conn = collections.defaultdict(list)
        for f in flights:
            conn[f[0]].append((f[1], f[2]))  # 연결 노드, 거리 순으로
        q = []
        INF = int(1e09)
        dist = [INF] * n
        dist[src] = 0
        heapq.heappush(q, (0, src, 0))
        while q:
            di, sr, count = heapq.heappop(q)
            if count >= k + 1:
                continue
            for adj, cost in conn[sr]:
                nowcost = di + cost
                dist[adj] = min(dist[adj],nowcost)
                heapq.heappush(q, (nowcost, adj, count + 1))
        print(dist)
        if dist[dst] >= INF:
            return -1
        else:
            return dist[dst]


sol = Solution()
assert sol.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1) == 700
assert sol.findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1) == 6
assert sol.findCheapestPrice(5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1) == -1
assert sol.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1) == 700
assert sol.findCheapestPrice(5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2) == 7
assert sol.findCheapestPrice(10,
                             [[3, 4, 4], [2, 5, 6], [4, 7, 10], [9, 6, 5], [7, 4, 4], [6, 2, 10], [6, 8, 6], [7, 9, 4],
                              [1, 5, 4], [1, 0, 4], [9, 7, 3], [7, 0, 5], [6, 5, 8], [1, 7, 6], [4, 0, 9], [5, 9, 1],
                              [8, 7, 3], [1, 2, 6], [4, 1, 5], [5, 2, 4], [1, 9, 1], [7, 8, 10], [0, 4, 2], [7, 2, 8]],
                             6, 0, 7) == 14
