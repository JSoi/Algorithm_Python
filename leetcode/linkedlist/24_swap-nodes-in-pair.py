# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + ' ' + str(self.next)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = None
        prev = None
        if not head or not head.next:
            return head
        else:
            while head:
                if not head.next:
                    prev.next = ListNode(head.val, None)
                    return answer
                second = ListNode(head.val, None)
                first = ListNode(head.next.val, second)
                if not answer:  # 처음 들어오는 값이라면 이전 값과 엮어줄 필요 없다
                    answer = first
                    prev = second
                else:
                    prev.next = first
                    prev = second
                head = head.next.next
        return answer


mylist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
sol = Solution()
print(sol.swapPairs(mylist))
