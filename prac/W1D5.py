graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def dfs_recursive(node, visited):
    visited.append(node)
    for n in graph[node]:
        if n not in visited:
            dfs_recursive(n, visited)
    return visited


def dfs_stack(start):
    visited = []
    stack = [start]
    while stack:
        top = stack.pop()
        visited.append(top)
        for n in graph[top]:
            if n not in visited:
                stack.append(n)
    return visited


assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]
