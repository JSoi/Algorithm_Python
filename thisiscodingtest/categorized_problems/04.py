# 만들수 없는 금액
import itertools
import sys

N = int(sys.stdin.readline().rstrip())
money = list(map(int, sys.stdin.readline().rstrip().split()))
money.sort()
hapset = set()
answer = sum(money)
for i in range(1, len(money)):
    for l in list(itertools.combinations(money, i)):
        hapset.add(sum(l))
for i in range(1, sum(money)):
    if i not in hapset:
        answer = i
        break
print(answer)

'''
5
3 2 1 1 9
'''
