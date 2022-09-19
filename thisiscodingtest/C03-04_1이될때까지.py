import sys

N, K = map(int, sys.stdin.readline().rstrip().split())


def solution_each(N, K):
    try_count = 0
    while N != 1:
        if N % K == 0:
            N /= K
        else:
            N -= 1
        try_count += 1
    print(try_count)


def solution_once(N, K):
    try_count = 0
    while True:
        while N % K != 0:
            N -= 1
            try_count += 1
        N /= K
        try_count += 1
        if N == 1:
            break
    print(try_count)


solution_once(N, K)
# 25 5
