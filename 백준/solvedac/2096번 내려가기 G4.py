from sys import stdin
'''
n = int(stdin.readline())
nums = [list(map(int, stdin.readline().split())) for i in range(n)]

dp = [[[0 for i in range(3)] for j in range(n)] for k in range(2)]

dp[0][0][0] = nums[0][0]
dp[0][0][1] = nums[0][1]
dp[0][0][2] = nums[0][2]

dp[1][0][0] = nums[0][0]
dp[1][0][1] = nums[0][1]
dp[1][0][2] = nums[0][2]

for i in range(1, n):
    left_max = max(dp[0][i-1][0], dp[0][i-1][1])
    right_max = max(dp[0][i-1][1], dp[0][i-1][2])
    dp[0][i][0] = nums[i][0] + left_max
    dp[0][i][1] = nums[i][1] + max(left_max, right_max)
    dp[0][i][2] = nums[i][2] + right_max
    
    left_min = min(dp[1][i-1][0], dp[1][i-1][1])
    right_min = min(dp[1][i-1][1], dp[1][i-1][2])
    dp[1][i][0] = nums[i][0] + left_min
    dp[1][i][1] = nums[i][1] + min(left_min, right_min)
    dp[1][i][2] = nums[i][2] + right_min
    
print(max(dp[0][-1]), end=' ')
print(min(dp[1][-1]))
'''

n = int(stdin.readline())
dp = [[0 for i in range(3)] for j in range(2)]
for i in range(n):
    nums = list(map(int, stdin.readline().rstrip().split()))
    
    left_max = max(dp[0][0], dp[0][1])
    right_max = max(dp[0][1], dp[0][2])
    
    left_min = min(dp[1][0], dp[1][1])
    right_min = min(dp[1][1], dp[1][2])
    
    dp[0][0] = nums[0] + left_max
    dp[0][1] = nums[1] + max(left_max, right_max)
    dp[0][2] = nums[2] + right_max
    
    dp[1][0] = nums[0] + left_min
    dp[1][1] = nums[1] + min(left_min, right_min)
    dp[1][2] = nums[2] + right_min

print(str(max(dp[0]))+' '+str(min(dp[1])))