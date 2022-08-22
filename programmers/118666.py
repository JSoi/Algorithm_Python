import collections


def solution(survey, choices):
    dict = collections.defaultdict(dict)
    chars = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    for c in chars:
        dict[c] = 0
    score = [0, -3, -2, -1, 0, 1, 2, 3]  # 스코어 리스트
    for i in range(len(survey)):
        minus = survey[i][0]  # 비동의시의 character
        plus = survey[i][1]  # 동의시의 character
        if score[choices[i]] < 0:
            dict[minus] += abs(score[choices[i]])
        else:
            dict[plus] += abs(score[choices[i]])
    dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
    answer = dict[0][0] + dict[1][0] + dict[2][0] + dict[3][0]
    print(answer)
    return answer


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
