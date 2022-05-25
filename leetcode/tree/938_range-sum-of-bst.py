# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.count =0
        def go(root):
            if not root:
                return
            if low <= root.val <= high:
                self.count += root.val
                go(root.right)
                go(root.left)
            else:
                go(root.right)
                go(root.left)
        go(root)
        return self.count


def listToNode(list, index):
    if index >= len(list):
        return None
    if not list[index]:
        return None
    root = TreeNode(list[index])
    l = listToNode(list, index * 2 + 1)
    r = listToNode(list, index * 2 + 2)
    root.left = l
    root.right = r
    return root


sol = Solution()
tree = listToNode([10, 5, 15, 3, 7, None, 18], 0)
ans = sol.rangeSumBST(tree, 7, 15)
print(ans)
