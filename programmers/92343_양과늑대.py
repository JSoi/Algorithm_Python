import collections
import copy


def solution(info, edges):
    connlist = collections.defaultdict(list)
    catchlist = [0 for _ in range(len(info) + 1)]
    # 최대 합 dictionary 설정
    max_catch_dict = collections.defaultdict(list)
    catchlist[0] = 1

    # 재귀
    def rec(pos_list, visit, lamb, wolf, info, connlist, max_catch_dict):
        max_catch_dict[lamb].append(visit.count(True))
        for i in range(len(pos_list)):
            target = pos_list[i]
            if visit[target]:
                continue
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
                rec(temppostlist, visit, nextlamb, nextwolf, info, connlist, max_catch_dict)
                visit[target] = False

    visit = [False for _ in range(len(info))]
    visit[0] = True
    for a, b in edges:
        connlist[a].append(b)
    # 방문 노드, 방문할 수 있는 노드 리스트, 방문 여부 배열, 양, 늑대, 연결 그래프
    rec(connlist[0], visit, 1, 0, info, connlist, max_catch_dict)
    return max(max_catch_dict.keys())


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
