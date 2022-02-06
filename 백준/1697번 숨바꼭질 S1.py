from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
q = deque()

check = [0 for i in range(100001)]

start = (n, 0)
q.append(start)
while q:
  now = q.popleft()
  check[now[0]] = 1
  if now[0] == k:
    print(now[1])
    break
  else:
    if now[0]-1 >= 0 and check[now[0]-1]==0:
      q.append((now[0]-1, now[1]+1))
    if now[0]+1 < 100001 and check[now[0]+1]==0:  
      q.append((now[0]+1, now[1]+1))
    if now[0]*2 < 100001 and check[now[0]*2]==0:
      q.append((now[0]*2, now[1]+1))
