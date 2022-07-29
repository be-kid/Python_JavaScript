from sys import stdin

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

for i in range(1, n):
    arr[i] = arr[i] + arr[i-1]

d = {}
