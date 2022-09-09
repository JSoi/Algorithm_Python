import math


def solution(n):
    sqrtval = math.sqrt(n)
    if sqrtval == int(sqrtval):
        return int((sqrtval+1)**2)
    return -1