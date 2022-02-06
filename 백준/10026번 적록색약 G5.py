from sys import stdin
from collections import deque

n = int(stdin.readline())
g = [list(stdin.readline().rstrip()) for i in range(n)]
check1 = [[0 for i in range(n)] for j in range(n)]

d = {0:(1,0), 1:(0,1), 2:(-1,0), 3:(0,-1)}

count1 = 1
q1 = deque()
q1.append((0,0))
check1[0][0] = 1

for i in range(n):
  for j in range(n):
    if check1[i][j] == 0:
      count1+=1
      q1.append((i,j))
      check1[i][j] = 1
    while q1:
      now = q1.popleft()
      for k in range(4):
        newx = now[0]+d[k][0]
        newy = now[1]+d[k][1]
        if 0 <= newx < n and 0 <= newy < n and check1[newx][newy]==0 and g[newx][newy] == g[now[0]][now[1]]:
          q1.append((newx,newy))
          check1[newx][newy] = 1

check2 = [[0 for i in range(n)] for j in range(n)]
count2 = 1
q2 = deque()
q2.append((0,0))
check2[0][0] = 1

for i in range(n):
  for j in range(n):
    if g[i][j] == 'G':
      g[i][j] = 'R'


for i in range(n):
  for j in range(n):
    if check2[i][j] == 0:
      count2+=1
      q2.append((i,j))
      check2[i][j] = 1
    while q2:
      now = q2.popleft()
      for k in range(4):
        newx = now[0]+d[k][0]
        newy = now[1]+d[k][1]
        if 0 <= newx < n and 0 <= newy < n and check2[newx][newy]==0 and g[newx][newy] == g[now[0]][now[1]]:
          q2.append((newx,newy))
          check2[newx][newy] = 1

print(count1, count2)
'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

4 3
'''