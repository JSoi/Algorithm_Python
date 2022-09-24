import collections

answer = 0


def solution(info, edges):
    global answer, visit
    connlist = collections.defaultdict(list)
    # 최대 합 dictionary 설정

    for a, b in edges:
        connlist[a].append(b)

    # 재귀
    def rec(pos_list, visit, lamb, wolf):
        global answer
        answer = max(answer, lamb)

        for i in range(len(pos_list)):
            # 방문할 수 있는 후보 노드를 모두 순환
            target = pos_list[i]
            nextwolf = wolf + (1 if info[target] == 1 else 0)
            nextlamb = lamb + (1 if info[target] == 0 else 0)
            # 후보 노드를 방문하게 될 시 다음 늑대, 다음 양 개수 저장
            if nextlamb <= nextwolf:  # 후보 노드 방문 시 늑대 수가 같아지거나 많아지면 진행하지 X
                continue
            if target not in visit:  # 후보 노드를 방문 하지 않았을 경우
                visit.append(target)  # 방문하고 - 1
                rec(pos_list + connlist[target], visit, nextlamb, nextwolf)
                # 재귀-후보 리스트에 후보 노드 자식노드 더함
                visit.pop()  # 원상복구 - 2

    visit = [0]
    rec(connlist[0], visit, 1, 0)
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
