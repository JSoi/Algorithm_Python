# https://www.acmicpc.net/problem/1966
import collections


class Node:
    def __init__(self, index, importance):
        self.index = index
        self.importance = importance


def go(imparr, t):
    dequeue = collections.deque()
    for i in range(len(imparr)):
        dequeue.append(Node(i, int(imparr[i])))
    pop_count = 0
    while True:
        first = dequeue[0]
        flag = False
        for node in dequeue:
            if first.importance < node.importance:
                flag = True
                break
        if flag:  # 큰 원소가 존재할 경우
            dequeue.append(dequeue.popleft())
        else:  # 큰 원소가 없을 경우 pop만 해준다
            pop_count += 1
            pop_element = dequeue.popleft()
            if pop_element.index == t:
                return str(pop_count)


cnt = int(input())
answer = ""
for i in range(cnt):
    line = input()
    impline = input()
    target = int(line.split(" ")[1])
    imp_arr = list(impline.split(" "))
    answer = answer + go(imp_arr, target)+"\n"
print(answer)
