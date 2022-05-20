from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def bfs_queue(start):
    visited = [start]  # 방문 배열을 첫 시작으로 넣어준다 - 이게 answer가 될 예정
    q = deque([start])  # 첫 시작이 들어 있는 큐를 만든다
    while q:
        now = q.popleft()
        for n in graph[now]:
            if n not in visited:
                q.append(n)
                visited.append(n)
    print(visited)
    return visited


bfs_queue(1)

graph_bfs = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def bfs_queue(start):
    queue = deque()
    visited = [start]
    while queue:
        pop = queue.popleft()
        for i in graph[pop]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    print(visited)
    return visited

bfs_queue()