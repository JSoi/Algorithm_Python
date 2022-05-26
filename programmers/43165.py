#https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    global answer
    answer = 0
    def dfs(index, hap):
        #print(hap)
        if index == len(numbers):
            if target == hap:
                global answer
                answer += 1
            return
        dfs(index + 1, hap + numbers[index])
        dfs(index + 1, hap - numbers[index])
    dfs(0, 0)
    return answer