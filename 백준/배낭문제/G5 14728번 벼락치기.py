from sys import stdin
n, T = map(int, stdin.readline().split())
k = [0 for i in range(n)] # 공부 시간
s = [0 for i in range(n)] # 배점
for i in range(n):
    k[i], s[i] = map(int, stdin.readline().split())
    
# 주어진 공부 시간 동안 효율적으로 공부해서 가장 높은 점수를 받아야한다.

dp = [[0 for i in range(T + 1)] for j in range(n)]

for i in range(n):
    for j in range(T + 1):
        if i == 0:
            if j < k[i]:
                dp[i][j] = 0
            else:
                dp[i][j] = s[i]
        else:
            if j < k[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-k[i]]+s[i])

print(dp[-1][-1])