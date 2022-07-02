from sys import stdin

n, m = map(int, stdin.readline().split())
w = list(map(int, stdin.readline().split()))

items = {}

for i in w:
    if i in items:
        items[i] += 1
    else:
        items[i] = 1

dp = [-1 for i in range(n+1)]
dp[0] = 0

'''
dp[n] -> n그릇을 몇번만에 만들 수 있나?
'''

for i in range(1, n + 1):
    