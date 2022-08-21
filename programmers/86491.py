def solution(sizes):
    garo = 0
    sero = 0
    for s in sizes:
        tGaro = max(s[0], s[1])
        tSero = min(s[0], s[1])
        garo = max(tGaro, garo)
        sero = max(tSero, sero)
    return garo * sero


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
