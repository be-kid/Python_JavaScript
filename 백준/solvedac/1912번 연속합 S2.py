from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

dp = [0 for _ in range(n)]


dp[0] = nums[0]

check = False

for i in range(1, n):
    dp[i] = max(dp[i-1]+nums[i] , 0)
    if nums[i] >= 0:
        check = True

if check:
    print(max(dp))
else:
    print(max(nums))
