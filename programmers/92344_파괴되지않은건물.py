import collections
import itertools


def solution_timeout(board, skill):
    for type, r1, c1, r2, c2, degree in skill:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                board[r][c] += ((-1 if type == 1 else 1) * degree)

    l = list(list(filter(lambda item: item > 0, b)) for b in board)
    return sum(len(ll) for ll in l)


def solution(board, skill):
    hap_map = collections.defaultdict(int)
    comb_dict = collections.defaultdict(set)
    for type, r1, c1, r2, c2, degree in skill:
        val = degree * (-1 if type == 1 else -1)
        if val not in comb_dict:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    comb_dict[val].add((r, c))


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
