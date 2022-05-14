# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + ' ' + str(self.next)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        while head:
            if not reverse:  # None일때
                reverse = ListNode(head.val, None)
            else:
                temp = reverse
                reverse = ListNode(head.val, temp)
            head = head.next
            print(reverse)
        return reverse


mylist = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
sol = Solution()
sol.reverseList(mylist)
