from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = []
        if not head.next:
            return True
        while head is not None:
            reverse.append(head.val)
            head = head.next
        while len(reverse) > 1:
            if reverse.pop() != reverse.pop(0):
                return False
        return True


head = ListNode(2, ListNode(1, ListNode(2, None)))
sol = Solution()
print(sol.isPalindrome(head))
