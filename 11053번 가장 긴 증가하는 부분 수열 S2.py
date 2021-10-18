from sys import stdin

n = int(stdin.readline())

nums = list(map(int, stdin.readline().split()))
dp = [0 for i in range(n)]

dp[0] = 1
max_num = nums[0]
for i in range(1, n):
    if nums[i] > nums[i-1]:
        if max_num < nums[i]:
            dp[i] = dp[i-1] + 1
            max_num = nums[i]
        else:
            if dp[i-1] > 2:
                dp[i] = dp[i-1]
            else:
                dp[i] = 2
                max_num = nums[i]
    else:
        dp[i] = dp[i-1]
print(dp)
print(dp[-1])


'''
6
10 20 10 30 20 50

1 2 2 3 3 4

i번째가 끝인 경우를 기록하면
i-1보다 크고 지금까지의 최대값보다 크면 dp[i-1] + 1
i-1보다 크고 지금까지의 최대값보다 크지 않으면 dp[i-1]
작으면 dp[i-1]


30 40 30 40 50 60
 1  2  2  2  3  4


5
40 1 5 10 90
 1 1 2  3  4

앞에꺼보다 크면 +1 할지말지 

16
277 730 790 994 242 185 633 545 830 557 194 994 44 28 755 661
  1   2   3   4   4   4   4   4   4   
'''