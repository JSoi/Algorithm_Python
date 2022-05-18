def solution(prices):
    answer = [0] * len(prices)
    temp = []
    for i, price in enumerate(prices):
        if len(temp) ==0:  # 비어있을 떄
            temp.append(i)
            continue
        for i in range(len(temp) - 1, -1, -1):
            p = temp[i]
            print(p)
            if price < prices[p]:
                answer[p] = i - p
                del p[i]

    return answer


print(solution(	[1, 2, 3, 2, 3]))
