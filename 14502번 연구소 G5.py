from sys import stdin
from collections import deque

#빈 칸 중에서 3칸을 골라 벽을 세운다
#그리고 바이러스 확산
#바이러스 확산된 범위 저장
#모든 경우 반복

dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]

def spread():
    global check, info, spread_result
    visited = [[0 for i in range(m)] for j in range(n)]
    #벽 세울 곳은 미리 방문 처리
    for i in range(len(check)):
        if check[i] == 1:
            visited[info[0][i][0]][info[0][i][1]] = 1

    q = deque()
    for i in info[2]:
        q.append(i)
        visited[i[0]][i[1]] = 1
    cnt = len(info[2])
    while q:
        temp = q.popleft()
        for i in range(4):
            nx = dx[i] + temp[0]
            ny = dy[i] + temp[1]
            if 0<=nx<n and 0<=ny<m and g[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt+=1
    spread_result = min(spread_result, cnt)

def build(p, k):
    global check
    if k == 3:
        spread()
        return
    for i in range(p, len(check)):
        if check[i] == 0:
            check[i] = 1
            build(i+1, k+1)
            check[i] = 0

n, m = map(int, stdin.readline().split())
g = [list(map(int, stdin.readline().split())) for i in range(n)]

info = {0:[], 1:[], 2:[]}
#0:빈 칸, 1:벽, 2:바이러스
for i in range(n):
    for j in range(m):
        info[g[i][j]].append((i,j))
check = [0 for i in range(len(info[0]))] #벽 세울 곳 체크
spread_result = 65
build(0, 0)


print(n*m - (len(info[1])+3) - spread_result)