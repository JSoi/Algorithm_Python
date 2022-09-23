import collections

answer = 0


def solution(info, edges):
    global answer
    connlist = collections.defaultdict(list)
    # 최대 합 dictionary 설정

    for a, b in edges:
        connlist[a].append(b)

    # 재귀
    def rec(pos_list, visit, lamb, wolf):
        global answer
        answer = max(answer, lamb)
        for i in range(len(pos_list)):
            target = pos_list[i]
            nextwolf = wolf + (1 if info[target] == 1 else 0)
            nextlamb = lamb + (1 if info[target] == 0 else 0)
            if nextlamb <= nextwolf:
                continue
            if not visit[target]:
                temppostlist = pos_list[::]
                for c in connlist[target]:
                    if not visit[c]:
                        temppostlist.append(c)
                visit[target] = True
                rec(temppostlist, visit, nextlamb, nextwolf)
                visit[target] = False

    visit = [False for _ in range(len(info))]
    visit[0] = True
    rec(connlist[0], visit, 1, 0)
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
