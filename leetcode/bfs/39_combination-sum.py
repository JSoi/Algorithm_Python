from typing import List
from itertools import combinations_with_replacement


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = list()
        candidates.sort()
        r = (target-candidates[0])//candidates[0]+1
        for i in range(r+1):
            for mytuple in combinations_with_replacement(candidates,i):
                print(mytuple)
                templist = list(mytuple)
                if sum(templist) == target:
                    comb.append(templist)
        print(comb)

sol = Solution()
sol.combinationSum([2, 3, 5], 8)
