# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = nums.index(min(nums))
        newnums = nums + nums[:minIndex]
        start, end = minIndex, len(newnums)-1
        print(newnums)
        while start <= end:
            mid = start + (end-start) // 2
            if target == newnums[mid]:
                return mid % len(nums)
            if target < newnums[mid]:
                end = mid -1
            else:
                start = mid + 1
        return -1


sol = Solution()
# print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))
# print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))
# print(sol.search([1,3], 3))
# print(sol.search([1,3],3))
print(sol.search([1,3,5],1))