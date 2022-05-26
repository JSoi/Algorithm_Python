import itertools
import re


def solution(s):
    slist = textAmend(s)
    slist.sort(key=len)
    answer = []
    for tuple in slist:
        for i in tuple:
            if i not in answer:
                answer.append(i)
    return answer


def textAmend(s):
    split_str = s.split('},')
    lst = []
    for s in split_str:
        minilist = list(map(int, re.sub('{|}', '', s).split(',')))
        lst.append(minilist)
    return lst


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
