import itertools

a, b = map(int, input().split())

for i in list(itertools.permutations(range(1, a + 1), b)):
    print(' '.join(map(str, list(i))))
