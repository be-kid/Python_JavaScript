x = input()
y = input()
dp = [[0 for i in range(len(y))] for i in range(len(x))]

if x[0] == y[0]:
   dp[0][0] = 1

for i in range(1, len(y)):
   if x[0] == y[i]:
      dp[0][i] = 1
   else:
      dp[0][i] = dp[0][i-1]


for i in range(1, len(x)):
   for j in range(len(y)):
      if j == 0 and x[i]==y[j]:
         dp[i][j] = 1
      elif j == 0 and x[i]!=y[j]:
         dp[i][j] = dp[i-1][j]
      else:
         if x[i]==y[j]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1, dp[i][j-1])
         else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
print(dp[-1][-1])         
