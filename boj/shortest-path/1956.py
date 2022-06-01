# https://www.acmicpc.net/problem/1956
import sys

V, E = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e09)
conn = [[INF] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    conn[a][b] = c

for a in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            conn[i][j] = min(conn[i][j], conn[i][a] + conn[a][j])
answer = INF
for b in range(1, V + 1):
    answer = min(answer, conn[b][b])
print(answer if answer != INF else -1)
