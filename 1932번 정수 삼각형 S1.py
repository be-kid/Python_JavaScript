from sys import stdin
n = int(stdin.readline())
tri = [list(map(int, stdin.readline().split())) for i in range(n)]

dp = [[0 for i in range(n)] for j in range(n)]

dp[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] = tri[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = tri[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = tri[i][j] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))
            