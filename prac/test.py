

from typing import List


def arrayPairSum(nums: List[int]):
    sum = 0
    pair = []
    nums.sort()
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum
