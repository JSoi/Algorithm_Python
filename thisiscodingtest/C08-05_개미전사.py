N = int(input())
arr = list(map(int, input().rstrip().split()))
dp = [0] * N
# 점화식 : f(x) = max(f(x-1), f(x-2)+arr[x])
# Bottom-up 방식
dp[0], dp[1] = arr[0], max(arr[1], arr[0])
for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
print(max(dp))
'''
4
1 3 1 5
'''
