def solution(n, lost, reserve):
    clothes = [1] * n
    for r in reserve:
        clothes[r - 1] += 1
    for l in lost:
        clothes[l - 1] -= 1
    for i in range(n):
        if clothes[i] == 2:
            if i - 1 in range(0, n) and clothes[i - 1] == 0:
                clothes[i] -= 1
                clothes[i - 1] += 1
            elif i + 1 in range(0, n) and clothes[i + 1] == 0:
                clothes[i] -= 1
                clothes[i + 1] += 1
    return n - clothes.count(0)