# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
import collections
import math


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val) + str(self.left and str(self.left)) + str(self.right and str(self.right))


class Codec:

    def serialize(self, root):
        def dfs(node):
            if not node:
                answer.append("None")
                return
            answer.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return

        answer = []
        dfs(root)
        res = ','.join(answer)
        return res

    def deserialize(self, data):
        def dfs(q):
            if q[0] == 'None':
                q.popleft()
                return
            target = q.popleft()
            newnode = TreeNode(target)
            newnode.left = dfs(q)
            newnode.right = dfs(q)
            return newnode
        mydata = data.split(',')
        queue = collections.deque(mydata)
        dfs(queue)


ser = Codec()
deser = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(deser.serialize(root))
ans = deser.deserialize(ser.serialize(root))
print(ans)
