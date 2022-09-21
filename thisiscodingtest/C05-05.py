def factorial_iter(i):
    if i == 0: return 0
    ans = 1
    for k in range(1, i + 1):
        ans *= k
    return ans


def factorial_rec(i):
    if i == 1:
        return i
    return i * factorial_rec(i - 1)


print(factorial_iter(5))
print(factorial_rec(5))
