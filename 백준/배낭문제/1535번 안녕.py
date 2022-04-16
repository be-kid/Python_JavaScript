from sys import stdin

n = int(stdin.readline())
lose = list(map(int, stdin.readline().split())) # 잃는 체력
joy = list(map(int, stdin.readline().split())) # 얻는 기쁨

dp = [[0 for i in range(100)] for j in range(n)]

for i in range(n):
    for j in range(100):
        if i == 0:
            if lose[i] > j:
                dp[i][j] = 0
            else:
                dp[i][j] = joy[i]
        else:
            if lose[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - lose[i]] + joy[i])

print(dp[-1][-1])