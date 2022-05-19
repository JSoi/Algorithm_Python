# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def p(arr, temp):
            if len(arr) == 0:
                result.append(temp)
            for i in range(len(arr)):
                p(arr[:i] + arr[i + 1:], temp + [arr[i]])

        p(nums, [])
        print(result)
        return result


sol = Solution()
sol.permute([1, 2, 3])
