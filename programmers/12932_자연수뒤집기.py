def solution(n):
    answer = []
    string = str(n)
    for i in range(len(n),-1):
        answer.append(int(string[i]))
    print(answer)
    return answer