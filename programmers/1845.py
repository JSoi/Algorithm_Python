import itertools

def solution(nums):
    answer = 0
    comb = list(itertools.combinations(nums,len(nums)//2))
    for c in comb:
        answer = max(len(set(c)),answer)
    return answer