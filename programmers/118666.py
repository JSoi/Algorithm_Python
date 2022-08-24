import collections


def solution(survey, choices):
    prob = collections.defaultdict(dict)
    chars = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    for c in chars:
        prob[c] = 0
    score = [0, -3, -2, -1, 0, 1, 2, 3]  # 스코어 리스트
    for i in range(len(survey)):
        minus = survey[i][0]  # 비동의시의 character
        plus = survey[i][1]  # 동의시의 character
        if score[choices[i]] < 0:
            prob[minus] += abs(score[choices[i]])
        elif score[choices[i]] > 0:
            prob[plus] += abs(score[choices[i]])
    answer = ''
    answer += 'T' if prob['T'] > prob['R'] else 'R'
    answer += 'F' if prob['F'] > prob['C'] else 'C'
    answer += 'M' if prob['M'] > prob['J'] else 'J'
    answer += 'N' if prob['N'] > prob['A'] else 'A'

    return answer