import collections
import itertools


def solution(orders, course):
    orderdict = collections.defaultdict(list)
    for o in range(len(orders)):
        for li in orders[o]:
            orderdict[li].append(o)
    print(orderdict)
    for c in course:
        for com in list(itertools.combinations(orderdict.keys(), c)):
            continue
    answer = []
    return answer


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4], )
