from typing import List


class Solution:
    answer = list()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        answer = []
        nextlist = nums[1:]
        for i in self.subsets(nextlist):
            answer.append(i)
            answer.append([nums[0]] + i)
        return answer


sol = Solution()
print(sol.subsets([1, 2, 3]))
