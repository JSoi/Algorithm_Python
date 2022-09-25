import collections
import sys

N = int(sys.stdin.readline().rstrip())
scoredict = collections.defaultdict(list)
for _ in range(N):
    name, score = sys.stdin.readline().rstrip().split()
    score = int(score)
    scoredict[score].append(name)
scoredict = sorted(scoredict.items(), key=lambda x: x[0])
# print(scoredict)
result = list()
for item in scoredict:
    result += item[1]
print(' '.join(result))
'''
2
홍길동 95
이순신 77
'''
