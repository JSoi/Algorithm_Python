def solution(arr):
    answer = 1
    maxval = 1
    minval = min(arr)

    if (len(arr) == 1):
        print(arr[0])
        return arr[0]
    for i in range(1, minval + 1):
        flag = False
        for j in arr:
            if j % i == 0:
                continue
            else:
                flag = True
                break
        if not flag:
            maxval = max(maxval, i)
    print(maxval)
    for i in arr:
        answer *= (i // maxval)
    print('answer', answer * maxval)
    return answer * maxval


solution([1, 4, 5, 6, 7])
