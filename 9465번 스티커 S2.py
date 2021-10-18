from sys import stdin

T = int(stdin.readline())

for i in range(T):
    n = int(stdin.readline())
    s = [list(map(int, stdin.readline().split())) for i in range(2)]

    dp = [[0 for i in range(n)] for j in range(2)]

    dp[0][0] = s[0][0]
    dp[1][0] = s[1][0]
    if n > 1:
        dp[0][1] = s[0][1] + s[1][0]
        dp[1][1] = s[1][1] + s[0][0]
    for i in range(2, n):
        for j in range(2):
            dp[j][i] = max(s[j][i] + dp[(j+1)%2][i-1], s[j][i] + dp[(j+1)%2][i-2])
            
    if n == 1:
        print(max(dp[0][-1], dp[1][-1]))
    else:
        print(max(max(dp[0][-1], dp[0][-2]), max(dp[1][-1], dp[1][-2])))

'''
3
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
4
100   1     1   100
  1   1   100     1


'''