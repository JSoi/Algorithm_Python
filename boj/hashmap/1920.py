import sys
#from pprint import pprint

a_cnt = int(input())
line_a = list(map(int, sys.stdin.readline().split()))
b_cnt = int(input())
line_b = list(map(int, sys.stdin.readline().split()))
# pprint(line_a)
# pprint(line_b)
answer = {}
a_map = {}
b_map = {}
for a in line_a:
    a_map[a] = 1 # 값이 들어가야 됨
for i in range(b_cnt):
    answer[i] = 0 # index가 필요
for i in range(b_cnt):
    if line_b[i] in a_map:
        answer[i] = 1
for i in range(b_cnt):
    print(answer.get(i))
