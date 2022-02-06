from sys import stdin
from collections import deque

a, b = map(int, stdin.readline().split())

q = deque()
q.append([a, 0])

check = True
while q:
    temp = q.popleft()

    if temp[0] * 2 == b or temp[0]*10 + 1 == b:
        print(temp[1]+2)
        check = False
        break
    if temp[0]*2 < b:
        q.append([temp[0]*2, temp[1]+1])
    if temp[0]*10 + 1 < b:
        q.append([temp[0]*10+1, temp[1]+1])

if check:
    print(-1)