# 클래스 만들고 init 만들기
class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self, to):
        print(f"hello {to}, I'm {self.name}")


rtan = Person("rtanny")
rtan.sayhello("really happy")


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LinkedList:
    # 삽입, 삭제
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head: # 연결 리스트가 비어있을 경우
            self.head = ListNode(val, None)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val, None)

    def delete(self,val)->int:
        if not self.head:
            return -1
        