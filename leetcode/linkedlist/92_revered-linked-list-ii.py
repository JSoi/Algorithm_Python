# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + ' ' + str(self.next)


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # left - right 까지 카운트를 해야될 것 같은데
        if not head.next:  # 들어온 리스트의 원소가 하나일때
            return head  # 문자 하나는 뒤집어도 하나니까 뒤집는다
        answer = []
        while head:  # head를 반복해서 순회한다
            answer.append(head.val)
            head = head.next
        if left != right:
            answer = answer[:left - 1] + answer[right - 1:left - 2 if left - 2 >= 0 else None:-1] + answer[right:]
            # Slicing 진행
        print(answer)
        answerNode = None
        for i in answer:
            if not answerNode:
                answerNode = ListNode(i, None)
            else:
                temp = answerNode
                while temp.next:
                    temp = temp.next
                temp.next = ListNode(i, None)
        return answerNode


class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # ROOT를 생성하는 방법
        root = start = ListNode(None) # root를 생성하는 방법
        root.next = head
        for _ in range(right - 1): # right 직전까지 순회한다
            start = start.next
        end = start.next
        temp = end.next
        for _ in range(right-left):
            end.next = temp.next
            temp.next = end
            start.next = temp
            temp = end.next
        print(root)
        return root



# mylist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
mylist2 = ListNode(3, ListNode(5, None))
sol = Solution()
# print(sol.reverseBetween(mylist, 2, 4))
print(sol.reverseBetween(mylist2, 1, 2))
