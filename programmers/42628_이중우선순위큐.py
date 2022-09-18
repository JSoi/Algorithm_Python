import collections
import heapq
from heapq import heappush, heappop


def solution(operations):
    mylist = collections.deque()
    for o in operations:
        oper, num = o.split(" ")
        num = int(num)
        if oper == 'D':  # 최대/최소 삭제
            if num == 1 and mylist:
                mylist.pop()
            elif num == -1 and mylist:
                mylist.popleft()
        else:
            mylist.append(num)
            mylist = collections.deque(sorted(mylist))
        # print(mylist)
    return [0, 0] if not mylist else [mylist[-1], mylist[0]]


def solution_heap(operations):
    heap = []
    for o in operations:
        oper, num = o.split(" ")
        num = int(num)
        if oper == 'D':  # 최대/최소 삭제
            if num == 1 and heap:
                # print('최대값삭제')
                heap.pop()
                heapq.heapify(heap)
            elif num == -1 and heap:
                # print('최소값삭제')
                heappop(heap)
        else:
            # print('삽입')
            heappush(heap, num)
        print(heap)
    return [0, 0] if not heap else [heap[-1], heap[0]]


# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 1", "I 2", "I 3", "I 4", "D 1","I 5", "I 6", "I 7", "D 1", "D -1"]))
# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
