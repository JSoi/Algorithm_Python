# https://leetcode.com/problems/design-circular-queue/
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + str(next)


class MyCircularQueue:
    def __init__(self, k: int):
        self.maxsize = k
        self.size = 0
        self.front = None

    # Inserts an element into the circular queue. Return true if the operation is successful.
    def enQueue(self, value: int) -> bool:
        if self.size == self.maxsize:
            return False
        if not self.front:  # 비어 있을 때
            self.front = Node(value, None)
            self.front.next = self.front
        else:
            node = self.front
            while node.next is not self.front:
                node = node.next
            node.next = Node(value, self.front)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if not self.front or self.size == 0:
            return False
        if self.front.next is self.front:
            self.front = None
        else:
            temp = self.front
            node = self.front.next
            while temp.next is not self.front:
                temp = temp.next
            temp.next = node
            self.front = node
            self.front.next = node.next
        self.size-=1
        return True

    def Front(self) -> int:
        if not self.front:
            return -1
        else:
            return self.front.val

    def Rear(self) -> int:
        if not self.front:
            return -1
        node = self.front
        while node.next is not self.front:
            node = node.next
        return node.val

    def isEmpty(self) -> bool:
        return self.front is None

    def isFull(self) -> bool:
        return self.size == self.maxsize


# Your MyCircularQueue object will be instantiated and called as such:
# myCircularQueue = MyCircularQueue(8);
# param_1 = myCircularQueue.enQueue(3)
# param_2 = myCircularQueue.enQueue(9)
# param_3 = myCircularQueue.enQueue(5)
# param_4 = myCircularQueue.enQueue(0);
# param_5 = myCircularQueue.deQueue();
# param_6 = myCircularQueue.deQueue();
# param_7 = myCircularQueue.Rear();
# param_8 = myCircularQueue.Rear();
# param_9 = myCircularQueue.deQueue();
# print(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9)
