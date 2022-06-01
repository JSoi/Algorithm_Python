import collections
import sys

student, compare = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e09)
high = collections.defaultdict(set)
low = collections.defaultdict(set)
for _ in range(compare):
    a, b = map(int, sys.stdin.readline().rstrip().split())  # a<b
    high[a].add(b)
    low[b].add(a)
print(high, low)
for k in range(1, student + 1):
    for a in range(1, student + 1):
        for b in range(1, student + 1):
            if k in high[a] and k in low[b]:
                for ele in list(low[a]): low[b].add(ele)
                for ele in list(low[k]): low[b].add(ele)
                for ele in list(high[k]): high[a].add(ele)
                for ele in list(high[b]): high[a].add(ele)
# print(high, low)
answer = 0
for i in range(1, student + 1):
    if len(low[i]) + len(high[i]) == student - 1:
        answer += 1
print(answer)
'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
