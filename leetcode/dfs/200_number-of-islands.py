# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        ds = [0, 0, -1, 1]
        dg = [-1, 1, 0, 0]
        S = len(grid)
        G = len(grid[0])

        def dfs(sero, garo):
            grid[sero][garo] = '0'
            for i in range(4):
                ns, ng = sero + ds[i], garo + dg[i]
                if ns < 0 or ns >= S or ng < 0 or ng >= G or int(grid[ns][ng]) == 0:
                    continue
                dfs(ns, ng)

        count = 0
        for i in range(S):
            for j in range(G):
                if int(grid[i][j]) == 1:
                    count += 1
                    dfs(i, j)
        return count


grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

sol = Solution()
sol.numIslands(grid)
