N, M = map(int, input().rstrip().split())
INF = int(1e09)
dp = [INF] * 10001
money = []
for _ in range(N):
    m = int(input().rstrip())
    dp[m] = 1
    money.append(m)
for i in range(2,M+1):
    if k in range(i,1,):
print(money)
# 3
'''
2 15
2
3
'''
