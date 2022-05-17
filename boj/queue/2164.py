# https://www.acmicpc.net/problem/2164
import collections

def do(cnt: int):
    deque = collections.deque()
    for i in range(1, cnt + 1):
        deque.append(i)
    while len(deque) > 1:
        deque.popleft()
        move = deque.popleft()
        deque.append(move)
    print(deque[0])

cnt = int(input())
do(cnt)

