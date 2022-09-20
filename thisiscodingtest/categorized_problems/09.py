# https://school.programmers.co.kr/learn/courses/30/lessons/60057
import sys


def solution(s):
    answer = sys.maxsize
    for cut in range(1, len(s) // 2 + 2):
        # print('cut', cut)
        i = 0
        bf_char = ''
        bf_count = 0
        cutchar = ''
        for i in range(0, len(s), cut):
            if bf_char == '':
                bf_char = s[i:i + cut]
                bf_count = 1
                continue
            if bf_char == s[i:i + cut]:  # 같을 경우
                bf_count += 1
            else:  # 다를 경우
                cutchar += (('' if bf_count <= 1 else str(bf_count)) + bf_char)
                bf_count = 1
            bf_char = s[i:i + cut]
        if i + cut >= len(s):
            cutchar += (('' if bf_count <= 1 else str(bf_count)) + bf_char)
        # print('i', i)
        # print(cutchar)
        answer = min(answer, len(cutchar))
        # print()
    return answer


print(solution("a"))
