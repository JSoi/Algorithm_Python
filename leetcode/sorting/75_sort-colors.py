import collections
import heapq
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(1, len(nums)):
            for j in range(len(nums) - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


sol = Solution()
print(sol.sortColors([2, 0, 2, 1, 1, 0]))
