from sys import stdin

n, k = map(int, stdin.readline().split())
items = [list(map(int, stdin.readline().split())) for i in range(n)]

dp = [[0 for i in range(k+1)] for j in range(n)]

for i in range(n):
    for j in range(1, k+1):
        if items[i][0] <= j:
            dp[i][j] = max(dp[i-1][j-items[i][0]] + items[i][1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])