from sys import stdin
from collections import deque

m,n,h = map(int, stdin.readline().split())

tmt = [[list(map(int, stdin.readline().split())) for i in range(n)] for j in range(h)]

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,-1,1]

q = deque()
for i in range(h):
  for j in range(n):
    for k in range(m):
      if tmt[i][j][k] == 1:
        q.append((i,j,k))

while q:
  now = q.popleft()
  for i in range(6):
    new_z = now[0]+dz[i]
    new_x = now[1]+dy[i]
    new_y = now[2]+dx[i]
    if 0<=new_z<h and 0<=new_x<n and 0<=new_y<m and tmt[new_z][new_x][new_y]==0:
      tmt[new_z][new_x][new_y]=tmt[now[0]][now[1]][now[2]]+1
      q.append((new_z,new_x,new_y))

check = True
ans = 0
for i in tmt:
  for j in i:
    if 0 in j:
      check = False
      break
    ans = max(ans, max(j)-1)
if check:
  print(ans)
else:
  print(-1)

  
'''
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
'''