from sys import stdin
from collections import deque

k = int(stdin.readline())
w, h = map(int, stdin.readline().split())
g = [list(map(int, stdin.readline().split())) for i in range(h)]

start = [0, 0]
end = [h-1, w-1]

q = deque()
q.append([start, k])
#원숭이의 움직임
mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]
#말의 움직임
hx = [1, 2, 2, 1, -1, -2, -2, -1]
hy = [-2, -1, 1, 2, 2, 1, -1, -2]

visited = [[[-1 for i in range(w)] for i in range(h)] for i in range(k + 1)]
def check_range(x, y):
    if 0 <= x < h and 0 <= y < w:
        return True
    return False

visited[k][0][0] = 0
result = -1
flag = False
while q:
    now = q.popleft()
    
    if now[0][0] == end[0] and now[0][1] == end[1]:
        result = visited[now[1]][now[0][0]][now[0][1]]
        break
    
    for i in range(4):
        nx = now[0][0] + mx[i]
        ny = now[0][1] + my[i]
        m = now[1]
        if check_range(nx, ny) and g[nx][ny] == 0 and visited[m][nx][ny] == -1:
            q.append([[nx,ny], m])
            visited[m][nx][ny] = visited[m][now[0][0]][now[0][1]] + 1
            if nx == end[0] and ny == end[1]:
                result = visited[m][nx][ny]
                flag = True
                break
    if flag:
        break
    if now[1] > 0:
        for i in range(8):
            nx = now[0][0] + hx[i]
            ny = now[0][1] + hy[i]
            m = now[1]
            
            if check_range(nx, ny) and g[nx][ny] == 0 and visited[m - 1][nx][ny] == -1:
                q.append([[nx,ny], m - 1])
                visited[m - 1][nx][ny] = visited[m][now[0][0]][now[0][1]] + 1
                if nx == end[0] and ny == end[1]:
                    result = visited[m - 1][nx][ny]
                    flag = True
                    break
    if flag:
        break
    
print(result)
    
'''
1
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
'''