import collections


def solution(n, results):
    windict = collections.defaultdict(set)  #
    losedict = collections.defaultdict(set)

    for r in results:
        windict[r[0]].add(r[1])
        losedict[r[1]].add(r[0])
    print(windict, losedict)

    for d in range(1, n + 1):
        for winele in windict[d]:  # 앞선 이긴 리스트
            for loseele in losedict[d]:
                losedict[winele].add(loseele)
                windict[loseele].add(winele)

    # print(windict, losedict)

    answer = 0
    for d in range(1, n + 1):
        concatset = set()
        concatset.update(windict[d])
        concatset.update(losedict[d])
        # print(d, 'concatset', concatset)
        if len(concatset) >= n - 1:
            answer += 1

    # print(answer)
    return answer


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
