import collections

dot, line, start = map(int, input().split())
my_dict = collections.defaultdict(list)
for _ in range(line):
    a, b = map(int, input().split())
    my_dict[a].append(b)
    my_dict[b].append(a)  # 양방향

for l in my_dict.values():
    l.sort()

visitlist = []
visitlist_2 = []

visit_matrix = [False] * (dot + 1)


def dfs(start: int):
    visitlist.append(start)
    for i in my_dict[start]:
        if i not in visitlist:
            dfs(i)


def dfs_2(start: int):
    visit_matrix[start] = True
    visitlist_2.append(start)
    for i in my_dict[start]:
        if not visit_matrix[i]:
            dfs_2(i)


def bfs(start: int):
    myqueue = collections.deque()
    myqueue.append(start)
    visited = [start]
    while myqueue:
        temp_left = myqueue.popleft()
        for d in my_dict[temp_left]:
            if d not in visited:
                visited.append(d)  # ...
                myqueue.append(d)
    return visited


dfs(start)
dfs_2(start)
bfs_raw_answer = bfs(start)

# print(' '.join(map(str, visitlist)))
# print(' '.join(map(str, bfs_raw_answer)))
print(' '.join(map(str, visitlist_2)))
