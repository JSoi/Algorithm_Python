import collections


def solution(n, edge):
    conn = collections.defaultdict(set)
    for e in edge:
        conn[e[0]].add(e[1])
        conn[e[1]].add(e[0])

    visit = [False] * (n + 1)
    dist = [0] * (n + 1)
    queue = collections.deque()
    queue.append((1, 0))
    while queue:
        target = queue.popleft()  # root
        visit[target[0]] = True
        for connected in conn[target[0]]:
            if not visit[connected]:
                queue.append((connected, target[1] + 1))
                visit[connected] = True
                dist[connected] = target[1] + 1

    return dist.count(max(dist))


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
