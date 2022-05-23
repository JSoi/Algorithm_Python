import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mydict = collections.defaultdict(list)
        for x, y, in prerequisites:
            mydict[x].append(y)
        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True
            traced.add(i)
            for y in mydict[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True

        for x in list(mydict):
            if not dfs(x):
                return False
        return True


sol = Solution()
print(sol.canFinish(2, [[1, 0], [0, 1]]))
