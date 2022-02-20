from sys import stdin

n = int(stdin.readline())

INF = float('inf')
dp = [INF for i in range(n+1)]

if n > 2:
    dp[3] = 1
if n > 4:
    dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-3]+1, dp[i-5]+1)

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])