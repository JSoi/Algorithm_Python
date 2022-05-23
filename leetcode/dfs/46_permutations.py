# https://leetcode.com/problems/permutations/
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def p(arr, temp):
            if len(arr) == 0:
                result.append(temp)
            for i in range(len(arr)):
                p(arr[:i] + arr[i + 1:], temp + [arr[i]])

        result = []
        p(nums, [])
        print(result)
        return result


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums, len(nums)))


class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = []

        def dfs(elements):
            if len(elements) == 0:
                res.append(prev[:])
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev.append(e)
                dfs(next_elements)
                prev.pop()

        dfs(nums)
        print(res)
        return res


sol = Solution3()
sol.permute([1, 2, 3])
