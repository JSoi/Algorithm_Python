import itertools


def solution(nums):
    answer = 0
    nums.sort()
    comblist = list(itertools.combinations(nums, 3))
    for c in comblist:
        if isPrime(sum(c)):
            answer += 1
    return answer


def isPrime(num):
    if num == 2:
        return True
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True
