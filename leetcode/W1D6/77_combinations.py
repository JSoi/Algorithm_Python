# https://leetcode.com/problems/combinations/
from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        mylist = []
        for i in range(1, n + 1):
            mylist.append(i)
        temp = list(combinations(mylist, k))
        res = []
        for t in temp:
            res.append(list(t))
        # print(res)
        return res


sol = Solution()
sol.combine(5, 2)
