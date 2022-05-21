# N-Queen
# https://www.acmicpc.net/problem/9663
N = int(input())
board = [-1] * N
count = 0
visited = [False] * N  # 열 방문 여부 저장


def go(row):
    if row >= N:  # 다 끝낸 것 - 정답 중 하나이다
        global count
        count += 1
        return
    # 다음으로 진행 필요
    for col in range(N):
        if visited[col]:
            continue
        board[row] = col
        if is_ok(row):
            visited[col] = True
            go(row + 1)
            visited[col] = False


def is_ok(check_row):  # 해당 행이 유효한지 검사함
    for each_row in range(check_row):
        if board[each_row] == board[check_row] or abs(check_row - each_row) == abs(board[check_row] - board[each_row]):
            return False
    return True


go(0)
print(count)
