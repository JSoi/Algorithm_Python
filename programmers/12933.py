def solution(n):
    dictlist = [0] * 10
    answer = ''
    strn = str(n)
    for i in range(len(strn)):
        dictlist[int(strn[i])] += 1
    for k in range(9, -1, -1):
        answer += ''.join([str(k) for _ in range(dictlist[k])])
    return int(answer)
