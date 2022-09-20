# row, col 식으로 입력받음
# 세로 : N , 가로 : M
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A, B, d = map(int, sys.stdin.readline().rstrip().split())

block = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(M)]
visit[A][B] = True

d_dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 바라보는 방향 - 북서남동 0 3 2 1 순서대로
f_dir = [0, 3, 2, 1]

nr, nc = A, B
d = f_dir[d]

while True:
    i = 1
    while i < 4:
        d = (d + i) % 4
        tr, tc = nr + d_dir[d][0], nc + d_dir[d][1]
        if tr in range(N) and tc in range(M):
            if block[tr][tc] == 0 and not visit[tr][tc]:  # 육지이고, 가보지 않은 경우
                visit[tr][tc] = True
                nr, nc = tr, tc
                break
        i += 1
    if i == 4:  # 다시 돌아온 경우
        d = (d + 2) % 4
        tr, tc = nr + d_dir[d][0], nc + d_dir[d][1]
        if block[tr][tc] == 1:
            break
move = 0
for vi in visit:
    move += vi.count(True)
print(move)

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
