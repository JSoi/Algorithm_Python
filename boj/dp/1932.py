import sys

cnt = int(sys.stdin.readline().rstrip())
INF = int(1e09)
triangle = []
dist = [[0] * cnt for _ in range(cnt)]
for _ in range(cnt):
    triangle.append(list(map(int, sys.stdin.readline().split())))
# print(triangle)
dist[0][0] = triangle[0][0]
for i in range(1, cnt):
    dist[i][0] = triangle[i][0] + dist[i - 1][0]
    for j in range(1, i + 1):
        dist[i][j] = triangle[i][j] + max(dist[i - 1][j], dist[i - 1][j - 1])
print(max(dist[cnt-1]))
