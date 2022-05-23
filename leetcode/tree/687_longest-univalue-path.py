# https://leetcode.com/problems/longest-univalue-path/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node):
            if not node:  # 리프
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result

    def longestUnivaluePath2(self, root: Optional[TreeNode]) -> int:
        self.answer = 0

        def dfs(root):
            l = dfs(root.left)
            r = dfs(root.right)
            if not root:
                return 0
            if root.left and root.left.val == root.val:
                l += 1
            else:
                l = 0
            if root.right and root.right.val == root.val:
                r += 1
            else:
                r = 0
            self.result = max(self.result, l + r)
            return max(l, r)

        dfs(root)
        return self.result


sample = TreeNode(5, TreeNode(4, TreeNode(1, None, None), TreeNode(1, None, None)),
                  TreeNode(5, None, TreeNode(5, None, None)))
sol = Solution()
print(sol.longestUnivaluePath(sample))
