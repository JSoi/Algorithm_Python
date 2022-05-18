def solution(arr1, arr2): # 3*2 - 2*3
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k]*arr2[k][j]
            row.append(temp)
        answer.append(row)
    return answer

a1 = [[1, 4], [3, 2], [4, 1]]
a2 = [[3, 3], [3, 3]]
print(solution(a1,a2))