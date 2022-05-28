# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sero = len(matrix)
        garo = len(matrix[0])
        if sero == garo == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False
        garostart = 0
        while garostart < garo:
            if target == matrix[0][garostart]:
                return True
            if target < matrix[0][garostart]:
                break
            serostart, seroend = 0, sero - 1
            while serostart <= seroend:
                seromid = (serostart + seroend) // 2
                if matrix[seromid][garostart] == target:
                    return True
                elif matrix[seromid][garostart] < target:
                    serostart = seromid + 1
                else:
                    seroend = seromid - 1
            garostart += 1
        return False


sample = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
sol = Solution()
# print(sol.searchMatrix(sample, 5))
print(sol.searchMatrix([[-1, 3]], 3))
