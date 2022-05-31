import heapq
import sys

testcase = int(sys.stdin.readline().rstrip())

ds = [0, 0, -1, 1]
dg = [1, 1, 0, 0]

INF = int(1e9)


def find_route(mat):
    N = len(mat)
    q = []
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = mat[0][0]
    heapq.heappush(q, (mat[0][0], 0, 0))
    while q:
        acc, s, g = heapq.heappop(q)
        if acc > dist[s][g]:
            continue
        for k in range(4):
            ns = s + ds[k]
            ng = g + dg[k]
            if ns < 0 or ns >= N or ng < 0 or ng >= N:
                continue
            cost = dist[s][g] + mat[ns][ng]
            if cost < dist[ns][ng]:
                dist[ns][ng] = cost
                heapq.heappush(q, (cost, ns, ng))
    return dist[N - 1][N - 1]


for _ in range(testcase):
    size = int(sys.stdin.readline().rstrip())
    matrix = list()
    for _ in range(size):
        matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(find_route(matrix))
'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
