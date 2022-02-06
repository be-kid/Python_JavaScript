from sys import stdin

n = int(stdin.readline())

nums = list(map(int, stdin.readline().split()))
dp = [0 for i in range(n)]
dp[0] = 1

for i in range(1, n):
    temp = 0
    for j in range(i):
        if nums[i] > nums[j]:
            temp = max(temp, dp[j])
    dp[i] = temp+1

print(max(dp))



'''
6
10 20 10 30 20 50
1 2 2 3 3 4

6
30 40 30 40 50 60
 1  2  2  2  3  4


5
40 1 5 10 90
 1 1 2  3  4


16
277 730 790 994 242 185 633 545 830 557 194 994 44 28 755 661

i번째가 마지막
1~i-1에서 i번째보다 작은것들 중 가장 큰 dp값

'''