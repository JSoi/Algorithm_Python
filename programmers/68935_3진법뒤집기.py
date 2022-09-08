def solution(n):
    ans = ''
    while n > 0:
        ans += str(n % 3)
        n //= 3
    realans = 0
    for i in range(len(ans)):
        realans += int(ans[i]) * (3 ** (len(ans) - i - 1))
    return realans


solution(45)
