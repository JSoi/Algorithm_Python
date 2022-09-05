import collections


def solution(N, stages):
    stageChallenge = [0] * (N + 2)
    stagePass = [0] * (N + 2)
    # 모든 스테이지에 대해서 순환한다

    for s in stages:
        for r in range(1, s):
            stageChallenge[r] += 1
            stagePass[r] += 1
        stageChallenge[s] += 1
    dic = collections.defaultdict(int)
    for i in range(1, N + 1):
        if stageChallenge[i] == 0:
            dic[i] = 0
        else:
            dic[i] = (stageChallenge[i]-stagePass[i]) / stageChallenge[i]
    dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    answer = list()
    for item in dic:
        answer.append(item[0])
    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
