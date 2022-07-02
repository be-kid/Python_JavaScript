from sys import stdin
from collections import deque

drop = [list(map(int, stdin.readline().split())) for i in range(7)]
b = int(stdin.readline())

qs = [deque() for i in range(7)]

sizeY = [0 for i in range(7)]

for i in range(7):
    for j in range(6, -1, -1):
        if drop[j][i] != 0:
            qs[i].append(drop[j][i])

for i in range(7):
    for j in range(len(qs[i])):
        if qs[i][j] != 0:
            sizeY[j] += 1
    
for i in qs:
    print(i)
print(sizeY)
