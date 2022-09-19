import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
cards = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
maxval = 0
for i in range(1, N + 1):
    mincard = min(cards[i - 1])
    if maxval <= mincard:
        maxval = mincard
print(maxval)
'''
3 3
3 1 2 
4 1 4
2 2 2
'''
'''
2 4
7 3 1 8
3 3 3 4
'''
