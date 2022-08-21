def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    ln = [1, 4, 7]
    rn = [3, 6, 9]
    for i in range(len(numbers)):
        now = giveNumber(numbers[i])
        if numbers[i] in ln:
            answer += 'L'
            left = now
        elif numbers[i] in rn:
            answer += 'R'
            right = now
        else:
            ld = abs(now[0] - left[0]) + abs(now[1] - left[1])
            rd = abs(now[0] - right[0]) + abs(now[1] - right[1])
            if ld < rd:
                answer += 'L'
                left = now
            elif ld > rd:
                answer += 'R'
                right = now
            else:
                if hand == "left":
                    answer += 'L'
                    left = now
                else:
                    answer += 'R'
                    right = now

    return answer


def giveNumber(num):
    keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    for i in range(4):
        for j in range(3):
            if keyboard[i][j] == num:
                return [i, j]
    return [-1, -1]



print(solution(	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))