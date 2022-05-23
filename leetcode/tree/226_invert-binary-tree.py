# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  # 루트노드이면 종료한다
            return
        root.right, root.left = root.left, root.right
        root.left, root.right = self.invertTree(root.left), self.invertTree(root.right)
        return root
