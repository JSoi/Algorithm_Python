# https://www.acmicpc.net/problem/1759
# 암호 만들기
import itertools

alp, alpcount = map(int, input().split())
line = list(map(str, input().split()))
line.sort()
print(line)
vowel = []
cons = []
answer = list()
for l in line:
    if l in 'aeiou':
        vowel.append(l)
    else:
        cons.append(l)


# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
# 모음 1개 자음 3개
# 모음 2개 자음 2개
# 3 ≤ L ≤ C ≤ 15.. 다행이다

def go():
    for l in list(itertools.combinations(line, alp)):
        mvo = mco = 0
        for li in ''.join(l):
            if li in vowel:
                mvo += 1
            if li in cons:
                mco += 1
        if mvo < 1 or mco < 2:
            continue
        else:
            print(''.join(l))


def back():
    pass
go()
