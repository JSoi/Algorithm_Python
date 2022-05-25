# https://leetcode.com/problems/merge-two-binary-trees/
# 두 이진 트리를 합치자

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def add(root1, root2):
            if not root1 and not root2:
                return None
            if not root1:
                return root2
            if not root2:
                return root1
            left = add(root1.left, root2.left)
            right = add(root1.right, root2.right)
            return TreeNode(root1.val + root2.val, left, right)

        return add(root1, root2)

    def mergeTrees_simple(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))  # 예외처리를 해준다.
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)  # 특이한 문법
        # t1이 None이면 t1, t1이 None이 아니면 t1.right
        return ans
