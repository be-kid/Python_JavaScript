from sys import stdin, version_info
from collections import deque
from typing import AnyStr

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    visited = [[[0 for i in range(m)] for j in range(n)] for k in range(2)]
    q = deque()
    q.append([(0,0), 1, False])
    visited[0][0][0] = 1
    
    while q:
        now = q.popleft()
        if now[0][0]==n-1 and now[0][1]==m-1:
            return 1
        for i in range(4):
            nx = now[0][0] + dx[i]
            ny = now[0][1] + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if now[2] == False: #벽을 뚫은 적이 없다
                    if g[nx][ny] == 0 and visited[0][nx][ny] == 0: #벽도 아니고 방문한적 없다
                        q.append([(nx, ny), now[1]+1, False])
                        visited[0][nx][ny] = now[1]+1
                        if nx==n-1 and ny==m-1:
                            return visited[0][nx][ny]
                    elif g[nx][ny] == 1 and visited[1][nx][ny] == 0 and visited[0][nx][ny] == 0: #벽이고 뚫은 적이 없다
                        q.append([(nx, ny), now[1]+1, True]) #뚫기
                        visited[1][nx][ny] = now[1]+1
                else: #뚫은 적이 있다
                    if g[nx][ny] == 0 and visited[1][nx][ny] == 0 and visited[0][nx][ny] == 0: #길이고 방문한 적이 없다
                        q.append([(nx, ny), now[1]+1, True])
                        visited[1][nx][ny] = now[1]+1
                        if nx==n-1 and ny==m-1:
                            return visited[1][nx][ny]
        
    return -1




n,m = map(int, stdin.readline().split())
g = [list(map(int, list(stdin.readline().rstrip()))) for i in range(n)]

print(bfs())


'''
13 13
0100011011000
0001001010000
0000100001000
1100010101011
1111101111000
1011010001001
0100001001001
0100111010001
0101010000100
0001110100000
0000001000100
1010001000111
1001000100000

27
'''