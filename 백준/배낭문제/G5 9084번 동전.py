from sys import stdin

# 동전 1~10000원
# 만들 금액 1~10000원

# 모든 방법의 수

# i번째 동전을 사용했을 때 j원을 만드는 방법...
# dp[i-1][j-coin[i]] + dp[i-1][j-coin[i]*2] + ...

test = int(stdin.readline())
for t in range(test):
    n = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    
    dp = [[0 for i in range(m + 1)] for j in range(n)]
    
    # 0원을 만드는 것은 1로 한다. 목표 금액이 coins[i]로 나누어 떨어지는 경우를 위해서
    
    for i in range(n):
        for j in range(m + 1):
            if i == 0:
                if j % coins[i] == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                for k in range(j, -1, -coins[i]):
                    dp[i][j] += dp[i-1][k]
    
    print(dp[-1][-1])