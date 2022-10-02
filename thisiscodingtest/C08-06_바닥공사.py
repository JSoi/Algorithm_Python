N = int(input())
dp = [0] * (N + 1)
dp[1] = 1  # 1칸
dp[2] = 3  # 2칸
for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796
print(dp[N])
# 3
