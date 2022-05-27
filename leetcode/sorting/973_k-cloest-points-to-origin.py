# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mylen = list()
        heap = list()

        def length(point):
            return math.sqrt(point[0] * point[0] + point[1] * point[1])

        for p in points:
            thislength = length(p)
            mylen.append(thislength)
            heapq.heappush(heap, thislength)

        standard = [heapq.heappop(heap) for _ in range(k)][-1]
        return [points[idx] for idx, val in enumerate(mylen) if val <= standard]


sol = Solution()
print(sol.kClosest([[0, 1], [1, 0]], 2))
