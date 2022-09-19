import itertools
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
ball_list = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
for a, b in list(itertools.combinations(ball_list, 2)):
    if a != b:
        count += 1
print(count)
'''
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
'''
