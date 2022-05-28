from bisect import bisect_left, bisect
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        for n1 in nums1:
            mys = bisect_left(nums2, n1)
            if mys < len(nums2) and nums2[mys] == n1:
                res.append(n1)

        return list(set(res))


sol = Solution()
print(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
