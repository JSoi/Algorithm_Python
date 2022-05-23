#https://leetcode.com/problems/implement-queue-using-stacks/
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class MyQueue:

    def __init__(self):
        self.front = None

    def push(self, x: int) -> None:
        if not self.front:
            self.front = Node(x, None)
            return
        node = self.front
        while node.next:
            node = node.next
        node.next = Node(x, None)

    def pop(self) -> int:
        if not self.front:
            return None
        node = self.front
        self.front = self.front.next
        return node.val


    def peek(self) -> int:
        if not self.front:
            return None
        return self.front.val

    def empty(self) -> bool:
        return self.front is None

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
param_1 = obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_1, param_2,param_3,param_4)
