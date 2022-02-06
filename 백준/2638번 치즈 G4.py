from sys import stdin
from collections import deque

#처음 탐색으로 공기 부분을 체크
#탐색을 반복하면서 녹을 치즈을 찾고 녹임
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def air(start):
    global cheese
    q = deque()
    q.append(start)
    cheese[start[0]][start[1]] = 2
    #2 : 공기
    while q:
        now = q.popleft()
        for i in range(4):
            nx = now[0]+dx[i]
            ny = now[1]+dy[i]
            if 0<=nx<n and 0<=ny<m and cheese[nx][ny] == 0:
                q.append((nx,ny))
                cheese[nx][ny] = 2
    
def findcheese():
    cheese_cnt = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                cheese_cnt+=1
    return cheese_cnt
    
def melt(cheese_cnt):
    global cheese
    melt_time = 0
    melt_cheese = 0
    
    while melt_cheese<cheese_cnt:
        melt_pos = deque()
        new_air = deque()
        for i in range(n):
            for j in range(m):
                if cheese[i][j] == 1:
                    air_cnt = 0
                    for k in range(4):
                        if cheese[i+dx[k]][j+dy[k]] == 2:
                            air_cnt+=1
                    if air_cnt > 1:
                        melt_pos.append((i,j))
                        for k in range(4):
                            if cheese[i+dx[k]][j+dy[k]] == 0:
                                new_air.append((i+dx[k],j+dy[k]))
        for pos in melt_pos:
            if cheese[pos[0]][pos[1]] == 1:
                cheese[pos[0]][pos[1]] = 2
                melt_cheese+=1
        for new in new_air:
            air(new)   
        melt_time+=1  
        
    return melt_time
    


n, m = map(int, stdin.readline().split())
cheese = [list(map(int, stdin.readline().split())) for i in range(n)]

air((0,0))
cheese_cnt = findcheese()
result = melt(cheese_cnt)
print(result)