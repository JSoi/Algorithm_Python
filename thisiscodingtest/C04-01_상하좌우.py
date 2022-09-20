import sys

N = int(sys.stdin.readline().rstrip())
trip = list(sys.stdin.readline().rstrip().split())
dr = [0, 0, -1, 1]  # LRUD
dc = [-1, 1, 0, 0]
nr = nc = 0
for t in trip:
    if t == 'L':
        tr, tc = nr + dr[0], nc + dc[0]
    elif t == 'R':
        tr, tc = nr + dr[1], nc + dc[1]
    elif t == 'U':
        tr, tc = nr + dr[2], nc + dc[2]
    else:
        tr, tc = nr + dr[3], nc + dc[3]
    if tr in range(N) and tc in range(N):
        nr, nc = tr, tc
print(nr + 1, nc + 1)
'''
5
R R R U D D
'''
