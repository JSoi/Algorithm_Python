# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 균형 트리인지를 판별하는 메서드
    # 왼쪽, 오른쪽 자식 노드의 레벨 차이가 1 이상 나지 않는다.
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.torf = True
        def depth(node):
            if not node:
                return -1
            left = depth(node.left) + 1
            right = depth(node.right) + 1
            if abs(left - right) > 1:
                self.torf = False
            return max(left, right)
        depth(root)
        return self.torf

    def listToNode(self, list, index):
        if index >= len(list):
            return None
        if not list[index]:
            return None
        left = self.listToNode(list, index * 2 + 1)
        right = self.listToNode(list, index * 2 + 2)
        tree = TreeNode(list[index], left, right)
        return tree


sol = Solution()
print(sol.isBalanced(sol.listToNode([1, 2, 2, 3, 3, None, None, 4, 4], 0)))
