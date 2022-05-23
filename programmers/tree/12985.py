import math


def solution(n, a, b):
    answer = 1
    tempA = a
    tempB = b
    a = min(tempA, tempB)
    b = max(tempA, tempB)
    while b - a != 1 or b // 2 - a // 2 != 1:
        answer += 1
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
    return answer


print(solution(1000000, 250000, 1))
