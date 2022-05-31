import collections
import heapq
from typing import List

# https://leetcode.com/problems/network-delay-time/
class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        conn = collections.defaultdict(list)
        for t in times:
            conn[t[0]].append((t[1], t[2]))  # des,time 순으로 들어감
        print(conn)
        INF = int(1e09)
        dist = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (0, k))
        dist[k] = 0
        while q:
            acc, cur = heapq.heappop(q)
            if acc > dist[cur]:
                continue
            for adj, d in conn[cur]:
                cost = acc + d
                if dist[adj] > cost:
                    dist[adj] = cost
                    heapq.heappush(q, (cost, adj))
        print(dist)
        ans = max(dist[1:])
        if ans >= INF:
            print('-1')
        else:
            print(ans)


sol = Solution()
# sol.networkDelayTime([[1, 2, 1]], 2, 2)
sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
