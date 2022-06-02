def solution(n, times):
    # n : 입국심사 기다리는 사람
    # times : 심사관이 한 명 심사하는 데 걸리는 시간
    mid = 0
    times.sort(reverse=True)
    s, l = 0, times[0] * n
    # 왠지 이진탐색
    while s <= l:
        mid = (s + l) // 2  # 시간을 기준으로
        handle_ppl = 0
        for t in times:
            handle_ppl += mid // t
        if handle_ppl >= n:
            l = mid - 1
        else: # handle_ppl<n
            s = mid + 1
    return s


print((solution(6, [7, 10])))
# assert (solution(6, [7, 10])) == 28
