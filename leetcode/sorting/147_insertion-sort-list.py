from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + str(self.next)


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resultNode = ListNode(None)

        while head:
            if not resultNode.next:
                resultNode.next = ListNode(head.val)
                head = head.next
                continue
            resultTemp = resultNode.next
            prevTemp = resultNode
            flag = False
            while resultTemp:
                if head.val < resultTemp.val:
                    node = ListNode(head.val, resultTemp)
                    prevTemp.next = node
                    flag = True
                    break
                prevTemp = resultTemp
                resultTemp = resultTemp.next
            # print(resultNode)
            if not flag:
                prevTemp.next = ListNode(head.val)
            head = head.next
        return resultNode.next


sample = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
sol = Solution()
print(sol.insertionSortList(sample))
