def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for adj in graph[v]:
        if not visited[adj]:
            dfs(graph, adj, visited)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * (len(graph) + 1)
dfs(graph, 1, visited)  # 연결 관계, 탐색 시작 index, 방문 여부
