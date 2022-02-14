from sys import stdin

n = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(n)]

dp = [0 for _ in range(n)]

dp[0] = nums[0]
if n>1:
    dp[1] = nums[0] + nums[1]
if n>2:
    dp[2] = max(nums[2]+nums[1], max(nums[2]+nums[0], dp[1]))

for i in range(3, n):
    dp[i] = max(nums[i]+nums[i-1]+dp[i-3], max(nums[i]+dp[i-2], dp[i-1]))
    
print(dp[-1])