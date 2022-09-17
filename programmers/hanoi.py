import sys

global minval,answer
minval = sys.maxsize
def solution(n):
    stack_1 = [i for i in range(n, 0, -1)]
    stack_2 = stack_3 = list()
    def go(s1, s2, s3, result):
        if len(s3) == n and len(result) < minval:
            answer = result
            val = len(result)
            return
        if s1:
            s1copy = s1[::]
            s1copy.pop()
            one = s1[-1]
            go(s1copy, s2.append(one), s3, result.append([1, 2]))
            go(s1copy, s2, s3.append(one), result.append([1, 3]))
        if s2:
            s2copy = s2[::]
            s2copy.pop()
            two = s2[-1]
            go(s1, s2copy, s3.append(two), result.append([2, 3]))

    answer = list()
    go(stack_1, stack_2, stack_3, answer)

    return answer


solution(2)
