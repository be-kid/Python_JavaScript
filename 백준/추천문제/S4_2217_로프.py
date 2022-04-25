from sys import stdin

n = int(stdin.readline())
ropes = [0 for i in range(n)]
for i in range(n):
    ropes[i] = int(stdin.readline())

ropes.sort()

answer = 0
for i in range(n):
    if answer < ropes[i] * (n-i):
        answer = ropes[i] * (n-i)
        
print(answer)