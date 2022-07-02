from sys import stdin

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

for i in range(1, n):
    arr[i] = arr[i] + arr[i-1]

d = {}
for i in range(len(arr)):
    d[arr[i]] = 0
answer = 0
for i in range(len(arr)):
    if arr[i] == k or arr[i] - k in d:
        answer += 1
    
print(answer)