from sys import stdin

mod = 1000000007

s = stdin.readline().rstrip()
n = len(s)
dp = [[0 for i in range(n)] for j in range(n)]

for i in range(0, n):
    for j in range(i + 1, n):
        