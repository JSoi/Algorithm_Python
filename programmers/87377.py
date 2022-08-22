from itertools import combinations


def solution(line):
    c = combinations(line, 2)
    cross = list()
    minX = minY = maxX = maxY = 0
    for line in c:
        a, b, e = line[0]
        c, d, f = line[1]
        parent = a * d - b * c
        if parent == 0 or (b * f - e * d) % parent != 0 or (e * c - a * f) % parent != 0:
            continue
        x = (b * f - e * d) // parent
        y = (e * c - a * f) // parent
        cross.append((x, y))
    cross.sort(key=lambda x: x[0])
    minX, maxX = cross[0][0], cross[-1][0]
    cross.sort(key=lambda x: (x[1],x[0]))
    minY, maxY = cross[0][1], cross[-1][1]
    # print(minX, maxX, minY, maxY)
    print('cross:', cross)
    answer = [['.' for xx in range(minX, maxX + 1)] for yy in range(minY, maxY + 1)]
    print(answer)
    for c in cross:
        print('test',int(c[1]) + abs(maxY),int(c[0]) + abs(minX))
        answer[int(c[1]) + abs(maxY)][int(c[0]) + abs(minX)] = '*'

    return [''.join(a) for a in answer]


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])