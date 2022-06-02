def solution(triangle):
    # INF = int(1e09)
    dp = [0] * (len(triangle) + 1)
    for i in range(len(triangle) - 1, -1, -1): # 행\
        for j in range(i + 1): # 열
            dp[j] = triangle[i][j] + max(dp[j], dp[j + 1])
    return dp[0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
