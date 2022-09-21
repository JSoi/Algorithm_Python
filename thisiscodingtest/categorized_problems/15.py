from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())
visit = [False for _ in range(N + 1)]
graph = [[False for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A][B] = True
queue = deque()
queue.append((1, 0))
visit[1] = True
answer = []
while queue:
    target, count = queue.popleft()
    if count == K:
        answer.append(target)
    for index in range(N + 1):
        if graph[target][index] and not visit[index]:
            visit[index] = True
            queue.append((index, count + 1))
answer.sort()
if not answer:
    print(-1)
else:
    for a in answer:
        print(a)
'''
4 4 2 1
1 2
1 3
2 3
2 4
'''

'''
4 3 2 1
1 2
1 3
1 4
'''

'''
4 4 1 1
1 2
1 3
2 3
2 4
'''