import collections


def solution(maps):
    answer = 0
    queue = collections.deque()
    queue.append([0, 0, 1])  # row, col, count
    ds = [1, -1, 0, 0]
    dg = [0, 0, 1, -1]
    sero = len(maps)
    garo = len(maps[0])
    while queue:
        s, g, c = queue.popleft()  # queue 사용
        for index in range(4):
            if s == sero - 1 and g == garo - 1:
                return c
            ns, ng = s + ds[index], g + dg[index]
            if ns < 0 or ns >= sero or ng < 0 or ng >= garo or maps[ns][ng] != 1:
                continue
            maps[ns][ng] = 0
            queue.append([ns, ng, c + 1])
    return -1
