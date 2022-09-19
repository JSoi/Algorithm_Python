# 모험가 길드
import sys

N = int(sys.stdin.readline().rstrip())
fearlist = list(map(int, sys.stdin.readline().rstrip().split()))
fearlist.sort(reverse=True)
answer = 0
i = 0
while i < len(fearlist):
    target = fearlist[i]
    i += target
    # print(i)
    answer += 1
print(answer)
'''
5
2 3 1 2 2
'''
