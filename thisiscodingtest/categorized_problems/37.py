import sys

citycnt = int(sys.stdin.readline().rstrip())
bustcnt = int(sys.stdin.readline().rstrip())
INF = int(1e09)
conn = [[INF] * citycnt for _ in range(citycnt)]
for c in range(citycnt):
    conn[c][c] = 0

for _ in range(bustcnt):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    conn[a - 1][b - 1] = min(conn[a - 1][b - 1], c)

for k in range(citycnt):
    for s in range(citycnt):
        for g in range(citycnt):
            conn[s][g] = min(conn[s][g], conn[s][k] + conn[k][g])

# print(conn)
for c in conn:
    print(' '.join(str(el) if el != INF else '0' for el in c))
