# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.answer = None
        def search(node):
            if not node:
                return
            if node.val == val:
                self.answer = node
                return
            search(node.left)
            search(node.right)
        search(root)
        return self.answer

    def searchBST_answer(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and val < root.val: # 루트가 존재하며 값이 val이 더 작은 경우
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        return root


def listToBST(list, index):
    if index >= len(list):
        return
    if not list[index]:
        return None
    tree = TreeNode(list[index])
    tree.left = listToBST(list, index * 2 + 1)
    tree.right = listToBST(list, index * 2 + 2)
    return tree


sol = Solution()
tree = listToBST([4,2,7,1,3],0)
print(sol.searchBST(tree, 2))
