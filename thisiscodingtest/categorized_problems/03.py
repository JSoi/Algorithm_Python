# 문자열 뒤집기
# https://www.acmicpc.net/problem/1439
import sys

S = sys.stdin.readline().rstrip()
numlist = [int(S[i]) for i in range(len(S))]
bf, to_one = numlist[0], 0
for i in range(1, len(S)):  # 0->1로
    if numlist[i] == 1:  # 1일 경우
        if bf == 0:  # 0-1 bf 뒤집어주기
            to_one += 1
    bf = numlist[i]

if numlist[-1] == 0:
    to_one += 1

bf, to_zero = numlist[0], 0
for i in range(1, len(S)):  # 1->0로
    if numlist[i] == 0:  # 0일 경우
        if bf == 1:  # 0-1 bf 뒤집어주기
            to_zero += 1
    bf = numlist[i]
if numlist[-1] == 1:
    to_zero += 1
# print(to_one, to_zero)
print(min(to_zero, to_one))
# 0001100
