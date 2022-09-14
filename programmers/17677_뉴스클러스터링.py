import itertools
import re


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    ccat1 = [str1[i1:i1 + 2] for i1 in range(len(str1) - 1)]
    ccat2 = [str2[i2:i2 + 2] for i2 in range(len(str2) - 1)]

    m = re.compile('[a-z]{2}')

    rslt1 = list(filter(lambda x: m.match(x), ccat1))
    rslt2 = list(filter(lambda x: m.match(x), ccat2))

    if len(rslt1) == 0 and len(rslt2) == 0:
        return 65536
    dict1 = dict2 = dict()

    for string in rslt1:
        dict1[string] = rslt1.count(string)
    for string in rslt2:
        dict2[string] = rslt2.count(string)

    intersection = union = list()
    for r1 in list(set(rslt1) | set(rslt2)):
        r1c = 0 if r1 not in dict1 else dict1[r1]
        r2c = 0 if r1 not in dict2 else dict2[r1]
        # print(r1, r1c, r2c)
        for i in range(min(r1c, r2c)):
            intersection.append(r1)
        for i in range(max(r1c, r2c)):
            union.append(r1)
    return int(65536 * (len(intersection) / len(union)))


# print(solution("E=M*C^2", "e=m*c^2"))
print(solution("handshake", "shake hands"))
