# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) + str(self.left) + str(self.right)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def spliting(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = spliting(nums[:mid])
            root.right = spliting(nums[mid + 1:])
            return root

        return spliting(nums)


nums = [-10, -3, 0, 5, 9]
sol = Solution()
print(sol.sortedArrayToBST(nums))
