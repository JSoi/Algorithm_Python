# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + str(self.next)


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = None

        while list1 is not None and list2 is not None:
            value = 0
            if list1.val <= list2.val:
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next
            if answer is None:
                answer = ListNode(value,None)
                continue
            point = answer
            while point.next:
                point = point.next
            point.next = ListNode(value, None)


        if list1 is not None:
            point = answer
            while point.next:
                point = point.next
            point.next = list1
        if list2 is not None:
            point = answer
            while point.next:
                point = point.next
            point.next = list2

        return answer


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution()
print(str(sol.mergeTwoLists(list1, list2)))
