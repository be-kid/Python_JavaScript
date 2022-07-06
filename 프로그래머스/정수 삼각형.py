def solution(triangle):
    t_len = len(triangle)
    
    dp = [[0 for i in range(t_len)] for j in range(t_len)]
    dp[0][0] = triangle[0][0]
    
    result = dp[0][0]
    
    for i in range(1, t_len):
        for j in range(0, i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif i == j:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(triangle[i][j]+dp[i-1][j-1], triangle[i][j]+dp[i-1][j])
            result = max(dp[i][j], result)
    return result
