# 수평으로 두 칸 이동 후 수직으로 한 칸
# 수직으로 두 칸 이동 후 수평으로 한 칸
import sys

move_type = [(-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
col_type = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
knight = sys.stdin.readline().rstrip()
col, row = knight[0], int(knight[1])
print(col, row)
for ct in range(len(col_type)):
    if col == col_type[ct]:
        col = ct + 1
answer = 0
for mt in move_type:
    if mt[0] + col in range(1, 9) and mt[1] + row in range(1, 9):
        answer += 1
print(answer)
