import sys

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
apple = list()
bg = [0, 1, -1, 0]
bs = [1, 0, 0, -1]
bl = [1, 3, 0, 2]  # 우측 회전
br = [2, 0, 3, 1]  # 좌측 회전
bamdir = 1  # 오른쪽으로 먼저 진행한다.
for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    apple.append([a, b])

for a in apple: # 사과는 2
    board[a[0] - 1][a[1] - 1] = 2

l = int(input())
timelist = list()
for _ in range(l):  # 왼쪽 : L, 오른쪽 : D
    x, c = input().rstrip().split()
    x = int(x)
    timelist.append([x, c])
time = 0
head = [0, 0]  # 머리 위치
board[0][0] = 1
bambody = list()
bambody.append(head)

while True:
    if len(timelist) > 0 and time == int(timelist[0][0]):  # 다음 시간이 있으면
        nexttime = timelist.pop(0)
        bamdir = br[bamdir] if nexttime[1] == 'D' else bl[bamdir]
    fs, fg = head[0] + bs[bamdir], head[1] + bg[bamdir]
    if fs < 0 or fs >= n or fg < 0 or fg >= n or board[fs][fg] == 1:
        break  # 벽에 부딪혔을 때, 자신의 몸에 닿았을 때
    else:  # 진행하기
        if board[fs][fg] != 2:  # 사과 못 먹기
            tail = bambody.pop(0) # 꼬리 치우기 - 1
            board[tail[0]][tail[1]] = 0  # 꼬리 치우기 - 2
        board[fs][fg] = 1
        head = [fs, fg]
        bambody.append([fs, fg])
    time += 1

print(time+1)
