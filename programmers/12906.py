def solution(arr):
    answer = []
    while len(arr) > 0:
        last_ele = arr.pop()
        if len(answer) == 0 or last_ele != answer[-1]:
            answer.append(last_ele)
    answer.reverse()
    return answer


solution([1, 1, 3, 3, 0, 1, 1])
