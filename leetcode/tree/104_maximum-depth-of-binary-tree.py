# https://leetcode.com/problems/maximum-depth-of-binary-tree/

import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        depth = 0

        while q:
            if not q[0]:
                break
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur:
                    continue
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return depth



node = TreeNode(3, TreeNode(9, None), TreeNode(20, TreeNode(15, None), TreeNode(7, None)))
sol = Solution()
print(sol.maxDepth(node))
