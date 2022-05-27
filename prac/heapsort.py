import heapq
from typing import List


class MaxHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2
        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        smallest = cur
        l = 2 * cur
        r = 2 * cur + 1
        if l <= len(self) and self.items[l] < self.items[smallest]:
            smallest = l
        if r <= len(self) and self.items[r] < self.items[smallest]:
            smallest = r
        if cur != smallest:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            self._percolate_down(smallest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None
        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)
        return root


def sorted_by_heap(lst):
    maxHeap = MaxHeap()
    for elem in lst:
        maxHeap.insert(elem)
    desc = [maxHeap.extract() for _ in range(len(lst))]
    print(desc)
    return desc


def sortArray(nums: List[int]) -> List[int]:
    minheap = list()
    for n in nums:
        heapq.heappush(minheap, n)
    return [heapq.heappop(minheap) for _ in range(len(nums))]

sorted_by_heap([5, 2, 3, 1])
print(sortArray([0,1,0,5,2,1]))
