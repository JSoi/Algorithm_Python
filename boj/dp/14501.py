import sys

cnt = int(input())
time = []
money = []
dp = [0] * cnt
for _ in range(cnt):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    time.append(a)
    money.append(b)
for i in range(cnt):
    if i + time[i] > cnt:
        continue
    dp[i] += money[i]
    for j in range(i + time[i], cnt):
        dp[j] = max(dp[i], dp[j])
    # print(i ,dp)
print(max(dp))
'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''
