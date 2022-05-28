# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def findByBinary(array, target, start, end):
            mid = (start + end) // 2
            while start <= end:
                if target == array[mid]:
                    return mid
                elif target < array[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        for i in range(len(numbers) - 1):
            val = findByBinary(numbers, target - numbers[i], i + 1, len(numbers) - 1)
            if val != -1:
                return [i + 1, val + 1]
