import itertools
import sys

global answer
answer = sys.maxsize

INF = int(1e09)


def solution(alp, cop, problems):
    alp_max = max(problems, key=lambda x: x[0])[0]
    cop_max = max(problems, key=lambda x: x[1])[1]
    alp = min(alp, alp_max)
    cop = min(cop, cop_max)
    cost = [[INF for _ in range(cop_max + 1)] for _ in range(alp_max + 1)]
    cost[alp][cop] = 0
    for r in range(alp, alp_max + 1):
        for c in range(cop, cop_max + 1):
            if r + 1 <= alp_max:
                cost[r + 1][c] = min(cost[r + 1][c], cost[r][c] + 1)
            if c + 1 <= cop_max:
                cost[r][c + 1] = min(cost[r][c + 1], cost[r][c] + 1)

            for alp_start, cop_start, alp_inc, cop_inc, cost_inc in problems:
                if alp_start > r or cop_start > c:
                    continue
                alp_next, cop_next = min(alp_max, r + alp_inc), min(cop_max, c + cop_inc)
                cost[alp_next][cop_next] = min(cost[alp_next][cop_next], cost[r][c] + cost_inc)
    return cost[alp_max][cop_max]


def solution_recursive(alp, cop, problems):
    # 모든 문제들을 풀 수 있으면 됨
    problems = sorted(problems, key=lambda x: (x[0], x[1]))
    alp_max = max(problems, key=lambda x: x[0])[0]
    cop_max = max(problems, key=lambda x: x[1])[1]
    alp = min(alp, alp_max)
    cop = min(cop, cop_max)

    def go(index, alp_now, cop_now, time):
        # print(index, alp_now, cop_now, time)
        global answer
        if alp_now >= alp_max and cop_now >= cop_max:
            answer = min(answer, time)
            return
        if index >= len(problems):
            return

        need_alp, need_cop, inc_alp, inc_cop, cost = problems[index]
        if alp_now >= need_alp and cop_now >= need_cop:  # 문제를 풀 수 있을 때
            go(index, alp_now + inc_alp, cop_now + inc_cop, time + cost)  # 풀고 증가시킴(한 번)
            go(index + 1, alp_now, cop_now, time)  # 풀지 않고 넘김
        else:  # 문제를 풀 수 없을 때
            cha_cop = 0 if need_cop <= cop_now else need_cop - cop_now
            cha_alp = 0 if need_alp <= alp_now else need_alp - alp_now
            go(index, need_alp, need_cop, time + cha_cop + cha_alp)  # 직접 증가시킴
            go(index + 1, alp_now, cop_now, time)  # 넘김

    go(0, alp, cop, 0)
    return answer


# print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
# print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
# print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
