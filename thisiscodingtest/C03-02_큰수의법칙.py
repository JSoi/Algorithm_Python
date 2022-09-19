import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort(reverse=True)
count = index = answer = 0
while M > 0:
    if count == K:
        count = 0
        index = 1
    answer += arr[index]
    count += 1
    if index == 1:
        count = 0
        index = 0
    M -= 1
print(answer)
'''
5 8 3
2 4 5 4 6
'''
