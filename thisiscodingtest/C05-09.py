from collections import deque


def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    while queue:
        target = queue.popleft()
        print(target, end=' ')
        for g in graph[target]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * (len(graph) + 1)
bfs(graph, 1, visited)  # 연결 관계, 탐색 시작 index, 방문 여부
