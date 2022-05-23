# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def height(p):
            if not p: return -1 #리프 노드일 경우 -1 반환
            left, right = height(p.left), height(p.right)
            self.ans = max(self.ans, 2 + left + right) # 합을 저장하는 변수 - 클래스 변수로 선언한다.
            return 1 + max(left, right) # 리프 노드까지의 거리를 반환한다.
        height(root)
        return self.ans


sol = Solution()
sample = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))
print(sol.diameterOfBinaryTree(sample))
