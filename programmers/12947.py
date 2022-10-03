def solution(x):
    total = 0
    strx = str(x)
    for i in range(len(strx)):
        total += int(strx[i])
    if x % total == 0:
        return True
    return False
