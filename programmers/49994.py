def solution(dirs):
    ds = [0, 0, 1, -1]
    dg = [1, -1, 0, 0]
    mydir = ['U', 'D', 'R', 'L']
    route = set()

    def go(s, g, di):  # 세로, 가로, 방향
        ns = s
        ng = g
        for i, j in enumerate(mydir):
            if j == di:
                ns += ds[i]
                ng += dg[i]
        if ns < -5 or ns > 5 or ng < -5 or ng > 5:
            ns, ng = s, g
        if ns != s or ng != g:
            sortlist = [(ns, ng), (s, g)]
            sortlist = sorted(sortlist, key=lambda x: (x[0], x[1]))
            # print(sortlist)
            route.add((sortlist[0][0], sortlist[0][1], sortlist[1][0], sortlist[1][1]))
        return ns, ng

    sero = garo = 0
    for d in dirs:
        sero, garo = go(sero, garo, d)
    print(route)
    return len(route)


def solution2(numbers, target):
    global answer
    answer = 0

    def dfs(index, hap):
        # print(hap)
        if index > len(numbers):
            return
        if index == len(numbers):
            if target == hap:
                global answer
                answer += 1
            return
        dfs(index + 1, hap + numbers[index])
        dfs(index + 1, hap - numbers[index])

    dfs(0, 0)
    return answer


# print(solution2([4, 1, 2, 1], 4))
print(solution("ULURRDLLU"))

print(solution("LULLLLLLU"))
