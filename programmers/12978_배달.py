import collections

INF = int(1e9)


def solution(N, road, K):
    # 1번에서 K시간 이내로 음식 배달을 받을 수 있는 마을의 개수 구하기
    dist = [INF] * (N + 1)
    queue = collections.deque()

    queue.append((1, 0))
    dist[1] = 0

    while queue:
        curr, total = queue.popleft()
        for a, b, c in road:
            new_distance = total + c
            if a == curr and new_distance < dist[b]:
                dist[b] = new_distance
                queue.append((b, new_distance))
            elif b == curr and new_distance < dist[a]:
                dist[a] = new_distance
                queue.append((a, new_distance))

    answer = 0
    for di in dist:
        if di <= K:
            answer += 1
    print(answer)
    return answer


solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
