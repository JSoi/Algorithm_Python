import sys

N = int(sys.stdin.readline().rstrip())
H = M = S = 0
# 3600, 60, 1
answer = 0
second = 0
while not (H == N and M == 59 and S == 59):
    second += 1
    H = second // 3600
    M = (second - H * 3600) // 60
    S = second % 60
    if '3' in str(H) + str(M) + str(S):
        answer += 1

print(answer)

# 5
