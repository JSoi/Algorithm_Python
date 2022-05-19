def solution(prices):
    answer = [0] * len(prices)
    temp = []
    for i, price in enumerate(prices):
        while temp and prices[temp[-1]] > price:
            tp = temp.pop()
            answer[tp] = i - tp
        temp.append(i)
    return answer


def solution2(prices):
    answer = [0] * len(prices)
    temp = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer

print(solution2([1, 2, 3, 2, 3]))
