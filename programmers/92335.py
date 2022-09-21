import math
import re


def solution(n, k):
    k_num = ''
    # N진수 변환
    while n > 0:
        k_num = str(n % k) + k_num
        n //= k
    prime_cand = list(map(int, re.sub('0+', '0', k_num).strip('0').split('0')))

    def prime(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    answer = 0
    for pk in prime_cand:
        if pk >= 2 and prime(pk):
            answer += 1

    return answer


# print(solution(1, 3))
# print(solution(110011, 10))
# print(solution(437674, 3))
