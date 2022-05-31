# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
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
            if count > k:
                continue
            for adj, cost in conn[sr]:
                nowcost = di + cost
                if nowcost < dist[adj] and count < k + 1:
                    dist[adj] = nowcost
                    heapq.heappush(q, (nowcost, adj, count + 1))
        print(dist)
        if dist[dst] >= INF:
            return -1
        else:
            return dist[dst]


sol = Solution()
# sol.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1)
# sol.findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1)

# sol.findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1)
sol.findCheapestPrice(5,[[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2)
# sol.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1)
