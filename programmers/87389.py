def solution(n):
    answer = 1
    while True:
        if n % answer==1:
            return answer
        else:
            answer+=1
    return answer